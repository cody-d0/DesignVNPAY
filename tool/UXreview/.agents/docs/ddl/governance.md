# DDL — Governance

> Checklist, do-not-touch, quality gates cho design data layer.

---

## Checklist khi viết docs / rules / skills

- Khi đề cập **backend schema** (entity, field, constraint): dùng **Thiết kế Database**.
- Khi đề cập **automation UI knowledge** (component, state, token, layout, copy): dùng **design_data_layer** (hoặc DDL).
- Không dùng "design database", "design DB" cho overlay — dùng design_data_layer.
- design_data_layer_scope chỉ doc-spec; ghi rõ nếu đã functional.
- Link glossary [glossary.md](glossary.md) khi giới thiệu khái niệm lần đầu.

---

## Do NOT touch

**Thiết kế Database** trong PRD:

- Tất cả `## 4. Thiết kế Database` trong XPOS, MarkdownSV, co-op-bank-khcn, package-2 — **không đổi tên**. Anchor được hardcode trong extraction logic.

**Rules / skills / agents** — các dòng đề cập Thiết kế Database như **extraction anchor** (không phải định nghĩa) — không cần sửa:

- .agents/docs/comp-extraction.mdc, pdr-component-pipeline.mdc
- .agents/docs/prd-full-pipeline.md
- .agents/skills/comp-extraction/SKILL.md, figma-to-prd-md/SKILL.md, screen-count-extraction/SKILL.md

---

## Quality gates (chạy tay sau khi sửa .agents/docs/ddl/)

1. **Term consistency:** `rg "design database|design DB" .agents/docs/ddl/` → 0 matches.
2. **Anchor compatibility:** `rg "Thiết kế Database" .agents/docs/ .agents/skills/ .agents/docs/` → đầy đủ như trước.
3. **Scope coverage:** Các scope values (token_only, component_only, state_only, compbase_only, compextend_only) có trong views-and-outputs.md.
4. **Glossary link:** README.md link tới glossary.md và các file con.
