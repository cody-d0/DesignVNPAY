# UX Review Report — Danh sách tiền gửi

## Tổng quan

- **Feature:** Danh sách tiền gửi
- **Product:** Co-opBank Mobile Banking
- **Domain:** Banking
- **Screens:** 1
- **Tổng check:** 20
- **Pass:** 8 | Gap: 11 | Unverifiable: 1
- **UX Score:** 40% (Simple) · 65% (Weighted)

---


**Total checks:** 20  
**Pass:** 8 | **Gap:** 11 | **Unverifiable:** 1  
**Simple Score:** 40%  
**Weighted Score:** 40%## Đề xuất cải tiến (Priority)

### Critical

- **[UXP-001]** Screen: `SCR-DSG-001` | **Empty state CTA sai pattern** — DDL `empty-state-1` yêu cầu CTA button chuẩn. Design dùng tooltip trôi nổi (không dismissable rõ ràng, không đủ touch target).
- **[UXP-002]** Screen: `SCR-DSG-001` | **Empty state thiếu illustration/icon** — DDL `empty-state-1` spec yêu cầu icon/illustration. Design chỉ có text body.

### Major

- **[UXP-003]** Screen: `SCR-DSG-001` | **Filter chip touch target thiếu** — Chips cao est. 28px < 44px minimum (Fitts's Law). Khó tap chính xác trên mobile.
- **[UXP-004]** Screen: `SCR-DSG-001` | **FAB thiếu ARIA label** — Icon "+" không có accessible name. Screen reader đọc là "button" không rõ mục đích.
- **[UXP-005]** Screen: `SCR-DSG-001` | **Filter icon header thiếu ARIA label** — Icon-only button không có accessible name (UXG-183).
- **[UXP-006]** Screen: `SCR-DSG-001` | **Loading/skeleton state thiếu** — Không có artboard skeleton loading khi đang tải danh sách.

### Minor

- **[UXP-007]** Screen: `SCR-DSG-001` | **Account number format thiếu grouping** — "12300123123000" (14 ký tự liên tiếp) khó đọc/so sánh. Nên dùng dấu chấm ngăn cách.
- **[UXP-008]** Screen: `SCR-DSG-001` | **Typo "Số số"** — Label "Số số: 1231233213" cần sửa thành "Số sổ" (serial number).
- **[UXP-009]** Screen: `SCR-DSG-001` | **Date field inconsistency** — Tiền gửi tích lũy có 2 ngày (tích lũy tiếp theo + đáo hạn); thường chỉ có 1 ngày (đến hạn) → gây confusion về schema thống nhất.
- **[UXP-010]** Screen: `SCR-DSG-001` | **Filter chip overflow indicator thiếu** — Không rõ chips có thể scroll ngang; thiếu fade/shadow hint.
- **[UXP-011]** Screen: `SCR-DSG-001` | **Account number masking** — Số TK hiển thị đầy đủ — cần xem xét chính sách partial masking (banking security policy).
- **[UXP-012]** Screen: `SCR-DSG-001` | **Balance label alignment mismatch** — "Số dư gốc hiện tại" label + value right-aligned khác với phần trên left-aligned; inconsistent reading pattern.

---

## Chi tiết theo màn hình

### 1. Danh sách tiền gửi › Danh sách

> `SCR-DSG-001` · list · 3 artboards (loaded-2cards, loaded-1card, empty-state)

**Score: 40% | Pass: 8 | Gap: 11 | Unverifiable: 1**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | FAB touch target ≥ 44px | Fitts's Law | — | Pass | Từ ảnh: FAB circle est. 44px, tại bottom-right cố định |
| 2 | Card tap target đủ lớn | Fitts's Law | — | Pass | Từ ảnh: Cards full-width 343px, height ~150-174px |
| 3 | Filter chip touch target ≥ 44px | Fitts's Law | — | Gap | Từ ảnh: chips cao est. 28px < 44px minimum touch target |
| 4 | Filter chips ≤ 7 options | Hick's Law | — | Pass | 3 chips (Tất cả / Thường / Tích lũy) — dưới ngưỡng 7 |
| 5 | Empty state CTA pattern | DDL comp | COMP:empty-state-1 | Gap | DDL cần button chuẩn. Từ ảnh 1603: tooltip trôi nổi gần FAB |
| 6 | Empty state illustration | DDL comp | COMP:empty-state-1 | Gap | DDL cần icon/illustration. Từ ảnh 1603: chỉ text body |
| 7 | FAB ARIA label | UXG-183 | UXG-183 | Gap | FAB "+" icon-only thiếu accessible name="Mở tiền gửi mới" |
| 8 | Filter icon ARIA label | UXG-183 | UXG-183 | Gap | Filter funnel icon-only, thiếu aria-label |
| 9 | Color not sole conveyor (status) | UXG-180 | UXG-180 | Pass | Từ ảnh: "Tạm dừng tích lũy" dùng cả text đỏ + label — hai kênh |
| 10 | Header contrast (WCAG AA) | WCAG AA | — | Pass | Từ ảnh: white text on #1E3A8A header, est. 8.5:1 — PASS |
| 11 | Status badge contrast | WCAG AA | — | Pass | Từ ảnh: "Tạm dừng tích lũy" đỏ on white card, est. 4.8:1 — PASS |
| 12 | Summary balance display | Vision | — | Pass | Từ ảnh: "Tổng số dư gốc / 10,000,000 VND" rõ ràng, bold |
| 13 | Loading / skeleton state | Vision | — | Gap | Không có artboard loading state — banking NFR thiếu |
| 14 | Account number readability | Vision | — | Gap | Từ ảnh: "12300123123000" 14 chars không grouping, khó đọc |
| 15 | Typo content | Vision | — | Gap | Từ ảnh 1602: "Số số: 1231233213" — lỗi đánh máy "Số sổ" |
| 16 | Date field consistency | Vision | — | Gap | Tích lũy: 2 ngày; Thường: 1 ngày — schema không nhất quán |
| 17 | App header completeness | DDL comp | COMP:app-header-1 | Pass | Từ ảnh: back chevron + title "Danh sách tiền gửi" + filter icon |
| 18 | Filter chip scroll indicator | Vision | — | Gap | Chips 3 items trên 375px — thiếu fade hint cho scroll ngang |
| 19 | Account number masking | Product | — | Unverifiable | Policy không rõ — 12300123123000 full display; cần banking security review |
| 20 | Balance alignment consistency | Vision | — | Gap | "Số dư gốc hiện tại" right-align vs summary row left-align — inconsistent |

---

## DDL References

| Ref | Type | Used At |
|-----|------|---------|
| COMP:empty-state-1 | Component | SCR-DSG-001 |
| COMP:app-header-1 | Component | SCR-DSG-001 |
| COMP:bottom-tab-bar-1 | Component | SCR-DSG-001 |
| UXG-183 | Guideline | SCR-DSG-001 |
| UXG-180 | Guideline | SCR-DSG-001 |
