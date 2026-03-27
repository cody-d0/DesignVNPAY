# SCR-DLB-001 — Đăng nhập báo lỗi › Form nhập thông tin

**Module:** Đăng nhập báo lỗi  
**Screen ID:** SCR-DLB-001  
**Screen Type:** Form nhập thông tin (auth)  
**Figma Node:** `142:17053` (base) + overlays: `142:17187`, `142:17362`, `142:17085`, `142:17119`, `142:17153`  
**Wireframes:** `ui/login-with-face-id.png`, `ui/popup.png`, `ui/popup-2.png`, `ui/popup-3.png`, `ui/popup-4.png`, `ui/noti.png`

---

## Section 1: Screen Overview

Màn hình đăng nhập chính của Co-opBank Mobile Banking dành cho user đã lưu thông tin đăng nhập. Hỗ trợ đăng nhập bằng Face ID. Màn hình có **6 states/variants**:

| State | Mô tả | Trigger |
|---|---|---|
| Base | Đăng nhập với Face ID, thông tin lưu sẵn | App launch |
| Popup cập nhật bắt buộc | Yêu cầu cập nhật app ngay | Version check fail |
| Popup cập nhật tùy chọn | Gợi ý cập nhật phiên bản mới | New version available |
| Popup mật khẩu hết hạn (đổi PIN) | Mật khẩu hết hạn, cần đổi | Password expiry policy |
| Popup mật khẩu hết hạn (quầy) | Mật khẩu kích hoạt hết hạn → ra quầy | Activation password expiry |
| Noti đổi mật khẩu thành công | Xác nhận sau khi đổi MK thành công | Post-change |

---

## Section 2: Flow & Navigation

**Triggered by:** App launch, biometric auth, session re-entry  
**Leads to:**
- → SCR-DLB-002 (nếu phiên hết hạn khi đăng nhập)
- → SCR-DLB-001 (overlays — popup/noti variants)
- → Home Dashboard (đăng nhập thành công)

**User Story:**
> Với tư cách là người dùng đã đăng ký Co-opBank Mobile Banking, tôi muốn đăng nhập nhanh chóng bằng Face ID hoặc mật khẩu, để có thể truy cập dịch vụ ngân hàng mà không cần nhập lại thông tin.

**Non-Functional:**
- Đăng nhập phải hoàn thành trong < 3 giây
- Thông tin nhạy cảm (số điện thoại) phải được mask
- Face ID phải tuân thủ platform security guidelines (iOS LocalAuthentication)
- Popup thông báo phải respectful — không block user quá lâu

---

## Section 3: Content Inventory (OCR)

**Base Login Screen:**
- `Co-opBank` (logo header)
- `Nguyen Hoang Khai` (tên user đã lưu)
- `090****882` (số điện thoại masked)
- `Mật khẩu` (input label)
- `Đăng nhập` (primary CTA)
- `Quên mật khẩu?` (secondary link)
- `Gói vay hỗ trợ mua nhà của Co-opBank` (banner ad)
- `Chi tiết` (banner link)
- `Thông báo` / `Hỗ trợ` / `ATM/CN` (bottom nav)

**Popup variants:**
- Popup 1 (bắt buộc cập nhật): *"Quý khách vui lòng cập nhật ứng dụng trước khi tiếp tục sử dụng dịch vụ"* → **Cập nhật**
- Popup 2 (tùy chọn cập nhật): *"Hiện ứng dụng đã có phiên bản mới với nhiều tính năng ưu việt..."* → **Để sau** | **Cập nhật**
- Popup 3 (MK hết hạn, đổi MK): *"Mật khẩu hiện tại của Quý khách đã hết hạn sử dụng theo quy định của Co-opBank. Đề nghị Quý khách thay đổi mật khẩu mới...Thời hạn hiệu lực 06 tháng..."* → **Cài mã PIN**
- Popup 4 (MK kích hoạt hết hạn): *"Mật khẩu kích hoạt đã hết hạn...vui lòng đến Quầy giao dịch gần nhất"* → **Cài mã PIN**
- Noti (đổi MK thành công): *"Đổi mật khẩu thành công. Quý khách vui lòng đăng nhập lại"* → **Đồng ý**

---

## Section 4: UX Augmentation

### UX Signals Detected

| Signal | Text | UX Implication |
|---|---|---|
| `auth` | "Đăng nhập", "Mật khẩu" | Primary auth flow — Fitts's Law: login button phải dễ tap |
| `biometric` | Face ID biometric icon | Convenience auth — reduce friction với returning users |
| `security` | "Đổi mật khẩu", "Mật khẩu hết hạn" | Security enforcement — trust-first pattern |
| `masked-pii` | "090****882" | Privacy by default — PDPA compliance |
| `forced-update` | "cập nhật ứng dụng trước khi tiếp tục" | Forced gate — high friction, risk of abandonment |
| `optional-update` | "Để sau" | Respectful nudge — user retains control |
| `branch-visit` | "đến Quầy giao dịch gần nhất" | Channel escalation — digital barrier, poor UX |

### DDL UX Signal inference (Phase 4e)
- **Security-first pattern:** COMP:login-form phải có loading state sau submit
- **Error recovery:** Popup với single CTA (chỉ "Cài mã PIN") có thể confuse user không biết có option nào khác
- **Fitts's Law:** Face ID button (40×40) cách login button — touch target audit cần thiết

---

## Section 5: Requirements & Gaps

### Functional Requirements
- [x] User name và phone number masked hiển thị đúng
- [x] Face ID integration
- [x] Multiple popup states handled
- [ ] Missing: "Đổi người dùng" option (user bị trap với saved account)
- [ ] Missing: Error count / lockout behavior not shown

### UX Gaps (Preliminary — sẽ được Skill C verify)
1. **Popup 3 & 4 đều show "Cài mã PIN"** — nhưng context khác nhau (đổi MK vs ra quầy). CTA misleading nếu popup 4 không thực sự dẫn đến flow PIN
2. **Dismiss option cho popup bắt buộc cập nhật (popup 1)** — không thấy nút "X" → user bị forced với 0 control
3. **Banner quảng cáo on login screen** — questionable UX priority cho auth flow
