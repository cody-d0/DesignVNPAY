# shadcn CLI ↔ DDL ↔ Figma Plugin — Insight

> **Bài toán:** Vẽ design elements và apply variable tokens vào props.  
> **Mục đích:** Giữ insight ngắn gọn; hỗ trợ agent Cursor xây dựng plugin Figma.

---

## 1. Bài toán tóm tắt

| Khái niệm | Ý nghĩa |
|-----------|---------|
| **Vẽ design elements** | Tạo/sync nodes trong Figma: components, variants, frames (tương ứng primitive/pattern trong DDL). |
| **Apply variable tokens vào props** | Gán token (color, spacing, typography) vào "props" của element — trong Figma là Variables/Styles hoặc component properties; trong code là CSS variables / Tailwind semantic classes. |

DDL đã có: `mode-light.json` / `mode-dark.json` (base.*, spacing, text.*), `block-catalog.json` (shadcn_deps, tokens_used). Thiếu: **contract rõ ràng giữa Figma ↔ code** và **nguồn canonical cho danh sách components + tên token**.

---

## 2. Giá trị dữ liệu từ shadcn CLI (theo [docs](https://ui.shadcn.com/docs/cli))

### 2.1 Registry: `view` / `search` / `list`

| Dữ liệu | Value cho bài toán |
|---------|--------------------|
| **Danh sách component** | Canonical list design elements (Button, Input, Dialog, Card, …). Plugin Figma: tạo/sync component set hoặc mapping type → Figma component. |
| **Metadata từ `view [item]`** | Tên, variants, dependencies. Dùng để: vẽ đúng cấu trúc (props/variants), đồng bộ với `block-catalog.shadcn_deps`. |
| **Search/List** | Gap analysis: so sánh DDL component_registry / block-catalog với registry → thiếu component nào, cần block nào. |

→ **Design elements** = registry components + (tùy chọn) block-catalog blocks; **props** gồm variant props của shadcn + token assignment.

### 2.2 Theming: `init` — CSS variables

| Dữ liệu | Value cho bài toán |
|---------|--------------------|
| **`--css-variables`** (default: true) | shadcn dùng CSS variables cho theme: `--background`, `--foreground`, `--muted`, `--border`, `--primary`, … |
| **`-b, --base-color`** | neutral, gray, zinc, stone, slate — không đổi tên semantic, chỉ đổi giá trị. |

→ **Variable tokens** cần map 1:1 với tên này để code gen đúng. DDL `base.*` (mode-light/mode-dark) trùng semantic với shadcn:

- `base.background` → `--background`
- `base.foreground` → `--foreground`
- `base.muted`, `base.border`, `base.primary`, …

→ Plugin Figma: Figma Variables (hoặc Styles) nên dùng **cùng tên semantic** (background, foreground, muted, border, primary, …) để export/import token ↔ DDL ↔ code không lệch.

### 2.3 Cấu trúc project: `add` / `components.json`

| Dữ liệu | Value cho bài toán |
|---------|--------------------|
| **`-p, --path`** | Nơi component được ghi (vd `@/components/ui`). |
| **`--src-dir` / `--no-src-dir`** | Cấu trúc file output. |
| **components.json** | Chuẩn cấu hình: `components`, `aliases`, `style`, `tailwind`, `tsx`. |

→ Dùng khi plugin hoặc agent **emit code** từ Figma: biết path và convention (src-dir, alias `@/`) để sinh đúng import và file.

### 2.4 Custom registry: `build`

| Dữ liệu | Value cho bài toán |
|---------|--------------------|
| **`registry.json` → build → JSON trong `public/r`** | Nếu DDL/pro-blocks được publish thành registry: mỗi item có dependencies (shadcn) + metadata. |

→ Design elements có thể là **block** (pattern) thay vì chỉ primitive; mỗi block có `shadcn_deps` + `tokens_used` → plugin có thể vẽ "block" = composition và gán tokens vào props của từng phần.

### 2.5 Migrate (rtl, radix, icons)

