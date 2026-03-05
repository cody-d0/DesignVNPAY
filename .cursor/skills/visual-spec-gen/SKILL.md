---
name: visual-spec-gen
description: "Generate mobile-first visual specs from pipeline outputs: Token Dictionary, Responsive Override Table, Component CSS Snippets, Screen Layout Specs, and Implementation Guide. Skill 4 in prd-full-pipeline, runs after comp-extraction."
---

# Visual Spec Generation -- Skill 4

Tổng hợp output từ Skill 0-3 thành bộ file .md phục vụ trực tiếp cho automation UI design. Tất cả output là **mobile-first**.

## When to Use

- Sau khi comp-extraction (Skill 3) hoàn thành trong pipeline
- Khi cần tạo bộ file .md automation UI design từ pipeline output
- Khi cần visual specs implementation-ready cho Figma plugin hoặc code generation

## Input Contract

| Parameter | Source | Description |
|-----------|--------|-------------|
| `design_handoff` | Skill 0 | Style, colors (HEX), typography, component CSS specs, color token proposals |
| `crossfile_handoff` | Skill 1 | Dependencies, shared fields, canonical contract, inconsistencies |
| `pdr_handoff` | Skill 2 | Merged screen registry, component registry, case matrix, variants/states, missing values |
| `comp_extraction_output` | Skill 3 | Token mapping (resolved + missing), state matrix, COMPextend proposals, UX writing |
| `token_file` | Config | Default `temp1.json` |
| `target_mode` | Config | Default `Mobile` (mobile-first baseline) |
| `target_stack` | Config | Default `html-tailwind` |
| `prd_folder` | Config | Path to PRD folder |

## Process -- 5 Sections Output

### Section 1: Token Dictionary

**Purpose**: Flatten temp1.json + design_handoff into a single human/machine-readable token reference.

**Steps:**

1. Parse temp1.json collection `"4. Custom".modes.Mobile` as **baseline values**.
2. Parse `"4. Custom".modes.Desktop` and compute diff -- only tokens where Desktop differs from Mobile.
3. Merge with `design_handoff.colors` and `design_handoff.color_token_proposals` -- tokens resolved from Skill 0.
4. Merge with `comp_extraction_output.token_mapping` where `status = RESOLVED_PROPOSED`.

**Output table:**

```markdown
## Token Dictionary

### Typography Tokens (from temp1.json)
| Token | Mobile Value (base) | Desktop Override | Type | Collection |
|-------|-------------------|-----------------|------|------------|

### Spacing Tokens (from temp1.json)
| Token | Mobile Value (base) | Desktop Override | Type | Collection |
|-------|-------------------|-----------------|------|------------|

### Color Tokens (from design_handoff + resolution chain)
| Token | Value (HEX) | Resolved From | Collection Target | Usage |
|-------|------------|---------------|-------------------|-------|

### Component Tokens (from design_handoff)
| Token | Value | Resolved From | Usage |
|-------|-------|---------------|-------|
```

**Rules:**
- Mobile value is always the baseline -- Desktop Override column is empty when values are identical.
- Tokens from temp1.json use `{collection.token}` format for values.
- Tokens from design_handoff/CSV use concrete HEX/px/rem values.
- Group by category: Typography, Spacing, Color, Component.

### Section 2: Responsive Override Table

**Purpose**: Show only tokens that need responsive adjustments (Desktop differs from Mobile).

**Steps:**

1. Compare every token in temp1.json `Mobile` vs `Desktop`.
2. Filter: only include tokens where values differ.
3. Add tokens from design_handoff that have responsive variants.

**Output table:**

```markdown
## Responsive Override Table

Tokens listed below need responsive CSS. All other tokens are identical across breakpoints.

| Token | Base (Mobile, < 768px) | Tablet (>= 768px) | Desktop (>= 1024px) | Category |
|-------|----------------------|-------------------|---------------------|----------|
```

**Rules:**
- If Mobile = Desktop, the token does NOT appear in this table.
- Tablet column: use Mobile value unless specific tablet override exists (currently temp1.json has no tablet mode, so Tablet = Mobile).
- Desktop column: value from `"4. Custom".modes.Desktop`.
- This table directly maps to CSS `@media (min-width: ...)` rules.

### Section 3: Component Visual Spec

**Purpose**: Per-component implementation spec with resolved tokens, CSS, and touch validation.

**Steps:**

1. Take de-duplicated `component_registry` from Skill 2+3.
2. For each unique `component_key`:
   a. List all screens where it appears.
   b. Map token assignments (resolved from token_mapping).
   c. Generate mobile-first CSS snippet from `design_handoff.component_specs` or `styles.csv`.
   d. List states with visual descriptions.
   e. Check touch target compliance (>= 44x44px for interactive components).

**Output per component:**

```markdown
## Component: {ComponentName}

**Group**: {group} | **Screens**: {screen1, screen2, ...} | **Touch Target**: {pass/fail/n-a}

### Token Assignments
| Property | Token / Value | Resolved From |
|----------|--------------|---------------|

### States
| State | Visual Description | Token Changes | Trigger |
|-------|--------------------|---------------|---------|

### Mobile-First CSS
```css
/* Base: Mobile (< 768px) */
.{component-key} {
  /* mobile styles */
}

/* Tablet (>= 768px) */
@media (min-width: 768px) {
  .{component-key} {
    /* tablet overrides if any */
  }
}

