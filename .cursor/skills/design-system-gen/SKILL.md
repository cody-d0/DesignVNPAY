---
name: design-system-gen
description: "Generate design system recommendation from ui-ux-pro-max for a given product type. Outputs design_handoff with style, colors (HEX), typography (fonts + CSS import), component CSS specs, and anti-patterns. Mobile-first by default. Use as Skill 0 in prd-full-pipeline before extraction skills."
---

# Design System Generation -- Skill 0

Generate a complete design system recommendation using `ui-ux-pro-max` as the foundation layer for downstream extraction and visual spec skills. All output is **mobile-first**.

## When to Use

- Before running pdr-extract / pdr-analyze / comp-extraction in a pipeline
- When a project needs color palette, typography, style direction, and component CSS specs
- When pipeline output shows 90%+ `missing_token` -- this skill fills the gap

## Input Contract

| Parameter | Required | Description |
|-----------|----------|-------------|
| `product_type` | Yes | Product description for search query (e.g. "POS retail payment mobile app") |
| `project_name` | Yes | Project name for output header (e.g. "XPOS") |
| `target_stack` | No | Default `html-tailwind`. Options: `react`, `vue`, `nextjs`, `flutter`, etc. |
| `output_dir` | No | Default `{prd_folder}/ui-automation/design-system/` |

## Process

### Step 1 -- Generate Design System

Run the ui-ux-pro-max design system generator with a mobile-first query:

```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py \
  "{product_type} mobile touch-first" \
  --design-system --persist -p "{project_name}" -f markdown
```

The `--persist` flag creates:
- `design-system/{project-slug}/MASTER.md` -- Global design rules
- `design-system/{project-slug}/pages/` -- Page-specific override folder

### Step 2 -- Extract design_handoff

Parse the design system generator output into a structured `design_handoff` object for downstream skills.

**design_handoff structure:**

```
design_handoff:
  style:
    name: string          # e.g. "Minimalism & Swiss Style"
    keywords: string      # e.g. "Clean, simple, spacious, functional"
    effects: string       # e.g. "Subtle hover (200-250ms), smooth transitions"
    performance: string   # e.g. "Excellent"
    accessibility: string # e.g. "WCAG AAA"
  colors:
    primary: string       # HEX e.g. "#0F172A"
    secondary: string     # HEX e.g. "#334155"
    cta: string           # HEX e.g. "#0369A1"
    background: string    # HEX e.g. "#F8FAFC"
    text: string          # HEX e.g. "#020617"
    border: string        # HEX (from colors.csv Notes or inferred)
    notes: string         # Color strategy notes
  typography:
    heading_font: string  # e.g. "Plus Jakarta Sans"
    body_font: string     # e.g. "Plus Jakarta Sans"
    mood: string          # e.g. "friendly, modern, saas, clean"
    google_fonts_url: string
    css_import: string
    tailwind_config: string
  pattern:
    name: string          # e.g. "Dashboard + Stats + Action Grid"
    sections: string      # e.g. "Header > Stats > Quick Actions > Recent"
    cta_placement: string
  anti_patterns: string   # What to avoid
  component_specs:
    buttons: string       # CSS for primary + secondary buttons
    cards: string         # CSS for cards
    inputs: string        # CSS for inputs + focus state
    modals: string        # CSS for modal overlay + content
  spacing:
    xs: string            # "4px / 0.25rem"
    sm: string            # "8px / 0.5rem"
    md: string            # "16px / 1rem"
    lg: string            # "24px / 1.5rem"
    xl: string            # "32px / 2rem"
    2xl: string           # "48px / 3rem"
  shadows:
    sm: string            # Subtle lift
    md: string            # Cards, buttons
    lg: string            # Modals, dropdowns
```

### Step 3 -- Supplement with Domain Searches (if needed)

Run additional targeted searches to fill gaps:

