# Mockup Design System — single source of truth

Ràng buộc kỹ thuật và thị giác để **mọi** mockup hand-drawn được sinh ra **đồng nhất tuyệt đối**. Mọi canvas creation (GenerateImage hoặc canvas-design) **bắt buộc** đọc file này và inject “Design system constraints” vào prompt/instruction. Tham chiếu: ui-ux-pro-max (consistency, design-system workflow), PHILOSOPHY_DEFAULT, CANVAS_RULES.

---

## Design System Variables (cố định)

| Biến | Giá trị | Mô tả |
|------|---------|--------|
| **Canvas ratio (frame / screen)** | **Width 400px, min-height 800px, max-height theo content** | Canvas trắng; width cố định 400px; **min-height 800px**; height tăng theo content (free). Dùng khi `type === "screen"`. |
| **Canvas ratio (component / state)** | **2:1 horizontal** (landscape) | width : height = 2 : 1. Dùng khi `type === "state_guide"`. |
| **Output (screen / frame)** | Canvas trắng 400×(>=800), top-constrained | Canvas #FFFFFF; width **400px**; **min-height 800px**; height theo content (free); **margin 5%** bốn cạnh; **constrain top** (trình bày từ trên xuống dưới, bám trên); **không vẽ khung thiết bị (device frame)**. Đảm bảo bằng `scripts/normalize-mockup-canvas.py --mode frame --width 400` sau khi gen. |
| **Line color** | #000000 (chủ đạo), xám đậm #374151 cho secondary | Không thêm màu ngoài accent. |
| **Line weight** | Mỏng, nhất quán; “wobbly” hand-drawn | Nét vẽ tay, hơi run, đồng nhất giữa các ảnh. |
| **Accent** | #7DD3FC (một màu duy nhất) | Chỉ dùng cho CTA, FAB, nút primary. Không dùng cho text body hoặc viền. |
| **Background** | #FFFFFF hoặc #FAFAFA | Nền canvas / nội dung. |
| **Typography** | Hand-lettered / sketch; title > label > placeholder | Không dùng font serif phức tạp. Phân cấp rõ. |
| **Spacing (padding nội dung)** | ~4% chiều cao vùng content trên/dưới, ~6% trái/phải | Padding bên trong vùng wireframe. |
| **Gap giữa component** | ~3–4% chiều cao vùng content | Khoảng cách giữa header, body, button. |

---

## Ràng buộc bắt buộc

- **Front-view only (bố cục nội dung):** Wireframe vuông góc với người xem; không tilt, không 3D, không perspective.
- **Một accent duy nhất:** Chỉ #7DD3FC cho một loại element (CTA / FAB / primary button); không thêm gradient hay màu nhấn thứ hai.
- **Không overlap:** Chữ và khối không chồng lên nhau; margin đủ.
- **Consistency:** Cùng line style và accent cho mọi mockup trong cùng một run (folder).

---

## Anti-patterns (cấm)

- Không 3D / tilt / perspective.
- Không thêm gradient ngoài fill đơn sắc cho accent.
- Không nhiều hơn một màu nhấn.
- Không thay đổi line weight hoặc accent giữa các ảnh trong cùng batch.
- Không dùng emoji làm icon UI (dùng ký hiệu đơn giản: ▼, +, ←).

---

## Prompt template (2 block)

Mọi lần sinh mockup **phải** dùng một template gồm **Block 1 (cố định)** và **Block 2 (thay đổi theo spec)**. Chỉ thay đổi Block 2 giữa các ảnh. **Chọn Block 1 theo type:** screen → Block 1 (screen); state_guide → Block 1 (state_guide). **Nguồn duy nhất:** Câu aspect ratio portrait 1:2 chỉ định nghĩa tại § Block 1 — Screen dưới đây; các skill (CANVAS_RULES, img-to-mockup, md-to-mockup, SPEC_FORMAT) chỉ tham chiếu section này, không lặp lại câu.

### Block 1 — Screen (frame / màn hình)

Dùng khi `type === "screen"`. Chỉ wireframe nội dung màn hình, **không** vẽ khung thiết bị (smartphone), **không** Dynamic Island. Prompt bắt buộc chỉ rõ **aspect ratio portrait 1:2** để ảnh gen ra đúng tỉ lệ ngay từ GenerateImage, giảm ép size sau.

**Bắt buộc giữ nguyên câu sau trong Block 1 (không bỏ khi copy prompt):**  
*"Output image aspect ratio: portrait 1:2 (width : height = 1 : 2); the image must be vertical, not horizontal or square."*

