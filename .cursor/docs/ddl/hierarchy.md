# DDL — Hierarchy: GLOBAL (Cross-Product) → PRODUCT (Global Product)

> Mọi lớp phủ (layer) tuân theo hierarchy có thể scale. **GLOBAL** áp dụng cho mọi sản phẩm; **PRODUCT** là override/mở rộng cho từng sản phẩm.

---

## Định nghĩa

| Scope | Nội dung |
|-------|----------|
| **GLOBAL (Cross-Product)** | Token gốc (TailwindCSS, Theme Default), ux-guidelines.csv, web-interface.csv, ux-laws.csv, styles/colors/typography base, component taxonomy chung. Độc lập sản phẩm. |
| **PRODUCT (Global Product)** | Theme VNPAY, mode Mobile/Desktop overrides, product-specific component keys, product UX overrides (nếu có), screen_registry / screen_boundaries theo PRD pack. Theo product/project. |

---

## Resolution order

Khi query một rule, token, hoặc component:

1. Nếu có **PRODUCT** (product_id) và có giá trị tương ứng trong PRODUCT → dùng giá trị PRODUCT.
2. Ngược lại → dùng **GLOBAL**.

Merge: GLOBAL + PRODUCT với **PRODUCT override** GLOBAL.

---

## Cấu trúc dữ liệu (gợi ý để scale)

- **GLOBAL:** Trỏ tới CSVs hiện tại tại `.agents/skills/ui-ux-pro-max/data/` (ux-guidelines.csv, web-interface.csv, colors.csv, typography.csv, styles.csv, icons.csv, ux-laws.csv). Hoặc thư mục `design-data-layer/global/` nếu tách sau.
- **PRODUCT:** Thư mục `design-data-layer/products/{product_id}/` (overrides: tokens, component_registry, ux_overrides.csv). Có thể bổ sung dần khi có nhu cầu.

Search / pipeline: tham số `scope=global` | `scope=product`, optional `product_id`. Khi `scope=product` thì merge GLOBAL + PRODUCT (core.py hoặc adapter DDL).

---

## Data sources (GLOBAL)

| Nguồn | Vai trò |
|-------|---------|
| temp1.json | Token hierarchy (TailwindCSS → Theme → Mode → Custom) |
| design-data-layer/global/pro-blocks/ | Pro-blocks TSX (primitives, patterns, compositions); code template dùng chung |
| design-data-layer/global/pro-blocks/block-catalog.json | Danh mục block: id, tier, category, file, description, shadcn_deps, tokens_used |
| design-data-layer/global/pro-blocks/pro-blocks-token-map.json | Map Tailwind class → DDL token (review, validation) |
| ux-guidelines.csv, web-interface.csv | UX rules; có thể có cột ux_law_ref → UX law |
| ux-laws.csv | Canonical UX laws (Fitts, Hick, Jakob, Miller, …) |
| colors.csv, typography.csv, styles.csv, icons.csv | Style/color/typography base |
| Component mapping (figma-to-prd-md) | Component taxonomy chung |

PRODUCT: theme/mode overrides (design-data-layer/products/{product_id}/theme-*.json), **block-registry.json** (chỉ định block nào dùng cho từng screen + content/copy overrides), screen_boundaries (từ Figma), screen_registry (từ PDR).
