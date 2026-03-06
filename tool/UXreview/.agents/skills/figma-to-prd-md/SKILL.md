---
name: figma-to-prd-md
description: "Nhận link Figma, sinh bộ PRD .md theo cấu trúc XPOS (overview + feature files với 5 section chuẩn). Bắt buộc suy luận UX theo biên màn hình (Phase 4e: gọi ux-signal-inference, merge prd_extension). Kết hợp augment từ ui-ux-pro-max + frontend-design. Output tương thích với prd-full-pipeline v3. Dùng khi user cung cấp Figma URL và cần bộ PRD markdown làm input cho pipeline."
---

# Figma to PRD Markdown Pack

Nhận link Figma (hoặc file_key + node_id), extract toàn bộ screens/frames, sinh bộ file PRD .md theo đúng cấu trúc XPOS PRD (1 overview + N feature files, mỗi file 5 section cố định). Output sẵn sàng feed vào `prd-full-pipeline` v3.

## When to Apply

- User cung cấp Figma URL và cần bộ PRD .md
- Cần chuyển Figma design thành PRD structured markdown
- Cần sinh input cho prd-full-pipeline v3 từ Figma
- Bridging: design (Figma) → PRD docs (structured .md) → pipeline (mockup-spec.json)

## Mối quan hệ với các skill khác

| Skill | Vai trò | Quan hệ |
|-------|---------|---------|
| **figma-to-prd-md** (skill này) | Sinh bộ PRD .md từ Figma | **Bước trước** pipeline |
| prd-full-pipeline v3 | Phân tích PRD → mockup-spec.json | **Bước sau** skill này |

**ui-ux-pro-max:** Tham chiếu [.agents/docs/ui-ux-pro-max-reference.md](.agents/docs/ui-ux-pro-max-reference.md) (canonical path data: `.agents/skills/ui-ux-pro-max/data/`).

```
Figma URL → [figma-to-prd-md] → PRD .md Pack → [prd-full-pipeline v3] → mockup-spec.json
```

## Input Contract

| Parameter | Required | Description |
|-----------|----------|-------------|
| `figma_url` | Yes (hoặc `file_key` + `node_id`) | Full Figma URL, vd: `https://figma.com/design/:fileKey/:fileName?node-id=1-2` |
| `file_key` | Alt | File key extracted từ URL |
| `node_id` | Alt | Node ID extracted từ URL (page-level hoặc section-level) |
| `product_name` | Yes | Tên sản phẩm (vd: "Co-op Bank KHCN", "xPOS") |
| `product_description` | No | Mô tả ngắn sản phẩm (dùng cho overview file) |
| `language` | No | Mặc định `vi` (Vietnamese). Options: `vi`, `en` |
| `token_file` | No | Mặc định `temp1.json` |
| `output_dir` | No | Mặc định `{workspace}/{product-slug}/` |
| `image_base_url` | No | Base URL cho link ảnh absolute (vd: `http://localhost:8080`). Để trống thì dùng relative path (cùng thư mục với .md). Dùng khi cần ảnh hiển thị đúng trên một localhost cố định. |
| `output_structure` | No | `section_folder` (mặc định): output theo cấu trúc figma-save-screenshot — mỗi section một folder, ảnh trong folder con `ui/`. Số file .md trong section = số distinct screen (`screen_boundaries`): **1 file .md per screen**. `flat`: overview + feature .md tại output_dir, ảnh trong output_dir/.../section/ui/). |
| `prd_file` | No | File PRD .md có sẵn (nếu có, dùng bổ sung business logic) |
| `allow_section_fallback` | No | Khi trong một section không sinh được `screen_boundaries`: `true` cho phép fallback 1 section = 1 screen (1 file .md) với warning `SCREEN_BOUNDARY_FALLBACK_USED`; `false` → fail `SCREEN_BOUNDARY_MISSING`. Mặc định `false`. |
| `include_unmapped_elements` | No | `true` (mặc định): đưa node không match component-mapping vào bảng Mô tả màn hình dưới dạng "Design element" (Phase 2b-bis). `false`: không thêm row cho unmapped. |
| `include_design_specs` | No | `true`: sinh `design_spec_summary` từ style_properties/auto_layout và subsection "Thông số design (tham khảo)" trong Section 3. Mặc định `false`. |
| `enable_ocr_reconciliation` | No | `true` (mặc định): **bước reconciliation ảnh (Phase 2g) bắt buộc** — phải sinh `ocr_full_table`, `ocr_gaps` cho mọi screen có ảnh. OCR thực hiện **bằng agent vision** (đọc ảnh từ path), **hai round** mỗi biên: Round 1 toàn bộ text, Round 2 toàn bộ icon + vị trí. Không dùng Tesseract hay script. `false`: bỏ qua 2g. |
| `mapping_canonical_language` | No | Ngôn ngữ chuẩn để so khớp pattern (term-equivalents + component-mapping). Mặc định `vi`. Figma layer name được chuẩn hóa về ngôn ngữ này ở 2b-pre. |
| `figma_label_language` | No | Ngôn ngữ nhãn/layer trong Figma (vd. `en`). Optional; nếu không truyền thì có thể tự phát hiện hoặc mặc định trùng với canonical. |
| `enable_ux_signal_inference` | No | **Bắt buộc chạy Phase 4e** (Suy luận UX theo biên màn hình). `true` (mặc định): gọi ux-signal-inference theo biên màn hình (scope=screen, một lần per screen), truyền đủ input theo contract (text_list, context_hint, ocr_icons, scope_id, domain, output_format); skill suy luận UX trong 1 screen, trả về prd_extension (có ddl_ref) → merge vào prd_augmented. Chỉ đặt `false` khi user **rõ ràng** yêu cầu bỏ qua Phase 4e (không khuyến nghị). |

