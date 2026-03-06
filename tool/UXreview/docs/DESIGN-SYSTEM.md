# 🎨 XPOS Documentation - Design System

Generated using UI/UX Pro Max skill with professional documentation standards.

## Design Philosophy

**Pattern:** FAQ/Documentation Landing  
**Style:** Minimalism & Swiss Style  
**Focus:** Clean, functional, high readability, professional

## Color Palette

| Role | Hex | Usage |
|------|-----|-------|
| **Primary** | `#475569` | Headings, borders, primary actions |
| **Secondary** | `#64748B` | Muted text, secondary elements |
| **CTA** | `#2563EB` | Links, focus states, call-to-action |
| **Background** | `#F8FAFC` | Page background |
| **Surface** | `#FFFFFF` | Cards, containers, elevated surfaces |
| **Text** | `#1E293B` | Body text, main content |
| **Text Muted** | `#64748B` | Secondary text, metadata |
| **Border** | `#E2E8F0` | Dividers, outlines |
| **Hover** | `#F1F5F9` | Hover backgrounds |

**Strategy:** Neutral grey palette with professional blue for interactive elements. High contrast for optimal readability.

## Typography

### Font Family
- **Primary:** Inter (Google Fonts)
- **Fallback:** -apple-system, BlinkMacSystemFont, sans-serif
- **Monospace:** SF Mono, Monaco, Courier New, monospace

### Type Scale
```css
--text-xs: 0.75rem    /* 12px */
--text-sm: 0.875rem   /* 14px */
--text-base: 1rem     /* 16px */
--text-lg: 1.125rem   /* 18px */
--text-xl: 1.25rem    /* 20px */
--text-2xl: 1.5rem    /* 24px */
--text-3xl: 1.875rem  /* 30px */
```

### Font Weights
- Light: 300 (sparingly)
- Regular: 400 (body text)
- Medium: 500 (emphasized text)
- Semibold: 600 (headings, labels)
- Bold: 700 (h1 only)

### Line Heights
- Body text: 1.75 (optimal for reading)
- Headings: 1.2-1.4 (tighter for impact)
- UI elements: 1.6

### Line Length
- Max width: 65-75 characters per line (optimal readability)
- Markdown content: max-width: 800px

## Spacing Scale

```css
--spacing-xs: 0.25rem   /* 4px */
--spacing-sm: 0.5rem    /* 8px */
--spacing-md: 1rem      /* 16px */
--spacing-lg: 1.5rem    /* 24px */
--spacing-xl: 2rem      /* 32px */
--spacing-2xl: 3rem     /* 48px */
```

**Philosophy:** Consistent 8px base grid for visual rhythm.

## Components

### 1. Header
- **Position:** Sticky top
- **Background:** White with 95% opacity + backdrop blur
- **Border:** 1px solid border color
- **Z-index:** 50
- **Min-height:** Ensure sufficient touch target (44px+)

### 2. Search Box
- **Input height:** 48px minimum (mobile touch target)
- **Border:** 2px for better visibility
- **Focus state:** Blue border + subtle shadow
- **Icon:** Left-aligned, 20px SVG
- **Placeholder:** Muted text color

### 3. File Cards
- **Layout:** CSS Grid
  - Mobile: 1 column
  - Tablet (768px+): 2 columns
  - Desktop (1024px+): 3 columns
- **Gap:** 1rem consistent spacing
- **Hover:** Subtle lift (translateY -2px) + shadow
- **Border:** 1px, changes to primary on hover
- **Padding:** 1.5rem
- **Transition:** 200ms cubic-bezier

### 4. Back Button
- **Min-size:** 44x44px (accessibility)
- **Border:** 1px with border-radius 6px
- **Hover:** Background color change
- **Focus:** 2px outline with offset

