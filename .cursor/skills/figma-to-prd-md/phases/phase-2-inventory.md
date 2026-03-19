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

**⛔ Pre-Phase-3 Boundary Validation Gate (MANDATORY — không được bỏ qua):**

Agent **PHẢI** thực hiện đầy đủ 5 bước dưới đây và ghi kết quả vào `{output_dir}/.handoff/screen_boundaries.json` trước khi chuyển Phase 3. Phase 3 **KHÔNG ĐƯỢC** bắt đầu nếu file này chưa tồn tại.

**Bước 1 — Liệt kê tên artboard gốc:**
Từ `get_metadata()` XML, extract **chính xác** tên (`name` attribute) của mỗi top-level frame trong section. **Không** tự đặt tên, không phiên dịch, không suy luận — dùng đúng string từ XML.

**Bước 2 — Nhóm theo tên Figma (exact string match):**
Group artboards theo tên chính xác (case-sensitive). Các artboard cùng tên = candidates cho cùng biên.

| Tên Figma (exact) | Node IDs | Dims | Count |
|---|---|---|---|
| `{tên}` | `[{ids}]` | `{w×h, w×h}` | `{N}` |

**Bước 2.5 — Extract icon fingerprint per artboard (CÙNG metadata, KHÔNG cần API call thêm):**

Từ **cùng file metadata XML** đã dùng ở Bước 1, extract tất cả frames có `name` bắt đầu bằng `ic_`, `back_`, `drop_`, `switch`, `arrow_` với `width ≤ 48` và `height ≤ 48`. Đây là icon elements.

```
Với mỗi artboard → icon_fingerprint = sorted(set(icon_names))
```

| Artboard | Icon Fingerprint | Icon Count |
|---|---|---|
| `{node_id}` | `[ic_contact, ic_money_tit, switch, ...]` | `{N}` |

**Flow-stage signals từ icon fingerprint:**

| Signal | Rule | Flow Stage |
|:---|:---|:---|
| `ic_backhome` present | Terminal screen — chỉ có nút về home | **Kết quả** |
| Icon count ≤ 2 (chỉ `back_white`, `drop_blue`) | Stripped UI — review/auth screen | **Xác nhận** |
| `ic_contact` + `switch` + (`ic_human_tit` hoặc `ic_money_tit`) | Rich form elements + trigger icons | **Khởi tạo** |

**Bước 2.6 — Overlay Structure Detection (BẮT BUỘC — chạy SAU 2.5, TRƯỚC Bước 3):**

Phát hiện artboard nào là **overlay/bottomsheet** chồng lên screen cha. Dùng **3 structural signals** (KHÔNG dùng text/icon content — dù content khác):

| # | Signal | Cách kiểm tra | Nếu TRUE → gộp vào biên cha |
|:---|:---|:---|:---|
| S1 | **Artboard name identity** | Artboard X có cùng `name` attribute (exact string) với artboard Y đã được classify là biên cha | Cùng tên = cùng screen. Figma designer coi X là state/variant của Y |
| S2 | **Base layer presence** | Trong XML, artboard X chứa **cả** base screen layer (form fields, header, btn_main) **bên dưới** overlay layer | Base form vẫn visible = overlay chồng lên, KHÔNG navigate-away |
| S3 | **Z-order overlay pattern** | Node overlay (danh bạ panel, ngân hàng picker, OTP sheet) nằm **SAU** base form node trong XML (z-index cao hơn = render on top) | Node sau = z-index cao hơn = overlay/bottomsheet |

**Rule:** Nếu artboard X thỏa **≥2 trong 3 signals** → X là **overlay state**, PHẢI gộp vào biên cha (artboard Y). KHÔNG tách biên riêng.

**Cách thực hiện:**

