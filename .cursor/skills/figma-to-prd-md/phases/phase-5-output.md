# Phase 5: Output .md Pack

**Tham chiếu:** `conventions.md` (Image Path Convention + Output Structure); `reference/citation-quality.md` (Citation Rules + Quality Gates + UI Automation Readiness).

## Mục tiêu

Sinh cây file .md cuối cùng, validate, sẵn sàng cho prd-full-pipeline v3.

## 5a. Sinh cây file

Theo **Output Structure** trong `conventions.md`. Tóm tắt:

**Khi `output_structure = section_folder` (mặc định):**
- Mỗi distinct screen = 1 file .md trong folder section; ảnh trong `ui/`. Path feature: `{output_dir}/{file_name}/{page}/{section}/{screen-slug}.md`.

**Khi `output_structure = flat`:** Overview + feature .md tại output_dir; ảnh vẫn tại `{output_dir}/{file_name}/{page}/{section}/ui/` (link trong .md: `ui/xxx.png`).

Ví dụ cây thư mục đầy đủ: `conventions.md` § Output Structure.

## 5a-verify. Kiểm tra screenshot files

Path và link ảnh: theo **Image Path Convention** trong `conventions.md`. Verify file .png tồn tại trước khi ghi .md; thiếu → warning trong Wireframe + UNSPECIFIED summary. Alt: mỗi ảnh có `alt_text` trong `wireframe_images[]` (Phase 2f); không sinh lại khi ghi .md (1:1 với filename).

## 5b. File naming convention

Overview: `{output_dir}/{file_name}/{product-slug}-overview.md` (section_folder) hoặc `{output_dir}/{product-slug}-overview.md` (flat). Feature: theo **Output Structure** trong `conventions.md` — `{section}/{screen-slug}.md`. Slug: kebab-case, bỏ dấu tiếng Việt.

## 5c. Internal links

Overview link feature: `./{page}/{section}/{screen-slug}.md`. Feature link ảnh: theo **Image Path Convention** trong `conventions.md`. Flat: overview `./{screen-slug}.md`; feature link ảnh relative từ output_dir.

## 5d. Validation (pre-output)

Load `reference/citation-quality.md` § Quality Gates cho gate cơ bản (structure, COMPbase citation, UNSPECIFIED, AI badge completeness, Alt text format). **Gate bổ sung đặc thù pipeline** (bảng dưới):

| Gate | Condition | Action nếu fail |
|------|-----------|------------------|
| Screen boundary ready | `screen_boundaries` hoặc `feature_file_plan` hợp lệ (theo phase-2 § 2a-bis Determinism rule) | `allow_section_fallback=false` → fail `SCREEN_BOUNDARY_MISSING`; `true` → ghi warning `SCREEN_BOUNDARY_FALLBACK_USED` |
| Structure complete | Mỗi feature file có đủ 5 section | Sinh section trống với UNSPECIFIED |
| User Flow populated | Ít nhất 1 flow per feature file | Sinh flow từ default screen → next screen |
| Wireframe complete | Mỗi feature có screenshot .png đã tải + bảng Mô tả | Verify file tồn tại trong `{section}/ui/{filename}.png` (section_folder) hoặc `screenshots/{slug}.png` (flat). Nếu thiếu → ghi placeholder warning trong .md |
| Screen parity | `count(overview mục 3) = count(overview mục 8) = count(feature .md files)` | Fail `SCREEN_PARITY_MISMATCH`, ghi chi tiết lệch count |
| US numbering | Mã US liên tục, không trùng | Auto-increment global counter |
| Citation coverage | COMPbase rows có citation figma:* | Ghi warning cho rows thiếu citation |
| UNSPECIFIED count | Đếm tất cả UNSPECIFIED markers | Report trong overview |
| **AI badge count** | Đếm tất cả `🤖 by AI` blockquote blocks | Report tổng số AI proposals trong overview |
| **AI badge citation** | Mọi `🤖 by AI` block có Nguồn + Độ tin cậy | Ghi warning cho blocks thiếu citation |
| **Screenshot files** | Mọi ảnh link trong .md tồn tại trên disk | List missing files trong overview summary |
| **OCR (bắt buộc)** | Với mỗi screen có ảnh trong `wireframe_images`, Phase 2 phải đã chạy OCR bằng **agent vision** (2 round: text + icon+vị trí). Nếu OCR chạy thành công: mỗi feature file có `ocr_gaps` (subsection Spec còn thiếu có dữ liệu hoặc xác nhận không có gap), và có thể có `ocr_screen_context`, `ocr_ux_improvements`. |
| **Alt text** | Mỗi ảnh có alt non-empty; length ≤ 125 ký tự; không trùng chuỗi alt giữa các ảnh khác nhau (trong cùng feature file) | Ghi warning trong overview/UNSPECIFIED summary; không chặn xuất file |
| **Component coverage (bao gồm design elements)** | Đếm số row trong Mô tả màn hình so với số node visible trong Figma (ước lượng); design elements từ 2b-bis tính vào coverage | Ghi chú trong overview/quality summary; không chặn xuất |

