---
name: md-to-mockup
description: Tạo mockup low-fi dạng hand-drawn từ file .md. Hình ảnh luôn front-view. Nếu là screen spec thì xuất wireframe màn hình trên canvas trắng width 400px, min-height 800px, height theo content (free), margin 5%, top-constrained; nếu là state/component guide thì chia nhóm và state với các design element. Sử dụng canvas-design cho triết lý thị giác và xuất .png.
license: Same as canvas-design
---

# Skill: Mockup low-fi hand-drawn từ Markdown

Skill này tạo mockup wireframe dạng vẽ tay (low-fi hand-drawn) từ file .md được chỉ định. Luôn dùng **front-view** (mặt trước, không nghiêng). Kết hợp **canvas-design** cho triết lý thiết kế và chất lượng hình ảnh.

## Khi nào dùng

- User yêu cầu tạo mockup low-fi / hand-drawn từ file .md
- User cần hình ảnh **front-view** (mặt trước thiết bị/màn hình)
- User cung cấp screen spec hoặc state-visual-guide dạng .md và cần xuất hình wireframe
- User muốn xuất screen dạng **wireframe trên canvas trắng width 400px, min-height 800px, height theo content (free), margin 5%, top-constrained** (không khung thiết bị)

## Input

| Tham số | Bắt buộc | Mô tả |
|--------|----------|--------|
| `md_file` | Có | Đường dẫn file .md (screen spec hoặc state-visual-guide). Khi dùng chế độ hai spec: đây là spec "before". |
| `output_dir` | Không | Thư mục lưu .png (mặc định: cùng thư mục với md_file hoặc `./output`) |
| `output_filename` | Không | Tên file .png khi lưu (không gồm path). VD: `mockup-before-ux-improve.png`. Khi có: ghi đúng tên này trong `output_dir`; khi không có: giữ hành vi hiện tại. |
| `philosophy_override_md` | Không | Đường dẫn .md triết lý thay thế (nếu không dùng mặc định hand-drawn low-fi) |
| `md_file_after` | Không | Đường dẫn file spec thứ hai (spec "after"). Chỉ dùng khi muốn sinh hai mockup trong một lần gọi. |
| `output_dir_after` | Không | Thư mục lưu .png cho spec after. Chỉ dùng khi có `md_file_after`. |
| `output_filename_before` | Không | Tên file .png cho spec before (chế độ hai spec). Nếu không có thì dùng `output_filename` cho lần gọi đầu. |
| `output_filename_after` | Không | Tên file .png cho spec after (chế độ hai spec). |
| `output_spec_path` | Không | Đường dẫn file để ghi spec trung gian (JSON hoặc .md) trước khi vẽ; dùng để debug hoặc làm input cho lần sau. |

## Định dạng spec trung gian (Mockup Spec)

Đầu ra **Bước 1** là một **Mockup Spec** theo định nghĩa chung. Chi tiết: `.cursor/skills/handdrawn-mockup-common/SPEC_FORMAT.md`.

- **type:** `"screen"` hoặc `"state_guide"`.
- **screen_title:** (khi type = screen) Tên màn hình.
- **component_stack:** (khi type = screen) Mảng `{ order, label_or_key, description? }` — thứ tự component từ trên xuống.
- **state_groups:** (khi type = state_guide) Mảng `{ component_key, states: [{ state, visual_description? }] }`.

Bước 2–4 dùng chung quy trình với **handdrawn-mockup-common** (triết lý → canvas-design → xuất .png). Tham chiếu: `CANVAS_RULES.md`, `PHILOSOPHY_DEFAULT.md` trong thư mục đó.

## Phân loại nội dung .md

Trước khi vẽ, **bắt buộc** phân biệt hai loại:

### Mockup Screen Spec (từ figma-to-prd-md)

**Format chuẩn:** File .md chỉ chứa `# Screen: {tên}` và block `### Mô tả màn hình` (bảng 4 cột: STT | Tên màn hình | Loại thành phần | Mô tả) hoặc **Component Stack** / **Mobile Layout** (Order | Component). Đây là format dùng cho spec "before" và "after" từ pipeline Figma-to-PRD. Skill xử lý giống loại **Screen** bên dưới (wireframe trên canvas trắng width 400px, min-height 800px, height theo content, margin 5%, top-constrained; theo thứ tự component).

### 1. Screen (màn hình)

**Dấu hiệu:** Trong file .md có ít nhất một trong các anchor sau:

- Tiêu đề dạng `# Screen:` hoặc `**Screen:**` + tên màn hình
- Bảng hoặc khối **Component Stack** / **Mobile Layout** / **Mobile Layout Skeleton**
- ASCII layout dạng `┌───┐` / `├───┤` / `└───┘` mô tả bố cục mobile
- Cột "Component" hoặc "Order | Component" rõ ràng

