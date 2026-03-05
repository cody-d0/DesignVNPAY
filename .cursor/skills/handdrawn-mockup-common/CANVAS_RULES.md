# Canvas Rules — mockup hand-drawn (dùng chung)

Ràng buộc và quy trình vẽ mockup low-fi hand-drawn. Áp dụng cho **md-to-mockup** và **img-to-mockup** sau khi đã có **Mockup Spec** (theo SPEC_FORMAT.md).

Tham chiếu: **canvas-design** `.cursor/skills/canvas-design/SKILL.md` (Design Philosophy Creation + DEDUCING REFERENCE + CANVAS CREATION).

---

## Mockup Design System (bắt buộc)

- **Bắt buộc:** Mọi canvas creation (GenerateImage hoặc canvas-design) **phải** đọc và tuân thủ **MOCKUP_DESIGN_SYSTEM** tại `handdrawn-mockup-common/MOCKUP_DESIGN_SYSTEM.md`.
- **Không** tạo ảnh mockup nào mà không inject đoạn “Design system constraints” (Block 1) từ file đó vào prompt/instruction.
- Quy trình: load nội dung MOCKUP_DESIGN_SYSTEM.md trước Bước 3 (canvas creation); dùng **một** prompt template với Block 1 cố định + Block 2 (nội dung spec); chỉ thay đổi Block 2 giữa các ảnh.
- **Batch theo biên màn hình:** Khi gen mockup từ ảnh (img-to-mockup), ưu tiên batch theo biên màn hình; trong mỗi batch dùng **shared base + per-image delta** để tối ưu context và đồng nhất (Block 1 + shared_screen_block + delta_i).

---

## Ràng buộc front-view

- **Bắt buộc:** Mọi hình xuất ra ở dạng **front-view** (mặt trước).
- **Cấm:** Góc nghiêng (tilt), perspective 3D, góc nhìn từ cạnh hoặc từ trên xuống để thấy độ dày máy.
- **Mockup screen (type = screen):** Chỉ wireframe nội dung màn hình, không khung thiết bị; đặt trên canvas trắng width 400px, min-height 800px, height theo content (free), margin 5%, **top-constrained**.
- **State-guide (type = state_guide):** Không vẽ khung điện thoại. Các khối component/state bố trí trên nền phẳng, front-view (vuông góc với người xem).

---

## Quy trình 2 bước (Bước 2–4 của skill)

### Bước 2: Triết lý thị giác (.md)

- Nếu có `philosophy_override_md`: dùng file đó.
- Nếu không: dùng **PHILOSOPHY_DEFAULT** (nội dung tại `handdrawn-mockup-common/PHILOSOPHY_DEFAULT.md` hoặc `.cursor/skills/md-to-mockup/handdrawn-lowfi-philosophy.md`). Có thể ghi ra file .md trong output_dir nếu cần.

### Bước 2b: Load Mockup Design System (bắt buộc trước khi vẽ)

- **Đọc** `handdrawn-mockup-common/MOCKUP_DESIGN_SYSTEM.md` và giữ nội dung trong context cho **mọi** lần vẽ.
- Dùng Block 1 và cấu trúc Block 2 từ file đó khi gọi canvas-design / GenerateImage ở Bước 3. **Type = "screen":** Block 1 lấy **nguyên văn** từ MOCKUP_DESIGN_SYSTEM § Block 1 — Screen (không rút gọn; câu aspect ratio portrait 1:2 đã nằm trong Block 1).

### Bước 3: Canvas creation (canvas-design)

Áp dụng **MOCKUP_DESIGN_SYSTEM** (Block 1 + Block 2) và **canvas-design** SKILL:

1. **Load:** Đảm bảo đã load MOCKUP_DESIGN_SYSTEM.md (Bước 2b). Mỗi lần vẽ: inject **Block 1** (Design system constraints) từ MOCKUP_DESIGN_SYSTEM + **Block 2** (screen_title, component_stack_text từ spec) vào prompt.
2. **DEDUCING THE SUBTLE REFERENCE:** Chủ đề ngầm = wireframe cho màn hình / giao diện (ngữ cảnh từ spec hoặc nguồn input) — thể hiện qua bố cục và từ khóa trong wireframe, không cần nói rõ.
3. **CANVAS CREATION:**
   - **Spec type = "screen":** Vẽ chỉ wireframe theo `component_stack` trên canvas trắng; width 400px, **min-height 800px**, height theo content (free), margin 5% bốn cạnh, **top-constrained**. Không vẽ khung thiết bị (device frame). Prompt = **Block 1** + Block 2 (screen_title, component_stack_text). Block 1 = nguyên văn từ MOCKUP_DESIGN_SYSTEM § Block 1 — Screen. Chỉ một màu nhấn #7DD3FC cho CTA/FAB. **Chuẩn hóa:** Sau khi lưu file mockup, chạy `scripts/normalize-mockup-canvas.py --mode frame --width 400` lên file đó để đảm bảo width 400px, min-height 800px, top-constrained, margin 5%.
   - **Spec type = "state_guide":** Không vẽ khung điện thoại; chia nhóm theo `state_groups`; vẫn inject Block 1 cho line/accent/typography. Canvas **2:1 horizontal** (landscape).
4. **Ràng buộc:** Một trang duy nhất, .png; front-view nghiêm ngặt; không overlap chữ/khối; margin đủ. Không thêm mô tả style ngoài template.

### Bước 4: Xuất kết quả

- Một file .png (mockup). Khi có `output_filename`: ghi đúng tên trong `output_dir`; không có thì tên do implementation quyết định.
- **Chuẩn hóa canvas (mockup screen):** Sau khi tạo canvas, chạy `scripts/normalize-mockup-canvas.py --mode frame --width 400` lên file mockup để đảm bảo width 400px, min-height 800px, height theo content (free), margin 5% bốn cạnh, **top-constrained**.
- Tùy chọn: file triết lý .md, tóm tắt (loại spec, nguồn, đường dẫn .png). Khi có `output_spec_path`: ghi spec trung gian (JSON hoặc .md) trước khi vẽ.

---

## Tham chiếu

- **MOCKUP_DESIGN_SYSTEM:** `handdrawn-mockup-common/MOCKUP_DESIGN_SYSTEM.md`
- **SPEC_FORMAT:** `handdrawn-mockup-common/SPEC_FORMAT.md`
- **PHILOSOPHY_DEFAULT:** `handdrawn-mockup-common/PHILOSOPHY_DEFAULT.md`
- **Canvas-design:** `.cursor/skills/canvas-design/SKILL.md`
