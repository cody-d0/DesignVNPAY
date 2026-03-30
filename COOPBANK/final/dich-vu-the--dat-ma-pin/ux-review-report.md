# UX Audit — Đặt mã PIN thẻ · Co-opBank

> **Module:** Dịch vụ thẻ · **Section:** Đặt mã PIN thẻ  
> **Generated:** 2026-03-23 · **Pipeline:** figma-to-ux-review v1  
> **Screens audited:** 3 (SCR-PIN-001, SCR-PIN-002, SCR-PIN-003)  
> **DDL:** `ddl-context.json` · Banking product · 69 guidelines · 60 laws

---


**Total checks:** 27  
**Pass:** 10 | **Gap:** 16 | **Unverifiable:** 1  
**Simple Score:** 37%  
**Weighted Score:** 37%## Tổng quan

| Metric | Value |
|---|---|
| Tổng check | 24 |
| Pass: 11 \| Gap: 12 \| Unverifiable: 1 | — |
| UX Score: 37% | Simple (11/24) |

---

## Đề xuất cải tiến

### Critical

- **[UXP-001]** Screen: `SCR-PIN-002` | **Không có inline error khi 2 PIN không khớp**
- **[UXP-002]** Screen: `SCR-PIN-002` | **Không có loading state sau submit — double-submit risk**
- **[UXP-003]** Screen: `SCR-PIN-003` | **Không có processing indicator sau face detection**

### Major

- **[UXP-004]** Screen: `SCR-PIN-002` | **Lockout warning (5 sai = khóa) chỉ trong overlay**
- **[UXP-005]** Screen: `SCR-PIN-002` | **CTA label ambiguous: Xác nhận vs Tiếp tục**
- **[UXP-006]** Screen: `SCR-PIN-002` | **Custom numpad chặn paste vi phạm Never Block Paste**
- **[UXP-007]** Screen: `SCR-PIN-002` | **6-cell PIN không có accessible names**
- **[UXP-008]** Screen: `SCR-PIN-002` | **Không có realtime PIN match indicator**
- **[UXP-009]** Screen: `SCR-PIN-003` | **Không có error/retry state khi face auth thất bại**

### Minor

- **[UXP-010]** Screen: `SCR-PIN-002` | **Notice rules bị truncate khi keyboard open**
- **[UXP-011]** Screen: `SCR-PIN-002` | **Error dialog Đồng ý destination không rõ**
- **[UXP-012]** Screen: `SCR-PIN-003` | **Thiếu bridge explanation tại sao cần face auth**

---

## Chi tiết theo màn hình

### 1. Dịch vụ thẻ (`SCR-PIN-001`)

> `SCR-PIN-001` · list · 2 artboards

**Score: 57% | Pass: 4 | Gap: 3**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|---|---|---|---|---|
| 1 | Touch target ≥ 44×44px cho 4 icon action grid | Skill A | UXG-165 | Gap | Từ ảnh: 4 action icons ~40×40px — nhỏ hơn WCAG/Apple 44pt minimum |
| 2 | Back button predictable (top-left, history) | Skill A | UXG-147 | Pass | Từ ảnh: `<` top-left, consistent iOS/Android placement |
| 3 | Von Restorff: Cài đặt PIN thẻ visually distinct | Skill A | UXG-219 | Gap | Từ ảnh: 4 icons cùng visual weight, size, màu — không có badge phân biệt |
| 4 | Status badge Hoạt động không convey bằng màu đơn | Skill A | UXG-180 | Pass | Badge xanh + text Hoạt động — text kèm màu ✅ |
| 5 | Hạn mức masked reveal pattern nhất quán | Skill A | UXG-197 | Gap | Hạn mức `******** VND` không có ic_eye (khác Số thẻ có ic_eye) |
| 6 | Card count badge — user biết đang xem card nào | Skill B | miller | Pass | Pagination dots (3 dots, 1 active) hiện diện |
| 7 | Carousel arrows contrast vs card art background | Skill B | UXG-219 | Pass | Arrows được đặt trên vùng tối, contrast acceptable |

---

### 2. Cài đặt mã PIN (`SCR-PIN-002`)

> `SCR-PIN-002` · form · 8 artboards (4 overlays)

