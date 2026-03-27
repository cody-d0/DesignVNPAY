# UX Review Report — Kích hoạt thẻ | Co-opBank Mobile Banking

**Product:** Co-opBank Mobile Banking  
**Section:** Dịch vụ thẻ / Kích hoạt thẻ  
**Figma:** `aYeSAVi94QlI4i4rL3xtmR` node `142:150749`  
**Generated:** 2026-03-23  
**Domain:** Banking  
**Screens reviewed:** 3  
**Total checks:** 26  
**Pass:** 12 | **Gap:** 14 | **Unverifiable:** 0  
**Simple Score:** 46%  
**Weighted Score:** 46%**Pass:** 0 | **Gap:** 0 | **Unverifiable:** 0  
**Simple Score:** 0%  
**Weighted Score:** 0%

> ⚠️ Overview counters replaced by ux-score-calculator.js after scoring.

---

## Methodology

Pipeline: Figma → OCR (2 rounds) → Boundary Detection (overlay-detect 7-signal) → DDL Prefetch → Skills A+B+C.

| Layer | Source | Coverage |
|:---|:---|:---|
| Skill A | DDL component specs (`otp-input-1`, `text-input-1`, `numpad-1`, `app-header-1`) | 3 screens |
| Skill B | 69 guidelines + banking product context | All screens |
| Skill C | Agent Vision (14 screenshots reviewed incl. rerun case-loi-4..10) | All screens |
| DDL Laws | Fitts, Hick, Zeigarnik, Peak-End (auto-triggered) | All screens |

---

## Chi tiết theo màn hình

### 1. Kích hoạt thẻ › Form nhập thông tin (`SCR-KHT-001`)

> `SCR-KHT-001` · form · 6 artboards

