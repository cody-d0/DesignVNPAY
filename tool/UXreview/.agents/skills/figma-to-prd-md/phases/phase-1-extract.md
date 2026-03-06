# Phase 1: Figma MCP Extract

**Tham chiếu:** `conventions.md` (Image Path Convention) — load trước khi thực hiện bước 1d.

## Mục tiêu

Trích xuất toàn bộ raw data từ Figma thông qua MCP.

## Bước thực hiện

**1a. Parse URL**
- Extract `file_key` và `node_id` từ `figma_url`
- Nếu URL format: `https://figma.com/design/:fileKey/:fileName?node-id=1-2` → fileKey = `:fileKey`, nodeId = `1:2`

**1b. Get metadata (page-level scan)**
- Gọi `get_metadata(fileKey, nodeId)` → scan tất cả frames/sections
- Nhận diện top-level frames = screens
- Lọc: chỉ giữ frames có kích thước viewport-like (width 320-428px cho mobile, hoặc > 800px cho desktop)

**1c. Get design context (per screen)**
- Với mỗi top-level frame: gọi `get_design_context(fileKey, nodeId)`
- Thu thập: component instances, text nodes, auto-layout properties, style properties

**1d. Get screenshots (per screen + per sub-frame) — tải về và lưu file**

Screenshot PHẢI được tải về local — file .md PRD cần ảnh wireframe. Dùng tool **`figma_save_section_screenshots`** (MCP server `figma-save`) với fallback terminal script. Tool **chỉ lưu từng artboard** (không có ảnh toàn section); thư mục `{output_base_dir}/{file_name}/{page}/{section}/` chứa các `{artboard}.png`. Sau đó post-step chuyển ảnh vào **folder `ui`** trong section (xem bước 3). Với `flat`: tạo `{output_dir}/screenshots/` nếu cần.

**Ràng buộc thực thi:** Nếu MCP `figma_save_section_screenshots` (server `figma-save`) **không có trong danh sách MCP enabled** hoặc gọi MCP thất bại, agent **BẮT BUỘC** phải chạy ngay **fallback terminal** (bước 5) — không chỉ ghi trong tài liệu hoặc bỏ qua. Pipeline không được kết thúc Phase 1 mà không thử lưu ảnh qua fallback khi MCP không khả dụng.

**1d-i. Screenshot theo section (chỉ từng artboard):**

Với mỗi **section** hoặc screen (top-level frame coi như section):

1. Gọi `get_screenshot(fileKey, sectionNodeId)` → preview trong chat (tùy chọn).

2. Thử gọi MCP tool **`figma_save_section_screenshots(fileKey, sectionNodeId, output_base_dir)`** (nếu server `figma-save` có trong project). Kết quả khi thành công:
   - Thư mục: `{output_dir}/{Figma file name}/{Figma page}/{section name}/`
   - File: **chỉ từng artboard** `{artboard-1}.png`, `{artboard-2}.png`, ... (không có ảnh toàn section).

3. **Post-step — tách ảnh vào folder `ui`:** Sau khi lưu xong (bằng MCP hoặc fallback), tạo folder `ui` trong section và chuyển toàn bộ file `.png` vào đó:
   - `mkdir -p "{output_dir}/{file_name}/{page}/{section}/ui"`
   - Di chuyển mọi `*.png` từ `{output_dir}/{file_name}/{page}/{section}/` vào `{output_dir}/{file_name}/{page}/{section}/ui/` (vd: `mv .../section/*.png .../section/ui/`).
   - Kết quả: ảnh nằm tại `{section}/ui/{artboard}.png`. Dùng path này cho `screenshot_path` (absolute) và `screenshot_relative` (path từ workspace root: `{output_dir}/{file_name}/{page}/{section}/ui/{filename}.png`).

4. **Xử lý kết quả — failure branching (bắt buộc):**