### Tool Requirements (Preflight)

Khi chạy standalone hoặc từ workflow, agent cần các tools sau:

| Tool | Required | Purpose |
|:---|:---:|:---|
| figma-save MCP (`figma_save_section_screenshots`) | ✅ | Export artboards → PNG |
| Figma Token (`FAT` hoặc `FIGMA_ACCESS_TOKEN` trong env) | ✅ | Auth cho Figma API |
| DDL Data (`.agents/skills/ui-ux-pro-max/data/*.csv`) | ✅ | UX rules cho Phase 4, OCR ux_improvements |
| Figma MCP (dev-mode, optional) | ❌ | Fallback/supplement cho metadata |

Khi chạy từ workflow `figma-to-ux-review`, các checks này nằm trong PREFLIGHT gate. Khi chạy standalone, agent nên verify token trước khi gọi Figma API.

### Phase 4e — Suy luận UX theo biên màn hình (ux-signal-inference) — BẮT BUỘC

Sau 4c pipeline **bắt buộc** thực hiện **Phase 4e** (trừ khi `enable_ux_signal_inference === false`):

- **Gọi theo biên màn hình:** Mỗi lần gọi skill **ux-signal-inference** = **một screen**; `scope = screen`; payload đầy đủ theo [input contract của ux-signal-inference](.agents/skills/ux-signal-inference/SKILL.md): `text_list` (từ ocr_round1_text của screen k), `context_hint` (ocr_screen_context), `ocr_icons` (ocr_round2_icons hoặc ocr_full_table), `scope_id`, `domain`, `output_format = prd_extension`. Không bỏ qua context_hint hay ocr_icons khi dữ liệu có sẵn.
- **Mục đích:** Skill suy luận UX trong 1 screen (flow, component, state); trả về prd_extension đã có ddl_ref (skill gọi DDL on demand). Pipeline merge prd_extension vào prd_augmented (§1 User Flow, §3 Mô tả màn hình) với badge `🤖 by AI` và citation signal_inference + ddl_ref.
- Chi tiết payload và bước thực hiện: `phases/phase-4-augment.md` § 4e.

## Output Determinism Contract (screen_boundaries)

