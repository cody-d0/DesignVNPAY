# Design System — UX Audit Pitch Deck

## Color Tokens (Light Theme — WCAG AA Compliant)

All text-on-background pairs verified ≥ 4.5:1 contrast ratio (WCAG AA).

```css
:root {
  /* Backgrounds */
  --bg-base: #ffffff;
  --bg-surface: #f8fafc;
  --bg-card: #ffffff;
  --bg-card-hover: #f1f5f9;

  /* Text — WCAG AA verified */
  --text-primary: #0f172a;    /* 17.85:1 on white — AAA */
  --text-secondary: #475569;  /*  7.58:1 on white — AAA */
  --text-muted: #64748b;      /*  4.76:1 on white — AA  */

  /* Accents — AA verified */
  --accent-gold: #b45309;     /*  5.02:1 on white */
  --accent-purple: #7c3aed;   /*  5.70:1 on white */
  --accent-blue: #2563eb;     /*  5.17:1 on white */

  /* Severity — AA verified */
  --sev-critical: #b91c1c;    /*  6.47:1 on white */
  --sev-critical-bg: rgba(185,28,28,.08);
  --sev-major: #c2410c;       /*  5.18:1 on white */
  --sev-major-bg: rgba(194,65,12,.08);
  --sev-minor: #92400e;       /*  7.09:1 on white — AAA */
  --sev-minor-bg: rgba(146,64,14,.08);
  --sev-pass: #15803d;        /*  5.02:1 on white */
  --sev-pass-bg: rgba(21,128,61,.08);

  /* Borders */
  --border: #e2e8f0;
  --border-light: #cbd5e1;
}
```

## Typography

```
Font: 'Manrope' — all text (headings, body, data, scores)
Weights: 400 (body), 500 (labels), 600 (nav/tags), 700 (headings), 800 (hero/display)
Google Fonts: https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap
```

## Contrast Rules

| Element | Color used | Min ratio |
|:---|:---|:---|
| Body text | text-primary | 17.85:1 AAA |
| Secondary text (descriptions) | text-secondary | 7.58:1 AAA |
| Muted text (meta labels) | text-muted | 4.76:1 AA |
| Hero sub text | text-secondary | 7.58:1 AAA |
| Nav links | text-secondary | 7.58:1 AAA |
| Severity badges | sev-* tokens | ≥5.02:1 AA |

> **Rule**: `--text-muted` MUST NOT be used on colored/gradient backgrounds (hero).
> Use `--text-secondary` for small text on non-white surfaces.

## Data Display Rules

- **No Pass stats**: Only show gaps/issues — do not display pass counts
- **No title truncation**: Finding card h3 titles display full content
- **No content truncation**: Hiện trạng and proposal sections display full text

## Motion

| Element | Duration | Trigger |
|---------|----------|---------|
| Scroll-reveal | 0.7s | IntersectionObserver (threshold: 0.12) |
| Card hover | 0.25s | hover + translateY(-2px) |
| Reduced motion | 0.01ms | prefers-reduced-motion: reduce |

## Severity Badges

```
Critical → background: rgba(185,28,28,.08), color: #b91c1c  (6.47:1)
Major    → background: rgba(194,65,12,.08), color: #c2410c  (5.18:1)
Minor    → background: rgba(146,64,14,.08), color: #92400e  (7.09:1)
```

## Score Ring SVG Formulas

All use: `stroke-dashoffset = circumference × (1 - score/100)`

```
Overall hero ring:   r=51, circumference=320
Screen score rings:  r=25, circumference=157
Heuristic rings:     r=33, circumference=207

Color thresholds:
  <50%  → --sev-critical (#b91c1c)
  50-69% → --sev-major (#c2410c)
  ≥70%  → --sev-pass (#15803d)
```
