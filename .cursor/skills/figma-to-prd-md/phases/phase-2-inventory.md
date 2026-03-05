# Phase 2: Screen Inventory

**Tham chiếu:** Load `data/component-mapping.md` khi thực hiện bước 2b; Load `data/term-equivalents.md` khi thực hiện bước 2b-pre (chuẩn hóa ngôn ngữ trước mapping).

## Mục tiêu

Từ figma_raw, nhận diện screens, map components, suy navigation flow, sinh figma_context_registry.

## 2a. Screen identification

- Mỗi top-level frame trong figma_raw.screens = 1 screen
- Sinh `screen_id` từ frame name (kebab-case: "Chuyển tiền nội bộ" → `chuyen-tien-noi-bo`)
- Sinh `screen_name_vi` giữ nguyên tên Figma (tiếng Việt)

## 2a-bis. Screen boundary detection (khi 1 Figma section chứa nhiều artboards)

Áp dụng khi figma_raw có nhiều artboards trong cùng một section (vd: 6 artboards trong section "Chuyển tiền nội bộ cùng chủ"). Mục tiêu: phân biệt **màn hình mới** vs **variant của cùng màn hình** để sinh đúng số file .md (mỗi distinct screen = 1 file .md).

**Heuristic (theo thứ tự ưu tiên):**
1. **Tên artboard khác biệt:** Artboard có tên rõ ràng khác (vd: "Chuyển tiền nội bộ", "Xác nhận giao dịch", "Kết quả giao dịch") → mỗi tên = 1 distinct screen. Sinh `screen_id` và `screen_name_vi` từ tên artboard.
2. **Cấu trúc UI khác biệt:** Phân tích layout/component từ design context: artboard chủ yếu form (nhiều input) → `screen_type=form`; artboard chủ yếu label-value (bill detail, summary) → `screen_type=confirm`; artboard có success icon + CTA "Tạo giao dịch mới" → `screen_type=result`. Hai artboard có `screen_type` khác nhau → 2 screens.
3. **Variant cùng màn hình:** Artboard cùng form nhưng khác state (vd: "đặt lịch bật" vs "đặt lịch tắt") → **cùng screen**, không tách file; liệt kê trong flow variants (Section 1 User Flow) của feature file đó.

**Output:** Bổ sung vào screen_inventory (hoặc figma_raw):
- `screen_boundaries`: mảng các item theo schema trong [.cursor/docs/ddl/glossary.md](.cursor/docs/ddl/glossary.md) § Screen boundaries schema. Trường bắt buộc: `screen_id`, `screen_name_vi`, `artboard_node_ids[]`, `screen_type`. `screen_type` ∈ { form, confirm, result, list, detail, error } (enum mở rộng được — có thể thêm onboarding, search, filter, …).
- Trường optional mở rộng (không phá tương thích): `order`, `variant_of`, `tags[]`, `source_anchor`.
- Khi có `screen_boundaries`: dùng làm nguồn cho "distinct screens" trong Phase 3a (Overview mục 3, 8) và Phase 3b (số feature files). Mỗi phần tử screen_boundaries = 1 file .md.

**Determinism rule (bắt buộc):**
- `screen_boundaries` không được rỗng (trừ khi allow_section_fallback).
- Nếu không sinh được boundaries:
    - `allow_section_fallback=false` → dừng pipeline với mã `SCREEN_BOUNDARY_MISSING`.
    - `allow_section_fallback=true` → ghi warning `SCREEN_BOUNDARY_FALLBACK_USED` và cho phép fallback 1 section = 1 .md ở Phase 3.