```
Với mỗi artboard X trong section:
  1. Kiểm tra S1: Tìm artboard(s) Y cùng tên Figma (exact match)
     → Nếu tìm được: S1 = TRUE
  2. Kiểm tra S2: Trong XML tree của X, tìm child nodes:
     → Nếu có ≥2 sibling groups lớn (>50% artboard height):
       - Group đầu tiên (base): chứa form fields / header / btn_main
       - Group sau (overlay): chứa content khác (danh sách, search bar, picker)
       → S2 = TRUE
  3. Kiểm tra S3: Node overlay nằm SAU node base trong XML sibling order
     → S3 = TRUE
  4. Nếu (S1 + S2 + S3) ≥ 2:
     → Gán X.overlay_of = Y.artboard_id
     → X sẽ được gộp vào biên chứa Y ở Bước 4
```

**Output per artboard (append vào icon fingerprint table):**

| Artboard | S1 (name) | S2 (base layer) | S3 (z-order) | overlay_of | Decision |
|:---|:---:|:---:|:---:|:---|:---|
| CTNTK_1 | — | — | — | — | Base screen |
| CTNTK_2 | ✅ cùng tên | ✅ form dưới, danh bạ trên | ✅ danh bạ sau form | CTNTK_1 | **Overlay → gộp** |
| ... | | | | | |

**Anti-pattern (lỗi thực tế — CASE STUDY):**
- ❌ Artboard "Danh bạ thụ hưởng" có TEXT khác ("Tìm kiếm", tên contacts) và ICON khác (`ic_search_grey`) so với form → agent phân tách thành biên riêng
- ✅ Nhưng cùng artboard name + base form visible bên dưới + overlay z-order → ĐÂY LÀ OVERLAY STATE, không phải separate screen
- **Nguyên tắc:** Structural signals (S1-S3) **OVERRIDE** content signals (text, icon) khi phân tách biên. Content khác ≠ Screen khác nếu structure cho thấy overlay.

**Lưu ý:**
- Icon fingerprint **tương tự** artboard khác trong cùng section → Cùng flow stage — candidate sub-screen → Cùng biên cha
- Icon fingerprint là **signal bổ sung**, không override text-based heuristic
- Khi text nói "Xác nhận giao dịch" VÀ icon stripped → confirm confidence cao
- Khi text nói "Danh bạ thụ hưởng" NHƯNG icon fingerprint ~= form screen → sub-screen của Khởi tạo, KHÔNG phải biên riêng

**Bước 3 — Áp dụng Heuristic theo thứ tự ưu tiên:**

Với mỗi nhóm trong bảng Bước 2, kết hợp **text patterns + icon fingerprint + overlay structure (Bước 2.6)**:

**3.0 Flow-stage classification (top-down, domain-aware) + Overlay enforcement:**
- Xác định domain flow pattern (vd: `banking_transfer` → 3 stages: Khởi tạo/Xác nhận/Kết quả)
- Dùng icon fingerprint signals + text keywords để classify mỗi artboard vào flow stage
- Artboards cùng flow stage = candidates cho cùng biên (hoặc parent-child trong biên)
- **⚠️ Overlay enforcement (BẮT BUỘC — từ Bước 2.6):** Nếu artboard X có `overlay_of = Y` → X **PHẢI** gộp vào biên chứa Y, **BẤT KỂ** text/icon content khác nhau. Overlay detection (Bước 2.6) **OVERRIDE** content-based heuristic (3.1-3.3)
- **Sub-screen detection (legacy — vẫn giữ nhưng Bước 2.6 ưu tiên hơn):** Artboard có `back_white` + icon fingerprint tương tự artboard khác → sub-screen, gộp vào biên cha

**3.1** **Tên artboard khác biệt** (Count = 1 trong Bước 2) → xem flow-stage: nếu cùng stage với artboard khác → **gộp vào biên cùng stage**, không tách riêng

**3.2** **Count > 1, cùng tên:**
   - Nếu `screen_type` khác nhau → kiểm tra flow-stage trước khi tách
   - Nếu `screen_type` giống → variant cùng biên (gộp `artboard_node_ids[]`)

