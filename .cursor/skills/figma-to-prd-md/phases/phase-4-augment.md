# Phase 4: Augment (ui-ux-pro-max + frontend-design + Case Study)

**Tham chiếu:** `conventions.md` (AI Badge Convention); `reference/badge-examples.md` (format ví dụ cho 5 sections).

## Mục tiêu

Bổ sung nội dung COMPextend vào PRD draft mà KHÔNG thay đổi cấu trúc 5 section. Mọi nội dung bổ sung hiển thị bằng `🤖 by AI` badge.

## 4a. Thu thập (chạy song song)

- **OCR per screen:** Đọc từ `screen_inventory.screens[k]`: `ocr_screen_context`, `ocr_ux_improvements`, `ocr_gaps`. `ocr_ux_improvements` đã được sinh với **tham chiếu DDL** (conventions § DDL reference). Khi 4b/4c chèn badge từ ocr_ux_improvements, **citation phải gồm ddl_ref** khi có.
- **Case study subagent:** Tạo subagent `generalPurpose`, prompt: nghiên cứu sản phẩm `{product_name}`; chạy search.py `--design-system` và `--domain product`; WebSearch 2-3 case study tương tự; trả về `persona_proposal`, `flow_improvements`, `feature_gaps` (format JSON do agent quyết định).
- **CSV + search.py:** Dữ liệu từ `.agents/skills/ui-ux-pro-max/data/`. Tham chiếu đầy đủ: [.cursor/docs/ui-ux-pro-max-reference.md](.cursor/docs/ui-ux-pro-max-reference.md). Bảng CSV → section: `ux-guidelines.csv` → §2 AC, §5 NFR; `web-interface.csv` → §2 Business Rule, AC; `colors.csv`, `typography.csv`, `styles.csv` → §5 NFR; `icons.csv` → §3 Mô tả. Chạy thêm: `search.py "error feedback loading empty" --domain ux`, `"form validation keyboard aria" --domain web`, `"touch target animation hover" --domain ux`.
- **Frontend-design:** Đọc `.cursor/skills/frontend-design/SKILL.md`. Design Thinking (Purpose, Tone, Constraints, Differentiation) per screen; Pre-Delivery Checklist (no emoji, contrast 4.5:1, touch 44pt, typography, focus, cursor, hover). Output đúng format section tương ứng (badge).

## 4b. Enrich PRD (tuần tự, dùng output 4a)

Áp dụng 1 bảng mapping — cross-reference draft với output 4a, sinh badge vào section tương ứng:

| Section PRD | Nguồn | Hành động |
|-------------|--------|-----------|
| Overview §1 Chân dung KH | case_study.persona_proposal + case_studies[].persona_insights | Nếu §1 trống → sinh badge persona (format bullet Đối tượng, Quy mô, Lĩnh vực, Nhu cầu). Ví dụ: `reference/badge-examples.md` (Chân dung KH). |
| Feature §1 User Flow | case_study.flow_improvements + ux-guidelines.csv#10 | Đề xuất luồng thiếu: error recovery, back navigation, timeout/retry, empty state. Format: `### 1.N. Tên luồng` + bảng 4 cột. Ví dụ: `reference/badge-examples.md` (User Flow). |
| Feature §2 User Story | case_study.feature_gaps + web-interface.csv + ux-guidelines | Đề xuất US: accessibility, loading/skeleton, edge case, competitor-inspired. Format: bảng 6 cột, AC dùng `<br>`. Ví dụ: trong `conventions.md` (badge User Story). |
| Feature §3 Wireframe / §5 NFR | ocr_ux_improvements + ocr_gaps | Nếu OCR đã gợi ý thiếu error/empty/retry copy hoặc cải thiện accessibility (từ ocr_ux_improvements hoặc ocr_gaps.missing_text/missing_components), Phase 4 bổ sung badge tương ứng vào §2 AC, §3 Mô tả màn hình, §5 Trải nghiệm. Ưu tiên màn có ocr_gaps không rỗng. **Citation badge phải gồm ddl_ref** khi item có (conventions § DDL reference). |
| Feature §5 NFR | frontend-design + ux-guidelines + colors/typography/styles | Đề xuất NFR: Bảo mật, Hiệu năng, Trải nghiệm. Format: bullets `- **Category:**` + 4-space indent. Ví dụ: `reference/badge-examples.md` (NFR). |

Patterns bắt buộc kiểm tra: error recovery (async screen), back + data retention (form), timeout/session (auth/OTP), empty state (list), confirmation trước destructive (delete/cancel).

## 4c. UX Writing

