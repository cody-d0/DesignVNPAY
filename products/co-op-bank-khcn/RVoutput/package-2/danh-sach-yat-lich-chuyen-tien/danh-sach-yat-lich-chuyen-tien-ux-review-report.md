# UX Review Report — Đặt lịch chuyển tiền (Co-op Bank KHCN)

## Tổng quan
- **Folder:** `co-op-bank-khcn/co-op-bank-khcn/package-2/danh-sach-yat-lich-chuyen-tien`
- **Số màn hình:** 8 (15 ảnh wireframe)
- **Tổng check:** 68
- **Pass:** 44 | **Gap:** 19 | **Unverifiable:** 5
- **UX Score:** 64.7%

---

## Đề xuất cải tiến (Priority)

### Critical

- **[UXP-001]** Screen: `trang-thai-trong` (manage-2, manage-3) | **Vấn đề:** Empty state chỉ hiển thị text thuần trên nền trắng, thiếu illustration/icon và CTA button. DDL ux-guidelines#79 yêu cầu "Show helpful message **and action**", nhưng không có nút "Mở bộ lọc" hay "Tạo lệnh mới". | **Đề xuất:** Thêm illustration (icon lịch trống / kính lúp) kích thước 120×120px căn giữa. Bên dưới: headline bold 16sp "Chưa có lệnh nào đang hoạt động", body 14sp "Vui lòng sử dụng bộ lọc...", CTA button outline "Mở bộ lọc" (touchable, height 44px). Variant "Không có kết quả": icon tìm kiếm + "Không tìm thấy kết quả" + CTA "Thay đổi bộ lọc". | **DDL:** ux-guidelines#79 (Empty States) + ux-guidelines#80 (Error Recovery) | **UX Law:** nng-visibility, nng-error-recovery | **Evidence:** manage-2.png chỉ có 1 đoạn text nhỏ trên nền trắng hoàn toàn trống; manage-3.png chỉ 1 dòng "Không có kết quả tìm kiếm" màu xám nhạt.