Theo **`phases/phase-2-inventory.md` § 2a-bis (Determinism rule)**: nguồn sự thật = `screen_boundaries` / `feature_file_plan`; parity mục 3 = mục 8 = số feature files = số screen. `allow_section_fallback` → SCREEN_BOUNDARY_MISSING hoặc warning khi không detect được boundaries trong section. Output .md và OCR đều theo **biên màn hình** (screen boundaries): mỗi biên = 1 file .md; mỗi biên chạy đủ **hai round** vision (Round 1: text, Round 2: icon + vị trí). **Phạm vi OCR (bắt buộc):** Với mỗi screen k, agent chạy Round 1 rồi Round 2 trên **tất cả** ảnh trong `screen_inventory.screens[k].wireframe_images`; `ocr_full_table` của screen k phủ text + icon (ít nhất một row cho mỗi filename khi có nội dung). Chi tiết tại Phase 2 § 2a-bis (mapping ảnh ↔ biên) và § 2g (contract OCR theo biên).

---

## Pipeline: 5 Phase → 6 Layers

```
Phase 0: Scan & Scope     (chỉ khi page-level link)
    ↓ 0a metadata scan → 0b scope
    ↓ section_list + scope decision
Phase 1: Figma MCP Extract
    ↓ figma_raw
Phase 2: Screen Inventory
    ↓ screen_inventory + figma_context_registry + flow_graph
Phase 3: PRD Structure Gen
    ↓ prd_draft (overview + feature files)
Phase 4: Augment (ui-ux-pro-max + frontend-design)
    ↓ prd_augmented
    [4e: Suy luận UX theo biên màn hình — bắt buộc]
    ↓ gọi ux-signal-inference theo biên màn hình → merge prd_extension
Phase 5: Output .md Pack
    ↓ Final .md files
```

Mỗi phase phải hoàn thành trước khi bắt đầu phase tiếp theo.

| Phase | Layer phủ (`design_data_layer`) | Data sinh ra |
|-------|----------------------------------|-------------|
| Phase 0 | — | section_list, scope decision. |
| Phase 1 | **L1** Figma Fundamentals | figma_raw: screens, screenshots, dimensions |
| Phase 2 | **L2** Advanced Figma | screen_inventory, component_registry, flow_graph, variables |
| Phase 3 | **L2** (structured PRD) | prd_draft: 5-section .md files |
| Phase 4 | **L3** UI Principles + **L5** UX Research | COMPextend proposals, case study, UX writing. **4e (bắt buộc):** Suy luận UX — gọi ux-signal-inference theo biên màn hình (scope=screen, payload đầy đủ per screen), merge prd_extension (có ddl_ref) vào prd_augmented. |
| Phase 5 | **L6** UX Strategy | Quality gates, UNSPECIFIED summary, AI summary, **Phase Report** |

Sau Phase 5, skill xuất **Phase Report** (kết quả từng phase 0→5) vào **cuối file overview** — section `## Kết quả chạy pipeline (Phase Report)`. Chi tiết: `phases/phase-5-output.md` §5f.

L4 (UI Implementation — token resolution, CSS specs) do `prd-full-pipeline` Skill 3-4 xử lý. Ref: [.agents/docs/ddl/contract.md](.agents/docs/ddl/contract.md), [.agents/docs/ddl/views-and-outputs.md](.agents/docs/ddl/views-and-outputs.md).

Skill này **gọi** design data layer (DDL) on-demand theo scope GLOBAL + PRODUCT để lấy UX rules, tokens, component mapping; không sở hữu DDL. Hierarchy: [.agents/docs/ddl/hierarchy.md](.agents/docs/ddl/hierarchy.md). Tham chiếu DDL khi sinh ocr_ux_improvements (Phase 2g): query scope GLOBAL (ux-guidelines.csv, web-interface.csv, ux-laws.csv tại `.agents/skills/ui-ux-pro-max/data/`), gắn mỗi đề xuất với rule tương ứng (`ddl_ref`) và citation trong output; chi tiết tại Phase 2g và 2g-bis.

---

## Phase Routing

Mỗi phase đọc file tương ứng trước khi thực hiện. **KHÔNG** đọc tất cả cùng lúc — chỉ load file của phase hiện tại + dependencies.

| Phase | File | conventions.md? | File khác? |
|-------|------|-----------------|------------|
| 0 | `phases/phase-0-scan.md` | Không | — |
| 1 | `phases/phase-1-extract.md` | **Có** | — |
| 2 | `phases/phase-2-inventory.md` | Không | **`data/component-mapping.md`** |
| 3 | `phases/phase-3-generate.md` | **Có** | — |
| 4 | `phases/phase-4-augment.md` | **Có** | **`reference/badge-examples.md`** |
| 5 | `phases/phase-5-output.md` | **Có** | **`reference/citation-quality.md`** |

