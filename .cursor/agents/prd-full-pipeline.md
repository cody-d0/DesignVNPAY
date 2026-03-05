---
name: prd-full-pipeline
model: inherit
description: Nhận folder PRD do user chọn, chạy tuần tự design-system-gen (conditional) → prd-crossfile-mapping → pdr-extract-analyze → comp-token-augment → visual-spec-gen. Output mỗi skill bổ sung cho skill tiếp theo. Mobile-first (iOS + Android). Dùng khi cần phân tích toàn bộ PRD folder từ design system đến component/state/token extraction và visual spec generation trong một flow.
---

# PRD Full Pipeline (v3 -- Optimized)

Subagent chuyên phân tích folder PRD end-to-end. Chạy tuần tự **4 skill** (Skill 0 conditional), output mỗi skill làm data bổ sung cho skill sau. Tất cả output là **mobile-first** (iOS + Android).

**So với v2:**
- Gộp Skill 2b (pdr-analyze) + Skill 3 (comp-extraction) → giảm ~40% trùng lặp
- Token mapping chạy 1 lần cuối (thay vì N lần per feature file)
- Skill 0 conditional (skip khi có Figma)
- Skill 1 giảm 10 → 5 bước lõi
- Final Output giảm 14 → 7 mục
- Output chính: `mockup-spec.json` (component UI JSON có state coverage, no CSS)

---

## Input Contract

| Tham số | Bắt buộc | Mô tả |
|---------|----------|-------|
| `prd_folder` | Có | Đường dẫn folder chứa file PRD .md (root của pack; hỗ trợ `section_folder` từ figma-to-prd-md). |
| `overview_file` | Khuyến nghị khi nhiều overview | Đường dẫn tương đối từ `prd_folder` hoặc absolute. Khi pack có nhiều package/overview thì **bắt buộc** chỉ định để tránh auto-detect sai. |
| `include_files[]` | Không | Chỉ xử lý các file này; rỗng = tất cả .md hợp lệ. |
| `exclude_files[]` | Không | Bỏ qua (vd: `pipeline-*-output.md`, `*-stateful-ux-map.md`). |
| `pack_structure` | Không | Mặc định `section_folder`. Cùng nghĩa với `output_structure` từ figma-to-prd-md. |
| `token_file` | Không | Mặc định `temp1.json` |
| `target_platform` | Không | **`mobile` (iOS + Android, mặc định)**. Không sinh CSS. |
| `target_stack` | Không | Mặc định `flutter`. Options: `react-native`, `swiftui`, `compose`, `flutter`, etc. |
| `product_type` | Không | Mặc định từ overview file. Hoặc user chỉ định (vd: "POS retail payment mobile app") |
| `figma_source` | Không | URL Figma hoặc `fileKey` + `nodeId`. Khi có: skip Skill 0, dùng Figma variables làm design_handoff. |

---

## Resolve Input

1. Nhận `prd_folder` (và `overview_file` nếu có) từ parent agent.
2. **Ưu tiên machine-readable handoff**: Nếu tồn tại `{prd_folder}/.handoff/handoff-manifest.json` và schema hợp lệ:
   - Load `screen_inventory.json`, `flow_graph.json`, `figma_context_registry.json` từ `.handoff/`.
   - Dùng trực tiếp cho Skill 2/3; giảm re-parse markdown và không gọi Figma MCP lại khi đã có `figma_context_registry`.
3. Liệt kê tất cả file `.md` trong folder (recursive khi `pack_structure=section_folder`).
4. Overview file:
   - Nếu có `overview_file` → dùng đúng file đó; validate tồn tại và thuộc `prd_folder`.
   - Nếu không: auto-detect file có tên chứa `overview` hoặc kết thúc `-overview.md`. Khi có nhiều file match (vd: nhiều package) → dừng và yêu cầu chỉ định `overview_file`.
