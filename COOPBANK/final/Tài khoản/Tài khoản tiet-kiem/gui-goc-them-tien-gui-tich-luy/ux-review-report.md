# UX Review Report — Gửi gốc thêm tiền gửi tích luỹ

## Tổng quan

- **Feature:** Gửi gốc thêm tiền gửi tích luỹ
- **Product:** Co-opBank Mobile Banking
- **Domain:** Banking
- **Screens:** 6
- **Tổng check:** 48
- **Pass:** 30 | Gap: 18 | Unverifiable: 0
- **UX Score:** 63%

---


**Total checks:** 44  
**Pass:** 26 | **Gap:** 18 | **Unverifiable:** 0  
**Simple Score:** 59%  
**Weighted Score:** 59%## Đề xuất cải tiến (Priority)

### Critical

- **[UXP-001]** Screen: `SCR-GG-003` | **Input validation error state thiếu** — DDL `text-input-1` yêu cầu error state. Design chỉ có helper text.
- **[UXP-002]** Screen: `SCR-GG-004` | **OTP resend flow thiếu** — DDL `otp-input-1` yêu cầu canResend + countdown. Design: 6 static cells, KHÔNG có resend UI.

### Major

- **[UXP-003]** Screen: `SCR-GG-001` | **Error popup không actionable** — Popup chỉ có "Đóng", thiếu hướng dẫn tạo TK.
- **[UXP-004]** Screen: `SCR-GG-002` | **Empty state thiếu** — Không có variant khi danh sách rỗng.
- **[UXP-005]** Screen: `SCR-GG-002` | **Loading state thiếu** — Banking app cần loading indicator.
- **[UXP-006]** Screen: `SCR-GG-003` | **Quick amount selection thiếu** — Nên có preset amount buttons.
- **[UXP-007]** Screen: `SCR-GG-003` | **Security indicator thiếu** — Form giao dịch tiền cần security badge.
- **[UXP-008]** Screen: `SCR-GG-004` | **Edit capability trước confirm thiếu** — Chỉ có back arrow.
- **[UXP-009]** Screen: `SCR-GG-005` | **Receipt chi tiết thiếu** — Chỉ 4 fields, thiếu kỳ hạn, loại SP.
- **[UXP-010]** Screen: `SCR-GG-006` | **Information grouping thiếu** — 15+ fields không có section dividers.

### Minor

- **[UXP-011]** Screen: `SCR-GG-001` | **Keyboard navigation** — Không verify được từ static screenshot.
- **[UXP-012]** Screen: `SCR-GG-002` | **Scroll indicator thiếu** — 3 cards nhưng không có scroll hint.
- **[UXP-013]** Screen: `SCR-GG-003` | **ARIA labels thiếu** — Dropdown không có ARIA label visible.
- **[UXP-014]** Screen: `SCR-GG-004` | **OTP auto-focus** — Không verify được từ static design.
- **[UXP-015]** Screen: `SCR-GG-006` | **Scrollable content indicator** — Content > viewport, không có scroll hint.
- **[UXP-016]** Screen: `SCR-GG-006` | **PII data masking** — Tên + STK hiện full, thiếu option ẩn/hiện.
- **[UXP-017]** Screen: `SCR-GG-006` | **Copy account number** — Không có copy icon cạnh STK.
- **[UXP-018]** Screen: `SCR-GG-006` | **Data freshness indicator** — Không có "Last updated" hay refresh.

---

## Chi tiết theo màn hình

### 1. Menu tiền gửi tiết kiệm › Danh mục chức năng

> `SCR-GG-001` · menu · 2 artboards

**Score: 71% | Pass: 5 | Gap: 2**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | Touch target ≥ 44px | Fitts's Law | — | Pass | Từ ảnh: 5 menu icons ~60x60px, spacing hợp lý |
| 2 | Menu items ≤ 7 | Hick's Law | — | Pass | 5 items — dưới ngưỡng 7 |
| 3 | Error popup actionable | UXG-235 | UXG-235 | Gap | Từ ảnh 1207: Chỉ "Đóng", thiếu hướng dẫn tạo TK |
| 4 | Error popup contrast | WCAG AA | — | Pass | Từ ảnh: Text đen/nền trắng, >7:1 |
| 5 | Nav consistency | DDL comp | COMP:app-header-1 | Pass | Back + title có đủ |
| 6 | Icon labels rõ ràng | Vision | — | Pass | Mỗi icon có text label |
| 7 | Keyboard navigation | UXG-184 | UXG-184 | Gap | Không verify được từ static screenshot |

### 2. Gửi gốc thêm tiền gửi tích luỹ › Danh sách tài khoản

> `SCR-GG-002` · list · 1 artboard

**Score: 57% | Pass: 4 | Gap: 3**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | Card tap target ≥ 44px | Fitts's Law | — | Pass | Từ ảnh: Cards cao ~100px, full width |
| 2 | Tổng dư gốc nổi bật | Hick's Law | — | Pass | "25,000,000 VND" bold blue |
| 3 | Empty state khi 0 TK | DDL comp | COMP:empty-state-1 | Gap | Không có artboard empty state |
| 4 | Loading state | Vision | — | Gap | Không có loading artboard |
| 5 | Filter clarity | Vision | — | Pass | Filter icon ở header right |
| 6 | Card visual distinction | Vision | — | Pass | Piggy + STK + ngày + dư |
| 7 | Scroll indicator | Vision | — | Gap | 3 cards, thiếu scroll/pull-to-refresh hint |

