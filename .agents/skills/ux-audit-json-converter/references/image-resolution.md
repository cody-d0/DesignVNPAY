# Image Resolution — Chiến lược map ảnh → UXP/Gap

## Data Sources (7 nguồn, xếp theo độ tin cậy)

| # | Source | Tin cậy | Coverage | File |
|---|--------|:-------:|:--------:|------|
| 1 | `artboard-index.json` | ⭐⭐⭐ | 25/28 | Module root |
| 2 | `screen_inventory.json` | ⭐⭐⭐ | 28/28 | `handoff/` |
| 3 | `SCR-*.md` wireframe refs | ⭐⭐ | 14/28 | Module root |
| 4 | Report evidence column | ⭐⭐ | 24/28 | `ux-review-report.md` |
| 5 | UXP block text refs | ⭐ | Variable | `ux-review-report.md` |
| 6 | Gap check# → evidence map | ⭐ | Variable | Derived |
| 7 | Fallback: SCR-ID → base | ⭐ | 28/28 | `screen_inventory.json` |

## Resolution Chain

```
UXP/Gap → cần screenshot_path
  │
  ├─ Có screen_id? ──────────────────────────────┐
  │   ├─ artboard-index[screen_id]? → filename   │
  │   ├─ inventory[screen_id].base? → filename   │
  │   └─ SCR-*.md ![](ui/XXX.png)? → filename   │
  │                                               │
  ├─ Có evidence text? ────────────────────────── │
  │   ├─ "Từ ảnh XXX.png" → direct ref           │
  │   ├─ "From image XXX" → direct ref            │
  │   └─ artboard-id (4 digits) → fuzzy match     │
  │                                               │
  ├─ Có gap_ref "Check #N"? ───────────────────── │
  │   └─ check#N → evidence → image extraction   │
  │                                               │
  └─ Fallback: screen_id → base image from inv   │
      └─ "ui/{first_wireframe_image.filename}"    │
```

## Image Roles

```
base                    — Trạng thái mặc định, dùng cho fallback
overlay:*               — Bottom sheet, popup, OTP, success
variant:*               — State khác (playing, expanded, filled)
error_*                 — Error states
loading_state           — Loading/processing
success_modal           — Success confirmation
```

## UXP Image Priority

1. Nếu UXP ref Check #N từ screen X → lấy ảnh evidence của Check #N
2. Nếu Check #N evidence ref ảnh cụ thể → dùng ảnh đó
3. Nếu không → lấy base image của screen X
4. Nếu UXP liên quan overlay → ưu tiên overlay image

## Gap Image Priority

1. Gap evidence ref ảnh trực tiếp → dùng ảnh đó
2. Gap thuộc screen X → base image của screen X
3. Gap liên quan overlay/popup → overlay image

## Fuzzy Matching: Artboard ID → Filename

Problem: Report viết `7101` nhưng file trên disk là `7101-huy-voice.png`

```python
def fuzzy_match_artboard(artboard_id: str, disk_images: list) -> str:
    """Match 4-digit artboard ID → actual filename on disk."""
    for img in disk_images:
        if img["filename"].startswith(artboard_id):
            return img["filename"]
    return None
```

## Coverage Report (28 modules)

- **UXP coverage:** 251/251 = 100% (trong modules đã convert)
- **Gap coverage:** 374/374 = 100%
- **Ảnh mồ côi:** 11 (trên disk, không ai dùng)
- **Ảnh thiếu:** 79 (referenced nhưng không có trên disk)
- **Root cause:** Artboard ID ≠ filename mismatch