```
Hand-drawn low-fi wireframe mockup. Content only: no phone frame, no device border, no Dynamic Island. White canvas #FFFFFF. Output image aspect ratio: portrait 1:2 (width : height = 1 : 2); the image must be vertical, not horizontal or square. Canvas width 400px, minimum height 800px; height can grow to fit content. Equal margin 5% on all four sides around the wireframe content. Top-constrained layout: start content at the top margin and flow downward (do not vertically center). Lines: black #000000, wobbly hand-drawn style, consistent thin weight. Only one accent color: light blue #7DD3FC for the single primary button or FAB only. Typography: hand-lettered/sketch, hierarchy title > label > placeholder. Spacing: clear gaps between header, body, buttons; no overlapping text or elements. No gradients, no second accent, no emoji icons. Do not draw any device or phone frame.
```

### Block 1 — State guide (component / state)

Dùng khi `type === "state_guide"`.

```
Hand-drawn low-fi wireframe. No phone frame. Canvas ratio 2:1 horizontal (landscape). Front view only. Lines: black #000000, wobbly hand-drawn style. Only one accent #7DD3FC for primary elements. Typography: hand-lettered/sketch. Clear gaps between component groups and states; no overlapping. No gradients, no second accent, no emoji icons.
```

### Block 2 — Content (thay đổi theo Mockup Spec)

- **screen_title:** Tiêu đề màn hình (vd. "Danh bạ thụ hưởng", "Chi tiết danh bạ").
- **component_stack_text:** Mô tả ngắn các thành phần theo thứ tự từ trên xuống (vd. "Header: back + title + trash icon; gray bar with instruction text; section Chuyển tiền nội bộ expanded with 3 list items; FAB plus bottom right").

**Ví dụ ghép Block 1 (screen) + Block 2:**

```
[Block 1 nguyên văn]

Content for this screen: Screen title: "Danh bạ thụ hưởng". From top to bottom: Header with back arrow, title "Danh bạ thụ hưởng", trash icon. Light gray bar with text "Chọn danh bạ mà Quý khách muốn xóa". Section "Chuyển tiền nội bộ" expanded, 3 rows (avatar, name, number). Two more sections collapsed. FAB with plus icon bottom right. Use accent #7DD3FC only for the FAB.
```

### Quy tắc dùng template

1. Luôn load MOCKUP_DESIGN_SYSTEM.md trước khi gọi GenerateImage/canvas-design.
2. Mỗi ảnh: build Block 2 từ Mockup Spec (screen_title + component_stack → component_stack_text), ghép Block 1 + Block 2 thành một prompt duy nhất.
3. Không tự ý thêm mô tả style khác; không bỏ bớt ràng buộc từ Block 1 — đặc biệt không được bỏ câu aspect ratio (đã nêu trong đoạn **Bắt buộc giữ nguyên** ngay trên code block Block 1 — Screen).
4. **Batch theo biên màn hình:** Khi gen mockup từ ảnh, ưu tiên **batch theo biên màn hình** (mỗi lượt = một screen). Trong mỗi batch: prompt = **Block 1 nguyên văn** (không rút gọn) + shared_screen_block + delta_i; chỉ phần Block 2 (component_stack_text) được thay bằng shared_screen_block + delta để tránh lặp dài.

---

## Pre-delivery checklist (mockup)

Trước khi coi một mockup là xong, kiểm tra:

- [ ] Canvas screen: width 400px, min-height 800px, height theo content (free), margin 5% bốn cạnh, top-constrained (type = screen); hoặc 2:1 horizontal (state_guide).
- [ ] Chỉ một màu nhấn (#7DD3FC) cho CTA/FAB.
- [ ] Không overlap chữ/khối; margin đủ.
- [ ] Line style wobbly, đồng nhất với các mockup khác trong cùng batch.
- [ ] Không vẽ khung thiết bị (device frame) khi type = screen.

---

## Tham chiếu

- **ui-ux-pro-max:** `.cursor/skills/ui-ux-pro-max/SKILL.md` — consistency (“Use same style across all pages”), design-system workflow, Implementation Checklist / Design System Variables.
- **PHILOSOPHY_DEFAULT:** `handdrawn-mockup-common/PHILOSOPHY_DEFAULT.md`
- **CANVAS_RULES:** `handdrawn-mockup-common/CANVAS_RULES.md`