### 3. Gửi gốc thêm tiền gửi tích luỹ › Form nhập thông tin

> `SCR-GG-003` · form · 1 artboard

**Score: 50% | Pass: 4 | Gap: 4**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | Input validation error state | DDL comp | COMP:text-input-1 | Gap | DDL cần error state. Từ ảnh: chỉ helper text |
| 2 | CTA touch target | Fitts's Law | — | Pass | Full-width button ~48px |
| 3 | Form labels alignment | Vision | — | Pass | Label-value pairs aligned |
| 4 | Quick amount buttons | DDL comp | COMP:numpad-1 | Gap | Không có preset amount selection |
| 5 | Dropdown accessible | UXG-183 | UXG-183 | Gap | Không có ARIA label visible |
| 6 | Note banner visibility | Vision | — | Pass | Teal banner cuối form nổi bật |
| 7 | Read-only vs editable | Vision | — | Pass | 2 sections phân biệt rõ |
| 8 | Security indicator | Product | — | Gap | Form giao dịch tiền thiếu security badge |

### 4. Gửi gốc thêm tiền gửi tích luỹ › Xác nhận giao dịch

> `SCR-GG-004` · confirm · 2 artboards

**Score: 63% | Pass: 5 | Gap: 3**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | OTP resend + countdown | DDL comp | COMP:otp-input-1 | Gap | DDL cần canResend + Gửi lại. Từ ảnh: 6 cells, KHÔNG có resend |
| 2 | Amount số + chữ | Vision | — | Pass | "20M VND" + "Hai mươi triệu đồng" |
| 3 | Confirmation completeness | Vision | — | Pass | 8 fields review đầy đủ |
| 4 | OTP warning visibility | Vision | — | Pass | Warning khoá sau 5 lần sai rõ ràng |
| 5 | Close OTP sheet | Vision | — | Pass | × icon top-right |
| 6 | Edit before confirm | Product | — | Gap | Chỉ back arrow, thiếu "Sửa" link |
| 7 | Auth method selection | Vision | — | Pass | Dropdown Soft OTP |
| 8 | OTP auto-focus | DDL comp | COMP:otp-input-1 | Gap | Không verify được từ static design |

### 5. Gửi gốc thêm tiền gửi tích luỹ › Kết quả giao dịch

> `SCR-GG-005` · result · 1 artboard

**Score: 86% | Pass: 6 | Gap: 1**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | Success state clear | Peak-End | — | Pass | Green checkmark + "thành công" + amount |
| 2 | Receipt completeness | DDL comp | COMP:receipt-preview-1 | Gap | Chỉ 4 fields, thiếu kỳ hạn, loại SP |
| 3 | Share/Save actions | Vision | — | Pass | "Chia sẻ" + "Lưu ảnh" |
| 4 | Navigation after success | Vision | — | Pass | 2 CTA paths |
| 5 | Transaction code visible | Vision | — | Pass | Mã GD: 0982312 |
| 6 | No back button | Product | — | Pass | Home only, prevent re-submit |
| 7 | Timestamp format | Vision | — | Pass | dd/MM/yyyy HH:mm |

### 6. Chi tiết tài khoản tiết kiệm › Chi tiết

> `SCR-GG-006` · detail · 1 artboard

**Score: 29% | Pass: 2 | Gap: 5**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | Scrollable indicator | Vision | — | Gap | Content 1039px > viewport, no scroll hint |
| 2 | Bottom tab bar | DDL comp | COMP:bottom-tab-bar-1 | Pass | 4 tabs icons + labels |
| 3 | Information grouping | Hick's Law | — | Gap | 15+ fields liệt kê liên tục, no sections |
| 4 | PII data masking | Product | — | Gap | Tên + STK hiện full |
| 5 | Tab actions accessible | Fitts's Law | — | Pass | Bottom tabs đủ lớn |
| 6 | Copy account number | Vision | — | Gap | Không có copy icon cạnh STK |
| 7 | Data freshness indicator | Vision | — | Gap | Không có Last updated/refresh |

---

## DDL References

| Ref | Type | Used At |
|-----|------|---------|
| COMP:app-header-1 | Component | SCR-GG-001 |
| COMP:empty-state-1 | Component | SCR-GG-002 |
| COMP:text-input-1 | Component | SCR-GG-003 |
| COMP:numpad-1 | Component | SCR-GG-003 |
| COMP:otp-input-1 | Component | SCR-GG-004 |
| COMP:receipt-preview-1 | Component | SCR-GG-005 |
| COMP:bottom-tab-bar-1 | Component | SCR-GG-006 |
| UXG-235 | Guideline | SCR-GG-001 |
| UXG-183 | Guideline | SCR-GG-003 |
| UXG-184 | Guideline | SCR-GG-001 |
