---
name: ux-signal-inference
description: "Skill dùng chung — suy luận UX tiềm ẩn từ text + ngữ cảnh + icon (pattern registry + DDL on demand). Dùng từ figma-to-prd-md (Phase 4e), prd-full-pipeline, review-ux, comp-extraction, hoặc standalone. Hỗ trợ workflow Improve UX (comparison mockups, đề xuất cải thiện, merge vào PRD) khi dùng standalone hoặc từ handoff. Áp dụng mọi ngành; mở rộng bằng data/text-signals-{domain}.json. Hỗ trợ scope=screen để suy luận trong giới hạn biên màn hình."
---

# UX Signal Inference

Suy luận UX tiềm ẩn (flow, component, state) từ text trên frame/screen và registry pattern (generic + domain). Output: tags_only | report_md | inferred_ux (JSON) | prd_extension (cho consumer cần merge PRD, đã gồm ddl_ref khi DDL khớp).

## When to Apply

- Cần infer flow/component/state từ text signal (vd. "Xóa (3)", "Chọn danh bạ muốn xóa") trên một màn hình.
- Consumer có dữ liệu theo biên màn hình (figma-to-prd Phase 4e, handoff screen_inventory) và cần đề xuất cải thiện UX có căn cứ.
- Review-ux, comp-extraction, prd-full-pipeline cần tag hoặc inferred_ux từ text.

## Input Contract

Mọi consumer phải truyền đủ theo khả năng. Khi `scope = screen`, toàn bộ input (text_list, context_hint, ocr_icons) phải thuộc **cùng một biên màn hình**.

| Tham số | Bắt buộc | Mô tả | Nguồn từ figma-to-prd (Phase 4e) |
|---------|----------|-------|-----------------------------------|
| `text_list` hoặc `text_source` + payload | Có | Danh sách chuỗi text để match; khi scope=screen chỉ text thuộc biên màn hình đó. | Flatten `ocr_round1_text` của screen k → mảng chuỗi |
| `scope` | Có | **screen** \| frame \| section \| file. **screen** = suy luận trong giới hạn một màn; mọi input thuộc cùng biên. | **screen** (một lần gọi = một màn) |
| `scope_id` | Nên có (bắt buộc khi scope=screen) | Id screen/frame để xác định biên. | `screen_inventory.screens[k].screen_id` hoặc name |
| `domain` | Optional | Domain để chọn registry (generic + text-signals-{domain}.json). | product_name / banking, … |
| `context_hint` | Optional | Ngữ cảnh của màn hình đó (list, form…); khi scope=screen phải cùng screen. | `ocr_screen_context` của screen k |
| `ocr_icons` | Optional | Icon + vị trí trong cùng màn hình; khi scope=screen chỉ icon thuộc biên đó. | `ocr_round2_icons[k]` hoặc ocr_full_table của screen k |
| `signal_registry_path` | Optional | Đường dẫn thư mục chứa text-signals-*.json; mặc định skill/data. | — |
| `output_format` | Có | report_md \| tags_only \| inferred_ux \| prd_extension | prd_extension |
| `product_name` | Optional | Tên sản phẩm (cho DDL / báo cáo). | product_name từ pack |

## Suy luận theo biên màn hình (screen-scoped inference)

Khi **scope = screen**, skill coi toàn bộ input (text_list, context_hint, ocr_icons) là **cùng một biên màn hình**. Inference chỉ xét tín hiệu trong biên đó để **hình dung/suy luận UX của 1 screen** (flow, component, state trong màn). Không kết hợp tín hiệu từ screen khác. Consumer có biên màn hình (figma-to-prd, handoff) nên gọi **một lần per screen** với payload đầy đủ theo biên — tối ưu hơn so với gọi theo frame/section chung.

## Output

Theo `output_format`:

- **report_md:** Markdown báo cáo match + inferred UX.
- **tags_only:** Mảng tag (vd. selection_mode, bulk_action).
- **inferred_ux:** JSON generic `{ flows[], components[], states[] }` — cho consumer không cần PRD.
- **prd_extension:** Đề xuất flow (Section 1) + component rows (Section 3), mỗi item có **ddl_ref** khi DDL khớp (format theo conventions § DDL reference).

## Quy trình 4 bước

