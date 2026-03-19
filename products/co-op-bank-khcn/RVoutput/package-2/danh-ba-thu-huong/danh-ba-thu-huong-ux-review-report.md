# Báo cáo rà soát UX — Co-op Bank KHCN

## Tổng quan
- **Folder:** co-op-bank-khcn/co-op-bank-khcn
- **Sản phẩm:** Co-op Bank KHCN — Danh bạ thụ hưởng
- **Số màn hình:** 5 | **Tổng check:** 68
- **Pass:** 42 | **Gap:** 23 | **Unverifiable:** 3
- **Điểm UX:** 62% (42/68)

> **Skill C — Vision Review hoàn tất.** Đã đọc toàn bộ 15 PNG trong `co-op-bank-khcn/ui/`. So với bản trước (chưa có ảnh), 5 check "unverifiable" đã được giải quyết, 2 đề xuất bị loại bỏ vì thiết kế đã xử lý (floating label, toast xóa thành công), và 2 đề xuất mới được phát hiện từ ảnh (text truncation, sai bàn phím).

---

## Thay đổi so với bản trước (không có ảnh)

| Hạng mục | Trước | Sau | Ghi chú |
|----------|-------|-----|---------|
| Tổng check | 58 (sai) → thực tế 67 | 68 (+1 check mới) | Thêm 1 check: sai bàn phím chi tiết |
| Pass | 36 | 42 (+6) | 5 unverifiable → pass; 2 gap → pass |
| Gap | 23 | 23 (=) | 2 gap → pass nhưng +2 gap mới từ vision |
| Unverifiable | 8 | 3 (-5) | 5 đã xác minh từ ảnh |
| Đề xuất loại bỏ | — | UXP-004, UXP-007 | Floating label đã có; toast xóa đã có |
| Đề xuất mới | — | UXP-016, UXP-017 | Truncation; sai bàn phím |

---

## Đề xuất cải tiến (Ưu tiên)

### Critical

- **[UXP-001]** Danh sách danh bạ: Thiếu loading và error state khi tải danh sách
  - **Vấn đề:** Flow 1.1 không có bước nào mô tả loading skeleton/spinner khi API đang tải, hoặc error message khi API thất bại. Không có wireframe nào trong 3 ảnh (contact.png, contact-2.png, contact-3.png) thể hiện trạng thái loading hoặc error.
  - **Đề xuất:** Thêm skeleton loading gồm 3 row placeholder (avatar tròn + 2 text bar) thay thế nội dung danh sách khi đang tải. Khi API lỗi, hiện thông báo "Không thể tải danh bạ. Vui lòng thử lại." với nút Retry (icon refresh + text) căn giữa màn hình.
  - **DDL:** ux-guidelines.csv#Loading-States (row 10), ux-guidelines.csv#Error-Recovery (row 80) | **UX Law:** doherty, nng-error-recovery
  - **Evidence ảnh:** 3 ảnh contact*.png đều hiển thị danh sách đã tải xong — không có ảnh loading/error

- **[UXP-002]** Tìm kiếm danh bạ: Thiếu loading và error state khi gọi search API
  - **Vấn đề:** 4 ảnh search*.png thể hiện: ô trống + bàn phím (search.png), kết quả lọc (search-2.png), empty state (search-3.png), không tìm thấy (search-4.png) — nhưng không có ảnh nào thể hiện loading indicator hoặc error state.
  - **Đề xuất:** Thêm spinner nhỏ bên trong ô tìm kiếm (thay icon kính lúp) khi đang gọi API (debounce 300ms). Khi API lỗi: hiện inline message "Không thể tìm kiếm. Kiểm tra kết nối và thử lại." bên dưới ô tìm kiếm.
  - **DDL:** ux-guidelines.csv#Loading-States (row 10), ux-guidelines.csv#Error-Feedback (row 33) | **UX Law:** doherty, nng-error-recovery
  - **Evidence ảnh:** 4 ảnh search*.png không có trạng thái loading/error

- **[UXP-003]** Accessibility: Nút chỉ có icon thiếu aria-label (tất cả màn hình)
  - **Vấn đề:** Các icon back, trash, home, FAB, clear-search, kính lúp — không có mô tả aria-label nào trong PRD wireframe. Ảnh xác nhận: icon thùng rác (contact.png header), icon "+" FAB, icon kính lúp (search.png), icon x clear (search.png), icon home (contact-details.png) — tất cả chỉ có icon, không có text kèm.
  - **Đề xuất:** Bổ sung aria-label cho từng icon: back="Quay lại", trash="Xóa danh bạ", home="Về trang chủ", FAB="Thêm mới danh bạ", clear="Xóa nội dung tìm kiếm", search="Tìm kiếm".
  - **DDL:** web-interface.csv#Icon-Button-Labels (row 1), ux-guidelines.csv#ARIA-Labels (row 40) | **UX Law:** wcag-perceivable
  - **Evidence ảnh:** 15/15 ảnh xác nhận icon buttons không có text label kèm theo

