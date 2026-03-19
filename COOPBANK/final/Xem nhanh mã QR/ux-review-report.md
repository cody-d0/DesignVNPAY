# UX Review Report — Co-opBank KHCN · Xem nhanh mã QR

## Tổng quan
- Folder: coopbank/final/Xem nhanh mã QR
- Số màn hình: 5 | Tổng check: 40
- Pass: 30 | Gap: 10 | Unverifiable: 0
- UX Score (Simple): 75% (30/40)
- UX Score (Weighted): 100%
- Proposals: 🔴 Critical: 1 | 🟡 Major: 3 | ⚪ Minor: 6 | Total: 10

## Đề xuất cải tiến (Priority)

### 🔴 Critical

#### UXP-001 · 🔴 Critical

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
| **Mức độ** | 🔴 Critical |
| **DDL** | UXG-165 |
| **UX Law** | fitts |

**🔍 Hiện trạng**

Từ ảnh xem-nhanh-ma-qr-3.png và xem-nhanh-ma-qr-6.png: Khi user tap toggle bật/tắt QR, popup xác nhận xuất hiện ngay lập tức với nút "Đồng ý". Không có trạng thái loading giữa lúc tap "Đồng ý" và khi popup kết quả hiển thị. Đây là thao tác bảo mật quan trọng (bật QR code hiển thị mà không cần đăng nhập), việc thiếu loading indicator khiến user không biết hệ thống đang xử lý.

> Evidence: Từ ảnh xem-nhanh-ma-qr-3.png — popup confirm chỉ có "Đóng"/"Đồng ý", không loading. Từ ảnh xem-nhanh-ma-qr-4.png — success popup xuất hiện mà không có transition loading.

**⚠️ Hậu quả**

- **User impact:** User có thể tap "Đồng ý" nhiều lần do không thấy phản hồi hệ thống.
- **Business impact:** Vi phạm nguyên tắc "Security-first" trong banking: thao tác bảo mật phải có feedback rõ ràng. Mất niềm tin nếu có delay mạng.
- **Violation:** UXG-165 (System Feedback), Fitts's Law (interactive element cần phản hồi).

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Button "Đồng ý" | Thêm loading spinner, disable button khi đang xử lý | Popup confirm |
| 2 | Transition | Hiển thị progress indicator trước khi chuyển sang popup kết quả | Giữa confirm và success |

---

### 🟡 Major

#### UXP-002 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-243 |
| **UX Law** | peak-end |

**🔍 Hiện trạng**

Từ ảnh xem-nhanh-ma-qr-3.png: Popup xác nhận BẬT tính năng QR chỉ có title "Thông báo" generic và body text dài. Không có icon cảnh báo (warning/shield) để nhấn mạnh đây là hành động bảo mật quan trọng. Tương tự ở xem-nhanh-ma-qr-6.png cho hành động TẮT.

> Evidence: Từ ảnh xem-nhanh-ma-qr-3.png — title "Thông báo" generic, không icon bảo mật. Body text dài, khó phân biệt với notification thông thường.

**⚠️ Hậu quả**

- **User impact:** User có thể không nhận ra mức độ quan trọng của hành động bảo mật.
- **Business impact:** Title "Thông báo" quá chung chung, trong context banking high-risk.
- **Violation:** UXG-243 (Error/Warning Feedback), Peak-End Rule (confirmation quality).

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Popup icon | Thêm icon shield/security phía trên title | Popup header |
| 2 | Title | Đổi "Thông báo" → "Xác nhận bảo mật" | Popup title |
| 3 | Body text | Highlight từ "không cần đăng nhập" bằng màu warning | Popup body |

---

#### UXP-003 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-78 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh xem-nhanh-ma-qr-2.png: Mô tả bảo mật phía trên danh sách tài khoản là 1 đoạn text dài liên tục: "Sau khi bật tính năng, Mã QR của Quý khách sẽ hiển thị nhanh chóng ngay từ màn hình đăng nhập. Để đảm bảo an toàn tài chính, Quý khách tuyệt đối không chia sẻ Mã QR và thông tin cá nhân cho người lạ." Text có bold highlight nhưng vẫn là 1 khối đặc.

> Evidence: Từ ảnh xem-nhanh-ma-qr-2.png — wall of text chiếm ~80px, khó scan trên mobile 375px viewport.

**⚠️ Hậu quả**

