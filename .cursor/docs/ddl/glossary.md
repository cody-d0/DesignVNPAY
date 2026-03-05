# DDL — Glossary

> Nguồn tham chiếu canon cho thuật ngữ design data layer trong repo.

---

## Thuật ngữ chính

| Term | Định nghĩa | Không nhầm với |
|------|-----------|----------------|
| design_data_layer | Bộ kiến thức (knowledge layer) gọi on-demand: component, state, token, layout, copy cho automation UI. Output materialized là derived từ PRD + tokens + handoff. | Thiết kế Database |
| Thiết kế Database | Anchor PRD §4 cho backend schema: entity, field, data type, constraint. Extraction anchor — **không thay đổi tên**. | design_data_layer |
| token_view | Subset DDL: token (typography, spacing, color, component tokens). Files: token-dictionary.md, token-gap-registry.md. | component_view |
| component_view | Subset: component registry + token assignments + states. component-catalog.md, component_registry trong mockup-spec.json. | state_view |
| state_view | Subset: state matrix (component × state × trigger × token). state-visual-guide.md. | component_view |
| screen_view | Subset: layout theo screen. screen-specs/{id}.md. | — |
| screen_registry | Danh sách màn hình canonical (PDR/PRD). mockup-spec.json: screen_registry[]. screen_id, source_file, optional screen_type. | screen_boundaries |
| screen_boundaries | Metadata khi một Figma section có nhiều artboards: ranh giới màn hình (artboard → screen, screen_type). Optional. Nguồn: figma-to-prd-md Phase 2a-bis. Schema: § Screen boundaries. | screen_registry |
| design_data_layer_scope | Tham số chọn nhánh output. Mặc định full. Doc-spec only. | — |
| COMPbase | Dữ liệu có bằng chứng trực tiếp từ PRD anchor (100% citation). | COMPextend |
| COMPextend | Bổ sung từ ui-ux-pro-max hoặc suy luận UX (bắt buộc ux_rule_ref). | COMPbase |
| generation-manifest.md | Index của toàn bộ DDL instance: read order, quality gates, source files. | — |
| mockup-spec.json | Canonical machine-readable view toàn bộ DDL. JSON, no CSS. | — |

---

## View hierarchy

```
PRD .md + temp1.json + design_handoff + csv (GLOBAL/PRODUCT)
                        │
                        ▼
               design_data_layer (knowledge)
                        │
    ┌───────────────────┼───────────────────┬────────────────┐
    ▼                   ▼                   ▼                ▼
token_view      component_view       state_view      screen_view   mockup-spec.json
    │                   │                   │                │
token-dictionary   component-catalog   state-visual   screen-specs/
token-gap-registry                     guide.md       {id}.md
```

---

## Screen boundaries schema (extensible)

Dùng khi Figma section chứa nhiều artboards để phân biệt distinct screen vs variant.

**Bắt buộc:**

| Field | Type | Mô tả |
|-------|------|--------|
| screen_id | string | Id canonical (kebab-case). |
| screen_name_vi | string | Tên hiển thị (tiếng Việt). |
| artboard_node_ids | string[] | Figma nodeId của artboard thuộc màn này. |
| screen_type | string | form, confirm, result, list, detail, error (mở rộng: onboarding, search, filter, …). |

**Optional:** order, variant_of, tags[], source_anchor (citation figma:{fileKey}/{nodeId}).

---

## Quan hệ với khái niệm khác

| Khái niệm | Quan hệ với DDL |
|-----------|-----------------|
| Thiết kế Database (PRD §4) | Nguồn extraction cho component/field — không phải DDL. |
| temp1.json | Nguồn token chính (GLOBAL). |
| design_handoff | Nguồn màu, component spec bổ sung. |
| ui-automation/ | Materialized output của DDL. |
| mockup-spec.json | Canonical JSON form. |
| generation-manifest.md | Index và quality gate report. |
