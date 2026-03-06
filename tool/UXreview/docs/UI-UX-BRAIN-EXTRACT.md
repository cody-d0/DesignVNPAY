# Trích xuất thông tin UI/UX từ Brain (Design Data Layer + ui-ux-pro-max)

> Tài liệu này tổng hợp các thông tin UI/UX từ **bộ kiến thức** (knowledge layer) trong repo: Design Data Layer (DDL) và skill **ui-ux-pro-max**. Dùng làm tham chiếu nhanh cho automation UI, PRD, design system, và pipeline.

---

## 1. Design Data Layer (DDL) — Tổng quan

- **Định nghĩa:** Bộ kiến thức (knowledge layer) gọi on-demand: component, state, token, layout, copy cho automation UI. **Không** phải database nghiệp vụ (Thiết kế Database).
- **Phạm vi query:** toàn bộ, token_only, component_only, state_only, screen:{id}, compbase_only, compextend_only.
- **Output materialized:** `ui-automation/*`, `mockup-spec.json`, `generation-manifest.md`.

### Views

| View | Nội dung | Artifact |
|------|----------|----------|
| **token_view** | Typography, spacing, color, component tokens | token-dictionary.md, token-gap-registry.md |
| **component_view** | Component registry + token + states | component-catalog.md, component_registry trong mockup-spec.json |
| **state_view** | Component × state × trigger × token | state-visual-guide.md |
| **screen_view** | Layout theo screen | screen-specs/{id}.md |
| **Copy (UX writing)** | Labels, error, empty, success, retry | ux-copy-bank.md |

### Hierarchy: GLOBAL → PRODUCT

- **GLOBAL:** Token gốc, ux-guidelines.csv, web-interface.csv, ux-laws.csv, styles/colors/typography base, component taxonomy. Nguồn: `.agents/skills/ui-ux-pro-max/data/`, `design-data-layer/global/`.
- **PRODUCT:** Theme/mode overrides, product-specific component keys, screen_registry, ux_overrides. Nguồn: `design-data-layer/products/{product_id}/`.
- **Resolution:** PRODUCT override GLOBAL khi có giá trị tương ứng.

### Constraints

- **Citation:** COMPbase 100% từ PRD; COMPextend bắt buộc `ux_rule_ref`.
- **Token:** Format `{collection.token}`; hierarchy TailwindCSS → Theme → Mode → Custom.
- **State chuẩn:** default, focus, active, disabled, loading, error, success, empty.

### Screen boundaries (Figma)

- screen_id, screen_name_vi, artboard_node_ids[], screen_type (form, confirm, result, list, detail, error, onboarding, search, filter…).

---

## 2. Nguồn dữ liệu ui-ux-pro-max (GLOBAL)

**Canonical path:** `.agents/skills/ui-ux-pro-max/`

| File | Vai trò |
|------|--------|
| ux-guidelines.csv | UX rules (accessibility, touch, error feedback…); §2 AC, §5 NFR, COMPextend |
| web-interface.csv | Web UI patterns; form/validation/keyboard, §2 Business Rule, AC |
| ux-laws.csv | UX laws (Fitts, Hick, Jakob, Miller, Doherty…); citation cho guidelines |
| colors.csv | Palettes HEX theo product type; design system, token |
| typography.csv | Font pairings, sizes; design system, NFR |
| styles.csv | Style recommendations (Minimalism, Glassmorphism, Dark Mode…) |
| icons.csv | Icon usage; §3 Mô tả, aria-label |
| ui-reasoning.csv | Reasoning rules theo UI_Category; COMPextend, pdr-analyze |

---

## 3. UX Guidelines — Tóm tắt theo category

(Trích từ `ux-guidelines.csv` — 99 rules)

### Navigation
- Smooth scroll (`scroll-behavior: smooth`), sticky nav + padding compensation, active state rõ ràng, back button đúng lịch sử, deep linking (URL phản ánh state), breadcrumbs cho 3+ cấp.

### Animation
- Giảm motion: 1–2 key elements/view; 150–300ms micro-interactions; `prefers-reduced-motion`; loading states (skeleton/spinner); không chỉ hover trên touch; infinite animation chỉ cho loader; dùng transform/opacity; ease-out/ease-in.