```bash
# Get stack-specific best practices
python3 .agents/skills/ui-ux-pro-max/scripts/search.py \
  "mobile touch form" --stack {target_stack}

# Get mobile-specific UX rules
python3 .agents/skills/ui-ux-pro-max/scripts/search.py \
  "touch target mobile interaction" --domain ux

# Get icon recommendations
python3 .agents/skills/ui-ux-pro-max/scripts/search.py \
  "{product_type}" --domain style
```

### Step 4 -- Build Color Token Proposal

Using `design_handoff.colors` + `.agents/skills/ui-ux-pro-max/data/colors.csv`, build a proposed token set to fill gaps in `temp1.json`:

| Proposed Token | HEX Value | Mapped From | Collection Target |
|----------------|-----------|-------------|-------------------|
| `color.primary` | `{colors.primary}` | design_system | 2. Theme |
| `color.secondary` | `{colors.secondary}` | design_system | 2. Theme |
| `color.cta` | `{colors.cta}` | design_system | 2. Theme |
| `color.background` | `{colors.background}` | design_system | 3. Mode |
| `color.text` | `{colors.text}` | design_system | 3. Mode |
| `color.border` | `{colors.border}` | design_system | 3. Mode |
| `color.error` | `#EF4444` | ux-convention | 2. Theme |
| `color.success` | `#22C55E` | ux-convention | 2. Theme |
| `color.warning` | `#F59E0B` | ux-convention | 2. Theme |
| `button.primary.bg` | `{colors.cta}` | design_system | 2. Theme |
| `button.primary.text` | `#FFFFFF` | contrast-rule | 2. Theme |
| `button.outline.border` | `{colors.primary}` | design_system | 2. Theme |
| `input.focus.border` | `{colors.primary}` | design_system | 2. Theme |
| `nav.active` | `{colors.cta}` | design_system | 2. Theme |
| `nav.inactive` | `{colors.secondary}` | design_system | 2. Theme |
| `badge.success` | `#22C55E` | ux-convention | 2. Theme |
| `badge.error` | `#EF4444` | ux-convention | 2. Theme |
| `growth.positive` | `#22C55E` | ux-convention | 2. Theme |
| `growth.negative` | `#EF4444` | ux-convention | 2. Theme |

This table becomes part of the `design_handoff` and is used by downstream skills (pdr-analyze Phase 3, comp-extraction Phase 5) to resolve `missing_token` entries.

## Output

### Markdown (always)

Output a single markdown document with sections:

1. **Design System Summary** -- style, pattern, key effects
2. **Color Palette** -- table with Role, HEX, CSS Variable
3. **Typography** -- fonts, CSS import, mood
4. **Spacing & Shadows** -- token tables
5. **Component CSS Specs** -- mobile-first CSS for buttons, cards, inputs, modals
6. **Color Token Proposals** -- proposed tokens to fill temp1.json gaps
7. **Anti-Patterns** -- what to avoid
8. **Mobile-First Checklist** -- viewport, touch targets, safe area, font size

### design_handoff (structured data for downstream skills)

Passed as internal data to Skill 1-4 in the pipeline. Not exported to user unless requested.

## Mobile-First Constraints

- All CSS snippets use base styles for mobile, `@media (min-width: 768px)` for tablet, `@media (min-width: 1024px)` for desktop.
- Touch targets minimum 44x44px in all component specs.
- Font size minimum 16px for body text on mobile.
- Query to ui-ux-pro-max always includes "mobile" keyword.
- Color Token Proposals use mobile-appropriate contrast (outdoor readability).

## Constraints

- design_handoff.colors must have concrete HEX values (not token references).
- design_handoff.typography must have concrete font names (not "system font").
- All proposed tokens must follow `{group.purpose}` naming convention.
- Do not hardcode if an equivalent token exists in temp1.json.
- If ui-ux-pro-max search returns no results for a domain, use sensible defaults from `colors.csv` row matching the product type.