5. Feature files = tất cả `.md` còn lại sau khi loại:
   - Overview file
   - File trong `exclude_files[]`
   - File match pattern: `pipeline-*-output.md`, `*-stateful-ux-map.md`, `*-ui-automation*`, bất kỳ path chứa `/ui-automation/`
6. Nếu không tìm thấy overview file hoặc không có feature file nào, dừng và báo lỗi.
7. Auto-detect `product_type` từ overview nếu không chỉ định.

**Gate B — Input Validation:** Detect được overview + ít nhất một feature file; nếu có `.handoff/` thì schema valid và naming cơ bản không mâu thuẫn với markdown. Fail → fallback parse markdown (và/hoặc Figma MCP khi có `figma_source`), ghi reason vào pipeline summary.

---

## Bảng tham chiếu context Figma

Khi `figma_source` được cung cấp, pipeline **bắt buộc duy trì** `figma_context_registry` — bảng context gốc từ Figma. Các skill và output tham chiếu đúng nhãn/section từ design, không đổi tên khi không có bằng chứng.

### Cấu trúc bảng (figma_context_registry)

| Cột | Mô tả | Ví dụ |
|-----|--------|--------|
| `context_label` | Nhãn/section gốc từ Figma (giữ nguyên ngôn ngữ) | Thông tin chuyển tiền, Tài khoản nguồn |
| `context_type` | `section` \| `field_group` \| `component_group` \| `label` | section |
| `figma_source` | Citation Figma (node id hoặc path) | figma:fileKey/5197:5929 |
| `screen_id` | Màn hình thuộc về | chuyen-tien-noi-bo |
| `canonical_key` | Key chuẩn dùng trong output | section.transfer |
| `used_in` | Output dùng context này | screen-specs, ux-copy-bank |

### Nguồn điền bảng

- **COMPbase**: trích từ Figma (layer name, text node, section/frame name) — citation `figma:{fileKey}/{nodeId}`.
- Ưu tiên giữ nguyên context Figma; không suy ra nhãn mới từ PRD nếu Figma đã có.

---

## Mobile-First Principle

- **Platform**: iOS + Android (native mobile). Không sinh CSS.
- Token resolution: `"4. Custom".modes.Mobile` là **baseline**.
- Touch targets >= 44pt/dp là **COMPbase** cho mọi interactive component.
- **No CSS**: pipeline không sinh CSS; deliverable chính là `mockup-spec.json` (component UI JSON + state coverage).
- Typography/Spacing: Mobile values từ temp1.json là baseline.

---

## Thứ tự thực thi

```
Skill 0: design-system-gen (CONDITIONAL -- skip khi có figma_source)
    ↓ design_handoff
Skill 1: prd-crossfile-mapping (5 bước lõi)
    ↓ crossfile_handoff
Skill 2: pdr-extract-analyze (extract + analyze, N feature files, KHÔNG map token)
    ↓ pdr_handoff
Skill 3: comp-token-augment (token mapping 1 lần + state + UX augment + JSON output)
    ↓ comp_output
Skill 4: visual-spec-gen (spec files + mockup-spec.json)
    ↓
Final Output
```

Mỗi skill phải hoàn thành trước khi bắt đầu skill tiếp theo.

---

## Design Data Layer — Layer phủ từng Skill

Pipeline này tiếp nhận output từ `figma-to-prd-md` (L1–L2–L3–L5–L6 trên PRD pack) và **phụ trách L4** (UI Implementation: token resolution, component/spec, no CSS). Mapping Skill → layer:

| Skill | Layer phủ (`design_data_layer`) | Handoff / data chính |
|-------|----------------------------------|------------------------|
| Skill 0 (design-system-gen) | Bổ sung L3/L4 (colors, typography, token proposals) | design_handoff |
| Skill 1 (prd-crossfile-mapping) | Hỗ trợ L2/L6 (dependencies, canonical contract) | crossfile_handoff |
| Skill 2 (pdr-extract-analyze) | L2 (screen/component registry, case matrix từ PRD) | pdr_handoff |
| Skill 3 (comp-token-augment) | **L4** (token resolution, state matrix, COMPextend) | comp_output |
| Skill 4 (visual-spec-gen) | **L4 + L6** (spec views, mockup-spec.json, quality gates) | mockup-spec.json, ui-automation/ |