**3.3** **Tên có suffix `/state`** → extract base name, gộp vào biên base name

**Bước 4 — Output `screen_boundaries` array:**
Mỗi item bắt buộc: `screen_id`, `screen_name_vi`, `artboard_node_ids[]`, `screen_type`, `variant_artboards[]` (tên + node_id + lý do gộp).

**Bước 5 — Self-check (4 assertions, tất cả phải PASS):**
1. `screen_boundaries.length > 0` — không rỗng
2. `sum(artboard_node_ids across all boundaries) === total top-level frames in section` — không artboard nào bị bỏ sót
3. `set(artboard_node_ids).size === sum(artboard_node_ids.length)` — không artboard nào bị gán vào 2 biên
4. Với mỗi `boundary_annotations[k]` có `inferred_target`: target screen PHẢI tồn tại trong `screen_boundaries` — nếu không → warning `TRIGGER_TARGET_MISSING` (không hard-fail, vì Phase 2d có thể suy luận sai)

Ghi kết quả 5 bước + 4 assertions vào `{output_dir}/.handoff/screen_boundaries.json`. **Nếu assertion 1-3 FAIL → dừng pipeline**, không chuyển Phase 3. Assertion 4 là warning, không dừng.

### 🛑 HUMAN_CHECKPOINT — Boundary Preview (SAU Boundary Gate PASS)

**⚠️ AGENT: DỪNG TẠI ĐÂY. Hiển thị toàn bộ kết quả suy luận biên và CHỜ user xác nhận.**

**MUST SHOW — Bảng 1: Screen Boundaries**
| # | screen_id | screen_name_vi | type | artboards |
|---|-----------|---------------|------|-----------|
| 1 | SCR-XXX-001 | {tên Figma gốc} | form | 2 |
| ... | | | | |
| Tổng | | {N} biên, {M} artboards | | |

**MUST SHOW — Bảng 2: Chi tiết artboards per biên**
- Liệt kê từng artboard: tên Figma gốc, node_id, kích thước, lý do gộp (nếu variant)

**MUST SHOW — Bảng 3: Boundary Gate Assertions**
- 4 assertion results (✅/❌/⚠️)

**Hỏi user:**
> - **[Y] Đúng** → tiếp tục Phase 2b
> - **[N] Sai** → dừng, user chỉ ra lỗi
> - **[E] Chỉnh sửa** → user mô tả merge/split, agent sửa rồi show lại

**CHỜ user trả lời. KHÔNG tiếp tục Phase 2b/2c/2c-bis cho đến khi user chọn [Y].**

**Anti-pattern (lỗi đã xảy ra — KHÔNG ĐƯỢC lặp lại):**
- ❌ Nhóm artboard theo "feature group" (vd: gộp 4 login screens vào 1 file)
- ❌ Dùng số file PRD đang mở trong editor làm nguồn cho số .md
- ❌ Tự đặt tên biên khác với tên Figma gốc (trừ khi normalize kebab-case)
- ❌ Bỏ qua Bước 1-5 và đi thẳng Phase 3 dựa trên "hiểu biết chung" về Figma
- ❌ Pass Boundary Gate rồi tiếp tục luôn mà không show cho user
- ❌ Chỉ show count tổng ("6 biên") mà không show chi tiết từng biên
- ❌ **OVERLAY-AS-SCREEN (Case study 2026-03-17):** Tách overlay/bottomsheet (danh bạ, chọn NH, OTP input) thành biên riêng khi artboard chứa cả base form layer bên dưới. **FIX:** Luôn chạy Bước 2.6 (Overlay Structure Detection) và enforce overlay_of merge trước Bước 3. Content signals (text ≠, icon ≠) KHÔNG override structural signals (cùng tên, base layer present, z-order overlay)
- ❌ Bỏ qua Bước 2.6 hoặc chỉ dùng text/icon để phân biệt biên mà không check structural signals

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

