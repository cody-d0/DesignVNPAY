# Nhập thông tin chuyển tiền nội bộ khác chủ

> **Figma:** [134:19728](https://www.figma.com/design/kPft93N2A3gYOC3YwuXpQR/Co-op-Bank-KHCN?node-id=134-19728&m=dev), [134:19817](https://www.figma.com/design/kPft93N2A3gYOC3YwuXpQR/Co-op-Bank-KHCN?node-id=134-19817&m=dev), [134:19855](https://www.figma.com/design/kPft93N2A3gYOC3YwuXpQR/Co-op-Bank-KHCN?node-id=134-19855&m=dev), [134:19895](https://www.figma.com/design/kPft93N2A3gYOC3YwuXpQR/Co-op-Bank-KHCN?node-id=134-19895&m=dev)

---

## 1. Chân dung khách hàng

| Thuộc tính | Mô tả |
|---|---|
| Đối tượng | Khách hàng cá nhân (KHCN) đã đăng ký Mobile Banking Co-op Bank |
| Nhu cầu | Chuyển tiền đến tài khoản khác chủ trong hệ thống Co-op Bank, hỗ trợ chuyển ngay hoặc đặt lịch định kỳ |
| Bối cảnh sử dụng | Trên thiết bị di động (iOS/Android), mọi lúc mọi nơi, khi cần thanh toán hoặc chuyển tiền nội bộ |
| Kỳ vọng | Nhập thông tin nhanh gọn, hỗ trợ danh bạ thụ hưởng, đặt lịch linh hoạt, giao diện dễ hiểu |

> **`🤖 by AI`** | Nguồn: UX best practice — banking app | Độ tin cậy: Medium
>
> **Persona mở rộng:**
> - Nhóm tuổi 25-55, quen dùng smartphone, ưu tiên tốc độ và an toàn
> - Pain point: nhập lại thông tin người nhận mỗi lần chuyển, quên lịch thanh toán định kỳ
> - Motivation: tiết kiệm thời gian, tự động hóa chuyển tiền định kỳ (tiền nhà, lương nhân viên)

---

## 2. User Story

| Epic chung | Mã US | Tiêu đề | Mô tả chi tiết | Business Rule | Acceptance Criteria |
|---|---|---|---|---|---|
| Chuyển tiền nội bộ | US-001 | Chọn tài khoản nguồn | Là KHCN, tôi muốn xem và chọn tài khoản nguồn để biết số dư trước khi chuyển. | Chỉ hiển thị tài khoản thanh toán active. Số dư khả dụng realtime. | - Hiển thị số tài khoản + số dư khả dụng (VND).<br>- Nhấn mũi tên dropdown → danh sách tài khoản.<br>- Tài khoản mặc định = tài khoản chính. |
| Chuyển tiền nội bộ | US-002 | Nhập thông tin người hưởng | Là KHCN, tôi muốn nhập số tài khoản/số thẻ/SĐT người hưởng để xác định người nhận. | Validate: chỉ nhận số tài khoản Co-op Bank hợp lệ. Auto-lookup tên người hưởng sau khi nhập đủ. | - Hiển thị "Thông tin người hưởng (1/10)" = danh bạ thụ hưởng đã lưu.<br>- Nhấn "Thêm người hưởng" → nhập mới.<br>- Nhập STK → API trả về tên (NGUYEN HOANG HIEU).<br>- Toggle "Lưu danh bạ thụ hưởng" → lưu vào danh bạ. |
| Chuyển tiền nội bộ | US-003 | Nhập thông tin chuyển tiền | Là KHCN, tôi muốn nhập số tiền, chọn đối tượng chịu phí, nhập nội dung giao dịch. | Số tiền > 0 và ≤ số dư khả dụng. Nội dung giao dịch max 160 ký tự, mặc định auto-fill. | - Field "Số tiền" + đơn vị VND.<br>- Dropdown "Đối tượng chịu phí" (mặc định: Người chuyển trả).<br>- Field "Nội dung giao dịch" hiển thị 30/160 ký tự.<br>- Auto-fill nội dung: "{TÊN NGƯỜI GỬI} chuyen tien". |
| Chuyển tiền nội bộ | US-004 | Đặt lịch chuyển tiền | Là KHCN, tôi muốn đặt lịch chuyển tiền định kỳ để tự động hóa các khoản thanh toán lặp lại. | Khi toggle ON: bắt buộc chọn tần suất, số lần, ngày bắt đầu. Ngày kết thúc = tự tính hoặc nhập. Phí + VAT theo quy định từng thời kỳ. | - Toggle "Đặt lịch chuyển tiền" (mặc định OFF).<br>- ON → hiện: Tần suất (Hàng tháng), Số lần giao dịch, Ngày bắt đầu (date picker).<br>- Ngày kết thúc tự tính (đỏ: "Ngày kết thúc: 15/06/2023").<br>- Lưu ý phí/VAT hiển thị cuối form. |
| Chuyển tiền nội bộ | US-005 | Xác nhận trước khi gửi | Là KHCN, tôi muốn kiểm tra lại thông tin trước khi gửi để tránh sai sót. | Hiển thị popup xác nhận khi có scheduled transfer. Nút "Đồng ý" / "Hủy". | - Nhấn "Tiếp tục" → popup xác nhận (blur overlay).<br>- Popup hiển thị thông báo "Bạn có chắc chắn..."<br>- "Đồng ý" → chuyển màn xác nhận giao dịch.<br>- "Hủy" → quay lại form. |

---

## 3. Wireframe / Mô tả màn hình

### State 1: Form nhập cơ bản (Toggle đặt lịch OFF)

![Nhập thông tin chuyển tiền - cơ bản](ui/internal-transaction.png)

| # | Thành phần | Loại | Mô tả | Figma Node |
|---|---|---|---|---|
| 1 | Header | `header` | "Chuyển tiền nội bộ khác chủ", icon back (←) trái, icon home (🏠) phải. Gradient #285598→#002a69. Height 86px (gồm status bar 44px). | 134:19729 |
| 2 | Balance Card | `card-item` | Card trắng, border-radius 12px. Logo Co-op Bank trái. "Tài khoản nguồn" (label muted 13px) + số TK "9099798712313123" (bold 15px). "Số dư khả dụng" (muted) + "20,000,000 VND" (bold 17px, primary #002a69). Mũi tên dropdown phải (↓). | 134:19730 |
| 3 | Section — Thông tin người hưởng | `section` | Tiêu đề: icon user (👤) + "Thông tin người hưởng (1/10)". Divider dưới. | 134:19742 |
| 4 | Menu Item — Thêm người hưởng | `list-item` | Icon (+) + "Thêm người hưởng". Divider dưới. Nhấn → thêm người hưởng mới. | 134:19744 |
| 5 | Input — Số tài khoản người hưởng | `input-field` | Placeholder "Số tài khoản/Số thẻ/Số điện thoại" (muted #acaeba). Icon danh bạ phải. Border-bottom. | 134:19745 |
| 6 | Section — Thông tin chuyển tiền | `section` | Tiêu đề: icon transaction (💳) + "Thông tin chuyển tiền". Divider dưới. | 134:19746 |
| 7 | Menu Item — Số tiền | `list-item` | Label "Số tiền" (muted) + value "VND" (bold) phải. | 134:19748 |
| 8 | Dropdown — Đối tượng chịu phí | `select-field` | Label "Đối tượng chịu phí" (muted 13px). Value "Người chuyển trả" (bold 15px). Icon dropdown (↓) phải. | 134:19749 |
| 9 | Input — Nội dung giao dịch | `input-field` | Label "Nội dung giao dịch" + counter "30/160" phải. Value "NGUYEN HOANG KHAI chuyen tien" (bold). | 134:19750 |
| 10 | Toggle — Đặt lịch chuyển tiền | `switch` | Icon calendar (📅) + "Đặt lịch chuyển tiền". Toggle OFF (mặc định). | 134:19751 |
| 11 | Button — Tiếp tục | `button-primary` | "Tiếp tục", full-width 343px, height 48px, gradient primary, border-radius 8px. | 134:19754 |

### State 2: Form nhập với đặt lịch (Toggle đặt lịch ON)

![Nhập thông tin chuyển tiền - đặt lịch](ui/internal-transaction-2.png)

| # | Thành phần | Loại | Mô tả | Figma Node |
|---|---|---|---|---|
| 1–6 | (Giống State 1) | — | Header, Balance Card, Section người hưởng. Khác biệt: "Thông tin người hưởng" (không có "(1/10)"). Input hiển thị tên người hưởng "NGUYEN HOANG HIEU" (bold, #050421). | — |
| 7 | Toggle — Lưu danh bạ thụ hưởng | `switch` | "Lưu danh bạ thụ hưởng" + Toggle (mặc định ON hoặc OFF tùy user). | 134:19835 |
| 8 | Section — Thông tin chuyển tiền | `section` | Giống State 1 nhưng label field dùng generic "Label" (Figma placeholder). | 134:19838 |
| 9 | Toggle — Đặt lịch chuyển tiền | `switch` | Toggle **ON** (active, màu xanh). | 134:19843 |
| 10 | Dropdown — Tần suất | `select-field` | Label chung. Value placeholder. Icon dropdown phải. Tùy chọn: Hàng tháng, Hàng tuần, etc. | 134:19847 |
| 11 | Input — Số lần giao dịch | `input-field` | Label chung. Value số lần (vd: 2). Icon dropdown phải. | 134:19848 |
| 12 | Date Picker — Ngày bắt đầu | `date-picker` | Label chung. Value ngày (vd: 15/05/2023). Icon calendar phải. | 134:19849 |
| 13 | Label — Ngày kết thúc | `helper-text` | "Ngày kết thúc: 15/06/2023" (bold 13px, đỏ #e50019). Tự động tính từ tần suất × số lần. | 134:19850 |
| 14 | Annotation — Lưu ý | `infobox` | Tiêu đề "Lưu ý" (bold 15px, primary #002a69). Nội dung: "Phí và VAT của từng giao dịch chuyển tiền theo lịch áp dụng theo quy định của Co-opBank trong từng thời kỳ." (regular 13px, muted). | 134:19851 |
| 15 | Button — Tiếp tục | `button-primary` | "Tiếp tục", height 44px, gradient primary. | 134:19854 |

### State 3: Popup xác nhận — Thông báo

![Popup thông báo](ui/internal-transaction-3.png)

| # | Thành phần | Loại | Mô tả | Figma Node |
|---|---|---|---|---|
| 1 | Blur overlay | `design-element` | Toàn màn hình, rgba(5,4,33,0.7). | 134:19893 |
| 2 | Popup — Thông báo | `dialog` | Card trắng, border-radius, centered. Tiêu đề "Thông báo". Nội dung xác nhận. Nút "Đồng ý". Width 343px, height ~168px. | 134:19894 |

### State 4: Popup xác nhận — Giới hạn giao dịch

![Popup giới hạn](ui/internal-transaction-4.png)

| # | Thành phần | Loại | Mô tả | Figma Node |
|---|---|---|---|---|
| 1 | Blur overlay | `design-element` | Toàn màn hình, rgba(5,4,33,0.7). | 134:19933 |
| 2 | Popup — Thông báo | `dialog` | Card trắng, centered. Nội dung cảnh báo (vd: giới hạn số tiền/số lần). Nút "Đồng ý". Width 343px, height ~148px. | 134:19934 |

---

## 4. Database / Data Fields

| # | Field | Type | Bắt buộc | Nguồn | Mô tả |
|---|---|---|---|---|---|
| 1 | source_account | string | Có | User chọn | Số tài khoản nguồn (tài khoản thanh toán) |
| 2 | source_balance | decimal | — | API | Số dư khả dụng (VND) |
| 3 | beneficiary_account | string | Có | User nhập | Số tài khoản / số thẻ / SĐT người hưởng |
| 4 | beneficiary_name | string | — | API lookup | Tên người thụ hưởng (auto-fill từ API) |
| 5 | is_saved_beneficiary | boolean | Không | User toggle | Lưu vào danh bạ thụ hưởng hay không |
| 6 | amount | decimal | Có | User nhập | Số tiền chuyển (VND) |
| 7 | amount_text | string | — | Computed | Số tiền bằng chữ ("Hai mươi triệu đồng") |
| 8 | fee_bearer | enum | Có | User chọn | Đối tượng chịu phí: "Người chuyển trả" / "Người nhận trả" |
| 9 | transaction_content | string(160) | Có | User nhập / auto | Nội dung giao dịch, max 160 ký tự |
| 10 | is_scheduled | boolean | Có | User toggle | Đặt lịch chuyển tiền ON/OFF |
| 11 | frequency | enum | Có (khi scheduled) | User chọn | Tần suất: "Hàng tháng", "Hàng tuần" |
| 12 | transaction_count | integer | Có (khi scheduled) | User nhập | Số lần giao dịch |
| 13 | start_date | date | Có (khi scheduled) | User chọn | Ngày bắt đầu (date picker) |
| 14 | end_date | date | — | Computed | Ngày kết thúc (tự tính từ frequency × count) |

---

## 5. NFR (Yêu cầu phi chức năng)

| # | Hạng mục | Yêu cầu |
|---|---|---|
| 1 | Responsive | Mobile-first 375×812pt (iPhone X). Hỗ trợ 320-428px width. |
| 2 | Performance | API lookup tên người hưởng < 2s. Load danh bạ thụ hưởng < 1s. |
| 3 | Accessibility | Mọi input có label (`aria-label`). Toggle có `role="switch"` + `aria-checked`. Touch target ≥ 44×44px cho tất cả interactive element. |
| 4 | Validation | Số tiền: > 0, ≤ số dư, numeric only. STK: chỉ số, validate Co-op Bank format. Nội dung: max 160 chars. Ngày bắt đầu ≥ today. |
| 5 | Security | Không hiển thị đầy đủ STK nguồn trên màn xác nhận (mask). Session timeout theo policy. |
| 6 | UX | Auto-focus vào field đầu tiên. Keyboard numeric cho số tiền/STK. Scroll smooth khi toggle đặt lịch expand. Date picker native hoặc custom. |
| 7 | Error Handling | Inline error (đỏ) dưới field lỗi. Toast cho lỗi network. Popup cho lỗi business (vd: vượt hạn mức). |

---

*Figma nodes: 134:19728, 134:19817, 134:19855, 134:19895 | Section: Chuyển tiền nội bộ khác chủ*
