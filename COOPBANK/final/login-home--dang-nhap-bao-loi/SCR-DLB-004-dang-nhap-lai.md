# SCR-DLB-004 — Đăng nhập báo lỗi › Đăng nhập lại

**Module:** Đăng nhập báo lỗi  
**Screen ID:** SCR-DLB-004  
**Screen Type:** Form nhập thông tin  
**Figma Node:** `142:17417`  
**Wireframes:** `ui/re-login.png`

---

## Section 1: Screen Overview

Màn hình đăng nhập lại sau khi user đổi mật khẩu thành công. Base screen là form đăng nhập bằng số điện thoại. Có popup thông báo lỗi "Tài khoản hoặc mật khẩu không chính xác" — cho thấy trạng thái khi user thử đăng nhập nhưng fail.

---

## Section 2: Flow & Navigation

**Triggered by:** Đổi mật khẩu thành công (SCR-DLB-003) → noti "Đồng ý" → đăng nhập lại  
**Leads to:**
- → Home Dashboard (đăng nhập thành công)
- → SCR-DLB-004 (đăng nhập sai → popup lỗi → Đồng ý → thử lại)

**User Story:**
> Với tư cách là người dùng vừa đổi mật khẩu, tôi muốn được đưa đến màn hình đăng nhập lại ngay lập tức, để tôi có thể đăng nhập với mật khẩu mới và tiếp tục sử dụng dịch vụ.

**Non-Functional:**
- Đây là re-login sau password change — phải clear session cũ
- Error message không được tiết lộ thông tin về mật khẩu cũ
- Max 5 lần thử → lockout policy

---

## Section 3: Content Inventory (OCR)

**Background (form đăng nhập):**
- `Số điện thoại` (input label)
- Face ID icon (biometric option)

**Popup lỗi:**
- `Thông báo` (popup title)
- `Tài khoản hoặc mật khẩu của Quý khách không chính xác. Vui lòng đăng nhập lại` (popup body)
- `Đồng ý` (popup CTA)

---

## Section 4: UX Augmentation

### UX Signals Detected

| Signal | Text | UX Implication |
|---|---|---|
| `login-error` | "Tài khoản hoặc mật khẩu không chính xác" | Error feedback — tốt (generic để bảo mật) |
| `re-auth` | "Vui lòng đăng nhập lại" | Clear recovery instruction |
| `phone-login` | "Số điện thoại" | Different login method than SCR-DLB-001 (Face ID → Phone number) |
| `single-cta-popup` | "Đồng ý" | Acknowledge error → dismiss → retry |

### DDL UX inference
- **Error visibility (Nielsen):** Error message rõ ràng nhưng thiếu: attempt count ("còn X lần"), lockout warning
- **Security:** Generic error "Tài khoản hoặc mật khẩu không chính xác" — tốt (không tiết lộ which is wrong)
- **Consistency violation:** SCR-DLB-001 dùng saved credentials + Face ID, SCR-DLB-004 yêu cầu phone + password mới — context break có thể confuse user

---

## Section 5: Requirements & Gaps

### Functional Requirements
- [x] Error popup với message rõ ràng
- [x] Dismiss popup (Đồng ý)
- [x] Phone number login form
- [ ] Missing: Attempt counter / lockout warning
- [ ] Missing: "Quên mật khẩu?" link visible
- [ ] Missing: Clear transition message (vừa đổi MK thành công → đăng nhập với MK mới)

### UX Gaps (Preliminary)
1. **Context break:** User vừa đổi mật khẩu theo flow nhưng màn hình re-login lại yêu cầu Số điện thoại thay vì Face ID → inconsistency với SCR-DLB-001
2. **Không có transition message:** Sau khi đổi MK thành công, nên có dòng nhắc "Hãy đăng nhập với mật khẩu mới" để user không nhầm nhập MK cũ
3. **Attempt limit không visible** — best practice banking: hiện số lần còn lại
