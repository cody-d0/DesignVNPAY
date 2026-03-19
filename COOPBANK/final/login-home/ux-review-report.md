# UX Review Report — Co-opBank (Login-Home)

## Tổng quan
- Folder: coopbank/final/login-home
- Số màn hình: 4 | Tổng check: 42
- Pass: 28 | Gap: 9 | Unverifiable: 5
- UX Score (Simple): 67% (28/42)
- UX Score (Weighted): 100%

---

## Đề xuất cải tiến (Priority)

### 🔴 Critical

#### UXP-001 · 🔴 Critical

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Đăng nhập › Form đăng nhập |
| **Mức độ** | 🔴 Critical |
| **DDL** | UXG-04 · UXG-78 |
| **UX Law** | Nielsen #9 (Help users recognize, diagnose, and recover from errors) |

**🔍 Hiện trạng**

Form đăng nhập (login-with-phone-number.png, login-with-touch-id.png) không hiển thị bất kỳ trạng thái lỗi nào: sai mật khẩu, tài khoản bị khóa, mạng lỗi, hoặc quá số lần thử. Không có error state nào trong 4 artboards của biên SCR-LH-001.

> Evidence: Xem xét 4 artboards login — chỉ có happy path (form trống, form đã điền, popup Touch ID). Không có variant error nào. DDL text-input-1 schema yêu cầu `state.error` field.

**⚠️ Hậu quả**

- **User impact:** User nhập sai mật khẩu không biết lý do (sai mật khẩu? tài khoản bị khóa? hệ thống lỗi?), gây frustration và task failure
- **Business impact:** Tăng tải support hotline, tăng tỷ lệ "Quên mật khẩu" không cần thiết, giảm conversion
- **Violation:** DDL text-input-1 schema `state.error` — thiếu error state; UXG-04: Error Recovery; Nielsen #9

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Text input (Mật khẩu) | Thêm error state: border đỏ `{base.destructive}` + helper text "Mật khẩu không đúng. Bạn còn X lần thử." | Dưới field Mật khẩu |
| 2 | Alert banner | Thêm alert khi tài khoản bị khóa: "Tài khoản đã bị khóa sau 5 lần thử sai. Vui lòng liên hệ hotline 1900-xxxx." | Trên form, full-width |
| 3 | Toast / Snackbar | Thêm network error feedback: "Không thể kết nối. Vui lòng kiểm tra mạng." | Top notification |

---

#### UXP-002 · 🔴 Critical

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Đăng nhập › Form đăng nhập |
| **Mức độ** | 🔴 Critical |
| **DDL** | UXG-10 · UXG-07 |
| **UX Law** | Fitts's Law |

**🔍 Hiện trạng**

Form login-with-phone-number.png không có label cho field "Số điện thoại" và "Mật khẩu" — chỉ dùng placeholder text. Khi user bắt đầu nhập, placeholder biến mất, user mất context về field đang nhập. DDL text-input-1 schema yêu cầu `overridable.label`.

> Evidence: OCR tại login-with-phone-number.png — "Số điện thoại" và "Mật khẩu" là placeholder, không phải label. DDL text-input-1 layout yêu cầu `label-row` node hiển thị label trên input.

**⚠️ Hậu quả**

- **User impact:** Accessibility fail — screen reader không đọc được label; user quên mình đang nhập field nào khi placeholder ẩn
- **Business impact:** WCAG 2.1 AA non-compliance; accessibility audit failure
- **Violation:** UXG-10 (Form Label); UXG-07 (Accessibility); DDL text-input-1 `overridable.label`

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Text input (Số điện thoại) | Thêm floating label "Số điện thoại" trên field, fontSize `{text.sm.font-size}`, fontWeight `{font-weight.medium}` | Trên input field |
| 2 | Text input (Mật khẩu) | Thêm floating label "Mật khẩu" trên field | Trên input field |

---

### 🟡 Major

#### UXP-003 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Trang chủ › Bảng điều khiển |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-45 · UXG-12 |
| **UX Law** | Hick's Law |

