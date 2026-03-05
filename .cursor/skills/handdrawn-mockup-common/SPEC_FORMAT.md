# Mockup Spec Format (trung gian)

Định dạng spec trung gian dùng chung cho **md-to-mockup** và **img-to-mockup**. Cả hai skill: Bước 1 sinh ra cấu trúc này; Bước 2–4 tiêu thụ để vẽ mockup (.png) theo CANVAS_RULES và PHILOSOPHY_DEFAULT.

---

## Cấu trúc (Mockup Spec)

```text
type: "screen" | "state_guide"
screen_title?: string          // bắt buộc khi type = "screen"
component_stack?: Array<{
  order: number,
  label_or_key: string,
  description?: string
}>
state_groups?: Array<{
  component_key: string,
  states: Array<{
    state: string,
    visual_description?: string
  }>
}>
```

- **type:** Loại mockup. `"screen"` = một màn hình (frame); output là wireframe trên canvas trắng **width 400px**, **min-height 800px**, height theo content (free), **margin 5%**, **top-constrained**; không khung thiết bị. `"state_guide"` = nhóm component/state, không khung thiết bị.
- **screen_title:** Tên màn hình (vd. "Chi tiết danh bạ", "Danh sách thụ hưởng"). Chỉ dùng khi `type === "screen"`.
- **component_stack:** Thứ tự thành phần từ trên xuống (header, field, button…). Mỗi item: `order` (1-based), `label_or_key` (tên hiển thị hoặc component_key), `description` (mô tả ngắn, tùy chọn).
- **state_groups:** Nhóm component kèm các state (default, focus, error, …). Chỉ dùng khi `type === "state_guide"`. Mỗi nhóm có `component_key` và mảng `states` với `state` + `visual_description` tùy chọn.

---

## Ví dụ: Screen

Spec từ file .md có bảng "Mô tả màn hình" hoặc Component Stack:

```json
{
  "type": "screen",
  "screen_title": "Chi tiết danh bạ",
  "component_stack": [
    { "order": 1, "label_or_key": "Header", "description": "Back + Chi tiết danh bạ + icon Home" },
    { "order": 2, "label_or_key": "Descriptions", "description": "Label-value: Loại chuyển tiền, Tên, Số TK, Ngân hàng" },
    { "order": 3, "label_or_key": "Input", "description": "Tên gợi nhớ — có thể sửa" },
    { "order": 4, "label_or_key": "Button", "description": "Cập nhật + Thực hiện giao dịch" }
  ]
}
```

---

## Ví dụ: State guide

Spec từ file .md có "State Visual Guide" / State Matrix:

```json
{
  "type": "state_guide",
  "state_groups": [
    {
      "component_key": "text-input",
      "states": [
        { "state": "default", "visual_description": "Viền mảnh, placeholder" },
        { "state": "focus", "visual_description": "Viền đậm, cursor" },
        { "state": "error", "visual_description": "Viền đỏ, message phía dưới" }
      ]
    },
    {
      "component_key": "primary-button",
      "states": [
        { "state": "default", "visual_description": "Màu nhấn, label rõ" },
        { "state": "disabled", "visual_description": "Xám, không click" }
      ]
    }
  ]
}
```

---

## Nguồn sinh spec

| Skill | Bước 1 → Spec |
|-------|----------------|
| **md-to-mockup** | Đọc .md → phân loại Screen / State-guide → parse bảng (Mô tả màn hình, Component Stack, State Matrix) → điền `screen_title` + `component_stack` hoặc `state_groups`. |
| **img-to-mockup** | Thu thập ảnh từ `images_path` → agent vision đọc từng ảnh → trích layout (header/body/footer), thành phần, text → điền cùng cấu trúc (một ảnh = một screen với `component_stack`, hoặc nhiều ảnh = `state_groups` khi heuristic nhận state). |

Sau khi có spec, cả hai skill áp dụng cùng quy trình: PHILOSOPHY_DEFAULT (hoặc override) → CANVAS_RULES (canvas-design) → xuất .png.

---

## Batch theo biên màn hình (img-to-mockup)

Khi img-to-mockup chạy **theo batch** (mỗi lượt = một biên màn hình), spec có thể gồm:

- **shared_screen_block (base):** Một lần per batch, tổng hợp từ tất cả spec trong batch. Gồm: `screen_title` (chuẩn), cấu trúc cố định (Header: back + title + [trash/home]; Section headers: [danh sách]; FAB bottom right; accent #7DD3FC only). **exact_strings chung:** screen_title, section_headers[], instruction_bar (nếu có). Dùng làm đoạn prompt chung cho mọi ảnh trong batch.
- **deltas[] (per-image):** Với mỗi ảnh i, chỉ phần **khác** so với base: instruction bar visible + exact text; search bar + placeholder; section nào expanded/collapsed + số item; modal (title, message, buttons); hoặc detail screen (label-value rows, input, buttons). Prompt cho ảnh i = Block 1 + shared_screen_block + deltas[i]. (Block 1 = nguyên văn từ MOCKUP_DESIGN_SYSTEM § Block 1 — Screen khi type = screen.)

**Lấy danh sách ảnh per screen:**
- Từ **screen_inventory:** Đọc file tại `screen_inventory_path`. Với mỗi `screens[k].wireframe_images`, mỗi phần tử có `filename`, `screenshot_relative` (path từ workspace root). Batch k = danh sách ảnh của screen k.
- Từ **screen_boundaries:** Đọc file tại `screen_boundaries_path`. Mỗi phần tử có `artboard_node_ids[]`; map node_id sang filename trong thư mục `images_path` (slug từ tên artboard hoặc mapping từ handoff figma-to-prd-md). Batch k = danh sách filename thuộc biên k.

Tham chiếu: figma-to-prd-md `phases/phase-2-inventory.md` § 2a-bis (mapping ảnh ↔ biên), § 2g (wireframe_images).
