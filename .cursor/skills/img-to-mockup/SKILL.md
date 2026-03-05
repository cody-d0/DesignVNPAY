---
name: img-to-mockup
description: Tạo mockup low-fi hand-drawn từ ảnh trong path bằng agent vision. Tạo folder tại path chỉ định, đọc toàn bộ ảnh trong folder, mỗi ảnh → một mockup .png; trích xuất layout bằng vision, sinh Mockup Spec rồi vẽ theo quy trình chung (triết lý hand-drawn, canvas-design, front-view).
license: Same as canvas-design
---

# Skill: Mockup low-fi hand-drawn từ ảnh (agent vision)

Skill này tạo mockup wireframe dạng vẽ tay (low-fi hand-drawn) từ **toàn bộ ảnh trong một folder** — **tạo folder đích** tại path chỉ định, dùng **agent vision** đọc từng ảnh, trích xuất layout/component, sinh Mockup Spec rồi vẽ **một mockup .png cho mỗi ảnh**, lưu vào folder đó. Luôn **front-view**; mỗi screen là wireframe màn hình trên **canvas trắng width 400px, min-height 800px, height theo content (free), margin 5%, top-constrained** (không vẽ khung thiết bị).

## Khi nào dùng

- User có thư mục ảnh wireframe/screenshot và muốn **chuyển toàn bộ ảnh trong folder thành mockup** hand-drawn
- User muốn tạo folder mockup tại path đó và lưu từng ảnh → một file mockup tương ứng
- User đã có output từ figma-to-prd-md (ảnh trong `ui/`) và cần bộ mockup hand-drawn cho tất cả ảnh

## Input

| Tham số | Bắt buộc | Mô tả |
|--------|----------|--------|
| `images_path` | Có | Đường dẫn thư mục chứa .png (từ workspace root, vd. `co-op-bank-khcn/.../danh-ba-thu-huong/ui`). Toàn bộ ảnh trong folder này sẽ được chuyển thành mockup. |
| `screen_inventory_path` | Không | Đường dẫn file JSON **screen_inventory** (từ workspace root). Nếu có: skill **ưu tiên batch theo biên màn hình** — mỗi lượt = một screen; danh sách ảnh mỗi batch = `screens[k].wireframe_images` (path = `screenshot_relative` hoặc `images_path` + filename). Tham chiếu: figma-to-prd-md Phase 2 § 2a-bis, 2g. |
| `screen_boundaries_path` | Không | Đường dẫn file JSON **screen_boundaries** (từ workspace root). Nếu có (và không có screen_inventory_path): đọc `screen_boundaries`; với mỗi phần tử k, map `artboard_node_ids[]` sang filename trong `images_path` (vd. slug từ tên artboard) → mỗi screen = một batch. |
| `output_dir` | Không | Thư mục đích để lưu .png mockup. **Skill tạo folder này nếu chưa tồn tại.** Mặc định: cùng cấp với `images_path`, tên folder `mockups` (vd. `.../danh-ba-thu-huong/mockups`). |
| `output_filename` | Không | Chỉ dùng khi chỉ có **một** ảnh hoặc khi muốn ghi đè tên duy nhất. Khi có nhiều ảnh: mỗi file mockup đặt tên theo ảnh gốc + suffix (vd. `contact.png` → `contact-mockup.png`). |
| `one_mockup_per_image` | Không | `true` (mặc định): mỗi ảnh → 1 mockup, lưu vào output_dir. `false`: gộp toàn bộ ảnh thành 1 spec → 1 file mockup (ít dùng). |
| `philosophy_override_md` | Không | Đường dẫn .md triết lý thay thế (nếu không dùng mặc định hand-drawn low-fi). |
| `output_spec_path` | Không | Đường dẫn file hoặc thư mục để ghi spec trung gian (JSON hoặc .md). Có thể là 1 file (mảng spec) hoặc folder (1 file spec per ảnh). |

## Tạo folder và quy ước tên file

- **Tạo folder:** Trước khi ghi bất kỳ .png nào, skill **tạo thư mục `output_dir`** nếu chưa tồn tại (mkdir). Path từ workspace root.
- **Tên file mockup (nhiều ảnh):** Với mỗi ảnh `{base}.png`, file mockup lưu là `{base}-mockup.png` (hoặc `{base}-handdrawn.png`) trong `output_dir`. Ví dụ: `contact.png` → `contact-mockup.png`, `contact-details-2.png` → `contact-details-2-mockup.png`.
- **Một ảnh và có `output_filename`:** Ghi đúng tên đó trong `output_dir`.

