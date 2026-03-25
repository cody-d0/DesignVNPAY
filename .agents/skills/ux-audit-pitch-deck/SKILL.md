---
name: ux-audit-pitch-deck
description: Generate a professional, industry-standard UX Audit Pitch Deck as a single-file HTML deliverable from ux-review-report.md and pipeline output. Use when the user requests a pitch deck, presentation, or professional deliverable from UX audit data. Triggers include "pitch deck", "presentation", "deliverable", "HTML report", "audit deck", "industry-standard report". Requires completed ux-review-report.md and .handoff/ directory with screen_inventory.json, flow_graph.json, and ddl-context.json (produced by figma-to-ux-review workflow). This skill is invoked as Phase 4 of the figma-to-ux-review workflow.
---

# UX Audit Pitch Deck Generator

Generate a professional HTML pitch deck from UX audit pipeline output. Single-file, zero dependencies, offline-capable. Light theme, WCAG AA compliant.

## Industry Standard Structure (NNg-aligned)

The deck MUST follow this 6-section structure:

| # | Section | Content |
|:--|:--------|:--------|
| 1 | **Hero** | Product name, module, total stats (screens, checks, gaps, proposals), overall score ring |
| 2 | **Tổng quan** | Severity breakdown badges, screen score cards with individual score rings |
| 3 | **Phương pháp** | 4 evaluation methods: Heuristic, Component Spec, Vision, UX Law |
| 4 | **Phát hiện** | UXP finding cards grouped by severity (Critical → Major → Minor), each with phone-frame screenshot + structured info |
| 5 | **Scorecard** | SVG score rings per heuristic category (6 categories) |
| 6 | **Gaps** | Detailed gap checklist grouped by screen, each gap with user impact, heuristic, and evidence |

## Mandatory Rules

1. **Sanitize PII**: Remove all fake account numbers, names, phone numbers, transaction IDs. Use generic descriptions.
2. **No abbreviations**: Write all terms in full Vietnamese — "Tài khoản" not "TK", "giao dịch" not "GD".
3. **Every UXP with screenshot**: Each finding card MUST embed a real screenshot inside a `.phone-frame` container.
4. **NNg heuristic references**: Each finding MUST cite the violated heuristic by name.
5. **Progressive disclosure**: Technical DDL references go inside `<details>` tags.
6. **No internal pipeline metadata**: No quality gate sections, pipeline timestamps, or internal tooling references.
7. **No hardcoded dates**: Footer contains DDL context info and product name only.

## Input Requirements

Read from:
- `{dir}/ux-review-report.md` — raw UX review with findings
- `{dir}/.handoff/screen_inventory.json` — screen data + image paths
- `{dir}/.handoff/ddl-context.json` — DDL component specs + guidelines
- `{dir}/*.md` — screen specification files (SCR-XXX) for state/overlay context
- `{dir}/*/ui/*.png` — actual screenshots

## Generation

### Option 1: Script (recommended — deterministic)

Run the bundled generator for consistent, deterministic output:

```bash
python3 {skill}/scripts/generate.py \
    --report {dir}/ux-review-report.md \
    --ui-dir {dir}/*/ui/ \
    --product "Product Name" \
    --client "Client Name" \
    --module "Module Name"
```

`--output` is **optional** — auto-generates ASCII filename from folder hierarchy:
```
Dịch vụ thẻ/Kích hoạt thẻ → dich-vu-the--kich-hoat-the--pitch-deck.html
Chuyển tiền/Trong hệ thống → chuyen-tien--trong-he-thong--pitch-deck.html
```

The script:
- Parses ux-review-report.md (supports 4 format variants: A, B, C, D)
- Extracts gaps with screen grouping
- Maps heuristics deterministically (20+ pattern rules)
- Infers user impact from check descriptions
- Generates SVG score rings with exact math
- Resolves image paths with 6-tier strategy:
  - Tier 1: Explicit `evidence_img` from report
  - Tier 1.5: **Screen MD-based check→image mapping** (authoritative, from `parse_screen_specs`)
  - Tier 2: Cross-reference `all_imgs`
  - Tier 2.5: Artboard ID match
  - Tier 3: State-aware keyword scoring
  - Tier 4-5: Inventory + fuzzy fallback
- **Augments shallow UXP hiện trạng** with screen MD context (state enumeration, overlay context, artboard evidence)
- Reads CSS from assets/template.html (single source of truth)
- Auto-generates ASCII filename from Vietnamese folder path
- Outputs JSON summary to stdout

### Option 2: Manual (fallback)

If the script cannot run, populate template.html manually:
1. Copy `assets/template.html` to output location
2. Replace all `{{PLACEHOLDER}}` tokens with data from inputs
3. Calculate SVG score rings using formulas below

