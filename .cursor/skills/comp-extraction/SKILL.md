---
name: comp-extraction
description: Extract components, states, and token mappings from PRD/PDR docs with citation-first evidence and dual outputs (JSON + Markdown) for Generated UI pipelines. Use when users ask for PRD-to-UI mapping, component registry extraction, state coverage, or token mapping from PRD anchors.
---

# Comp Extraction

## When to Apply

Use this skill when the request involves:

- PRD/PDR to UI generation mapping
- Component extraction from `Wireframe` tables
- State mapping from `User Story` and `Non-functional requirement`
- Token mapping using `temp1.json` hierarchy
- Building reusable UI specs from PRD-like docs
- Closing missing UI/UX states to approach full case coverage
- Improving UX writing quality from PRD baselines

## Required Inputs (v2)

Run this skill with explicit runtime inputs:

- `md_files[]` (required): list of `.md` PRD/PDR files to process in one run.
- `token_file` (optional, default `temp1.json`): token reference source.
- `target_mode` (optional, default `Mobile`): `Mobile` or `Desktop`.
- `target_theme` (optional, default `Default`): `Default` or `VNPAY`.
- `output_mode` (optional): `single-file` or `merged`.

Multi-file behavior:

1. Process each file in `md_files[]` independently for extraction and citation.
2. Merge outputs only after per-file extraction is complete.
3. Keep row-level provenance (`source_file`, `source_anchor`, `line_range`) in merged outputs.
4. For conflicting rows (same `component_key` + state), keep all variants and mark conflict in `assumptions_unspecified`.

## Source of Truth and Anchor Policy

- PRD/PDR is the only source of truth for component/state behavior.
- Primary extraction focus:
  - `Wireframe > Mô tả màn hình` (component inventory baseline)
  - `temp1.json` (token hierarchy baseline)
- Extract only from approved anchors:
  - `User Flow`
  - `User Story` (`Business Rule`, `Acceptance Criteria`)
  - `Wireframe > Mô tả màn hình`
  - `Thiết kế Database`
  - `Non-functional requirement`
  - `Phạm vi sản phẩm` (`In Scope (MVP)`, `Out of Scope & Roadmap`)
- If anchor evidence is missing, return `UNSPECIFIED` (do not infer).

## Dual-Layer Model (Required)

Always produce two explicit layers:

1. `COMPbase Layer` (facts from PRD anchors only)
2. `COMPextend Layer` (improvements from `ui-ux-pro-max` for full case/full state/full UX writing)

Rules:

- Never mix COMPextend items into COMPbase counts/mappings.
- COMPextend items must include `proposal_basis` and `ui_ux_rule_ref`.
- COMPbase items keep strict citation from PRD.

## Supported PRD Table Headers

- `Bước | Tên màn hình | Tên hành động | Kết quả`
- `Epic chung | Mã US | Tiêu đề | Mô tả chi tiết | Business Rule | Acceptance Criteria`
- `STT | Tên màn hình | Loại thành phần | Mô tả`
- `Field | Data Type | Constraint | Description`
- `STT | Tên tính năng | Mô tả`
- `STT | Tài liệu | Mô tả chức năng`

## Extraction Pipeline

### Phase 1 - Extract

1. Build `screen_registry` from `User Flow` + `Wireframe`.
2. Build `component_registry` from `Wireframe > Mô tả màn hình` (`Loại thành phần`).
3. Collect evidence anchors (`file`, `section`, `line_range`, excerpt).

### Phase 2 - Extract Component Props from `Mô tả màn hình`

Derive component-level details from the `Mô tả` column and keep citation-first records.

- Build `component_props_from_prd[]` rows:
  - `screen_id`
  - `component_key`
  - `prop_key`
  - `prop_value_excerpt`
  - `source_file`
  - `source_anchor`
  - `line_range`
- Only include values explicitly present in PRD text.
- If the value is implied but not explicit, output `UNSPECIFIED`.

Example:

- `Header` -> `greeting_text = "Chào buổi sáng"`
- `Header` -> `store_name = "Cửa hàng ABC"`

### Phase 3 - Normalize

1. Normalize `prd_type -> component_key`.
2. Group component into one of:
   - `Input/Form`
   - `Layout`
   - `Navigation/Action`
   - `Search/Filter`
   - `Cards/Lists`
   - `Info/Feedback`
   - `Special`
3. If unknown `prd_type` appears:
   - keep original value
   - create normalized fallback key
   - mark `NEW_KEY_CANDIDATE`

### Phase 4 - Map States