**Hành vi:** Coi nội dung là **một màn hình** → xuất **mockup wireframe màn hình** trên **canvas trắng**, width 400px, min-height 800px, height theo content (free), margin 5%, top-constrained; không vẽ khung thiết bị.

### 2. State / Component guide (không phải screen)

**Dấu hiệu:** Trong file .md có ít nhất một trong các anchor sau:

- Tiêu đề "State Visual Guide" / "State Matrix" / "Component Registry"
- Bảng có cột `component_key` (hoặc "Component") và `state` (hoặc "State")
- Mô tả trạng thái: default, focus, error, loading, success, empty, disabled, v.v.

**Hành vi:** Coi nội dung là **tập component và state** → xuất **nhóm design elements** theo component/state, **không** đặt trong khung điện thoại. Mỗi nhóm gồm: tên component, các state kèm visual description ngắn, có thể kèm token ref nếu có trong .md.

## Ràng buộc front-view

- **Bắt buộc:** Mọi hình xuất ra phải ở dạng **front-view** (mặt trước).
- **Cấm:** Góc nghiêng (tilt), perspective 3D, góc nhìn từ cạnh hoặc từ trên xuống để thấy độ dày máy.
- **Cho state-guide:** Các khối component/state bố trí trên nền phẳng, không cần khung thiết bị.

## Triết lý mặc định: Hand-drawn low-fi wireframe

Khi không có `philosophy_override_md`, dùng triết lý sau và ghi vào file .md (theo quy trình canvas-design):

**Tên:** "Sketch Clarity" hoặc "Hand-Drawn Low-Fi"

**Nội dung triết lý (4–6 đoạn ngắn):**

- **Form:** Đường nét giống vẽ tay: hơi run, không hoàn hảo, nét đen chủ đạo; hình chữ nhật và ô nhập có thể hơi lệch.
- **Space:** Khoảng trống rõ ràng giữa từng block (header, field, button); không che khuất.
- **Color:** Chủ yếu trắng/nền sáng + đen/xám cho chữ và viền; **chỉ một màu nhấn** (ví dụ xanh nhạt) cho CTA chính (button Xác nhận / Gửi / Primary).
- **Typography:** Chữ giống hand-lettered hoặc font mô phỏng viết tay; kích thước phân cấp (tiêu đề > label > placeholder).
- **Placeholder:** Ô nhập có thể biểu diễn bằng gạch ngang sóng (wavy lines) hoặc ô trống; dropdown có ký hiệu tam giác ▼ bên phải.
- **Craftsmanship:** Bản vẽ phải trông như được phác thảo cẩn thận, có chủ đích, không lộ vẻ AI cứng nhắc; mỗi thành phần nhận ra được (input, dropdown, button, header).

Triết lý này được dùng làm input cho bước **Express on canvas** của canvas-design.

## Quy trình thực thi

Chạy **tuần tự**:

### Bước 1: Đọc và phân loại .md → Mockup Spec

1. Đọc toàn bộ `md_file`.
2. Áp dụng **Phân loại nội dung .md** ở trên → kết luận **Screen** hoặc **State/Component guide**.
3. Trích xuất và **sinh Mockup Spec** (theo SPEC_FORMAT tại `handdrawn-mockup-common/SPEC_FORMAT.md`):
   - **Nếu Screen:** `type: "screen"`, `screen_title` = tiêu đề màn hình, `component_stack` = danh sách component theo thứ tự (từ Component Stack / Mobile Layout / bảng Mô tả màn hình), mỗi item có `order`, `label_or_key`, `description` (từ bảng hoặc mô tả).
   - **Nếu State-guide:** `type: "state_guide"`, `state_groups` = nhóm theo component_key, mỗi nhóm có `states` với `state` và `visual_description`.
4. (Tùy chọn) Khi có `output_spec_path`: ghi spec ra file JSON hoặc .md tại đường dẫn đó.

### Bước 2: Tạo triết lý thị giác (.md)

- Nếu có `philosophy_override_md`: dùng file đó.
- Nếu không: dùng triết lý **Hand-drawn low-fi** từ `handdrawn-mockup-common/PHILOSOPHY_DEFAULT.md` (hoặc `.cursor/skills/md-to-mockup/handdrawn-lowfi-philosophy.md`). Có thể tạo file .md trong `output_dir` nếu cần làm input cho canvas-design.

### Bước 3: Tạo canvas (.png) theo canvas-design

Áp dụng **CANVAS_RULES** tại `handdrawn-mockup-common/CANVAS_RULES.md` và **canvas-design** (`.cursor/skills/canvas-design/SKILL.md`):