1. **Chuẩn hóa text:** Từ text_list hoặc text_source (ocr_text, prd_md, figma_mcp) → mảng chuỗi.
2. **Match registry → inference rules:** Load text-signals-generic.json + text-signals-{domain}.json (nếu có). Match pattern (instruction, counter, action, cancel, tags) → áp dụng inference_rules → inferred_ux. **Khi scope=screen:** chỉ xét tín hiệu trong biên; không gộp tín hiệu từ scope khác.
3. **DDL on demand (khi output cần ddl_ref):** Nếu output_format là prd_extension hoặc report_md có citation, skill **gọi DDL on demand** — query scope GLOBAL theo pattern/keyword tương ứng inferred UX (vd. "bulk action", "selection mode", "confirmation destructive") tại `.agents/skills/ui-ux-pro-max/data/` (ux-guidelines.csv, web-interface.csv, ux-laws.csv) để lấy **ddl_ref** (vd. `ux-guidelines.csv#22`); gắn ddl_ref vào từng flow/component row trong output.
4. **Xuất:** Theo output_format (report_md | tags_only | inferred_ux | prd_extension).

## Data & Reference

- **Pattern registry:** `data/text-signals-schema.md`, `data/text-signals-generic.json`, `data/text-signals-{domain}.json`.
- **Inference rules:** `reference/inference-rules.md`.
- **DDL (call on demand):** [.agents/docs/ddl/contract.md](.agents/docs/ddl/contract.md), [.agents/docs/ddl/hierarchy.md](.agents/docs/ddl/hierarchy.md). Conventions § DDL reference: [.agents/skills/figma-to-prd-md/conventions.md](.agents/skills/figma-to-prd-md/conventions.md).

## Improve UX workflows (optional)

Dùng khi consumer muốn luồng **cải thiện UX** và so sánh trước/sau (comparison mockups). Không bắt buộc khi chỉ cần suy luận (prd_extension merge trong figma-to-prd Phase 4e).

**Khi nào dùng:** Sau khi đã có PRD .md (từ figma-to-prd hoặc tay) và muốn tạo "đề xuất cải thiện UX" hoặc mockup so sánh trước/sau.

**Đề xuất cải thiện UX:** Output `prd_extension` (với ddl_ref) từ skill này có thể dùng như danh sách "đề xuất cải thiện UX". Khi input là OCR (text_list từ ocr_round1_text, context_hint từ ocr_screen_context, ocr_icons từ ocr_round2_icons), output tương đương ocr_ux_improvements với ddl_ref. Có thể merge vào PRD §1, §3 với badge và citation.

**Comparison mockups (before/after):**

- **Input:** Handoff từ figma-to-prd (screen_inventory với ocr_*, prd_augmented) hoặc PRD .md đã ghi.
- **Bước 1 — Spec "before":** Từ prd_augmented (hoặc PRD trước khi áp dụng prd_extension): Section 3 Mô tả màn hình + (tùy chọn) block "Đề xuất cải thiện UX (chưa áp dụng)" từ prd_extension/ocr_ux_improvements. Ghi file spec .md (Mockup Screen Spec). Tham chiếu: `.agents/skills/md-to-mockup/SKILL.md` § Mockup Screen Spec.
- **Bước 2:** Gọi skill **md-to-mockup** với file spec → output `.mockups/before/mockup-before-ux-improve.png`.
- **Bước 3:** Áp dụng prd_extension vào PRD (merge flow + component rows, badge), ghi .md.
- **Bước 4 — Spec "after":** Trích từ feature .md đã ghi (heading + ### Mô tả màn hình). Ghi file spec .md.
- **Bước 5:** Gọi skill **md-to-mockup** → output `.mockups/after/mockup-after-ux-improve.png`.
- **Gate:** Hai file .png phải tồn tại; nếu thiếu báo **MOCKUP_GATE_FAILED**.

**Mockup capability check (optional):** Trước khi chạy workflow mockup, có thể gọi md-to-mockup với spec tối thiểu (vd. `# Screen: Test`, bảng Mô tả màn hình 1 row) để kiểm tra khả năng tạo .png — tương đương bước 0b-bis trước đây trong figma-to-prd.

## Ràng buộc

- Inferred UX phải gắn với matched signal (pattern_group_id).
- Regex trong JSON escape đúng (vd. `\\d+`, `\\(`, `\\)` trong chuỗi JSON).
