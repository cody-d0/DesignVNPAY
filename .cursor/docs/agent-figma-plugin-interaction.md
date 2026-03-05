# Agent ↔ Figma/Plugin — Interaction Model

> **Mục đích:** Tài liệu chuẩn hóa cách agent (Cursor) tương tác với Figma và plugin — dựa trên nghiên cứu đa ngôn ngữ (EN/JA/ZH/KO/DE/ES/FR/PT/RU/IT).  
> **Scope:** Viết thiết kế elements + apply variable tokens vào Figma từ agent.

---

## 1. Hai chiều tương tác

| Chiều | Hướng | Kênh | Mô tả |
|-------|--------|------|--------|
| **Read** | Figma → Agent | **MCP** | Agent đọc design context, selection, variables, components từ Figma. Dùng để sinh spec, review, sync code. |
| **Write** | Agent → Figma | **Spec JSON + Plugin** | Agent xuất Spec JSON; Plugin nhận và tạo node + bind variable theo Phase A/B. |

Hai chiều **độc lập** — không phụ thuộc nhau, kết hợp khi cần round-trip.

---

## 2. Kênh Read: MCP (Figma → Agent)

### 2.1 Figma Desktop MCP (official)

**Cách bật:**
1. Mở Figma Desktop (bản mới nhất).
2. Mở file Design, bật Dev Mode (`Shift+D`).
3. Inspect panel → mục MCP server → "Enable desktop MCP server".
4. Server chạy tại `http://127.0.0.1:3845/mcp`.

**Cấu hình trong Cursor (mcp.json):**
```json
{
  "servers": {
    "figma-desktop": {
      "type": "http",
      "url": "http://127.0.0.1:3845/mcp"
    }
  }
}
```

**Kiểm tra:** Gõ `#get_design_context` trong Cursor chat.

**Capabilities:** Lấy design context (layout, variables, components), Code Connect mappings, screenshot, metadata. Không tạo/ghi node.

### 2.2 MCP bên thứ ba (Figma-Context, Talk To Figma)

| Server | Endpoint mẫu | Ghi chú |
|--------|-------------|--------|
| Figma-Context MCP | `http://localhost:3333/sse` | REST API + token; realtime selection. |
| Talk To Figma (Cursor) | local stdio hoặc HTTP | Đọc + ghi node qua plugin + websocket. |

**Thiết lập:**
```json
{
  "mcpServers": {
    "figma-local": {
      "command": "node",
      "args": ["path/to/mcp-server.js"],
      "env": { "FIGMA_PERSONAL_ACCESS_TOKEN": "..." }
    }
  }
}
```

### 2.3 REST API (ngoài plugin)

Dùng khi agent/script cần đọc file metadata, export asset, lấy component list ngoài plugin:
```
GET https://api.figma.com/v1/files/:fileKey
X-Figma-Token: {token}
```
Hữu ích cho: gap analysis component, export token từ Figma → DDL, lấy danh sách variables collection.

---

## 3. Kênh Write: Spec JSON + Plugin (Agent → Figma)

Có **ba cách** chuyển Spec từ agent vào Plugin, xếp theo mức độ tự động:

### Cách 1 — Chat + Paste (thủ công, linh hoạt)

```
Agent (chat) → sinh Spec JSON
     ↓
User copy → paste vào Plugin UI (textarea)
     ↓
Plugin UI: postMessage → main thread (code.ts)
     ↓
Plugin tạo node (Phase A) → place instance (Phase B)
```

**Ưu:** Không cần cấu hình; tương tác ngôn ngữ tự nhiên, sửa spec từng bước.  
**Nhược:** Thao tác tay; không tự động, khó replay.  
**Khi dùng:** Chỉnh spec nhỏ, thử ý tưởng nhanh cùng designer.

### Cách 2 — File + Load (version control, cân bằng)

```
Agent (chat hoặc terminal) → ghi spec.json ra repo
     ↓
User mở Plugin → "Load from file" → chọn file
     ↓
Plugin đọc JSON → postMessage → Phase A → Phase B
```

**Ưu:** Spec nằm trong repo, git diff/track, replay; CI có thể generate.  
**Nhược:** Vẫn cần click "Load" (không hoàn toàn tự động).  
**Khi dùng:** Pipeline DDL → spec; designer load đúng file tương ứng từ repo.

