# SCR-TRK-004 — Xác nhận yêu cầu tra soát › Xác nhận giao dịch

**Screen ID:** SCR-TRK-004  
**Figma nodes:** 142:29454 (base), 142:29557 (overlay: Chi tiết GD), 142:29509 (overlay: OTP)  
**Screen type:** confirm  
**Flow:** Tạo yêu cầu tra soát khác  
**Wireframes:** `ui/tra-soat-khac-3.png`, `ui/tra-soat-mobile-11.png`, `ui/tra-soat-khac-5.png`

---

## 1. Flow & Navigation

- **Entry:** SCR-TRK-003 (CTA "Tra soát")
- **Overlay 1:** Bottom sheet "Chi tiết giao dịch" (triggered by link "Chi tiết giao dịch >")
  - Close: × button → đóng bottom sheet, giữ base screen
- **Overlay 2:** Bottom sheet "Xác thực giao dịch" (OTP) (triggered by CTA "Tiếp tục")
  - Close: × button → đóng OTP sheet
  - Confirm: "Xác nhận" → SCR-TRK-005
- **Back:** Quay về SCR-TRK-003 (giữ dữ liệu form)

### User Story

> Là người dùng Co-opBank, tôi muốn xem lại thông tin tra soát trước khi xác nhận, và có thể xem chi tiết giao dịch đang tra soát. Sau đó xác thực bằng OTP để gửi yêu cầu.

---

## 2. UX Signal Inference (Phase 4e · scope=screen)

**Signals detected — base screen:**
- "Chi tiết giao dịch >" → progressive disclosure trigger
- "Tiếp tục" → multi-step flow CTA (không phải submit cuối)
- "5,500 VND" → phí tra soát displayed → user aware of cost before confirming

**Signals detected — bottom sheet Chi tiết GD:**
- 11 data rows → extensive transaction details
- "Label 2" → placeholder chưa fill (status)
- "Trạng thái giao dịch" → status field cần clear value, không phải placeholder

**Signals detected — OTP overlay:**
- "098****123" → masked phone number → privacy-compliant
- 6 digit cells → OTP 6 chữ số
- "Xác nhận" → submit OTP

**Inferred UX:**
- **Pattern:** Review → Progressive Disclosure → OTP Auth flow
- **Component:** Review card (2 sections), Bottom sheet (scrollable), OTP 6-digit input
- **State:** base / overlay-chi-tiet / overlay-otp
- **DDL ref:** ux-guidelines.csv#52 (Review Step), ux-guidelines.csv#61 (OTP Input), ux-laws.csv#miller (7±2 items per section)

---

## 3. Mô tả màn hình

### Base screen (tra-soat-khac-3.png)

| Element | Nội dung | Ghi chú |
|---------|---------|---------|
| Header | "Xác nhận yêu cầu" | Back + Home |
| Section 1 | "Thông tin giao dịch" | Badge S đỏ |
| Ngày giao dịch | 20/02/2025 | Read-only |
| Loại giai dịch | 12312329 | **Lỗi typo:** "giai" → "giao" |
| Số TK/ Số thẻ GD | 1212390002122 | Read-only |
| Chi tiết giao dịch | Link "Chi tiết giao dịch >" | → bottom sheet |
| Section 2 | "Thông tin tra soát" | Badge S đỏ |
| Lý do tra soát | Chưa nhận được tiền | Read-only |
| Nội dung tra soát | abc123 | Read-only |
| Tài khoản thu phí | 1212390002122 | Read-only |
| Phí tra soát | **5,500 VND** | Hiển thị chi phí |
| CTA | "Tiếp tục" | → trigger OTP sheet |

### Overlay: Chi tiết giao dịch (tra-soat-mobile-11.png)

| Field | Giá trị | Ghi chú |
|-------|---------|---------|
| Thời gian giao dịch | 20/02/2025 18:00 | |
| Mã giao dịch | 1123123 | |
| Tài khoản nguồn | 123123123123123 | |
| Tài khoản thụ hưởng | 563243433222233 | |
| Ngân hàng thụ hưởng | Vietcombank | |
| Số tiền giao dịch | 100,000 VND | |
| Đối tượng chịu phí | Người chuyển trả | |
| Phí giao dịch và thuế | 5,500 VND | |
| Loại giao dịch | Chuyển tiền nhanh 24/7 qua tài khoản | |
| Nội dung giao dịch | abc123 | |
| Trạng thái giao dịch | Label 2 | **BUG:** Placeholder chưa fill |

### Overlay: OTP (tra-soat-khac-5.png)

| Element | Nội dung | Ghi chú |
|---------|---------|---------|
| Title | "Xác thực giao dịch" | + × close |
| Instruction | "Quý khách vui lòng nhập mã OTP đã được gửi về số điện thoại 098****123" | Masked phone |
| OTP Input | 6 digit cells | 44×44px each |
| CTA | "Xác nhận" | Active sau khi nhập đủ 6 digits |

### NFR

- Bottom sheet: swipe-to-dismiss support
- OTP: auto-focus first cell, auto-advance, paste support
- OTP: countdown timer (thời hạn OTP), link "Gửi lại" khi hết hạn
- Bottom sheet scrollable (11 rows > viewport)

---

## 4. UX Improvements (từ signal inference)

- **[Critical] Typo "Loại giai dịch":** Trên màn xác nhận base screen, field "Loại giai dịch" có typo — đúng là "Loại giao dịch". Lỗi typo trên màn xác nhận gây mất tin tưởng. DDL ref: ux-guidelines.csv#72 (Content Accuracy)
- **[Critical] "Trạng thái giao dịch: Label 2":** Bottom sheet "Chi tiết giao dịch" hiển thị "Label 2" là giá trị placeholder chưa được fill — cần map sang trạng thái thực (VD: "Thành công", "Đang xử lý"). DDL ref: ux-guidelines.csv#72
- **[Major] OTP thiếu countdown timer:** Màn OTP không hiển thị thời gian còn lại và link "Gửi lại OTP" — người dùng không biết khi nào OTP hết hạn. DDL ref: ux-guidelines.csv#61 (OTP UX), ux-laws.csv#doherty (Response time feedback)
- **[Major] Xác nhận thiếu total summary:** Section 1 chỉ hiển thị 3 fields (không đủ context) — người dùng phải click "Chi tiết giao dịch" để xem đầy đủ. Thông tin tối thiểu (số tiền, ngân hàng nhận) nên visible trực tiếp. DDL ref: ux-guidelines.csv#52
- **[Minor] Bottom sheet 11 rows không có divider nhóm:** 11 rows trong chi tiết không có visual grouping — Hick's Law: nên nhóm 3-4 fields có liên quan (thông tin bên nhận / số tiền / loại GD). DDL ref: ux-laws.csv#miller