## 2c-bis. Icon Extraction — Pipe 1 (deterministic, cheap)

**Mục đích:** Extract icon inventory per screen **trước** flow inference (2d), để 2d có thêm signal cho agent reasoning.

**Phương pháp — Figma metadata grep (primary):**
- Từ `get_metadata()` XML đã có (Phase 1), grep tất cả `<frame>` nodes có naming convention icon:
  - Pattern: `name` starts with `ic_`, `drop_`, `switch`, `back_`, `clear_`, `btn_`, `close`, `arrow_`, `check_`, `logo_`
  - Hoặc: `width <= 48 AND height <= 48` (kích thước icon chuẩn mobile)
- Với mỗi icon match, ghi: `icon_name`, `figma_node_id`, `x`, `y`, `width`, `height`, `parent_screen_id`

**Phương pháp — Agent vision (fallback, khi metadata thiếu):**
- Nếu screen có `wireframe_images` mà metadata grep chỉ phát hiện ≤1 icon → agent đọc ảnh để bổ sung icons có tên generic (VD: `Group 12345` nhưng vision thấy là icon danh bạ)
- Khi dùng vision fallback, ghi `source: "vision"` thay vì `source: "metadata"`

**Output per screen:** `icon_inventory[]` — flat list, **KHÔNG có inference** (chưa suy luận trigger):
```json
[
  {
    "icon_name": "ic_contact",
    "figma_node_id": "22:5517",
    "x": 335, "y": 299,
    "width": 24, "height": 24,
    "parent_screen_id": "SCR-CTNTK-001",
    "source": "metadata"
  }
]
```

**Ràng buộc:**
- Phase 2c-bis là **extraction only** — không có reasoning, không có inference
- Agent KHÔNG suy luận trigger, target, interaction_type ở bước này
- Tốc độ: nhanh (grep trên data đã có), không tốn thêm API call

**⚠️ Gate D: Icon Inventory Validation (WARNING — sau Phase 2c-bis, trước 2d):**

Agent tự kiểm tra trước khi vào Phase 2d:
1. Mỗi icon phải có: `icon_name`, `figma_node_id`, `parent_screen_id`
2. Không có duplicate `figma_node_id` — nếu có → log warning + dedupe
3. Nếu tổng icons = 0 across ALL screens → warning `ICON_EMPTY_ALL` (không hard-fail)
4. Log số icons per screen vào output

**MUST SHOW:** Agent PHẢI hiển thị bảng số icons per screen:
```
Gate D Results:
| Screen | Icons | Categories |
|--------|------:|------------|
| SCR-XX | 12    | trigger:5, nav:3, decoration:4 |
...
Total: {N} icons, {M} screens. Gate D: PASS/WARN
```

> **📌 Xả context:** Sau Gate D, chỉ giữ `icon_inventory[]` summary (per screen counts). Raw metadata XML có thể xả nếu đã extract xong text_nodes + icon_inventory.

## 2d. Navigation flow inference (mở rộng: icon-augmented agent reasoning)

Phase 2d gồm **3 sub-steps** theo thứ tự:

### 2d.1 Text-based flow inference (giữ nguyên)

- Scan text nodes cho pattern: "Tiếp tục", "Quay lại", "Xác nhận", navigation labels
- Scan bottom-bar items → link giữa screens
- Scan button actions → suy luận screen transitions
- Nếu Figma có prototype links (từ design_context): dùng trực tiếp
- COMPbase khi có Figma evidence; UNSPECIFIED khi suy luận
- Output: `text_flow_edges[]`

### 2d.2 Icon-augmented trigger inference — Pipe 2 (agent reasoning)

**Mục đích:** Agent suy luận mỗi icon (từ 2c-bis `icon_inventory`) có khả năng trigger mở screen khác không.

**Method: AGENT REASONING — không phải lookup table.**