**Mapping ảnh ↔ biên màn hình:**
- Với mỗi phần tử `screen_boundaries[k]`, tập ảnh (PNG) thuộc biên đó = các file tương ứng với `artboard_node_ids[]` (map node_id → filename trong `{section}/ui/`, ví dụ slug từ tên artboard). `screen_inventory.screens[k].wireframe_images` **chỉ** chứa đúng các ảnh thuộc biên màn hình k: không thêm ảnh của biên khác, không bỏ ảnh thuộc biên này.
- **Ràng buộc:** `length(screen_inventory.screens) === length(screen_boundaries)`. Mỗi screen k có `wireframe_images` = danh sách **đầy đủ** các PNG của biên k (không nhiều hơn, không ít hơn so với artboard_node_ids của biên đó).

## 2b-pre. Language normalization + semantic equivalence (trước 2b)

Chuẩn hóa chuỗi từ Figma (layer name, label) về cùng ngôn ngữ canonical và áp dụng bảng tương đương nghĩa để giảm gap khi Figma dùng ngôn ngữ khác so với component-mapping.

**Load `data/term-equivalents.md` ngay bây giờ.**

- **Input:** Tham số `mapping_canonical_language` (mặc định `vi`). Với mỗi layer name / label từ Figma:
  1. Chuẩn hóa tối thiểu: trim, lowercase (hoặc normalize Unicode theo ngôn ngữ).
  2. Tra bảng term-equivalents: nếu chuỗi (hoặc từ khóa trong chuỗi) nằm trong **aliases** của một canonical_term → thay bằng **canonical_term** để dùng cho match.
  3. Kết quả: `layer_name_normalized` (và giữ `layer_name` gốc để citation). Đầu vào cho 2b là `layer_name_normalized` (và tùy chọn thử cả `layer_name` gốc nếu normalized không match).
- **Output:** Không đổi schema; 2b nhận chuỗi đã chuẩn hóa nên tỷ lệ match tăng. Citation vẫn dùng layer name gốc từ Figma.

## 2b. Component recognition (per screen)

Map Figma layer names → `prd_type` + `component_key` theo bảng trong `data/component-mapping.md`. **Đầu vào:** tên layer đã qua 2b-pre (chuẩn hóa + synonym từ term-equivalents).

**Load `data/component-mapping.md` ngay bây giờ để thực hiện bước này.**

Ghi chú khi nhận ra component (dùng cho Phase 4 augment): icon-only button thiếu aria-label; touch target < 44px; emoji làm icon UI (đề xuất SVG); fixed navbar che content; font generic (Arial/Inter).

## 2b-bis. Unmapped elements → Design element (sau 2b)

Sau 2b, với mỗi screen: duyệt `figma_raw.screens[i].layout_tree` (hoặc `component_instances` nếu layout_tree không có) để lấy danh sách node con. Với mỗi node **chưa** có trong `components` (chưa được map ở 2b):

- Nếu node visible và có thể đặt tên (tên Figma hoặc inferred: "Illustration", "Icon", "Shape", "Background"…) → thêm 1 phần tử vào `screen_inventory.screens[k].components` với:
  - `prd_type`: "Design element" (hoặc "Illustration"/"Decoration" theo heuristic)
  - `component_key`: `design-element-{kebab-case-name}` hoặc `illustration`, `decoration`
  - `component_group`: "Special" (hoặc nhóm "Decoration")
  - `description_vi`: mô tả ngắn từ tên Figma hoặc "Phần tử trang trí / minh họa"
  - `figma_layer_path`: node_id / path
  - `is_new_key`: true
- Quy ước: giới hạn độ sâu/lọc (vd chỉ node trực tiếp dưới frame hoặc kích thước > ngưỡng) để tránh quá nhiều row. Áp dụng khi `include_unmapped_elements` = true (mặc định true).

## 2b-ter. Design spec summary (optional, khi include_design_specs = true)

Từ `figma_raw.screens[i].style_properties` và `auto_layout`, sinh object tóm tắt per screen: `design_spec_summary`: `{ gap_common, padding_common, border_radius_common, has_fills }` hoặc mảng rút gọn. Bổ sung vào `screen_inventory.screens[k].design_spec_summary`.

## 2c. Text/Label extraction

