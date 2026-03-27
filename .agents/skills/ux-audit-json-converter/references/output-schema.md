# Output Schema — report-data.json

Consumer: `render_report.py` (ux-audit-pitch-deck skill)

## Top-Level Structure

```jsonc
{
  "meta":            {},    // Module metadata
  "stats":           {},    // Aggregate statistics
  "screens":         [],    // Per-screen summary
  "uxps":            [],    // UX improvement proposals
  "gaps_by_screen":  [],    // Gaps grouped by screen
  "heuristics":      [],    // Category scores
  // Optional enrichment metadata
  "_image_enrichment": {},
  "_ref_enrichment":   {}
}
```

## Field Reference

### meta

| Field | Type | Source | Required |
|-------|------|--------|:--------:|
| `client_name` | string | H1 hoặc **Product** | ✅ |
| `product_name` | string | Metadata block | ✅ |
| `module_name` | string | H1 hoặc **Section** | ✅ |
| `domain` | string | **Domain:** | ✅ |
| `section` | string | Parent folder hoặc **Section** | ✅ |
| `module_dir` | string | Runtime absolute path | ✅ |

### stats

| Field | Type | Derived From | Required |
|-------|------|-------------|:--------:|
| `screen_count` | int | len(screens) | ✅ |
| `check_count` | int | Sum all checks | ✅ |
| `gap_count` | int | Sum verdict=gap | ✅ |
| `pass_count` | int | Sum verdict=pass | ✅ |
| `proposal_count` | int | len(uxps) | ✅ |
| `overall_score` | int | pass/(pass+gap)*100 | ✅ |
| `overall_score_color` | string | <50→red, <70→orange, ≥70→green | ✅ |
| `overall_score_offset` | int | 314*(1-score/100) | ✅ |
| `severity_counts` | object | {critical, major, minor} | ✅ |

### screens[]

| Field | Type | Required |
|-------|------|:--------:|
| `id` | string (SCR-XXX-NNN) | ✅ |
| `name` | string | ✅ |
| `type` | string (list/form/confirm/detail) | ✅ |
| `score` | int | ✅ |
| `score_color` | string | ✅ |
| `score_offset` | int | ✅ |
| `gap_count` | int | ✅ |
| `artboard_count` | int | ✅ |

### uxps[]

| Field | Type | Required |
|-------|------|:--------:|
| `id` | string (UXP-NNN) | ✅ |
| `severity` | string (Critical/Major/Minor) | ✅ |
| `screen_tag` | string | ✅ |
| `problem` | string | ✅ |
| `gap_ref` | string | ✅ |
| `ddl_ref` | string | ✅ |
| `solution` | string | ✅ |
| `screenshot_path` | string | ❌ (enrichment) |
| `_enriched_ref` | object | ❌ (enrichment) |

### gaps_by_screen[]

| Field | Type | Required |
|-------|------|:--------:|
| `screen_id` | string | ✅ |
| `screen_name` | string | ✅ |
| `screen_type` | string | ✅ |
| `gaps[].num` | int | ✅ |
| `gaps[].title` | string | ✅ |
| `gaps[].ref` | string | ✅ |
| `gaps[].severity` | string | ✅ |
| `gaps[].evidence` | string | ✅ |
| `gaps[].screenshot_path` | string | ❌ |

### heuristics[]

Fixed set — 6 categories:

```python
HEURISTIC_CATEGORIES = [
    {"key": "flow",      "name_vi": "Luồng người dùng",    "name_en": "Flow & Navigation"},
    {"key": "component", "name_vi": "Thành phần",          "name_en": "Component & DDL"},
    {"key": "visual",    "name_vi": "Thiết kế trực quan",   "name_en": "Visual Design"},
    {"key": "content",   "name_vi": "Nội dung",            "name_en": "Content & Copy"},
    {"key": "a11y",      "name_vi": "Tiếp cận",            "name_en": "Accessibility"},
    {"key": "trust",     "name_vi": "Tin cậy & Bảo mật",   "name_en": "Trust & Security"},
]
```

## Score Color Derivation

```python
def score_color(score: int) -> str:
    if score < 50: return "#b91c1c"   # red
    if score < 70: return "#c2410c"   # orange
    return "#15803d"                   # green

def score_offset(score: int) -> int:
    return round(314 * (1 - score / 100))
```
