---
name: ux-audit-json-converter
description: >-
  Convert UX audit report markdown + handoff data into canonical report-data.json
  for pitch deck generation. Handles 12+ format variants deterministically.
  Self-learning: unknown formats trigger reasoning → reprocess → save new template.
  LLM enrichment: generate high-fidelity impact narratives, heuristic citations,
  and artboard-aware descriptions via manifest→agent→merge pipeline.
  Triggers: "convert report", "tạo report-data.json", "chạy converter",
  "convert ux-review-report", "parse audit report", "generate report JSON",
  "run converter on module", "convert module", "enrich LLM", "enrich module".
---

# UX Audit JSON Converter

3-layer deterministic pipeline: Raw Sources → Module Index → Consumer JSON.
Parse `ux-review-report.md` + `handoff/` → output `report-data.json` cho
`ux-audit-pitch-deck` consume.

## Core Principles

1. **3-Layer Architecture** — Raw → module-index.json (canonical) → report-data.json (consumer)
2. **Dual enrichment** — Deterministic baseline (enrich_inline.py) + LLM-powered deep enrichment (enrich_llm.py + merge_llm.py)
3. **Stdlib-only** — No external Python dependencies
4. **Self-learning** — Unknown format → log → reason → reprocess → save template
5. **Consumer-backward** — Output schema locked to `render_report.py` contract (~48 field paths)
6. **Module-level** — Process 1 module at a time, deep context-aware indexing
7. **5-tier Image Resolution** — EXACT → ORDINAL → ARTBOARD → SEMANTIC → DEFAULT

## Pipeline Flow

```
Raw Sources (7+ nguồn, 12+ format variants)
    │
    ├─ Step 1: INDEX  ──────────────→  module-index.json (Lớp 2: SSOT)
    │  scripts/index_module.py
    │  scripts/index_handoff.py  (handoff data sub-indexer)
    │  scripts/index_images.py   (image resolution engine)
    │
    ├─ Step 2: CONVERT ─────────────→  report-data.json (Lớp 3: consumer)
    │  scripts/convert.py
    │
    ├─ Step 3: VALIDATE ────────────→  ✅ / ❌ (schema gate)
    │  scripts/validate.py
    │
    ├─ Step 4: TEMPLATE CHECK ──────→  🛑 HUMAN CHECKPOINT
    │  scripts/template_check.py       (consumer-backward + enrichment preview)
    │  references/template-contract.json (golden reference từ template.html)
    │
    ├─ Step 5: ENRICH INLINE ───────→  report-data.json (baseline enriched)
    │  scripts/enrich_inline.py         (user_impact, heuristic, ref_count)
    │
    └─ Step 6: ENRICH LLM ─────────→  report-data.json (V2 enriched)
       scripts/enrich_llm.py   → llm-manifest.json  (context bundle)
       [AGENT]                 → llm-enriched.json   (generated content)
       scripts/merge_llm.py    ← validate + merge    (quality gates)
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

## Human Checkpoint — Template Check

`template_check.py` là **consumer-backward validation gate** đặt sau validate,
trước enrich. Agent **PHẢI** dừng và report kết quả cho user tại đây.

### Khi nào trigger
- Pipeline chạy qua `tpl-check` step → report tự động in ra terminal
- Agent chạy standalone: `python3 template_check.py --module /path/`

### Report bao gồm
| Section | Nội dung |
|---------|----------|
| Status | ✅ PASS / ❌ FAIL với tổng errors/warnings |
| Summary | Score, screens, UXPs, gaps |
| Image Coverage | Disk total, used, unused (list file names) |
| **Reference Coverage** | **UXP/Gap với citations (%), sources breakdown (NNG/W3C/Laws of UX)** |
| **🔮 Enrichment Preview** | **Status của enrichment fields (user_impact, heuristic, ref_count) — ✅/⭕/⚠️** |
| Errors | Missing required fields, type mismatch, formula sai |
| Warnings | Short text, pattern mismatch, cross-validation |
| Human Decision | Fix source → re-run / Update contract / Override |

### Quyết định tại checkpoint
1. **Fix source** — Sửa ux-review-report.md → re-run từ `index`
2. **Update contract** — Template HTML đã đổi → update `references/template-contract.json`
3. **Override** — Chấp nhận warnings, tiếp tục enrich + render

### Maintain contract

Khi `template.html` thay đổi → update `references/template-contract.json`:
- Thêm/xóa placeholder → thêm/xóa field trong contract
- Đổi formula → update `formula` field
- Đổi label → update `_label_contract`

## Scripts

| Script | Mục đích | Size | Usage |
|--------|----------|------|-------|
| `scripts/pipeline.py` | **Full orchestrator** (Index→Convert→Validate→TplCheck→Enrich→LLM→Render) | 8KB | `python3 pipeline.py --module /path/to/module` |
| `scripts/score_engine.py` | **Scoring engine** (ported from `tools/ux-score-calculator.js`) — simple + weighted scores, discrepancy detection | 12KB | Library: imported by convert.py. CLI: `python3 score_engine.py --module /path/ [--json]` |
| `scripts/index_module.py` | Index single module → module-index.json | 49KB | `python3 index_module.py --module /path/to/module` |
| `scripts/index_handoff.py` | Index handoff/ data (screen_inventory, manifest, flow_graph) | 31KB | Called by index_module.py |
| `scripts/index_images.py` | Image resolution engine (artboard-index, SCR-MDs, disk scan) | 32KB | Called by index_module.py |
| `scripts/convert.py` | Convert module-index.json → report-data.json (baseline) | 30KB | `python3 convert.py --module /path/to/module` |
| `scripts/enrich_inline.py` | **Deterministic enrichment** — generates user_impact, heuristic, ref_count from existing data | 16KB | `python3 enrich_inline.py --module /path/to/module` |
| `scripts/enrich_llm.py` | **LLM context assembler** — assembles context bundle per finding → llm-manifest.json for agent enrichment | 29KB | `python3 enrich_llm.py --module /path/to/module [--prompt]` |
| `scripts/merge_llm.py` | **LLM merger** — validates + merges llm-enriched.json back into report-data.json with quality gates | 15KB | `python3 merge_llm.py --module /path/to/module [--dry-run\|--force]` |
| `scripts/validate.py` | Schema validation gate | 9KB | `python3 validate.py --module /path/to/module` |
| `scripts/template_check.py` | **Consumer-backward validation + human checkpoint** | 32KB | `python3 template_check.py --module /path/to/module` |

## References

| File | Nội dung | Khi nào đọc |
|------|----------|-------------|
| [output-schema.md](references/output-schema.md) | Canonical output schema + field docs | Khi implement converter hoặc debug output |
| [format-registry.md](references/format-registry.md) | Registry các format variants đã xử lý (15 entries: FMT-001→FMT-072) | Khi gặp format mới hoặc debug parsing |
| [image-resolution.md](references/image-resolution.md) | Chiến lược map ảnh → UXP/Gap (5-tier resolution engine) | Khi implement image resolver |
| [template-contract.json](references/template-contract.json) | **Golden reference** — mọi field map 1:1 với {{PLACEHOLDER}} trong template.html | Khi template.html thay đổi → update contract |
| [heuristic-db.json](references/heuristic-db.json) | **Shared heuristic reference DB** — 10 Nielsen, 8 WCAG, 9 Laws of UX + context mapping | Khi cần thêm/sửa heuristic citations |

## Usage — Per Module

```bash
# Full pipeline (recommended): Index → Convert → Validate → TplCheck → Enrich Inline → Render
python3 scripts/pipeline.py --module "/path/to/module/"