- Extract tất cả visible text nodes per screen
- Phân loại: `label`, `helper`, `value`, `heading`
- Giữ nguyên ngôn ngữ gốc (tiếng Việt)

## 2d. Navigation flow inference

- Scan text nodes cho pattern: "Tiếp tục", "Quay lại", "Xác nhận", navigation labels
- Scan bottom-bar items → link giữa screens
- Scan button actions → suy luận screen transitions
- Nếu Figma có prototype links (từ design_context): dùng trực tiếp
- Output: `flow_graph` (directed edges giữa screens)
- COMPbase khi có Figma evidence; UNSPECIFIED khi suy luận

## 2e. Figma context registry

- Từ text nodes + section frames, sinh `figma_context_registry`
- Giữ nguyên `context_label` từ Figma (vd: "Thông tin chuyển tiền", "Tài khoản nguồn")
- Phân loại `context_type`: section, field_group, component_group, label
- Gán `screen_id` và `canonical_key`

## 2f. Alt text assignment (bắt buộc trước khi sinh Section 3 Wireframe)

- **Input:** Với mỗi screen trong figma_raw: danh sách ảnh có (screenshot chính + sub_screenshots), mỗi item tương ứng file trong `{section}/ui/{filename}.png`.
- **Hành động:** Với **từng** ảnh, theo đúng thứ tự (ảnh chính trước, rồi sub_screenshots theo thứ tự):
  1. Xem nội dung ảnh (đọc file ảnh từ disk hoặc `get_screenshot`/design context cho node tương ứng).
  2. Sinh **một** alt text theo format và độ dài quy định (xem Quy tắc ảnh — max 125 ký tự, cấu trúc `[Loại] — [Nội dung chính]`, tiếng Việt).
  3. Gán alt vào figma_raw: `screenshot_alt` cho ảnh chính, `alt_text` cho từng phần tử `sub_screenshots[]`.
  4. Sinh và điền `wireframe_images` trong screen_inventory: danh sách theo thứ tự ảnh chính (1 phần tử từ `screenshot_path`/`screenshot_relative`/`screenshot_alt`) rồi lần lượt từng `sub_screenshots[]`; mỗi phần tử `{ filename, screenshot_relative, alt_text }` với `filename` = basename của path (vd: `internal-transaction.png`); không sinh lại alt khi ghi .md.
- **Ràng buộc:** Mỗi lần chỉ sinh alt cho **một** ảnh, gán xong rồi mới sang ảnh tiếp theo — tránh sinh một lúc N caption rồi paste nhầm thứ tự (swap). Alt phải mô tả đúng nội dung ảnh đó (màn hình/trạng thái, nội dung nổi bật), không dùng chung caption theo tên frame Figma.

## 2g. OCR reconciliation (bắt buộc) — chạy sau 2f cho từng screen có wireframe_images

**Contract OCR theo biên màn hình:**
- **Đơn vị thực thi:** Một lượt OCR = **một biên màn hình** (một screen k).
- **Phạm vi ảnh:** Trong một lượt, chỉ dùng **tất cả và chỉ** các ảnh trong `screen_inventory.screens[k].wireframe_images` (đúng các PNG thuộc biên k). Không gộp ảnh của biên khác; không bỏ bất kỳ ảnh nào thuộc biên này.
- **Kết quả:** Sau khi chạy đủ **hai round** cho biên k (Round 1 + Round 2), điền xong `ocr_full_table` (và ocr_round1_text, ocr_round2_icons), rồi thực hiện Bước 2–4 (gap, ocr_screen_context, ocr_ux_improvements) **chỉ** cho biên màn hình k; gán vào `screen_inventory.screens[k]`.
- **DDL:** Tham chiếu DDL (ux-guidelines, web-interface, ux-laws) khi sinh `ocr_ux_improvements` được thực hiện **theo từng biên màn hình**; mỗi đề xuất gắn với screen_id/biên tương ứng và `ddl_ref` tương ứng.

