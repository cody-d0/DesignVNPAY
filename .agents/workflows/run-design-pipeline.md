---
description: Chạy design pipeline end-to-end từ PRD folder cho xPOS hoặc product khác
---

# Run Design Pipeline

Workflow chạy `prd-full-pipeline` (v3) trên folder PRD.

## Bước 1: Xác định input

Xác định PRD folder và overview file:
- **xPOS app**: `products/xpos/prd/xpos-app/`
- **xPOS BO**: `products/xpos/prd/xpos-bo/`
- **Co-op Bank**: `products/co-op-bank-khcn/prd/`

## Bước 2: Chạy pipeline

Truyền tham số cho subagent `prd-full-pipeline`:

```
prd_folder: <đường dẫn PRD đã chọn>
overview_file: <file overview trong folder, thường *-overview.md>
target_platform: mobile
target_stack: flutter
```

// turbo
## Bước 3: Kiểm tra output

Output nằm trong `{prd_folder}/ui-automation/`:
- `mockup-spec.json` — deliverable chính
- `generation-manifest.md`
- `token-dictionary.md`
- `component-catalog.md`
- `state-visual-guide.md`
- `ux-copy-bank.md`
- `screen-specs/` — 1 file per screen

## Bước 4: Review

Kiểm tra quality gates trong `mockup-spec.json`:
- `citation_coverage`: phải = 100%
- `token_resolution_rate`: phải >= 70%
- `state_coverage`: 8/8 states
- `touch_target_compliance`: tất cả pass