# Batch: All modules under base
python3 scripts/pipeline.py --base "/path/to/final/"

# Partial re-run: start from a specific step
# Available steps: index, convert, validate, tpl-check, enrich-inline, enrich-llm, enrich-img, enrich-ref, render
python3 scripts/pipeline.py --module "/path/to/module/" --from enrich-inline

# Template check only (standalone — human review)
python3 scripts/template_check.py --module "/path/to/module/" -v
python3 scripts/template_check.py --base "/path/to/final/"  # batch

# Enrichment dry-run (preview without writing)
python3 scripts/pipeline.py --module "/path/to/module/" --dry-run --skip-render

# Skip render (only index + convert + validate + tpl-check + enrich)
python3 scripts/pipeline.py --module "/path/to/module/" --skip-render

# ═══ LLM Enrichment (3-step workflow) ═══
# Step 1: Generate manifest (context bundle per finding)
python3 scripts/enrich_llm.py --module "/path/to/module/"

# Step 2: Agent reads llm-manifest.json → generates llm-enriched.json
# (This is done by the agent, not a script)

# Step 3: Validate + merge into report-data.json
python3 scripts/merge_llm.py --module "/path/to/module/"
python3 scripts/merge_llm.py --module "/path/to/module/" --dry-run   # preview
python3 scripts/merge_llm.py --module "/path/to/module/" --force     # skip quality gates

# Batch LLM enrichment
python3 scripts/enrich_llm.py --base "/path/to/final/"    # all manifests
python3 scripts/merge_llm.py --base "/path/to/final/"     # merge all
```

## Pipeline Architecture

```
Index → Convert → Validate → TplCheck → Enrich Inline → Enrich LLM → Enrich Img → Render
  │        │          │          │             │               │            │            │
  │        │          │     template_      enrich_         enrich_llm.py    │            │
  │        │          │     check.py       inline.py       merge_llm.py     │            │
  │        │          │     🛑 HUMAN      (deterministic)   (LLM-powered)   │            │
  │        │          │                                                      │            │
  ▼        ▼          ▼          ▼             ▼               ▼              ▼            ▼