**Case routing:**
- `node_id` là PAGE (nhiều sections) → bắt đầu Phase 0 (0a → 0b → 0c nếu BATCH).
- `node_id` là section/frame cụ thể → bỏ qua Phase 0, vào Phase 1.

**Chạy tiếp Phase 2 → 5 (mặc định — standalone):** Sau khi hoàn thành Phase 0 (nếu chạy) và Phase 1, agent **luôn mặc định chạy tiếp Phase 2 → 3 → 4 → 5** đến khi pipeline kết thúc (Phase Report đã ghi). Không dừng giữa chừng để hỏi user "có chạy tiếp không"; chỉ dừng khi gate fail (vd. OCR_GATE_FAILED) hoặc user **rõ ràng** yêu cầu dừng.

**Khi chạy từ workflow `figma-to-ux-review`:** Run-to-completion vẫn áp dụng nhưng phải dừng tại các Human Checkpoints do workflow định nghĩa:
- **HC-1** (sau Phase 0-1): Verify ảnh export thành công → user xác nhận
- **HC-2** (sau Phase 2g): Verify OCR completeness → user xác nhận
- **HC-3** (sau Phase 3, optional): PRD draft sanity check
- **HC-4** (sau Phase 5): Pre-handoff gate (7 checks bao gồm IMAGE_EXIST)
Khi chạy **standalone** (không qua workflow): mặc định run-to-completion như trên.

**OCR (bắt buộc khi enable_ocr_reconciliation === true):** **Phạm vi theo biên màn hình:** (a) Đơn vị thực thi = một biên màn hình (screen k). (b) Với mỗi screen k, agent chạy **đủ hai round** vision trên **tất cả** ảnh trong `screen_inventory.screens[k].wireframe_images`: Round 1 (toàn bộ text) → Round 2 (toàn bộ icon + vị trí). (c) Kết quả: `ocr_full_table` (và ocr_round1_text, ocr_round2_icons) phủ mọi file ảnh thuộc biên. Agent sinh `ocr_full_table`, `ocr_gaps`, `ocr_screen_context`, `ocr_ux_improvements`. **Phương pháp duy nhất:** Agent vision (đọc ảnh từ path); không Tesseract, không script. Gate: Phase 3 chỉ chạy khi mọi screen có ảnh đều có `ocr_full_table` và file `.handoff/.ocr_done` tồn tại. Chi tiết: `phases/phase-2-inventory.md` § 2g.

**OCR execution contract (khi enable_ocr_reconciliation === true):** (1) Thực hiện 2g bằng **agent vision** (đọc ảnh từ path), **hai round** mỗi screen có ảnh: Round 1 text, Round 2 icon + vị trí. (2) Sau khi hoàn thành 2g cho mọi screen: ghi `.handoff/.ocr_done`. (3) Phase 5 Pre-output check: mọi screen có ảnh phải có `ocr_full_table`; thiếu → `OCR_GATE_FAILED`. Chi tiết: `phases/phase-2-inventory.md` § 2g, § Implementation 2g, `phases/phase-5-output.md` §5d.

**Chạy đến bước cuối (Run to completion):** Khi user cung cấp Figma URL (hoặc file_key + node_id) và cần bộ PRD .md, **mặc định** coi là chạy pipeline đến bước cuối: Phase 0 → 1 → 2 → 3 → 4 → 5; sau Phase 1 **luôn chạy tiếp Phase 2 → 5** không cần xác nhận. **(1)** Giữ `enable_ocr_reconciliation === true` (mặc định). **(2)** Phase 2g: dùng agent vision, **hai round** (Round 1 text, Round 2 icon + vị trí) cho từng screen có ảnh; điền ocr_round1_text, ocr_round2_icons, ocr_full_table rồi Bước 2–4. **(3)** Sau khi hoàn thành 2g cho mọi screen: ghi `.handoff/.ocr_done`. **(4)** Chỉ khi đã có `.ocr_done` (và pass Pre-output OCR check ở Phase 5) mới ghi file .md. Bước cuối của skill là **Phase 5** (ghi .md pack + Phase Report). Skill này **không** bao gồm prd-full-pipeline v3 (mockup-spec.json); pipeline v3 gọi riêng sau khi có bộ PRD .md. Workflow so sánh trước/sau (comparison mockups) và mockup: xem skill ux-signal-inference.

