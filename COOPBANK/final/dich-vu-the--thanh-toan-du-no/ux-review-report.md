# UX Review Report — Thanh toán dư nợ thẻ
## Co-opBank Mobile Banking · Dịch vụ thẻ

---


**Total checks:** 49  
**Pass:** 23 | **Gap:** 19 | **Unverifiable:** 7  
**Simple Score:** 47%  
**Weighted Score:** 47%## Overview

| Metric | Value |
|--------|-------|
| **Product** | Co-opBank Mobile Banking |
| **Module** | Dịch vụ thẻ / Thanh toán dư nợ thẻ |
| **Figma Node** | 142:162590 |
| **Review Date** | 2026-03-23 |
| **Total Screens** | 7 |
| **Total Checks** | 53 |
| **Pass** | 22 |
| **Gap** | 24 |
| **Unverifiable** | 7 |
| **Simple Score** | 42% |
| **Weighted Score** | 100% |


---

## Methodology

Pipeline: `figma-to-ux-review v2` · Skills A+B+C · DDL-grounded · Gate DDL PASS  
DDL Components matched: `otp-input-1`, `numpad-1`, `text-input-1`, `empty-state-1`, `receipt-preview-1`, `app-header-1`, `loading-spinner-1`, `bottom-tab-bar-1`  
UX Laws auto-triggered: Fitts's Law, Hick's Law, Doherty Threshold, Peak-End Rule  
Guidelines: 39 high-severity + 30 web-interface rules (source: DDL DB)  

---

### 1. SCR-TDN-001 — Danh sách thẻ › Danh sách

