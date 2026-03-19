# UX Review Report — Co-op Bank KHCN: Chuyển tiền nội bộ khác chủ

## Tổng quan

- **Folder:** `co-op-bank-khcn/co-op-bank-khcn/package-2/chuyen-tien-noi-bo-khac-chu`
- **Số màn hình:** 3 (7 states) | **Tổng check:** 49
- **Pass:** 26 | **Gap:** 17 | **Unverifiable:** 6
- **UX Score: 60%**
- **Figma source:** `kPft93N2A3gYOC3YwuXpQR` | Screenshots reviewed via Figma MCP

| Màn hình | States | Pass | Gap | Unverifiable | Score |
|---|---|---|---|---|---|
| Nhập thông tin chuyển tiền | 4 | 10 | 8 | 2 | 56% |
| Xác nhận giao dịch | 2 | 7 | 6 | 2 | 54% |
| Kết quả giao dịch | 1 | 9 | 3 | 2 | 75% |

---

## Đề xuất cải tiến (Priority)

### Critical

- **[UXP-001]** Screen: nhap-thong-tin-chuyen-tien (State 3) | **Mất confirm dialog cho đặt lịch** | PRD US-005 mô tả popup "Bạn có chắc chắn..." với nút "Đồng ý"/"Hủy" khi đặt lịch, nhưng wireframe State 3 thực tế là popup validation "Vui lòng nhập Thông tin thụ hưởng là số tài khoản để sử dụng chức năng Đặt lịch" chỉ có nút "Đóng". Confirm dialog xác nhận đặt lịch **không tồn tại** trong bộ wireframe. | **Đề xuất:** Bổ sung wireframe State 3b: popup xác nhận đặt lịch với nội dung "Bạn có chắc chắn muốn đặt lịch chuyển tiền định kỳ?", nút "Đồng ý" (primary) + "Hủy" (secondary). | DDL: `ux-guidelines.csv#35` (Confirmation Dialogs) + `nng-error-prevention` | Evidence: Figma 134:19855 cho thấy popup validation, không phải confirmation.

- **[UXP-002]** Screen: nhap-thong-tin-chuyen-tien | **Thiếu toàn bộ error states cho form** | NFR#7 mô tả "Inline error (đỏ) dưới field lỗi, toast cho lỗi network, popup cho lỗi business" nhưng không có wireframe nào thể hiện: số tài khoản không hợp lệ, số tiền vượt số dư, field bắt buộc trống, API lookup thất bại. | **Đề xuất:** Bổ sung wireframe State 5 (Form error): hiển thị inline error text đỏ (13px, `#e50019`) dưới mỗi field lỗi, vd: dưới input STK "Số tài khoản không hợp lệ", dưới input số tiền "Số tiền vượt quá số dư khả dụng". Border-bottom field lỗi đổi thành đỏ. | DDL: `ux-guidelines.csv#33` (Error Feedback) + `web-interface.csv#15` (Inline Errors) + `nng-error-recovery` | Evidence: Chỉ có popup giới hạn (State 4) và popup validation (State 3), không có inline error.

- **[UXP-003]** Screen: xac-nhan-giao-dich | **Thiếu OTP error/retry states** | NFR mô tả 3 error states (sai OTP: shake + clear, hết hạn: thông báo hết hạn, quá 3 lần: khóa giao dịch) nhưng wireframe chỉ có default state và happy path. | **Đề xuất:** Bổ sung 3 wireframe states cho OTP sheet: (a) Error state: 6 ô OTP viền đỏ + shake indicator + text "Mã OTP không đúng. Bạn còn 2 lần thử" (13px, `#e50019`), (b) Expired: text "Mã OTP đã hết hạn" + link "Gửi lại mã" (primary), (c) Locked: text "Giao dịch bị khóa tạm thời. Vui lòng thử lại sau hoặc liên hệ hotline 1900xxxx". | DDL: `ux-guidelines.csv#33` (Error Feedback) + `ux-guidelines.csv#80` (Error Recovery) + `nng-error-recovery` | Evidence: Figma 134:20006 chỉ hiển thị 6 ô trống + nút xác nhận.

