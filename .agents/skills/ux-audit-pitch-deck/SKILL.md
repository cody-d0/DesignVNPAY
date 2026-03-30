---
name: ux-audit-pitch-deck
description: Render a professional UX Audit Pitch Deck as single-file HTML from report-data.json. Pure renderer — no parsing, no enrichment, no data mutation. Supports both deterministic (enrich_inline) and LLM-powered (enrich_llm + merge_llm) enrichment fields. Triggers include "pitch deck", "render deck", "gen pitch", "HTML report", "audit deck". Requires report-data.json (produced by ux-audit-json-converter skill pipeline). This skill is the final consumer in the UX audit pipeline.
---

# UX Audit Pitch Deck — HTML Renderer

Render `report-data.json` → single-file HTML pitch deck. Zero dependencies, offline-capable.

## Role in Pipeline

```
ux-audit-json-converter          │  ux-audit-pitch-deck (THIS)
─────────────────────────────────┼──────────────────────────────
index_module.py → module-index   │
convert.py      → report-data   │
validate.py     → schema gate   │
template_check.py → 🛑 human    │
enrich_inline.py → enriched     │
enrich_llm.py  → llm-manifest   │
[AGENT]         → llm-enriched  │
merge_llm.py   → V2 enriched    │
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
| `heuristics` | array | 6-category heuristic scorecard (currently hidden) |

### Enrichment Fields (from enrich_inline.py + merge_llm.py)

Renderer consumes canonical enrichment fields with priority fallbacks:

| Field | Source | Used in | Priority |
|-------|--------|---------|----------|
| `hiện_trạng` | merge_llm.py | UXP/Gap → "Hiện trạng" row | **V2 (LLM)** — falls back to `problem` |
| `user_impact` | enrich_inline.py / merge_llm.py | UXP/Gap → "Tác động" row | LLM > inline |
| `heuristic` | enrich_inline.py / merge_llm.py | UXP → "Nguyên tắc" row | LLM > inline |
| `solution_steps` | merge_llm.py | UXP → green proposal bullet list | **V2 (LLM)** — falls back to `solution` string |
| `ref_count` | enrich_inline.py / merge_llm.py | Gap → "📚 N nguồn" collapsible footer | auto-count |
| `references[]` | convert.py (heuristic-db.json lookup) / merge_llm.py | UXP/Gap → citation blocks | merged, deduplicated |

### Renderer Priority Rules

```
Hiện trạng: uxp['hiện_trạng'] || uxp['problem']          # LLM > raw
Đề xuất:    uxp['solution_steps'][] || uxp['solution']    # list > string
Tác động:   uxp['user_impact']                             # LLM or inline
Nguyên tắc: uxp['heuristic']                               # LLM or inline
```

## Output

Single self-contained HTML file: `{slug}--pitch-deck.html`

Filename auto-generated from module metadata:
```
Dịch vụ thẻ/Kích hoạt thẻ → dich-vu-the--kich-hoat-the--pitch-deck.html
```

## HTML Structure (3 active sections)

| # | Section | Builder | Status |
|:--|:--------|:--------|:-------|
| 1 | **Hero** | Product name, stats, overall score ring | ✅ Active |
| 2 | **Tổng quan** | Severity badges, screen score cards (3-col grid) | ✅ Active |
| 3 | **Phát hiện** | UXP cards grouped by severity, table-based layout | ✅ Active |
| 4 | **Gaps** | Detailed gap checklist by screen, table-based layout | ✅ Active |

> **Note:** Methodology and Heuristic Scorecard sections have been removed. Numbering: 01 Tổng quan → 02 Phát hiện → Gaps (unnumbered).

## Design System

CSS tokens in `assets/template.html` (single source of truth). Details in `references/design-system.md`.

### Key CSS Classes

**Finding Cards (Section 4):**
- `.finding-card` → card container with hover shadow
- `.finding-accent.{critical|major|minor}` → 3px severity color bar
- `.card-header` → `[card-id] [badge] h3` layout
- `.card-body` → `grid-template-columns: 500px 1fr` (phone + table)
- `.card-visual` → phone frame container
- `.phone-frame` → clickable screenshot with lightbox
- `.card-table` → data rows: Hiện trạng, Tác động, Nguyên tắc, Đề xuất
- `.td-label` → 110px uppercase label column
- `.td-value.proposal` → green-tinted solution list
- `.card-footer` → screen tags + `<details>` technical refs

**Gap Cards (Section 6):**
- `.gap-card` → card container with table layout
- `.gap-header` → `[gap-num circle] title [gap-ref badge]`
- `.gap-table` → data rows: Hiện trạng, Tác động, Nguyên tắc, Bằng chứng, Tham chiếu
- `.gap-screen` → blue screen ID badge
- `.img-cite` → clickable screenshot citation in evidence

**Lightbox:**
- `.lightbox-overlay` → fullscreen dark backdrop with blur
- `.lightbox-close` → top-right close button
- `.lightbox-caption` → filename display

## Score Ring SVG Formulas

```
stroke-dashoffset = circumference × (1 - score/100)