Với mỗi screen A trong `screen_boundaries`:
  Với mỗi icon trong `A.icon_inventory`:

1. **Agent NHÌN context:**
   - `icon.icon_name` + `icon.position (x,y)` + `icon.size`
   - `adjacent_text_nodes[]` — text nodes gần icon (trong bán kính ~100px hoặc cùng parent group)
   - `A.screen_type` + `A.components[]`
   - Danh sách `screen_boundaries` cùng section

2. **Agent SUY LUẬN (reasoning prompts — hướng dẫn, KHÔNG bắt buộc theo):**
   > "Icon `{name}` ({w}×{h}) tại vị trí ({x},{y}), bên cạnh text `{adjacent}` trong screen `{A.screen_type}`.
   > Trong section này có các screens: `{list B, C, D...}` với titles `{...}`.
   > → Icon này có khả năng trigger mở screen nào?
   > → Interaction type: overlay / push / modal / inline_dropdown / none?
   > → Confidence: high / medium / low?
   > → Reasoning?"

3. **Agent OUTPUT per icon:**
   ```json
   {
     "icon_name": "ic_contact",
     "source_screen": "SCR-CTNTK-001",
     "inferred_target": "SCR-CTNTK-002",   // hoặc null nếu không trigger screen mới
     "interaction_type": "overlay",          // overlay | push | modal | inline_dropdown | none
     "confidence": "high",                  // high | medium | low
     "reasoning": "ic_contact nằm bên phải field 'TK thụ hưởng'. Cùng section có screen 'Danh bạ thụ hưởng' (list_picker). Pattern: contact icon bên cạnh input field → mở picker overlay.",
     "evidence": "icon_trigger_inference"
   }
   ```

4. **Agent CÓ QUYỀN:**
   - ✅ Phát hiện icon không tên chuẩn (dùng vision check)
   - ✅ Ghi `"inferred_target": null` khi không tìm được target
   - ✅ Ghi `"confidence": "low"` khi không chắc
   - ✅ Override pattern phổ biến khi context khác biệt
   - ✅ Suy luận CTA button triggers ("Xác nhận" → OTP) — cross-reference với 2d.1
   - ✅ Ghi reasoning log giải thích quyết định

5. **Agent KHÔNG ĐƯỢC:**
   - ❌ Bỏ qua icon mà không ghi reasoning (phải ghi ít nhất `"confidence": "low", "reasoning": "..."` hoặc `"inferred_target": null, "reasoning": "..."`)  
   - ❌ Dùng lookup table cứng — phải suy luận từ context thực tế

Output: `icon_trigger_edges[]`

### 2d.3 Boundary annotation (agent reasoning — constrained)

**Mục đích:** Dựa trên `icon_trigger_edges` từ 2d.2, annotate thêm metadata vào `screen_boundaries` (từ 2a-bis).

**Ràng buộc quan trọng:**
- Agent **CHỈ ĐƯỢC annotate** (thêm metadata) — **KHÔNG ĐƯỢC restructure** boundaries (không merge, không split, không xóa)
- Chỉ annotate khi `confidence >= "medium"`
- Mỗi annotation PHẢI có reasoning log

**Output:** `boundary_annotations[]` — tách riêng file, KHÔNG overwrite `screen_boundaries`:
```json
[
  {
    "screen_id": "SCR-CTNTK-002",
    "boundary_type": "overlay",           // overlay | sub_screen | modal
    "triggered_by": "SCR-CTNTK-001",
    "trigger_icon": "ic_contact",
    "confidence": "high",
    "reasoning": "Screen 'Danh bạ thụ hưởng' (list_picker) triggered by ic_contact in form. Evidence: icon position bên cạnh field 'TK thụ hưởng', screen title match 'Danh bạ'."
  }
]
```

Sau khi hoàn tất, ghi `boundary_annotations` vào `{output_dir}/.handoff/screen_boundaries.json` (append vào file đã có từ 2a-bis, field mới `boundary_annotations[]`).