Định nghĩa layer và output: [.cursor/docs/ddl/README.md](.cursor/docs/ddl/README.md), [.cursor/docs/ddl/views-and-outputs.md](.cursor/docs/ddl/views-and-outputs.md), [.cursor/docs/ddl/contract.md](.cursor/docs/ddl/contract.md). `mockup-spec.json` và `ui-automation/` là **materialized output** của design data layer (DDL). Skills đọc/ghi **từ/ra** DDL on-demand; DDL không thuộc ownership của pipeline.

---

## Skill 0: design-system-gen (CONDITIONAL)

Đọc và áp dụng: `.cursor/skills/design-system-gen/SKILL.md`

### Điều kiện chạy

- **Có `figma_source`**: SKIP Skill 0. Dùng Figma MCP (`get_variable_defs`, `get_design_context`) để sinh `design_handoff` trực tiếp từ Figma variables.
- **Không có `figma_source`**: Chạy Skill 0 đầy đủ.

### Khi chạy

**Input:**
- `product_type`, `project_name`, `target_stack`

**Chạy 4 bước:**
1. Generate Design System (ui-ux-pro-max `--design-system`)
2. Extract design_handoff (structured data)
3. Supplement with domain searches
4. Build Color Token Proposal (fill temp1.json gaps)

**Gate 0:**
- `design_handoff.colors` phải có ít nhất 5 HEX values.
- `design_handoff.typography` phải có concrete font names.
- Nếu fail: dùng defaults từ colors.csv + typography.csv.

**Sinh `design_handoff`:**

```
design_handoff:
  style:              # name, keywords, accessibility
  colors:             # primary, secondary, cta, background, text, border (HEX)
  typography:         # heading_font, body_font, mood
  component_specs:    # structured spec cho buttons, cards, inputs (no CSS)
  spacing:            # xs through 2xl (pt/dp)
  shadows:            # sm, md, lg
  color_token_proposals: # proposed tokens to fill temp1.json gaps
```

### Khi skip (có figma_source)

Figma variables được transform thành cùng format `design_handoff`:
- `get_variable_defs` → `colors`, `spacing`, `typography`
- `get_design_context` → `component_specs` (từ Figma component instances)
- Token proposals = Figma variables chưa có trong temp1.json

---

## Skill 1: prd-crossfile-mapping (5 bước lõi)

Đọc và áp dụng: `.cursor/skills/prd-crossfile-mapping/SKILL.md`

**Input:**
- `target_dir` = `prd_folder`
- `overview_file` = file overview đã detect
- `include_files[]` và `exclude_files[]`

### 5 bước lõi (giảm từ 10)

| # | Bước | Gộp từ v2 | Mô tả |
|---|------|-----------|-------|
| 1 | File Registry + Dependencies | Step 1+2+3 | Liệt kê files, scan links, phân loại upstream/downstream |
| 2 | Shared Field Catalog | Step 4+5 | Fields xuất hiện 2+ files, gồm entry vs display mapping |
| 3 | Inconsistency Detection | Step 7+8 | Impact rules + conflict detection trong 1 pass |
| 4 | Canonical Field Contract | Step 9 | Resolve alias drift, 1 canonical name per concept |
| 5 | Priority Findings | Step 6+10 | Summary + mermaid diagram (presentation) |

**Tại sao gộp:** Step 5 (Cross-Display), Step 6 (Supporting-Info), Step 7 (Impact Map) là **view khác nhau của cùng data** từ Step 3+4. Sinh tự động từ dependency graph + shared fields, không cần scan file thêm lần nào.