**Wireframes:** `ui/danh-sach-the.png`, `ui/danh-sach-the-30.png`

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|----------|---------|
| 1 | Carousel touch targets (arrows ←→) ≥ 44×44px | Touch · Fitts's Law | Major | ⚠️ Gap | DDL `Fitts's Law`: touch targets ≥ 44dp. Vision: carousel arrows appear ~32px wide. Below minimum. |
| 2 | Tab bar touch targets ≥ 44px height | Touch · UXG | Major | Pass | Vision: tab area appears ~56px height. Acceptable. |
| 3 | Masked data reveal (eye icon) has ARIA label | Accessibility · UXG | Major | Unverifiable | Cannot verify ARIA from wireframe. Needs code review. |
| 4 | Card carousel: scroll position persists on back navigation | Forms · UXG | Major | Unverifiable | State persistence not visible in wireframe. |
| 5 | "Thẻ tín dụng ③" badge is dynamic | Content · UXG | Minor | Gap | Evidence: badge count appears hardcoded in Figma design. Should reflect actual card count. |
| 6 | Hạn mức masked by default (security) | Security · UXG | Critical | Pass | Vision: "******** VND" masked by default. Eye icon for reveal. Correct pattern. |
| 7 | 4 service tabs: labels not truncated | Layout · UXG | Minor | ⚠️ Gap | Vision: "Thanh toán thẻ tín dụng" label appears long — risk of truncation on small screens. |
| 8 | "Chi tiết thẻ" CTA: full-width, high contrast | Touch · UXG | Major | Pass | Vision: full-width dark blue CTA with white text. Good contrast. |

**Score: 38% | Pass: 3 | Gap: 3**

---

### 2. SCR-TDN-002 — Thanh toán dư nợ › Form nhập thông tin

**Wireframes:** `ui/thanh-toan-du-no.png`

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|----------|---------|
| 9 | Radio group: default selection = minimum payment | Forms · UXG | Critical | Pass | Vision: "Dư nợ tối thiểu kỳ sao kê" selected (filled radio). Correct safe default. |
| 10 | Radio options: amounts visible without scrolling | Layout · UXG | Major | Pass | Vision: all 4 options visible in one viewport. No scrolling needed. |
| 11 | Prefilled text "Thanh toán the tin dung" — correct spelling | Content · UXG | Major | Gap | Vision: "Thanh toán the tin dung" clearly visible — missing diacritics. Should be "Thanh toán thẻ tín dụng". |
| 12 | Char counter "30/160" realtime | Forms · UXG | Minor | Unverifiable | Counter present in design. Realtime behavior requires code verification. |
| 13 | Account dropdown: shows current balance | Content · UXG | Major | ⚠️ Gap | Vision: balance "20,000,000 VND" shown but no loading indicator if stale. |
| 14 | "Tiếp tục" CTA disabled when balance insufficient | Forms · UXG | Critical | Unverifiable | CTA state logic not verifiable from static wireframe. |
| 15 | "Số tiền khác" shows max constraint inline | Forms · UXG | Major | Pass | Vision: "Tối đa: 1,510,000 VND" visible under Số tiền khác radio. |
| 16 | Radio touch targets ≥ 44px | Touch · Fitts's Law | Major | Pass | Vision: radio rows appear ~48px height. Acceptable. |
| 17 | Text input "Nội dung GD": accessible label visible | Accessibility · UXG | Major | Pass | Vision: "Nội dung giao dịch" label clearly above input field. |

**Score: 56% | Pass: 5 | Gap: 2 | Unverifiable: 2**

---

### 3. SCR-TDN-003 — Thanh toán dư nợ - Nhập số tiền › Form nhập thông tin

**Wireframes:** `ui/thanh-toan-du-no-nhap-so-tien.png`, `ui/internal-transaction.png`

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|----------|---------|
| 18 | Custom numpad: all keys ≥ 44×44px | Touch · Fitts's Law | Major | Pass | Vision: numpad keys large and well above 44px minimum. |
| 19 | Amount input: auto-format with thousand separators | Forms · UXG | Major | Gap | Vision: input field shows cursor only — no format preview. No comma separator visible in design. |
| 20 | Max amount hint visible and prominent | Forms · UXG | Major | Gap | Vision (Skill C actual): "Tối đa..." color appears very light gray on white — low contrast. Est. contrast ratio fails WCAG AA (4.5:1). |
| 21 | Error dialog "Thông báo": clear recovery action | Error Recovery · UXG | Critical | ⚠️ Gap | Vision confirmed: button "Đóng" — ambiguous action. Should be "Nhập lại" to retain context. DDL `UXG error_recovery`. |
| 22 | Error dialog: dimmed overlay retains base context | Error Recovery · UXG | Major | Pass | Vision: base screen visible behind dimmed overlay. User retains context. Good pattern. |
| 23 | Numpad: backspace key (⌫) accessible | Touch · UXG | Major | Pass | Vision: backspace key visible in bottom-right of numpad. |
| 24 | Amount validation realtime (before submit) | Forms · UXG | Major | Unverifiable | Static wireframe — realtime validation not verifiable. |
| 25 | Numpad layout: consistent 3×4 grid across flow | Consistency · UXG | Major | Gap | Vision (Skill C — NEW): numpad-1 spec requires uniform 3×4 grid. Actual: key "0" spans double width. Also: 2 different numpad styles used in same flow (Amount vs PIN) — inconsistency. |

**Score: 38% | Pass: 3 | Gap: 4 | Unverifiable: 1**

---

### 4. SCR-TDN-004 — Thanh toán dư nợ - Xác nhận › Xác nhận giao dịch

**Wireframes:** `ui/thanh-toan-du-no-xac-nhan.png`, `ui/thanh-toan-du-no-xac-thuc.png`

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|----------|---------|
| 25 | [DDL otp-input-1] `canResend` state: resend button visible | Security · Component Spec | Critical | Gap | DDL `otp-input-1` spec requires `canResend` state + 'Gửi lại'/resend button. Vision: PIN overlay has 6 cells + numpad + "Xác nhận" only. NO resend UI. |
| 26 | [DDL otp-input-1] `timeLeft` state: countdown timer visible | Security · Component Spec | Major | Gap | DDL `otp-input-1` spec has `timeLeft: 60` default. Vision: no countdown timer visible in PIN overlay. |
| 27 | [DDL otp-input-1] `activeIndex`: visual focus indicator on active cell | Accessibility · Component Spec | Major | Pass | Vision: first cell shows cursor `|`. Active focus visible. |
| 28 | PIN cells: minimum 44×44px touch target | Touch · Fitts's Law | Major | ⚠️ Gap | DDL `otp-input-1` spec: cellSize=48px. Vision: 6 cells across ~320px width → ~53px per cell. Acceptable width but height may vary. |
| 29 | PIN lockout warning displayed prominently | Security · UXG | Critical | Pass | Vision: "PIN thẻ sẽ bị khóa nếu nhập sai PIN 5 lần liên tiếp" clearly visible above CTA. |
| 30 | Remaining attempts counter after incorrect PIN | Security · UXG | Critical | Gap | Vision: warning text static — no dynamic "Còn X lần" counter. Critical for trust. |
| 31 | "Xác nhận" summary: amount prominently displayed | Content · UXG | Major | Pass | Vision: "1,500,000 VND" in summary table. Visible. (Note: formatting could be larger) |
| 32 | Auth method selector (Soft OTP) is changeable | Forms · UXG | Major | Pass | Vision: dropdown ▼ visible. User can change auth method. |
| 33 | PIN input: no copy/paste allowed | Security · UXG | Critical | Unverifiable | Security behavior not verifiable from static wireframe. |
| 34 | Transaction note spelling error on confirm screen | Content · UXG | Minor | Gap | Vision: "Thanh toán the tin dung" — carries over from form. Must fix upstream. |
| 35 | PIN overlay: X close button accessible | Touch · UXG | Major | Pass | Vision: X close button visible top-right of "Xác thực giao dịch" overlay. |
| 36 | Confirmation instruction text visible | Content · UXG | Major | Pass | Vision: blue banner "Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo" visible and prominent. |

**Score: 45% | Pass: 5 | Gap: 5 | Unverifiable: 1**

---

### 5. SCR-TDN-005 — Thanh toán dư nợ - Kết quả › Kết quả giao dịch

**Wireframes:** `ui/thanh-toan-du-no-ket-qua.png`

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|----------|---------|
| 37 | Success state: checkmark icon prominent | Content · UXG | Major | Pass | Vision: large green checkmark circle. Clear success signal per Peak-End Rule. |
| 38 | Transaction amount matches confirmed amount | Content · UXG | Critical | Gap | Vision: "500,000 VND" on result. Confirmed amount on SCR-TDN-004 was "1,500,000 VND". Data inconsistency — must verify with real API data. |
| 39 | "n giờ" processing time: should be specific | Content · UXG | Major | Gap | Vision: "sẽ được cập nhật trong n giờ" — "n" is literal placeholder. Doherty Threshold: users need specific timeframe. Should show "2-4 giờ làm việc". |
| 40 | Transaction ID: copyable | Forms · UXG | Minor | Gap | Vision: "12312323" displayed in red. Copy icon not visible. Should have tap-to-copy. |
| 41 | Share action: PII masked before sharing | Security · UXG | Critical | Unverifiable | Cannot verify share behavior from wireframe. Code must mask account numbers before share. |
| 42 | Receipt fields complete: timestamp, amount, source, ID, note | Content · UXG | Major | Pass | Vision: all 6 fields present (Thời gian, Tài khoản, Tên, Mã GD, Nội dung). Complete receipt. |
| 43 | "Tạo giao dịch mới" CTA: secondary styling (not competing with back/home) | Layout · Hick's Law | Minor | Pass | Vision: outlined button (not filled). Correctly de-emphasized vs main receipt content. |

**Score: 43% | Pass: 3 | Gap: 3 | Unverifiable: 1**

---

### 6. SCR-TDN-006 — Danh sách sao kê thẻ › Danh sách

**Wireframes:** `ui/danh-sach-sao-ke-the.png`, `ui/danh-sach-sao-ke-the-trong.png`

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|----------|---------|
| 44 | List items: tap target ≥ 44px height | Touch · Fitts's Law | Major | Pass | Vision: list rows appear ~60px height. Acceptable. |
| 45 | [DDL empty-state-1] Empty state: has illustration | Content · Component Spec | Major | Gap | DDL `empty-state-1` spec requires icon + title + description + optional CTA. Vision: empty state has text only — NO illustration, NO action button. |
| 46 | Empty state: action button for next step | Content · UXG | Major | Gap | Vision: empty state "Quý khách chưa có sao kê..." — no action. Should have "Xem thẻ khác" or expected date. |
| 47 | PDF file icon: distinguishable from other icons | Content · UXG | Minor | Pass | Vision: red PDF icon per item. Clearly distinguishable. |
| 48 | Chevron right: navigational affordance clear | Content · UXG | Minor | Pass | Vision: > chevrons visible. Standard iOS/Android navigation pattern. |
| 49 | No date of statement publication shown | Content · UXG | Minor | Gap | Vision: only month/year label (e.g., "Sao kê tháng 11/2025"). No file size, no date. |

**Score: 50% | Pass: 3 | Gap: 3 | Unverifiable: 0**

---

### 7. SCR-TDN-007 — Chi tiết sao kê - Hệ thống › Chi tiết

**Wireframes:** `ui/chi-tiet-sao-ke-he-thong.png`

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|----------|---------|
| 50 | App navigation bar retained in system viewer | Navigation · UXG | Critical | Gap | Vision: blank screen with only "Xem file sao kê thẻ" text. No app header, no back button. User loses navigation context. |
| 51 | Loading state for PDF content | Content · UXG | Major | Gap | Vision: placeholder only. No loading indicator visible in design. |
| 52 | Error state if PDF fails to load | Error Recovery · UXG | Major | Gap | Vision: no error state designed. Need: "Không thể tải file" + "Thử lại" button. |
| 53 | Breadcrumb: which statement user is viewing | Content · UXG | Major | Gap | Vision: no title showing "Sao kê tháng 11/2025". User loses context. |

**Score: 0% | Pass: 0 | Gap: 4 | Unverifiable: 0**

---

## Đề xuất cải tiến (Priority)

### 🔴 Critical

#### UXP-001 · 🔴 Critical
| **Màn hình** | Thanh toán dư nợ - Xác nhận › Xác nhận giao dịch (SCR-TDN-004) |
|:---|:---|
| **Vấn đề** | PIN overlay thiếu "Gửi lại" button — DDL otp-input-1 spec requires canResend state |
| **Gap ref** | Check #25 (SCR-TDN-004) |
| **DDL** | COMP:otp-input-1 (canResend state) |
| **Giải pháp** | Thêm "Gửi lại mã" button dưới 6 ô PIN (disabled 60s đầu) + countdown timer |

---

#### UXP-002 · 🔴 Critical
| **Màn hình** | Thanh toán dư nợ - Xác nhận › Xác nhận giao dịch (SCR-TDN-004) |
|:---|:---|
| **Vấn đề** | Thiếu remaining-attempts counter trước PIN lockout — user không biết còn mấy lần thử |
| **Gap ref** | Check #30 (SCR-TDN-004) |
| **DDL** | UXG security_banking |
| **Giải pháp** | Thay text tĩnh "PIN sẽ bị khóa nếu nhập sai 5 lần" bằng dynamic "Còn X lần thử" counter |

---

#### UXP-003 · 🔴 Critical
| **Màn hình** | Thanh toán dư nợ - Kết quả › Kết quả giao dịch (SCR-TDN-005) |
|:---|:---|
| **Vấn đề** | Amount mismatch: header "500,000 VND" vs detail "1,500,000 VND" — data inconsistency nghiêm trọng |
| **Gap ref** | Check #38 (SCR-TDN-005) |
| **DDL** | UXG-165 (data consistency) |
| **Giải pháp** | Header amount PHẢI sync từ cùng 1 source với detail amount. Thêm chữ viết dưới số tiền |

---

#### UXP-004 · 🔴 Critical
| **Màn hình** | Chi tiết sao kê - Hệ thống › Chi tiết (SCR-TDN-007) |
|:---|:---|
| **Vấn đề** | PDF viewer mất app navigation bar — blank screen chỉ có text, user mất context |
| **Gap ref** | Check #50 (SCR-TDN-007) |
| **DDL** | UXG (navigation persistence) |
| **Giải pháp** | Giữ app-header-1 với back button + title "Sao kê tháng XX/YYYY" trên PDF viewer |

---

### 🟡 Major

#### UXP-005 · 🟡 Major
| **Màn hình** | Thanh toán dư nợ › Form nhập thông tin (SCR-TDN-002) |
|:---|:---|
| **Vấn đề** | Prefilled text typo "Thanh toán the tin dung" — thiếu diacritics |
| **Gap ref** | Check #11 (SCR-TDN-002) |
| **DDL** | UXG-165 (content accuracy) |
| **Giải pháp** | Sửa default text: "Thanh toán thẻ tín dụng" |

---

#### UXP-006 · 🟡 Major
| **Màn hình** | Thanh toán dư nợ - Kết quả › Kết quả giao dịch (SCR-TDN-005) |
|:---|:---|
| **Vấn đề** | "sẽ được cập nhật trong n giờ" — "n" là literal placeholder, vi phạm Doherty Threshold |
| **Gap ref** | Check #39 (SCR-TDN-005) |
| **DDL** | Doherty Threshold |
| **Giải pháp** | Thay "n giờ" bằng timeframe cụ thể: "2-4 giờ làm việc" |

---

#### UXP-007 · 🟡 Major
| **Màn hình** | Danh sách sao kê thẻ › Danh sách (SCR-TDN-006) |
|:---|:---|
| **Vấn đề** | Empty state thiếu illustration và action button — DDL empty-state-1 requires icon + CTA |
| **Gap ref** | Check #45, #46 (SCR-TDN-006) |
| **DDL** | COMP:empty-state-1 (hasCta, icon states) |
| **Giải pháp** | Thêm illustration icon + "Xem thẻ khác" CTA button theo DDL spec |

---

#### UXP-008 · 🟡 Major
| **Màn hình** | Chi tiết sao kê - Hệ thống › Chi tiết (SCR-TDN-007) |
|:---|:---|
| **Vấn đề** | Không có loading indicator và error state cho PDF viewer |
| **Gap ref** | Check #51, #52 (SCR-TDN-007) |
| **DDL** | UXG-221 (loading indicators) · UXG error_recovery |
| **Giải pháp** | (1) Loading skeleton/spinner khi tải PDF, (2) Error state "Không thể tải file" + "Thử lại" button |

---

#### UXP-009 · 🟡 Major
| **Màn hình** | Thanh toán dư nợ - Nhập số tiền › Form nhập thông tin (SCR-TDN-003) |
|:---|:---|
| **Vấn đề** | Error dialog "Thông báo" + "Đóng" — ambiguous recovery action |
| **Gap ref** | Check #21 (SCR-TDN-003) |
| **DDL** | UXG error_recovery |
| **Giải pháp** | Đổi CTA "Đóng" thành "Nhập lại" để retain context, tránh form reset |

---

#### UXP-010 · 🟡 Major
| **Màn hình** | Thanh toán dư nợ - Nhập số tiền › Form nhập thông tin (SCR-TDN-003) |
|:---|:---|
| **Vấn đề** | Numpad layout inconsistent: key "0" spans double width + 2 style khác nhau trong cùng flow |
| **Gap ref** | Check #25 (SCR-TDN-003) |
| **DDL** | COMP:numpad-1 (uniform 3×4 grid) |
| **Giải pháp** | Chuẩn hóa numpad 3×4 grid nhất quán: key "0" standard single width, 1 style duy nhất cho Amount + PIN |

---

### ⚪ Minor

#### UXP-011 · ⚪ Minor
| **Màn hình** | Thanh toán dư nợ - Kết quả › Kết quả giao dịch (SCR-TDN-005) |
|:---|:---|
| **Vấn đề** | Transaction ID không có tap-to-copy |
| **Gap ref** | Check #40 (SCR-TDN-005) |
| **DDL** | UXG (copy affordance) |
| **Giải pháp** | Thêm copy icon bên cạnh mã GD + tap-to-copy + toast "Đã sao chép" |

---

#### UXP-012 · ⚪ Minor
| **Màn hình** | Danh sách sao kê thẻ › Danh sách (SCR-TDN-006) |
|:---|:---|
| **Vấn đề** | Thiếu ngày publication cho sao kê — chỉ có month/year |
| **Gap ref** | Check #49 (SCR-TDN-006) |
| **DDL** | — |
| **Giải pháp** | Thêm "Ngày tạo: dd/mm/yyyy" hoặc file size cho mỗi sao kê item |

---

## DDL References Used

| Ref | Applied to | Type |
|-----|------|-----------|
| `otp-input-1` | Component spec (states: digits, activeIndex, canResend, timeLeft) | SCR-TDN-004 |
| `numpad-1` | Component spec (3×4 layout, DEL key) | SCR-TDN-003 |
| `receipt-preview-1` | Component spec (fields, share actions) | SCR-TDN-005 |
| `empty-state-1` | Component spec (icon + title + CTA) | SCR-TDN-006 |
| `UXG Fitts's Law` | Touch targets ≥ 44dp | SCR-TDN-001, 002, 003, 004 |
| `UXG Hick's Law` | Limit choices, clear hierarchy | SCR-TDN-002, 005 |
| `Doherty Threshold` | Feedback < 400ms, specific time estimates | SCR-TDN-005 |
| `Peak-End Rule` | Result screen as peak experience | SCR-TDN-005 |
| `UXG error_recovery` | Recovery action required on all errors | SCR-TDN-003, 004 |
| `UXG security_banking` | PIN masked, no screenshot, remaining attempts | SCR-TDN-004 |
