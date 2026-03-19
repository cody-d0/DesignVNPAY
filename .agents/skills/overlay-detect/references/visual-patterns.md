# Visual Patterns for Overlay Detection

Reference for agent vision analysis of overlay/modal/bottom-sheet patterns.

## Pattern 1: Dimmed Background (S3 — weight 3)

**What to look for:**
- Semi-transparent dark layer behind content (rgba black 30-70% opacity)
- Previous screen partially visible but darkened
- Content card/sheet appears "elevated" from background

**Strong indicators:** Background content is readable but clearly dimmed.
**Weak indicators:** Background is solid color (might just be a white screen, not overlay).

**Not overlay:** Solid background matching the screen's own color scheme (white, themed gray).

## Pattern 2: Close Affordance (S4 — weight 2)

**Types:**
| Type | Visual | Position |
|------|--------|----------|
| X button | × or close icon | Top-right of sheet/modal title bar |
| Swipe indicator | Horizontal pill/bar ~40px wide | Top-center of bottom sheet |
| Pull handle | Thin gray bar ~32-48px | Top-center, above content |
| Implicit close | Dimmed background is tappable | Darkened area outside modal |
| Back only | ← back arrow | Top-left (usually NOT overlay — this is navigation) |

**Key distinction:** `← Back` in header = **screen navigation** (NOT overlay).  `× Close` or swipe bar = **overlay dismiss** (IS overlay).

## Pattern 3: Partial Screen Coverage (S5 — weight 2)

**Bottom sheet patterns:**
- Content starts at 20-80% from top of viewport
- Dimmed area visible above the sheet
- Rounded top corners on the content card

**Centered modal:**
- Content card centered vertically and horizontally
- Dimmed area visible on all sides
- Usually has rounded corners

**Full-screen modal:**
- Content covers entire viewport
- Distinguished by close X (not back arrow) and no system navigation
- Score via S4 (close X) not S5

## Pattern 4: Shared Header (S2 — weight 2)

**What to compare:**
- Read the header area (top ~100-120px below status bar) of the candidate overlay
- Compare with other artboards in the same section
- If 2 artboards share the same title text in header → one is likely an overlay on the other

**Example:** Two artboards both show "Xác nhận giao dịch" header. One has transaction details + "Xác nhận" button. The other shows the same header but with an OTP bottom sheet over it. → The OTP artboard is an overlay on the confirm artboard.

## Pattern 5: Picker/Selector List (S6 — weight 1)

**Indicators:**
- Scrollable list of selectable items
- Search bar at top
- Each item has consistent structure (icon + name + details)
- Title describes what is being selected ("Danh bạ thụ hưởng", "Ngân hàng thụ hưởng")

**Common banking pickers:** Contact list, bank list, branch list, account selector, fee type selector.

## Decision Matrix (Quick Reference)

| Visual Pattern | S1 | S2 | S3 | S4 | S5 | S6 | S7 | Min Score |
|---------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---------:|
| Bottom sheet with dim BG | ? | ? | ✅3 | ✅2 | ✅2 | ? | ? | **7+** |
| Full-screen picker with X | ✅1 | — | — | ✅2 | — | ✅1 | ✅1 | **5** |
| OTP on confirm screen | ✅1 | ✅2 | ✅3 | ✅2 | — | — | — | **8** |
| Keyboard state on form | ✅1 | ✅2 | — | — | — | — | — | **3** ❌ |
| Error dialog | ? | — | ✅3 | ✅2 | ✅2 | — | — | **7+** |
| Loading state | ✅1 | ✅2 | — | — | — | — | — | **3** ❌ |