**Gate 1:**
- Mọi factual row phải có `source_file` + `source_anchor`.
- Nếu thiếu citation ở conflict rows: dừng, báo gap.

**Sinh `crossfile_handoff`:**

```
crossfile_handoff:
  file_registry:      # file, purpose, key_entities, entry_points
  dependencies:       # provider_file, consumer_file, relationship
  shared_fields:      # canonical_field, db_key, appears_in_files, type, required
  inconsistencies:    # conflict_id, conflict_type, file_a, definition_a, file_b, definition_b
  canonical_contract: # canonical_field, aliases, canonical_type, canonical_enum, required, owner_module
```

---

## Skill 2: pdr-extract-analyze (N feature files)

Đọc và áp dụng:
- `.cursor/skills/pdr-extract/SKILL.md`
- `.cursor/skills/pdr-analyze/SKILL.md` (chỉ Bước 1: suy case ngầm)
- Rule: `.cursor/rules/pdr-component-pipeline.mdc`

**Thay đổi so v2:** Gộp extract (Skill 2a) + analyze Bước 1 (suy case ngầm). **KHÔNG map token** (dồn cho Skill 3). Không chạy 6 CSV augment (dồn cho Skill 3).

### Lặp theo từng feature file

**Input mỗi file:**
- `feature_md` = feature file hiện tại
- `overview_md` = file overview
- `crossfile_handoff` (dùng dependencies + canonical_contract)

**Chạy 4 bước gọn:**

| # | Bước | Mô tả | Output |
|---|------|-------|--------|
| 1 | Ngữ cảnh Overview | Đọc scope, integrations, related modules | scope_mvp, integrations |
| 2 | Parse Mô tả màn hình | Extract screen_registry + component_registry (prd_type → component_key, group) | screen_registry, component_registry |
| 3 | Đối chiếu hành vi | Scan User Flow + User Story + NFR → behavior_rules per component | behavior_rules, cross_references |
| 4 | Suy case ngầm | Đọc cột "Mô tả" → suy case từ pattern (khi/nếu, ẩn/hiện, đếm ngược, v.v.) | case_matrix (COMPbase) |

**KHÔNG làm:**
- Map token (Skill 3 sẽ làm 1 lần)
- Tra 6 CSV (Skill 3 sẽ làm 1 lần)
- Sinh UX writing (Skill 3)

**Khi có `figma_source`:** Bước 2 sinh thêm `figma_context_registry` từ Figma layer names + text nodes.

### Gộp kết quả thành `pdr_handoff`

```
pdr_handoff:
  merged_screen_registry:     # gộp từ mọi feature, ghi rõ source_file
  merged_component_registry:  # gộp, giữ screen + source_file + description gốc
  case_matrix:                # gộp, COMPbase only (chưa có COMPextend)
  behavior_rules:             # gộp, per component + citation
  cross_references:           # gộp, module → module impacts
  figma_context_registry:     # bảng context Figma (chỉ khi có figma_source)
```

**Gate 2:**
- Mọi component trong registry phải có citation PDR.
- Mọi case trong case_matrix phải có citation.
- Nếu fail: ghi vào Assumptions, tiếp tục Skill 3.

---

## Skill 3: comp-token-augment (1 lần duy nhất)

Đọc và áp dụng:
- `.cursor/skills/comp-extraction/SKILL.md` (Phase 3-8)
- `.cursor/skills/pdr-analyze/SKILL.md` (Bước 2-3: 6 CSV augment + token mapping)
- Rule: `.cursor/rules/comp-extraction.mdc`

**Thay đổi so v2:** Gộp token mapping + UX augment + comp-extraction Phase 3-8 thành **1 lần duy nhất** trên merged data (thay vì N lần per file + lặp lại trong Skill 3).

### Input