- State set:
  - `default`, `focus`, `active`, `disabled`, `loading`, `error`, `success`, `empty`
- Assign `COMPbase` only with PRD evidence.
- Otherwise mark `UNSPECIFIED`.
- Respect dependency rules; do not multiply unrelated states/variables.

### Phase 5 - Map Tokens (Mobile-First + Resolution Chain)

**Primary source**: `temp1.json` with **Mobile mode as baseline**.

**Step 5a -- temp1.json resolution (mobile-first):**

- Resolve in strict hierarchy within temp1.json:
  1. `TailwindCSS`
  2. `Theme` (`Default`, `VNPAY` based on `target_theme`)
  3. `Mode` (`Light`, `Dark`)
  4. `Custom` -- always resolve from `Mobile` mode first. Desktop values only appear in `desktop_override` column when different from Mobile.
- Use token references in `{collection.token}` format.
- If token exists in temp1.json: `resolved_from = "temp1.json"`, `status = "RESOLVED"`.

**Step 5b -- Resolution Chain for missing tokens:**

When a token is not found in temp1.json, resolve through this chain (stop at first match):

```
1. temp1.json "4. Custom".modes.Mobile        → resolved_from: "temp1.json"
2. design_handoff.colors                       → resolved_from: "design_handoff"
3. design_handoff.component_specs              → resolved_from: "design_handoff"
4. design_handoff.color_token_proposals        → resolved_from: "design_handoff"
5. colors.csv (match product type)             → resolved_from: "colors.csv"
6. styles.csv (Design System Variables column) → resolved_from: "styles.csv"
7. Fallback: missing_token + proposed_name + proposed_value
```

`design_handoff` is the output of Skill 0 (design-system-gen). When available, it provides:
- HEX color values for primary, secondary, CTA, background, text, error, success
- CSS specs for buttons, cards, inputs, modals
- Color Token Proposals mapping common missing tokens to HEX values

**Step 5c -- Output columns (enhanced):**

Each token_mapping row now includes:
- `component_key`
- `state`
- `token_ref` -- `{collection.token}` if from temp1.json, or proposed token name
- `token_source_level` -- `TailwindCSS` | `Theme` | `Mode` | `Custom` | `design_system` | `csv`
- `resolution_mode` -- `Mobile` (baseline) | `Desktop` (only as override)
- `status` -- `RESOLVED` | `RESOLVED_PROPOSED` | `missing_token`
- `proposed_token_name` -- when not in temp1.json
- `proposed_value` -- HEX/px/rem value when resolved from chain (NEW)
- `resolved_from` -- `temp1.json` | `design_handoff` | `colors.csv` | `styles.csv` | `missing` (NEW)
- `desktop_override` -- value only when Desktop differs from Mobile (NEW)

**Step 5d -- Mobile-first touch requirements:**

For all interactive components (buttons, links, inputs, cards with tap actions, bottom bar items):
- Verify `touch_target >= 44x44px` -- this is COMPbase (mobile-first requirement, not COMPextend)
- If PRD does not specify size, still mark as COMPbase requirement
- Add `touch_target_check` field: `pass` | `fail` | `unspecified`

### Phase 6 - Coverage Diff vs `temp1.json` + COMPbase Matrix

Build explicit gap sets after token/state mapping:

1. `missing_components[]`
   - component exists in PRD extraction but cannot be mapped to sufficient token coverage.
2. `missing_component_states[]`
   - component is present, but required/expected states are absent in COMPbase evidence and unresolved by token support.
3. `missing_tokens[]`
   - keep existing logic with `proposed_token_name`, `target_group`, and `mode`.

Comparison logic:

- Input for diff = `component_registry + state_matrix + token_mapping + component_props_from_prd`.
- Use `target_mode` and `target_theme` as the resolution filter.
- Never auto-delete COMPbase rows during diffing.

### Phase 7 - UX Gap Augmentation (ui-ux-pro-max)

Use `ui-ux-pro-max` after COMPbase extraction and coverage diff.

Input bundle to enrichment:

- COMPbase `component_registry`
- COMPbase `component_props_from_prd`
- COMPbase `state_matrix`
- `missing_components`
- `missing_component_states`
- COMPbase/missing `token_mapping`
- current `Wireframe > Mô tả màn hình`

Generate proposal sets:

1. `comp_extend_components`
2. `comp_extend_state_extensions`
3. `ux_writing_proposals`
4. `ui_enrichment_proposals` (new, component detail enrichment)

