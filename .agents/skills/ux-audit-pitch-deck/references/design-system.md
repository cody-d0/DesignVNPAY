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

## Layout — Finding Cards (Section 4)

Table-based scannable layout with side-by-side phone + data:

| Class | Purpose | Spec |
|-------|---------|------|
| `.finding-card` | Card container | border-radius:12px, hover shadow |
| `.finding-accent.{sev}` | Top color bar | height:3px, severity color |
| `.card-header` | Header row | flex, bg-surface, border-bottom |
| `.card-id` | UXP-ID badge | blue bg, rounded |
| `.card-body` | Main content | `grid-template-columns: 420px 1fr` |
| `.card-visual` | Screenshot panel | bg-surface, border-right |
| `.phone-frame` | Clickable image | border-radius:16px, hover scale |
| `.card-table` | Data rows | border-collapse, full width |
| `.td-label` | Label column | width:110px, uppercase 10.5px |
| `.td-value.proposal` | Solution cells | green-tinted bg, ul padding |
| `.card-footer` | Tags + refs | flex-column, bg-surface |

## Layout — Gap Cards (Section 6)

Table-based scannable layout:

| Class | Purpose | Spec |
|-------|---------|------|
| `.gap-card` | Card container | border-radius:10px, hover shadow |
| `.gap-header` | Header row | flex, bg-surface, border-bottom |
| `.gap-num` | Circle number | 24×24 blue circle, white text |
| `.gap-ref` | Ref badge | purple bg, 10px font |
| `.gap-screen` | Screen ID badge | blue bg, white-space:nowrap |
| `.gap-table` | Data rows | border-collapse, full width |
| `.gap-table .td-label` | Label column | width:120px, uppercase |
| `.gap-table .td-ddl` | DDL evidence | italic, muted color |
| `.gap-table .td-ref` | Reference cell | reduced padding |

## Lightbox System

Fullscreen image viewer triggered by clicking phone frames or 📸 citations:

| Class | Purpose | Spec |
|-------|---------|------|
| `.img-cite` | Clickable citation | blue bg, hover scale+shadow |
| `.lightbox-overlay` | Backdrop | fixed, rgba(0,0,0,.85), blur(8px) |
| `.lightbox-overlay.active` | Visible state | display:flex, opacity:1 |
| `.lightbox-overlay img` | Large image | max-width:90vw, max-height:80vh |
| `.lightbox-close` | Close button | 40×40 circle, top-right |
| `.lightbox-caption` | Filename | monospace, semi-transparent bg |

## Motion

| Element | Duration | Trigger |
|---------|----------|---------|
| Scroll-reveal | 0.7s | IntersectionObserver (threshold: 0.12) |
| Card hover | 0.2s-0.25s | hover + translateY(-2px) or shadow |
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

## Responsive Breakpoint

```css
@media (max-width: 960px) {
  /* Card body: single column */
  /* Phone frame: max-width 420px centered */
  /* Hero score ring: hidden */
  /* Grids: single column */
  /* Padding reduced: 32px 24px */
  /* Table labels: 90px width */
}
```