- `pdr_handoff` (Skill 2) — component_registry, case_matrix, behavior_rules đã merge
- `crossfile_handoff` (Skill 1) — canonical_contract, shared_fields, inconsistencies
- `design_handoff` (Skill 0 hoặc Figma)
- `figma_context_registry` (khi có figma_source)
- `temp1.json`
- 6 CSV: ux-guidelines, web-interface, colors, typography, styles, icons

### Chạy 6 phase (gọn từ 8+4)

| # | Phase | Gộp từ v2 | Mô tả |
|---|-------|-----------|-------|
| 1 | Normalize | Skill 3 Phase 3 | Chuẩn hóa component_key, áp dụng canonical_contract, resolve aliases |
| 2 | Map States | Skill 3 Phase 4 + Skill 2b Bước 1 | Gán state set cho mỗi component, dùng case_matrix làm baseline |
| 3 | Map Tokens (1 lần) | Skill 2b Bước 3 + Skill 3 Phase 5 | Resolution chain 7 bước trên **toàn bộ merged registry** (không lặp N lần) |
| 4 | Coverage Diff | Skill 3 Phase 6 | Tìm missing_components, missing_states, missing_tokens |
| 5 | UX Augment | Skill 2b Bước 2 + Skill 3 Phase 7 | Tra 6 CSV, sinh COMPextend (components + states + UX writing + UI enrichment) |
| 6 | Output | Skill 3 Phase 8 | Sinh JSON + Markdown |

### Phase 3: Token Resolution Chain (chạy 1 lần)

```
1. temp1.json "4. Custom".modes.Mobile        → resolved_from: "temp1.json"
2. design_handoff.colors                       → resolved_from: "design_handoff"
3. design_handoff.component_specs              → resolved_from: "design_handoff"
4. design_handoff.color_token_proposals        → resolved_from: "design_handoff"
5. colors.csv (match product type)             → resolved_from: "colors.csv"
6. styles.csv (Design System Variables)        → resolved_from: "styles.csv"
7. Fallback: missing_token + proposed_name + proposed_value
```

Chạy trên **toàn bộ merged_component_registry** 1 lần. Không lặp per feature file.

### Phase 5: UX Augment (tra 6 CSV 1 lần)

Tra `ux-guidelines.csv`, `web-interface.csv`, `colors.csv`, `typography.csv`, `styles.csv`, `icons.csv` trên **toàn bộ merged data** 1 lần. Sinh:
- `comp_extend_components[]`
- `comp_extend_state_extensions[]`
- `ux_writing_proposals[]`
- `ui_enrichment_proposals[]`

### Sinh `comp_output`

```
comp_output:
  component_registry:         # normalized, deduplicated
  state_matrix:               # COMPbase + COMPextend, per component
  token_mapping:              # resolved + proposed + missing
  missing_components:         # gap list
  missing_states:             # gap list
  missing_tokens:             # truly unresolved
  comp_extend_components:     # UX proposals
  comp_extend_states:         # UX state proposals
  ux_writing_proposals:       # error, empty, success, retry
  ui_enrichment_proposals:    # detail enrichment
  figma_context_registry:     # passthrough (enriched with canonical_key)
  quality_gates:              # citation_coverage, token_resolution_rate, etc.
```

**Gate 3:**
- Citation 100% cho COMPbase.
- Token resolution rate >= 70%.
- UX writing cover ít nhất: error, empty, success.
- Nếu fail: ghi Gap Report.

---

## Skill 4: visual-spec-gen (spec files + mockup-spec.json)

Đọc và áp dụng: `.cursor/skills/visual-spec-gen/SKILL.md`

### Input

- `design_handoff` (Skill 0 hoặc Figma)
- `crossfile_handoff` (Skill 1)
- `pdr_handoff` (Skill 2)
- `comp_output` (Skill 3)
- `figma_context_registry`
- `temp1.json`
- `target_platform`, `target_stack`, `prd_folder`