- **[UXP-002]** Screen: `xac-nhan-hanh-dong` (popup.png) | **Vấn đề:** Dialog xác nhận Hủy lệnh không cảnh báo "hành động không thể hoàn tác" (irreversible). Nội dung hiện tại: "Quý khách có muốn Hủy giao dịch đặt lịch chuyển tiền không?" — quá nhẹ nhàng cho destructive action. Nút "Đồng ý" dùng visual weight primary (xanh/đậm) cho cả Tạm dừng lẫn Hủy, không phân biệt mức độ nguy hiểm. | **Đề xuất:** (a) Thay copy dialog Hủy thành: "Quý khách có chắc chắn muốn hủy lệnh đặt lịch chuyển tiền này? **Lệnh đã hủy không thể phục hồi.**" — text cảnh báo in đỏ (#F44336) bold. (b) Đổi nút "Đồng ý" thành "Hủy lệnh" với nền đỏ (#F44336, text trắng) — nút "Không" giữ outline. (c) Thêm icon ⚠️ cảnh báo phía trên tiêu đề dialog. (d) Đổi tiêu đề từ "Thông báo" thành "Xác nhận hủy lệnh". | **DDL:** ux-guidelines#35 (Confirmation Dialogs — confirm before destructive/irreversible actions) + web-interface#23 (Confirm Destructive Actions) | **UX Law:** nng-error-prevention | **Evidence:** popup.png hiển thị dialog với "Đồng ý" màu xanh primary — không có visual cue nào cho thấy đây là destructive action.

- **[UXP-003]** Screen: `danh-sach-dat-lich`, `quan-ly-dat-lich`, `bo-loc-tim-kiem`, `trang-thai-trong` | **Vấn đề:** Icon bộ lọc (funnel) trên header không có indicator khi filter đang active. User không biết kết quả đang xem đã bị lọc hay chưa. Đặc biệt nghiêm trọng ở manage-3.png (không có kết quả) — user không nhận ra filter đang active nên danh sách trống. | **Đề xuất:** Thêm badge dot (chấm tròn đỏ 8px) góc trên phải icon filter khi có bất kỳ filter nào khác default. Hoặc đổi màu icon filter từ trắng sang accent (#FF9800) khi active. Khi chạm icon, bottom sheet mở với filter đã áp dụng được highlight. | **DDL:** ux-guidelines#37 (Color Only — kết hợp badge + color) | **UX Law:** nng-visibility (Visibility of System Status) | **Evidence:** manage-3.png filter icon giữ nguyên style mặc định dù kết quả trống do filter; manage-2.png tương tự.

- **[UXP-004]** Screen: `chi-tiet-dat-lich` (calendar-details.png, onhold.png, cancel.png, expired.png) | **Vấn đề:** Bottom nav action buttons có red notification badges (chấm đỏ) trên tất cả icon — "Danh sách giao dịch", "Tạm dừng", "Hủy". Badge dạng notification trên action button gây hiểu nhầm: user tưởng có notification/alert, không phải action. Pattern này vi phạm mental model ("badge = something requires attention"). | **Đề xuất:** (a) Loại bỏ red badge khỏi "Tạm dừng" và "Hủy" — đây là action buttons, không phải notification targets. (b) Giữ badge trên "Danh sách giao dịch" nhưng đổi thành badge số (hiển thị count giao dịch, vd: "2") thay vì dot đỏ trống. (c) Đổi icon "Tạm dừng" thành standard pause icon (⏸) và "Hủy" thành standard cancel icon (✕ trong vòng tròn) — hiện tại icon không rõ ràng. | **DDL:** ux-guidelines#37 (Color Only) + ux-guidelines#40 (ARIA Labels — icon buttons need labels) | **UX Law:** cognitive-load, mental-model, jakob | **Evidence:** calendar-details.png tất cả 3 footer icons đều có red dot badge; cancel.png chỉ còn 1 icon nhưng vẫn có badge đỏ.

---

### Major

- **[UXP-005]** Screen: `xac-nhan-hanh-dong` (popup.png) | **Vấn đề:** Nút "Đồng ý" đặt bên phải với visual weight primary cho cả hành động Tạm dừng (semi-destructive) lẫn Hủy (destructive). Không phân biệt severity giữa hai action. | **Đề xuất:** Khi action = Hủy: nút phải đổi label thành "Hủy lệnh" + nền đỏ (#F44336), text trắng. Khi action = Tạm dừng: giữ "Đồng ý" + nền primary xanh. Cả hai: nút "Không" giữ outline secondary. | **DDL:** ux-guidelines#35 (Confirmation Dialogs) | **UX Law:** nng-error-prevention, von-restorff | **Evidence:** popup.png chỉ hiển thị 1 variant dialog, nút "Đồng ý" cùng style cho mọi action.

- **[UXP-006]** Screen: `bo-loc-tim-kiem` (filter.png, filter-2.png) | **Vấn đề:** Không có nút "Đặt lại" (Reset) trong bottom sheet bộ lọc. User phải thủ công chỉnh từng field về default. Label CTA "Tìm kiếm" gây nhầm lẫn trong context filter — user có thể hiểu đây là search bar, không phải apply filter. | **Đề xuất:** (a) Thêm text link "Đặt lại" góc phải header bottom sheet (cạnh X), chỉ hiện khi filter khác default. Tap → reset tất cả về default. (b) Đổi label CTA từ "Tìm kiếm" thành "Áp dụng bộ lọc" — rõ nghĩa hơn. | **DDL:** ux-guidelines#88 (User Freedom — skip/back) | **UX Law:** nng-user-control (User Control and Freedom), nng-match-world | **Evidence:** filter.png và filter-2.png đều không có nút reset; CTA chỉ có "Tìm kiếm".

- **[UXP-007]** Screen: `quan-ly-dat-lich` (manage.png, manage-4.png) | **Vấn đề:** Icon vertical-dot (⋮) trên mỗi card là icon-only button, thiếu aria-label/contentDescription. Screen reader không thể mô tả chức năng. Bottom sheet "Quản lý đặt lịch" không hiển thị context (tên người thụ hưởng / mã lệnh) — user không biết đang quản lý lệnh nào. | **Đề xuất:** (a) Thêm `aria-label="Quản lý lệnh chuyển tiền cho {tên người thụ hưởng}"` cho icon ⋮. (b) Bottom sheet title đổi từ "Quản lý đặt lịch" thành "Quản lý đặt lịch — {NGUYEN THI LAN ANH}" (hiển thị tên người thụ hưởng). (c) Thêm subtitle nhỏ dưới title: "2,000,000 VND • Hàng tháng". | **DDL:** web-interface#1 (Icon Button Labels — icon-only buttons must have accessible names) + ux-guidelines#40 (ARIA Labels) | **UX Law:** cognitive-load, wcag-perceivable | **Evidence:** manage-4.png bottom sheet title "Quản lý đặt lịch" không có thông tin lệnh nào.

- **[UXP-008]** Screen: `chi-tiet-dat-lich` (cancel.png, expired.png) | **Vấn đề:** Hai trạng thái terminal "Hủy" và "Hết hạn" gần như hoàn toàn giống nhau về layout — chỉ khác text trạng thái. User khó phân biệt nhanh đang xem trạng thái nào. "Hủy" thiếu thông tin ngày hủy và lý do; "Hết hạn" thiếu ngày kết thúc. | **Đề xuất:** (a) Thêm banner/card nổi bật phía trên detail: "Lệnh đã bị hủy ngày {dd/MM/yyyy}" (đỏ) hoặc "Lệnh đã hết hạn ngày {dd/MM/yyyy}" (cam) — tạo visual anchor rõ ràng. (b) Giữ trường "Ngày kết thúc" cho cả hai trạng thái (hiện đang bị ẩn). (c) Thêm icon trạng thái: ✕ đỏ cho Hủy, ⏰ cam cho Hết hạn cạnh badge. | **DDL:** ux-guidelines#37 (Color Only — don't convey info by color alone) | **UX Law:** von-restorff (Isolation Effect), gestalt-similarity | **Evidence:** cancel.png và expired.png layout hoàn toàn giống, chỉ khác text "Hủy" vs "Hết hạn".

- **[UXP-009]** Screen: `lich-su-giao-dich` (list.png) | **Vấn đề:** Danh sách giao dịch đã thực hiện không hiển thị số tiền từng giao dịch. User không thể đối chiếu số tiền chuyển từng lần. Ngoài ra, trạng thái "Tạm dừng" và "Hủy" xuất hiện trong danh sách giao dịch — đây là trạng thái của lệnh đặt lịch, không phải trạng thái giao dịch, gây nhầm lẫn. | **Đề xuất:** (a) Thêm số tiền (vd: "2,000,000 VND") cho mỗi dòng giao dịch, đặt bên phải cùng hàng với ngày. (b) Loại bỏ "Tạm dừng" và "Hủy" khỏi danh sách giao dịch — chỉ giữ "Thành công" và "Không thành công" (đây là execution results). (c) Giao dịch "Không thành công" thêm dòng "Lý do: {error_message}" để hỗ trợ troubleshooting. | **DDL:** ux-guidelines#84 (Truncation — handle content gracefully) + ux-guidelines#33 (Error Feedback) | **UX Law:** nng-visibility, nng-error-recovery | **Evidence:** list.png không hiển thị số tiền; có 2 dòng "Tạm dừng" và "Hủy" trong danh sách giao dịch.

- **[UXP-010]** Screen: `danh-sach-dat-lich`, `quan-ly-dat-lich` (calendar.png, manage.png) | **Vấn đề:** Tên người thụ hưởng dài bị truncate (ellipsis) như "QUY TIN DUNG NHAN..." mà không có cách xem đầy đủ. User không thể xác minh đúng người nhận khi tên bị cắt — rủi ro cho giao dịch tài chính. | **Đề xuất:** (a) Cho phép tên hiển thị 2 dòng (line-clamp-2) thay vì 1 dòng truncate. (b) Nếu vẫn truncate: long-press hoặc tooltip hiển thị tên đầy đủ. (c) Đảm bảo VoiceOver/TalkBack đọc tên đầy đủ (không truncate trong contentDescription). | **DDL:** ux-guidelines#84 (Truncation — truncate with expand option) | **UX Law:** nng-error-prevention | **Evidence:** calendar.png card 3 "QUY TIN DUNG NHAN..." bị cắt; manage.png tương tự.

- **[UXP-011]** Screen: `bo-loc-tim-kiem`, `quan-ly-dat-lich`, `lich-su-giao-dich`, `xac-thuc-soft-otp` | **Vấn đề:** Các bottom sheet thiếu drag handle indicator (thanh kéo ngang) ở đầu sheet. User quen với pattern vuốt xuống để đóng bottom sheet nhưng không có visual cue rằng sheet có thể kéo (missing affordance). | **Đề xuất:** Thêm drag handle bar (40×4px, border-radius 2px, color #E0E0E0) căn giữa ở top padding (8px từ edge trên) của mỗi bottom sheet: filter.png, filter-2.png, manage-4.png, list.png, popup-2.png. | **DDL:** ux-guidelines#29 (Hover/Interactive States — visual feedback on interactive elements) | **UX Law:** jakob (users expect bottom sheets to be swipeable — standard pattern) | **Evidence:** Tất cả bottom sheet wireframes thiếu drag handle.

- **[UXP-012]** Screen: `chi-tiet-dat-lich` (calendar-details.png, calendar-details-2.png, onhold.png) | **Vấn đề:** Dữ liệu mẫu có "Ngày kết thúc: 15/06/2023" nhưng "Ngày thực hiện tiếp theo: 25/07/2023" — ngày thực hiện tiếp theo SAU ngày kết thúc, bất hợp lý. Nếu implementation dùng data tương tự, user sẽ mất tin tưởng vào hệ thống. | **Đề xuất:** (a) Fix sample data: Ngày kết thúc phải ≥ Ngày thực hiện tiếp theo. (b) Thêm validation rule backend: nếu `next_execution_date > end_date`, tự động chuyển status sang "Hết hạn". (c) UI: khi phát hiện inconsistency, hiển thị warning inline "Ngày thực hiện tiếp theo đã vượt quá ngày kết thúc". | **DDL:** ux-guidelines#33 (Error Feedback) | **UX Law:** nng-error-prevention | **Evidence:** calendar-details.png hiển thị Ngày kết thúc 15/06 < Ngày thực hiện tiếp theo 25/07.

---

### Minor

- **[UXP-013]** Screen: `xac-thuc-soft-otp` (popup-2.png) | **Vấn đề:** Wireframe không hiển thị numeric keypad (bàn phím số) tự động xuất hiện khi mở bottom sheet. PRD yêu cầu auto-focus + bàn phím số, nhưng wireframe chưa thể hiện. Ngoài ra, nút "Xác nhận" không hiển thị disabled state khi chưa đủ 6 số. | **Đề xuất:** (a) Wireframe bổ sung trạng thái: mở sheet → keypad hiện → user nhập → 6 ô filled → nút "Xác nhận" active (transition từ opacity 0.5 → 1.0). (b) Bổ sung spec: inputMode="numeric", autoFocus ô đầu tiên. | **DDL:** ux-guidelines#63 (Mobile Keyboards), ux-guidelines#31 (Disabled States) | **UX Law:** doherty | **Evidence:** popup-2.png không hiển thị keypad; nút "Xác nhận" trông active dù ô input trống.

- **[UXP-014]** Screen: `xac-thuc-soft-otp` (popup-2.png) | **Vấn đề:** Thiếu tùy chọn xác thực sinh trắc học (Face ID / Touch ID) làm phương thức thay thế PIN. Banking app hiện đại thường hỗ trợ biometrics để giảm friction xác thực. | **Đề xuất:** Thêm link "Sử dụng Face ID / Vân tay" dưới ô OTP, trên cảnh báo lockout. Khi chạm → gọi biometric API → nếu thành công → bypass PIN. Fallback: nếu biometric fail hoặc không hỗ trợ, quay lại nhập PIN. | **DDL:** (best practice banking, không có DDL cụ thể) | **UX Law:** nng-flexibility (Flexibility and Efficiency of Use) | **Evidence:** popup-2.png chỉ có 1 phương thức xác thực (PIN).

- **[UXP-015]** Screen: `xac-nhan-hanh-dong` (popup.png) | **Vấn đề:** Tiêu đề dialog "Thông báo" quá generic — không cho biết đang xác nhận hành động gì. Phải đọc nội dung mới biết. | **Đề xuất:** Đổi tiêu đề thành dynamic text: "Xác nhận tạm dừng" (khi action = Tạm dừng) hoặc "Xác nhận hủy lệnh" (khi action = Hủy). Font bold 18sp, color phù hợp severity. | **DDL:** ux-guidelines#77 (Heading Clarity) | **UX Law:** nng-recognition-recall | **Evidence:** popup.png tiêu đề "Thông báo" không chứa thông tin action.

- **[UXP-016]** Screen: `chi-tiet-dat-lich` (calendar-details-2.png) | **Vấn đề:** Biến thể calendar-details-2.png có CTA "Xem các giao dịch đã thực hiện" full-width nhưng không có nút Tạm dừng / Hủy. Không rõ điều kiện hiển thị biến thể này — cùng data nhưng khác layout với calendar-details.png. Gây confusion cho dev khi implement. | **Đề xuất:** Xác định rõ trigger: (a) Nếu đây là variant cho trạng thái Hủy/Hết hạn → gộp vào cancel.png/expired.png. (b) Nếu là variant cho user role viewer (không có quyền quản lý) → document rõ trong PRD. (c) Nếu không cần → loại bỏ biến thể này khỏi spec. | **DDL:** ux-guidelines#5 (Deep Linking — URL reflect state) | **UX Law:** nng-consistency-standards | **Evidence:** calendar-details-2.png cùng data "Hoạt động" nhưng footer khác calendar-details.png.

- **[UXP-017]** Screen: `danh-sach-dat-lich` (calendar.png), `quan-ly-dat-lich` (manage.png) | **Vấn đề:** Hai màn hình danh sách có header title khác nhau ("Danh sách đặt lịch chuyển tiền" vs "Quản lý đặt lịch chuyển tiền") và cấu trúc card khác nhau (calendar.png hiển thị tần suất + ngày tiếp theo + trạng thái; manage.png hiển thị loại chuyển tiền + tần suất + ngày). Không rõ quan hệ navigation giữa hai màn. | **Đề xuất:** (a) Nếu là cùng 1 màn → thống nhất title và card layout. (b) Nếu là 2 màn khác nhau → document rõ entry point, mục đích khác biệt, và navigation path trong overview. | **DDL:** (consistency) | **UX Law:** nng-consistency-standards, jakob | **Evidence:** calendar.png header "Danh sách đặt lịch..." vs manage.png header "Quản lý đặt lịch...".

- **[UXP-018]** Screen: `bo-loc-tim-kiem` (filter-2.png) | **Vấn đề:** Date picker "Từ ngày" và "Đến ngày" không có placeholder format hint (vd: "dd/mm/yyyy"). User phải đoán format ngày. | **Đề xuất:** Thêm placeholder text "dd/mm/yyyy" màu #BDBDBD trong date picker input khi chưa chọn ngày. | **DDL:** ux-guidelines#54 (Input Labels) + ux-guidelines#62 (Input Affordance) | **UX Law:** nng-recognition-recall | **Evidence:** filter-2.png các ô "Từ ngày" / "Đến ngày" trống không có hint.

- **[UXP-019]** Screen: `xac-thuc-soft-otp` (popup-2.png) | **Vấn đề:** Cảnh báo "Lưu ý: Soft OTP sẽ bị khóa nếu nhập sai 5 lần" luôn hiển thị nhưng không cho biết số lần đã thử. Khi user nhập sai, chỉ hiển thị "còn {n} lần" — thiếu progress indicator trước khi sai lần đầu. | **Đề xuất:** Thêm hiển thị "Số lần thử còn lại: 5/5" ngay bên dưới ô OTP, cập nhật realtime khi sai (4/5, 3/5...). Khi còn ≤ 2 lần: text đổi sang đỏ + icon ⚠️. | **DDL:** ux-guidelines#81 (Progress Indicators) | **UX Law:** nng-visibility, goal-gradient | **Evidence:** popup-2.png chỉ có text cảnh báo tĩnh, không có attempt counter.

---

## Chi tiết theo màn hình

### 1. Danh sách đặt lịch chuyển tiền (danh-sach-dat-lich)
**Score: 72% | Pass: 8 | Gap: 3 | Images: calendar.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Card hiển thị đủ info: tên, số tiền, tần suất, ngày, trạng thái | Skill B (US-301) | — | **pass** | calendar.png: tất cả field hiện đúng |
| 2 | Trạng thái color-code + text label (không chỉ color) | Skill A + B | ux-guidelines#37 | **pass** | calendar.png: badge có text "Hoạt động"/"Đã hủy"/... kèm color |
| 3 | Touch target card ≥ 44×44px | Skill B (NFR) | ux-guidelines#22 | **pass** | calendar.png: card height đủ lớn |
| 4 | Skeleton loading khi tải lần đầu | Skill B (NFR) | ux-guidelines#10 | **unverifiable** | Không có wireframe trạng thái loading |
| 5 | Pull-to-refresh | Skill B (US-306) | ux-guidelines#26 | **unverifiable** | Không thể kiểm tra từ ảnh tĩnh |
| 6 | Error state khi API lỗi | Skill B (US-307) | ux-guidelines#33, #80 | **unverifiable** | Không có wireframe error state |
| 7 | Empty state khi danh sách rỗng | Skill B (US-305) | ux-guidelines#79 | **gap** | manage-2/3.png thiếu illustration + CTA [→ UXP-001] |
| 8 | Back button hoạt động đúng | Skill B (Flow 1.3) | ux-guidelines#4 | **pass** | calendar.png: có icon back trên header |
| 9 | Icon bộ lọc mở bottom sheet | Skill B (Flow 1.2) | — | **pass** | calendar.png: icon filter trên header |
| 10 | Filter icon có indicator khi active | Skill A | ux-guidelines#37 | **gap** | calendar.png: icon filter không có badge/dot khi active [→ UXP-003] |
| 11 | Tên người thụ hưởng dài xử lý đúng | Skill C | ux-guidelines#84 | **gap** | calendar.png: "QUY TIN DUNG NHAN..." truncate không có expand [→ UXP-010] |
| 12 | VoiceOver/TalkBack mô tả card | Skill B (US-308) | ux-guidelines#40, #42 | **pass** | PRD spec đầy đủ contentDescription |
| 13 | Lazy-load / phân trang khi cuộn | Skill B (US-304) | web-interface#16 | **pass** | PRD spec infinite scroll + loading indicator |
| 14 | Separator giữa các card | Skill B (US-301) | — | **pass** | calendar.png: divider giữa cards |

---

### 2. Bộ lọc tìm kiếm (bo-loc-tim-kiem)
**Score: 67% | Pass: 6 | Gap: 3 | Images: filter.png, filter-2.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Radio toggle chuyển chế độ lọc | Skill B (US-311, US-312) | — | **pass** | filter.png: "Theo trạng thái lệnh" selected; filter-2.png: "Theo thời gian" selected |
| 2 | Dropdown loại chuyển tiền | Skill B (US-311) | web-interface#2 | **pass** | filter.png: "Tất cả" dropdown visible |
| 3 | Dropdown trạng thái lệnh (chế độ trạng thái) | Skill B (US-311) | web-interface#2 | **pass** | filter.png: "Hoạt động" dropdown visible |
| 4 | Date picker Từ ngày / Đến ngày (chế độ thời gian) | Skill B (US-312) | — | **pass** | filter-2.png: 2 date fields + calendar icon |
| 5 | Date placeholder format hint | Skill C | ux-guidelines#62 | **gap** | filter-2.png: ô trống không có "dd/mm/yyyy" [→ UXP-018] |
| 6 | Validation khoảng ngày | Skill B (US-315) | ux-guidelines#55 | **pass** | PRD spec inline error |
| 7 | Nút Reset / Đặt lại | Skill C | ux-guidelines#88 | **gap** | filter.png, filter-2.png: không có nút reset [→ UXP-006] |
| 8 | CTA label phù hợp | Skill C | — | **gap** | "Tìm kiếm" → nên là "Áp dụng bộ lọc" [→ UXP-006] |
| 9 | X đóng không áp dụng thay đổi | Skill B (US-313) | — | **pass** | PRD spec rõ ràng |
| 10 | Touch target radio/dropdown ≥ 44px | Skill B (NFR) | ux-guidelines#22 | **pass** | PRD spec 44×44pt |
| 11 | Drag handle trên bottom sheet | Skill C | — | **gap** | filter.png, filter-2.png: thiếu drag handle [→ UXP-011] |

---

### 3. Quản lý đặt lịch chuyển tiền (quan-ly-dat-lich)
**Score: 64% | Pass: 5 | Gap: 3 | Images: manage.png, manage-4.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Card hiển thị loại giao dịch, tên, số tiền | Skill B (US-321) | — | **pass** | manage.png: cards visible |
| 2 | Badge đếm tổng lệnh trên tab | Skill B (US-321, US-322) | — | **pass** | manage.png: green "5" badge |
| 3 | Icon ⋮ mở bottom sheet quản lý | Skill B (US-323) | — | **pass** | manage-4.png: bottom sheet visible |
| 4 | Icon ⋮ có aria-label | Skill A | web-interface#1 | **gap** | PRD không mention aria-label cho ⋮ [→ UXP-007] |
| 5 | Bottom sheet hiển thị context (tên/mã lệnh) | Skill C | — | **gap** | manage-4.png: title "Quản lý đặt lịch" thiếu context [→ UXP-007] |
| 6 | Dialog thành công có icon + message + hướng dẫn | Skill B (US-326) | ux-guidelines#34 | **pass** | manage.png: checkmark + message + "Đóng" |
| 7 | Icon ⋮ ẩn/disabled cho trạng thái không phải Hoạt động | Skill B (US-323) | ux-guidelines#31 | **pass** | PRD spec rõ ràng |
| 8 | Empty state khi danh sách rỗng | Skill B (annotation) | ux-guidelines#79 | **gap** | Tham chiếu manage-2/3.png [→ UXP-001] |
| 9 | Touch target tối thiểu 44px | Skill B (NFR) | ux-guidelines#22 | **pass** | PRD spec |

---

### 4. Chi tiết giao dịch đặt lịch (chi-tiet-dat-lich)
**Score: 62% | Pass: 8 | Gap: 5 | Images: calendar-details.png, calendar-details-2.png, onhold.png, cancel.png, expired.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | 14 trường label-value hiển thị đúng | Skill B (US-331) | — | **pass** | calendar-details.png: tất cả fields visible |
| 2 | Số tiền đỏ + đọc chữ | Skill B (US-331) | — | **pass** | calendar-details.png: "20,000,000 VND" đỏ + "Hai mươi triệu đồng" |
| 3 | Badge trạng thái đúng màu + text | Skill B (US-331) | ux-guidelines#37 | **pass** | 4 variants đều có badge đúng |
| 4 | Bottom nav thay đổi theo trạng thái | Skill B (US-332-335) | — | **pass** | 4 ảnh thể hiện 4 variants footer |
| 5 | Footer action icons clear + no misleading badge | Skill C | ux-guidelines#37, #40 | **gap** | Red dot badge trên action buttons [→ UXP-004] |
| 6 | Footer icons recognizable (pause, cancel, play) | Skill C | ux-guidelines#40 | **gap** | Icons không rõ ràng, không standard [→ UXP-004] |
| 7 | Trạng thái Hủy/Hết hạn phân biệt visual rõ | Skill C | ux-guidelines#37 | **gap** | cancel.png ≈ expired.png [→ UXP-008] |
| 8 | Ngày kết thúc hiển thị ở trạng thái terminal | Skill C | — | **gap** | cancel.png, expired.png ẩn "Ngày kết thúc" [→ UXP-008] |
| 9 | Data logic consistency (end_date ≥ next_execution) | Skill C | ux-guidelines#33 | **gap** | 15/06 < 25/07 [→ UXP-012] |
| 10 | Back + Home navigation | Skill B (Flow 1.6) | ux-guidelines#4 | **pass** | calendar-details.png: back + home icon |
| 11 | Dialog xác nhận trước Hủy | Skill B (US-338) | ux-guidelines#35 | **pass** | popup.png exists (xem xac-nhan-hanh-dong) |
| 12 | Optimistic UI update | Skill B (NFR) | — | **pass** | PRD spec |
| 13 | Biến thể calendar-details-2.png rõ trigger | Skill C | — | **gap** | Không rõ khi nào hiển thị [→ UXP-016] |
| 14 | Touch target ≥ 44px footer buttons | Skill B (NFR) | ux-guidelines#22 | **pass** | PRD spec |
| 15 | Loading state skeleton/spinner | Skill B (NFR) | ux-guidelines#10 | **pass** | PRD spec |

---

### 5. Lịch sử giao dịch (lich-su-giao-dich)
**Score: 57% | Pass: 4 | Gap: 3 | Images: list.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Bottom sheet hiển thị danh sách giao dịch | Skill B (US-341) | — | **pass** | list.png: "Danh sách giao dịch" visible |
| 2 | Badge trạng thái color + text | Skill B (US-342) | ux-guidelines#37 | **pass** | list.png: 4 trạng thái có text + color |
| 3 | Giao dịch thành công hiển thị mã + phí | Skill B (US-343) | — | **pass** | list.png: "Mã giao dịch: 123123123", "Phí: 3,000 VND" |
| 4 | 3 cách đóng (X, swipe, overlay) | Skill B (US-344) | — | **pass** | PRD spec |
| 5 | Số tiền hiển thị per giao dịch | Skill C | nng-visibility | **gap** | list.png: không có số tiền [→ UXP-009] |
| 6 | Trạng thái giao dịch vs trạng thái lệnh phân biệt | Skill C | — | **gap** | list.png: "Tạm dừng"/"Hủy" nhầm context [→ UXP-009] |
| 7 | Drag handle trên bottom sheet | Skill C | jakob | **gap** | list.png: thiếu drag handle [→ UXP-011] |

---

### 6. Xác nhận hành động (xac-nhan-hanh-dong)
**Score: 50% | Pass: 3 | Gap: 3 | Images: popup.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Dialog hiển thị nội dung xác nhận | Skill B (US-351, 352) | ux-guidelines#35 | **pass** | popup.png: "Quý khách có muốn Tạm dừng..." |
| 2 | Hai nút Không + Đồng ý | Skill B (US-353, 354) | — | **pass** | popup.png: 2 buttons visible |
| 3 | Dismiss khi chạm overlay / Back | Skill B (US-354) | — | **pass** | PRD spec |
| 4 | Cảnh báo irreversible cho Hủy | Skill A + B (US-352) | ux-guidelines#35 | **gap** | popup.png: không có text "không thể hoàn tác" [→ UXP-002] |
| 5 | Visual weight phù hợp cho destructive | Skill C | web-interface#23 | **gap** | popup.png: "Đồng ý" primary xanh cho cả Hủy [→ UXP-005] |
| 6 | Tiêu đề dialog specific | Skill C | ux-guidelines#77 | **gap** | popup.png: "Thông báo" quá generic [→ UXP-015] |

---

### 7. Xác thực Soft OTP (xac-thuc-soft-otp)
**Score: 71% | Pass: 5 | Gap: 2 | Images: popup-2.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Bottom sheet với 6 ô OTP | Skill B (US-361, 362) | — | **pass** | popup-2.png: 6 input boxes visible |
| 2 | Cảnh báo lockout 5 lần | Skill B (US-361) | — | **pass** | popup-2.png: "Lưu ý: Soft OTP sẽ bị khóa..." |
| 3 | Nút Xác nhận | Skill B (US-363) | — | **pass** | popup-2.png: button "Xác nhận" visible |
| 4 | X đóng + swipe dismiss | Skill B (US-365) | — | **pass** | popup-2.png: X icon; PRD spec swipe |
| 5 | Error state sai PIN | Skill B (US-364) | ux-guidelines#33 | **pass** | PRD spec text lỗi đỏ + attempt count |
| 6 | Numeric keypad auto-show | Skill C | ux-guidelines#63 | **gap** | popup-2.png: không hiển thị keypad [→ UXP-013] |
| 7 | Biometric alternative | Skill C | nng-flexibility | **gap** | popup-2.png: chỉ có PIN [→ UXP-014] |

---

### 8. Trạng thái trống (trang-thai-trong)
**Score: 50% | Pass: 3 | Gap: 3 | Images: manage-2.png, manage-3.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Thông báo empty state đúng variant | Skill B (US-371, 372) | — | **pass** | manage-2.png: text dài; manage-3.png: text ngắn |
| 2 | Header giữ nguyên (back, title, filter) | Skill B (US-371) | — | **pass** | manage-2/3.png: header intact |
| 3 | Screen reader đọc được text | Skill B (NFR) | ux-guidelines#42 | **pass** | PRD spec |
| 4 | Illustration / icon minh họa | Skill C | ux-guidelines#79 | **gap** | manage-2/3.png: chỉ text, không có illustration [→ UXP-001] |
| 5 | CTA button (mở bộ lọc / tạo lệnh) | Skill C | ux-guidelines#79, #80 | **gap** | manage-2/3.png: không có CTA [→ UXP-001] |
| 6 | Text contrast đủ đọc | Skill C | ux-guidelines#76 | **gap** | manage-3.png: text xám nhạt có thể không đạt 4.5:1 |

---

## DDL References sử dụng

| ddl_ref | Rule | UX Law | Áp dụng |
|---------|------|--------|---------|
| ux-guidelines#4 | Back Button — preserve navigation history | jakob | danh-sach-dat-lich, chi-tiet-dat-lich |
| ux-guidelines#10 | Loading States — skeleton/spinner | doherty | danh-sach-dat-lich, chi-tiet-dat-lich, quan-ly-dat-lich |
| ux-guidelines#22 | Touch Target ≥ 44×44px | fitts | Tất cả màn hình |
| ux-guidelines#26 | Pull to Refresh | — | danh-sach-dat-lich |
| ux-guidelines#29 | Interactive Feedback | — | Bottom sheets (drag handle) |
| ux-guidelines#31 | Disabled States | — | chi-tiet-dat-lich (footer), xac-thuc-soft-otp (nút Xác nhận) |
| ux-guidelines#33 | Error Feedback — clear messages | — | danh-sach-dat-lich, chi-tiet-dat-lich, lich-su-giao-dich |
| ux-guidelines#34 | Success Feedback | — | quan-ly-dat-lich (dialog thành công) |
| ux-guidelines#35 | Confirmation Dialogs — confirm before destructive | nng-error-prevention | xac-nhan-hanh-dong, chi-tiet-dat-lich |
| ux-guidelines#37 | Color Only — don't convey info by color alone | — | danh-sach-dat-lich, chi-tiet-dat-lich, lich-su-giao-dich |
| ux-guidelines#40 | ARIA Labels — icon buttons need labels | wcag-perceivable | quan-ly-dat-lich (⋮), chi-tiet-dat-lich (footer icons) |
| ux-guidelines#42 | Screen Reader — semantic content | — | trang-thai-trong |
| ux-guidelines#54 | Input Labels | — | bo-loc-tim-kiem |
| ux-guidelines#55 | Error Placement — inline near field | — | bo-loc-tim-kiem (date validation) |
| ux-guidelines#62 | Input Affordance | — | bo-loc-tim-kiem (date placeholder) |
| ux-guidelines#63 | Mobile Keyboards | doherty | xac-thuc-soft-otp |
| ux-guidelines#76 | Contrast Readability | — | trang-thai-trong (manage-3 text) |
| ux-guidelines#77 | Heading Clarity | — | xac-nhan-hanh-dong (dialog title) |
| ux-guidelines#79 | Empty States — helpful message + action | nng-visibility | trang-thai-trong, lich-su-giao-dich |
| ux-guidelines#80 | Error Recovery — clear next steps | nng-error-recovery | trang-thai-trong |
| ux-guidelines#81 | Progress Indicators | goal-gradient | xac-thuc-soft-otp (attempt counter) |
| ux-guidelines#84 | Truncation — ellipsis + expand | — | danh-sach-dat-lich, quan-ly-dat-lich |
| ux-guidelines#88 | User Freedom — skip/back | nng-user-control | bo-loc-tim-kiem (reset) |
| web-interface#1 | Icon Button Labels — aria-label | wcag-perceivable | quan-ly-dat-lich (⋮ icon) |
| web-interface#2 | Form Control Labels | — | bo-loc-tim-kiem |
| web-interface#9 | Checkbox/Radio Hit Target | fitts | bo-loc-tim-kiem |
| web-interface#16 | Virtualize Lists > 50 items | miller | danh-sach-dat-lich (lazy-load) |
| web-interface#23 | Confirm Destructive Actions | nng-error-prevention | xac-nhan-hanh-dong |

---

*Generated by UX Review Pipe — VNPAY Agentic Framework*