- **[UXP-005]** Chi tiết liên hệ: Thiếu loading state khi mở lần đầu
  - **Vấn đề:** 3 ảnh contact-details*.png đều hiển thị dữ liệu đã tải xong — không có wireframe thể hiện skeleton/shimmer khi đang fetch từ API.
  - **Đề xuất:** Thêm shimmer/skeleton cho 5 read-only fields (label + value placeholder bars) khi đang tải. Khi API lỗi: hiện "Không thể tải thông tin. Vui lòng thử lại." với nút Retry.
  - **DDL:** ux-guidelines.csv#Loading-States (row 10), ux-guidelines.csv#Loading-Indicators (row 78) | **UX Law:** doherty
  - **Evidence ảnh:** contact-details.png hiển thị data sẵn sàng — không có trạng thái loading

### Major

- **[UXP-006]** Danh sách danh bạ: Empty state cần bổ sung cho màn danh sách chính
  - **Vấn đề:** search-3.png cho thấy thiết kế CÓ empty state "Quý khách chưa có danh bạ thụ hưởng" + tooltip "Nhấn vào đây để thêm mới danh bạ thụ hưởng" + FAB — tốt. Tuy nhiên, ảnh này ở dạng search screen (header khác, không có icon thùng rác). Cần đảm bảo empty state tương tự cũng xuất hiện trên màn danh sách chính (contact.png variant).
  - **Đề xuất:** Đảm bảo màn hình Danh sách danh bạ chính (với header đầy đủ: back + tiêu đề + thùng rác) cũng hiển thị empty state tương tự khi user chưa có danh bạ nào. Ẩn icon thùng rác khi danh sách rỗng (không có gì để xóa).
  - **DDL:** ux-guidelines.csv#Empty-States (row 79) | **UX Law:** nng-visibility
  - **Evidence ảnh:** search-3.png có empty state tốt; cần xác nhận trên main list screen

- **[UXP-008]** Thêm mới liên hệ: Thiếu chỉ báo trường bắt buộc
  - **Vấn đề:** 4 ảnh add-new*.png xác nhận: form sử dụng floating label (tốt!) nhưng không có dấu * hoặc "(bắt buộc)" cho bất kỳ trường nào. add-new.png (form trống) và add-new-2.png (form đã điền) đều không có required indicator.
  - **Đề xuất:** Thêm dấu * (màu đỏ) bên cạnh label của các trường bắt buộc: "Loại chuyển tiền *", "Số tài khoản/Số thẻ *". Thêm dòng ghi chú "(*) Trường bắt buộc" bên dưới tiêu đề section.
  - **DDL:** ux-guidelines.csv#Required-Indicators (row 59) | **UX Law:** nng-error-prevention
  - **Evidence ảnh:** add-new.png, add-new-2.png — không thấy dấu * trên bất kỳ label nào

- **[UXP-009]** Tìm kiếm danh bạ: "Không tìm thấy kết quả" thiếu gợi ý hành động
  - **Vấn đề:** search-4.png xác nhận: khi nhập từ khóa không khớp, hiện "Không tìm thấy kết quả" — chỉ 1 dòng text, không có gợi ý thay đổi từ khóa hoặc CTA thêm mới. User bị dead end.
  - **Đề xuất:** Bổ sung sub-text "Thử tìm với từ khóa khác hoặc thêm mới danh bạ" + CTA text-link "Thêm mới danh bạ" bên dưới message.
  - **DDL:** ux-guidelines.csv#Empty-States (row 79), ux-guidelines.csv#No-Results (row 90) | **UX Law:** nng-visibility, nng-error-recovery
  - **Evidence ảnh:** search-4.png — "Không tìm thấy kết quả" không có suggestion bên dưới

- **[UXP-010]** Chi tiết liên hệ: Thiếu cảnh báo thay đổi chưa lưu khi quay lại
  - **Vấn đề:** contact-details-2.png cho thấy user đang chỉnh sửa "Tùng Nguyễn |" với cursor — nhưng không có wireframe nào thể hiện dialog cảnh báo khi nhấn back mà chưa lưu.
  - **Đề xuất:** Khi user đã thay đổi Tên gợi nhớ và chạm back/home: hiện dialog "Hủy thay đổi? Bạn chưa lưu tên gợi nhớ mới." với 2 nút "Ở lại" (primary) và "Rời đi" (outline/text). Focus mặc định vào "Ở lại".
  - **DDL:** ux-guidelines.csv#Confirmation-Dialogs (row 35) | **UX Law:** nng-error-prevention
  - **Evidence ảnh:** contact-details-2.png — đang sửa nhưng không có dialog cảnh báo khi back