### Chạy 4 sections + 1 JSON

| # | Section | Mô tả |
|---|---------|-------|
| 1 | Token Dictionary | Mobile baseline + Desktop overrides (từ temp1.json + resolved tokens) |
| 2 | Component UI Spec | Per-component structure: props, states, tokens, touch validation. No CSS. |
| 3 | Screen Layout Specs | Per-screen mobile layout skeleton (component tree) |
| 4 | Implementation Guide | Mobile checklist + quality gates + file index |
| 5 | **mockup-spec.json** | **Deliverable chính**: component UI JSON có state coverage (xem schema dưới) |

**Gate 4:**
- Token Dictionary cover 100% resolved tokens.
- Mỗi interactive component có touch_target_check.
- Mỗi screen có component_tree trong mockup-spec.json.
- Mỗi component có >= 1 state trong mockup-spec.json.

### mockup-spec.json Schema

```json
{
  "meta": {
    "target_platforms": ["ios", "android"],
    "target_stack": "flutter",
    "product_type": "Retail Banking",
    "figma_source": "figma:fileKey/nodeId",
    "generated_at": "ISO-8601",
    "schema_version": "mockup-spec-v1",
    "pipeline_version": "v3"
  },
  "design_system": {
    "colors": { "primary": "#HEX", "secondary": "#HEX", "cta": "#HEX" },
    "typography": { "heading_font": "string", "body_font": "string" },
    "spacing": { "xs": "4", "sm": "8", "md": "16", "lg": "24" }
  },
  "screens": [
    {
      "screen_id": "chuyen-tien-noi-bo",
      "screen_name": "Chuyển tiền nội bộ cùng chủ",
      "source": "feature.md#Wireframe",
      "figma_source": "figma:fileKey/nodeId",
      "component_tree": [
        {
          "component_key": "header",
          "children": []
        },
        {
          "component_key": "balance-card",
          "children": [
            { "component_key": "icon-chevron", "children": [] }
          ]
        },
        {
          "component_key": "section-header",
          "props": { "label_key": "section.transfer" },
          "children": [
            { "component_key": "text-field", "children": [] },
            { "component_key": "text-field", "children": [] }
          ]
        }
      ]
    }
  ],
  "components": [
    {
      "component_key": "button-primary",
      "group": "Navigation/Action",
      "screens": ["chuyen-tien-noi-bo", "confirmation"],
      "props": {
        "label_key": "button.continue",
        "accessibility_label": "Tiếp tục"
      },
      "tokens": {
        "background": "{custom.cta}",
        "text_color": "{custom.cta_text}",
        "border_radius": "{radius.md}"
      },
      "touch_target": { "min_dp": 44, "check": "pass" },
      "states": [
        {
          "state": "default",
          "visual_description": "Gradient background, white text",
          "token_changes": {},
          "trigger": null,
          "status": "COMPbase",
          "source": "figma:fileKey/nodeId"
        },
        {
          "state": "disabled",
          "visual_description": "Grayed out, not clickable",
          "token_changes": { "background": "{custom.disabled_bg}", "opacity": "0.5" },
          "trigger": "Form validation incomplete",
          "status": "COMPextend",
          "source": "ux-guidelines.csv#10"
        },
        {
          "state": "loading",
          "visual_description": "Spinner icon, disabled",
          "token_changes": {},
          "trigger": "Submit in progress",
          "status": "COMPextend",
          "source": "ux-guidelines.csv#10"
        }
      ],
      "figma_context_label": "Tiếp tục"
    }
  ],
  "figma_context_registry": [
    {
      "context_label": "Thông tin chuyển tiền",
      "context_type": "section",
      "figma_source": "figma:fileKey/134:19702",
      "screen_id": "chuyen-tien-noi-bo",
      "canonical_key": "section.transfer"
    }
  ],
  "ux_copy": [
    {
      "screen_id": "chuyen-tien-noi-bo",
      "component_key": "button-primary",
      "writing_type": "label",
      "text": "Tiếp tục",
      "status": "COMPbase",
      "source": "figma:fileKey/nodeId"
    },
    {
      "screen_id": "chuyen-tien-noi-bo",
      "component_key": "text-field",
      "writing_type": "error",
      "text": "Vui lòng nhập số tiền.",
      "status": "COMPextend",
      "source": "ux-guidelines.csv#10"
    }
  ],
  "gaps": {
    "state_gaps": [],
    "token_gaps": [],
    "interaction_gaps": [],
    "ux_improvement_proposals": []
  },
  "quality_gates": {
    "citation_coverage": "100%",
    "token_resolution_rate": "70%",
    "state_coverage": "8/8",
    "ux_writing_coverage": "error+empty+success",
    "touch_target_compliance": "15/15"
  }
}
```