**Phương pháp duy nhất — Agent vision:** Agent đọc từng file ảnh từ path `screenshot_relative` (tool Read với path ảnh). **Không** còn fallback script, **không** Tesseract, **không** bước kiểm tra môi trường. OCR thực hiện bằng **hai round** bắt buộc cho mỗi screen có `wireframe_images`.

**Hai round bắt buộc cho mỗi screen k có `wireframe_images`:**

- **Round 1 — Text:** Agent đọc **tất cả** ảnh trong `wireframe_images[k]`, trích xuất **toàn bộ text** (mọi dòng, nhãn, placeholder, giá trị hiển thị).
  - **Mục đích dữ liệu:** UX writing, suy luận ngữ cảnh màn hình, suy luận UX, đối chiếu/mapping với spec.
  - **Output Round 1:** Điền `ocr_round1_text` (mảng `{ filename, text_content, lines?, source }` hoặc tương đương) và các row `type: "text"` vào `ocr_full_table`; giữ `ocr_full_text` (tương thích) nếu cần.
- **Round 2 — Icons + vị trí:** Agent đọc lại **cùng tập ảnh** của biên k, trích xuất **tất cả icon** và **thông tin vị trí** của từng icon.
  - **Vị trí:** Gồm zone (header | body | footer | left | right | top | bottom) và chi tiết (trái/phải, trên/dưới, inline_left, inline_right, …) để phục vụ suy luận và mapping.
  - **Output Round 2:** Điền `ocr_round2_icons` (mảng `{ filename, description_or_label, position_zone, position_detail?, source }`) và thêm các row `type: "icon"` vào `ocr_full_table` (kèm `position_zone`, `position_detail?`).

**Thứ tự thực thi:** Với từng screen k: chạy Round 1 xong (đủ ảnh của k) → chạy Round 2 (cùng ảnh) → sau khi có đủ `ocr_full_table` (text + icon) mới chạy Bước 2–4 (đối chiếu → ocr_gaps, ocr_screen_context, ocr_ux_improvements).

**Input:** Với mỗi screen: `wireframe_images[]` (filename, screenshot_relative → đọc file từ disk), `components`, `text_nodes` cho screen đó.

**Bước 2 — Đối chiếu từ bảng → gap:** Từ `ocr_full_table`, đối chiếu từng row với `text_nodes` và `components` (2b, 2b-bis). Gán mỗi row: **matched_spec** (Y/N). Chuẩn hóa và match (substring/token). Các row **N** → ghi vào `ocr_gaps.missing_text[]` hoặc `ocr_gaps.missing_components[]` tùy loại (text vs icon). Icon có thể match với component Design element / Icon theo mô tả + vị trí. Citation mỗi item: `ocr:{filename}`.

**Bước 3 — Suy luận ngữ cảnh:** Từ `ocr_round1_text` / `ocr_full_text` (hoặc ocr_full_table) + `components`, sinh `ocr_screen_context`: 1–2 câu tóm tắt màn hình (loại màn, thành phần chính, hành động chính).

**Bước 4 — Suy luận UX tiềm tàng / cải thiện:** Từ `ocr_gaps` + `ocr_full_table`/`ocr_full_text` + `components`, sinh `ocr_ux_improvements`. **Bắt buộc tham chiếu DDL** (conventions § DDL reference): query scope GLOBAL (ux-guidelines.csv, web-interface.csv, ux-laws.csv), đối chiếu phát hiện tiềm tàng với rule tương ứng và gắn `ddl_ref` (vd. `ux-guidelines.csv#22`, `web-interface.csv#39`). Mỗi item có citation và **ddl_ref** khi có rule khớp.

