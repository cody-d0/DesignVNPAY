# DDL — Query Contract (On-Demand)

> Design data layer là **read-optimized knowledge store**. Consumer **query** theo view và scope — không sở hữu layer. figma-to-prd-md và prd-full-pipeline là **consumer**, không owner.

---

## Query types

| Query by | Mô tả | Ví dụ |
|----------|--------|-------|
| **View** | token_view, component_view, state_view, screen_view | Lấy token dictionary; lấy component registry; lấy state matrix; lấy screen layout. |
| **Scope** | GLOBAL \| PRODUCT (+ optional product_id) | GLOBAL: ux-guidelines, web-interface, token base, styles/colors/typography. PRODUCT: theme/mode overrides, screen_registry, product UX overrides. |
| **Pattern** | Keyword (e.g. "touch target", "focus state") | Trả về UX rules/laws tương ứng từ ux-guidelines, web-interface, ux-laws. |

Resolution: khi query với scope PRODUCT, merge GLOBAL + PRODUCT với **PRODUCT override** GLOBAL. Chi tiết: [hierarchy.md](hierarchy.md).

---

## Call-on-demand routing

Khi user intent cần:

- **UX rules**, **token**, **component registry**, **state coverage** → route tới **DDL query** (hoặc skill đọc từ DDL knowledge). Không bắt buộc chạy full figma-to-prd-md hay full prd-full-pipeline.
- Ref: [call-on-demand-intent-router.md](../call-on-demand-intent-router.md). Link DDL docs: `.agents/docs/ddl/contract.md`.

---

## UX guideline citation và UX law

Khi áp dụng UX guideline từ ux-guidelines.csv hoặc web-interface.csv: nếu row có **ux_law_ref** thì citation bao gồm cả UX law. Ví dụ: `ux-guidelines.csv#22` (Touch Target Size) → Fitts's Law. Mapping: [hierarchy.md](hierarchy.md) (data sources), ux-laws.csv trong `.agents/skills/ui-ux-pro-max/data/`.
