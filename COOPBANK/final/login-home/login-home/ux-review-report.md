# UX Review Report — Co-opBank (Login-Home)

## Tổng quan
- Folder: coopbank/final/login-home
- Số màn hình: 4 | Tổng check: 42
- Pass: 28 | Gap: 9 | Unverifiable: 5
- UX Score (Simple): 67% (28/42)
- UX Score (Weighted): 100%

---


**Total checks:** 42  
**Pass:** 28 | **Gap:** 9 | **Unverifiable:** 5  
**Simple Score:** 67%  
**Weighted Score:** 67%## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Đăng nhập › Form đăng nhập |
|:---|:---|
| **Vấn đề** | Form đăng nhập (login-with-phone-number |
| **Gap ref** | Check #5 |
| **DDL** | UXG-04 · UXG-78 · Law:Nielsen #9 (Help users recognize, diagnose, and recover from errors) |
| **Giải pháp** | Thêm error state: border đỏ `{base.destructive}` + helper text "Mật khẩu không đúng. Bạn còn X lần thử."; Thêm alert khi tài khoản bị khóa: "Tài kh... |

---

#### UXP-002 · Critical
| **Màn hình** | Đăng nhập › Form đăng nhập |
|:---|:---|
| **Vấn đề** | Form login-with-phone-number |
| **Gap ref** | Check #6, Check #10 |
| **DDL** | UXG-10 · UXG-07 · Law:Fitts's Law |
| **Giải pháp** | Thêm floating label "Số điện thoại" trên field, fontSize `{text.sm.font-size}`, fontWeight `{font-weight.medium}`; Thêm floating label "Mật khẩu" t... |

---

#### UXP-003 · Major
| **Màn hình** | Trang chủ › Bảng điều khiển |
|:---|:---|
| **Vấn đề** | Trang chủ expanded (homepage-expand-2 |
| **Gap ref** | Check #6 |
| **DDL** | UXG-45 · UXG-12 · Law:Hick's Law |
| **Giải pháp** | Hiển thị 6 items "Hay dùng" mặc định + "Xem tất cả" CTA. User tùy chỉnh danh sách; Collapse mặc định, hiện 3 items + "Xem thêm (5)". Reduce cogniti... |

---

#### UXP-004 · Major
| **Màn hình** | Thông tin cá nhân › Chi tiết |
|:---|:---|
| **Vấn đề** | Màn hình basic-infor |
| **Gap ref** | Check #4, Check #6 |
| **DDL** | UXG-78 · UXG-55 · Law:Nielsen #7 (Flexibility and efficiency of use) |
| **Giải pháp** | Thêm "Yêu cầu cập nhật thông tin" → mở form request online (mô tả thay đổi + upload giấy tờ); Thêm "Gọi hotline 1900-xxxx" link trực tiếp; Thêm edi... |

---

#### UXP-005 · Major
| **Màn hình** | Cài đặt › Danh sách |
|:---|:---|
| **Vấn đề** | Mục "Thoát ứng dụng" trong settings |
| **Gap ref** | Check #6, Check #7 |
| **DDL** | UXG-04 · UXG-36 · Law:Nielsen #5 (Error prevention) |
| **Giải pháp** | Đổi màu text sang `{base.destructive}` (đỏ), thêm icon logout riêng biệt; Thêm divider trước "Thoát ứng dụng" để tách khỏi menu thông thường; Thêm ... |

---

#### UXP-006 · Minor
| **Màn hình** | Đăng nhập › Form đăng nhập |
|:---|:---|
| **Vấn đề** | Popup Touch ID (popup-touch-id |
| **Gap ref** | Check #10 |
| **DDL** | UXG-07 · Law:Jakob's Law |
| **Giải pháp** | Đổi thành "ATM/Chi nhánh" đầy đủ hoặc "Điểm GD" nếu cần ngắn; Cân nhắc thêm subtitle VN "Xác thực vân tay" bên dưới "Touch ID" để hỗ trợ user lớn tuổi |

---

#### UXP-007 · Minor
| **Màn hình** | Trang chủ › Bảng điều khiển |
|:---|:---|
| **Vấn đề** | Banner quảng cáo (homepage-shorten |
| **Gap ref** | Check #10 |
| **DDL** | UXG-52 · Law:Aesthetic-Usability Effect |
| **Giải pháp** | Thêm auto-scroll animation (3-5s interval) + swipe indicator (arrow hints); Tăng touch target ≥ 44×44px theo iOS HIG |

---

## Chi tiết theo màn hình

### 1. Đăng nhập › Form đăng nhập
> `SCR-LH-001` · login · 4 artboards
>
> **Score: 67% | Pass: 8 | Gap: 3 | Unverifiable: 1 | Images: login-with-phone-number.png, login-with-touch-id.png, login-with-face-id.png, popup-touch-id.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Login form hiển thị fields đăng nhập | Skill B: flow_checks | UXG-10 | Pass | login-with-phone-number.png — 2 fields: "Số điện thoại" + "Mật khẩu" visible |
| 2 | CTA "Đăng nhập" rõ ràng, vị trí dễ nhấn | Skill B: component_checks | UXG-52 | Pass | CTA button primary xanh, centered, width ~200px |
| 3 | Biometric authentication option hiển thị | Skill B: flow_checks | — | Pass | Touch ID icon (40×40) bên phải CTA, Face ID icon variant |
| 4 | Popup Touch ID có nội dung rõ ràng + dismiss | Skill B: flow_checks | UXG-36 | Pass | popup-touch-id.png — title + body text VN + "Hủy" button |
| 5 | Form có error state | Skill A: signal_inference | UXG-04 | Gap | Không có artboard error — thiếu sai mật khẩu, tài khoản bị khóa, network error |
| 6 | Form fields có label (không chỉ placeholder) | Skill C: vision | UXG-10 | Gap | Chỉ placeholder text, không có floating/fixed label trên field |
| 7 | Password field có eye toggle | Skill C: vision | — | Pass | Eye icon visible bên phải field Mật khẩu |
| 8 | Link "Quên mật khẩu?" accessible | Skill B: flow_checks | UXG-78 | Pass | Link blue, dưới CTA, text rõ ràng |
| 9 | Bottom bar tabs có touch targets đủ lớn | Skill C: vision | UXG-52 | Pass | 3 tabs Thông báo/Hỗ trợ/ATM·CN, kích thước hợp lý |
| 10 | Language consistency (VN/EN) | Skill C: vision | UXG-07 | Gap | "Touch ID" (EN) mixed với text VN khác |
| 11 | SĐT masked properly | Skill C: vision | UXG-55 | Pass | "090****882" — masked hợp lý |
| 12 | Loading/processing state cho đăng nhập | Skill A: signal_inference | UXG-78 | Unverifiable | Không thể verify từ ảnh tĩnh |

### 2. Trang chủ › Bảng điều khiển
> `SCR-LH-002` · dashboard · 5 artboards
>
> **Score: 67% | Pass: 8 | Gap: 2 | Unverifiable: 2 | Images: homepage-shorten.png, homepage-shortenhidden-balance.png, homepage-expand.png, homepage-expand-2.png, change-avt.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Thông tin tài khoản hiển thị (tên, STK, số dư) | Skill B: component_checks | — | Pass | "Nguyen Hoang Khai", "130099380022", "20,000,000 VND" visible |
| 2 | Số dư có toggle ẩn/hiện | Skill C: vision | UXG-55 | Pass | homepage-shortenhidden-balance.png — "********* VND" + eye icon |
| 3 | Quick actions (4 items) hiển thị rõ ràng | Skill B: component_checks | UXG-52 | Pass | 4 icons + labels: Tài khoản, Chuyển tiền, QR Pay, Nạp tiền |
| 4 | Banner có slider dots | Skill C: vision | — | Pass | 2 dots dưới banner |
| 5 | Navigation bar 5 tabs hiển thị đúng | Skill C: vision | bottom-tab-bar-1 | Pass | 5 tabs: Trang chủ (active), Tin tức, Dịch vụ QR, Thông báo (badge 12), Cài đặt |
| 6 | Information hierarchy cho 20+ service items | Skill C: vision | UXG-45 | Gap | Tất cả service items đồng nhất style, không phân biệt priority. Hick's Law violation |
| 7 | Change avatar overlay có close affordance | Skill C: vision | UXG-36 | Pass | change-avt.png — X close icon top-right |
| 8 | Change avatar options đầy đủ | Skill B: flow_checks | — | Pass | 3 options: Từ camera, Từ thư viện ảnh, Xóa ảnh |
| 9 | Notification badge hiển thị | Skill C: vision | — | Pass | Badge "12" on Thông báo tab |
| 10 | Banner CTA touch target ≥ 44px | Skill C: vision | UXG-52 | Gap | "Chi tiết" CTA trên banner nhỏ (~60×30), dưới 44px height |
| 11 | Empty state cho danh sách trống | Skill A: signal_inference | empty-state-1 | Unverifiable | Không có artboard empty state — không thể verify từ ảnh |
| 12 | Pull-to-refresh dashboard | Skill A: signal_inference | UXG-78 | Unverifiable | Không thể verify interaction từ ảnh tĩnh |

### 3. Cài đặt › Danh sách
> `SCR-LH-003` · settings · 2 artboards
>
> **Score: 70% | Pass: 7 | Gap: 2 | Unverifiable: 1 | Images: settings.png, settings-2.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Menu list hiển thị đầy đủ 9 items | Skill B: component_checks | — | Pass | settings.png — 9 menu items visible |
| 2 | Expandable section (Soft OTP) hoạt động | Skill C: vision | — | Pass | settings-2.png — Cấu hình Soft OTP expanded: 2 sub-items |
| 3 | Chevron indicator cho expandable items | Skill C: vision | UXG-12 | Pass | Chevron down icon cho Soft OTP và Quản lý danh bạ |
| 4 | "Thông tin cá nhân" link visible | Skill B: flow_checks | — | Pass | Link blue dưới tên user |
| 5 | Navigation bar Cài đặt tab active | Skill C: vision | bottom-tab-bar-1 | Pass | "Cài đặt" tab active (highlighted icon) |
| 6 | "Thoát ứng dụng" có visual differentiation | Skill C: vision | UXG-36 | Gap | Cùng style với các menu items thông thường, không có warning visual |
| 7 | "Thoát ứng dụng" có confirmation dialog | Skill A: signal_inference | UXG-04 | Gap | Không có artboard confirmation — destructive action thiếu safeguard |
| 8 | Menu icons nhất quán style | Skill C: vision | UXG-12 | Pass | Tất cả icons cùng size, style outline |
| 9 | Touch targets menu items ≥ 44px | Skill C: vision | UXG-52 | Pass | Mỗi menu item full-width, height ước lượng ≥ 48px |
| 10 | Scroll indicator khi nội dung dài | Skill C: vision | UXG-45 | Unverifiable | settings-2.png — "Thoát ứng dụng" bị cắt bottom, nhưng không thể confirm scroll behavior |

### 4. Thông tin cá nhân › Chi tiết
> `SCR-LH-004` · detail · 1 artboard
>
> **Score: 63% | Pass: 5 | Gap: 2 | Unverifiable: 1 | Images: basic-infor.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header có back arrow + title | Skill C: vision | app-header-1 | Pass | Back arrow + "Thông tin cá nhân" header |
| 2 | 6 fields thông tin hiển thị đầy đủ | Skill B: component_checks | — | Pass | Tên ĐN, Ngày sinh, CMND, Ngày cấp, Địa chỉ, Email — đủ 6 |
| 3 | Username masked mặc định | Skill C: vision | UXG-55 | Pass | "●●●●●●●●●●" + eye toggle icon |
| 4 | PII (CMND, ngày sinh) hiển thị rõ ràng | Skill C: vision | UXG-55 | Gap | CMND "012547288" và ngày sinh "12/05/1981" hiển thị plaintext, không có option ẩn |
| 5 | Footnote hướng dẫn cập nhật | Skill C: vision | — | Pass | Footnote text hướng dẫn liên hệ chi nhánh visible |
| 6 | CTA để yêu cầu cập nhật thông tin | Skill B: flow_checks | UXG-78 | Gap | Chỉ có footnote text, không có button hay link actionable |
| 7 | Fields read-only có visual indicator | Skill C: vision | UXG-12 | Pass | Tất cả fields hiển thị dạng text (không có input border editable) |
| 8 | Email format validation display | Skill C: vision | — | Unverifiable | Read-only, không thể verify validation |

---

## DDL References sử dụng

| ddl_ref | Rule | UX Law | Áp dụng |
|---------|------|--------|---------|
| UXG-04 | Error Recovery — cung cấp phản hồi lỗi rõ ràng | Nielsen #9 | SCR-LH-001 (login error), SCR-LH-003 (logout confirm) |
| UXG-07 | Language Consistency — tránh mixed language | Jakob's Law | SCR-LH-001 (Touch ID EN/VN mixed) |
| UXG-10 | Form Label — mọi input phải có label rõ ràng | WCAG 2.1 AA | SCR-LH-001 (placeholder-only) |
| UXG-12 | Visual Feedback — trạng thái tương tác rõ ràng | — | SCR-LH-003 (chevrons), SCR-LH-004 (read-only indicator) |
| UXG-36 | Destructive Action Safeguard — xác nhận trước hành động xóa/thoát | Nielsen #5 | SCR-LH-003 (Thoát ứng dụng) |
| UXG-45 | Information Hierarchy — phân cấp nội dung rõ ràng | Hick's Law | SCR-LH-002 (service grid) |
| UXG-52 | Touch Target — vùng chạm ≥ 44×44px | Fitts's Law | SCR-LH-002 (banner CTA) |
| UXG-55 | Privacy — mask/ẩn thông tin nhạy cảm | — | SCR-LH-001 (SĐT), SCR-LH-004 (CMND exposed) |
| UXG-78 | Action Availability — cung cấp CTA cho task khả thi | Nielsen #7 | SCR-LH-004 (thiếu CTA cập nhật) |