---

## Tích hợp với prd-full-pipeline v3

Sau khi skill này chạy xong:

1. User có bộ PRD .md theo cấu trúc XPOS
2. Gọi `prd-full-pipeline` v3:
   ```
   prd_folder = {output_dir}
   figma_source = {figma_url}
   ```
3. Pipeline v3 skip Skill 0 (có Figma), chạy Skill 1-4
4. Output: `mockup-spec.json` + 7 file ui-automation .md

---

## Structured Handoff

Phase 5 ghi **machine-readable handoff** vào `{output_dir}/.handoff/`. **BẮT BUỘC** khi chạy từ workflow `figma-to-ux-review`; optional nếu chạy standalone.

| File | Bắt buộc | Nội dung |
|------|:---:|----------|
| `screen_inventory.json` | **Có** | Danh sách screen + **`consumer_payload`** per screen (xem bảng dưới). Pipe 2 (ux-review-pipe) dùng fast-path khi có file này. |
| `handoff-manifest.json` | **Có** | `schema_version`, `generated_at`, `figma_source`, `output_structure`, `flags`, `ocr_done`, `phases_completed` |
| `flow_graph.json` | Nên có | Cạnh luồng (edges) giữa các screen (from, to, trigger, type) |
| `figma_context_registry.json` | Tuỳ chọn | context_label, context_type, figma_source, screen_id, canonical_key |

### Consumer Payload per Screen (trong screen_inventory.json)

Mỗi screen phải chứa `consumer_payload` với:

| Field | Nguồn | Mô tả |
|:---|:---|:---|
| `text_list` | `ocr_round1_text` (flatten) | Mảng string toàn bộ text trên screen |
| `context_hint` | `ocr_screen_context` | Ngữ cảnh tổng hợp (1-2 câu) |
| `ocr_icons` | `ocr_round2_icons` | Mảng object `{ icon, position, file }` |
| `ocr_screen_context` | Phase 2g tổng hợp | Context dài hơn context_hint |

**Schema version:** `figma-prd-handoff-v1`. Khi downstream có `.handoff/` hợp lệ, ưu tiên load; không có thì fallback parse markdown.

**Quy tắc:** Phase 5 phải validate schema trước khi ghi; nếu fail → không ghi `.handoff/`, vẫn ghi .md pack bình thường, log `HANDOFF_SCHEMA_INVALID`.


---

## Post-processing: OCR sau khi đã có .md và ảnh wireframe

Khi đã có feature .md và ảnh trong `ui/`, có thể chạy **OCR reconciliation sau** (2g-bis) để bổ sung Spec còn thiếu, Ngữ cảnh màn hình và Đề xuất cải thiện UX mà không cần chạy lại Phase 1–2. Agent đọc ảnh từ path, chạy **Round 1** (text) rồi **Round 2** (icon + vị trí), điền ocr_full_table và cập nhật Section 3. **Chi tiết:** `phases/phase-2-inventory.md` § 2g-bis. Workflow so sánh trước/sau và mockup: xem skill ux-signal-inference.

---

## Constraints

- PRD .md files là **human-readable first** — phải đọc được như tài liệu PRD thật
- Giữ nguyên ngôn ngữ tiếng Việt cho labels, screen names, mô tả (trừ technical terms)
- KHÔNG sinh CSS — output là .md PRD documents
- KHÔNG sinh mockup-spec.json (đó là việc của prd-full-pipeline)
- Figma context registry truyền qua cho pipeline v3 thông qua `figma_source` parameter
- Nếu `prd_file` được cung cấp: dùng như **source bổ sung** cho Business Rule và Database (ưu tiên PRD > suy luận từ Figma)
- Chi tiết boundary detection/classifier/variant merge nằm ở `phases/phase-2-inventory.md` (2a-bis); overview parity và file plan nằm ở `phases/phase-3-generate.md` + `phases/phase-5-output.md`.