### Pre-output OCR check (bắt buộc khi enable_ocr_reconciliation === true)

**Thực hiện trước khi ghi bất kỳ file .md nào.** Khi `enable_ocr_reconciliation === true`:

1. Với mọi screen có `wireframe_images` không rỗng: kiểm tra `screen_inventory.screens[k]` có tồn tại `ocr_full_table` và là mảng (có thể rỗng nếu ảnh không có text/icon, nhưng phải có sau khi đã chạy 2 round vision).
2. Nếu có ít nhất một screen có ảnh mà **không** có `ocr_full_table` (hoặc null/undefined): **không được ghi .md pack**; báo mã `OCR_GATE_FAILED`, liệt kê screen_id/screen_name thiếu, và dừng Phase 5. Gợi ý: "Phase 2g chưa chạy đủ 2 round vision cho mọi screen có ảnh; xem phase-2-inventory.md § 2g (Round 1 + Round 2) và § Implementation 2g checklist."

Bước này bắt buộc; không được ghi file .md khi OCR gate fail.

### Gate A — Pipeline Readiness (cho prd-full-pipeline)

Khi chuẩn bị cho prd-full-pipeline v3, đảm bảo:

| Gate | Condition | Action nếu fail |
|------|-----------|------------------|
| 5 section | Mỗi feature file có đủ 5 section | Sinh section trống với UNSPECIFIED |
| Wireframe links | Link ảnh wireframe tồn tại trên disk | List missing trong summary; pipeline có thể fallback |
| US numbering | Mã US không trùng | Auto-increment / warning |
| COMPbase citation | COMPbase rows có citation | Ghi warning |
| Structured handoff (optional) | Nếu bật: `.handoff/*.json` hợp schema `figma-prd-handoff-v1` | Không ghi `.handoff/`; vẫn xuất .md pack |

Sau khi pass 5d, có thể ghi `.handoff/screen_inventory.json`, `flow_graph.json`, `figma_context_registry.json`, `handoff-manifest.json` (khi bật structured handoff).

## 5e. UNSPECIFIED + AI Proposals Summary

Cuối overview file, thêm **2 section riêng biệt**:

```markdown
---

## Các mục cần bổ sung (UNSPECIFIED)

Danh sách các mục hoàn toàn trống — cần BA/PM bổ sung:

| # | File | Section | Mục | Lý do |
|---|------|---------|-----|-------|
| 1 | overview | 6. Success Metrics | Toàn bộ | Không có trong Figma, không đủ dữ liệu để suy luận |
| ... | ... | ... | ... | ... |

---

## Tổng hợp nội dung AI đề xuất (🤖 by AI)

Danh sách tất cả nội dung do AI sinh — cần review trước khi chốt PRD.

Thứ tự hiển thị **theo đúng cấu trúc tài liệu gốc**: Overview sections (1→8) trước, sau đó Feature files theo thứ tự trong bảng "Cấu trúc tài liệu PRD", mỗi feature file liệt kê theo thứ tự sections (1→5).

### Overview

| # | Section | Loại đề xuất | Độ tin cậy | Nguồn |
|---|---------|-------------|-----------|-------|
| 1 | 1. Chân dung khách hàng | Persona đề xuất | Medium | search.py + case study |
| 2 | 2. Tổng quan sản phẩm | Đơn vị tham khảo | Medium | case study |
| 3 | 4. Phạm vi sản phẩm | Out of Scope đề xuất | Low | case study |
| 4 | 6. Success Metrics | Metrics đề xuất | Low | search.py --domain product |

### {feature-1-slug}.md

| # | Section | Loại đề xuất | Độ tin cậy | Nguồn |
|---|---------|-------------|-----------|-------|
| 1 | 1. User Flow | Luồng error recovery | Medium | ux-guidelines.csv#10 |
| 2 | 1. User Flow | Luồng back navigation | Medium | web-interface.csv#3 |
| 3 | 2. User Story | US accessibility | High | web-interface.csv#1 |
| 4 | 2. User Story | AC bổ sung touch target | High | ux-guidelines.csv#22 |
| 5 | 2. User Story | UX copy (error/empty/retry) | High | ux-guidelines.csv#10 |
| 6 | 3. Wireframe | Icon recommendation | Medium | icons.csv |
| 7 | 4. Thiết kế Database | Schema INFERRED | High | figma_inferred |
| 8 | 5. NFR | Bảo mật bổ sung | Medium | case study |
| 9 | 5. NFR | Hiệu năng bổ sung | High | ux-guidelines.csv |
| 10 | 5. NFR | Trải nghiệm bổ sung | High | frontend-design |

### {feature-2-slug}.md
(cùng format...)

---

**Thống kê:**
- Tổng số `🤖 by AI` blocks: {N}
- High confidence: {N1} | Medium: {N2} | Low: {N3}
- Nguồn: Case study ({N_cs}) | CSV ({N_csv}) | search.py ({N_sp}) | INFERRED ({N_inf})
```