## Định dạng spec trung gian (Mockup Spec)

Đầu ra **Bước 1** là **Mockup Spec** theo định nghĩa chung tại `.cursor/skills/handdrawn-mockup-common/SPEC_FORMAT.md`. Khi chạy **theo batch (một biên màn hình)**, spec có thể gồm **shared_screen_block** (base) + **deltas[]** (per-image) để tối ưu token và đồng nhất — xem § Batch theo biên màn hình và SPEC_FORMAT § Base + delta. Bước 2–4 áp dụng **handdrawn-mockup-common** (CANVAS_RULES.md, **MOCKUP_DESIGN_SYSTEM.md**, PHILOSOPHY_DEFAULT.md) — cùng quy trình với md-to-mockup. **MOCKUP_DESIGN_SYSTEM** là MASTER cho mockup hand-drawn (consistency, single prompt template); tham chiếu ui-ux-pro-max § design-system và "Use same style across all pages".

## Batch theo biên màn hình

- **Mỗi lượt tạo mockup** = xử lý **một biên màn hình** (một screen). Toàn bộ ảnh thuộc biên đó được gen trong cùng một lượt, dùng **cùng** Block 1 + cùng **shared_screen_block** (base) → đồng nhất tối đa (casing, line weight, spacing, accent) giữa các mockup của cùng màn.
- **Nguồn batch:** Khi có `screen_inventory_path` hoặc `screen_boundaries_path`: đọc file (từ workspace root); với mỗi screen k, batch = danh sách ảnh thuộc screen đó (xem § Thu thập ảnh). Khi **không có**: fallback = toàn bộ `*.png` trong `images_path` coi như một batch (hoặc heuristic theo thư mục con / prefix tên file).
- **Trong mỗi batch:** (1) Vision extraction cho từng ảnh → spec từng ảnh; (2) Gộp thành **shared_screen_block** (base) và **delta** từng ảnh; (3) Generate mockup từng ảnh với prompt = **Block 1** + shared_screen_block + delta_i — không lặp lại toàn bộ component_stack_text dài.
- **Lợi ích:** Giảm lặp token; context một lần load Block 1 + base, chỉ thay delta giữa các lần gen; đồng nhất tối đa trong cùng biên.

## Quy trình thực thi

Chạy **tuần tự**:

### Bước 1: Thu thập ảnh và vision extraction → Mockup Spec (theo batch biên màn hình)

1. **Tạo folder đích:** Resolve `output_dir` (mặc định: `{parent của images_path}/mockups`). **Tạo thư mục này nếu chưa tồn tại** (mkdir).

2. **Thu thập ảnh và chia batch (biên màn hình):**
   - **Nếu có `screen_inventory_path`:** Đọc file JSON từ workspace root. Với mỗi `screens[k]`, lấy `wireframe_images`; mỗi phần tử có `filename` và (nếu có) `screenshot_relative`. Path ảnh = `screenshot_relative` nếu có, ngược lại = `images_path` + `/` + `filename`. Batch k = danh sách `[{ filename, path_from_workspace }]` của screen k. Lặp k = 0..length(screens)-1 → danh sách các batch.
   - **Nếu có `screen_boundaries_path` (và không có screen_inventory_path):** Đọc file JSON; với mỗi phần tử có `artboard_node_ids[]`, map node_id sang filename trong thư mục `images_path` (quy ước: slug từ tên artboard hoặc mapping từ handoff). Batch k = danh sách ảnh thuộc biên k.
   - **Nếu không có cả hai:** Một batch duy nhất = list tất cả `*.png` trong `images_path` (hoặc từ file list path nếu `images_path` trỏ tới file) → `[{ filename, path_from_workspace }]`. Có thể chia heuristic theo thư mục con hoặc prefix tên file (tùy chọn).
   - **Giới hạn:** Khuyến nghị tối đa 20–30 ảnh mỗi batch; nếu một screen có quá nhiều ảnh, document hoặc xử lý theo lô con.

