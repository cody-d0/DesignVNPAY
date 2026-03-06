# DDL — Views and Outputs

> Các view của design data layer và artifact output khi pipeline chạy. Scope values điều khiển nhánh nào được generate.

---

## Views

| View | Nội dung | File / artifact |
|------|----------|------------------|
| **token_view** | Token (typography, spacing, color, component tokens) | token-dictionary.md, token-gap-registry.md |
| **component_view** | Component registry + token assignment + states | component-catalog.md, component_registry trong mockup-spec.json |
| **state_view** | State matrix (component × state × trigger × token) | state-visual-guide.md |
| **screen_view** | Layout theo screen (component stack, data deps) | screen-specs/{id}.md |
| **Copy (UX writing)** | Labels, error, empty, success, retry | ux-copy-bank.md |

---

## Output (materialized)

Pipeline sinh ra:

| File / artifact | View | Ghi chú |
|-----------------|------|---------|
| token-dictionary.md | token_view | |
| token-gap-registry.md | token_view | missing_token backlog |
| component-catalog.md | component_view | |
| state-visual-guide.md | state_view | |
| screen-specs/{id}.md | screen_view | Nguồn screen list: screen_registry hoặc screen_boundaries |
| ux-copy-bank.md | UX writing | |
| generation-manifest.md | Index | Quality gates, read order, source files |
| mockup-spec.json | Toàn bộ | Canonical machine-readable; no CSS |

---

## Scope values (design_data_layer_scope)

| Value | Output được generate | Use case |
|-------|------------------------|----------|
| full | Tất cả ui-automation/* + mockup-spec.json | Mặc định |
| token_only | token-dictionary.md, token-gap-registry.md | Cập nhật token |
| component_only | component-catalog.md, subset trong mockup-spec.json | Review component |
| state_only | state-visual-guide.md | Audit state |
| screen:{id} | screen-specs/{id}.md | Một màn hình |
| compbase_only | Chỉ rows COMPbase trong mọi view | Deliverable chính xác |
| compextend_only | Chỉ rows COMPextend | UX proposal review |

**Trạng thái:** design_data_layer_scope hiện **doc-spec only** — chưa functional parameter trong pipeline. Mặc định full.

---

## Use cases tiêu thụ

| Use case | Nhánh cần | Files |
|----------|------------|-------|
| Figma import token | token_view | token-dictionary.md |
| Code generation | Toàn bộ | mockup-spec.json + token-dictionary.md |
| Visual regression test | state_view + token_view | state-visual-guide.md + token |
| Accessibility audit | token_view | token-dictionary.md (contrast) |
| UX copy review | Copy | ux-copy-bank.md |
| Screen implementation | screen_view + component_view | screen-specs/{id}.md + component-catalog.md |