**🔍 Hiện trạng**

Trang chủ expanded (homepage-expand-2.png) hiển thị tổng cộng 20+ service items trong 3 sections (Tài chính: 6, Mua sắm: 8, Tiện ích: 6) mà không có bất kỳ hierarchy visual nào — tất cả đều icon grid 3 cột đồng nhất kích thước và style.

> Evidence: OCR homepage-expand-2.png — 3 section titles + 20 service items. Tất cả icon cùng kích thước, cùng style grid 3 cột. Không có featured item, không có "Xem thêm" collapse.

**⚠️ Hậu quả**

- **User impact:** Cognitive overload (Hick's Law) — quá nhiều lựa chọn cùng cấp gây decision paralysis. User khó tìm dịch vụ cần dùng thường xuyên.
- **Business impact:** Giảm engagement với dịch vụ ít phổ biến; tăng time-to-task; giảm feature discovery hiệu quả
- **Violation:** UXG-45 (Information Hierarchy); Hick's Law (thời gian quyết định tăng logarithmic theo số lựa chọn)

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Service grid | Hiển thị 6 items "Hay dùng" mặc định + "Xem tất cả" CTA. User tùy chỉnh danh sách | Body section Tài chính |
| 2 | Mua sắm / Tiện ích | Collapse mặc định, hiện 3 items + "Xem thêm (5)". Reduce cognitive load | Sections phụ |
| 3 | Quick Actions bar | Cho phép user tùy chỉnh 4 quick actions (drag-and-drop reorder) | Action bar area |

---

#### UXP-004 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Thông tin cá nhân › Chi tiết |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-78 · UXG-55 |
| **UX Law** | Nielsen #7 (Flexibility and efficiency of use) |

**🔍 Hiện trạng**

Màn hình basic-infor.png hiển thị 6 fields thông tin khách hàng dạng read-only, KHÔNG có bất kỳ CTA nào để yêu cầu cập nhật trực tuyến. Footnote chỉ ghi "liên hệ Điểm giao dịch Co-opBank" — bắt user phải đến chi nhánh offline.

> Evidence: OCR basic-infor.png footnote: "Nếu các thông tin chưa chính xác. Quý khách vui lòng liên hệ các Điểm giao dịch Co-opBank để cập nhật điều chỉnh". Không có button "Yêu cầu cập nhật" hay "Gọi hotline".

**⚠️ Hậu quả**

- **User impact:** Friction cao — user phải offline effort để cập nhật email/địa chỉ. Task abandonment rate cao.
- **Business impact:** Tăng trải nghiệm tiêu cực; dữ liệu KH lỗi thời (email sai → không gửi được thông báo → miss marketing revenue)
- **Violation:** UXG-78 (Action Availability); Nielsen #7 (cung cấp shortcut cho task phổ biến)

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | CTA button | Thêm "Yêu cầu cập nhật thông tin" → mở form request online (mô tả thay đổi + upload giấy tờ) | Dưới footnote |
| 2 | Contact shortcut | Thêm "Gọi hotline 1900-xxxx" link trực tiếp | Dưới footnote, bên cạnh CTA |
| 3 | Edit icon | Thêm edit icon nhỏ bên cạnh các field cho phép thay đổi (Email, Địa chỉ) để indicate editable possibility | Bên phải mỗi field |

---

#### UXP-005 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Cài đặt › Danh sách |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-04 · UXG-36 |
| **UX Law** | Nielsen #5 (Error prevention) |

**🔍 Hiện trạng**

Mục "Thoát ứng dụng" trong settings.png nằm cuối danh sách menu, cùng style và kích thước với các mục khác (Hỗ trợ, ATM/Chi nhánh). Không có separator, không có warning icon, không có confirmation state.

> Evidence: OCR settings.png — "Thoát ứng dụng" là menu-item cuối cùng, style đồng nhất: icon + text, không khác biệt visual. Không có artboard nào cho confirmation dialog "Bạn có chắc muốn thoát?".

**⚠️ Hậu quả**

- **User impact:** Mistouch → đăng xuất bất ngờ → phải đăng nhập lại = time waste + frustration
- **Business impact:** Tăng session loss; tăng hỗ trợ "tôi bị logout"
- **Violation:** UXG-04 (Error Recovery — destructive action thiếu confirm); UXG-36 (Destructive Action Safeguard); Nielsen #5

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Menu item "Thoát" | Đổi màu text sang `{base.destructive}` (đỏ), thêm icon logout riêng biệt | Cuối danh sách |
| 2 | Separator | Thêm divider trước "Thoát ứng dụng" để tách khỏi menu thông thường | Trước item cuối |
| 3 | Confirmation dialog | Thêm confirm dialog: "Bạn có chắc muốn thoát ứng dụng?" + CTA "Thoát" (destructive) + "Hủy" | Modal overlay |

---

### ⚪ Minor

#### UXP-006 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Đăng nhập › Form đăng nhập |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-07 |
| **UX Law** | Jakob's Law |

**🔍 Hiện trạng**

Popup Touch ID (popup-touch-id.png) hiển thị nội dung mô tả bằng tiếng Việt nhưng title "Touch ID" vẫn để English. Bottom bar đăng nhập có "ATM/CN" — viết tắt không rõ nghĩa cho user mới.

> Evidence: OCR popup-touch-id.png — "Touch ID" (EN) + "Vui lòng chạm vào cảm biến..." (VN). OCR login screens — "ATM/CN" — abbreviation.

**⚠️ Hậu quả**

- **User impact:** Consistency nhỏ — user lớn tuổi có thể không hiểu "Touch ID" hoặc "ATM/CN"
- **Business impact:** Nhỏ — nhưng ảnh hưởng inclusivity
- **Violation:** UXG-07 (Language Consistency — mixed EN/VN)

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Tab "ATM/CN" | Đổi thành "ATM/Chi nhánh" đầy đủ hoặc "Điểm GD" nếu cần ngắn | Bottom bar |
| 2 | Popup title | Cân nhắc thêm subtitle VN "Xác thực vân tay" bên dưới "Touch ID" để hỗ trợ user lớn tuổi | Overlay popup |

---

#### UXP-007 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Trang chủ › Bảng điều khiển |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-52 |
| **UX Law** | Aesthetic-Usability Effect |

**🔍 Hiện trạng**

Banner quảng cáo (homepage-shorten.png) "Mùa Giáng sinh ấm áp cùng Co-opBank" chiếm không gian lớn trên trang chủ nhưng chỉ có dot slider indicator (2 dots), không có swipe hint hoặc auto-scroll indicator. CTA "Chi tiết" trên banner login nhỏ, khó nhấn.

> Evidence: OCR homepage-shorten.png — banner area ~30% viewport height, dot slider 2 dots, CTA "Chi tiết" nhỏ khoảng 60×30px.

**⚠️ Hậu quả**

- **User impact:** User có thể không nhận ra banner có thể swipe; CTA nhỏ khó tap trên mobile
- **Business impact:** Banner campaign reach giảm nếu user không tương tác
- **Violation:** UXG-52 (Touch Target); Fitts's Law (target nhỏ)

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Banner slider | Thêm auto-scroll animation (3-5s interval) + swipe indicator (arrow hints) | Banner area |
| 2 | CTA "Chi tiết" | Tăng touch target ≥ 44×44px theo iOS HIG | Trên banner |

---

## Chi tiết theo màn hình

### 1. Đăng nhập › Form đăng nhập
> `SCR-LH-001` · login · 4 artboards
>
> **Score: 67% | Pass: 8 | Gap: 3 | Unverifiable: 1 | Images: login-with-phone-number.png, login-with-touch-id.png, login-with-face-id.png, popup-touch-id.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Login form hiển thị fields đăng nhập | Skill B: flow_checks | UXG-10 | ✅ Pass | login-with-phone-number.png — 2 fields: "Số điện thoại" + "Mật khẩu" visible |
| 2 | CTA "Đăng nhập" rõ ràng, vị trí dễ nhấn | Skill B: component_checks | UXG-52 | ✅ Pass | CTA button primary xanh, centered, width ~200px |
| 3 | Biometric authentication option hiển thị | Skill B: flow_checks | — | ✅ Pass | Touch ID icon (40×40) bên phải CTA, Face ID icon variant |
| 4 | Popup Touch ID có nội dung rõ ràng + dismiss | Skill B: flow_checks | UXG-36 | ✅ Pass | popup-touch-id.png — title + body text VN + "Hủy" button |
| 5 | Form có error state | Skill A: signal_inference | UXG-04 | ❌ Gap | Không có artboard error — thiếu sai mật khẩu, tài khoản bị khóa, network error |
| 6 | Form fields có label (không chỉ placeholder) | Skill C: vision | UXG-10 | ❌ Gap | Chỉ placeholder text, không có floating/fixed label trên field |
| 7 | Password field có eye toggle | Skill C: vision | — | ✅ Pass | Eye icon visible bên phải field Mật khẩu |
| 8 | Link "Quên mật khẩu?" accessible | Skill B: flow_checks | UXG-78 | ✅ Pass | Link blue, dưới CTA, text rõ ràng |
| 9 | Bottom bar tabs có touch targets đủ lớn | Skill C: vision | UXG-52 | ✅ Pass | 3 tabs Thông báo/Hỗ trợ/ATM·CN, kích thước hợp lý |
| 10 | Language consistency (VN/EN) | Skill C: vision | UXG-07 | ❌ Gap | "Touch ID" (EN) mixed với text VN khác |
| 11 | SĐT masked properly | Skill C: vision | UXG-55 | ✅ Pass | "090****882" — masked hợp lý |
| 12 | Loading/processing state cho đăng nhập | Skill A: signal_inference | UXG-78 | ⚠️ Unverifiable | Không thể verify từ ảnh tĩnh |

### 2. Trang chủ › Bảng điều khiển
> `SCR-LH-002` · dashboard · 5 artboards
>
> **Score: 67% | Pass: 8 | Gap: 2 | Unverifiable: 2 | Images: homepage-shorten.png, homepage-shortenhidden-balance.png, homepage-expand.png, homepage-expand-2.png, change-avt.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Thông tin tài khoản hiển thị (tên, STK, số dư) | Skill B: component_checks | — | ✅ Pass | "Nguyen Hoang Khai", "130099380022", "20,000,000 VND" visible |
| 2 | Số dư có toggle ẩn/hiện | Skill C: vision | UXG-55 | ✅ Pass | homepage-shortenhidden-balance.png — "********* VND" + eye icon |
| 3 | Quick actions (4 items) hiển thị rõ ràng | Skill B: component_checks | UXG-52 | ✅ Pass | 4 icons + labels: Tài khoản, Chuyển tiền, QR Pay, Nạp tiền |
| 4 | Banner có slider dots | Skill C: vision | — | ✅ Pass | 2 dots dưới banner |
| 5 | Navigation bar 5 tabs hiển thị đúng | Skill C: vision | bottom-tab-bar-1 | ✅ Pass | 5 tabs: Trang chủ (active), Tin tức, Dịch vụ QR, Thông báo (badge 12), Cài đặt |
| 6 | Information hierarchy cho 20+ service items | Skill C: vision | UXG-45 | ❌ Gap | Tất cả service items đồng nhất style, không phân biệt priority. Hick's Law violation |
| 7 | Change avatar overlay có close affordance | Skill C: vision | UXG-36 | ✅ Pass | change-avt.png — X close icon top-right |
| 8 | Change avatar options đầy đủ | Skill B: flow_checks | — | ✅ Pass | 3 options: Từ camera, Từ thư viện ảnh, Xóa ảnh |
| 9 | Notification badge hiển thị | Skill C: vision | — | ✅ Pass | Badge "12" on Thông báo tab |
| 10 | Banner CTA touch target ≥ 44px | Skill C: vision | UXG-52 | ❌ Gap | "Chi tiết" CTA trên banner nhỏ (~60×30), dưới 44px height |
| 11 | Empty state cho danh sách trống | Skill A: signal_inference | empty-state-1 | ⚠️ Unverifiable | Không có artboard empty state — không thể verify từ ảnh |
| 12 | Pull-to-refresh dashboard | Skill A: signal_inference | UXG-78 | ⚠️ Unverifiable | Không thể verify interaction từ ảnh tĩnh |

### 3. Cài đặt › Danh sách
> `SCR-LH-003` · settings · 2 artboards
>
> **Score: 70% | Pass: 7 | Gap: 2 | Unverifiable: 1 | Images: settings.png, settings-2.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Menu list hiển thị đầy đủ 9 items | Skill B: component_checks | — | ✅ Pass | settings.png — 9 menu items visible |
| 2 | Expandable section (Soft OTP) hoạt động | Skill C: vision | — | ✅ Pass | settings-2.png — Cấu hình Soft OTP expanded: 2 sub-items |
| 3 | Chevron indicator cho expandable items | Skill C: vision | UXG-12 | ✅ Pass | Chevron down icon cho Soft OTP và Quản lý danh bạ |
| 4 | "Thông tin cá nhân" link visible | Skill B: flow_checks | — | ✅ Pass | Link blue dưới tên user |
| 5 | Navigation bar Cài đặt tab active | Skill C: vision | bottom-tab-bar-1 | ✅ Pass | "Cài đặt" tab active (highlighted icon) |
| 6 | "Thoát ứng dụng" có visual differentiation | Skill C: vision | UXG-36 | ❌ Gap | Cùng style với các menu items thông thường, không có warning visual |
| 7 | "Thoát ứng dụng" có confirmation dialog | Skill A: signal_inference | UXG-04 | ❌ Gap | Không có artboard confirmation — destructive action thiếu safeguard |
| 8 | Menu icons nhất quán style | Skill C: vision | UXG-12 | ✅ Pass | Tất cả icons cùng size, style outline |
| 9 | Touch targets menu items ≥ 44px | Skill C: vision | UXG-52 | ✅ Pass | Mỗi menu item full-width, height ước lượng ≥ 48px |
| 10 | Scroll indicator khi nội dung dài | Skill C: vision | UXG-45 | ⚠️ Unverifiable | settings-2.png — "Thoát ứng dụng" bị cắt bottom, nhưng không thể confirm scroll behavior |

### 4. Thông tin cá nhân › Chi tiết
> `SCR-LH-004` · detail · 1 artboard
>
> **Score: 63% | Pass: 5 | Gap: 2 | Unverifiable: 1 | Images: basic-infor.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header có back arrow + title | Skill C: vision | app-header-1 | ✅ Pass | Back arrow + "Thông tin cá nhân" header |
| 2 | 6 fields thông tin hiển thị đầy đủ | Skill B: component_checks | — | ✅ Pass | Tên ĐN, Ngày sinh, CMND, Ngày cấp, Địa chỉ, Email — đủ 6 |
| 3 | Username masked mặc định | Skill C: vision | UXG-55 | ✅ Pass | "●●●●●●●●●●" + eye toggle icon |
| 4 | PII (CMND, ngày sinh) hiển thị rõ ràng | Skill C: vision | UXG-55 | ❌ Gap | CMND "012547288" và ngày sinh "12/05/1981" hiển thị plaintext, không có option ẩn |
| 5 | Footnote hướng dẫn cập nhật | Skill C: vision | — | ✅ Pass | Footnote text hướng dẫn liên hệ chi nhánh visible |
| 6 | CTA để yêu cầu cập nhật thông tin | Skill B: flow_checks | UXG-78 | ❌ Gap | Chỉ có footnote text, không có button hay link actionable |
| 7 | Fields read-only có visual indicator | Skill C: vision | UXG-12 | ✅ Pass | Tất cả fields hiển thị dạng text (không có input border editable) |
| 8 | Email format validation display | Skill C: vision | — | ⚠️ Unverifiable | Read-only, không thể verify validation |

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