3. **Với mỗi batch (một biên màn hình):**
   - **Vision extraction (từng ảnh trong batch):** Đọc từng ảnh bằng tool Read(path). Trích xuất: layout (header, body, footer), thành phần (label, ô nhập, nút, icon), text hiển thị. Sinh **một** Mockup Spec `type: "screen"` cho mỗi ảnh: `screen_title`, `component_stack`, và (nếu trích được) exact_strings (title, instruction_bar, section_headers[], button labels).
   - **Build shared_screen_block (base):** Từ tất cả spec trong batch, gộp thành một **base** chung: `screen_title` (dùng phiên bản chuẩn nếu có khác nhau), cấu trúc cố định (Header: back + title + [trash/home]; Section headers: [danh sách]; FAB bottom right; accent #7DD3FC only cho FAB/primary). **exact_strings chung:** screen_title, section_headers[] (thứ tự từ trên xuống), nếu có instruction bar mặc định. Lưu vào biến `shared_screen_block` (text) cho batch này.
   - **Build delta từng ảnh:** Với mỗi ảnh i trong batch, sinh **delta_i** = chỉ phần khác so với base: instruction bar visible + exact text (nếu có); search bar + placeholder (nếu có); section nào expanded/collapsed + số item; modal overlay (title, message, buttons) nếu có; hoặc detail screen (label-value rows, input, buttons). Lưu mảng `deltas[]` (theo filename hoặc order).

4. **one_mockup_per_image:**
   - **true (mặc định):** Mỗi ảnh trong batch tương ứng một file mockup `{basename}-mockup.png` trong output_dir; prompt cho ảnh i = **Block 1** + shared_screen_block + delta_i (khi có base) hoặc Block 1 + Block 2 đầy đủ (khi không build được base).
   - **false:** Gộp toàn bộ ảnh trong batch thành một spec → một file mockup; dùng `output_filename` nếu có.

5. **(Tùy chọn)** Khi có `output_spec_path`: ghi spec — per batch có thể ghi một file chứa `shared_screen_block` + `deltas[]` (theo filename); hoặc mảng spec đầy đủ; hoặc từng file `{basename}-spec.json` tương ứng từng ảnh.

### Bước 2: Tạo triết lý thị giác (.md)

- Nếu có `philosophy_override_md`: dùng file đó.
- Nếu không: dùng **PHILOSOPHY_DEFAULT** từ `handdrawn-mockup-common/PHILOSOPHY_DEFAULT.md`. Có thể ghi ra file .md trong output_dir nếu cần cho canvas-design.

### Bước 2b: Load Mockup Design System (bắt buộc trước khi vẽ)

- **Đọc** `handdrawn-mockup-common/MOCKUP_DESIGN_SYSTEM.md` và giữ nội dung trong context cho **mọi** lần vẽ.
- Dùng **Block 1** và cấu trúc **Block 2** từ file đó khi gọi canvas-design / GenerateImage ở Bước 3. **Type = screen:** Block 1 copy **nguyên văn** từ MOCKUP_DESIGN_SYSTEM § Block 1 — Screen (không rút gọn; câu aspect ratio portrait 1:2 đã nằm trong Block 1).

### Bước 3: Tạo canvas (.png) theo canvas-design

Áp dụng **CANVAS_RULES** tại `handdrawn-mockup-common/CANVAS_RULES.md`, **MOCKUP_DESIGN_SYSTEM** tại `handdrawn-mockup-common/MOCKUP_DESIGN_SYSTEM.md`, và **canvas-design** (`.cursor/skills/canvas-design/SKILL.md`):

- **Prompt template (bắt buộc):**
  - **Khi batch có shared_screen_block + deltas:** Với mỗi ảnh i trong batch: prompt = **Block 1** + **shared_screen_block** (base: screen_title, section headers, exact_strings chung, cấu trúc header/FAB) + **delta_i** (chỉ phần khác: instruction bar, search bar, expanded section, modal, detail layout). Cuối prompt: "Use accent #7DD3FC only for FAB/primary. Do not paraphrase exact strings." Không lặp lại toàn bộ component_stack_text dài cho từng ảnh.
  - **Khi không có base/delta (batch đơn ảnh hoặc fallback):** Prompt = **Block 1** + **Block 2** đầy đủ: `screen_title` + `component_stack_text` (build từ Mockup Spec: screen_title và component_stack → mô tả ngắn từ trên xuống). Ví dụ: "[Block 1] … Content for this screen: Screen title: {screen_title}. From top to bottom: {component_stack_text}. Use accent #7DD3FC only for primary button/FAB."
- **Spec type = "screen":** Vẽ **chỉ wireframe nội dung màn hình** (không khung máy, không island), đặt trên **canvas trắng**, **width 400px**, **min-height 800px**, **height theo content (free)**, **margin 5%** bốn cạnh, **top-constrained**. Prompt = Block 1 + (shared_screen_block + delta_i) hoặc Block 1 + Block 2. Block 1 = nguyên văn từ MOCKUP_DESIGN_SYSTEM § Block 1 — Screen.
- **Spec type = "state_guide":** Không khung điện thoại; nhóm theo `state_groups`; vẫn inject Block 1 cho line/accent/typography. Canvas **2:1 horizontal** (landscape).
- Ràng buộc: một trang .png, front-view nghiêm ngặt, không overlap, margin đủ. Không tự ý thêm mô tả style ngoài template.

(Khi có nhiều spec hoặc nhiều ảnh trong batch: lặp Bước 2–3 cho từng ảnh; mỗi mockup lưu vào output_dir với tên `{basename}-mockup.png`.)

### Bước 4: Xuất kết quả

- **Bắt buộc:** Tạo folder `output_dir` nếu chưa có; ghi từng file .png mockup vào folder đó. Nhiều ảnh: tên file `{basename}-mockup.png`; một ảnh và có `output_filename`: dùng tên đó.
- **Canvas output:** Mọi mockup screen: canvas trắng **width 400px**, **min-height 800px**, **height theo content (free)**, **margin 5%** bốn cạnh, **top-constrained**. Đảm bảo bằng bước chuẩn hóa: sau mỗi lần gen mockup, chạy `scripts/normalize-mockup-canvas.py --mode frame --width 400` (xem § Scripts).
- **Khuyến nghị:** Tóm tắt: nguồn (images_path), số ảnh, số file mockup đã ghi, đường dẫn folder và danh sách file .png. Khi có `output_spec_path`: đã ghi spec tại Bước 1.

## Output

| Đầu ra | Mô tả |
|--------|--------|
| **Folder** | `output_dir` — được tạo nếu chưa tồn tại. |
| **.png** | Một file mockup cho mỗi ảnh: `{basename}-mockup.png` trong folder (wireframe trên canvas trắng width 400px, min-height 800px, height theo content, margin 5%, top-constrained). |
| Spec (tùy chọn) | File hoặc folder tại `output_spec_path` (mảng spec hoặc 1 file per ảnh). |
| Tóm tắt | Nguồn ảnh, số ảnh, đường dẫn folder, danh sách file mockup đã tạo. |

## Path convention

- Path ảnh luôn **từ workspace root** (giống Phase 2g/2g-bis và figma-to-prd-md conventions). Tương thích với output từ figma-to-prd-md: ảnh trong `{section}/ui/*.png`.

## Tham chiếu

- **Mockup Design System (MASTER):** `.cursor/skills/handdrawn-mockup-common/MOCKUP_DESIGN_SYSTEM.md` — single source of truth cho canvas (width 400px, min-height 800px, top-constrained cho frame/screen; 2:1 horizontal cho component/state), line, accent, typography, spacing; prompt template Block 1 + Block 2.
- **Mockup Spec (common):** `.cursor/skills/handdrawn-mockup-common/SPEC_FORMAT.md`, `CANVAS_RULES.md`, `PHILOSOPHY_DEFAULT.md`.
- **ui-ux-pro-max:** `.cursor/skills/ui-ux-pro-max/SKILL.md` — consistency ("Use same style across all pages"), design-system workflow; Mockup Design System áp dụng tương tự cho hand-drawn mockup.
- **md-to-mockup:** Cùng quy trình Bước 2–4; khác nguồn Bước 1 (.md vs ảnh).
- **OCR (agent vision):** `.cursor/skills/figma-to-prd-md/phases/phase-2-inventory.md` § 2g, 2g-bis — cách đọc ảnh từ path (Read tool), hai round text + icon; skill này chỉ cần trích đủ cho component_stack/state_groups, không sinh ocr_full_table/ocr_gaps. **Batch theo biên:** § 2a-bis (screen_boundaries, mapping ảnh ↔ biên), § 2g (wireframe_images per screen).
- **Canvas-design:** `.cursor/skills/canvas-design/SKILL.md`.
- **Image path convention:** `.cursor/skills/figma-to-prd-md/conventions.md` § Image Path Convention.
- **Chuẩn hóa canvas:** `scripts/normalize-mockup-canvas.py` — chế độ frame: width 400px, min-height 800px, height theo content, margin 5%, top-constrained (`--mode frame --width 400`).

## Lưu ý

- **Tạo folder:** Skill luôn tạo `output_dir` trước khi ghi file; path từ workspace root.
- **Toàn bộ ảnh → mockup:** Mặc định mỗi ảnh trong folder tạo một mockup; tên file `{basename}-mockup.png` trong output_dir.
- Vision cost: nhiều ảnh = nhiều lần đọc và nhiều lần vẽ; có thể xử lý theo lô (vd. 10 ảnh/lần) nếu folder rất lớn.
