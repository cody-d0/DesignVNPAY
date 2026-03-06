# Design Data Layer (DDL) — Overview

> **Design data layer** là **bộ kiến thức** (knowledge layer) gọi on-demand: tập dữ liệu có cấu trúc mô tả giao diện (component, state, token, layout, copy) phục vụ automation UI. Consumer **query** theo scope (GLOBAL / PRODUCT) và view — không sở hữu layer.

---

## Định nghĩa

- **Không** phải database nghiệp vụ (entity, schema backend) — đó là **Thiết kế Database** (anchor PRD §4).
- **Là** read-optimized knowledge store: token, UX rules, component taxonomy, state matrix — dùng làm nguồn khi cần token/UX/component/state cho pipeline hoặc skill bất kỳ.

Phạm vi query có thể: toàn bộ, chỉ token, chỉ component, chỉ state, chỉ screen, hoặc theo scope GLOBAL / PRODUCT (xem [hierarchy.md](hierarchy.md)).

---

## Disambiguation

| Thuật ngữ | Nghĩa | Dùng ở đâu |
|-----------|-------|------------|
| **Thiết kế Database** | Anchor PRD §4 cho backend schema (entity, field, constraint) | PRD `.md` — **không thay đổi tên** |
| **design_data_layer** | Lớp kiến thức design (component/state/token/layout/copy) cho automation UI | `.agents/docs/ddl/`, contract, pipeline consumers |

---

## Ba vai trò

1. **Input (scope):** Tham số chọn nhánh khi chạy pipeline (full, token_only, component_only, state_only, screen:{id}, compbase_only, compextend_only). Chi tiết: [views-and-outputs.md](views-and-outputs.md).
2. **Output (materialized):** Pipeline sinh ra `ui-automation/*`, `mockup-spec.json`, `generation-manifest.md` — đây là **kết quả**; DDL knowledge được **gọi on-demand** trong quá trình chạy.
3. **Layer trung gian:** Một cấu trúc dữ liệu trung tâm (schema) mà skills đọc/ghi; projection ra nhiều view. Roadmap v4+.

---

## Constraints

- **Citation:** COMPbase 100% source; COMPextend bắt buộc `ux_rule_ref`.
- **Token:** Format `{collection.token}`; hierarchy TailwindCSS → Theme → Mode → Custom.
- **State:** Tập chuẩn `default`, `focus`, `active`, `disabled`, `loading`, `error`, `success`, `empty`.
- **Single source of truth:** PRD (và Figma khi dùng figma-to-prd-md) là nguồn gốc; DDL là lớp **derived** / knowledge — không thay thế Thiết kế Database.

---

## Doc trong thư mục này

| File | Nội dung |
|------|----------|
| [contract.md](contract.md) | Query contract, views, scope, call-on-demand routing |
| [hierarchy.md](hierarchy.md) | GLOBAL (Cross-Product) vs PRODUCT (Global Product), resolution order |
| [views-and-outputs.md](views-and-outputs.md) | token/component/state/screen view, outputs, scope values |
| [glossary.md](glossary.md) | Thuật ngữ canon, screen_boundaries schema |
| [governance.md](governance.md) | Checklist, do-not-touch, quality gates |

---

## Tham khảo ngoài

- [Martin Fowler – Design Token-Based UI Architecture](https://martinfowler.com/articles/design-token-based-ui-architecture.html)
- [Brad Frost – Design System Ecosystem](https://bradfrost.com/blog/post/the-design-system-ecosystem/)
- [Style Dictionary](https://styledictionary.com/)
- [Apollo TN0042 – SDUI Client Design](https://www.apollographql.com/docs/technotes/TN0042-sdui-client-design)