**Score: 29% | Pass: 4 | Gap: 10**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|---|---|---|---|---|
| 1 | Inline error khi 2 PIN không khớp | Skill A | UXG-176 | Gap | Không có error state dưới field Nhập lại mã PIN |
| 2 | Loading state sau submit | Skill A | UXG-221 | Gap | CTA direct→overlay, không có intermediate spinner |
| 3 | Lockout warning (5 lần sai) trong form chính | Skill A | UXG-176 | Gap | Warning chỉ trong overlay auth sheet, không trong main form |
| 4 | CTA label nhất quán (không thay đổi label) | Skill A | UXG-204 | Gap | State 1: Xác nhận; State 2: Tiếp tục — 2 labels khác nhau |
| 5 | Notice rules không bị truncate khi keyboard open | Skill A | UXG-197 | Gap | Rules bị cắt dưới edge notice section khi keyboard mở |
| 6 | Never Block Paste — numpad không chặn paste | Skill B | UXG-254 | Gap | Custom numpad thay system keyboard → không paste được |
| 7 | Accessible name cho 6-ô PIN input | Skill B | UXG-183 | Gap | 6 cells không có individual ARIA label |
| 8 | Submit feedback — Facepay error destination rõ | Skill B | UXG-204 | Gap | Nút Đồng ý trong dialog Facepay không có action destination |
| 9 | Touch target numpad keys ≥ 44×44pt | Skill B | UXG-165 | Pass | Keys ~56-60px height — đủ lớn |
| 10 | Confirmation dialog trước action (xác thực giao dịch) | Skill B | UXG-178 | Pass | Overlay Xác thực giao dịch hiện diện trước commit |
| 11 | Realtime PIN match indicator (field 2 vs field 1) | Skill B | UXG-176 | Gap | Field 2 đủ 6 chấm nhưng không có match indicator |
| 12 | Success dialog clear (checkmark + text) | Skill C | UXG-204 | Pass | Checkmark circle + text thành công — clear signal |
| 13 | Error dialogs pattern nhất quán (layout) | Skill C | UXG-178 | Pass | 2 error states cùng structure, nhất quán |
| 14 | Lockout warning color urgency (amber/warning) | Skill C | UXG-219 | Gap | Warning text cùng font/color với body — không đủ urgency |

---

### 3. Xác thực khuôn mặt (`SCR-PIN-003`)

> `SCR-PIN-003` · verify · 1 artboard

**Score: 33% | Pass: 2 | Gap: 3**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|---|---|---|---|---|
| 1 | Processing indicator sau face detection | Skill A | UXG-153 | Gap | UI static sau face detected — không có spinner/progress |
| 2 | Error/retry state khi face auth thất bại | Skill A | UXG-176 | Gap | Chỉ 1 artboard — không có error/retry state |
| 3 | Camera permission denied state | Skill A | UXG-176 | Unverifiable | Không có artboard permission denied — không verify được |
| 4 | Bridge explanation: tại sao face auth sau PIN | Skill B | jakob | Gap | Jump PIN→Face auth không có transition/explanation |
| 5 | Font size instruction banner ≥ 16px | Skill B | UXG-210 | Pass | Đưa mặt vào giữa khung hình — ước tính ≥18px, rõ ràng |
| 6 | Back button nhất quán (top-left) | Skill B | UXG-147 | Pass | `<` top-left — nhất quán với toàn flow |

---

## DDL References

| DDL ID | Nội dung | Áp dụng |
|---|---|---|
| UXG-147 | Back navigation consistency (Jakob's Law) | A2, B11 |
| UXG-153 | Loading states — processing feedback | A11, C, Phase 4e |
| UXG-165 | Touch target minimum 44×44pt (Fitts's Law) | A1, B6 |
| UXG-171 | Focus indicator visibility | C4 |
| UXG-175 | Loading button states | A7 |
| UXG-176 | Error feedback and recovery | A6, A8, A12, B8, B9 |
| UXG-178 | Confirmation dialogs before destructive actions | B7, C6 |
| UXG-180 | Color should not be only differentiator | A4, C7 |
| UXG-183 | ARIA accessible names for inputs | B4 |
| UXG-197 | Input labels and truncation | A5, A10, B5 |
| UXG-204 | Submit feedback and CTA clarity | A9, B5 |
| UXG-210 | Minimum font size 16px | B10 |
| UXG-219 | Contrast and readability | A3, B2, C1, C3 |
| UXG-221 | Loading indicators | A7, A11 |
| UXG-244 | WCAG AA accessibility | B4 |
| UXG-254 | Never block paste in input fields | B3 |
| UXG-257 | Inline error validation | A6 |
| miller | Miller's Law — 7±2 items | B1 |
| jakob | Jakob's Law — familiar patterns | A2, B9, B11 |
| doherty | Doherty Threshold — response ≤400ms | A7, A11 |