### Layout
- Z-index scale (10, 20, 30, 50); tránh overflow hidden cắt nội dung; fixed positioning có safe area; content jumping: reserve space (aspect-ratio/fixed height); viewport: dvh thay 100vh mobile; container text: max-width 65–75ch.

### Touch (Mobile)
- Touch target tối thiểu 44×44px; khoảng cách giữa target ≥ 8px; tránh gesture conflict với system; tap delay: touch-action / fastclick; pull-to-refresh tắt khi không cần; haptic có chừng mực.

### Interaction
- Focus states visible (focus:ring-2); hover states; active/pressed state; disabled rõ (opacity + cursor-not-allowed); loading button: disable + spinner; error/success feedback rõ; confirmation cho hành động destructive.

### Accessibility
- Color contrast ≥ 4.5:1 (normal text); không chỉ dùng màu để truyền thông tin; alt text cho ảnh; heading hierarchy h1→h6; aria-label cho nút chỉ icon; keyboard navigation; semantic HTML + ARIA; label cho input; error với role=alert/aria-live; skip links.

### Performance
- Image optimization (size, WebP); lazy loading below-fold; code splitting; cache headers; font-display swap/optional; script async/defer; bundle size; critical CSS inline.

### Forms
- Label visible (không chỉ placeholder); error dưới field; validate on blur; input type phù hợp (email, tel, number…); autocomplete; required indicators; password visibility toggle; submit feedback (loading → success/error); input affordance; mobile: inputmode.

### Responsive
- Mobile first; test 320, 375, 414, 768, 1024, 1440; touch-friendly; body text ≥ 16px mobile; viewport meta; tránh horizontal scroll; image max-width:100%.

### Typography
- Line height 1.5–1.75 body; line length 65–75 ch; font size scale nhất quán; font loading + fallback; contrast readability; heading khác body (size/weight).

### Feedback
- Loading > 300ms: spinner/skeleton; empty states có message + action; error recovery (Try again + help); progress multi-step; toast auto-dismiss 3–5s; confirmation sau success.

### Content
- Truncate + expand; date/number format locale; placeholder realistic.

### AI Interaction
- Ghi rõ nội dung AI; streaming thay vì chờ full text; feedback loop (thumbs up/down, Regenerate).

### Sustainability
- Video click-to-play / pause off-screen; asset nén, lazy load 3D.

---

## 4. Web Interface rules — Điểm chính

(Trích từ `web-interface.csv`)

- **Accessibility:** Icon button có aria-label; form control có label/aria-label; keyboard (onKeyDown + tabIndex); semantic HTML (button/a/label trước ARIA); aria-live cho async; decorative icon aria-hidden.
- **Focus:** Focus-visible ring; không outline-none không thay thế; checkbox/radio hit target chung với label.
- **Forms:** autocomplete; input type semantic; không chặn paste; spellcheck=false cho code/email; submit enabled + spinner khi loading; inline errors gần field.
- **Performance:** Virtualize list > 50 items; tránh layout read trong render; batch DOM write/read; preconnect CDN; lazy load ảnh below-fold.
- **State:** URL phản ánh state (query params); deep linking; confirm destructive.
- **Typography:** Unicode đúng (ellipsis, quotes); truncate/line-clamp; nbsp cho số + đơn vị.
- **Anti-pattern:** Không disable zoom viewport; tránh transition:all (chỉ định property); outline-none phải có ring thay thế; date/number dùng Intl.

---

## 5. UX Laws — Tham chiếu

(Trích từ `ux-laws.csv` — dùng làm ux_law_ref trong citation)

| law_id | Tên | Statement ngắn |
|--------|-----|-----------------|
| fitts | Fitts's Law | Thời gian chạm mục tiêu phụ thuộc khoảng cách và kích thước → target lớn, gần = nhanh hơn |
| hick | Hick's Law | Nhiều lựa chọn → quyết định chậm hơn |
| jakob | Jakob's Law | User quen site khác → làm giống convention |
| miller | Miller's Law | Working memory ~7±2 items → chunking |
| doherty | Doherty Threshold | Tương tác < 400ms → productivity cao |
| peak-end | Peak-End Rule | Trải nghiệm nhớ theo peak + kết thúc |
| gestalt-proximity | Proximity | Gần nhau → nhóm với nhau |
| von-restorff | Von Restorff | Nổi bật → dễ nhớ |
| cognitive-load | Cognitive Load | Giảm tải nhận thức không cần thiết |
| goal-gradient | Goal-Gradient | Gần đích → động lực tăng (progress bar) |
| wcag-* | WCAG POUR | Perceivable, Operable, Understandable, Robust |
| nng-* | Nielsen Heuristics | Visibility, match world, user control, consistency, error prevention, recognition vs recall, flexibility, minimal design, error recovery, help |