- **User impact:** User skip đọc thông tin bảo mật quan trọng do wall of text.
- **Business impact:** Thông điệp bảo mật bị giảm impact, tăng risk sharing QR.
- **Violation:** UXG-78 (Content Scannability).

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Alert card | Tách thành warning card với icon ⚠️ + 2 bullet points ngắn | Trên danh sách TK |
| 2 | Collapsible | Collapse mô tả chi tiết, chỉ hiện warning icon + text ngắn | Header area |

---

#### UXP-004 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-52 |
| **UX Law** | hicks |

**🔍 Hiện trạng**

Từ ảnh xem-nhanh-ma-qr-10.png: Popup "Mã QR của tôi" hướng dẫn user đăng nhập để BẬT tính năng, có nút "Cài đặt ngay". Tuy nhiên, user chưa đăng nhập, vậy tap "Cài đặt ngay" sẽ dẫn đến đâu? Popup không làm rõ flow tiếp theo.

> Evidence: Từ ảnh xem-nhanh-ma-qr-10.png — nút "Cài đặt ngay" chưa rõ flow: đăng nhập trước → mở Cài đặt QR, hay mở trực tiếp?

**⚠️ Hậu quả**

- **User impact:** Không biết "Cài đặt ngay" sẽ đi qua bao nhiêu bước. Có thể mất context sau đăng nhập.
- **Business impact:** Giảm conversion rate cho feature activation.
- **Violation:** UXG-52 (Navigation Clarity), Hick's Law (unclear decision path).

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Button text | Đổi "Cài đặt ngay" → "Đăng nhập để cài đặt" | Popup CTA |
| 2 | Auto-redirect | Sau đăng nhập tự động redirect đến màn Cài đặt QR | Login flow |
| 3 | Description | Thêm "Bạn sẽ được hướng dẫn sau khi đăng nhập" | Popup body |

---

### ⚪ Minor

#### UXP-005 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-10 |
| **UX Law** | doherty |

**🔍 Hiện trạng**

Từ ảnh xem-nhanh-ma-qr-4.png và xem-nhanh-ma-qr-7.png: Popup kết quả thành công chỉ có nút "Đóng" và không tự động đóng. User phải chủ động tap "Đóng" sau mỗi lần bật/tắt thành công.

> Evidence: Từ ảnh xem-nhanh-ma-qr-4.png — success popup chỉ có "Đóng", không auto-dismiss timer.

**⚠️ Hậu quả**

- **User impact:** Thêm 1 bước thao tác không cần thiết cho mỗi lần toggle.
- **Business impact:** Giảm hiệu quả sử dụng khi quản lý nhiều tài khoản.
- **Violation:** UXG-10 (Auto-dismiss), Doherty Threshold (response time).

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Success popup | Auto-dismiss sau 2-3 giây, giữ "Đóng" cho dismiss sớm | Popup |

---

#### UXP-006 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Xem nhanh mã QR › Chi tiết |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-32 |
| **UX Law** | fitts |

**🔍 Hiện trạng**

Từ ảnh xem-nhanh-ma-qr-16.png: Bottom sheet "Mã QR của tôi" có arrows trái/phải để swipe giữa các tài khoản, nhưng thiếu pagination indicator (dots) để user biết có bao nhiêu tài khoản.

> Evidence: Từ ảnh xem-nhanh-ma-qr-16.png — arrows visible nhưng không có dots indicator.

**⚠️ Hậu quả**

- **User impact:** Không biết đang ở tài khoản nào, có bao nhiêu tài khoản.
- **Business impact:** Giảm discoverability cho QR multi-account.
- **Violation:** UXG-32 (Pagination Indicator), Fitts's Law.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Pagination | Thêm dots indicator (●○○) dưới QR code | Bottom sheet |
| 2 | Counter | Hoặc hiển thị "1/3" bên cạnh tên TK | Header area |

---

#### UXP-007 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Xem nhanh mã QR › Tính năng |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-78 |
| **UX Law** | hicks |

**🔍 Hiện trạng**

Từ ảnh xem-nhanh-ma-qr-12.png: Bottom tab bar của màn Quét QR có 5 tabs, mỗi tab đều có badge đỏ. Tất cả 5 tabs có badges đỏ cùng lúc tạo visual noise, đặc biệt trên nền camera tối.

> Evidence: Từ ảnh xem-nhanh-ma-qr-12.png — 5/5 tabs có badge đỏ, visual clutter.