## 5f. Phase Report

Sau 5e, thu thập số liệu từ các phase (figma_raw, screen_inventory, feature_file_plan, output files đã ghi) và ghi **Phase Report** vào **cuối overview file** dưới dạng section: `## Kết quả chạy pipeline (Phase Report)`. Mục đích: mỗi lần skill chạy xong có báo cáo ngắn gọn kết quả từng phase (0→5).

**Nguồn số liệu:** Các biến/object đã có sau khi chạy Phase 0–5 (section_list, figma_raw, screen_inventory, flow_graph, feature_file_plan, danh sách file .md đã ghi, kết quả validation 5d).

**Nội dung Phase Report (theo phase):**

| Phase | Nội dung báo cáo |
|-------|-------------------|
| **Phase 0** | Đã chạy hay bỏ qua (node = section thì bỏ qua). Nếu chạy: số section trong `section_list`, scope (ALL / SELECTED / BATCH). |
| **Phase 1** | `file_key`, `node_id`; số screen/frame; số ảnh đã lưu (screenshot_path non-null); có variables hay không. |
| **Phase 2** | Số screen trong `screen_inventory`; có `screen_boundaries` không (và số item nếu có); tổng số component (mapped + Design element) — per screen hoặc tổng; có `design_spec_summary` (Nhóm B) cho màn nào không; **OCR: đã chạy 2 round vision (text, icon+vị trí) cho N màn có ảnh**; **ocr_gaps: X màn có gap** (khi OCR thành công); **ocr_screen_context / ocr_ux_improvements: đã sinh cho M màn**. Số edge trong `flow_graph`. |
| **Phase 3** | Số file trong `feature_file_plan`; số overview + feature file sẽ ghi. |
| **Phase 4** | Đã áp dụng augment (case study, CSV, frontend-design) hay không; có thể ước lượng số badge đã chèn (không bắt buộc). **Phase 4e (Suy luận UX — bắt buộc):** đã gọi ux-signal-inference cho N màn (theo biên màn hình, scope=screen, payload đầy đủ); skill đã call DDL on demand; số flow/component row đã merge (kèm ddl_ref). |
| **Phase 5** | Số file .md đã ghi; validation (pass / warning / fail) tóm tắt; path `output_dir`. |

**Format trong overview:** Markdown bảng hoặc list; đặt ngay sau phần "Tổng hợp nội dung AI đề xuất" (và thống kê), trước footer `*Generated by VNPAY Agentic Framework*`. Ví dụ:

```markdown
---

## Kết quả chạy pipeline (Phase Report)

| Phase | Kết quả |
|-------|---------|
| 0 | Bỏ qua (node section). |
| 1 | file_key: xxx, node_id: xxx; 3 screens; 15 ảnh lưu; variables: có. |
| 2 | 3 screens; screen_boundaries: 3; components tổng: 42; design_spec_summary: không; OCR: đã chạy 2 round vision (text, icon+vị trí) cho 3 màn có ảnh; ocr_gaps: 1 màn có gap; ocr_screen_context/ocr_ux_improvements: đã sinh cho 3 màn; flow_graph: 5 edges. |
| 3 | feature_file_plan: 3; 1 overview + 3 feature files. |
| 4 | Augment: case study + CSV + frontend-design. **4e Suy luận UX (bắt buộc):** đã gọi ux-signal-inference cho N màn (scope=screen); M flow/row đã merge (ddl_ref). |
| 5 | 4 file .md đã ghi; validation: pass; output_dir: MarkdownSV/1/co-op-bank-khcn. |
```