### 2d.4 Flow graph finalization

- Merge `text_flow_edges` (2d.1) + `icon_trigger_edges` (2d.2)
- Dedupe edges (cùng from + to + action → giữ edge có confidence cao hơn)
- Output: `flow_graph` (directed edges giữa screens)

**Anti-pattern:**
- ❌ Chỉ dùng text-based flow mà bỏ qua icon triggers
- ❌ Dùng icon trigger lookup table thay vì agent reasoning
- ❌ Annotate boundary mà không ghi reasoning log
- ❌ Restructure (merge/split) boundaries ở Phase 2d — boundaries chỉ được sửa ở 2a-bis

**⛔ Gate E: Flow Graph Validation (MANDATORY — sau 2d.4, trước 2e):**

Agent tự kiểm tra trước khi chuyển Phase 2e:
1. `flow_graph.edges.length > 0` — phải có ≥1 edge (WARNING nếu 0 — có thể single-screen section)
2. Mọi `from_screen` và `to_screen` phải tồn tại trong `screen_boundaries` — **HARD-FAIL** nếu vi phạm (orphan reference)
3. Không có self-loops (`from_screen === to_screen`) — WARNING
4. Icon-inferred edges (`evidence = "icon_trigger_inference"`) PHẢI có `trigger_icon` + `confidence` — **HARD-FAIL** nếu thiếu
5. Coverage: ≥50% screens phải xuất hiện trong ít nhất 1 edge — WARNING nếu không đạt

Ghi `flow_graph.json` vào `{output_dir}/.handoff/flow_graph.json`. **Nếu assertion 2 hoặc 4 FAIL → dừng**, sửa lỗi trước khi tiếp tục.

**MUST SHOW:** Agent PHẢI hiển thị kết quả từng assertion:
```
Gate E Results:
✅ 1. edges.length = {N} (> 0)
✅ 2. All from/to screens exist in boundaries
✅ 3. No self-loops
✅ 4. Icon edges have trigger_icon + confidence
⚠️ 5. Coverage: {X}% ({Y}/{Z} screens)
Gate E: PASS/FAIL
```

> **📌 Xả context:** Sau Gate E, xả `icon_inventory` raw list và icon reasoning intermediate. Giữ lại: `icon_trigger_edges`, `boundary_annotations`, `flow_graph`.

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
  icon_inventory?: [                  // 2c-bis; flat list per screen, extraction only
    {
      icon_name: string,
      figma_node_id: string,
      x: number, y: number,
      width: number, height: number,
      parent_screen_id: string,
      source: string                 // "metadata" | "vision"
    }
  ],
  screen_boundaries: [               // mỗi item = 1 file .md
    {
      screen_id: string,
      screen_name_vi: string,
      artboard_node_ids: [ string ],
      screen_type: string,           // form | confirm | result | list | detail | error (extensible)
      // optional: order?, variant_of?, tags?, source_anchor?
    }
  ],
  boundary_annotations?: [           // 2d.3; agent reasoning output, tách riêng từ boundaries
    {
      screen_id: string,
      boundary_type: string,         // overlay | sub_screen | modal
      triggered_by: string,          // screen_id của parent
      trigger_icon?: string,         // icon_name triggered mở screen này
      confidence: string,            // high | medium | low
      reasoning: string              // bắt buộc — agent phải giải thích
    }
  ]
}

flow_graph = {
  edges: [
    {
      from_screen: string,
      to_screen: string,
      action: string,
      evidence: string,   // "figma_prototype" | "button_text" | "nav_item" | "icon_trigger_inference" | "UNSPECIFIED"
      citation: string,
      trigger_icon?: string,         // 2d.2; icon_name if trigger is icon-based
      interaction_type?: string,     // 2d.2; overlay | push | modal | inline_dropdown
      confidence?: string            // 2d.2; high | medium | low (chỉ cho icon-inferred edges)
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