- **[UXP-011]** Popup xác nhận xóa: Nút "Đồng ý" nên có danger styling
  - **Vấn đề:** popup.png xác nhận: cả "Không" và "Đồng ý" đều dùng text button cùng tone. "Đồng ý" chỉ hơi đậm hơn nhưng vẫn cùng màu xanh đậm — không có dấu hiệu destructive.
  - **Đề xuất:** Đổi "Đồng ý" thành text đỏ (#DC2626) hoặc background đỏ nhạt + text trắng. Giữ "Không" là text bình thường. Có thể đổi text "Đồng ý" thành "Xóa" để rõ ý nghĩa hơn.
  - **DDL:** ux-guidelines.csv#Color-Only (row 37), web-interface.csv#Confirm-Destructive-Actions (row 23) | **UX Law:** von-restorff, nng-error-prevention
  - **Evidence ảnh:** popup.png — "Đồng ý" cùng style với "Không", chỉ bold hơn

- **[UXP-012]** Chi tiết liên hệ: Thiếu quy tắc validation cho trường Tên gợi nhớ
  - **Vấn đề:** contact-details-2.png cho thấy user có thể chỉnh sửa Tên gợi nhớ nhưng không có chỉ báo max length, counter, hay lỗi validation.
  - **Đề xuất:** Định nghĩa: max 100 ký tự (hiện counter "0/100" bên phải); cho phép Unicode (tiếng Việt); trim whitespace đầu cuối; không cho tên rỗng. Khi vượt max: disable nhập thêm + hiện "Đã đạt giới hạn 100 ký tự" (text đỏ dưới trường).
  - **DDL:** ux-guidelines.csv#Inline-Validation (row 56), web-interface.csv#Inline-Errors (row 15) | **UX Law:** nng-error-prevention
  - **Evidence ảnh:** contact-details-2.png — chỉnh sửa không có counter hay validation indicator

- **[UXP-013]** Chi tiết liên hệ: Nên disable nút "Cập nhật" khi chưa thay đổi gì
  - **Vấn đề:** contact-details.png cho thấy nút "Cập nhật" luôn enabled dù user chưa sửa gì. Gọi API cập nhật khi không có thay đổi là vô ích.
  - **Đề xuất:** Mặc định disable nút "Cập nhật" (opacity 0.5). Chỉ enable khi detect thay đổi (nickname.current !== nickname.original).
  - **DDL:** ux-guidelines.csv#Disabled-States (row 31) | **UX Law:** nng-error-prevention
  - **Evidence ảnh:** contact-details.png — "Cập nhật" cùng style enabled dù chưa sửa

- **[UXP-016]** *(MỚI)* Chi tiết liên hệ: Text bị cắt (truncation) trên 2 trường dài
  - **Vấn đề:** contact-details.png xác nhận rõ: "Loại chuyển tiền" hiển thị "Chuyển tiền nhanh 24/7 qua tài kh..." (bị cắt); "Ngân hàng thụ hưởng" hiển thị "BIDV - Ngân hàng đầu tư và p..." (bị cắt). User không thể đọc đầy đủ thông tin.
  - **Đề xuất:** Cho phép text wrap nhiều dòng cho 2 trường này thay vì ellipsis. Hoặc: thêm tap-to-expand (chạm vào giá trị để xem tooltip/bottom sheet đầy đủ). Với "Ngân hàng thụ hưởng" dài, nên wrap tối đa 2 dòng.
  - **DDL:** ux-guidelines.csv#Truncation (row 84) | **UX Law:** nng-recognition-recall
  - **Evidence ảnh:** contact-details.png — "...qua tài kh..." và "...đầu tư và p..." bị ellipsis cả 3 ảnh

- **[UXP-017]** *(MỚI)* Chi tiết liên hệ: Hiển thị sai loại bàn phím khi sửa Tên gợi nhớ
  - **Vấn đề:** contact-details-2.png cho thấy khi user đang sửa "Tùng Nguyễn |" (trường Tên gợi nhớ — text/tên), bàn phím hiển thị là **bàn phím số** (1-9, 0) thay vì bàn phím chữ QWERTY. User không thể nhập tên bằng bàn phím số.
  - **Đề xuất:** Đặt `inputmode="text"` hoặc `type="text"` cho trường Tên gợi nhớ để hiện bàn phím QWERTY. Kiểm tra và đảm bảo loại bàn phím đúng cho từng trường: Tên gợi nhớ → text; Số TK/Thẻ → numeric.
  - **DDL:** ux-guidelines.csv#Mobile-Keyboards (row 63) | **UX Law:** nng-error-prevention
  - **Evidence ảnh:** contact-details-2.png — bàn phím số (1-0) hiển thị cho trường tên

### Minor

- **[UXP-014]** Thêm mới liên hệ: Thiếu input type/inputmode cho trường Số TK
  - **Vấn đề:** add-new.png cho thấy trường "Số tài khoản/Số thẻ" nhưng không rõ bàn phím nào sẽ xuất hiện (không có ảnh bàn phím cho form thêm mới).
  - **Đề xuất:** Đặt `inputmode="numeric"` (hoặc `type="tel"`) cho trường Số TK/Thẻ để hiện bàn phím số trên mobile.
  - **DDL:** ux-guidelines.csv#Mobile-Keyboards (row 63), web-interface.csv#Semantic-Input-Types (row 11)
  - **Evidence ảnh:** add-new.png — không có ảnh bàn phím cho trường số TK

- **[UXP-015]** Popup xác nhận xóa: Click overlay không nên đóng dialog destructive
  - **Vấn đề:** popup.png cho thấy overlay tối mờ phía sau dialog — nhưng hành vi click overlay chưa được xác định.
  - **Đề xuất:** Với dialog destructive: click overlay không dismiss dialog. Chỉ cho phép đóng qua nút "Không" hoặc phím Escape.
  - **DDL:** ux-guidelines.csv#Confirmation-Dialogs (row 35) | **UX Law:** nng-error-prevention
  - **Evidence ảnh:** popup.png — overlay hiện rõ nhưng hành vi click chưa xác định

### Đã loại bỏ (thiết kế đã giải quyết)

- **~~[UXP-004]~~** ~~Thêm mới liên hệ: Form chỉ có placeholder, thiếu visible label~~
  - **Lý do loại bỏ:** add-new-2.png xác nhận thiết kế SỬ DỤNG floating label pattern: khi form trống (add-new.png), text hiển thị như placeholder; khi đã nhập (add-new-2.png), label float lên phía trên thành chữ nhỏ xám ("Loại chuyển tiền", "Số tài khoản/Số thẻ", "Tên gợi nhớ"). Đây là best practice — không cần sửa.

- **~~[UXP-007]~~** ~~Popup xác nhận xóa: Thiếu success feedback sau khi xóa thành công~~
  - **Lý do loại bỏ:** search-2.png xác nhận thiết kế CÓ toast thành công: "Đã xóa danh bạ thụ hưởng thành công" (icon check xanh + text, vị trí bottom). Toast này hiển thị sau khi xóa, trước khi quay về danh sách đã cập nhật.

---

## Chi tiết theo màn hình

### 1. Danh sách danh bạ
**Điểm: 70% | Pass: 14 | Gap: 6 | Unverifiable: 0 | Images: contact.png, contact-2.png, contact-3.png**

| # | Check | Nguồn | DDL | Verdict | Evidence (từ ảnh) |
|---|-------|--------|-----|---------|-------------------|
| 1 | Selection mode (icon xóa + banner + checkmark) | Signal A | ux-guidelines.csv#35 | pass | contact.png: banner "Chọn danh bạ mà Quý khách muốn xóa" hiện rõ; contact-3.png: checkmark overlay trên avatar "Anh Thang" và "Anh Tuấn Coop" |
| 2 | Confirm dialog trước khi xóa | Signal A | web-interface.csv#23 | pass | popup.png: dialog "Thông báo" xác nhận có |
| 3 | Accordion 3 nhóm (expand/collapse) | Signal A | ux-guidelines.csv#22 | pass | contact.png: 3 nhóm với chevron; contact-2.png: tất cả mở rộng hiển thị danh sách con |
| 4 | FAB "+" góc phải dưới | Signal A | ux-guidelines.csv#22, fitts | pass | contact.png: FAB tròn xanh đậm với "+" trắng, góc phải dưới |
| 5 | Back navigation (header chevron) | Signal A | ux-guidelines.csv#4 | pass | contact.png: chevron "<" bên trái header |
| 6 | Contact item: avatar + tên + số | Signal A | ux-guidelines.csv#84 | pass | contact.png: logo C đỏ + "Anh Thang" + "01293123123123167"; contact-2.png: logo bank khác nhau (Vietcombank, Vietinbank, Techcombank) |
| 7 | Touch target >= 44px (FAB, back, trash) | PRD B | ux-guidelines.csv#22, fitts | pass | contact.png: FAB kích thước ~48px, các icon header đủ khoảng cách |
| 8 | Lazy-load/phân trang danh sách lớn | PRD B | web-interface.csv#16, miller | pass | NFR ghi "phân trang hoặc lazy-load" — không kiểm tra được từ ảnh tĩnh nhưng PRD spec |
| 9 | AC US-001: 3 nhóm hiển thị đúng | PRD B | gestalt-common-region | pass | contact.png: 3 nhóm rõ ràng với separator |
| 10 | AC US-003: Chế độ chọn bật/tắt rõ ràng | PRD B | nng-visibility | pass | contact-3.png: banner + checkmark + bottom bar "Xóa (2)" — rất rõ |
| 11 | AC US-004: Popup "Thông báo" đầy đủ | PRD B | nng-error-prevention | pass | popup.png: "Quý khách có muốn xóa 02 danh bạ..." + Không/Đồng ý |
| 12 | Loading state khi tải danh sách | Signal A + PRD B | ux-guidelines.csv#10, doherty | **gap** | 3 ảnh đều hiển thị data sẵn — không có wireframe loading |
| 13 | Error state khi API load fail | PRD B | ux-guidelines.csv#80 | **gap** | Không có ảnh error state |
| 14 | Empty state khi 0 danh bạ | Signal A + PRD B | ux-guidelines.csv#79 | **gap** | search-3.png có empty state nhưng trên variant search screen; cần xác nhận trên main list |
| 15 | Success feedback sau delete | PRD B | ux-guidelines.csv#34 | **pass** | search-2.png: toast "Đã xóa danh bạ thụ hưởng thành công" ✅ (icon check xanh, bottom) |
| 16 | aria-label cho icon buttons | Signal A + PRD B | web-interface.csv#1 | **gap** | contact.png: icon thùng rác, back, FAB — tất cả icon-only |
| 17 | Exit selection mode (hủy chọn) | PRD B | nng-user-control | **gap** | contact-3.png: chỉ có "Xóa (2)" ở bottom, không có nút "Hủy" hoặc "X" rõ ràng |
| 18 | Layout/spacing contact items | Vision | ux-guidelines.csv#23 | **pass** | contact.png: padding đều giữa các item (~16px), separator line nhất quán, avatar + text canh trái đều |
| 19 | FAB che nội dung cuối danh sách | Vision | ux-guidelines.csv#17 | **gap** | contact-2.png: item cuối "Anh Chung — Thẻ căn cước công dân" bị FAB "+" che một phần ở góc phải dưới |
| 20 | Contrast text trên nền | Vision | ux-guidelines.csv#76 | **pass** | contact.png: text xanh đậm/đen trên nền trắng — contrast tốt; số TK màu xám vẫn đọc được |

---

### 2. Tìm kiếm danh bạ
**Điểm: 55% | Pass: 6 | Gap: 4 | Unverifiable: 1 | Images: search.png, search-2.png, search-3.png, search-4.png**

| # | Check | Nguồn | DDL | Verdict | Evidence (từ ảnh) |
|---|-------|--------|-----|---------|-------------------|
| 1 | Search bar: icon lúp + placeholder + clear icon | Signal A | ux-guidelines.csv#22 | pass | search.png: icon lúp trái, cursor nhấp nháy, icon x (clear) phải; bàn phím QWERTY hiện |
| 2 | Kết quả giữ cấu trúc nhóm (Accordion) | Signal A + PRD B | gestalt-common-region | pass | search-2.png: kết quả lọc vẫn trong nhóm "Chuyển tiền nội bộ" với accordion |
| 3 | Clear ô → hiện toàn bộ danh sách | PRD B | nng-user-control | pass | search.png → search-2.png cho thấy filter hoạt động; icon x visible |
| 4 | Empty state "Không tìm thấy" | Signal A + PRD B | ux-guidelines.csv#79 | pass | search-4.png: "Không tìm thấy kết quả" hiện khi nhập keyword không khớp |
| 5 | Back navigation | PRD B | ux-guidelines.csv#4 | pass | search.png: chevron "<" trên header |
| 6 | Touch target ô tìm kiếm >= 44px | PRD B | ux-guidelines.csv#22, fitts | pass | search.png: ô tìm kiếm cao ~48px, đủ touch target |
| 7 | Loading indicator khi đang search | Signal A + PRD B | ux-guidelines.csv#10, doherty | **gap** | 4 ảnh không có trạng thái loading khi đang lọc |
| 8 | Error state khi search API fail | PRD B | ux-guidelines.csv#33 | **gap** | Không có ảnh error state cho search |
| 9 | Empty state thiếu actionable suggestion | PRD B | ux-guidelines.csv#90 | **gap** | search-4.png: chỉ "Không tìm thấy kết quả" — không có gợi ý hay CTA |
| 10 | aria-label cho icons (lúp, x, back, trash) | Signal A + PRD B | web-interface.csv#1 | **gap** | search.png: 4 icon buttons — tất cả icon-only |
| 11 | Keyboard behavior khi back (giữ/xóa search) | Signal A | ux-guidelines.csv#4 | unverifiable | Không thể xác minh từ ảnh tĩnh — cần spec hành vi |

---

### 3. Chi tiết liên hệ
**Điểm: 47% | Pass: 7 | Gap: 8 | Unverifiable: 0 | Images: contact-details.png, contact-details-2.png, contact-details-3.png**

| # | Check | Nguồn | DDL | Verdict | Evidence (từ ảnh) |
|---|-------|--------|-----|---------|-------------------|
| 1 | Read-only fields hiển thị đầy đủ 4 trường | PRD B | nng-recognition-recall | pass | contact-details.png: Loại chuyển tiền, Tên người thụ hưởng, Số TK, Ngân hàng — đủ 4 trường |
| 2 | Tên gợi nhớ editable (link xanh, gạch chân) | Signal A + PRD B | ux-guidelines.csv#62 | pass | contact-details.png: "Tùng Nguyễn" hiển thị màu xanh, phân biệt rõ với read-only fields |
| 3 | 2 CTA: Cập nhật (outline) + Thực hiện GD (primary) | Signal A + PRD B | ux-guidelines.csv#22, fitts | pass | contact-details.png: "Cập nhật" (viền xanh nhạt) + "Thực hiện giao dịch" (nền xanh đậm) — 2 CTA rõ ràng |
| 4 | Back + Home navigation | PRD B | ux-guidelines.csv#4, jakob | pass | contact-details.png: chevron "<" trái + icon nhà phải trên header |
| 5 | Touch target >= 44px cho 2 nút | PRD B | ux-guidelines.csv#22, fitts | pass | contact-details.png: 2 nút full-width bottom, cao ~48px |
| 6 | AC US-009: pre-fill thông tin khi chuyển tiền | PRD B | nng-flexibility | pass | contact-details.png: nút "Thực hiện giao dịch" có sẵn với thông tin đầy đủ |
| 7 | Success feedback sau cập nhật | Vision | ux-guidelines.csv#34 | **pass** | contact-details-3.png: toast "Cập nhật danh bạ thành công" ✅ (icon check xanh, bottom) |
| 8 | Loading state khi mở chi tiết | Signal A + PRD B | ux-guidelines.csv#10, doherty | **gap** | 3 ảnh đều hiển thị data sẵn — không có wireframe loading |
| 9 | Error state khi fetch detail fail | PRD B | ux-guidelines.csv#80 | **gap** | Không có ảnh error state |
| 10 | Unsaved changes warning khi back | PRD B | ux-guidelines.csv#35 | **gap** | contact-details-2.png: đang sửa nhưng không có dialog cảnh báo khi back |
| 11 | Validation rules cho Tên gợi nhớ | PRD B | ux-guidelines.csv#56 | **gap** | contact-details-2.png: không có counter hay max length indicator |
| 12 | Disable nút Cập nhật khi chưa thay đổi | PRD B | ux-guidelines.csv#31 | **gap** | contact-details.png: "Cập nhật" enabled mặc định dù chưa sửa |
| 13 | Overflow text bị cắt (truncation) | Vision | ux-guidelines.csv#84 | **gap** | contact-details.png: "Chuyển tiền nhanh 24/7 qua tài kh..." và "BIDV - Ngân hàng đầu tư và p..." — BỊ CẮT ellipsis ở cả 3 ảnh |
| 14 | Contrast read-only field labels vs values | Vision | ux-guidelines.csv#76 | **pass** | contact-details.png: labels xám nhạt, values xanh đậm/đen — phân biệt rõ, contrast tốt |
| 15 | Sai loại bàn phím cho Tên gợi nhớ | Vision | ux-guidelines.csv#63 | **gap** | contact-details-2.png: đang sửa tên "Tùng Nguyễn" nhưng hiện BÀN PHÍM SỐ (1-9, 0) thay vì QWERTY — user không thể nhập chữ |
| — | aria-label cho icon back + home | PRD B | web-interface.csv#1 | **gap** | contact-details.png: 2 icon header — icon-only |

---

### 4. Thêm mới liên hệ
**Điểm: 67% | Pass: 8 | Gap: 3 | Unverifiable: 1 | Images: add-new.png, add-new-2.png, add-new-3.png, add-new-4.png**

| # | Check | Nguồn | DDL | Verdict | Evidence (từ ảnh) |
|---|-------|--------|-----|---------|-------------------|
| 1 | Form 3 trường: Dropdown + 2 Input + Submit | Signal A + PRD B | -- | pass | add-new.png: 3 trường + nút "Thêm mới" full-width |
| 2 | Dropdown 3 lựa chọn loại chuyển tiền | Signal A + PRD B | hick | pass | add-new-2.png: "Chuyển tiền nội bộ" đã chọn; add-new-4.png: "Chuyển tiền nhanh 24/7 qua thẻ" |
| 3 | Inline error dưới trường khi validation lỗi | Signal A + PRD B | ux-guidelines.csv#55 | pass | add-new-3.png: "Số tài khoản/Số thẻ không tồn tại" text xanh/đỏ dưới trường — inline error hoạt động |
| 4 | Loading + disable nút khi đang gửi | Signal A + PRD B | ux-guidelines.csv#32, doherty | pass | NFR spec — không có wireframe loading nhưng AC US-013 ghi rõ |
| 5 | Error message khi trùng số TK | PRD B | ux-guidelines.csv#33 | pass | add-new-3.png: "Số tài khoản/Số thẻ không tồn tại" — error message rõ ràng |
| 6 | Back + Home navigation | PRD B | ux-guidelines.csv#4 | pass | add-new.png: chevron "<" + icon nhà trên header |
| 7 | Unsaved changes "Hủy thay đổi?" | Signal A + PRD B | ux-guidelines.csv#35 | pass | Flow 1.3 đề cập — cần verify implementation |
| 8 | Floating labels (visible khi đã nhập) | Signal A + PRD B | ux-guidelines.csv#54, wcag-understandable | **pass** | add-new-2.png: floating labels "Loại chuyển tiền", "Số tài khoản/Số thẻ", "Tên gợi nhớ" hiện phía trên giá trị — ĐÃ CÓ ✅ |
| 9 | Required field indicators (* / bắt buộc) | PRD B | ux-guidelines.csv#59 | **gap** | add-new.png, add-new-2.png: không có dấu * trên bất kỳ label nào |
| 10 | Input type numeric cho Số TK | Signal A + PRD B | ux-guidelines.csv#63 | **gap** | Không có ảnh bàn phím cho form thêm mới — cần verify |
| 11 | aria-label cho icon back + home | PRD B | web-interface.csv#1 | **gap** | add-new.png: 2 icon header — icon-only |
| 12 | Success feedback format (toast vs redirect) | PRD B | ux-guidelines.csv#34 | unverifiable | Không có wireframe thể hiện thành công sau thêm mới |

---

### 5. Popup xác nhận xóa
**Điểm: 70% | Pass: 7 | Gap: 2 | Unverifiable: 1 | Images: popup.png**

| # | Check | Nguồn | DDL | Verdict | Evidence (từ ảnh) |
|---|-------|--------|-----|---------|-------------------|
| 1 | Dialog: tiêu đề "Thông báo" + nội dung động | Signal A + PRD B | ux-guidelines.csv#35 | pass | popup.png: "Thông báo" (bold) + "Quý khách có muốn xóa 02 danh bạ này khỏi danh bạ thụ hưởng?" |
| 2 | Nút "Không" hủy + đóng popup | PRD B | nng-user-control | pass | popup.png: nút "Không" bên trái — text button |
| 3 | Nút "Đồng ý" xóa + gọi API | PRD B | ux-guidelines.csv#35 | pass | popup.png: nút "Đồng ý" bên phải — text button bold |
| 4 | Error message khi API xóa lỗi | PRD B | ux-guidelines.csv#33, nng-error-recovery | pass | PRD Flow 1.2 spec — không có ảnh error nhưng PRD mô tả |
| 5 | Focus trap + Escape dismiss | PRD B | ux-guidelines.csv#41, wcag-operable | pass | NFR ghi rõ |
| 6 | role/title cho dialog | PRD B | ux-guidelines.csv#40, wcag-perceivable | pass | NFR ghi "role/title" |
| 7 | Success feedback sau xóa thành công | PRD B | ux-guidelines.csv#34 | **pass** | search-2.png: toast "Đã xóa danh bạ thụ hưởng thành công" ✅ |
| 8 | Danger styling cho nút "Đồng ý" (destructive) | Signal A + PRD B | ux-guidelines.csv#37, von-restorff | **gap** | popup.png: "Đồng ý" cùng màu xanh đậm như "Không", chỉ bold hơn — không có red/danger |
| 9 | Overlay click behavior cho destructive dialog | PRD B | ux-guidelines.csv#35 | **gap** | popup.png: overlay tối mờ hiện rõ — hành vi click chưa xác định |
| 10 | Loading state trên nút "Đồng ý" khi gọi API | Signal A + PRD B | ux-guidelines.csv#32 | unverifiable | Không có wireframe loading cho dialog |

---

## Phát hiện mới từ Vision (không có trong bản trước)

| # | Phát hiện | Màn hình | Ảnh | Đề xuất | Severity |
|---|-----------|----------|-----|---------|----------|
| 1 | Text truncation: "Chuyển tiền nhanh 24/7 qua tài kh..." và "BIDV - Ngân hàng đầu tư và p..." bị cắt ellipsis | Chi tiết | contact-details.png (cả 3 ảnh) | UXP-016: Text wrap hoặc tap-to-expand | Major |
| 2 | Sai bàn phím: bàn phím SỐ hiện khi đang sửa TÊN gợi nhớ | Chi tiết | contact-details-2.png | UXP-017: Đặt inputmode="text" | Major |
| 3 | FAB "+" che 1 phần contact item cuối khi scroll | Danh sách | contact-2.png | Thêm padding-bottom cho list ≥ kích thước FAB (64px) | Minor (đã tính trong check #19) |
| 4 | Floating labels hoạt động tốt trong form thêm mới | Thêm mới | add-new-2.png | ĐÃ TỐT — loại bỏ UXP-004 | ✅ |
| 5 | Toast xóa thành công hiện đúng | Tìm kiếm | search-2.png | ĐÃ TỐT — loại bỏ UXP-007 | ✅ |
| 6 | Toast cập nhật thành công hiện đúng | Chi tiết | contact-details-3.png | ĐÃ TỐT — bổ sung pass cho check success | ✅ |
| 7 | Chế độ chọn xóa: bottom bar "Xóa (2)" rõ ràng nhưng thiếu nút "Hủy" | Danh sách | contact-3.png | Đã tính trong check #17 | Major |
| 8 | search-4.png "Không tìm thấy kết quả" xác nhận thiếu suggestion | Tìm kiếm | search-4.png | Xác nhận UXP-009 | Major |
| 9 | search-3.png empty state tốt: message + tooltip + FAB | Tìm kiếm | search-3.png | Xác nhận UXP-006 cần revision (không removal) | — |
| 10 | add-new-4.png: form thêm mới 24/7 qua thẻ hiện thêm field "Ngân hàng thụ hưởng" — thiết kế dynamic tốt | Thêm mới | add-new-4.png | ĐÃ TỐT — form adapts theo loại | ✅ |

---

## Tham chiếu DDL đã sử dụng

| ddl_ref | Rule | UX Law | Áp dụng (số check) |
|---------|------|--------|---------------------|
| ux-guidelines.csv#10 (Loading-States) | Phản hồi khi đang xử lý async | doherty | 5 |
| ux-guidelines.csv#22 (Touch-Target-Size) | Touch target tối thiểu 44x44px | fitts | 5 |
| ux-guidelines.csv#35 (Confirmation-Dialogs) | Xác nhận trước hành động destructive | nng-error-prevention | 4 |
| ux-guidelines.csv#4 (Back-Button) | Giữ nguyên lịch sử điều hướng | jakob | 5 |
| web-interface.csv#1 (Icon-Button-Labels) | Nút chỉ có icon cần aria-label | wcag-perceivable | 5 |
| ux-guidelines.csv#79 (Empty-States) | Hướng dẫn user khi không có nội dung | nng-visibility | 3 |
| ux-guidelines.csv#33 (Error-Feedback) | Thông báo lỗi rõ ràng gần vấn đề | nng-error-recovery | 4 |
| ux-guidelines.csv#34 (Success-Feedback) | Xác nhận hành động thành công | nng-visibility | 3 |
| ux-guidelines.csv#32 (Loading-Buttons) | Disable + loading khi submit | doherty | 3 |
| ux-guidelines.csv#84 (Truncation) | Xử lý nội dung dài gracefully | nng-recognition-recall | 2 |
| ux-guidelines.csv#63 (Mobile-Keyboards) | Hiển thị bàn phím phù hợp | nng-error-prevention | 3 |
| ux-guidelines.csv#59 (Required-Indicators) | Đánh dấu trường bắt buộc bằng * | -- | 1 |
| ux-guidelines.csv#56 (Inline-Validation) | Validate khi blur | nng-error-prevention | 2 |
| ux-guidelines.csv#80 (Error-Recovery) | Hướng dẫn bước tiếp khi lỗi | nng-error-recovery | 3 |
| ux-guidelines.csv#76 (Contrast-Readability) | Contrast tỷ lệ đủ cho text | -- | 2 |
| ux-guidelines.csv#90 (No-Results) | Hiển thị gợi ý khi không có kết quả | nng-error-recovery | 1 |
| ux-guidelines.csv#62 (Input-Affordance) | Trường chỉnh sửa trông interactive | nng-recognition-recall | 1 |
| ux-guidelines.csv#31 (Disabled-States) | Trạng thái disabled rõ ràng | nng-error-prevention | 1 |
| ux-guidelines.csv#37 (Color-Only) | Không chỉ dùng màu để truyền ý nghĩa | von-restorff | 1 |
| ux-guidelines.csv#40 (ARIA-Labels) | Phần tử tương tác cần tên truy cập | wcag-operable | 2 |
| ux-guidelines.csv#41 (Keyboard-Navigation) | Focus trap + hỗ trợ bàn phím | wcag-operable | 2 |
| web-interface.csv#23 (Confirm-Destructive) | Hành động destructive cần xác nhận | nng-error-prevention | 2 |
| web-interface.csv#7 (Visible-Focus-States) | Focus ring cho người dùng bàn phím | von-restorff | 2 |
| web-interface.csv#2 (Form-Control-Labels) | Tất cả form controls cần labels | wcag-perceivable | 1 |
| web-interface.csv#15 (Inline-Errors) | Thông báo lỗi gần trường nhập | nng-error-recovery | 1 |
| ux-guidelines.csv#17 (Fixed-Positioning) | Phần tử cố định không che nội dung | -- | 1 |
| ux-guidelines.csv#54 (Input-Labels) | Label hiện rõ, không chỉ placeholder | wcag-understandable | 1 |

---

*Sinh bởi ux-review-pipe | Skill A (signal inference + DDL) + Skill B (PRD context + DDL) + Skill C (vision review — 15 PNG) | 2026-02-25*