---

## 6. UI Reasoning / Product-Style mapping (ui-reasoning.csv)

Mỗi **UI_Category** (SaaS, E-commerce, Healthcare, Fintech, Government…) có:
- **Recommended_Pattern** (Hero+CTA, Feature-Rich, Conversion-Optimized…)
- **Style_Priority** (Glassmorphism, Minimalism, Accessible & Ethical…)
- **Color_Mood**, **Typography_Mood**, **Key_Effects**
- **Decision_Rules** (if_ux_focused, must_have WCAG…)
- **Anti_Patterns** (tránh: excessive animation, dark mode mặc định, AI purple/pink gradient tùy ngành)

Ví dụ: Government/Public → Accessible & Ethical, WCAG AAA, keyboard navigation; Fintech Banking → Trust & Authority, security-first; Healthcare → wcag-aaa-compliance, calm blue/green.

---

## 7. Colors (colors.csv)

Theo **Product Type**: Primary, Secondary, CTA, Background, Text, Border (HEX). Ví dụ:
- SaaS: #2563EB, #F97316 CTA, #F8FAFC bg
- E-commerce Luxury: dark + gold #CA8A04
- Government: navy #0F172A, blue #0369A1
- Healthcare: cyan #0891B2, green #059669

---

## 8. Styles (styles.csv)

**Style Category:** Minimalism, Neumorphism, Glassmorphism, Brutalism, 3D & Hyperrealism, Vibrant & Block-based, Dark Mode (OLED), Accessible & Ethical, Claymorphism, Aurora UI, Retro-Futurism, Flat Design, Skeuomorphism, Liquid Glass, Motion-Driven, Micro-interactions, Inclusive Design, Zero Interface, Soft UI Evolution, Hero-Centric, Conversion-Optimized, Feature-Rich Showcase, Data-Dense Dashboard, Heat Map, Bento Box Grid, Neubrutalism…

Mỗi style có: Primary/Secondary Colors, Effects & Animation, Best For, Do Not Use For, Light/Dark, Performance, Accessibility, Mobile-Friendly, Framework Compatibility, Implementation Checklist, Design System Variables.

---

## 9. Icons (icons.csv)

**Library:** Lucide. Categories: Navigation (menu, arrow-left/right, chevron, home, x, external-link), Action (plus, minus, trash, edit, save, download, upload, copy, share, search, filter, settings), Status (check, check-circle, x-circle, alert-triangle, alert-circle, info, loader, clock), Communication (mail, message-circle, phone, send, bell), User (user…)…

Usage: aria-label cho icon-only button; decorative → aria-hidden.

---

## 10. Query contract (DDL)

- **Query by View:** token_view, component_view, state_view, screen_view.
- **Query by Scope:** GLOBAL | PRODUCT (product_id).
- **Query by Pattern:** keyword (e.g. "touch target", "focus state") → UX rules/ux-laws.
- **Citation:** Khi dùng guideline từ ux-guidelines.csv/web-interface.csv, nếu có ux_law_ref thì ghi cả law (vd: ux-guidelines.csv#22 → Fitts's Law).

---

## 11. Đường dẫn tham chiếu

| Nội dung | Đường dẫn |
|----------|-----------|
| DDL docs | `.cursor/docs/ddl/` (README, contract, hierarchy, glossary, views-and-outputs, governance) |
| ui-ux-pro-max reference | `.cursor/docs/ui-ux-pro-max-reference.md` |
| Skill ui-ux-pro-max | `.agents/skills/ui-ux-pro-max/SKILL.md` |
| Data CSV | `.agents/skills/ui-ux-pro-max/data/` |
| Search script | `.agents/skills/ui-ux-pro-max/scripts/search.py` |
| Pro-blocks (GLOBAL) | `design-data-layer/global/pro-blocks/` |

---

*File này được sinh từ trích xuất Design Data Layer và ui-ux-pro-max; cập nhật khi DDL hoặc CSV thay đổi.*