**⚠️ Hậu quả**

- **User impact:** Badge đỏ mất ý nghĩa khi tất cả tabs đều có. Phân tâm khỏi hành động quét QR.
- **Business impact:** Giảm quality perception.
- **Violation:** UXG-78 (Visual Noise), Hick's Law.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Badges | Chỉ hiển thị badge trên tabs có thông tin mới thực sự | Tab bar |
| 2 | Tab bar | Ẩn khi camera active, chỉ hiện khi user tap vùng dưới | Bottom area |

---

#### UXP-008 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-32 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh xem-nhanh-ma-qr-9.png: Banner quảng cáo "Gói vay hỗ trợ mua nhà của Co-opBank" bị cắt ở bên phải. Nút "Chi tiết" nằm ở edge phải, giảm touch target.

> Evidence: Từ ảnh xem-nhanh-ma-qr-9.png — banner image bị crop, CTA "Chi tiết" gần edge.

**⚠️ Hậu quả**

- **User impact:** Nội dung quảng cáo không đầy đủ, CTA khó tap.
- **Business impact:** Giảm banner CTR.
- **Violation:** UXG-32 (Touch Target Spacing).

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Banner | Đảm bảo nội dung trong safe area, CTA padding ≥16px từ edge | Banner card |

---

#### UXP-009 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
| **Mức độ** | ⚪ Minor |
| **DDL** | COMP:empty-state-1 |
| **UX Law** | — |

**🔍 Hiện trạng**

Màn hình hiển thị 2 tài khoản với toggle. DDL có component `empty-state-1` cho trường hợp không có tài khoản nào, nhưng design không có artboard cho trạng thái này.

> Evidence: Không có artboard cho empty state. DDL COMP:empty-state-1 requires icon + title + CTA.

**⚠️ Hậu quả**

- **User impact:** Edge case chưa được design. User có thể thấy màn hình trống.
- **Business impact:** Thiếu guidance, giảm onboarding quality.
- **Violation:** COMP:empty-state-1 (empty state spec).

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Empty state | Thiết kế empty state theo DDL spec: icon 48px + title + CTA | Center screen |

---

#### UXP-010 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Xem nhanh mã QR › Form nhập thông tin |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-88 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh popup-touch-id.png: Popup Touch ID dùng nút "Hủy" cho hành động dismiss. Trong khi các popup khác (xem-nhanh-ma-qr-3, 4, 6, 7, 10, 15) dùng "Đóng". Không nhất quán trong wording.

> Evidence: Từ ảnh popup-touch-id.png — "Hủy" vs các popup khác dùng "Đóng".

**⚠️ Hậu quả**

- **User impact:** Inconsistency trong microcopy, "Hủy" nghe tiêu cực hơn "Đóng".
- **Business impact:** Minor friction.
- **Violation:** UXG-88 (Consistent Microcopy).

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Button text | Thống nhất dùng "Đóng" hoặc "Hủy xác thực" cho rõ ý | Popup Touch ID |

---

## Chi tiết theo màn hình

### 1. Xem nhanh mã QR › Danh sách
> `SCR-QR-001` · list · 1 artboard
>
> **Score: 86% | Pass: 6 | Gap: 1 | Unverifiable: 0 | Images: xem-nhanh-ma-qr-1.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Contrast đủ cho menu text | Skill C | UXG-165 | ✅ Pass | Từ ảnh: Text đen trên nền trắng, đủ contrast |
| 2 | Touch target ≥44px cho menu items | Skill C | UXG-32 | ✅ Pass | Từ ảnh: Mỗi row menu cao ~56px |
| 3 | Tab bar icons có label | Skill C | COMP:bottom-tab-bar-1 | ✅ Pass | Từ ảnh: 5 tabs đều có icon + text label |
| 4 | Dropdown chevron cho expandable items | Skill C | — | ✅ Pass | Từ ảnh: Soft OTP và Quản lý danh bạ có chevron |
| 5 | Active tab state rõ ràng | Skill C | COMP:bottom-tab-bar-1 | ✅ Pass | Từ ảnh: Tab "Cài đặt" có highlight khác biệt |
| 6 | Hick's Law — số lượng menu items hợp lý | Skill A | hicks | ⚠️ Gap | Từ ảnh: 9 menu items + 5 tabs = 14 choices. Trigger: ≥5 interactive |
| 7 | Fitts's Law — menu items dễ tap | Skill A | fitts | ✅ Pass | Từ ảnh: rows 56px, full-width, dễ tap |

