---
name: ux-audit-json-converter
description: >-
  Convert UX audit report markdown + handoff data into canonical report-data.json
  for pitch deck generation. Handles 12+ format variants deterministically.
  Self-learning: unknown formats trigger reasoning → reprocess → save new template.
  Triggers: "convert report", "tạo report-data.json", "chạy converter",
  "convert ux-review-report", "parse audit report", "generate report JSON",
  "run converter on module", "convert module".
---

# UX Audit JSON Converter

3-layer deterministic pipeline: Raw Sources → Module Index → Consumer JSON.
Parse `ux-review-report.md` + `handoff/` → output `report-data.json` cho
`ux-audit-pitch-deck` consume.

## Core Principles

1. **3-Layer Architecture** — Raw → module-index.json (canonical) → report-data.json (consumer)
2. **Deterministic** — Zero API/LLM calls. Pure regex + alias mapping
3. **Stdlib-only** — No external Python dependencies
4. **Self-learning** — Unknown format → log → reason → reprocess → save template
5. **Consumer-backward** — Output schema locked to `render_report.py` contract (37 fields)
6. **Module-level** — Process 1 module at a time, deep context-aware indexing

## Pipeline Flow

```
Raw Sources (7+ nguồn, 12+ format variants)
    │
    ├─ Step 1: INDEX  ──────────────→  module-index.json (Lớp 2: SSOT)
    │  scripts/index_module.py
    │
    ├─ Step 2: CONVERT ─────────────→  report-data.json (Lớp 3: consumer)
    │  scripts/convert.py
    │
    └─ Step 3: VALIDATE ────────────→  ✅ / ❌
       scripts/validate.py
```

## Self-Learning Protocol

Khi indexer gặp format không khớp templates trong
[format-registry.md](references/format-registry.md):

1. **Detect** — Extraction trả 0 kết quả hoặc unknown key
2. **Log** — Ghi structured issue vào `_meta.issues[]`
3. **Reason** — Agent đọc raw MD, so sánh với known templates
4. **Adapt** — Tạo regex/alias mới cho format mới
5. **Reprocess** — Chạy lại indexer với adaptation
6. **Save** — Append template mới vào `references/format-registry.md`

> **Quan trọng:** KHÔNG sửa index_module.py mỗi lần gặp format mới.
> Ưu tiên cập nhật format-registry.md. Chỉ sửa code khi cần logic mới.

## Scripts

| Script | Mục đích | Usage |
|--------|----------|-------|
| `scripts/pipeline.py` | **Full orchestrator** (Index→Convert→Validate→Enrich→Render) | `python3 pipeline.py --module /path/to/module` |
| `scripts/index_module.py` | Index single module → module-index.json | `python3 index_module.py --module /path/to/module` |
| `scripts/convert.py` | Convert module-index.json → report-data.json | `python3 convert.py --module /path/to/module` |
| `scripts/validate.py` | Schema validation gate | `python3 validate.py --module /path/to/module` |

## References

| File | Nội dung | Khi nào đọc |
|------|----------|-------------|
| [output-schema.md](references/output-schema.md) | Canonical output schema + field docs | Khi implement converter hoặc debug output |
| [format-registry.md](references/format-registry.md) | Registry các format variants đã xử lý | Khi gặp format mới hoặc debug parsing |
| [image-resolution.md](references/image-resolution.md) | Chiến lược map ảnh → UXP/Gap | Khi implement image resolver |

## Usage — Per Module

```bash
# Full pipeline (recommended): Index → Convert → Validate → Enrich → Render
python3 scripts/pipeline.py --module "/path/to/module/"

# Batch: All modules under base
python3 scripts/pipeline.py --base "/path/to/final/"

# Partial re-run (skip index/convert, only re-enrich + re-render)
python3 scripts/pipeline.py --module "/path/to/module/" --from enrich-img

# Enrichment dry-run (preview without writing)
python3 scripts/pipeline.py --module "/path/to/module/" --dry-run --skip-render
```

## Pipeline Architecture

```
Index → Convert → Validate → Enrich Images → Enrich Refs → Render
  │        │          │            │               │           │
  │        │          │     evidence-img       evidence-info   │
  │        │          │     (artboard ctx)     (official refs) │
  │        │          │                                        │
  ▼        ▼          ▼                                        ▼
module-  report-    ✅/❌     report-data.json           pitch-deck
index    data       gate      (enriched)                 .html
.json    .json
```

## Consumer Contract

Output `report-data.json` phải 100% tương thích với:
- `ux-audit-pitch-deck/scripts/render_report.py` — HTML generator (37+ fields)
- `evidence-img` skill — image enrichment (`_enriched_*` fields)
- `evidence-info` skill — reference enrichment (`_enriched_*` fields)

Schema chi tiết: xem [output-schema.md](references/output-schema.md)

