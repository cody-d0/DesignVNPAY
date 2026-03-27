# SCR-DLB-003 — Đăng nhập báo lỗi › Đặt lại mật khẩu

**Module:** Đăng nhập báo lỗi  
**Screen ID:** SCR-DLB-003  
**Screen Type:** Form nhập thông tin  
**Figma Node:** `142:17396`  
**Wireframes:** `ui/change-password.png`

---

## Section 1: Screen Overview

Form đổi mật khẩu bắt buộc khi mật khẩu của user đã hết hạn (theo policy Co-opBank — 6 tháng). User phải nhập mật khẩu cũ + mật khẩu mới + xác nhận mật khẩu mới, và tuân thủ các điều kiện đặt mật khẩu được hiển thị inline.

---

## Section 2: Flow & Navigation

**Triggered by:** Popup mật khẩu hết hạn (SCR-DLB-001, popup-3) → "Cài mã PIN"  
**Leads to:**
- → SCR-DLB-004 (Tiếp tục → đổi mật khẩu thành công → đăng nhập lại)
- → SCR-DLB-001 (Back → hủy flow)

**User Story:**
> Với tư cách là người dùng có mật khẩu đã hết hạn, tôi muốn được hướng dẫn rõ ràng để tạo mật khẩu mới an toàn, để có thể tiếp tục sử dụng dịch vụ ngân hàng mà không cần ra quầy.

**Non-Functional:**
- Điều kiện mật khẩu phải validate real-time khi user nhập
- Mật khẩu mới phải khác mật khẩu cũ (policy banking)
- Không được lưu mật khẩu vào clipboard hoặc autofill

---

## Section 3: Content Inventory (OCR)

**Header:**
- `Đổi mật khẩu` (screen title)
- Back arrow icon (quay lại)

**Form fields:**
- `Mật khẩu cũ` (input 1)
- `Mật khẩu mới` (input 2)  
- `Nhập lại mật khẩu mới` (input 3)
- Eye icon (×3) — ẩn/hiện mật khẩu

**Điều kiện section:**
- `Điều kiện đặt mật khẩu` (section header)
- `Mật khẩu có độ dài từ 8-20 ký tự`
- `Mật khẩu chứa ít nhất 01 ký tự số, 01 ký tự chữ và 01 ký tự đặc biệt. Ví dụ: abc@1234; a&123456; 12345678a$...`

**CTA:**
- `Tiếp tục` (primary button, bottom)

---

## Section 4: UX Augmentation

### UX Signals Detected

| Signal | Text | UX Implication |
|---|---|---|
| `security-form` | "Mật khẩu cũ", "Mật khẩu mới" | Password change pattern — verify+set |
| `validation-rules` | "8-20 ký tự", "ký tự số, chữ, đặc biệt" | Inline guidance — reduces errors |
| `eye-toggle` | Eye icon ×3 | User control over visibility — good |
| `mandatory-change` | Context từ popup mật khẩu hết hạn | Forced task — UX phải friction-free |
| `confirmation-field` | "Nhập lại mật khẩu mới" | Error prevention — confirm identity |

### DDL UX inference
- **Miller's Law:** 3 input fields là vừa phải — không overload
- **Error prevention (Nielsen):** Rules section giúp user nhập đúng ngay lần đầu
- **Real-time validation expected:** Rule checkmarks nên update khi user nhập
- **Banking NFR:** Field "Mật khẩu cũ" phải có rate-limiting để chống brute force

---

## Section 5: Requirements & Gaps

### Functional Requirements
- [x] 3 password fields với eye toggle
- [x] Password rules displayed inline
- [x] Single primary CTA (Tiếp tục)
- [x] Back navigation
- [ ] Missing: Real-time validation indicators (checkmarks per rule)
- [ ] Missing: Password strength indicator
- [ ] Missing: Error state when passwords don't match

### UX Gaps (Preliminary)
1. **Static rules** — Điều kiện không có visual feedback (checkmark/X) khi user nhập → violated Feedback principle (Nielsen)
2. **CTA label "Cài mã PIN" trong popup nhưng screen tên "Đổi mật khẩu"** — terminology inconsistency
3. **Không có password strength meter** — user không biết mật khẩu của mình có đủ mạnh không