### Cách 3 — Local URL + Plugin Fetch (tự động cao nhất) ⭐ recommended

```
Agent (terminal) → ghi/cập nhật spec.json → local server serve file
     ↓                 (hoặc CI artifact URL)
Plugin UI: fetch("http://localhost:PORT/spec.json")
     ↓
Plugin UI: postMessage → main thread (code.ts)
     ↓
Phase A (create nodes + bind variable)
     ↓ (nếu có mapping componentRef)
Phase B (replace với instance + set props + variable modes)
```

**Thiết lập plugin:**
- `manifest.json`: thêm `networkAccess.allowedDomains: ["http://localhost", "http://127.0.0.1"]`.
- Plugin UI: `fetch(url)` trong iframe → nhận JSON → `parent.postMessage({ pluginMessage: spec }, '*')`.
- Plugin main: `figma.ui.on('message', msg => runPhaseA(msg.spec))`.

**Ưu:** Agent chạy script một lần (terminal/CI) → Plugin bấm "Reload" luôn lấy spec mới; dễ automation, không copy/paste, replay sạch.  
**Nhược:** Cần chạy local server (đơn giản: `npx serve`, `python -m http.server`, hoặc custom Node server).  
**Khi dùng:** Pipeline tự động, agent CI/terminal generate spec từ DDL/PRD, team load từ URL.

---

## 4. Kiến trúc plugin: main thread vs UI thread

Figma Plugin có **hai luồng bắt buộc**; hiểu đúng để đặt logic đúng chỗ:

| Luồng | File | Có thể làm | Không thể làm |
|-------|------|------------|---------------|
| **Main thread** | `code.ts` | Gọi Figma API (tạo node, bind variable, đọc file), chạy logic plugin. | Fetch network, DOM, hiển thị UI. |
| **UI thread** | `ui.html` | Fetch network (extern URL/localhost), render UI (React/HTML), nhận input user. | Gọi Figma API trực tiếp. |

**Luồng dữ liệu:**
```
UI thread (fetch URL / paste) ──postMessage──▶ Main thread (createFrame, setBoundVariable…)
Main thread ──figma.ui.postMessage──▶ UI thread (kết quả, trạng thái)
```

Quy tắc: **Spec JSON đi vào qua UI thread** (fetch hoặc textarea), **Plugin API (tạo node, bind) chạy trong main thread**.

---

## 5. Phase A → B trong plugin

Khi plugin nhận spec (từ cách 1/2/3), chạy tuần tự:

**Phase A — Create from spec:**
```typescript
// main (code.ts)
for (const el of spec.elements) {
  const node = el.type === 'frame' ? figma.createFrame() : figma.createRectangle();
  node.x = el.rect.x; node.y = el.rect.y;
  node.resize(el.rect.width, el.rect.height);
  if (el.cornerRadius) node.cornerRadius = el.cornerRadius;
  if (el.fills) node.fills = el.fills;  // fallback fills
  nodeMap[el.key] = node;
  figma.currentPage.appendChild(node);
}

for (const binding of spec.bindings) {
  const node = nodeMap[binding.nodeKey];
  const variable = binding.variableId
    ? await figma.variables.getVariableByIdAsync(binding.variableId)
    : (await figma.variables.getLocalVariablesAsync()).find(v => v.name === binding.variableName);

  if (binding.field === 'fills' || binding.field === 'strokes') {
    // bind paint
    const paint = figma.variables.setBoundVariableForPaint(node.fills[0], 'color', variable);
    node.fills = [paint];
  } else {
    // bind layout (VariableBindableNodeField)
    node.setBoundVariable(binding.field, variable.id);
  }
}
```

**Phase B — Place instances (optional, nếu spec có `componentRef`):**
```typescript
for (const [key, node] of Object.entries(nodeMap)) {
  const el = spec.elements.find(e => e.key === key);
  if (!el.componentRef) continue;
  const component = figma.root.findOne(n => n.type === 'COMPONENT' && n.name === el.componentRef);
  if (!component) continue;  // giữ node từ Phase A

  const instance = (component as ComponentNode).createInstance();
  instance.x = node.x; instance.y = node.y;
  instance.resize(node.width, node.height);
  // set props/variants nếu el.props có
  // bind variables theo el.variableModes nếu có
  node.parent?.insertChild(node.parent.children.indexOf(node), instance);
  node.remove();
}
```