Scan PRD draft: thiếu error message, helper text, loading/success/retry copy, empty state copy. **Scan thêm** từ `ocr_gaps` (missing_text có thể là label/placeholder chưa có trong spec) và `ocr_ux_improvements`: chèn error/empty/success/retry copy vào §2 AC, §3 Mô tả (bảng 4 cột), §5 Trải nghiệm. Chèn badge vào §2 AC, §3 Mô tả (bảng 4 cột), §5 Trải nghiệm. Ví dụ bảng 4 cột (Loading/Success/Error/Empty): `reference/badge-examples.md` (Wireframe).

**Thứ tự:** 4a song song → xong hết mới 4b → 4c (4c dùng output 4b).

## 4e. Suy luận UX theo biên màn hình — BẮT BUỘC

**Điều kiện:** Tham số `enable_ux_signal_inference !== false` (mặc định bật). Phase 4e **bắt buộc** — pipeline luôn chạy sau 4c trừ khi user rõ ràng đặt `enable_ux_signal_inference = false`. Thực hiện **sau khi** 4c xong. **Chỉ dùng dữ liệu đã kết xuất**: `screen_inventory`, `prd_augmented` (§1, §3). Không gọi Figma MCP, không extract mới.

**Mục tiêu:** Gọi skill **ux-signal-inference** theo **biên màn hình** (một lần per screen, scope=screen) với payload đầy đủ theo input contract của skill, nhận prd_extension (đã có ddl_ref khi DDL khớp), merge vào prd_augmented để Phase 5 ghi .md.

### Định nghĩa payload đầy đủ (theo input contract ux-signal-inference)

Phase 4e **truyền đầy đủ** các input mà skill ux-signal-inference cần; không bỏ qua context_hint hay ocr_icons khi dữ liệu có sẵn. Với **mỗi screen k**, build payload **screen-scoped** (mọi field chỉ thuộc screen đó):

| Tham số skill | Nguồn từ screen_inventory (screen k) | Ghi chú |
|---------------|--------------------------------------|---------|
| `text_list` | Flatten `ocr_round1_text[k]` (text_content, lines) → mảng chuỗi; fallback: lọc row type "text" từ `ocr_full_table[k]` hoặc `text_nodes[k]` | Bắt buộc |
| `scope` | `"screen"` | Một lần gọi = một màn |
| `scope_id` | `screen_inventory.screens[k].screen_id` hoặc `screen_name_vi` | Bắt buộc khi scope=screen |
| `context_hint` | `ocr_screen_context` của screen k (nếu có) | Truyền khi có |
| `ocr_icons` | Từ `ocr_round2_icons[k]` hoặc row type "icon" trong `ocr_full_table[k]` → `[{ description_or_label, position_zone }]` | Truyền khi có |
| `domain` | product_name / product (vd. banking) | Optional |
| `output_format` | `"prd_extension"` | Cố định cho Phase 4e |
| `product_name` | product_name từ pack | Optional |

**Ràng buộc:** Phase 4e gọi ux-signal-inference **theo biên màn hình**: mỗi lần gọi = một screen, scope=screen, payload đầy đủ (text_list, context_hint, ocr_icons) **chỉ thuộc screen đó**; truyền đủ input theo contract.

### Bước 4e-1. Với mỗi screen (biên màn hình)

1. Đọc từ `screen_inventory.screens[k]`: ocr_round1_text, ocr_screen_context, ocr_round2_icons, ocr_full_table, screen_id, screen_name_vi.
2. Build payload như bảng trên (text_list, scope="screen", scope_id, context_hint, ocr_icons, domain, output_format="prd_extension", product_name).
3. Gọi skill **ux-signal-inference** với payload đầy đủ. Skill thực hiện inference trong biên màn hình đó và **trong skill** call DDL on demand để gắn ddl_ref vào prd_extension.
4. Nhận prd_extension: suggested flow (Section 1), suggested component rows (Section 3), mỗi item có **ddl_ref** khi DDL khớp.

### Bước 4e-2. Merge vào prd_augmented

- Merge prd_extension vào prd_augmented tương ứng feature file của screen k: thêm flow vào §1 User Flow, thêm component rows vào §3 Mô tả màn hình.
- Mọi nội dung thêm hiển thị với badge `🤖 by AI`.
- Citation: **signal_inference:{pattern_group_id}** và **ddl_ref** (đã có sẵn trong prd_extension). Tuân conventions § DDL reference.
- Ghi nhận đã chạy Phase 4e (số màn đã gọi, số flow/row đã merge) để Phase Report (§5f).

### Handoff

- Không thay đổi handoff; Phase 5 có thể ghi `.handoff/screen_inventory.json` chứa đủ ocr_round1_text, ocr_screen_context, ocr_round2_icons per screen để skill ux-signal-inference có thể chạy standalone từ handoff (build payload theo từng screen, scope=screen).