### Major

- **[UXP-004]** Screen: nhap-thong-tin-chuyen-tien | **Thiếu loading state khi lookup tên người hưởng** | API lookup tên < 2s (NFR#2) nhưng không có wireframe cho trạng thái đang tra cứu. User nhập xong STK sẽ thấy blank trước khi tên hiện lên — gây confusion. | **Đề xuất:** Sau khi user nhập đủ STK, hiển thị skeleton text 1 dòng (height 16px, bg `#f6f7f9`, border-radius 4px, animate-pulse) tại vị trí tên người hưởng. Hoặc inline spinner (16px) bên phải input. Khi có kết quả → thay bằng tên. Khi lỗi → inline error "Không tìm thấy tài khoản". | DDL: `ux-guidelines.csv#10` (Loading States) + `ux-guidelines.csv#78` (Loading Indicators) + `doherty` | Evidence: Figma 134:19817 (State 2) hiển thị tên trực tiếp "NGUYEN HOANG HIEU", không có trạng thái chuyển tiếp.

- **[UXP-005]** Screen: xac-nhan-giao-dich | **Thiếu "Gửi lại mã" + countdown trong OTP sheet** | US-012 mô tả link "Gửi lại mã" sau countdown 60s nhưng wireframe OTP sheet không hiển thị. User không nhận được OTP sẽ không biết cách gửi lại. | **Đề xuất:** Thêm text "Gửi lại mã sau 59s" (muted, 13px) giữa OTP input và nút "Xác nhận". Sau countdown hết → chuyển thành link "Gửi lại mã" (primary, underline). Quá 5 lần → "Vui lòng liên hệ hotline 1900xxxx" (thay thế link). | DDL: `ux-guidelines.csv#80` (Error Recovery) + `nng-user-control` | Evidence: Figma 134:20006 OTP sheet chỉ có: instruction + 6 ô + nút, không có resend link.

- **[UXP-006]** Screen: ket-qua-giao-dich | **Thiếu failure state wireframe** | NFR#6 mô tả failure: icon × đỏ thay ✓ xanh, "Giao dịch thất bại", nút "Thử lại" thay "Tạo GD mới", hiển thị mã lỗi. Nhưng chỉ có wireframe success. Failure là trạng thái quan trọng — "peak-end" experience. | **Đề xuất:** Bổ sung wireframe failure state: (a) Icon ✕ đỏ (40×40px, `#e50019`) thay ✓ xanh, (b) Text "Giao dịch thất bại" (bold 15px, `#e50019`), (c) Mã lỗi: "Mã lỗi: ERR-1234" (muted 13px), (d) Mô tả: "Giao dịch không thể thực hiện. Vui lòng kiểm tra lại thông tin hoặc thử lại sau." (regular 13px), (e) Nút "Thử lại" (primary) + "Về trang chủ" (secondary/text). | DDL: `ux-guidelines.csv#80` (Error Recovery) + `peak-end` + `nng-error-recovery` | Evidence: Figma 134:20066 chỉ hiển thị success state.

- **[UXP-007]** All screens | **Thiếu progress indicator cho flow 3 bước** | Flow gồm 3 bước (Nhập → Xác nhận → Kết quả) nhưng user không có visual cue biết đang ở bước nào. Đặc biệt quan trọng khi form dài (scheduled transfer). | **Đề xuất:** Thêm step indicator bar dưới header (height 4px hoặc dot indicator): 3 steps — "Nhập thông tin" (active) → "Xác nhận" → "Kết quả". Dùng primary color cho step hiện tại, muted cho step chưa đến, accent cho step hoàn thành. Tại Screen 3 (kết quả), có thể ẩn hoặc đánh dấu tất cả completed. | DDL: `ux-guidelines.csv#81` (Progress Indicators) + `goal-gradient` | Evidence: Cả 3 header chỉ có title, không có step indicator.

- **[UXP-008]** Screen: nhap-thong-tin-chuyen-tien | **Nút "Tiếp tục" thiếu disabled + loading states** | Button luôn active (gradient) bất kể form đã điền hay chưa. Không có loading state khi submit. Có thể dẫn đến double-tap. | **Đề xuất:** (a) Disabled state: opacity 50%, cursor not-allowed khi required fields chưa hoàn tất. (b) Loading state: thay text "Tiếp tục" bằng spinner (16px white) + "Đang xử lý..." khi API call. Prevent double-tap. | DDL: `ux-guidelines.csv#32` (Loading Buttons) + `web-interface.csv#14` (Submit Button) + `doherty` | Evidence: Figma 134:19728 button luôn hiển thị active gradient.

- **[UXP-009]** Screen: xac-nhan-giao-dich | **TK nguồn không được mask trên màn xác nhận** | NFR#5 (Screen 1) nêu rõ "Không hiển thị đầy đủ STK nguồn trên màn xác nhận (mask)". Nhưng wireframe hiển thị "98712313123" không mask. | **Đề xuất:** Mask TK nguồn thành "****313123" (4 dấu * + 6 số cuối) hoặc "9871****3123" (4 số đầu + 4 dấu * + 4 số cuối). Giữ nguyên TK thụ hưởng (không mask vì user cần verify). | DDL: Security best practice + NFR#5 | Evidence: Figma 134:19985 hiển thị "98712313123" đầy đủ.

- **[UXP-010]** Screen: nhap-thong-tin-chuyen-tien (State 2) | **"Lưu ý" infobox bị che bởi sticky button** | Khi toggle Đặt lịch ON, phần "Lưu ý: Phí và VAT..." nằm sát cuối form nhưng nút "Tiếp tục" fixed ở bottom che mất nội dung. User có thể bỏ lỡ thông tin phí quan trọng. | **Đề xuất:** (a) Thêm padding-bottom 80px cho form container khi toggle ON để content không bị che. (b) Hoặc di chuyển "Lưu ý" lên trên button area. (c) Đảm bảo "Lưu ý" nằm trong viewport khi scroll hết. | DDL: `ux-guidelines.csv#17` (Fixed Positioning) + `ux-guidelines.csv#16` (Overflow Hidden) | Evidence: Figma 134:19817 — "Tiếp tục" button cắt ngang dưới cùng, "Lưu ý" bị ẩn phía sau.

- **[UXP-011]** Screens: xac-nhan-giao-dich + ket-qua-giao-dich | **"Nội dung giao dịch" hiển thị "Balance" — mock data không nhất quán** | Screen 1 hiển thị "NGUYEN HOANG KHAI chuyen tien" nhưng Screen 2 và 3 hiển thị "Balance". Gây nhầm lẫn khi review thiết kế — stakeholders có thể hiểu nhầm "Balance" là giá trị thực. | **Đề xuất:** Thống nhất mock data: Screen 2 + 3 nên hiển thị "NGUYEN HOANG KHAI chuyen tien" hoặc tương đương. Tránh placeholder text "Balance" trong wireframe final. | DDL: `ux-guidelines.csv#87` (Placeholder Content) + `nng-consistency-standards` | Evidence: Figma 134:19985 + 134:20066 hiển thị "Balance"; Figma 134:19728 hiển thị "NGUYEN HOANG KHAI chuyen tien".

### Minor

- **[UXP-012]** Screen: ket-qua-giao-dich | **Số tiền header vs chi tiết không khớp** | Header card hiển thị "50,000 VND" nhưng chi tiết hiển thị "20,000,000 VND". Mock data inconsistency gây confusion khi review. | **Đề xuất:** Thống nhất số tiền: header amount = chi tiết amount (vd: "20,000,000 VND"). | DDL: `ux-guidelines.csv#87` (Placeholder Content) | Evidence: Figma 134:20066 — "50,000 VND" ở header, "20,000,000 VND" ở detail row.

- **[UXP-013]** Screen: nhap-thong-tin-chuyen-tien | **Thiếu empty state cho danh bạ thụ hưởng (0/N)** | Wireframe hiển thị "(1/10)" nhưng không có state cho user mới chưa lưu danh bạ nào. User thấy section trống sẽ không biết cách bắt đầu. | **Đề xuất:** Khi danh bạ rỗng: thay "(0/0)" bằng helper text "Chưa có danh bạ thụ hưởng" (muted 13px). Giữ "Thêm người hưởng" button nổi bật hơn (icon + text + highlight). Ẩn hoặc disable section header count. | DDL: `ux-guidelines.csv#79` (Empty States) | Evidence: Figma 134:19728 chỉ hiển thị state (1/10).

- **[UXP-014]** Screen: nhap-thong-tin-chuyen-tien (State 2) | **Dropdown "Đối tượng chịu phí" không hiển thị khi toggle Đặt lịch ON** | State 2 (scheduled) không thể hiện dropdown "Đối tượng chịu phí" — có thể bị cuộn mất hoặc bị ẩn. User phải nhớ giá trị đã chọn. | **Đề xuất:** Đảm bảo "Đối tượng chịu phí" luôn visible trong cả hai states. Nếu form quá dài, cân nhắc accordion/collapse cho sections. | DDL: `nng-recognition-recall` (Recognition Rather Than Recall) | Evidence: Figma 134:19817 — không thấy "Đối tượng chịu phí" dropdown.

- **[UXP-015]** Screen: nhap-thong-tin-chuyen-tien (State 3) | **Popup "Thông báo" generic — không phân biệt validation vs confirmation** | Cả popup validation (State 3) và popup giới hạn (State 4) đều dùng title "Thông báo" và nút "Đóng". Không phân biệt được loại thông báo. | **Đề xuất:** (a) Validation popup: giữ "Thông báo" + icon ⚠️ warning vàng + "Đóng". (b) Limit popup: dùng icon ⛔ hoặc cảnh báo đỏ. (c) Confirm popup (mới, UXP-001): dùng title "Xác nhận đặt lịch" + 2 nút. Mỗi loại popup có visual cue riêng. | DDL: `nng-consistency-standards` + `gestalt-similarity` | Evidence: Figma 134:19855 và 134:19895 đều dùng cùng template.

---

## Chi tiết theo màn hình

### Nhập thông tin chuyển tiền

**Score: 56% | Pass: 10 | Gap: 8 | Unverifiable: 2 | Images: 134:19728, 134:19817, 134:19855, 134:19895**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Happy path liên tục (form → popup → next screen) | Flow | `ux-guidelines.csv#4` | **pass** | Form → Tiếp tục → popup/xác nhận giao dịch. Flow rõ ràng. |
| 2 | Error flow — inline validation cho form fields | Flow + DDL | `ux-guidelines.csv#33`, `web-interface.csv#15` | **gap** | Không có wireframe error state. NFR#7 mô tả nhưng không thể hiện. → UXP-002 |
| 3 | Back navigation hoạt động | Flow | `ux-guidelines.csv#4` | **pass** | Icon back (←) trên header. Figma 134:19728 hiển thị rõ. |
| 4 | Loading state cho beneficiary API lookup | Signal + DDL | `ux-guidelines.csv#10`, `doherty` | **gap** | Figma 134:19817 hiện tên trực tiếp, không có skeleton/spinner. → UXP-004 |
| 5 | Empty state cho danh bạ thụ hưởng (0/N) | DDL | `ux-guidelines.csv#79` | **gap** | Chỉ có state (1/10). Không có state khi danh bạ trống. → UXP-013 |
| 6 | Input focus states hiển thị | DDL | `web-interface.csv#7` | **gap** | Wireframe chỉ hiện default state cho input fields. Focus ring/border không thể hiện. |
| 7 | Button "Tiếp tục" disabled/loading states | DDL | `ux-guidelines.csv#32`, `web-interface.csv#14` | **gap** | Button luôn active gradient. Không có disabled/loading. → UXP-008 |
| 8 | Progress indicator (bước 1/3) | DDL | `ux-guidelines.csv#81`, `goal-gradient` | **gap** | Header chỉ có title, không có step indicator. → UXP-007 |
| 9 | Touch target ≥ 44×44px | NFR | `ux-guidelines.csv#22`, `fitts` | **pass** | NFR#3 nêu rõ 44×44px. Visual inspection: buttons và toggle đủ lớn. |
| 10 | Keyboard numeric cho số tiền/STK | NFR | `ux-guidelines.csv#63` | **pass** | NFR#6 nêu "Keyboard numeric cho số tiền/STK". |
| 11 | Aria-label cho icon buttons (back, home, contact) | DDL | `web-interface.csv#1` | **unverifiable** | Không thể verify từ visual wireframe. NFR#3 nêu `aria-label`. |
| 12 | Confirm popup cho scheduled transfer (US-005) | PRD + DDL | `ux-guidelines.csv#35`, `nng-error-prevention` | **gap** | Figma 134:19855 là validation popup, KHÔNG phải confirm. Confirm dialog mất. → UXP-001 |
| 13 | Date formatting nhất quán (dd/mm/yyyy) | DDL | `ux-guidelines.csv#85` | **pass** | "15/05/2023", "15/06/2023" — format nhất quán. |
| 14 | Character counter cho nội dung giao dịch | PRD | — | **pass** | "30/160" hiển thị rõ. Figma 134:19728 xác nhận. |
| 15 | Auto-fill nội dung giao dịch | PRD | — | **pass** | "NGUYEN HOANG KHAI chuyen tien" auto-filled. |
| 16 | Toggle đặt lịch ON/OFF states | PRD | — | **pass** | State 1 (OFF) + State 2 (ON) đều có wireframe. |
| 17 | Scroll smooth khi toggle expand | NFR | `ux-guidelines.csv#1` | **unverifiable** | Hành vi dynamic, không verify được từ static wireframe. |
| 18 | Field labels (không chỉ placeholder) | DDL | `ux-guidelines.csv#54`, `web-interface.csv#2` | **gap** | State 2 (Figma 134:19817) một số field dùng label generic từ Figma component. → UXP-014 |
| 19 | Phí/VAT disclosure khi đặt lịch | PRD | — | **pass** | "Lưu ý" infobox hiển thị. Nhưng bị che 1 phần bởi button. → UXP-010 |
| 20 | Popup giới hạn giao dịch (business rule) | Flow | — | **pass** | Figma 134:19895: "Số lần giao dịch không được vượt quá 10 lần". |

---

### Xác nhận giao dịch

**Score: 54% | Pass: 7 | Gap: 6 | Unverifiable: 2 | Images: 134:19985, 134:20006**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Happy path (review → chọn auth → OTP → confirm) | Flow | — | **pass** | State 1 (review) → State 2 (OTP sheet) liên tục. |
| 2 | OTP error states (sai/hết hạn/bị khóa) | Flow + DDL | `ux-guidelines.csv#33`, `nng-error-recovery` | **gap** | NFR#5 mô tả 3 error states nhưng không có wireframe. → UXP-003 |
| 3 | Back navigation + close OTP sheet | Flow | `ux-guidelines.csv#4`, `nng-user-control` | **pass** | Back (←) trên header + close (×) trên OTP sheet. Figma xác nhận. |
| 4 | "Gửi lại mã" OTP + countdown | PRD US-012 + DDL | `ux-guidelines.csv#80`, `nng-user-control` | **gap** | Figma 134:20006: OTP sheet không có resend link/countdown. → UXP-005 |
| 5 | OTP auto-focus + auto-advance | NFR | `ux-guidelines.csv#28` | **pass** | NFR#4 mô tả rõ. Wireframe hiện 6 ô riêng biệt (auto-advance implied). |
| 6 | OTP paste support | NFR | `web-interface.csv#12` | **pass** | NFR#3 nêu "hỗ trợ paste (không block clipboard)". |
| 7 | Button loading khi verify OTP | DDL | `ux-guidelines.csv#32`, `doherty` | **gap** | Nút "Xác nhận" không có loading state. → phụ thuộc UXP-008 pattern. |
| 8 | Phone number masking | NFR + DDL | Security | **pass** | "098****123" — mask đúng format (3 đầu + 4 sao + 3 cuối). Figma xác nhận. |
| 9 | Progress indicator (bước 2/3) | DDL | `ux-guidelines.csv#81`, `goal-gradient` | **gap** | Không có step indicator. → UXP-007 |
| 10 | Focus trap trong bottom sheet | NFR | `web-interface.csv#3` | **unverifiable** | Hành vi keyboard trap, không verify được từ static wireframe. |
| 11 | Escape key đóng bottom sheet | NFR | — | **unverifiable** | NFR#3 nêu nhưng không verify được từ wireframe. |
| 12 | TK nguồn masked trên review | NFR Screen 1 #5 | Security | **gap** | "98712313123" hiển thị không mask. NFR nêu rõ "mask". → UXP-009 |
| 13 | Bill detail đầy đủ tất cả fields | PRD US-010 | — | **pass** | 9 fields review + auth method. Tất cả hiển thị. |
| 14 | Blur overlay cho OTP sheet | PRD | — | **pass** | Figma 134:20006: overlay blur rõ ràng. |
| 15 | Mock data nhất quán (Nội dung GD) | DDL | `ux-guidelines.csv#87` | **gap** | "Balance" thay vì "NGUYEN HOANG KHAI chuyen tien". → UXP-011 |

---

### Kết quả giao dịch

**Score: 75% | Pass: 9 | Gap: 3 | Unverifiable: 2 | Images: 134:20066**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Success state hiển thị rõ | PRD | `ux-guidelines.csv#34` | **pass** | Logo + ✓ xanh + "Đặt lịch chuyển tiền thành công". Visual hierarchy mạnh (dark bg + white card). |
| 2 | Tất cả detail fields hiển thị | PRD US-020 | — | **pass** | 12 fields: Thời gian, TK nguồn, TK hưởng, Tên, Số tiền, Tần suất, Số lần, Ngày bắt đầu/kết thúc, Mã đặt lịch, Nội dung. |
| 3 | Share action available | PRD US-021 | — | **pass** | Icon "Chia sẻ" hiển thị rõ ở bottom card. Figma xác nhận. |
| 4 | Save image action available | PRD US-021 | — | **pass** | Icon "Lưu ảnh" hiển thị rõ cạnh Chia sẻ. |
| 5 | "Tạo giao dịch mới" CTA | PRD US-022 | — | **pass** | Button primary ở bottom. Figma 134:20066 xác nhận. |
| 6 | Home navigation | PRD US-023 | — | **pass** | Icon home visible trên header (left). |
| 7 | Back button disabled (không quay lại OTP) | NFR | `ux-guidelines.csv#4` | **pass** | Header không có back icon, chỉ có home. Đúng behavior. |
| 8 | Failure state wireframe | NFR #6 + DDL | `ux-guidelines.csv#80`, `peak-end` | **gap** | Chỉ có success. NFR mô tả failure nhưng không có wireframe. → UXP-006 |
| 9 | Pending/processing state | DB schema | — | **gap** | DB có status "PENDING" nhưng không có wireframe state. |
| 10 | Amount highlight đỏ + bold | PRD | `von-restorff` | **pass** | "50,000 VND" (green accent header) + "20,000,000 VND" (đỏ detail). Visual prominence ✓. |
| 11 | Receipt design (dark bg + dash divider) | PRD + DDL | `peak-end`, `aesthetic-usability` | **pass** | Dark blue background (#002a69) + floating white card + dash divider. Receipt metaphor rõ ràng. |
| 12 | Aria-label cho success icon | NFR | `web-interface.csv#1` | **unverifiable** | NFR#3 nêu `aria-label="Giao dịch thành công"` nhưng không verify từ wireframe. |
| 13 | Screen reader order (label → value) | NFR | `web-interface.csv#5` | **unverifiable** | Không verify được từ static wireframe. |
| 14 | Mock data: header amount vs detail amount | DDL | `ux-guidelines.csv#87` | **gap** | "50,000 VND" (header) ≠ "20,000,000 VND" (detail). → UXP-012 |

---

## Phát hiện thêm từ Vision Review (Skill C)

Các phát hiện dưới đây được rút ra trực tiếp từ phân tích ảnh Figma, bổ sung cho kết quả Skill A + B:

### 1. Spacing & Alignment
- **Nhất quán tốt:** Spacing giữa các sections, list items, và card elements đồng đều across 3 screens. Typography hierarchy (label muted → value bold) nhất quán.
- **Lưu ý:** State 2 (scheduled) làm form dài hơn đáng kể — cần test scroll behavior trên thiết bị nhỏ (320px width).

### 2. Color System
- **Primary #002a69 (dark blue):** Header gradient, button gradient, success card background → nhất quán.
- **Accent #e50019 (red):** Dùng cho: ngày kết thúc auto-computed, tần suất/số lần trên review, số tiền bằng chữ, amount kết quả → nhất quán cho "dynamic/computed values".
- **Concern:** Red color dùng cho cả "computed values" và tiềm năng "error states" — có thể gây nhầm lẫn khi implement error. Cân nhắc dùng orange (#f59e0b) hoặc red-600 (#dc2626) riêng cho errors.

### 3. Icon Consistency
- **Back arrow (←):** Hiển thị trên Screen 1 + 2, vắng mặt trên Screen 3 (đúng).
- **Home icon:** Chỉ hiển thị rõ trên Screen 3 (left). Screen 1 PRD nêu home icon phải nhưng Figma không thấy rõ — cần verify.
- **Action icons:** Chia sẻ + Lưu ảnh trên Screen 3 nhỏ (28×28px) + label dưới — đủ rõ nghĩa.

### 4. Popup Pattern
- Cả 2 popups (State 3 + 4) dùng cùng template: title "Thông báo" + body + 1 button "Đóng". Không có differentiation giữa validation alert vs business rule warning. OTP bottom sheet dùng pattern khác (slide up + header + close). Pattern rõ ràng cho bottom sheet, nhưng popup cần cải thiện.

### 5. Keyboard & Input Behavior (từ wireframe analysis)
- Không có wireframe nào hiển thị keyboard state (numeric keyboard for amount, date picker modal). Cần bổ sung nếu muốn handoff đầy đủ cho FE.

---

## DDL References sử dụng

| ddl_ref | Rule | UX Law | Áp dụng |
|---------|------|--------|---------|
| `ux-guidelines.csv#4` | Back Button: Preserve navigation history properly | `jakob` | Screen 1, 2: back icon. Screen 3: disabled (correct). |
| `ux-guidelines.csv#10` | Loading States: Show feedback during async operations | `doherty` | UXP-004: beneficiary API lookup thiếu loading. |
| `ux-guidelines.csv#16` | Overflow Hidden: Test content fits within containers | — | UXP-010: "Lưu ý" bị button che. |
| `ux-guidelines.csv#17` | Fixed Positioning: Account for safe areas | — | UXP-010: fixed button overlap content. |
| `ux-guidelines.csv#22` | Touch Target Size: Minimum 44×44px | `fitts` | NFR#3 stated. Visual check: buttons đủ lớn. |
| `ux-guidelines.csv#32` | Loading Buttons: Prevent double submission | `doherty` | UXP-008: "Tiếp tục" và "Xác nhận" thiếu loading state. |
| `ux-guidelines.csv#33` | Error Feedback: Show clear error messages | — | UXP-002, UXP-003: thiếu error states toàn flow. |
| `ux-guidelines.csv#34` | Success Feedback: Confirm successful actions | — | Screen 3: success state hiển thị tốt. |
| `ux-guidelines.csv#35` | Confirmation Dialogs: Confirm destructive/irreversible | — | UXP-001: confirm dialog đặt lịch bị mất. |
| `ux-guidelines.csv#54` | Input Labels: Always show visible label | — | Partial: một số field State 2 dùng generic label. |
| `ux-guidelines.csv#63` | Mobile Keyboards: Show appropriate keyboard | — | NFR stated. Không verify visual. |
| `ux-guidelines.csv#78` | Loading Indicators: Spinner/skeleton > 300ms | `doherty` | UXP-004: API lookup cần indicator. |
| `ux-guidelines.csv#79` | Empty States: Show helpful message + action | — | UXP-013: danh bạ trống. UXP-006: failure state. |
| `ux-guidelines.csv#80` | Error Recovery: Provide clear next steps | — | UXP-003, UXP-005, UXP-006. |
| `ux-guidelines.csv#81` | Progress Indicators: Show step in multi-step process | `goal-gradient` | UXP-007: thiếu step indicator 3 bước. |
| `ux-guidelines.csv#85` | Date Formatting: Use locale-appropriate | — | dd/mm/yyyy nhất quán ✓. |
| `ux-guidelines.csv#87` | Placeholder Content: Use realistic sample data | — | UXP-011, UXP-012: mock data không nhất quán. |
| `web-interface.csv#1` | Icon Button Labels: aria-label required | — | NFR stated. Unverifiable từ wireframe. |
| `web-interface.csv#2` | Form Control Labels: All inputs need labels | — | Partial gap: placeholder-only trên một số fields. |
| `web-interface.csv#7` | Visible Focus States: focus-visible ring | `von-restorff` | Unverifiable từ static wireframe. |
| `web-interface.csv#12` | Never Block Paste: Allow paste on OTP | — | NFR stated ✓. |
| `web-interface.csv#14` | Submit Button Enabled: Show spinner | `doherty` | UXP-008. |
| `web-interface.csv#15` | Inline Errors: Near problem field | — | UXP-002: không có inline error wireframe. |
| `peak-end` | Peak-End Rule | Kahneman | Screen 3 result = "end" of flow. Success design tốt. Failure state thiếu = risk UX tiêu cực. |
| `goal-gradient` | Goal-Gradient Effect | — | UXP-007: progress indicator tạo motivation hoàn thành flow. |
| `nng-error-prevention` | Error Prevention | Nielsen | UXP-001: confirm dialog trước action irreversible (đặt lịch). |
| `nng-error-recovery` | Help Users Recover from Errors | Nielsen | UXP-002, UXP-003, UXP-006: error states cần clear next steps. |
| `nng-user-control` | User Control and Freedom | Nielsen | UXP-005: OTP resend = "emergency exit" khi không nhận OTP. |
| `nng-consistency-standards` | Consistency and Standards | Nielsen | UXP-011, UXP-015: mock data + popup pattern consistency. |
| `nng-recognition-recall` | Recognition Rather Than Recall | Nielsen | UXP-014: "Đối tượng chịu phí" không visible khi scroll. |

---

*Generated by UX Review Pipe | Skill A (Signal Inference + DDL) + Skill B (PRD Context + DDL) + Skill C (Vision Review via Figma MCP) | Domain: banking*