| Dữ liệu | Value cho bài toán |
|---------|--------------------|
| **RTL / radix / icons** | Biết component có hỗ trợ RTL, dùng radix-ui, icon lib nào. |

→ Hữu ích cho **spec** (state_view, component_view): ghi chú variant hoặc constraint khi vẽ/sync Figma (vd RTL layout, icon slot).

---

## 3. Luồng dữ liệu gợi ý

```
┌─────────────────┐     ┌──────────────────────┐     ┌─────────────────┐
│ shadcn Registry │────▶│ DDL                  │────▶│ Figma           │
│ (view/search/   │     │ - block-catalog       │     │ - Variables     │
│  list)          │     │   (shadcn_deps,       │     │   (semantic     │
│                 │     │    tokens_used)      │     │    names = base.*)
│ components.json │     │ - mode-light/dark     │     │ - Components    │
│ (css-variables, │     │   (base.*, spacing,  │     │   (map shadcn   │
│  path)          │     │    text.*)           │     │    + blocks)     │
└─────────────────┘     └──────────────────────┘     │ - Props =       │
                                                     │   variants +    │
                                                     │   token refs     │
                                                     └─────────────────┘
```

- **Design elements:** Registry (+ block-catalog) → Figma components / component sets.
- **Variable tokens:** DDL mode-*.json (base.*, spacing, text.*) ↔ Figma Variables (cùng tên semantic) ↔ code CSS variables (shadcn init).

---

## 4. Hỗ trợ Agent Cursor xây dựng Figma Plugin

### 4.1 Inputs agent nên đọc