Overall hero:    r=51, circumference=320
Screen scores:   r=25, circumference=157
Heuristic rings: r=33, circumference=207

Color: <50% → #b91c1c | 50-69% → #c2410c | ≥70% → #15803d
```

## Finding Card Layout (Table-based)

```
┌─ .finding-accent (3px severity color bar) ─────────────────────┐
│ .card-header: [UXP-ID] [Badge] Title                           │
├─ .card-body ────────────────────────────────────────────────────┤
│ 420px Phone   │ <table .card-table>                            │
│  Screenshot   │   Hiện trạng  │ description text               │
│   (click →    │   Tác động    │ impact text                    │
│   lightbox)   │   Nguyên tắc  │ heuristic + ref citation       │
│               │   Đề xuất     │ green proposed list             │
├─ .card-footer ──────────────────────────────────────────────────┤
│ [screen-tag]                         [Tham chiếu kỹ thuật →]   │
└─────────────────────────────────────────────────────────────────┘
```

## Gap Card Layout (Table-based)

```
┌─ .gap-header ──────────────────────────────────────────────────┐
│ [●N] Gap Title                                    [UXG-XXX]   │
├─ <table .gap-table> ───────────────────────────────────────────┤
│ Hiện trạng  │ description text                                 │
│ Tác động    │ impact text                                      │
│ Nguyên tắc  │ Nielsen #N — Name                                │
│ Bằng chứng  │ evidence text  [📸 screenshot.png]               │
│ Tham chiếu  │ <details> DDL + sources list </details>          │
└─────────────────────────────────────────────────────────────────┘
```

## Vietnamese Labels (Template Convention)

Template uses fully Vietnamese labels. Renderer MUST match:

| Section | Label | Template reference |
|---------|-------|--------------------|
| Hero stats | Màn hình, Tổng kiểm tra, Cần cải thiện, Đề xuất | L184-187 |
| Summary badges | Nghiêm trọng, Quan trọng, Cải thiện | L198-200 |
| Methodology | Đánh giá Heuristic, Đối chiếu thông số thiết kế, Kiểm tra trực quan, Đối chiếu nguyên tắc UX | L220-223 |
| Finding table | Hiện trạng, Tác động, Nguyên tắc | L262-271 |
| Gap table | Hiện trạng, Tác động, Nguyên tắc, Bằng chứng, Tham chiếu | L344-370 |
| Screen score | N hạng mục cần cải thiện | L209 |
| Footer | Đánh giá trải nghiệm người dùng dựa trên thông số thiết kế (DDL) | L381 |

## Mandatory Rules

1. **Sanitize PII**: No fake account numbers, names, phone numbers
2. **No abbreviations**: Full Vietnamese terms
3. **Every UXP with screenshot**: phone-frame container
4. **Progressive disclosure**: DDL refs inside `<details>` tags
5. **No pipeline metadata**: No timestamps, gate results, or tooling refs
6. **Vietnamese-first labels**: All user-facing labels in Vietnamese (badge, methodology, footer)
7. **Table-based layout**: Both findings and gaps use `<table>` for scannable data display