## Output

Single file: `{dir}/pitch-deck.html`

JSON summary (from script stdout):
```json
{
  "screens": 3, "checks": 9, "gaps": 4,
  "proposals": 5, "score": 56,
  "critical": 3, "major": 2, "minor": 0,
  "images_mapped": 5, "images_available": 18
}
```

## Design System

Use the design tokens defined in [references/design-system.md](references/design-system.md). Template CSS already implements these tokens.

## Finding Card Layout

Each UXP finding uses a 2fr:3fr phone-frame layout:

```
┌────────────────────────────────────────────────────┐
│ [severity accent bar: 4px colored strip]           │
│ ┌──────────────────┬───────────────────────────┐   │
│ │  ┌────────────┐  │ UXP-XXX  [severity badge] │   │
│ │  │            │  │ Full descriptive title      │   │
│ │  │ screenshot │  │ Tác động: description       │   │
│ │  │ (phone     │  │ Heuristic: Name (#N)        │   │
│ │  │  frame)    │  │ ┌─ Proposed box ──────────┐ │   │
│ │  │            │  │ │ • improvement items     │ │   │
│ │  └────────────┘  │ └────────────────────────┘ │   │
│ │  ⚠️ Overlay label │ [screen tags]              │   │
│ │      (2fr)       │ ▸ Xem tham chiếu → (3fr)  │   │
│ └──────────────────┴───────────────────────────┘   │
└────────────────────────────────────────────────────┘
```

Findings are **grouped by severity** with colored group headers:
- 🔴 Critical — Cần xử lý ngay (red header)
- 🟡 Major — Ưu tiên cao (orange header)
- ⚪ Minor — Cải thiện (amber header)

## Score Ring SVG Formulas

```
stroke-dashoffset = circumference × (1 - score/100)

Overall hero:    r=51, circumference=320
Screen scores:   r=25, circumference=157
Heuristic rings: r=33, circumference=207

Color: <50% → sev-critical, 50-69% → sev-major, ≥70% → sev-pass
```

## Post-generation Tools

### Image Fix (repairs incorrect image mappings)

Uses a 7-strategy resolution chain (S1 gap-ref → S2 direct → S3 screen-hdr → S4 artboard-ID → S5 gap-check → S6 screen-check → S7 fuzzy → S8 proportional).

```bash
python3 {skill}/scripts/fix_images.py audit --base /path/to/project
python3 {skill}/scripts/fix_images.py fix --base /path/to/project [--dry]
```

### Audit (validates structural integrity)

Checks hero, scorecard, sections, nav, image existence, dominance, empty alts, and generic "Từ ảnh" references.

```bash
python3 {skill}/scripts/audit.py --base /path/to/project [--json /tmp/results.json]
```

### Enrichment Cache

`enrich.py` supports cache validation — skips re-enrichment if the report hasn't changed (MD5 hash match). Use `--force` to bypass:

```bash
python3 {skill}/scripts/enrich.py --report path/to/ux-review-report.md --force
```

## Screen MD-Based Image Resolution

When screen specification `.md` files exist alongside the report (e.g., `danh-sach-the.md`, `thong-tin-the.md`), the generator parses them to build an authoritative check→image mapping:

1. `parse_screen_specs()` — extracts `wireframe_images`, `states`, and `overlays` with keywords from each screen MD
2. `build_check_image_map()` — maps `Check #N (SCR-XXX)` references to the most contextually relevant image using keyword overlap
3. `build_check_content_map()` — extracts check content from report tables for context enrichment

This provides **Tier 1.5** resolution (after explicit evidence_img, before cross-reference fallbacks), ensuring OTP-related checks map to OTP artboards, empty-state checks map to empty state artboards, etc.

## UXP Reasoning Augmentation

`augment_uxp_hien_trang()` automatically enriches shallow UXP descriptions (< 100 chars, typically from Format D table-only reports) using screen MD context:

| Issue Type | Augmentation |
|---|---|
| **Overlay-specific** (OTP, PIN, Date Picker) | Prepends `Overlay "Name" trên SCR-XXX:` context |
| **Screen-wide** (color, accessibility) | Prepends `Tất cả N trạng thái (state1, state2...) đều` |
| **Missing state** (error, validation, empty) | Appends `Trong N artboard của biên SCR-XXX, không có artboard nào thể hiện` |
| **Already detailed** (≥ 100 chars, Format A/B) | Preserved unchanged |

False positive prevention: requires ≥2 keyword overlap for overlay matching, or explicit overlay terms (`\boverlay\b`, `\botp\b`, `\bpin\b.*auth`) in the text.