| Kết quả | Hành động |
|---------|-----------|
| **Thành công** | Sau post-step (move vào `ui/`), ghi `screenshot_path` (absolute tới file trong `ui/`) + `screenshot_relative` (path từ workspace root tới `.../section/ui/{filename}.png`) vào figma_raw. Tiếp tục. |
| **MCP tool không tìm thấy / không khả dụng** | **Thực thi ngay** fallback terminal (bước 5). Không bỏ qua. |
| **API error 403 (token sai/hết hạn)** | Ghi warning: "Figma token invalid — kiểm tra FAT/FIGMA_ACCESS_TOKEN". `screenshot_path = null`. KHÔNG fallback (token sai thì terminal cũng fail). |
| **API error 404 (node không tồn tại)** | Ghi warning: "Node {nodeId} not found". `screenshot_path = null`. KHÔNG fallback. |
| **API error 429 (rate limit)** | Chờ 10s, retry 1 lần. Nếu vẫn fail → thử **fallback terminal**. |
| **API error 5xx / network** | Retry 1 lần (delay 2s). Nếu vẫn fail → thử **fallback terminal**. |
| **Fallback terminal cũng fail** | Ghi warning, `screenshot_path = null`. Tiếp tục Phase 2 — không block pipeline. |

5. **Fallback terminal (BẮT BUỘC khi MCP không khả dụng hoặc lỗi network/5xx):**

Agent **phải chạy** lệnh sau (thay `<workspace_root>`, `<file_key>`, `<node_id>`, `[output_base_dir]` bằng giá trị thực; `output_base_dir` thường = `output_dir` hoặc `{product-slug}`):

```bash
cd "<workspace_root>" && set -a && [ -f .env ] && . ./.env && set +a \
  && node scripts/save-figma-section-screenshots.js <file_key> <node_id> [output_base_dir]
```

- Token nằm trong `.env` dưới tên `FAT` hoặc `FIGMA_ACCESS_TOKEN`. Nếu thiếu token sau khi load `.env` → script báo lỗi rõ, ghi warning, `screenshot_path = null`.
- Sau khi script chạy xong: thực hiện post-step (bước 3) nếu ảnh nằm tại `{output_base_dir}/{file_name}/{page}/{section}/` (script có thể tạo `co-op-bank-khcn/co-op-bank-khcn/...` tùy slug Figma); nếu feature .md nằm ở path khác (vd. `Co-op-Bank-KHCN/app/main/`), copy hoặc link ảnh vào `ui/` tương ứng để link trong .md resolve đúng.

**1d-ii. Nhiều section trong cùng file:**

- Với mỗi section cần export: gọi **`figma_save_section_screenshots(fileKey, sectionNodeId, output_dir)`** một lần (MCP hoặc fallback terminal). Mỗi section = một thư mục con, không ghi đè.

Path và link ảnh: theo **Image Path Convention** trong `conventions.md`.

**1e. Get variables**
- Gọi `get_variable_defs(fileKey, nodeId)` → token variables
- Thu thập: variable names, collections, modes, resolved values, bindings

## Output (figma_raw)

```
figma_raw = {                   // design_data_layer: L1 (Figma Fundamentals)
  file_key: string,
  page_node_id: string,
  screens: [
    {
      node_id: string,
      name: string,              // Figma frame name
      width: number,
      height: number,
      layout_tree: [],           // nested layer hierarchy
      component_instances: [],   // named component usages
      text_nodes: [],            // {text, font_family, font_size, font_weight, color}
      style_properties: [],      // {fills, strokes, effects, border_radius, padding, gap}
      auto_layout: [],           // {direction, gap, padding, alignment}
      screenshot_path: string,    // absolute path to first artboard .png (null if failed)
      screenshot_relative: string, // for .md: path from workspace root to first artboard in ui/, vd ".../package-2/{section}/ui/{artboard-1}.png"
      screenshot_alt: string,     // alt text cho ảnh chính; để trống nếu chưa gán, sẽ điền ở bước Alt assignment (Phase 2f)
      sub_screenshots: [           // sub-frame screenshots (Phase 1d-ii)
        {
          node_id: string,
          section_name: string,    // Figma frame name (vd: "Thông tin chuyển tiền")
          screenshot_path: string,
          screenshot_relative: string,  // path from workspace root: ".../section/ui/artboard-slug.png"
          alt_text: string        // alt text cho artboard này; để trống nếu chưa gán, sẽ điền ở bước Alt assignment (Phase 2f)
        }
      ]
    }
  ],
  variables: [],                 // {name, collection, mode, resolved_value, bound_to}
}
```