**Output:** Bổ sung vào `screen_inventory.screens[k]`:
- **ocr_round1_text**: mảng từ Round 1 (text đầy đủ theo ảnh): `[{ filename, text_content, lines?, source }]`.
- **ocr_round2_icons**: mảng từ Round 2 (icon + position): `[{ filename, description_or_label, position_zone, position_detail?, source }]`.
- **ocr_full_table**: mảng gộp: row từ Round 1 (`type: "text"`) + row từ Round 2 (`type: "icon"`, có `position_zone`, `position_detail?`), sau Bước 2 có thêm `matched_spec?`. Bắt buộc khi đã chạy OCR.
- `ocr_gaps`: `{ missing_text: [...], missing_components: [...] }` — chỉ các item **không** khớp spec (từ bảng ocr_full_table). Mỗi item có `source_image`, citation `ocr:{filename}`. Khi OCR không chạy hoặc fail: `ocr_gaps: null`.
- `ocr_full_text`: (tùy chọn, tương thích) tổng hợp toàn bộ text Round 1 theo từng ảnh (citation `ocr:{filename}`).
- `ocr_screen_context`: string mô tả ngắn ngữ cảnh màn hình (suy từ OCR + components).
- `ocr_ux_improvements`: mảng `[{ description_vi, source_image?, component_key?, citation, ddl_ref? }]`. `ddl_ref`: tham chiếu DDL (conventions § DDL reference) khi có rule khớp.

Spec thiếu từ OCR là COMPbase với citation `ocr:{filename}`. Subsection "Spec còn thiếu (phát hiện từ ảnh)" trong Section 3 **chỉ** xuất các dòng gap (từ ocr_gaps / từ ocr_full_table có matched_spec=N).

### Implementation 2g — Agent vision (2 round)

Với mỗi screen có `wireframe_images`, agent thực hiện **đủ hai round** bằng cách đọc ảnh từ path `screenshot_relative` (tool Read với path từ workspace root), rồi Bước 2–4. Sau khi hoàn thành mọi screen: ghi `{output_dir}/.handoff/.ocr_done`. Gate: Phase 3 chỉ chạy khi mọi screen có ảnh đều có `ocr_full_table` và file `.ocr_done` tồn tại.

**Chia lượt:** Mỗi lượt = **một biên màn hình** (một screen). Mỗi lượt thực thi **Round 1** rồi **Round 2** trên đúng tập PNG của biên đó; sau khi có kết quả đầy đủ (ocr_round1_text, ocr_round2_icons, ocr_full_table) mới chạy Bước 2–4 và gán vào `screen_inventory.screens[k]`. Lần lượt xử lý từng screen, rồi chuyển sang screen tiếp theo.

**Checklist thực thi (bắt buộc — không được chuyển Phase 3 nếu chưa hoàn thành cho mọi screen có ảnh):**

1. **Với từng screen `k` có `wireframe_images` không rỗng:**
   - **Round 1:** Đọc **tất cả** ảnh trong `wireframe_images[k]` tại path `workspace_root + "/" + screenshot_relative`. Trích xuất toàn bộ text → điền `ocr_round1_text` và thêm row `type: "text"` vào `ocr_full_table`. Mỗi row citation `ocr:{filename}`.
   - **Round 2:** Đọc lại **cùng tập ảnh** của screen k. Trích xuất toàn bộ icon và thông tin vị trí (position_zone, position_detail) → điền `ocr_round2_icons` và thêm row `type: "icon"` vào `ocr_full_table` (kèm position_zone, position_detail). Mỗi row citation `ocr:{filename}`.
   - **Bước 2–4:** Đối chiếu ocr_full_table với text_nodes và components (2b, 2b-bis) → ocr_gaps; suy luận ocr_screen_context và ocr_ux_improvements (DDL ref). Gán toàn bộ vào `screen_inventory.screens[k]`.
2. Sau khi hoàn thành **mọi** screen có ảnh: kiểm tra không còn screen nào có `wireframe_images` nhưng thiếu `ocr_full_table`. Ghi `{output_dir}/.handoff/.ocr_done` với nội dung `{"ocr_done": true, "at": "<ISO8601>"}`.

**Không được chuyển sang Phase 3 nếu chưa hoàn thành bước 1 cho mọi screen có ảnh.**

