# Project brain — context for AI (Gemini / Cursor)

This folder (`.gemini`) is the **project brain**: persistent context and knowledge loaded for the AI so you don’t have to repeat it every time.

---

## Project identity

- **Repo:** Design-data-layer + PRD/PDR pipeline, viewer, XPOS, co-op-bank-khcn, MarkdownSV, product deliverables.
- **Languages:** Vietnamese (nghiệp vụ, PRD) + English (code, docs, tokens). Keep terms like "Thiết kế Database", "Mô tả màn hình", "design_data_layer" as-is.
- **Default UX scope:** Mobile-first (iOS + Android), then desktop. Accessibility: WCAG AA/AAA where required (e.g. Government, Healthcare).

---

## Design Data Layer (DDL)

- **Role:** Read-only knowledge layer for UI automation: tokens, components, states, screens, copy. Not the business database (that’s "Thiết kế Database" in PRD §4).
- **Views:** token_view, component_view, state_view, screen_view. Outputs: `mockup-spec.json`, `ui-automation/*`, `generation-manifest.md`.
- **Scope:** GLOBAL (cross-product) + PRODUCT (per-product overrides). PRODUCT overrides GLOBAL.
- **Paths:** DDL docs `.cursor/docs/ddl/`; GLOBAL data `.agents/skills/ui-ux-pro-max/data/` and `design-data-layer/global/`.

---

## UI/UX rules (summary)

- **Touch:** Min 44×44px targets; ≥8px gap between targets.
- **Focus:** Visible focus ring (e.g. focus:ring-2); never outline-none without a replacement.
- **Forms:** Visible labels (not placeholder-only); errors inline near field; autocomplete; no blocking paste.
- **A11y:** Contrast ≥4.5:1; icon buttons have aria-label; semantic HTML + ARIA; keyboard navigable; errors with role=alert/aria-live.
- **Motion:** Respect prefers-reduced-motion; micro-interactions 150–300ms; avoid infinite animation except loaders.
- **State set:** default, focus, active, disabled, loading, error, success, empty.
- **Citation:** COMPbase from PRD; COMPextend must have ux_rule_ref (e.g. ux-guidelines.csv, ux-laws.csv).

---

## Full UI/UX brain

Detailed extract (guidelines, web-interface rules, UX laws, colors, styles, icons, query contract): **`UI-UX-BRAIN-EXTRACT.md`** at repo root. Use it when you need token view, component view, product-style mapping, or citation format.

---

## Conventions

- **Tokens:** `{collection.token}`; hierarchy TailwindCSS → Theme → Mode → Custom.
- **Screen types:** form, confirm, result, list, detail, error, onboarding, search, filter.
- **Skills:** figma-to-prd-md, design-system-gen, prd-crossfile-mapping, pdr-extract, comp-token-augment, visual-spec-gen, review-ux, ux-signal-inference. Canonical skill paths under `.cursor/skills/` or `.agents/skills/` (see ui-ux-pro-max-reference.md).
