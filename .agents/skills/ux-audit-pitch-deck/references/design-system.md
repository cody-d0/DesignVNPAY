# Design System — UX Audit Pitch Deck

## Color Tokens (Dark OLED Theme)

```css
:root {
  --bg-base: #0a0e1a;
  --bg-surface: #111827;
  --bg-card: #1a2235;
  --bg-card-hover: #1f2a40;
  --text-primary: #f1f5f9;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --accent-gold: #f59e0b;
  --accent-purple: #8b5cf6;
  --accent-blue: #3b82f6;
  --severity-critical: #ef4444;
  --severity-major: #f97316;
  --severity-minor: #eab308;
  --severity-pass: #22c55e;
}
```

## Typography

```
Font sans:    'IBM Plex Sans' — body, financial trustworthy
Font display: 'Playfair Display' — headings, editorial premium
Font mono:    'IBM Plex Mono' — scores, IDs, data
```

## Motion

| Element | Duration | Trigger |
|---------|----------|---------|
| Score rings | 1.5s | IntersectionObserver |
| Counter animation | ~1.2s | IntersectionObserver |
| Scroll-reveal | 0.7s | IntersectionObserver (threshold: 0.12) |
| Card hover | 0.25s | hover |
| Reduced motion | 0.01ms | prefers-reduced-motion: reduce |

## Severity Badges

```
Critical → background: rgba(239,68,68,.15), color: #fca5a5
Major    → background: rgba(249,115,22,.15), color: #fdba74
Minor    → background: rgba(234,179,8,.15),  color: #fde047
Pass     → background: rgba(34,197,94,.15),  color: #86efac
```