/* Desktop (>= 1024px) */
@media (min-width: 1024px) {
  .{component-key} {
    /* desktop overrides if any */
  }
}
```
```

**Rules:**
- CSS is mobile-first: base = mobile, media queries = progressive enhancement.
- Interactive components (buttons, links, inputs, cards) must pass touch target check.
- CSS uses design_handoff.component_specs as base, customized per component's token assignments.
- Only include media query blocks when there are actual overrides.

### Section 4: Screen Layout Specs

**Purpose**: Per-screen layout skeleton describing mobile viewport first.

**Steps:**

1. Take `screen_registry` from Skill 2.
2. For each screen:
   a. List components in visual order (top to bottom for mobile vertical flow).
   b. Assign spacing tokens between components.
   c. Note cross-module data dependencies from `crossfile_handoff`.
   d. Add progressive enhancement notes for tablet/desktop.

**Output per screen:**

```markdown
## Screen: {Screen Name}

**Source**: {feature_file}#Wireframe | **Components**: {count} | **Viewport**: 375px (mobile base)

### Mobile Layout (375px)
```
┌─────────────────────────┐
│ {Component 1}           │  ← {spacing token}
├─────────────────────────┤
│ {Component 2}           │  ← {spacing token}
├─────────────────────────┤
│ {Component 3}           │  ← {spacing token}
└─────────────────────────┘
```

### Component Stack (mobile vertical flow)
| Order | Component | Spacing Above | Token Ref |
|-------|-----------|---------------|-----------|

### Data Dependencies
| Data Field | Source Module | Relationship |
|-----------|--------------|-------------|

### Progressive Enhancement
- **Tablet (768px+)**: {layout changes if any}
- **Desktop (1024px+)**: {layout changes if any}
```

**Rules:**
- Mobile layout is always the primary skeleton.
- Component order follows PRD Wireframe top-to-bottom.
- Spacing uses Mobile tokens from Token Dictionary.
- Cross-module dependencies come from crossfile_handoff.

### Section 5: Implementation Guide

**Purpose**: Checklist and best practices for implementing the UI from these specs.

**Steps:**

1. Compile mobile-first checklist from frontend-design and ux-guidelines.csv.
2. Add stack-specific guidelines from `stacks/{target_stack}.csv`.
3. Add quality gates from comp-extraction output.
4. Generate file index and execution order.

**Output:**

```markdown
## Implementation Guide

### Mobile-First Checklist
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] All touch targets >= 44x44px
- [ ] No horizontal scroll on mobile (375px)
- [ ] Body font-size >= 16px
- [ ] Safe area padding for notched devices (`env(safe-area-inset-*)`)
- [ ] Focus states visible on all interactive elements
- [ ] `prefers-reduced-motion` respected
- [ ] Color contrast >= 4.5:1 (WCAG AA)
- [ ] No emojis as icons (use SVG: Heroicons/Lucide)
- [ ] cursor-pointer on all clickable elements
- [ ] Responsive: 375px (base), 768px (tablet), 1024px (desktop)

### Stack Guidelines ({target_stack})
{guidelines from stacks/{target_stack}.csv}

### Quality Gates
| Gate | Value | Status |
|------|-------|--------|
| Token Resolution Rate | {resolved}/{total} ({percent}%) | {pass/fail} |
| Citation Coverage (COMPbase) | {percent}% | {pass/fail} |
| State Coverage | {covered}/{total} | {info} |
| UX Writing Coverage | {error + empty + success covered?} | {pass/fail} |
| Touch Target Compliance | {passed}/{interactive_total} | {pass/fail} |

### File Index
| File | Purpose | Read Order |
|------|---------|------------|
| `token-dictionary.md` | Token reference (mobile baseline) | 1 |
| `token-gap-registry.md` | Unresolved tokens backlog | 2 |
| `component-catalog.md` | Component specs with CSS | 3 |
| `state-visual-guide.md` | State coverage reference | 4 |
| `ux-copy-bank.md` | UX writing organized by type | 5 |
| `screen-specs/*.md` | Per-screen layout + tokens | 6 |
| `generation-manifest.md` | This file (index + quality) | 0 |
```

## Final Assembly

After generating all 5 sections, assemble into the target .md files:

| Pipeline Section | Target File |
|-----------------|------------|
| Section 1: Token Dictionary | `token-dictionary.md` |
| Section 1 (missing subset) + Skill 3 missing_tokens | `token-gap-registry.md` |
| Section 3: Component Visual Spec | `component-catalog.md` |
| Section 4: Screen Layout Specs | `screen-specs/{screen-name}.md` (1 file per screen) |
| Skill 3: State Mapping + COMPextend states | `state-visual-guide.md` |
| Skill 3: UX Writing Proposals | `ux-copy-bank.md` |
| Section 5: Implementation Guide | `generation-manifest.md` |

Output location: `{prd_folder}/ui-automation/`

## Constraints

- All output is mobile-first: Mobile values are baseline, Desktop is progressive enhancement.
- CSS snippets use `@media (min-width: ...)` breakpoints, never `max-width`.
- Screen layout specs start from 375px mobile viewport.
- Token Dictionary uses Mobile values as primary column.
- Touch target (44x44px) is COMPbase for all interactive components.
- Font size minimum 16px for body text on mobile.
- Every token/value must trace back to source: temp1.json, design_handoff, CSV, or missing.
- Do not generate CSS for components that have no token assignments at all -- mark as `needs-design-input`.