**Gate artifact (khi enable_ocr_reconciliation === true):** Sau khi hoàn thành bước 1 cho **mọi** screen có ảnh: tạo `{output_dir}/.handoff` nếu chưa có, ghi `{output_dir}/.handoff/.ocr_done`. Phase 3 chỉ chạy khi file này tồn tại.

### 2g-bis. OCR post-processing (khi đã có file .md hoàn chỉnh và ảnh trong ui/)

Áp dụng khi **đã có** feature .md với wireframe đã chèn ảnh (link `ui/xxx.png`), nhưng OCR (2g) chưa chạy hoặc cần chạy bổ sung. Không cần figma_raw/screen_inventory trong bộ nhớ — dùng .md và file ảnh trên disk.

**Phương pháp:** Agent đọc từng ảnh từ path (screenshot_relative), chạy **Round 1** (text) rồi **Round 2** (icon + vị trí), điền ocr_full_table (và ocr_round1_text, ocr_round2_icons nếu cần), rồi Bước 2–4 và cập nhật Section 3.

**Input:** Đường dẫn tới feature .md (vd. `{output_dir}/.../danh-bach-thu-huong.md`) hoặc thư mục `ui/` (vd. `{output_dir}/.../app/main/ui/`). Workspace root để resolve path.

**Bước thực hiện:**

1. **Thu thập danh sách ảnh:**  
   - Cách A: Parse file .md, regex tìm tất cả `!\[.*\]\(ui/([^)]+\.png)\)` → danh sách `filename`. Với mỗi filename, `screenshot_relative` = path từ workspace root tới file (vd. `co-op-bank-khcn/Co-op-Bank-KHCN/app/main/ui/contact.png`).  
   - Cách B: List file trong thư mục `ui/` (cùng thư mục với .md): `*.png` → filename; `screenshot_relative` = path từ workspace root tới từng file.  
   - Ghi mảng `wireframe_images`: `[{ "filename": "xxx.png", "screenshot_relative": "..." }]`.

2. **Điền ocr_full_table (2 round vision):**  
   Đọc từng file ảnh tại path `workspace_root + "/" + screenshot_relative`. **Round 1:** Trích xuất toàn bộ text → ocr_round1_text + row text vào ocr_full_table. **Round 2:** Trích xuất toàn bộ icon + vị trí → ocr_round2_icons + row icon (position_zone, position_detail) vào ocr_full_table.

3. **Bước 2–4 (logic giống 2g):** Đối chiếu → `ocr_gaps` (tập so sánh = text extract từ .md: bảng Mô tả màn hình, User Story, Section 1 User Flow; chuẩn hóa tương tự 2g). Suy luận `ocr_screen_context` và `ocr_ux_improvements` (conventions § DDL reference). Input từ .md + ảnh disk; không có screen_inventory trong bộ nhớ.

4. **Cập nhật file .md:**  
   Trong Section 3 Wireframe, theo thứ tự block (phase-3 § Section 3): thêm hoặc cập nhật **(a)** subsection **"### Kết quả OCR (toàn bộ)"** (bảng Ảnh | Loại | Nội dung | Vị trí | Đã khớp spec) từ ocr_full_table khi có; **(b)** **"### Spec còn thiếu (phát hiện từ ảnh)"** (chỉ các dòng gap từ bảng OCR, bảng/bullet, citation `ocr:{filename}`); **(c)** **"### Ngữ cảnh màn hình (từ OCR)"** khi có ocr_screen_context; **(d)** **"### Đề xuất cải thiện UX (từ OCR)"** khi có ocr_ux_improvements (bullet hoặc bảng, badge `🤖 by AI` | Nguồn: ocr + components | Độ tin cậy: Medium). Nếu subsection đã tồn tại thì merge/append, tránh trùng dòng. Format tham chiếu: Phase 3 § Section 3 Wireframe.