| Nguồn | Mục đích |
|-------|----------|
| **shadcn CLI docs** ([ui.shadcn.com/docs/cli](https://ui.shadcn.com/docs/cli)) | Convention: tên CSS variables, components.json, registry (view/search/list/build). |
| **DDL** | `design-data-layer/global/mode-light.json` (và mode-dark), `design-data-layer/global/pro-blocks/block-catalog.json` (shadcn_deps, tokens_used). |
| **Figma API** | Variables (VariableCollections, VariableAlias), Component properties, ComponentSet. |

### 4.2 Việc plugin có thể làm (gợi ý)

1. **Sync tokens:** Đọc DDL `mode-*.json` → resolve references → tạo/cập nhật Figma Variables (semantic names: background, foreground, muted, border, primary, …) và gán vào Styles nếu cần.
2. **Sync design elements:** Đọc registry (qua `shadcn view` hoặc registry JSON) + block-catalog → tạo/sync Figma components với props/variants tương ứng; gắn token (variable ref) vào fill/typography/spacing của từng variant.
3. **Export từ Figma → DDL/code:** Đọc Figma Variables + component tree → xuất token JSON (mode-* format) và/hoặc gợi ý Tailwind/shadcn code (dùng mapping DDL ↔ Tailwind class trong README-DDL-VALUES.md).

### 4.3 Contract cần giữ ổn định

- **Tên token semantic:** DDL `base.*` = shadcn `--*` = Figma variable name (background, foreground, muted, border, primary, primary-foreground, …).
- **Component id:** block-catalog `id` + shadcn component name → Figma component name hoặc mapping table (như `figma-wireframe-generation.yaml` component_mapping).

### 4.4 Tài liệu liên quan trong repo

- [.cursor/docs/ddl/views-and-outputs.md](ddl/views-and-outputs.md) — token_view, component_view, use case "Figma import token".
- [.cursor/docs/ddl/hierarchy.md](ddl/hierarchy.md) — GLOBAL/PRODUCT, resolution order.
- [design-data-layer/global/pro-blocks/README-DDL-VALUES.md](../../design-data-layer/global/pro-blocks/README-DDL-VALUES.md) — Tailwind class ↔ DDL token; build-time/runtime apply.
- [MarkdownSV/design/wireframes/figma-wireframe-generation.yaml](../../MarkdownSV/design/wireframes/figma-wireframe-generation.yaml) — Ví dụ global_tokens + component_mapping cho Figma automation.

---

## 5. Contract Agent ↔ Plugin (Spec JSON + Figma API)

### 5.1 Đánh giá spec

| Khía cạnh | Đánh giá | Ghi chú |
|-----------|----------|---------|
| **Tách elements vs bindings** | ✅ Hợp lý | Elements mô tả hình học/look; bindings mô tả gắn token (variable) vào node — đúng với Figma (node trước, bind sau). |
| **elements: type, rect, cornerRadius, fills/strokes** | ✅ Đủ cho primitive | Map trực tiếp sang `createFrame`/`createRectangle`; fills/strokes dùng làm giá trị khởi tạo, sau đó plugin thay bằng variable ref khi có binding. |
| **bindings: nodeKey/idx + variableId hoặc variableName + field** | ✅ Linh hoạt | Cho phép agent dùng id (ổn định) hoặc name (dễ sinh từ DDL); plugin resolve name → id qua `getLocalVariablesAsync()` nếu cần. |
| **field = VariableBindableNodeField hoặc "fills"/"strokes"** | ✅ Đúng API | Layout (width, height, x, y, paddingLeft, …) → `setBoundVariable`; paint → `setBoundVariableForPaint` rồi gán lại fills/strokes. |
| **Plugin: getVariableByIdAsync / getLocalVariablesAsync** | ✅ Đúng | Variables phải có sẵn trong file (sync từ DDL hoặc tạo trước); plugin chỉ đọc và bind. |
| **Plugin: createFrame / createRectangle hoặc createNodeFromJSXAsync** | ✅ Đủ lựa chọn | Frame/Rectangle cho spec đơn giản; JSX cho cấu trúc phức tạp (component tree). |
| **Bind layout → setBoundVariable; bind màu → setBoundVariableForPaint + gán lại fills/strokes** | ✅ Đúng thứ tự | Figma: bind variable trước, sau đó set paint/layout để tham chiếu variable (alias). |

**Rủi ro / cần lưu ý:**

- **variableName → id:** Nếu spec dùng `variableName`, plugin cần resolve bằng `getLocalVariablesAsync()` và match tên (hoặc quy ước collection + name); trùng tên trong nhiều collection cần quy định rõ.
- **Thứ tự tạo node:** Tạo node → bind layout (setBoundVariable) → bind paint (setBoundVariableForPaint, rồi node.fills = … / node.strokes = …). Không bind trước khi node tồn tại.
- **fills/strokes sau bind:** Sau `setBoundVariableForPaint` phải gán lại `fills`/`strokes` với paint dạng `{ type: 'VARIABLE_ALIAS', variableId }` (hoặc tương đương) thì node mới hiển thị đúng theo variable.

---

### 5.2 Spec JSON từ Agent

**(1) elements** — Mảng mô tả từng node cần tạo:

| Thuộc tính | Kiểu | Mô tả |
|------------|------|--------|
| `type` | string | Loại node: `"frame"` \| `"rectangle"` \| (mở rộng: `"text"`, `"component"`, …). |
| `rect` | `{ x, y, width, height }` | Layout (px). Plugin có thể dùng cho `x`, `y`, `resize(width, height)` hoặc bind qua variable. |
| `cornerRadius` | number (hoặc array 4 số) | Góc bo. |
| `fills` | array (paint) | Fill khởi tạo; nếu có binding cho `"fills"` thì sẽ bị thay bằng variable alias. |
| `strokes` | array (paint) | Stroke khởi tạo; nếu có binding cho `"strokes"` thì tương tự. |
| `key` \| `idx` | string \| number | Định danh node cho bindings tham chiếu (nodeKey/idx). |

**(2) bindings** — Mảng gắn variable vào thuộc tính node:

| Thuộc tính | Kiểu | Mô tả |
|------------|------|--------|
| `nodeKey` hoặc `idx` | string \| number | Trỏ tới element (key hoặc index trong mảng elements). |
| `variableId` | string | Figma variable id (ưu tiên nếu có). |
| `variableName` | string | Tên variable (semantic, trùng DDL/shadcn); plugin resolve bằng `getLocalVariablesAsync()` nếu không có `variableId`. |
| `field` | string | `VariableBindableNodeField` (layout: `"width"`, `"height"`, `"x"`, `"y"`, `"paddingLeft"`, …) **hoặc** `"fills"` \| `"strokes"` (paint). Plugin map `"fills"`/`"strokes"` sang `setBoundVariableForPaint` rồi gán lại `fills`/`strokes`. |

Ví dụ spec tối thiểu:

```json
{
  "elements": [
    { "key": "card-bg", "type": "rectangle", "rect": { "x": 0, "y": 0, "width": 320, "height": 200 }, "cornerRadius": 8, "fills": [{ "type": "SOLID", "color": { "r": 1, "g": 1, "b": 1 } }] }
  ],
  "bindings": [
    { "nodeKey": "card-bg", "variableName": "background", "field": "fills" },
    { "nodeKey": "card-bg", "variableId": "VAR_ID_PADDING", "field": "paddingLeft" }
  ]
}
```

---

### 5.3 Plugin: luồng xử lý (Figma API)

1. **Lấy variable:** `figma.variables.getVariableByIdAsync(id)` nếu spec có `variableId`; nếu chỉ có `variableName` thì `figma.variables.getLocalVariablesAsync()` rồi tìm theo `variable.name`.
2. **Tạo node:** Với từng entry trong `elements`: `figma.createFrame()` hoặc `figma.createRectangle()` (hoặc `figma.createNodeFromJSXAsync()` nếu dùng JSX); set `x`, `y`, `resize(width, height)`, `cornerRadius`, `fills`, `strokes` từ spec.
3. **Bind layout:** Với binding có `field` ∈ VariableBindableNodeField (vd `width`, `height`, `x`, `y`, `paddingLeft`, …): gọi `node.setBoundVariable(field, variableId)`.
4. **Bind màu (paint):** Với binding có `field` = `"fills"` hoặc `"strokes"`: gọi `node.setBoundVariableForPaint(paintIndex, variableId)` (thường index 0), sau đó gán lại `node.fills` / `node.strokes` với paint có `type: 'VARIABLE_ALIAS'` và `variableId` tương ứng để node hiển thị đúng theo variable.

Lưu ý: Variables (semantic names từ DDL) phải đã tồn tại trong file — plugin sync từ DDL (mode-*.json) sang Figma Variables trước, hoặc dùng file đã có sẵn collection.

---

### 5.4 Tóm tắt contract

- **Agent output:** Một Spec JSON gồm `elements` (type, rect, cornerRadius, fills/strokes, key hoặc idx) và `bindings` (nodeKey/idx, variableId hoặc variableName, field).
- **Plugin input:** Spec JSON + (variables đã có trong file).
- **Plugin output:** Cây node trong Figma; layout và paint được gắn với Variable qua `setBoundVariable` (layout) và `setBoundVariableForPaint` + gán lại fills/strokes (màu).

---

## 6. Insights từ tìm kiếm sâu (EN / JA / ZH) — Đánh giá và bổ sung

Các nguồn dưới bổ sung chi tiết API và góc nhìn đa ngôn ngữ cho bài toán: vẽ elements + apply variables. Đánh giá ngắn và gợi ý tích hợp vào spec/plugin.

### 6.1 Tạo node hàng loạt: `createNodeFromJSXAsync` (EN)

| Nội dung | Đánh giá | Bổ sung vào tài liệu |
|----------|----------|----------------------|
| Tạo cây node từ JSX (Widget API), trả về `Promise<SceneNode>`; sau khi tạo có thể gọi `setBoundVariable` trên node trả về. | ✅ Hữu ích | Chuẩn hóa luồng: (A) JSON → createFrame/createRectangle thủ công, hoặc (B) JSON → JSX → `createNodeFromJSXAsync` → loop bind variable. |
| Cần: `@figma/widget-typings`, tsconfig `jsx: "react"`, `jsxFactory: "figma.widget.h"`, file `.tsx`. | ✅ Cần ghi | Plugin chọn (B) thì cần typings và build step cho JSX. |
| Hạn chế: không cover mọi thuộc tính (style IDs, instance); có thể set thêm property trực tiếp lên node sau khi tạo. | ✅ Quan trọng | Spec/agent không nên dựa vào JSX cho style IDs hoặc instance swap; bước post-process set property sau khi tạo. |

→ **Gợi ý:** Agent sinh Spec JSON; plugin (A) map JSON → createFrame/createRectangle từng node, hoặc (B) map JSON → JSX rồi `createNodeFromJSXAsync` — sau đó trong mọi trường hợp loop bind variable theo §5.3.

### 6.2 Bind variable: hai API khác nhau (EN)

| Nội dung | Đánh giá | Bổ sung vào tài liệu |
|----------|----------|----------------------|
| **VariableBindableNodeField** (dùng với `setBoundVariable`): không có fills/strokes. | ✅ Quan trọng | Spec `field` cho layout/paint phải tách rõ: layout → setBoundVariable; paint → setBoundVariableForPaint. |
| Danh sách field bindable (layout): height, width, characters, itemSpacing, paddingLeft/Right/Top/Bottom, visible, topLeftRadius…, minWidth, maxWidth, minHeight, maxHeight, counterAxisSpacing, strokeWeight (và từng cạnh), opacity, gridRowGap, gridColumnGap. | ✅ Bổ sung | Dùng làm whitelist cho spec `field` khi không phải "fills"/"strokes". |
| Màu (fill/stroke): `figma.variables.setBoundVariableForPaint(paint, 'color', variable)` trả về paint mới; gán lại `node.fills` / `node.strokes`. | ✅ Đúng API | Plugin: gọi setBoundVariableForPaint với paint hiện có và variable → nhận paint mới (alias) → gán lại mảng fills/strokes. |

**Danh sách VariableBindableNodeField (để spec agent dùng):**  
`height`, `width`, `x`, `y`, `characters`, `itemSpacing`, `paddingLeft`, `paddingRight`, `paddingTop`, `paddingBottom`, `visible`, `topLeftRadius`, `topRightRadius`, `bottomLeftRadius`, `bottomRightRadius`, `minWidth`, `maxWidth`, `minHeight`, `maxHeight`, `counterAxisSpacing`, `strokeWeight`, `opacity`, `gridRowGap`, `gridColumnGap` (và các strokeWeight theo cạnh nếu API hỗ trợ). **Không** có `fills` hay `strokes` — những thứ đó dùng `setBoundVariableForPaint`.

### 6.3 JSON → Figma hiện có (EN)

| Công cụ / nguồn | Mô tả ngắn | Đánh giá |
|------------------|------------|----------|
| JSON to Figma (Pavel Laptev) | Populate layer có sẵn bằng data JSON (text, image URL); match key với tên layer. | Không tạo node từ spec, không bind variable. GitHub archived; bản trả phí trên Community. |
| JSON to Figma Import | Tạo component từ JSON export (REST/fig-to-json). | Không thấy tài liệu bind variable. |

→ **Kết luận:** Chưa có plugin sẵn “JSON spec → tạo node mới + bind variable”; cần tự build hoặc mở rộng (spec §5.2 + luồng §5.3).

### 6.4 Tiếng Nhật (JA) — Variables, modes, alias

| Nội dung | Đánh giá | Bổ sung |
|----------|----------|---------|
| Goodpatch Tech: `getLocalVariableCollectionsAsync()`, `getLocalVariablesAsync()`; collection có **modes** (modeId, name), variable có **valuesByMode**. | ✅ Hữu ích | DDL mode-light/mode-dark map 1:1 với Figma modes (modeId hoặc name); sync token cần set value per mode. |
| Đặt alias: `variable.setValueForMode(modeId, { id: sourceVariableId, type: "VARIABLE_ALIAS" })`. | ✅ Kỹ thuật | Khi sync DDL → Figma: variable semantic (background, foreground…) có thể alias tới variable nguồn theo từng mode (light/dark). |
| Plugin “node-type UI”: React Flow + Vite + shadcn để chỉnh alias giữa các nhóm màu. | ✅ Tham khảo | Kiến trúc UI plugin (iframe) có thể dùng stack tương tự. |
| debiru/localvariablesmanipulator: Export/Import Local Variables. | ✅ Công cụ | Dùng để round-trip variables (export → chỉnh → import); không thay thế “tạo node + bind”. |
| Design Tokens Community Group: plugin xuất variables ra format DTCG. | ✅ Chuẩn | Xuất Figma Variables → DTCG; có thể kết nối với DDL/token pipeline. |

### 6.5 Tiếng Trung (ZH) — Kiến trúc plugin, tạo node

| Nội dung | Đánh giá | Bổ sung |
|----------|----------|---------|
| Hai luồng: **main** (code.ts) — gọi Figma API; **UI** (ui.html) — iframe, postMessage. Tạo node trong main. | ✅ Chuẩn | Plugin: main thread tạo node (createRectangle, resize, fills = [...], appendChild); UI chỉ gửi lệnh/spec qua postMessage. |
| Ví dụ: `figma.createRectangle()`, `resize()`, `fills = [...]`, `figma.currentPage.appendChild(rect)`. | ✅ Khớp §5.3 | Xác nhận luồng “tạo node → set property → append” đúng; thêm bước bind variable sau khi tạo. |
| Styles to Variables / Variables Import Export: style → variable, import/export variable. | ✅ Design system | Hữu ích cho sync token (style ↔ variable); không thay thế “tạo element từ spec + bind”. |

### 6.6 Công cụ token / layer (EN)

| Công cụ | Mô tả | Đánh giá |
|---------|--------|----------|
| Tokens Studio for Figma | Quản lý tokens, sync với Variables. | Không tạo node từ JSON spec. |
| jsonToLayers | Gán data JSON lên text layer có sẵn. | Không tạo node mới, không bind variable. |
| TokensBrücke, Storyblok design-tokens-figma-plugin | Figma variables → JSON (export). | Chiều export; không có “JSON spec → nodes + bind”. |

→ **Kết luận:** Các công cụ hiện có phục vụ token/variable management và export; **không** giải bài “JSON spec → tạo node mới + bind variable”. Plugin theo spec §5 cần implement từ đầu hoặc kết hợp: dùng Tokens Studio / Variables Import Export để có sẵn Variables trong file, rồi plugin đọc spec và thực hiện create node + bind.

### 6.7 Tóm tắt đánh giá và hành động

- **createNodeFromJSXAsync:** Lựa chọn (B) khi cần cây node phức tạp; cần typings + JSX build; sau tạo vẫn loop bind variable. Spec JSON giữ nguyên (elements + bindings).
- **Hai API bind:** Layout → `setBoundVariable(field, variableId)` với field ∈ VariableBindableNodeField; paint → `setBoundVariableForPaint(paint, 'color', variable)` rồi gán lại fills/strokes. Spec `field` dùng whitelist layout hoặc `"fills"`/`"strokes"`.
- **JSON → Figma hiện có:** Không cover “spec → node mới + bind”; cần tự build.
- **JA/ZH:** Modes/valuesByMode và setValueForMode(alias) cho sync DDL mode-light/dark; kiến trúc main vs UI (postMessage) chuẩn; Variables Import Export / DTCG dùng cho token round-trip.
- **Token tools:** Hỗ trợ variable/token management và export; không thay thế create node + bind — dùng kết hợp (variables có sẵn + plugin đọc spec).

---

## 7. Tạo từ spec vs đặt instance: A, B, hay tuần tự A → B?

### 7.1 Hai cách

| Cách | Mô tả | Ưu | Nhược |
|------|--------|-----|--------|
| **(A) Tạo từ spec thuần** | Frame + rectangle + text + bind variable; không dùng component có sẵn. | Không phụ thuộc component library; spec → node 1:1; chạy được mọi file; mọi element đều có mặt. | Không tự động theo design system; nhiều node; không cập nhật khi library đổi. |
| **(B) Đặt instance component có sẵn** | Đặt instance (Button, Card…) rồi set props + variable modes. | Nhất quán design system; ít node; cập nhật theo component gốc. | Cần library trong file; spec phải map type → component + props; không có component thì không vẽ được. |

### 7.2 Cách hiệu quả nhất: tuần tự A → B

Cách hiệu quả nhất **không phải** chọn A *hoặc* B, mà **tuần tự A rồi B**: làm (A) trước để có đủ structure và bindings, sau đó (B) nâng cấp lên instance ở chỗ có component tương ứng.

**Lý do:**

1. **Luôn có kết quả:** Phase A đảm bảo mọi element trong spec đều thành node và bind variable; không bị thiếu vì “chưa có component”.
2. **Nâng cấp có điều kiện:** Phase B chạy trên cây đã có: với từng node (hoặc nhóm node), nếu có mapping spec type → component (vd từ block-catalog / shadcn_deps), thì *thay* bằng instance, set props và variable modes; nếu không có mapping thì giữ nguyên node từ A.
3. **Fallback rõ ràng:** File không có component library → chỉ A vẫn dùng được; có library → B tăng chất lượng design system mà không làm mất element nào.
4. **Traceability:** A cho biết spec → node; B cho biết node nào đã “upgrade” thành component nào → dùng cho gap analysis (type nào chưa có component trong library).

### 7.3 Luồng gợi ý trong plugin

1. **Phase A (create from spec):** Với Spec JSON (elements + bindings): tạo node (frame/rectangle/text) theo §5.3, bind layout và paint (setBoundVariable, setBoundVariableForPaint + gán lại fills/strokes). Lưu mapping `nodeKey/idx` → `SceneNode` (và nếu có, `element.type`).
2. **Phase B (optional — place instances):** Đầu vào: mapping `spec type` → `Figma Component` (vd từ block-catalog + component library trong file). Duyệt nodes từ A: nếu `element.type` (hoặc role/label trong spec) khớp với một component, tạo instance từ component đó, copy layout (x, y, width, height) và bind variable tương ứng, set props/variants theo spec; có thể *thay* node cũ bằng instance hoặc chèn instance và ẩn/xóa node cũ. Nếu không khớp → giữ node từ A.

Spec có thể mở rộng: phần tử có thêm `componentRef` (vd `"Button"`, `"Card"`) để Phase B biết nên thay bằng instance nào; nếu không có `componentRef` thì chỉ A.

### 7.4 Tóm tắt

- **A alone:** Đủ khi không có component library hoặc cần output thuần spec.
- **B alone:** Rủi ro thiếu element khi spec có type chưa có component.
- **A → B (tuần tự):** Hiệu quả nhất: A đảm bảo đủ structure + bind; B nâng cấp lên instance + props + variable modes ở chỗ có mapping; không mất element, vẫn tận dụng design system khi có.

---

## Quick reference cho Agent (Figma plugin)

- **Vẽ elements:** `shadcn search/list @shadcn` + `block-catalog.json` (shadcn_deps, tokens_used) → Figma components/variants.
- **Tokens → props:** DDL `mode-light.json` / `mode-dark.json` → Figma Variables (tên semantic = base.* bỏ prefix: background, foreground, muted, border, primary…) → bind vào fill/type/spacing của component.
- **Một nguồn sự thật:** Tên token thống nhất DDL ↔ shadcn CSS vars ↔ Figma Variables để round-trip không lệch.
- **Agent → Plugin:** Emit Spec JSON (elements + bindings); Plugin tạo node (createFrame/createRectangle), lấy variable (getVariableByIdAsync / getLocalVariablesAsync), bind layout (setBoundVariable), bind màu (setBoundVariableForPaint + gán lại fills/strokes). Chi tiết §5.
- **Insights sâu (EN/JA/ZH):** createNodeFromJSXAsync (JSX path); VariableBindableNodeField whitelist vs setBoundVariableForPaint(paint,'color',variable); chưa có plugin “spec → node + bind” sẵn; modes/valuesByMode cho DDL light-dark. §6.
- **Tạo từ spec vs instance:** Hiệu quả nhất là tuần tự A → B: (A) tạo từ spec thuần (frame/rect/text + bind variable), rồi (B) thay bằng instance component + set props + variable modes ở chỗ có mapping. §7.