module-  report-    ✅/❌    ✅ or 🛑    report-data      report-data      images       pitch-deck
index    data       schema   consumer     .json             .json            enriched     .html
.json    .json      gate     contract     (baseline)        (V2 enriched)
```

### Pipeline Steps Detail

| Step | Script | Critical | Description |
|------|--------|:--------:|-------------|
| `index` | index_module.py | ✅ | Parse ux-review-report.md + handoff/ → module-index.json |
| `convert` | convert.py | ✅ | Transform module-index.json → report-data.json |
| `validate` | validate.py | ✅ | Schema gate — stops pipeline if fails |
| `tpl-check` | template_check.py | ✅ | **Consumer-backward validation + human checkpoint** — baseline errors + 🔮 enrichment preview |
| `enrich-inline` | enrich_inline.py | ✅ | **Deterministic enrichment** — generates user_impact, heuristic, ref_count |
| `enrich-llm` | enrich_llm.py + merge_llm.py | ❌ | **LLM-powered enrichment** — artboard-aware descriptions, domain-specific impact, heuristic citations (opt-in, requires agent) |
| `enrich-img` | evidence-img skill | ❌ | Image enrichment (optional external skill) |
| `render` | ux-audit-pitch-deck skill | ❌ | Generate pitch-deck.html |

## Image Resolution — 5-Tier Engine

Built into `convert.py` (L66-333). Resolution priority:

| Tier | Name | Signal | Confidence |
|------|------|--------|:----------:|
| T1 | EXACT | Filename ref from evidence ("Từ ảnh xxx.png") | ⭐⭐⭐ |
| T2 | ORDINAL | "state N" maps to Nth image in SCR-MD order | ⭐⭐⭐ |
| T3 | ARTBOARD | 4-digit artboard ID prefix match on filename | ⭐⭐ |
| T4 | SEMANTIC | Keyword scoring (role, alt_text, context overlap) | ⭐⭐ |
| T5 | DEFAULT | Base image or first available on disk | ⭐ |

Each UXP and gap record includes `_img_tier` diagnostic field.

## Consumer Contract

Output `report-data.json` phải 100% tương thích với:
- `ux-audit-pitch-deck/scripts/render_report.py` — HTML generator (~48 field paths)
- `enrich_inline.py` — deterministic enrichment (user_impact, heuristic, ref_count)
- `merge_llm.py` — LLM enrichment (hiện_trạng, tác_động, nguyên_tắc, solution_steps, references)
- `template-contract.json` — golden reference với `"source": "enrich_inline"` annotation cho enrichment fields

### LLM Enrichment — Field Mapping

When `merge_llm.py` merges `llm-enriched.json`:

| LLM field | → report-data field | Used by renderer |
|-----------|---------------------|------------------|
| `hiện_trạng` | `hiện_trạng` (UXP) / `description` + `hiện_trạng` (Gap) | "Hiện trạng" row |
| `tác_động` | `user_impact` | "Tác động" row |
| `nguyên_tắc` | `heuristic` | "Nguyên tắc" row |
| `đề_xuất_steps` | `solution_steps` (array) | Green proposal list (UXP only) |
| `references` | `references[]` (merged, deduplicated) | Citation blocks + ref_count |

Renderer priority: `hiện_trạng` > `problem` (fallback); `solution_steps[]` > `solution` string (fallback).

### Score Models

> **Source:** `tools/ux-score-calculator.js` → ported to `scripts/score_engine.py`
> and integrated into `convert.py` at convert time.

**Simple Score** (displayed in hero ring):
```python
simple_score = round(pass_count / total_checks * 100)
```

**Weighted Score** (severity-aware, available in stats + per-screen):
```python
SEVERITY_WEIGHTS = {'critical': 3.0, 'major': 2.0, 'minor': 1.0}
weighted_penalty = sum(SEVERITY_WEIGHTS[uxp.severity] for uxp in screen_uxps)
max_penalty = verifiable_checks * 3.0  # worst case: all critical
weighted_score = max(0, round((1 - weighted_penalty / max_penalty) * 100))
```

**Discrepancy Detection:** The engine re-counts pass/gap from raw check data
and compares against claimed values in ux-review-report.md. Discrepancies
are logged to `_score_discrepancies[]` in report-data.json.

### Score Ring Formula (SVG offsets)

```python
# Hero ring (r=51, circumference=320)
overall_score_offset = round(320 * (1 - score / 100))

# Screen ring (r=25, circumference=157)
screen_score_offset = round(157 * (1 - score / 100))

# Color thresholds
score < 50  → "#b91c1c"  # red
score < 70  → "#c2410c"  # orange
score >= 70 → "#15803d"  # green
```

Schema chi tiết: xem [output-schema.md](references/output-schema.md)