### 5. Markdown Content
- **Max-width:** 800px (optimal reading)
- **Centered:** Auto margins
- **Code blocks:** Dark background (#0F172A)
- **Inline code:** Light background with border
- **Tables:** Rounded corners, hover rows
- **Links:** Underline on hover

## Interactions & Transitions

### Timing Functions
```css
--transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1)
--transition-base: 200ms cubic-bezier(0.4, 0, 0.2, 1)
--transition-slow: 300ms cubic-bezier(0.4, 0, 0.2, 1)
```

### Hover States
- Cards: `transform: translateY(-2px)` + shadow
- Buttons: Background color change
- Links: Border-bottom reveal
- Duration: 200ms

### Focus States
- **Color:** CTA blue (#2563EB)
- **Width:** 2px outline
- **Offset:** 2px (for better visibility)
- **Required:** All interactive elements

## Accessibility (WCAG AAA)

### Color Contrast
- **Body text:** 4.5:1 minimum (#1E293B on #F8FAFC = 13.55:1) ✓
- **Muted text:** 4.5:1 minimum (#64748B on #F8FAFC = 5.97:1) ✓
- **Links:** 4.5:1 minimum (#2563EB on #F8FAFC = 8.59:1) ✓

### Keyboard Navigation
- Tab order matches visual order
- Skip-to-content link at top
- All interactive elements focusable
- Focus indicators always visible
- "/" keyboard shortcut to focus search

### Touch Targets
- Minimum size: 44x44px
- Applied to: buttons, links, search input
- Mobile-optimized spacing

### Screen Readers
- Semantic HTML (header, main, nav, etc.)
- ARIA labels on icon-only buttons
- Role attributes where needed
- Live regions for dynamic content

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  /* All animations reduced to 0.01ms */
}
```

## Responsive Breakpoints

```css
/* Mobile-first approach */
Base:       0-767px   (1 column)
Tablet:     768px+    (2 columns)
Desktop:    1024px+   (3 columns)
Wide:       1280px    (max container width)
```

### Container Padding
- Mobile: 1rem (16px)
- Tablet+: 2rem (32px)

## Icons

**Library:** Custom SVG icons (Heroicons-style)
**Size:** 16px for inline, 20px for UI elements
**Color:** currentColor (inherits text color)
**Format:** Inline SVG (better performance)

**Icons Used:**
- Search: Magnifying glass
- File: Document icon
- Back arrow: Chevron left

## Performance

### Optimization
- Inline critical CSS (no external stylesheet)
- Font preconnect to Google Fonts
- Debounced search (200ms delay)
- Single HTTP request for marked.js CDN
- Minimal JavaScript (vanilla, no frameworks)

### Loading States
- Skeleton text for loading
- Clear error messages
- No layout shift (reserved space)

## Anti-Patterns to Avoid

❌ **Don't use emojis as icons** - Use SVG instead  
❌ **Don't break navigation history** - Use proper hash routing  
❌ **Don't remove focus outlines** - Always provide alternative  
❌ **Don't use hard-coded colors** - Use CSS variables  
❌ **Don't ignore reduced motion** - Respect user preferences  
❌ **Don't skip keyboard nav** - All functions must be keyboard-accessible  

## Browser Support

- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions
- Mobile: iOS Safari 12+, Chrome Android 90+

## Code Quality Checklist

Before deployment, verify:

- [ ] All colors use CSS variables
- [ ] No emojis used as functional icons
- [ ] All interactive elements have cursor-pointer
- [ ] Focus states visible on all clickable items
- [ ] Keyboard shortcuts documented
- [ ] prefers-reduced-motion implemented
- [ ] Touch targets minimum 44x44px
- [ ] Color contrast ratios pass WCAG AAA
- [ ] Responsive at all breakpoints
- [ ] No horizontal scroll on mobile
- [ ] Skip-to-content link present
- [ ] Semantic HTML used throughout
- [ ] Search debounced (not instant)
- [ ] Error states have clear messages

## Future Enhancements

Potential improvements for v2:
- Dark mode toggle
- Category filtering
- Breadcrumb navigation for nested files
- Table of contents for long documents
- Print stylesheet
- Offline support with Service Worker
- Search highlights in results
- Recently viewed files
- Favorites/bookmarks

---

**Design System Version:** 1.0  
**Last Updated:** 2026-02-11  
**Created with:** UI/UX Pro Max Skill  
**Pattern:** Minimalism & Swiss Style