---

## 6. Mô hình tổng thể (round-trip)

```
DDL (mode-*.json, block-catalog)
       │
       ▼ [agent script / terminal]
    spec.json ──────────────────────────────────────────────────────┐
       │                                                            │
  [Cách 1] paste  [Cách 2] Load file  [Cách 3] fetch(localhost)    │
       │               │                      │                    │
       └───────────────┴──────────────────────┘                    │
                       ▼                                            │
                Plugin UI thread                                    │
                (postMessage)                                       │
                       ▼                                            │
                Plugin Main thread                                  │
                Phase A: create nodes + bind variable               │
                Phase B: place instances + set props                │
                       ▼                                            │
               Figma Canvas (nodes + variables bound)               │
                       │                                            │
          [MCP Figma Desktop / Figma-Context MCP] ─────────────────┘
                       ▼
          Agent (Cursor chat) — đọc lại: get_design_context
          → review, refine spec → loop
```

---

## 7. Bảng quyết định: chọn cách tương tác

| Tình huống | Cách chọn |
|------------|-----------|
| Làm việc trực tiếp, chỉnh spec nhanh trong chat | **Cách 1** (paste) |
| Spec nằm trong repo, nhiều người dùng, cần version | **Cách 2** (load file) |
| Automation, CI generate spec từ DDL/PRD | **Cách 3** (local URL) |
| Agent cần đọc thiết kế hiện có trong Figma | **MCP** (read-only) |
| Agent cần ghi + đọc lại (round-trip) | **Cách 3** + **MCP** kết hợp |

---

## 8. Cấu trúc Spec JSON (tóm tắt)

```jsonc
{
  "elements": [
    {
      "key": "card-bg",           // id dùng trong bindings
      "type": "rectangle",        // "frame" | "rectangle" | "text"
      "rect": { "x": 0, "y": 0, "width": 320, "height": 200 },
      "cornerRadius": 8,
      "fills": [{ "type": "SOLID", "color": { "r": 1, "g": 1, "b": 1 } }],
      "componentRef": "Card"      // (Phase B) tên component để thay instance
    }
  ],
  "bindings": [
    { "nodeKey": "card-bg", "variableName": "background", "field": "fills" },
    { "nodeKey": "card-bg", "variableName": "spacing.4",  "field": "paddingLeft" }
  ]
}
```

**field whitelist:**
- **Paint:** `"fills"` | `"strokes"` → `setBoundVariableForPaint(paint, 'color', variable)` + gán lại.
- **Layout (VariableBindableNodeField):** `width`, `height`, `x`, `y`, `paddingLeft`, `paddingRight`, `paddingTop`, `paddingBottom`, `itemSpacing`, `topLeftRadius`, `topRightRadius`, `bottomLeftRadius`, `bottomRightRadius`, `minWidth`, `maxWidth`, `minHeight`, `maxHeight`, `counterAxisSpacing`, `strokeWeight`, `opacity`, `gridRowGap`, `gridColumnGap`, `characters`, `visible`.

---

## 9. Tài liệu liên quan

| File | Nội dung |
|------|---------|
| [shadcn-cli-ddl-figma-plugin-insight.md](shadcn-cli-ddl-figma-plugin-insight.md) | shadcn CLI value, Spec JSON chi tiết (§5), Insights EN/JA/ZH (§6), Phase A/B (§7). |
| [ddl/views-and-outputs.md](ddl/views-and-outputs.md) | token_view, component_view, use case "Figma import token". |
| [ddl/hierarchy.md](ddl/hierarchy.md) | GLOBAL/PRODUCT, resolution order token. |
| [design-data-layer/global/pro-blocks/README-DDL-VALUES.md](../../design-data-layer/global/pro-blocks/README-DDL-VALUES.md) | Tailwind class ↔ DDL token; build-time apply. |

---

## Quick reference

```
READ  Figma → Agent : MCP (http://127.0.0.1:3845/mcp hoặc Figma-Context)
WRITE Agent → Figma : spec.json → Plugin (paste / load file / fetch localhost)
EXEC  Plugin         : Phase A (create + bind) → Phase B (instance + props)
```
