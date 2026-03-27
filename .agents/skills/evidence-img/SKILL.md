---
name: evidence-img
description: >
  Enrich report-data.json with better image assignments by merging
  artboard-index.json, Screen MDs, and screen_inventory.json.
  Operates BETWEEN convert_report.py and render_report.py.
  No HTML mutation — pure JSON-level enrichment.
---

# evidence-img — Image Evidence Enricher

## Purpose

Improve `report-data.json` screenshot_path accuracy by merging
additional artboard metadata from **artboard-index.json** and
**Screen MDs** that `convert_report.py` does not read.

## Architecture Position

```
[ux-audit-json-converter]
  convert_report.py → report-data.json (baseline)
                        ↓
                enrich_images.py ← merges artboard-index.json + SCR-*.md
                        ↓
                    report-data.json (image-enriched)
                        ↓
[ux-audit-pitch-deck]
                render_report.py → pitch-deck.html
```

## Usage

```bash
# Enrich single module
python3 enrich_images.py --module path/to/module/

# Enrich all modules under base
python3 enrich_images.py --base path/to/final/

# Audit-only (no write)
python3 audit_images.py --base path/to/final/
```

## Data Sources Merged

| Source | What it provides |
|--------|-----------------|
| `artboard-index.json` | Per-artboard roles + text_elements + names |
| `SCR-*.md` | Variant descriptions from Variants table |
| `screen_inventory.json` | Wireframe image list + OCR (fallback) |

## Scripts

- `scripts/enrich_images.py` — Main enrichment engine
- `scripts/audit_images.py` — Quality audit & diversity metrics
