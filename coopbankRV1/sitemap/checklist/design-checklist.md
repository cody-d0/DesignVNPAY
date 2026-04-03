# 📋 Design Checklist — Co-opBank KHCN

> **Source:** Pipeline audit v2.0 (87 heuristics, 8 domains) + Known issues backlog
> **Modules:** HOME · TRANSFER · PAYMENT
> **Updated:** 2025-03-30 · Auto-generated from domain packs + audit data

---

## ✦ Cross-cutting (Tất cả modules)

### 🛡️ OTP Compliance
- [ ] 🔴 OTP 6-cell input với auto-tab giữa ô `OTP-01`
- [ ] 🔴 Countdown timer hiển thị rõ ràng `OTP-01`
- [ ] 🔴 Nút Gửi lại OTP khi hết giờ `NUG-C24K-002`
- [ ] 🟠 Xác thực sinh trắc học: có fallback OTP khi thất bại `OTP-03`
- [ ] 🟠 Back navigation từ OTP screen có dialog "Hủy xác thực?" `OTP-02`
- [ ] 🟠 Error text contrast ≥ 4.5:1 (dùng #D32F2F) `OTP-04`
- [ ] 🟡 Timer announcement mỗi 15s khi < 60s (screen reader) `OTP-05`

### 🔒 PII & Bảo mật
- [ ] 🔴 TK nguồn masked: •••• XXXX format trên form + confirm `NUG-CTCC-002`
- [ ] 🟠 Thông tin cá nhân (CMND, ngày sinh) masked default + toggle reveal `NUG-DNBL-001`

### 📐 Layout & Typography
- [ ] ⬜ Header/title hiển thị đúng cấp bậc (font size, weight)
- [ ] ⬜ Spacing giữa các thành phần nhất quán (8px grid)
- [ ] ⬜ Text truncation xử lý đúng cho nội dung dài
- [ ] ⬜ Responsive layout ở nhiều kích thước màn hình

### 🧭 Navigation & Flow
- [ ] ⬜ Nút Back hoạt động đúng (quay về MH trước)
- [ ] ⬜ Breadcrumb / tiêu đề MH giúp user biết vị trí hiện tại
- [ ] ⬜ Luồng chuyển tiếp giữa các MH mượt mà (transition)

### ⚠️ Error & Edge Cases
- [ ] 🟠 Có xử lý trạng thái trống (empty state) với illustration + CTA
- [ ] 🟠 Có hiển thị loading state (skeleton shimmer) khi chờ dữ liệu
- [ ] 🟠 Error message rõ ràng, có hướng dẫn khắc phục + retry CTA
- [ ] 🟠 Xử lý timeout / mất kết nối với thông báo cụ thể

### ♿ Accessibility & UX
- [ ] ⬜ Contrast ratio đạt WCAG AA (4.5:1 cho text)
- [ ] ⬜ Touch target ≥ 48dp cho mobile (không phải 44px)
- [ ] ⬜ Label rõ ràng cho các input/action

### ✍️ Copy & Microcopy
- [ ] 🟠 Không có typo "Qúy" — phải là "Quý" `NUG-CTCC-003`
- [ ] 🟠 Confirmation title cụ thể (KHÔNG "Thông báo") `NUG-CTCC-004`
- [ ] 🟠 Hotline number thực — KHÔNG placeholder "1900 xxxx" `OTP-01`

---

## 🏠 HOME

### Dashboard Core
- [ ] 🟠 Widget số dư ẩn/hiện đúng (masked default + toggle) `NUG-DNBL-001`
- [ ] 🟠 BalanceCard loading state: skeleton shimmer `HD-01`
- [ ] 🟠 BalanceCard currency label "₫" hiển thị nhất quán `HD-05`
- [ ] 🟠 Quick actions sắp xếp logic, mặc định: CT, TT, QR, TK `HD-06`
- [ ] 🟠 GreetingHeader: contextual greeting "Xin chào [name]" `NUG-HOME-003`
- [ ] 🟠 GreetingHeader error: fallback "Xin chào bạn" khi không có name `HD-02`
- [ ] 🟡 CooperativeCard: thông tin HTX (cổ tức, thành viên) `NUG-HOME-004`

### Layout & Information Architecture
- [ ] 🟠 Feature overload: balance-first card layout, giảm clutter `NUG-HOME-001`
- [ ] 🟠 Quick actions hỗ trợ customizable (long-press reorder) `NUG-HOME-002`
- [ ] 🟡 Long-press tutorial tooltip overlay cho lần đầu `HD-03`
- [ ] 🟡 "☰" More icon: dùng "Khác" label hoặc "···" icon `HD-04`

### Accessibility HOME
- [ ] 🟠 CooperativeCard screen reader: "Thành viên HTX, cổ tức [X]%" `HD-08`
- [ ] 🟠 Settings icon touch target ≥ 48dp `HD-07`

### States HOME
- [ ] ⬜ Default state — trang chủ đầy đủ data
- [ ] ⬜ Loading state — skeleton cho tất cả cards
- [ ] ⬜ Empty state — user mới, chưa có giao dịch
- [ ] ⬜ Error state — không load được data
- [ ] ⬜ Offline state — cached data + offline banner

---

## 💸 TRANSFER

### Flow & Data Integrity
- [ ] 🔴 Data consistency form → confirm screen phải khớp 100% `NUG-CTCC-001`
- [ ] 🔴 Lịch sử giao dịch đặt lịch: data consistency `NUG-CTDL-001`
- [ ] 🟠 Flow 3 bước: Select → Enter → Confirm (giảm từ 6 bước) `NUG-CTKC-001`
- [ ] 🟠 Phí giao dịch hiển thị inline trên form, TRƯỚC confirm `NUG-CTKC-002`
- [ ] 🟠 Số tiền bằng chữ: "500,000 → Năm trăm nghìn đồng" `NUG-CTKC-003`

### Validation & Input
- [ ] 🟠 Validation số tài khoản/thẻ real-time với inline error `NUG-C24T-001`
- [ ] 🟠 Error state cho invalid input: red border + helper text `NUG-C24K-001`
- [ ] 🟠 Helper text cho input types (STK, thẻ, SĐT) `NUG-C24T-003`
- [ ] 🟠 Auto-fill label phân biệt "[Tự động]" vs user-entered `NUG-C24T-002`

### Xác nhận & Navigation
- [ ] 🟠 Progress indicator (step 1/3) trên mỗi bước `IT-04`
- [ ] 🟠 Back navigation có dialog "Hủy giao dịch?" `IT-01`
- [ ] 🟠 Max transfer limit: error "Vượt hạn mức. Quý khách liên hệ..." `IT-02`
- [ ] 🟠 Offline error handling: connectivity-specific messages `IT-03`
- [ ] 🟠 OTP cell spacing ≥ 8dp (hiện 4dp) `IT-06`

### Danh bạ thụ hưởng
- [ ] 🟠 Toast hướng dẫn xóa contact `NUG-DBTH-001`
- [ ] 🟠 Empty state: danh bạ mới chưa có người hưởng `NUG-DBTH-002`
- [ ] 🟡 Search + filter cho danh bạ > 20 entries `NUG-DBTH-003`

### Đặt lịch
- [ ] 🟠 Loading state cho history list `NUG-CTDL-002`
- [ ] 🟠 Empty state cho lịch trống `NUG-CTDL-003`
- [ ] 🟡 Date picker: calendar view thay dropdown `NUG-CTDL-004`

### Interbank-specific
- [ ] 🟠 NAPAS downtime: error state + re-check schedule `IB-02`
- [ ] 🟠 Processing time: hiển thị "~5-30 giây" (không misleading) `IB-03`

### States TRANSFER
- [ ] ⬜ Default — form trống, ready input
- [ ] ⬜ Loading — khi kiểm tra TK thụ hưởng
- [ ] ⬜ Error — input invalid, TK không tồn tại
- [ ] ⬜ Success — kết quả giao dịch thành công
- [ ] ⬜ Failed — kết quả giao dịch thất bại + retry
- [ ] ⬜ Timeout — nghi vấn do timeout + hướng dẫn

---

## 🧾 PAYMENT

### Thanh toán hóa đơn Core
- [ ] 🟠 Smart search: tìm theo tên nhà cung cấp/mã HĐ `NUG-TTOAN-001`
- [ ] 🟠 Banner cảnh báo "Kiểm tra kỹ thông tin trước khi xác nhận" `NUG-TTOAN-001`
- [ ] 🟠 PII: TK nguồn masked trên confirm screen `NUG-TTOAN-002`
- [ ] 🟠 Confirmation title: "Xác nhận thanh toán [Provider]" `NUG-TTOAN-003`
- [ ] 🟠 Chi tiết hóa đơn hiển thị đầy đủ trước thanh toán

### Saved Bills & Recurring
- [ ] 🟠 1-tap pay: QuickPayDialog confirmation (không skip confirm) `BP-02`
- [ ] 🟠 SavedBillCard "paying" state: loading overlay `BP-05`
- [ ] 🟡 Recurring bill reminders: push notification trước hạn `BP-03`

### Layout & Categories
- [ ] 🟠 Category icon spacing ≥ 8dp `BP-06`
- [ ] 🟡 Provider logos cho visual recognition
- [ ] 🟡 Auto-pay scheduling cho hóa đơn định kỳ

### States PAYMENT
- [ ] ⬜ Default — danh sách dịch vụ/provider
- [ ] ⬜ Loading — khi tra cứu hóa đơn
- [ ] ⬜ Empty — chưa có hóa đơn đã lưu
- [ ] ⬜ Error — không tra cứu được + retry CTA
- [ ] ⬜ Success — thanh toán thành công + receipt

---

> **Legend:**
> 🔴 Critical — Fix TRƯỚC khi đi design | 🟠 Major — Fix trong Sprint 1-2
> 🟡 Minor — Backlog | ⬜ Standard — Best practice chung
> `ID` = Source reference (NUG-xxx = Nugget, HD/IT/IB/BP/OTP = Known Issue)

*Generated from: domain packs, audit reports v2.0, known-issues-backlog, qa-checklist*