**Score: 44% | Pass: 4 | Gap: 5**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:-------:|:---------|
| 1 | `text-input-1` spec: helper_text below input field | Skill A · C1 | COMP:text-input-1 | Gap | Từ ảnh kich-hoat-the-1.png: Chỉ có label trên input, thiếu helper text hướng dẫn dưới field theo spec |
| 2 | CTA button màu primary match brand token navy | Skill C · C2 | TOKEN:base.primary=#1E3A8A | Pass | Từ ảnh kich-hoat-the-1.png: Nút "Tiếp tục" màu navy blue match brand token |
| 3 | Error strategy: inline error thay vì modal interrupt | Skill B · C3 | UXG-165 | Gap | Từ ảnh kich-hoat-the-case-loi-1.png: Lỗi nhập trống dùng modal "Thông báo" + "Đóng" thay vì inline error dưới input |
| 4 | Security: mask số thẻ sau nhập | Skill B | — | Pass | Từ ảnh danh-sach-the-21.png: Số thẻ "1234 **** **** 1121" — đúng chuẩn mask |
| 5 | Progress indicator cho 3-step flow (step dots) | Skill B | COMP:step-indicator-1 | Gap | Từ ảnh kich-hoat-the-1.png: Không có progress bar / step indicator — user không biết flow gồm mấy bước |
| 6 | Keypad button touch target ≥44px (Fitts's Law) | DDL Law | fitts | Pass | Từ ảnh kich-hoat-the-1.png: Custom keypad chiếm ~50% height màn hình, buttons ≈80-100px — đạt Fitts's Law |
| 7 | CTA count ≤2 per state (Hick's Law) | DDL Law | hick | Pass | Từ ảnh: Mỗi state chỉ 1 primary CTA ("Tiếp tục" hoặc "Đóng") — đạt Hick's Law |
| 8 | Badge contrast "Chờ kích hoạt" WCAG AA (≥4.5:1) | Skill B · C2 | UXG-243 | Gap | Từ ảnh danh-sach-the-21.png: Badge màu nhạt trên nền trắng — est. contrast <4.5:1, FAIL WCAG AA |
| 9 | CTA label nhất quán ("Tiếp tục" vs "Xác nhận") | Skill B | UXG-165 | Gap | Từ ảnh: kich-hoat-the-1.png = "Tiếp tục", kich-hoat-the-2.png = "Xác nhận" — không nhất quán cùng action |

---

### 2. Kích hoạt thẻ › Xác nhận giao dịch (`SCR-KHT-002`)

> `SCR-KHT-002` · confirm · 2 artboards

**Score: 38% | Pass: 3 | Gap: 5**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:-------:|:---------|
| 10 | `otp-input-1` spec: canResend state + "Gửi lại" button | Skill A · C1 | COMP:otp-input-1 | Gap | Từ ảnh kich-hoat-the-3.png: OTP bottom sheet không có "Gửi lại" button — DDL otp-input-1 spec: canResend là mandatory state |
| 11 | `otp-input-1` spec: timeLeft countdown timer | Skill A · C1 | COMP:otp-input-1 | Gap | Từ ảnh kich-hoat-the-3.png: Text "bị khóa sau 5 lần" nhưng không có countdown timer — user không track attempts |
| 12 | `otp-input-1` spec: mask_toggle eye icon | Skill A · C1 | COMP:otp-input-1 | Gap | Từ ảnh kich-hoat-the-3.png: Không có eye icon trong OTP area — user không verify PIN trước submit |
| 13 | `numpad-1`: button size ≥80px adequate target | Skill A · C1 | COMP:numpad-1 | Pass | Từ ảnh kich-hoat-the-3.png: Phím keypad ước tính ~110×80px — đáp ứng Fitts's Law và DDL spec |
| 14 | Security: lockout warning rõ ràng với attempt counter | Skill B | UXG-243 | Gap | Từ ảnh kich-hoat-the-3.png: "Bị khóa sau 5 lần liên tiếp" nhưng thiếu attempt counter ("Còn X lần") — cảnh báo passive |
| 15 | Progress indicator: Zeigarnik Effect compliance | DDL Law | zeigarnik | Gap | Từ ảnh kich-hoat-the-3.png: Không có step indicator — user không feel progress → anxiety tăng |
| 16 | Success modal quality — Peak-End Rule | DDL Law | peak-end | Pass | Từ ảnh kich-hoat-the-4.png: Modal có checkmark, text rõ ràng "Đã kích hoạt thành công", 2 CTA phân cấp tốt |
| 17 | CTA hierarchy: Primary vs Secondary trong modal | Skill B | UXG-165 | Pass | Từ ảnh kich-hoat-the-4.png: "Cài đặt mã PIN" (filled/primary) vs "Bỏ qua" (ghost/secondary) — hierarchy đúng |

---

### 3. Kích hoạt thẻ › Đặt mã PIN thẻ (`SCR-KHT-003`)

> `SCR-KHT-003` · form · 10 artboards

**Score: 56% | Pass: 5 | Gap: 4**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:-------:|:---------|
| 18 | `otp-input-1` spec: mask_toggle (show/hide PIN) | Skill A · C1 | COMP:otp-input-1 | Gap | Từ ảnh kich-hoat-the-6.png + case-loi-4..10 (rerun): Không có eye icon trong tất cả 10 artboards — confirmed gap |
| 19 | `otp-input-1` spec: real-time validation checklist | Skill A · C1 | COMP:otp-input-1 | Gap | Từ ảnh kich-hoat-the-6.png: Rules trong Lưu ý static. Không có real-time feedback khi user nhập PIN |
| 20 | Error coverage: đầy đủ 7 error states — inline pattern | Skill B | UXG-165 | Pass | Rerun vision case-loi-4..10: 7 error states với inline messages dưới field đúng. case-loi-4: "PIN trùng nhau" dưới Nhập mã PIN; case-loi-9: "PIN không khớp" dưới Nhập lại mã PIN |
| 21 | PIN rules nhất quán với error messages | Skill B | — | Pass | Từ ảnh: Rules "liên tiếp/trùng nhau" trong Lưu ý khớp với case-loi-4,5 error messages |
| 22 | Success state color (navy brand token) | Skill C · C2 | TOKEN:base.primary=#1E3A8A | Pass | Từ ảnh kich-hoat-the-8.png: Checkmark dùng navy blue — nhất quán brand identity Co-opBank |
| 23 | PIN success modal quality (Peak-End Rule) | DDL Law | peak-end | Pass | Từ ảnh kich-hoat-the-8.png: "Cài đặt mã PIN thành công" + "Đóng" — cuối flow rõ ràng, clean |
| 24 | Information architecture: Lưu ý block không chiếm quá 25% height | Skill B | UXG-165 | Gap | Từ ảnh kich-hoat-the-6.png: Khối Lưu ý chiếm ~30% height màn hình, đẩy PIN form xuống dưới |
| 25 | PIN input cells touch area (Fitts's Law) | DDL Law | fitts | Pass | Từ ảnh kich-hoat-the-6.png: Các ô PIN (6 cells) chiếm full width — adequate touch area |
| 26 | Error state: input fields có red border visual affordance | Skill C · C3 | UXG-165 | Gap | Rerun vision case-loi-4..10: Tất cả 7 error artboards — error text hiển thị nhưng input cells KHÔNG có border màu đỏ. Thiếu visual affordance chỉ rõ field lỗi |

---

## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Kích hoạt thẻ › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | Soft OTP thiếu attempt counter, countdown timer, và "Gửi lại" button |
| **Gap ref** | Check #10, #11, #14 |
| **DDL** | COMP:otp-input-1 (canResend, timeLeft, lockout states) |
| **Giải pháp** | Thêm: (1) "Còn X lần thử" counter, (2) Countdown "Gửi lại sau Xs", (3) "Gửi lại OTP" button |

---

#### UXP-002 · Critical
| **Màn hình** | Kích hoạt thẻ › Đặt mã PIN thẻ |
|:---|:---|
| **Vấn đề** | PIN input thiếu show/hide toggle — user nhập blind, tăng risk lỗi |
| **Gap ref** | Check #12, #18 |
| **DDL** | COMP:otp-input-1 (mask_toggle) |
| **Giải pháp** | Thêm eye icon (show/hide) cho cả 2 PIN fields trên SCR-KHT-003; cũng áp dụng cho Soft OTP field SCR-KHT-002 |

---

#### UXP-003 · Critical
| **Màn hình** | Kích hoạt thẻ › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Modal error interrupt thay vì inline error — disruptive UX pattern |
| **Gap ref** | Check #3 |
| **DDL** | UXG-165 (error handling best practices) |
| **Giải pháp** | Replace modal bằng inline error message dưới input field với icon cảnh báo |

---

#### UXP-004 · Major
| **Màn hình** | Kích hoạt thẻ › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | 3-step flow (Nhập số thẻ → OTP → PIN) không có progress indicator |
| **Gap ref** | Check #5, #15 |
| **DDL** | COMP:step-indicator-1, Law:zeigarnik |
| **Giải pháp** | Thêm step dots hoặc "Bước 1/3" ở header. Zeigarnik: user cần biết progress |

---

#### UXP-005 · Major
| **Màn hình** | Kích hoạt thẻ › Đặt mã PIN thẻ |
|:---|:---|
| **Vấn đề** | Validation rules hiển thị static trong Lưu ý, không có real-time feedback |
| **Gap ref** | Check #19 |
| **DDL** | COMP:otp-input-1 (realtime_validation) |
| **Giải pháp** | Checklist rules đổi màu từ xám → xanh real-time khi user nhập đạt điều kiện |