`ui_enrichment_proposals` is used for granular sub-component/prop completions that are described by PRD text but not represented in extracted keys.

Required fields:

- `proposal_type` = `ui_enrichment`
- `target`
- `proposal_key`
- `proposal_detail`
- `ui_ux_rule_ref`
- `priority`
- `impact`
- `proposal_basis`
- `status` = `COMPextend`

Priority order (must follow):

1. Accessibility + Touch + Interaction (Critical)
2. Layout + Performance (High)
3. Typography/Color + Animation + Content Writing (Medium)

### Phase 8 - Output

- Always return both:
  - machine-readable JSON
  - human-readable Markdown review

Source datasets for augmentation:

- `data/ux-guidelines.csv`
- `data/web-interface.csv`
- `data/ui-reasoning.csv`

## PRD Component Registry (Known Seed Set for xpos-app)

Seed mapping below is the initial dictionary and can be extended.

### Input/Form
- `Input Field` -> `InputField`
- `Input Field (SĐT)` -> `InputFieldPhone`
- `Input Field (Pass)` -> `InputFieldPassword`
- `Input Fields` -> `InputFields`
- `OTP Input` -> `OTPInput`
- `Pin Input` -> `PinInput`
- `Pass Fields` -> `PasswordFields`
- `Read-only Field` -> `ReadOnlyField`

### Layout
- `Header` -> `Header`
- `Header View` -> `HeaderView`
- `Footer` -> `Footer`
- `Sticky Footer` -> `StickyFooter`
- `Bottom Bar` -> `BottomBar`
- `Separator` -> `Separator`

### Navigation/Action
- `Button` -> `Button`
- `Button (Primary)` -> `ButtonPrimary`
- `Button (Outline)` -> `ButtonOutline`
- `Action Buttons` -> `ActionButtons`
- `Action Link` -> `ActionLink`
- `Link` -> `Link`
- `Logout Button` -> `LogoutButton`

### Search/Filter
- `Search Bar` -> `SearchBar`
- `Dropdown Filter` -> `DropdownFilter`
- `Filter Tabs` -> `FilterTabs`

### Cards/Lists
- `Card Item` -> `CardItem`
- `Product Card` -> `ProductCard`
- `Order Card` -> `OrderCard`
- `Statistic Cards` -> `StatisticCards`
- `Recent Orders List` -> `RecentOrdersList`
- `List Item` -> `ListItem`

### Info/Feedback
- `Infobox` -> `InfoBox`
- `Requirement Box` -> `RequirementBox`
- `Helper Text` -> `HelperText`
- `Growth Label` -> `GrowthLabel`
- `Success Header` -> `SuccessHeader`
- `Success Popup` -> `SuccessPopup`

### Special
- `Upload Area` -> `UploadArea`
- `Timer` -> `Timer`
- `Order Detail Summary` -> `OrderDetailSummary`
- `Payment Options` -> `PaymentOptions`
- `QR Code Container` -> `QRCodeContainer`
- `Bill Detail` -> `BillDetail`
- `Section Info` -> `SectionInfo`
- `Section Items` -> `SectionItems`
- `Form Section (1)` -> `FormSection1`
- `Form Section (2)` -> `FormSection2`
- `Switch` -> `Switch`
- `Dialog` -> `Dialog`

## Output Contract

### A) Markdown Output (v2, backward-compatible)

Keep legacy sections and add v2 sections for richer extraction.

1. `Nguồn trích`
2. `Component Registry (Unique)`
3. `Component Props from Mô tả màn hình` (new)
4. `State Mapping`
5. `Token Mapping`
6. `Missing Components & Missing States` (new)
7. `COMPextend Components (ui-ux-pro-max)`
8. `COMPextend State Extensions (ui-ux-pro-max)`
9. `UI Enrichment Proposals (ui-ux-pro-max)` (new)
10. `UX Writing Proposals (ui-ux-pro-max)`
11. `Assumptions & Unspecified`

#### `Component Registry (Unique)` columns

- `group`
- `prd_type`
- `component_key`
- `source_file`
- `source_anchor`
- `evidence_excerpt`

#### `State Mapping` columns

- `component_key`
- `state`
- `trigger_from_prd`
- `status` (`COMPbase` | `UNSPECIFIED`)
- `source_file`
- `source_anchor`

#### `Component Props from Mô tả màn hình` columns

- `screen_id`
- `component_key`
- `prop_key`
- `prop_value_excerpt`
- `source_file`
- `source_anchor`
- `line_range`

#### `Token Mapping` columns