### 2. Xem nhanh mã QR › Form nhập thông tin
> `SCR-QR-002` · form · 7 artboards
>
> **Score: 60% | Pass: 6 | Gap: 4 | Unverifiable: 0 | Images: xem-nhanh-ma-qr-2.png, xem-nhanh-ma-qr-3.png, xem-nhanh-ma-qr-4.png, xem-nhanh-ma-qr-5.png, xem-nhanh-ma-qr-6.png, xem-nhanh-ma-qr-7.png, xem-nhanh-ma-qr-8.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header có back + home buttons | Skill C | COMP:app-header-1 | ✅ Pass | Từ ảnh: ic_back trái, ic_home phải |
| 2 | Toggle switch có ON/OFF state rõ ràng | Skill C | — | ✅ Pass | Từ ảnh: Toggle OFF xám, ON xanh dương có check |
| 3 | Popup confirm có nút primary + secondary | Skill C | — | ✅ Pass | Từ ảnh: "Đóng" (secondary) + "Đồng ý" (primary bold) |
| 4 | Loading state khi toggle action | Skill C | UXG-165 | ❌ Gap | Từ ảnh xem-nhanh-ma-qr-3.png: Không loading giữa confirm và success → UXP-001 |
| 5 | Popup title phù hợp context bảo mật | Skill C | UXG-243 | ❌ Gap | Từ ảnh xem-nhanh-ma-qr-3.png: Title "Thông báo" generic → UXP-002 |
| 6 | Mô tả bảo mật scannable | Skill C | UXG-78 | ❌ Gap | Từ ảnh xem-nhanh-ma-qr-2.png: Wall of text → UXP-003 |
| 7 | Empty state coverage | Skill A | COMP:empty-state-1 | ❌ Gap | Không có artboard cho TK rỗng → UXP-009 |
| 8 | Fitts's Law — toggle size đủ lớn | Skill A | fitts | ✅ Pass | Từ ảnh: Toggle ~48px width, đủ target |
| 9 | Peak-End Rule — kết thúc tích cực | Skill A | peak-end | ✅ Pass | Từ ảnh xem-nhanh-ma-qr-4.png: Check icon + success message |
| 10 | Hick's Law — limited choices | Skill A | hicks | ✅ Pass | Từ ảnh: 2 TK, mỗi TK 1 toggle = clear decision |

### 3. Xem nhanh mã QR › Form nhập thông tin
> `SCR-QR-003` · form · 5 artboards
>
> **Score: 75% | Pass: 9 | Gap: 3 | Unverifiable: 0 | Images: xem-nhanh-ma-qr-9.png, xem-nhanh-ma-qr-10.png, xem-nhanh-ma-qr-14.png, xem-nhanh-ma-qr-15.png, popup-touch-id.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Login form có label cho input fields | Skill C | COMP:text-input-1 | ✅ Pass | Từ ảnh xem-nhanh-ma-qr-14.png: "Số điện thoại" + "Mật khẩu" labels |
| 2 | Password eye toggle | Skill C | COMP:text-input-1 | ✅ Pass | Từ ảnh: ic_eye_toggle bên phải field Mật khẩu |
| 3 | Biometric option visible | Skill C | — | ✅ Pass | Từ ảnh xem-nhanh-ma-qr-9.png: Fingerprint icon cạnh Đăng nhập |
| 4 | QR shortcuts visible và accessible | Skill C | UXG-32 | ✅ Pass | Từ ảnh: "Quét QR" + "QR của tôi" icon + label, đủ size |
| 5 | Popup "Cài đặt ngay" flow clarity | Skill C | UXG-52 | ❌ Gap | Từ ảnh xem-nhanh-ma-qr-10.png: Nút chưa rõ flow → UXP-004 |
| 6 | Popup kích hoạt ứng dụng actionable | Skill C | — | ✅ Pass | Từ ảnh xem-nhanh-ma-qr-15.png: Message rõ "cần kích hoạt trước" |
| 7 | Touch ID popup wording consistency | Skill C | UXG-88 | ❌ Gap | Từ ảnh popup-touch-id.png: "Hủy" vs "Đóng" → UXP-010 |
| 8 | Banner CTA touch target | Skill C | UXG-32 | ❌ Gap | Từ ảnh xem-nhanh-ma-qr-9.png: "Chi tiết" gần edge → UXP-008 |
| 9 | Fitts's Law — CTA size đủ lớn | Skill A | fitts | ✅ Pass | Từ ảnh: Nút "Đăng nhập" full-width, đủ height |
| 10 | Hick's Law — decision complexity | Skill A | hicks | ✅ Pass | Từ ảnh: Login có ít choices, clear primary action |
| 11 | Auto-dismiss success popup | Skill C | UXG-10 | ✅ Pass | Popup kích hoạt chỉ có 1 nút "Đóng", phù hợp cho error-type |
| 12 | Forgot password accessible | Skill C | — | ✅ Pass | Từ ảnh: "Quên mật khẩu?" link visible dưới CTA |

