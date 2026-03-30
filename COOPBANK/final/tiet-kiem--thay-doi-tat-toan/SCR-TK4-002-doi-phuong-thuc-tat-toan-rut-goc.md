# SCR-TK4-002 — Đổi phương thức tất toán/ rút gốc › Form nhập thông tin

**Screen ID:** SCR-TK4-002  
**Flow:** Thay đổi phương thức tất toán/ rút gốc  
**Product:** CoopBank Mobile Banking  
**Domain:** Banking  
**Screen Type:** form  
**Artboards:** 1502 (×4 variants), 1505 (overlay)  
**Wireframes:** `ui/1502-yoi-phuong-thuc-tat-toan.png`, `ui/1502-yoi-phuong-thuc-tat-toan-2.png`, `ui/1502-yoi-phuong-thuc-tat-toan-3.png`, `ui/1502-yoi-phuong-thuc-tat-toan-4.png`, `ui/1505-yoi-phuong-thuc-tat-toan.png`

---

## 1. Overview

Màn hình chọn phương thức tất toán/ rút gốc với 2 lựa chọn: **trực tuyến (online)** hoặc **tại quầy giao dịch**. Sau khi chọn và submit, hệ thống xác nhận qua popup → tiến hành xác thực bằng Soft OTP hoặc Face ID (tùy cấu hình sinh trắc học). Bao gồm xử lý edge cases: chưa đăng ký sinh trắc học, giấy tờ hết hạn.

**Mục tiêu người dùng:**
- Thay đổi phương thức tất toán/ rút gốc từ online sang tại quầy hoặc ngược lại

**Màn hình liên quan:**
- ← SCR-TK4-001 (entry point)
- → SCR-TK4-003 (khi cần xác thực Facepay)
- → SCR-TK4-001 (khi thành công)

---

## 2. User Story

> Là **khách hàng Co-opBank**, tôi muốn **thay đổi phương thức tất toán/ rút gốc tài khoản tiết kiệm từ online sang tại quầy** để **phù hợp với nhu cầu thực tế của mình**.

**Acceptance Criteria:**
- 2 options hiển thị rõ ràng: Tất toán / rút gốc online | Tất toán / rút gốc tại quầy
- Radio button thể hiện option đang chọn
- Popup xác nhận trước khi thay đổi
- Xác thực bằng Soft OTP (6 ô PIN) hoặc Face ID
- Edge case: Thông báo khi giấy tờ hết hạn / chưa đăng ký sinh trắc học

---

## 3. Screen Content (OCR)

| Element | Text |
|:--------|:-----|
| Header | Đổi phương thức tất toán/ rút gốc |
| Option 1 (selected) | Tất toán / rút gốc online |
| Option 2 (unselected) | Tất toán / rút gốc tại quầy |
| Popup title | Thông báo |
| Confirm question | Quý khách có chắc chắn thay đổi phương thức tất toán/ rút gốc của tài khoản không? |
| Cancel CTA | Huỷ |
| Confirm CTA | Đồng ý |
| Facepay popup | Giao dịch yêu cầu xác thực bằng Facepay. Quý khách vui lòng đăng ký "Thu thập sinh trắc học" để tiếp tục thực hiện giao dịch. |
| Change biometric CTA | Thay đổi |
| Expired ID popup | Giấy tờ của Quý khách đã hết hạn. Quý khách vui lòng thu thập lại thông tin sinh trắc học để tiếp tục thực hiện giao dịch. |
| OTP sheet title | Xác thực giao dịch |
| OTP instruction | Quý khách vui lòng nhập mã PIN của Soft OTP để xác thực giao dịch |
| OTP warning | Lưu ý: Soft OTP sẽ bị khóa nếu Quý khách nhập sai PIN 5 lần liên tiếp |
| OTP confirm CTA | Xác nhận |

---

## 4. Flow & Navigation

```
[SCR-TK4-001] → Đổi phương thức tất toán/ rút gốc
  ↓
[Form: chọn radio online / tại quầy]
  ↓ submit
  → [Popup xác nhận: "Huỷ" | "Đồng ý"]
      ↓ Đồng ý
      ├─ [Case 1: Facepay required] → Popup sinh trắc học → "Đồng ý" → SCR-TK4-003
      ├─ [Case 2: Giấy tờ hết hạn] → Popup expired → "Thay đổi" → cập nhật sinh trắc học
      ├─ [Case 3: Soft OTP] → Bottom-sheet OTP (6 cells) → "Xác nhận" → thành công
      └─ [Case 4: Thành công] → Success popup → "Đóng" → SCR-TK4-001
```

---

## 5. Non-Functional Requirements

- **Security:** Soft OTP lock sau 5 lần nhập sai — thông báo rõ ràng
- **Performance:** Form load instant (không call API cho đến khi submit)
- **Biometric fallback:** Hỗ trợ Soft OTP khi Facepay không khả dụng
- **Error handling:** Xử lý đầy đủ: giấy tờ hết hạn, chưa đăng ký, OTP sai

---

## 6. UX Signal Analysis (Phase 4e)

**Signals detected:**
- `"radio/check"` + `"radio/uncheck"` → selection pattern → only 2 options → correct use
- `"Soft OTP"` → security authentication → 6-cell input → banking OTP standard
- `"Facepay"` → biometric authentication → high trust requirement
- `"Lưu ý: Soft OTP sẽ bị khóa nếu nhập sai PIN 5 lần"` → security warning → prominent placement critical
- `"Thu thập sinh trắc học"` → onboarding dependency → user may not be enrolled → error path critical

**UX Laws triggered:**
- **Doherty Threshold:** 3 confirmation hops (select → confirm popup → OTP) → cognitive fatigue risk
- **Fitts' Law:** OTP 6-cell inputs spaced 59.8px gap → verify touch target accuracy
- **Error Prevention (Nielsen):** Popup "Huỷ | Đồng ý" — secondary action should be left/less prominent
