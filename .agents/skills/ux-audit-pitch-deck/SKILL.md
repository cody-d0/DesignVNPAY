---
name: ux-audit-pitch-deck
description: Render a professional UX Audit Pitch Deck as single-file HTML from report-data.json. Pure renderer — no parsing, no enrichment, no data mutation. Triggers include "pitch deck", "render deck", "gen pitch", "HTML report", "audit deck". Requires report-data.json (produced by ux-audit-json-converter skill pipeline). This skill is the final consumer in the UX audit pipeline.
---

# UX Audit Pitch Deck — HTML Renderer

Render `report-data.json` → single-file HTML pitch deck. Zero dependencies, offline-capable.

## Role in Pipeline

```
ux-audit-json-converter          │  ux-audit-pitch-deck (THIS)
─────────────────────────────────┼──────────────────────────────
index_module.py → module-index   │
convert.py      → report-data    │
validate.py     → schema gate    │
evidence-img    → image enrich   │
evidence-info   → ref enrich     │
                                 │  render_report.py → pitch-deck.html
                                 │  audit.py         → quality check
```

**Boundary**: This skill ONLY reads `report-data.json`. It never parses markdown, never resolves images, never enriches data. All upstream work happens in `ux-audit-json-converter`.

## Scripts

| Script | Mục đích | Usage |
|--------|----------|-------|
| `scripts/render_report.py` | JSON → HTML renderer | `python3 render_report.py --module /path/to/module` |
| `scripts/audit.py` | Validate pitch deck output | `python3 audit.py --base /path/to/project` |

## Usage

```bash
# Single module
python3 scripts/render_report.py --module "/path/to/module/"

# Batch (all modules)
python3 scripts/render_report.py --base "/path/to/final/"

# Quality audit
python3 scripts/audit.py --base "/path/to/project/" [--json /tmp/results.json]
```

## Input Contract

Reads `report-data.json` with these required top-level keys:

| Key | Type | Content |
|-----|------|---------|
| `meta` | object | `client_name`, `product_name`, `module_name`, `section` |
| `stats` | object | `screen_count`, `check_count`, `gap_count`, `proposal_count`, `overall_score`, `overall_score_color`, `overall_score_offset`, `severity_counts` |
| `screens` | array | Per-screen score cards |
| `uxps` | array | UXP finding cards with `screenshot_path` |
| `gaps_by_screen` | array | Gaps grouped by screen |
| `heuristics` | array | 6-category heuristic scorecard |

### Enriched Fields (optional, from evidence-img/evidence-info)

| Field | Source | Rendered as |
|-------|--------|------------|
| `_enriched_narrative` | evidence-info | Richer "Hiện trạng" text |
| `_enriched_ref` | evidence-info | Canonical URL citation card |
| `_enriched_severity` | evidence-info | Severity justification in details |
| `_enriched_impact` | evidence-info | Override `user_impact` for gaps |
| `_enriched_sources` | evidence-info | Heuristic source tags on gaps |

## Output

Single self-contained HTML file: `{slug}--pitch-deck.html`

Filename auto-generated from module metadata:
```
Dịch vụ thẻ/Kích hoạt thẻ → dich-vu-the--kich-hoat-the--pitch-deck.html
```

## HTML Structure (6 sections)

| # | Section | Builder |
|:--|:--------|:--------|
| 1 | **Hero** | Product name, stats, overall score ring |
| 2 | **Tổng quan** | Severity badges, screen score cards |
| 3 | **Phương pháp** | 4 evaluation methods (static) |
| 4 | **Phát hiện** | UXP cards grouped by severity, phone-frame screenshots |
| 5 | **Scorecard** | SVG score rings per heuristic category |
| 6 | **Gaps** | Detailed gap checklist by screen |

## Design System

CSS tokens in `assets/template.html` (single source of truth). Details in `references/design-system.md`.

## Score Ring SVG Formulas

```
stroke-dashoffset = circumference × (1 - score/100)

Overall hero:    r=51, circumference=320
Screen scores:   r=25, circumference=157
Heuristic rings: r=33, circumference=207

Color: <50% → #b91c1c | 50-69% → #c2410c | ≥70% → #15803d
```

## Finding Card Layout

```
┌────────────────────────────────────────────────────┐
│ [severity accent bar: 4px colored strip]           │
│ ┌──────────────────┬───────────────────────────┐   │
│ │  ┌────────────┐  │ UXP-XXX  [severity badge] │   │
│ │  │ screenshot │  │ Problem title              │   │
│ │  │ (phone     │  │ Hiện trạng: description    │   │
│ │  │  frame)    │  │ Nguyên tắc: + ref citation │   │
│ │  └────────────┘  │ ┌─ Proposed box ──────────┐│   │
│ │  ⚠️ Overlay label │ │ • improvement items     ││   │
│ │      (2fr)       │ └────────────────────────┘ │   │
│ └──────────────────┴───────────────────────────┘   │
└────────────────────────────────────────────────────┘
```

## Mandatory Rules

1. **Sanitize PII**: No fake account numbers, names, phone numbers
2. **No abbreviations**: Full Vietnamese terms
3. **Every UXP with screenshot**: phone-frame container
4. **Progressive disclosure**: DDL refs inside `<details>` tags
5. **No pipeline metadata**: No timestamps, gate results, or tooling refs