**Lưu ý:** Path `screenshot_relative` phải đúng từ workspace root. Nếu feature .md nằm trong `app/main/` và ảnh trong `app/main/ui/`, thì `screenshot_relative` = `{output_dir_relative}/app/main/ui/{filename}.png`.

## Output

```
screen_inventory = {           // design_data_layer: L2 (Advanced Figma); components[] và flow_graph feed vào L3 augmentation
  screens: [
    {
      screen_id: string,
      screen_name_vi: string,
      figma_node_id: string,
      screenshot_path: string,      // L1: absolute path to local .png
      screenshot_relative: string,  // for .md: path from workspace root to image in ui/, vd ".../section/ui/{slug}.png"; link trong .md = "ui/{filename}.png"
      wireframe_images: [           // danh sách ảnh có thứ tự cho Section 3 Wireframe; nguồn từ figma_raw (screenshot chính + sub_screenshots) + bước Alt assignment (Phase 2f)
        { filename: string,         // vd: "internal-transaction.png", "internal-transaction-2.png"
          screenshot_relative: string,
          alt_text: string }        // max 125 ký tự, tiếng Việt; dùng khi ghi .md: ![alt_text](ui/filename)
      ],
      components: [
        {
          stt: number,
          prd_type: string,
          component_key: string,
          component_group: string,
          description_vi: string,     // mô tả từ Figma context
          figma_layer_path: string,
          is_new_key: boolean
        }
      ],
      text_nodes: [
        { text: string, type: string, parent_component: string }
      ],
      design_spec_summary?: { gap_common?, padding_common?, border_radius_common?, has_fills? },  // optional; khi include_design_specs = true (2b-ter)
      ocr_round1_text?: [{ filename, text_content, lines?, source }],   // 2g Round 1; text đầy đủ theo ảnh
      ocr_round2_icons?: [{ filename, description_or_label, position_zone, position_detail?, source }],  // 2g Round 2; icon + vị trí
      ocr_full_table?: [{ filename, type, content_or_description, bbox?, source, matched_spec?, position_zone?, position_detail? }],  // 2g; type = "text" | "icon"; icon có position_zone, position_detail; matched_spec Y/N sau đối chiếu
      ocr_gaps?: { missing_text: [{ text_raw, normalized, source_image, bbox? }], missing_components: [{ description_vi, source_image }] },  // 2g; chỉ item không khớp từ ocr_full_table; mỗi item citation "ocr:{filename}"; null khi OCR không chạy
      ocr_full_text?: [{ filename, lines?, raw?, citation }],   // 2g; tùy chọn tương thích (tổng hợp Round 1)
      ocr_screen_context?: string,                              // 2g; ngữ cảnh màn hình suy từ OCR + components
      ocr_ux_improvements?: [{ description_vi, source_image?, component_key?, citation, ddl_ref? }]  // 2g; đề xuất cải thiện UX từ OCR; ddl_ref bắt buộc tham chiếu DDL để kết xuất/kết luận
    }
  ],
  // Row "Design element" (2b-bis): prd_type = Design element, component_key = design-element-{slug}, is_new_key = true.
  // Khi có Phase 2a-bis (multi-screen section): danh sách distinct screens để sinh nhiều .md per section
  // Schema canon + mở rộng: .cursor/docs/ddl/glossary.md § Screen boundaries schema
  screen_boundaries: [               // mỗi item = 1 file .md
    {
      screen_id: string,
      screen_name_vi: string,
      artboard_node_ids: [ string ],
      screen_type: string,           // form | confirm | result | list | detail | error (extensible)
      // optional: order?, variant_of?, tags?, source_anchor?
    }
  ]
}

flow_graph = {
  edges: [
    {
      from_screen: string,
      to_screen: string,
      action: string,
      evidence: string,   // "figma_prototype" | "button_text" | "nav_item" | "UNSPECIFIED"
      citation: string
    }
  ]
}

figma_context_registry = [
  {
    context_label: string,
    context_type: string,
    figma_source: string,
    screen_id: string,
    canonical_key: string,
    used_in: string
  }
]
```
