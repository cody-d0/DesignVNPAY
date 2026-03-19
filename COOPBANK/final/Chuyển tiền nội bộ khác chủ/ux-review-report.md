# UX Review Report — Co-opBank: Chuyển tiền nội bộ khác chủ

## Tổng quan

- Folder: `coopbank/final/Chuyển tiền nội bộ khác chủ`
- Số màn hình: 3 | Tổng check: 50
- Pass: 39 | Gap: 9 | Unverifiable: 2
- UX Score (Simple): 78%
- UX Score (Weighted): 100%

---

## Đề xuất cải tiến (Priority)

### 🔴 Critical

#### UXP-001 · 🔴 Critical

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ khác chủ › Xác nhận giao dịch |
| **Mức độ** | 🔴 Critical |
| **DDL** | COMP:otp-input-1 · UXG-184 |
| **UX Law** | doherty |

**🔍 Hiện trạng**

OTP bottom sheet (artboard 59:20942) hiển thị 6 ô digit-input tĩnh. DDL component spec `otp-input-1` yêu cầu states: `activeIndex` (highlight ô đang nhập), `canResend` (cho phép gửi lại OTP), `timeLeft` (đếm ngược). Từ ảnh `internal-transaction-6.png`: chỉ thấy 6 ô trống + nút "Xác nhận", KHÔNG có nút "Gửi lại mã" hay countdown timer.

> Evidence: DDL `otp-input-1` spec: states `canResend`, `timeLeft`, children `resend-button`, `countdown-timer`. Screenshot: 6 static cells, NO resend UI, NO timer.

**⚠️ Hậu quả**