### Sinh file output

```
{prd_folder}/ui-automation/
  ├── mockup-spec.json          ← DELIVERABLE CHÍNH (luôn tạo)
  ├── generation-manifest.md    ← Section 4 (read first)
  ├── figma-context-registry.md ← Bảng context Figma (chỉ khi có figma_source)
  ├── token-dictionary.md       ← Section 1
  ├── token-gap-registry.md     ← Missing tokens
  ├── component-catalog.md      ← Section 2 (human-readable view of mockup-spec.json)
  ├── state-visual-guide.md     ← State matrix
  ├── ux-copy-bank.md           ← UX writing proposals
  └── screen-specs/
      ├── screen-{name}.md      ← Section 3 (1 file per screen)
      └── ...
```

---

## Final Output

### A) mockup-spec.json (luôn tạo — DELIVERABLE CHÍNH)

File JSON tổng hợp component + state + token + figma context. Dùng trực tiếp cho:
- Tạo mockup (Figma plugin, AI mockup gen)
- Đề xuất UX improvement (COMPextend + state gaps + ux_writing)
- Cover state (mỗi component liệt kê states + visual description + trigger)
- Handoff cho iOS/Android dev

### B) Pipeline Summary (Markdown, luôn trả)

7 mục (giảm từ 14):

| # | Mục | Gộp từ v2 | Nội dung |
|---|-----|-----------|----------|
| 1 | **Design System + Token** | v2 mục 1+7+8 | Style, colors, typography + Token Dictionary + Responsive overrides |
| 2 | **Dependencies + Inconsistencies** | v2 mục 2+3 | Priority findings + mermaid diagram + conflicts |
| 3 | **Component Registry + State** | v2 mục 4+6+9+10 | Gộp COMPbase + COMPextend (tách bằng cột status), gồm component + state + COMPextend proposals |
| 4 | **Figma Context Registry** | v2 mục 5 | Bảng context Figma (chỉ khi có figma_source) |
| 5 | **UX Writing** | v2 mục 11 | Labels, error, empty, success, retry |
| 6 | **Component UI Spec** | v2 mục 12 | Per-component JSON structure + state. No CSS. |
| 7 | **Gaps + Assumptions** | v2 mục 13+14 | Missing tokens + missing states + unspecified + conflicts |

### C) UI Automation Files (.md, luôn tạo)

Tự động generate vào `{prd_folder}/ui-automation/` bởi Skill 4.

### D) Full JSON (khi user yêu cầu)

Theo output contract của comp-extraction v3, bổ sung:
- `crossfile.dependencies[]`, `crossfile.shared_fields[]`, `crossfile.conflicts[]`
- `design_system.colors`, `design_system.typography`

---

## Ràng buộc chung

### Mobile-First (iOS + Android)
- `target_platform = mobile` (iOS + Android) là mặc định.
- Token resolution từ temp1.json dùng Mobile mode làm baseline.
- Touch targets >= 44pt/dp là COMPbase cho interactive components.
- **No CSS**: pipeline không sinh CSS; deliverable là `mockup-spec.json`.