1. **DEDUCING THE SUBTLE REFERENCE:** Chủ đề ngầm = "wireframe cho màn hình ngân hàng / giao dịch" (hoặc theo ngữ cảnh md_file) — thể hiện qua bố cục và từ khóa trong wireframe.
2. **CANVAS CREATION:** Theo Mockup Spec đã có:
   - **type = "screen":** Vẽ chỉ wireframe màn hình theo `component_stack` trên **canvas trắng**; width 400px, min-height 800px, height theo content (free), margin 5% bốn cạnh, top-constrained. Không vẽ khung thiết bị. Chữ và thành phần theo triết lý Hand-drawn low-fi; CTA một màu nhấn. Dùng **Block 1 (screen) nguyên văn** từ MOCKUP_DESIGN_SYSTEM § Block 1 — Screen (không rút gọn).
   - **type = "state_guide":** Không vẽ khung điện thoại; chia nhóm theo `state_groups`, mỗi nhóm có tiêu đề (component_key) và các state với mô tả/ký hiệu trực quan. Bố cục phẳng, front-view. Canvas **2:1 horizontal** (landscape).
3. **Ràng buộc:** Một trang duy nhất, .png; front-view nghiêm ngặt; không overlap chữ/khối; margin đủ.

### Bước 4: Xuất kết quả

- **Bắt buộc:** Một file .png (mockup hoặc state/component layout). Khi có `output_filename`: ghi đúng tên này trong `output_dir`; khi không có: tên do implementation quyết định.
- **Canvas output (mockup screen):** Mọi mockup screen: canvas trắng **width 400px**, **min-height 800px**, **height theo content (free)**, **margin 5%** bốn cạnh, **top-constrained**. Đảm bảo bằng bước chuẩn hóa: chạy `scripts/normalize-mockup-canvas.py --mode frame --width 400` sau mỗi lần gen mockup.
- **Khuyến nghị:** Một file .md triết lý (nếu vừa tạo mới) và tóm tắt ngắn: loại đã nhận diện (Screen / State-guide), file nguồn (md_file), đường dẫn .png. Khi có `output_spec_path`: đã ghi spec trung gian tại bước 1.

### Chế độ hai spec (khi có md_file_after và output_dir_after)

Khi có `md_file_after` và `output_dir_after`: chạy quy trình Bước 1–4 **hai lần** — lần 1 với `md_file` → `output_dir`, dùng `output_filename_before` hoặc `output_filename` nếu có; lần 2 với `md_file_after` → `output_dir_after`, dùng `output_filename_after` nếu có. Trả về cả hai đường dẫn .png trong tóm tắt.

## Output

| Đầu ra | Mô tả |
|--------|--------|
| `.png` | Mockup low-fi hand-drawn, front-view: wireframe màn hình trên canvas trắng width 400px, min-height 800px, height theo content (free), margin 5%, top-constrained HOẶC nhóm component/state. Khi có `output_filename`: tên file đúng theo tham số. |
| `.md` (tùy chọn) | Triết lý thị giác dùng để vẽ (theo canvas-design) |
| Tóm tắt | Loại (Screen / State-guide), file nguồn, đường dẫn .png. Chế độ hai spec: trả về cả hai đường dẫn .png. |

## Tham chiếu

- **Mockup Spec (common):** `.cursor/skills/handdrawn-mockup-common/SPEC_FORMAT.md` — định dạng spec trung gian; CANVAS_RULES.md, PHILOSOPHY_DEFAULT.md — quy trình Bước 2–4.
- **Canvas-design:** `.cursor/skills/canvas-design/SKILL.md` — dùng cho Design Philosophy Creation và Canvas Creation.
- **Mockup Screen Spec (figma-to-prd-md):** Format chuẩn cho spec before/after: `# Screen:`, `### Mô tả màn hình` (bảng 4 cột). Xem pipeline tại `.cursor/skills/figma-to-prd-md/SKILL.md` § Comparison mockups.
- **Screen spec mẫu:** File có `# Screen:`, `Component Stack`, ASCII layout ┌─┐.
- **State guide mẫu:** File có `State Visual Guide`, bảng `component_key | state | visual_description`.
- **Front-view:** Hình ảnh mặt trước, không nghiêng.
- **Chuẩn hóa canvas:** `scripts/normalize-mockup-canvas.py` — chế độ frame: width 400px, min-height 800px, height theo content, margin 5%, top-constrained (`--mode frame --width 400`).

## Lưu ý

- Nếu .md vừa có cấu trúc screen vừa có bảng state: ưu tiên **Screen** khi có `# Screen:` hoặc Component Stack rõ ràng; khi đó chỉ xuất một mockup screen (wireframe trên canvas width 400px, min-height 800px, free height, margin 5%, top-constrained), không xuất thêm sơ đồ state riêng trừ khi user yêu cầu.
- Font và nét vẽ: ưu tiên thư mục `./canvas-fonts` (theo canvas-design) nếu có; không thì chọn font có cảm giác hand-lettered/sketch.
- Đảm bảo mọi text trong wireframe (tiêu đề, label, nút) nằm trong biên, không bị cắt.