- `component_key`
- `state`
- `token_ref`
- `token_source_level` (`TailwindCSS` | `Theme` | `Mode` | `Custom` | `design_system` | `csv`)
- `resolution_mode` (`Mobile` (baseline) | `Desktop` (override only))
- `status` (`RESOLVED` | `RESOLVED_PROPOSED` | `missing_token`)
- `proposed_token_name`
- `proposed_value` (HEX/px/rem when resolved from chain)
- `resolved_from` (`temp1.json` | `design_handoff` | `colors.csv` | `styles.csv` | `missing`)
- `desktop_override` (value only when Desktop differs from Mobile, empty otherwise)

#### `Missing Components & Missing States` columns

- `gap_type` (`missing_component` | `missing_component_state`)
- `component_key`
- `state` (nullable)
- `reason_gap_from_diff`
- `status` (`MISSING`)
- `source_file`
- `source_anchor`

#### `COMPextend Components (ui-ux-pro-max)` columns

- `screen_id`
- `proposal_component_key`
- `reason_gap_from_prd`
- `ui_ux_rule_ref`
- `priority`
- `impact`
- `status` (`COMPextend`)

#### `COMPextend State Extensions (ui-ux-pro-max)` columns

- `component_key`
- `proposal_state`
- `reason_gap_from_prd`
- `ui_ux_rule_ref`
- `priority`
- `status` (`COMPextend`)

#### `UI Enrichment Proposals (ui-ux-pro-max)` columns

- `screen_id`
- `component_key`
- `proposal_key`
- `proposal_detail`
- `ui_ux_rule_ref`
- `priority`
- `impact`
- `status` (`COMPextend`)

#### `UX Writing Proposals (ui-ux-pro-max)` columns

- `screen_id`
- `component_key`
- `writing_type` (`label` | `helper` | `error` | `empty` | `success` | `retry`)
- `proposal_text_vi`
- `ui_ux_rule_ref`
- `priority`
- `status` (`COMPextend`)

### B) JSON Output (machine-readable)

```json
{
  "meta": {
    "pdr_files": ["string"],
    "generated_at": "ISO-8601",
    "schema_version": "comp-extraction-v3",
    "token_file": "temp1.json",
    "target_mode": "Mobile",
    "target_theme": "Default",
    "design_handoff_available": true,
    "resolution_chain": ["temp1.json", "design_handoff", "colors.csv", "styles.csv"]
  },
  "sources": [
    {
      "file": "string",
      "anchor": "string",
      "line_range": "string"
    }
  ],
  "screen_registry": [],
  "component_registry": [],
  "component_props_from_prd": [],
  "state_matrix": [],
  "token_mapping": [],
  "missing_components": [],
  "missing_component_states": [],
  "comp_extend_components": [],
  "comp_extend_state_extensions": [],
  "ui_enrichment_proposals": [],
  "ux_writing_proposals": [],
  "missing_tokens": [],
  "assumptions_unspecified": [],
  "quality_gates": {
    "citation_coverage": 0,
    "unknown_key_count": 0,
    "unspecified_count": 0,
    "ux_gap_count": 0
  }
}
```

## Citation and Quality Rules

- Every row in `Component Registry (Unique)`, `State Mapping`, and `Token Mapping` must include citation fields.
- Every row in `Component Props from Mô tả màn hình` must include citation fields.
- Never output COMPbase mappings without `source_file` + `source_anchor`.
- Every COMPextend row must include `ui_ux_rule_ref` + `proposal_basis`.
- COMPextend rows must not claim `COMPbase`.
- If no anchor exists:
  - do not hard-map
  - return `UNSPECIFIED` or `missing_token`
- Report explicit gaps in `assumptions_unspecified`.

## Validation Playbook

Run dry-run checks on:

- `xpos-app/home.md` for dashboard patterns
- `xpos-app/order-payment.md` for payment and async-oriented components
- `xpos-app/settings.md` for settings/forms/dialog patterns

For `md_files[]`, validate with at least 2 input files in one run.

Validation checks:

1. Consistent `prd_type -> component_key` normalization.
2. New unknown keys are flagged `NEW_KEY_CANDIDATE`.
3. JSON schema keys are complete.
4. Markdown sections are in required order.
5. Citation coverage is 100 percent for COMPbase mappings.
6. COMPextend items are clearly separated from COMPbase items.
7. `component_props_from_prd` rows have full citation coverage.
8. `missing_components` and `missing_component_states` are reflected in proposal sections.
9. UX writing proposals cover at least: `error`, `empty`, `success`.
