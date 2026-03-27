---
name: evidence-info
description: >
  Enrich report-data.json with reference citations, heuristic sources,
  impact narratives, and DDL evidence from enriched-data.json and
  official reference databases. Operates BETWEEN convert_report.py
  and render_report.py. No HTML mutation — pure JSON-level enrichment.
---

# evidence-info — Reference Evidence Enricher

## Purpose

Improve `report-data.json` reference quality by merging:
- **enriched-data.json** → heuristic names, impact narratives, DDL evidence
- **references/official-urls.md** → canonical Nielsen/WCAG/Laws URLs + quotes
- **handoff/ddl-context.json** → DDL token/guideline references

## Architecture Position

```
[ux-audit-json-converter]
  convert_report.py → report-data.json (baseline)
                        ↓
                enrich_images.py (evidence-img) ← optional
                        ↓
                enrich_refs.py ← merges enriched-data + refs + DDL
                        ↓
                    report-data.json (fully enriched)
                        ↓
[ux-audit-pitch-deck]
                render_report.py → pitch-deck.html
```

## Usage

```bash
# Enrich single module
python3 enrich_refs.py --module path/to/module/

# Enrich all modules
python3 enrich_refs.py --base path/to/final/

# Audit-only
python3 audit_refs.py --base path/to/final/
```

## Data Sources

| Source | Fields Enriched |
|--------|----------------|
| `enriched-data.json` | gap heuristic, impact, hiện_trạng, heuristic_sources |
| `references/official-urls.md` | Canonical URLs + quotes for Nielsen/WCAG/Laws |
| `handoff/ddl-context.json` | DDL component refs, token evidence |

## Scripts

- `scripts/enrich_refs.py` — Main reference enrichment engine
- `scripts/audit_refs.py` — Reference quality audit