### Source of Truth
- PRD markdown là nguồn duy nhất cho dữ liệu gốc.
- Không suy luận hành vi từ free text khi thiếu anchor evidence.

### Anchor hợp lệ
- `User Flow`
- `User Story` (`Business Rule`, `Acceptance Criteria`)
- `Wireframe > Mô tả màn hình`
- `Thiết kế Database`
- `Non-functional requirement`
- `Phạm vi sản phẩm` (`In Scope (MVP)`, `Out of Scope & Roadmap`)

### COMPbase vs COMPextend
- `COMPbase`: evidence trực tiếp từ PRD anchor + mobile-first requirements (touch targets).
- `COMPextend`: bổ sung từ ui-ux-pro-max hoặc suy luận UX.
- KHÔNG trộn COMPextend vào số liệu COMPbase.

### State chuẩn
- `default`, `focus`, `active`, `disabled`, `loading`, `error`, `success`, `empty`

### Token Resolution Chain (chạy 1 lần trong Skill 3)
```
1. temp1.json "4. Custom".modes.Mobile
2. design_handoff.colors (Skill 0 hoặc Figma)
3. design_handoff.component_specs
4. design_handoff.color_token_proposals
5. colors.csv (product type match)
6. styles.csv (Design System Variables)
7. Fallback: missing_token + proposed_name + proposed_value
```

### Token Hierarchy (within temp1.json)
1. `TailwindCSS`
2. `Theme` (`Default`, `VNPAY`)
3. `Mode` (`Light`, `Dark`)
4. `Custom` (`Desktop`, `Mobile` -- Mobile first)

Format: `{collection.token}`. Không hardcode khi có token tương đương.

### Citation
- COMPbase: 100% citation (`source_file`, `source_anchor`).
- COMPextend: bắt buộc `ux_rule_ref`.
- Giá trị thiếu: `UNSPECIFIED` hoặc `missing_token` kèm `proposed_token_name` + `proposed_value`.
- Token resolved từ chain: `RESOLVED_PROPOSED` kèm `resolved_from`.

---

## So sánh v2 → v3

| Metric | v2 | v3 | Cải thiện |
|--------|----|----|-----------|
| Số skill | 5 (luôn chạy) | 4 (Skill 0 conditional) | -1 skill khi có Figma |
| Bước Skill 1 | 10 | 5 | -50% |
| Token mapping | N lần (per file) | 1 lần cuối | **-N+1 lần** |
| 6 CSV augment | N lần (per file) | 1 lần cuối | **-N+1 lần** |
| Trùng Skill 2b / Skill 3 | ~60% trùng | 0% (gộp) | **Xóa trùng** |
| Output sections | 14 | 7 | -50% |
| Deliverable chính | 7 file .md | `mockup-spec.json` + .md | JSON first |
| Tổng bước (8 files) | ~83 | ~44 | **-47%** |
| CSS output | Có (component-catalog) | Không (no CSS) | Platform agnostic |

### Backward Compatibility

- `.cursor/skills/pdr-extract/SKILL.md`: vẫn dùng nguyên (Skill 2 Bước 1-3).
- `.cursor/skills/pdr-analyze/SKILL.md`: dùng Bước 1 trong Skill 2, Bước 2-3 trong Skill 3.
- `.cursor/skills/comp-extraction/SKILL.md`: dùng Phase 3-8 trong Skill 3.
- `.cursor/skills/visual-spec-gen/SKILL.md`: vẫn dùng (Skill 4), bổ sung Section 5 (mockup-spec.json).
- `.cursor/skills/prd-crossfile-mapping/SKILL.md`: vẫn dùng, pipeline chỉ chạy 5 bước lõi (skill file giữ nguyên 10 bước cho standalone use).
- 7 file .md automation: vẫn sinh (backward compatible), bổ sung `mockup-spec.json`.