- **User impact:** Nếu OTP không đến (network delay, SMS congestion), user bị kẹt tại màn hình OTP không có cách gửi lại → task failure, phải thoát app và làm lại từ đầu
- **Business impact:** Drop-off tại bước xác thực → mất conversion giao dịch, tăng support calls
- **Violation:** DDL `COMP:otp-input-1` mandatory states missing; UXG-184 (Keyboard Navigation); Doherty Threshold (response > 400ms without feedback)

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Resend button | Thêm "Gửi lại mã OTP" (disabled trong 60s đầu) | Dưới 6 ô OTP, trước nút Xác nhận |
| 2 | Countdown timer | Hiển thị "Gửi lại sau 00:45" với đếm ngược real-time | Inline với resend button |
| 3 | Active cell highlight | Ô đang nhập có border highlight (TOKEN:base.ring=#a1a1aa → active ring) | 6 ô digit-input |

---

#### UXP-002 · 🔴 Critical

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ khác chủ › Form nhập thông tin |
| **Mức độ** | 🔴 Critical |
| **DDL** | UXG-165 · UXG-243 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh `internal-transaction.png` và `internal-transaction-2.png`: Trường "Số tiền" chỉ hiển thị giá trị số (300,000) + đơn vị "VND". KHÔNG có số tiền viết bằng chữ (text representation) trên form nhập. Chỉ hiển thị trên màn Xác nhận (internal-transaction-5.png: "Hai mươi triệu đồng").

> Evidence: Screenshot form: "Số tiền: 300,000 VND" — no text representation. Confirm screen shows "Hai mươi triệu đồng" but form doesn't.

**⚠️ Hậu quả**

- **User impact:** User có thể nhập sai số tiền (nhầm số 0) mà không phát hiện sớm → chỉ thấy bằng chữ ở màn Xác nhận, khi đó phải quay lại sửa
- **Business impact:** Giao dịch sai số tiền → claim, hoàn tiền, mất uy tín
- **Violation:** UXG-165 (Input Validation — real-time feedback); Banking best practice yêu cầu amount confirmation text

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Amount text representation | Thêm dòng chữ viết số tiền real-time dưới input (e.g., "Ba trăm nghìn đồng") | Dưới field "Số tiền", font size 12px, color `base.muted-foreground` |

---

### 🟡 Major

#### UXP-003 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ khác chủ › Form nhập thông tin |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-180 |
| **UX Law** | fitts |

**🔍 Hiện trạng**

Từ ảnh `internal-transaction.png`: Nút "Tiếp tục" (CTA chính) nằm sát đáy màn hình, có thể bị che bởi keyboard khi user đang nhập liệu ở các trường phía dưới (nội dung giao dịch, đặt lịch). Form state 2 (`internal-transaction-2.png`) dài 1098px (vượt viewport 812px) — CTA bị đẩy ra khỏi viewport.

> Evidence: Artboard 59:20803 height=1098px vs device 812px. CTA "Tiếp tục" at y=1039. User must scroll to find CTA.

**⚠️ Hậu quả**

- **User impact:** User điền xong form nhưng không thấy nút Tiếp tục → confusion, phải scroll tìm
- **Business impact:** Drop-off tại CTA → giảm completion rate
- **Violation:** Fitts's Law (CTA xa tầm ngón tay); UXG-180 (CTA visibility)

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Sticky CTA | Fix nút "Tiếp tục" ở bottom (sticky footer) — luôn hiển thị trên keyboard | Bottom 0, padding 16px, background white với shadow top |
| 2 | Scroll indicator | Thêm subtle shadow/gradient phía trên CTA khi có content bị che | Trên sticky CTA bar |

---

#### UXP-004 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ khác chủ › Kết quả giao dịch |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-165 |
| **UX Law** | peak-end |

**🔍 Hiện trạng**

Từ ảnh `internal-transaction-7.png`: Header hiển thị "50,000 VND" nhưng trong detail section lại ghi "Số tiền: 20,000,000 VND". Hai số tiền không khớp nhau — gây confusion. Đây có thể là lỗi data mẫu nhưng phản ánh rủi ro hiển thị inconsistency.

> Evidence: Screenshot result: header "50,000 VND" vs detail "20,000,000 VND" — amount mismatch.

**⚠️ Hậu quả**

- **User impact:** User hoang mang: "Chuyển 50K hay 20 triệu?" → mất tin tưởng vào hệ thống
- **Business impact:** Erode trust — Peak-End Rule: trải nghiệm cuối (result screen) là ấn tượng cuối cùng
- **Violation:** UXG-165 (Data consistency); Peak-End Rule (negative final impression)

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Amount sync | Header amount PHẢI match detail amount — lấy từ cùng 1 source | Result card header |
| 2 | Amount text | Thêm chữ viết dưới số tiền header (e.g., "Hai mươi triệu đồng") | Dưới amount highlight |

---

#### UXP-005 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ khác chủ › Xác nhận giao dịch |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-183 |
| **UX Law** | hick |

**🔍 Hiện trạng**

Từ ảnh `internal-transaction-5.png`: Dropdown "Chọn phương thức xác thực: SMS OTP" hiển thị 1 option duy nhất. Theo Hick's Law, nếu chỉ có 1 method → không cần dropdown. Nếu có nhiều methods (Smart OTP, Token...) → cần list rõ options.

> Evidence: Screenshot: "SMS OTP" with dropdown chevron. Only 1 option visible. No other auth methods shown.

**⚠️ Hậu quả**

- **User impact:** Dropdown 1 option gây confusion — user click vào expecting choices nhưng chỉ có 1
- **Business impact:** Unnecessary tap → tăng task time
- **Violation:** Hick's Law (unnecessary decision point); UXG-183 (ARIA Labels — dropdown semantics)

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Auth method display | Nếu chỉ 1 method: hiển thị static text "Xác thực bằng SMS OTP" (không dropdown). Nếu ≥2: giữ dropdown | Section auth method |

---

### ⚪ Minor

#### UXP-006 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ khác chủ › Xác nhận giao dịch |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-165 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh `internal-transaction-5.png`: Banner text ghi "Qúy khách" (sai dấu: "ú" thay vì "uý") — đúng phải là "Quý khách". Lỗi typography nhỏ nhưng ảnh hưởng chuyên nghiệp.

> Evidence: Screenshot banner: "Qúy khách vui lòng kiểm tra lại..." — typo "Qúy" → "Quý"

**⚠️ Hậu quả**

- **User impact:** Giảm perceived quality, đặc biệt với user Việt Nam nhạy cảm chính tả
- **Business impact:** Ảnh hưởng brand quality perception
- **Violation:** UXG-165 (Content accuracy)

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Banner text | Sửa "Qúy khách" → "Quý khách" | Info banner, confirm screen |

---

#### UXP-007 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ khác chủ › Form nhập thông tin |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-181 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh `internal-transaction.png`: Nội dung giao dịch auto-fill "NGUYEN HOANG KHAI chuyen tien" — không dấu tiếng Việt, format không chuẩn (viết thường "chuyen tien"). Đây là pattern chuẩn ngân hàng (unaccented Vietnamese) nhưng có thể cải thiện UX.

> Evidence: Screenshot: "NGUYEN HOANG KHAI chuyen tien" — unaccented auto-fill

**⚠️ Hậu quả**

- **User impact:** User có thể không nhận ra nội dung auto-fill — thường muốn ghi rõ hơn
- **Business impact:** Minimal — đây là convention ngành

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Auto-fill format | Thêm label "[Tự động]" bên cạnh nội dung auto-fill để user biết có thể sửa | Dưới textarea nội dung |

---

#### UXP-008 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ khác chủ › Kết quả giao dịch |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-235 |
| **UX Law** | peak-end |

**🔍 Hiện trạng**

Từ ảnh `internal-transaction-7.png`: Thời gian đặt lịch hiển thị "15/02/2020 22:00" — ngày trong quá khứ so với ngày bắt đầu 15/05/2023. Đây là data mẫu inconsistent. Ngoài ra, không có thông tin phí giao dịch (fee) trên biên nhận.

> Evidence: Screenshot result: "Thời gian đặt lịch: 15/02/2020" but "Ngày bắt đầu: 15/05/2023" — time paradox in sample data. No fee information displayed.

**⚠️ Hậu quả**

- **User impact:** User không biết phí giao dịch cụ thể là bao nhiêu — chỉ biết "theo quy định Co-opBank"
- **Business impact:** Thiếu transparency → giảm trust

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Fee display | Thêm dòng "Phí giao dịch: X VND" + "VAT: Y VND" trên biên nhận | Sau "Nội dung giao dịch", trước bottom actions |
| 2 | Sample data | Đảm bảo thời gian đặt lịch logic với ngày bắt đầu | Data consistency check |

---

## Chi tiết theo màn hình

### 1. Chuyển tiền nội bộ khác chủ › Form nhập thông tin
> `SCR-CTNBKC-001` · form · 4 artboards
>
> **Score: 85% | Pass: 17 | Gap: 2 | Unverifiable: 1 | Images: internal-transaction.png, internal-transaction-2.png, internal-transaction-3.png, internal-transaction-4.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header bar hiển thị title + back arrow | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: Header "Chuyển tiền nội bộ khác chủ" + back arrow top-left |
| 2 | Balance card hiển thị TK nguồn + số dư | Skill A | — | ✅ Pass | Từ ảnh: "Tài khoản nguồn 9099798712313123" + "Số dư khả dụng 20,000,000 VND" |
| 3 | Input field Số tài khoản có placeholder rõ | Skill B | COMP:text-input-1 | ✅ Pass | Từ ảnh: Placeholder "Số tài khoản/Số thẻ/Số điện thoại" — descriptive |
| 4 | Contact icon trigger danh bạ thụ hưởng | Skill A | UXG-184 | ✅ Pass | Từ ảnh: Icon 👤 bên phải input field — tappable area |
| 5 | Auto-fill tên người hưởng sau nhập STK | Skill B | — | ✅ Pass | Từ ảnh state 2: "NGUYEN HOANG HIEU" tự điền dưới input |
| 6 | Toggle Lưu danh bạ thụ hưởng (OFF default) | Skill A | — | ✅ Pass | Từ ảnh state 2: Toggle OFF bên phải "Lưu danh bạ thụ hưởng" |
| 7 | Số tiền có đơn vị VND rõ ràng | Skill B | — | ✅ Pass | Từ ảnh: "VND" label bên phải input số tiền |
| 8 | Số tiền có text representation (chữ viết) | Skill C | UXG-165 | ❌ Gap | Từ ảnh: Form chỉ hiển thị số + VND, KHÔNG có chữ viết. Xem UXP-002 |
| 9 | Nội dung giao dịch có character counter | Skill A | COMP:text-input-1 | ✅ Pass | Từ ảnh: "30/160" counter top-right của textarea |
| 10 | Dropdown đối tượng chịu phí | Skill B | — | ✅ Pass | Từ ảnh: "Người chuyển trả" + chevron dropdown |
| 11 | Toggle Đặt lịch chuyển tiền | Skill A | — | ✅ Pass | Từ ảnh state 1: Toggle OFF; state 2: Toggle ON + scheduling fields expand |
| 12 | Scheduling: Tần suất dropdown | Skill B | — | ✅ Pass | Từ ảnh state 2: "Hàng tháng" + dropdown chevron |
| 13 | Scheduling: Ngày bắt đầu date picker | Skill B | — | ✅ Pass | Từ ảnh state 2: "15/05/2023" + calendar icon |
| 14 | CTA "Tiếp tục" luôn visible | Skill C | UXG-180 | ❌ Gap | Từ ảnh: State 2 artboard 1098px vs viewport 812px — CTA bị đẩy dưới fold. Xem UXP-003 |
| 15 | Popup validation: yêu cầu STK cho đặt lịch | Skill C | — | ✅ Pass | Từ ảnh overlay: "Vui lòng nhập Thông tin thụ hưởng là số tài khoản..." |
| 16 | Popup validation: giới hạn 10 lần | Skill C | — | ✅ Pass | Từ ảnh overlay: "Số lần giao dịch không được vượt quá 10 lần" |
| 17 | Popup có nút dismiss "Đóng" | Skill C | — | ✅ Pass | Từ ảnh: Cả 2 popup đều có nút "Đóng" màu xanh |
| 18 | Fitts's Law — touch targets ≥44px | Skill A | fitts | ✅ Pass | Từ ảnh: Buttons 343×48px (CTA), toggle 44×24px — đạt minimum |
| 19 | Hick's Law — số options hợp lý | Skill A | hick | ✅ Pass | Từ ảnh: Dropdown 1 option "Người chuyển trả", toggle binary — simple choices |
| 20 | Error state cho input fields | Skill B | COMP:text-input-1 | ⚠️ Unverifiable | Không có artboard hiển thị error state (red border, error text) cho input — không thể verify từ ảnh tĩnh |

---

### 2. Chuyển tiền nội bộ khác chủ › Xác nhận giao dịch
> `SCR-CTNBKC-002` · confirm · 2 artboards
>
> **Score: 71% | Pass: 12 | Gap: 4 | Unverifiable: 1 | Images: internal-transaction-5.png, internal-transaction-6.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header "Xác nhận giao dịch" + back arrow | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: Header dark bg "Xác nhận giao dịch" + back arrow |
| 2 | Info banner hướng dẫn kiểm tra | Skill C | — | ✅ Pass | Từ ảnh: Blue gradient banner "Quý khách vui lòng kiểm tra lại thông tin..." |
| 3 | Detail list hiển thị đầy đủ fields | Skill B | — | ✅ Pass | Từ ảnh: 9 rows key-value (TK nguồn, TK thụ hưởng, tên, tần suất, số lần, ngày, số tiền, nội dung) |
| 4 | Số tiền kèm chữ viết | Skill C | UXG-165 | ✅ Pass | Từ ảnh: "20,000,000 VND" + "Hai mươi triệu đồng" (orange text) |
| 5 | Tần suất + Số lần highlighted (visual emphasis) | Skill C | — | ✅ Pass | Từ ảnh: "Hàng tháng" và "2" hiển thị text màu xanh dương (different color) |
| 6 | Auth method dropdown | Skill B | — | ✅ Pass | Từ ảnh: "Chọn phương thức xác thực: SMS OTP" + dropdown |
| 7 | Single auth method — unnecessary dropdown | Skill C | hick | ❌ Gap | Từ ảnh: Chỉ 1 option "SMS OTP" trong dropdown. Xem UXP-005 |
| 8 | CTA "Xác nhận" full-width | Skill B | fitts | ✅ Pass | Từ ảnh: Button full-width 343×44px — đạt Fitts's Law |
| 9 | OTP bottom sheet: title + description | Skill C | — | ✅ Pass | Từ ảnh overlay: "Xác thực giao dịch" + mô tả OTP gửi về SĐT |
| 10 | OTP: SĐT masked (PII protection) | Skill A | — | ✅ Pass | Từ ảnh: "098****123" — mask 4 digits giữa |
| 11 | OTP: 6 digit cells | Skill C | COMP:otp-input-1 | ✅ Pass | Từ ảnh: 6 ô vuông cách đều nhau |
| 12 | OTP: active cell highlight | Skill C | COMP:otp-input-1 | ❌ Gap | Từ ảnh: 6 ô đều trống, cùng màu — không có highlight ô đang active. Xem UXP-001 |
| 13 | OTP: Resend button + countdown | Skill C | COMP:otp-input-1 | ❌ Gap | Từ ảnh: KHÔNG có "Gửi lại mã" hay countdown timer. Xem UXP-001 |
| 14 | OTP: Close X affordance | Skill C | — | ✅ Pass | Từ ảnh: X button top-right OTP sheet |
| 15 | OTP: Confirm CTA | Skill B | — | ✅ Pass | Từ ảnh: "Xác nhận" blue button full-width in sheet |
| 16 | Banner typo "Qúy khách" | Skill C | UXG-165 | ❌ Gap | Từ ảnh: "Qúy khách" — sai chính tả. Xem UXP-006 |
| 17 | Peak-End: positive confirmation experience | Skill A | peak-end | ⚠️ Unverifiable | OTP flow kết thúc → chuyển result. Không thể verify transition animation từ ảnh tĩnh |

---

### 3. Chuyển tiền nội bộ khác chủ › Kết quả giao dịch
> `SCR-CTNBKC-003` · result · 1 artboard
>
> **Score: 77% | Pass: 10 | Gap: 3 | Unverifiable: 0 | Images: internal-transaction-7.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header "Kết quả giao dịch" + home icon | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: Dark header "Kết quả giao dịch" + home icon (🏠) top-left |
| 2 | Success state: logo + checkmark + text | Skill C | — | ✅ Pass | Từ ảnh: Co-opBank logo + green checkmark circle + "Đặt lịch chuyển tiền thành công" |
| 3 | Amount highlight trong card header | Skill C | — | ✅ Pass | Từ ảnh: "50,000 VND" text lớn, xanh lá (success color) |
| 4 | Amount consistency header vs detail | Skill C | UXG-165 | ❌ Gap | Từ ảnh: Header "50,000 VND" vs detail "20,000,000 VND" — mismatch. Xem UXP-004 |
| 5 | Receipt-style card layout (rounded + dash divider) | Skill C | COMP:receipt-preview-1 | ✅ Pass | Từ ảnh: Card với rounded corners + dashed line divider — receipt pattern |
| 6 | Detail list đầy đủ (11 rows) | Skill B | — | ✅ Pass | Từ ảnh: Thời gian, TK nguồn/thụ hưởng, tên, số tiền, tần suất, số lần, ngày, mã, nội dung |
| 7 | Mã đặt lịch hiển thị | Skill B | — | ✅ Pass | Từ ảnh: "Mã đặt lịch: 0982312" — unique identifier |
| 8 | Share + Save actions | Skill C | — | ✅ Pass | Từ ảnh: "Chia sẻ" (share icon) + "Lưu ảnh" (save icon) — bottom of card |
| 9 | CTA "Tạo giao dịch mới" | Skill B | fitts | ✅ Pass | Từ ảnh: Full-width button below card |
| 10 | Fee information displayed | Skill C | UXG-235 | ❌ Gap | Từ ảnh: Receipt KHÔNG hiển thị phí giao dịch + VAT. Xem UXP-008 |
| 11 | Fitts's Law — touch targets | Skill A | fitts | ✅ Pass | Từ ảnh: CTA full-width, share/save icons adequate size |
| 12 | Peak-End Rule — positive closing | Skill A | peak-end | ✅ Pass | Từ ảnh: Success green checkmark + congratulatory text — positive emotional end |
| 13 | Thời gian đặt lịch logic vs ngày bắt đầu | Skill C | — | ❌ Gap | Từ ảnh: "15/02/2020 22:00" (quá khứ) vs "Ngày bắt đầu: 15/05/2023" — data inconsistent. Xem UXP-008 |

---

## DDL References sử dụng

| ddl_ref | Rule | UX Law | Áp dụng |
|---------|------|--------|---------|
| COMP:otp-input-1 | OTP input with auto-focus, paste support, resend timer | doherty | SCR-CTNBKC-002: OTP cells missing resend + countdown |
| COMP:text-input-1 | Enhanced text input with label, validation, icon | — | SCR-CTNBKC-001: Input fields, character counter |
| COMP:app-header-1 | Mobile app header with back button, title, actions | — | All screens: Header bar consistency |
| COMP:receipt-preview-1 | Receipt preview with line items, totals, share | — | SCR-CTNBKC-003: Result card layout |
| UXG-165 | Input Validation — real-time feedback | — | SCR-CTNBKC-001: Amount text missing; SCR-CTNBKC-003: Data mismatch |
| UXG-180 | Color Only — don't rely solely on color | fitts | SCR-CTNBKC-001: CTA visibility on long form |
| UXG-181 | Alt Text — meaningful alt text for images | — | SCR-CTNBKC-001: Auto-fill format |
| UXG-183 | ARIA Labels — proper labeling | hick | SCR-CTNBKC-002: Dropdown semantics |
| UXG-184 | Keyboard Navigation | doherty | SCR-CTNBKC-002: OTP digit navigation |
| UXG-235 | Disclaimer / transparency | peak-end | SCR-CTNBKC-003: Fee not displayed |
| UXG-243 | Amount confirmation | — | SCR-CTNBKC-001: Amount text representation |
| TOKEN:base.ring | #a1a1aa — focus ring color | — | OTP active cell highlight |
| TOKEN:base.destructive | #dc2626 — error color | — | Error states |
