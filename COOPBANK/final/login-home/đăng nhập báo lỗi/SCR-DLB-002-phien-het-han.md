# SCR-DLB-002 — Đăng nhập báo lỗi › Lỗi - Phiên hết hạn

**Module:** Đăng nhập báo lỗi  
**Screen ID:** SCR-DLB-002  
**Screen Type:** Lỗi (error)  
**Figma Node:** `142:17221`, `142:17291`  
**Wireframes:** `ui/login-expired.png`, `ui/login-expired-2.png`

---

## Section 1: Screen Overview

Popup "Phiên đăng nhập hết hạn" xuất hiện ngay trên màn hình chính (Home Dashboard) khi session user hết hạn trong lúc đang sử dụng app. User được yêu cầu nhập lại mật khẩu nhanh để tiếp tục mà không cần rời trang hiện tại.

**2 states:**
| State | Mô tả |
|---|---|
| Base | Popup phiên hết hạn với form nhập mật khẩu nhanh |
| Keyboard state | Bàn phím iOS mở khi đang nhập mật khẩu |

**Context đặc biệt:** Màn hình chính (Home) vẫn visible phía sau popup, user thấy balance (20,000,000 VND) và shortcuts (Chuyển tiền, QR Pay).

---

## Section 2: Flow & Navigation

**Triggered by:** Session timeout while app is in use  
**Leads to:**
- → SCR-DLB-001 (Bỏ qua — user bị đăng xuất)
- → Home (Tiếp tục — xác thực thành công)
- → SCR-DLB-003 (nếu cần đổi mật khẩu)

**User Story:**
> Với tư cách là người dùng đang sử dụng app, khi phiên đăng nhập hết hạn, tôi muốn có thể xác thực lại nhanh chóng mà không mất đi ngữ cảnh đang làm việc, để tôi không phải điều hướng lại từ đầu.

**Non-Functional:**
- Session timeout phải có thông báo rõ ràng và kịp thời
- Blur background phải đủ để không đọc được data nhạy cảm phía sau
- Quick re-auth phải hoàn thành trong < 5 giây

---

## Section 3: Content Inventory (OCR)

**Popup content:**
- `Phiên đăng nhập hết hạn. Quý khách vui lòng đăng nhập lại.` (title + body)
- `Nhập mật khẩu` (input placeholder)
- `Bỏ qua` (secondary CTA)
- `Tiếp tục` (primary CTA)

**Background visible (không interactive):**
- `20,000,000 VND` (user balance)
- `Chuyển tiền`, `QR Pay` (home shortcuts)

**Keyboard state (login-expired-2):**
- `●●●●●●●●●●` (password dots — đang nhập)
- `Phiên đăng nhập hết hạn` (reduced title)
- iOS keyboard rows visible

---

## Section 4: UX Augmentation

### UX Signals Detected

| Signal | Text | UX Implication |
|---|---|---|
| `session-error` | "Phiên đăng nhập hết hạn" | Error state — cần clear indicator + recovery path |
| `quick-reauth` | "Nhập mật khẩu", "Tiếp tục" | Inline re-auth pattern — giữ user context |
| `dismissable` | "Bỏ qua" | User có lựa chọn thoát — good for autonomy |
| `context-preservation` | Home visible behind popup | User thấy context → reduce anxiety |
| `masked-input` | "●●●●●●●●●●" | Password masking during input — expected |

### DDL UX inference
- **Doherty Threshold:** Quick re-auth phải feedback < 400ms để không break flow
- **Fitts's Law:** "Tiếp tục" là primary action — phải to hơn "Bỏ qua" có thể nhầm
- **Error prevention:** Blur background không hoàn toàn che balance data

---

## Section 5: Requirements & Gaps

### Functional Requirements
- [x] Popup hiển thị đúng context (phiên hết hạn)
- [x] Quick password re-entry field
- [x] Dismiss option (Bỏ qua)
- [x] Continue option (Tiếp tục)
- [ ] Missing: Face ID option for quick re-auth (thấy trong SCR-DLB-001 nhưng không rõ có trong popup này không)
- [ ] Missing: Forgot password link

### UX Gaps (Preliminary)
1. **Balance visible behind blur** — `20,000,000 VND` vẫn có thể đọc → security risk nếu shoulder surfing
2. **Single CTA pair** (Bỏ qua/Tiếp tục) — thiếu Face ID quick re-auth mặc dù màn hình login chính có Face ID
3. **No error state shown** — Nếu nhập sai mật khẩu thì popup thay đổi như thế nào? (không có trong design)