### 4. Xem nhanh mã QR › Tính năng
> `SCR-QR-004` · feature · 1 artboard
>
> **Score: 80% | Pass: 4 | Gap: 1 | Unverifiable: 0 | Images: xem-nhanh-ma-qr-12.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Camera guideline text rõ ràng | Skill C | UXG-165 | ✅ Pass | Từ ảnh: Mô tả rõ ràng cách quét |
| 2 | Partner logos visible | Skill C | — | ✅ Pass | Từ ảnh: napas 247, VNPAY QR hiển thị đầy đủ |
| 3 | Tab bar badges visual noise | Skill C | UXG-78 | ❌ Gap | Từ ảnh: 5/5 tabs có badge đỏ → UXP-007 |
| 4 | Back navigation accessible | Skill C | COMP:app-header-1 | ✅ Pass | Từ ảnh: ic_back góc trái trên |
| 5 | Camera action buttons accessible | Skill C | UXG-32 | ✅ Pass | Từ ảnh: gallery + flashlight icons giữa screen, đủ size |

### 5. Xem nhanh mã QR › Chi tiết
> `SCR-QR-005` · detail · 2 artboards
>
> **Score: 83% | Pass: 5 | Gap: 1 | Unverifiable: 0 | Images: xem-nhanh-ma-qr-16.png, xem-nhanh-ma-qr-17.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Close X button visible | Skill C | — | ✅ Pass | Từ ảnh xem-nhanh-ma-qr-16.png: X button góc phải trên |
| 2 | QR code hiển thị đủ lớn | Skill C | — | ✅ Pass | Từ ảnh: QR code ~60% width, đủ để scan |
| 3 | Account info đầy đủ | Skill C | — | ✅ Pass | Từ ảnh: Tên, STK, Alias hiển thị rõ |
| 4 | Share + Save actions accessible | Skill C | UXG-32 | ✅ Pass | Từ ảnh: "Chia sẻ" + "Lưu ảnh" buttons với icons |
| 5 | Pagination indicator cho multi-account | Skill C | UXG-32 | ❌ Gap | Từ ảnh: Arrows trái/phải nhưng thiếu dots → UXP-006 |
| 6 | Fitts's Law — action buttons size | Skill A | fitts | ✅ Pass | Từ ảnh: Buttons icon + text, đủ touch target |

---

## DDL References sử dụng

| ddl_ref | Rule | UX Law | Áp dụng |
|---------|------|--------|---------|
| UXG-10 | Auto-dismiss Notifications | doherty | SCR-QR-002 success popup không auto-dismiss |
| UXG-32 | Touch Target Spacing | fitts | SCR-QR-003 banner CTA, SCR-QR-005 pagination |
| UXG-52 | Navigation Clarity | hicks | SCR-QR-003 popup flow unclear |
| UXG-78 | Content Scannability | — | SCR-QR-002 wall of text, SCR-QR-004 badge noise |
| UXG-88 | Consistent Microcopy | — | SCR-QR-003 "Hủy" vs "Đóng" |
| UXG-165 | System Feedback / Text Legibility | fitts | SCR-QR-002 loading state missing |
| UXG-243 | Error/Warning Feedback | peak-end | SCR-QR-002 popup title generic |
| COMP:app-header-1 | App header spec | — | All screens header check |
| COMP:bottom-tab-bar-1 | Bottom tab bar spec | — | SCR-QR-001, SCR-QR-004 tab bars |
| COMP:empty-state-1 | Empty state spec | — | SCR-QR-002 missing empty state |
| COMP:text-input-1 | Text input spec | — | SCR-QR-003 login fields |
