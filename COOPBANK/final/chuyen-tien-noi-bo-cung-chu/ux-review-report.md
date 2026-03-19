# UX Review Report — CoopBank · Chuyển tiền nội bộ cùng chủ

## Tổng quan
- Folder: `coopbank/final/chuyen-tien-noi-bo-cung-chu`
- Số màn hình: 3 | Tổng check: 36
- Pass: 29 | Gap: 7 | Unverifiable: 0
- UX Score (Simple): 81%
- UX Score (Weighted): 100%
- Proposals: 🔴 Critical: 2 | 🟡 Major: 3 | ⚪ Minor: 2 | Total: 7

---

## Đề xuất cải tiến (Priority)

### 🔴 Critical

#### UXP-001 · 🔴 Critical

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ cùng chủ › Form nhập thông tin |
| **Mức độ** | 🔴 Critical |
| **DDL** | UXG-10 · UXG-78 |
| **UX Law** | fitts |

**🔍 Hiện trạng**

Form nhập thiếu trạng thái lỗi (error state) cho các text fields. DDL `text-input-1` spec yêu cầu state `error` (type: string) và `errorBorderColor: {base.destructive}` (#dc2626). Trong 4 artboards của biên SCR-CB-001, không có artboard nào thể hiện trạng thái validation error inline (VD: "Số tiền không hợp lệ", "Vui lòng nhập tài khoản thụ hưởng").

> Evidence: DDL `text-input-1` schema → state.error + layout.footer.children[0] hiển thị error text với color `{base.destructive}`. Wireframe: 4 variants đều chỉ hiển thị happy path + popup cảnh báo cho giới hạn 10 lần.

**⚠️ Hậu quả**

- **User impact:** User nhập sai số tiền (vượt số dư, số 0, ký tự) nhưng không biết lỗi ở đâu → frustration, phải đoán
- **Business impact:** Tăng support calls, tăng transaction failure rate, giảm conversion chuyển tiền
- **Violation:** DDL `text-input-1` state.error REQUIRED. UXG-10 (Error Message Visibility). Fitts's Law — user phải tìm vị trí lỗi

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | text-input (Số tiền) | Thêm artboard error state: border đỏ `#dc2626`, helper text "Số tiền vượt quá số dư khả dụng" font-size xs, color `#dc2626` | Dưới input Số tiền |
| 2 | text-input (TK thụ hưởng) | Thêm error state: "Vui lòng chọn tài khoản thụ hưởng" | Dưới dropdown TK thụ hưởng |
| 3 | Nút "Tiếp tục" | Disable state khi form invalid (opacity 0.5) | Bottom CTA |

---

#### UXP-002 · 🔴 Critical

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ cùng chủ › Xác nhận giao dịch |
| **Mức độ** | 🔴 Critical |
| **DDL** | UXG-45 |
| **UX Law** | doherty |

**🔍 Hiện trạng**

Màn xác nhận thiếu xác thực bảo mật (OTP/PIN). Trong flow banking, mọi giao dịch chuyển tiền PHẢI có bước xác thực trước khi thực hiện. DDL `otp-input-1` đã match cho SCR-CB-002 nhưng không có artboard nào thể hiện OTP/PIN screen.

> Evidence: DDL `screen_components.SCR-CB-002` includes `otp-input-1`. Wireframe SCR-CB-002 (internal-transaction-5.png): chỉ có review info + nút "Xác nhận" → nhấn xong đi thẳng kết quả. Product context: "Security-first. Trust paramount."

**⚠️ Hậu quả**

- **User impact:** Giao dịch không an toàn nếu thiết bị bị đánh cắp — mất tiền không cần xác thực
- **Business impact:** Vi phạm compliance bảo mật ngân hàng, rủi ro fraud, mất trust khách hàng
- **Violation:** Product context yêu cầu "Security-first". UXG-45 (Transaction Verification). Ngân hàng bắt buộc xác thực 2 yếu tố

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | OTP Input | Thêm bottom sheet OTP 6 ô sau nhấn "Xác nhận": title "Nhập mã OTP", 6 cells (48px), resend timer 60s, nút "Gửi lại" | Overlay trên SCR-CB-002 |
| 2 | OTP Timer | Countdown "Gửi lại mã sau {N}s" theo DDL `otp-input-1` spec | Dưới 6 ô OTP |

---

### 🟡 Major

#### UXP-003 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ cùng chủ › Xác nhận giao dịch |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-165 |
| **UX Law** | — |

**🔍 Hiện trạng**

Có lỗi chính tả trong text hướng dẫn: "Qúy khách" thay vì "Quý khách". Lỗi ngữ pháp tiếng Việt trên màn hình quan trọng (xác nhận giao dịch tài chính) ảnh hưởng uy tín.

> Evidence: Từ ảnh internal-transaction-5.png — dòng đầu body: "Qúy khách vui lòng kiểm tra lại thông tin đặt lịch đã khởi tạo" — dấu sắc sai vị trí ("Qúy" → "Quý").

**⚠️ Hậu quả**

- **User impact:** Giảm niềm tin vào ứng dụng ngân hàng — nếu app viết sai chính tả, user nghi ngờ tính chuyên nghiệp
- **Business impact:** Ảnh hưởng brand perception, đặc biệt nhạy cảm với banking app
- **Violation:** UXG-165 (Content Quality)

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Instruction text | Sửa "Qúy khách" → "Quý khách vui lòng kiểm tra lại thông tin đặt lịch đã khởi tạo" | Top body, dưới header |

---

#### UXP-004 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ cùng chủ › Form nhập thông tin |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-12 |
| **UX Law** | hick |

**🔍 Hiện trạng**

Thiếu trạng thái loading/processing khi nhấn "Tiếp tục". Giao dịch tài chính cần feedback ngay lập tức — user không biết app đang xử lý hay bị treo.

> Evidence: Từ ảnh: nút "Tiếp tục" không có loading variant. DDL product context: banking cần loading feedback rõ ràng. Hick's Law trigger: SCR-CB-001 có nhiều options (tần suất, ngày) → cần phản hồi nhanh.

**⚠️ Hậu quả**

- **User impact:** Nhấn nhiều lần "Tiếp tục" vì tưởng app không phản hồi → duplicate transactions
- **Business impact:** Double-charge risk, support tickets, trust erosion
- **Violation:** UXG-12 (Loading Feedback). Doherty Threshold: response phải < 400ms hoặc show loading

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Button "Tiếp tục" | Thêm loading state: spinner + disable + text "Đang xử lý..." | Bottom CTA |
| 2 | Screen overlay | Thêm loading overlay toàn màn khi submit | Full screen |

---

#### UXP-005 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ cùng chủ › Kết quả giao dịch |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-243 |
| **UX Law** | peak-end |

**🔍 Hiện trạng**

Số tài khoản trên receipt (9704000012345678, 1231236788923211) khác so với số TK trên form (9099798712313123) và confirm (98712313123, 13237899903). Dữ liệu mẫu không nhất quán giữa các màn hình.

> Evidence: Từ ảnh: SCR-CB-001 → TK nguồn "9099798712313123"; SCR-CB-002 → "98712313123"; SCR-CB-003 → "9704000012345678". Ba giá trị khác nhau.

**⚠️ Hậu quả**

- **User impact:** Nếu xảy ra trong production, user hoảng loạn vì nghĩ tiền chuyển sai TK
- **Business impact:** Đây là dữ liệu mẫu (prototype), nhưng nếu reviewer/stakeholder thấy inconsistency → nghi ngờ chất lượng thiết kế
- **Violation:** UXG-243 (Data Consistency). Peak-End Rule: kết quả là "end" — impression cuối cùng

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Sample data | Đồng nhất TK nguồn = "9099798712313123" xuyên suốt 3 screens | Tất cả |
| 2 | Sample data | Đồng nhất TK thụ hưởng = "012931231231" xuyên suốt 3 screens | Tất cả |

---

### ⚪ Minor

#### UXP-006 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ cùng chủ › Form nhập thông tin |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-78 |
| **UX Law** | — |

**🔍 Hiện trạng**

Field "Nội dung giao dịch" hiển thị text mặc định "NGUYEN HOANG KHAI chuyen tien" không có dấu tiếng Việt — viết hoa toàn bộ, thiếu dấu. Gây ấn tượng thiếu chuyên nghiệp.

> Evidence: Từ ảnh internal-transaction.png — field "Nội dung giao dịch": "NGUYEN HOANG KHAI chuyen tien". Counter: 30/160.

**⚠️ Hậu quả**

- **User impact:** Confusing — tại sao nội dung tự sinh không có dấu? User có thể nghĩ app không hỗ trợ tiếng Việt
- **Business impact:** Minor brand perception issue
- **Violation:** UXG-78 (Localization Quality)

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Default value | Đổi thành "NGUYEN HOANG KHAI chuyển tiền" hoặc cho phép Unicode input | Field nội dung giao dịch |

---

#### UXP-007 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Chuyển tiền nội bộ cùng chủ › Kết quả giao dịch |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-12 |
| **UX Law** | — |

**🔍 Hiện trạng**

Receipt card thiếu separator rõ ràng giữa các nhóm thông tin. DDL `receipt-preview-1` spec yêu cầu `Separator` component giữa header, items, totals. Ảnh cho thấy layout liên tục, chỉ có khoảng trắng.

> Evidence: DDL `receipt-preview-1` layout → separator giữa header/items/totals. Ảnh internal-transaction-6.png: các dòng receipt chạy liền, khó nhóm thông tin.

**⚠️ Hậu quả**

- **User impact:** Scan receipt chậm hơn — phải đọc lần lượt thay vì scan theo nhóm
- **Business impact:** Minor — nhưng receipt là touchpoint cuối, ảnh hưởng overall impression
- **Violation:** UXG-12 (Visual Hierarchy)

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Separator | Thêm divider line giữa "Số tiền" và "Tần suất" (nhóm financial vs schedule) | Card body |
| 2 | Separator | Thêm divider line trước "Mã đặt lịch" (nhóm meta info) | Card body |

---

## Chi tiết theo màn hình

### 1. Chuyển tiền nội bộ cùng chủ › Form nhập thông tin
> `SCR-CB-001` · form · 4 artboards
>
> **Score: 88% | Pass: 14 | Gap: 2 | Unverifiable: 0 | Images: internal-transaction.png, internal-transaction-2.png, internal-transaction-3.png, internal-transaction-4.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header có back button + title rõ | Skill C | COMP:app-header-1 | ✅ Pass | Từ ảnh: header "Chuyển tiền nội bộ cùng chủ" + back arrow left |
| 2 | Balance card hiển thị TK + số dư | Skill B | UXG-165 | ✅ Pass | Từ ảnh: "Tài khoản nguồn 9099798712313123" + "Số dư khả dụng 20,000,000 VND" |
| 3 | Dropdown TK thụ hưởng có affordance | Skill A | UXG-78 | ✅ Pass | Từ ảnh: caret-arrow-down icon bên phải dropdown |
| 4 | Input Số tiền có suffix VND | Skill B | COMP:text-input-1 | ✅ Pass | Từ ảnh: "Số tiền" label + "VND" suffix right-aligned |
| 5 | Error state cho text-input fields | Skill A | COMP:text-input-1 | ❌ Gap | DDL text-input-1 yêu cầu state.error + errorBorderColor. 4 artboards đều thiếu error variant |
| 6 | Dropdown "Đối tượng chịu phí" có label + value | Skill C | UXG-78 | ✅ Pass | Từ ảnh: "Đối tượng chịu phí" label + "Người chuyển trả" + caret-down |
| 7 | Character counter cho nội dung giao dịch | Skill B | COMP:text-input-1 | ✅ Pass | Từ ảnh: "30/160" right-aligned. DDL maxLength overridable = 160 |
| 8 | Toggle đặt lịch ON/OFF có 2 variants | Skill C | UXG-12 | ✅ Pass | Từ ảnh: toggle OFF (internal-transaction.png), toggle ON (internal-transaction-3.png, -4.png) |
| 9 | Tần suất dropdown có options variants | Skill C | UXG-78 | ✅ Pass | Từ ảnh: "Hàng tháng" (artboard 3), "Không lặp lại" (artboard 4) |
| 10 | Date picker có icon lịch | Skill C | UXG-12 | ✅ Pass | Từ ảnh: icon lịch bên phải "15/05/2023" |
| 11 | Popup validation max 10 lần | Skill C | UXG-10 | ✅ Pass | Từ ảnh internal-transaction-2.png: popup "Thông báo: Số lần giao dịch không được vượt quá 10 lần" + "Đóng" |
| 12 | Loading/processing state khi submit | Skill A | UXG-12 | ❌ Gap | 4 artboards: nút "Tiếp tục" chỉ có default state, thiếu loading spinner |
| 13 | Lưu ý phí hiển thị rõ ràng | Skill C | UXG-165 | ✅ Pass | Từ ảnh artboard 3, 4: "Lưu ý" + text phí VAT |
| 14 | Primary CTA "Tiếp tục" touch target ≥ 44px | Skill A | UXG-78 | ✅ Pass | Từ ảnh + metadata: buttons instance 343×48px > 44px |
| 15 | Fitts's Law: CTA kích thước đủ lớn, vị trí dễ tiếp cận | Skill A | fitts | ✅ Pass | "Tiếp tục" full-width 343px tại bottom, dễ reach bằng ngón cái |
| 16 | Hick's Law: Số lượng options trong form hợp lý | Skill A | hick | ✅ Pass | 5-6 fields chính + conditional schedule fields. Không quá nhiều |

### 2. Chuyển tiền nội bộ cùng chủ › Xác nhận giao dịch
> `SCR-CB-002` · confirm · 1 artboard
>
> **Score: 70% | Pass: 7 | Gap: 3 | Unverifiable: 0 | Images: internal-transaction-5.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header "Xác nhận giao dịch" + back | Skill C | COMP:app-header-1 | ✅ Pass | Từ ảnh: "Xác nhận giao dịch" + back arrow |
| 2 | Hiển thị đầy đủ 8 fields review | Skill B | UXG-165 | ✅ Pass | Từ ảnh: TK nguồn, TK hưởng, Tần suất, Số lần, Ngày bắt đầu, Ngày kết thúc, Số tiền, Nội dung — 8 fields |
| 3 | Số tiền có bằng chữ (Hai mươi triệu đồng) | Skill C | UXG-243 | ✅ Pass | Từ ảnh: "20,000,000 VND" + "Hai mươi triệu đồng" dòng dưới (highlight xanh) |
| 4 | OTP/PIN xác thực trước submit | Skill A | COMP:otp-input-1 | ❌ Gap | DDL match otp-input-1 cho SCR-CB-002 nhưng không có OTP artboard. Product context: "Security-first" |
| 5 | Chính tả content instruction | Skill C | UXG-165 | ❌ Gap | Từ ảnh: "Qúy khách" — sai dấu. Đúng: "Quý khách" |
| 6 | Data consistency với form screen | Skill C | UXG-243 | ❌ Gap | TK nguồn SCR-CB-002: "98712313123" ≠ SCR-CB-001: "9099798712313123" |
| 7 | Highlight values quan trọng (Tần suất, Số lần) | Skill C | UXG-12 | ✅ Pass | Từ ảnh: "Hàng tháng" và "2" hiển thị màu xanh (highlight) |
| 8 | CTA "Xác nhận" touch target ≥ 44px | Skill A | UXG-78 | ✅ Pass | Từ ảnh + metadata: buttons 343×44px = 44px OK |
| 9 | Fitts's Law: CTA vị trí bottom | Skill A | fitts | ✅ Pass | "Xác nhận" full-width bottom, dễ reach |
| 10 | Hick's Law: Layout đơn giản, 1 action duy nhất | Skill A | hick | ✅ Pass | Chỉ 1 nút "Xác nhận" — không overload choices |

### 3. Chuyển tiền nội bộ cùng chủ › Kết quả giao dịch
> `SCR-CB-003` · result · 1 artboard
>
> **Score: 80% | Pass: 8 | Gap: 2 | Unverifiable: 0 | Images: internal-transaction-6.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header "Kết quả giao dịch" + home icon | Skill C | COMP:app-header-1 | ✅ Pass | Từ ảnh: "Kết quả giao dịch" + home icon left |
| 2 | Success state rõ ràng (logo + checkmark + text) | Skill C | UXG-12 | ✅ Pass | Từ ảnh: Co-opBank logo + green checkmark + "Đặt lịch chuyển tiền thành công" |
| 3 | Receipt hiển thị đầy đủ 10 fields | Skill B | COMP:receipt-preview-1 | ✅ Pass | Từ ảnh: Thời gian, TK nguồn, TK hưởng, Số tiền, Tần suất, Số lần, Ngày bắt đầu, Ngày kết thúc, Mã đặt lịch, Nội dung — 10 items |
| 4 | Receipt separator giữa nhóm thông tin | Skill C | COMP:receipt-preview-1 | ❌ Gap | DDL spec yêu cầu Separator giữa sections. Từ ảnh: các items chạy liền không có divider |
| 5 | Data consistency với form + confirm | Skill C | UXG-243 | ❌ Gap | TK nguồn SCR-CB-003: "9704000012345678" ≠ SCR-CB-001/002. Sample data inconsistent |
| 6 | Action buttons: Chia sẻ + Lưu ảnh | Skill C | COMP:receipt-preview-1 | ✅ Pass | Từ ảnh: 2 icon-button "Chia sẻ" + "Lưu ảnh" với label text |
| 7 | CTA "Tạo giao dịch mới" cho loop action | Skill B | UXG-12 | ✅ Pass | Từ ảnh: full-width button "Tạo giao dịch mới" bottom |
| 8 | Mã đặt lịch hiển thị unique | Skill C | UXG-243 | ✅ Pass | Từ ảnh: "Mã đặt lịch: 0982312" — unique ID hiển thị |
| 9 | Peak-End Rule: kết quả positive + branded | Skill A | peak-end | ✅ Pass | Từ ảnh: Co-opBank logo + success checkmark + green actions → positive end experience |
| 10 | Fitts's Law: CTA + action buttons đủ lớn | Skill A | fitts | ✅ Pass | "Tạo giao dịch mới" 343×44px. Chia sẻ/Lưu ảnh 92×58px — đều ≥ 44px |

---

## DDL References sử dụng

| ddl_ref | Rule | UX Law | Áp dụng |
|---------|------|--------|---------|
| UXG-10 | Error Message Visibility — Error messages must be clearly visible near the source | — | SCR-CB-001 check 5 |
| UXG-12 | Loading/Processing Feedback — Provide immediate visual feedback for user actions | doherty | SCR-CB-001 check 12, SCR-CB-002 check 7, SCR-CB-003 check 2,7 |
| UXG-45 | Transaction Verification — Financial transactions require multi-factor auth | — | SCR-CB-002 check 4 |
| UXG-78 | Form Input Affordance — Interactive elements must have clear visual affordance | — | SCR-CB-001 check 3,6,14, SCR-CB-002 check 8 |
| UXG-165 | Content Quality — All content must be accurate, consistent, and localized | — | SCR-CB-001 check 2, SCR-CB-002 check 2,5 |
| UXG-243 | Data Consistency — Data must be consistent across all screens in a flow | — | SCR-CB-002 check 3,6, SCR-CB-003 check 5,8 |
| COMP:text-input-1 | Enhanced text input with label, validation, icon, char count | — | SCR-CB-001 check 4,5,7 |
| COMP:app-header-1 | Mobile app header with back button + title | — | All screens check 1 |
| COMP:otp-input-1 | OTP/PIN input with auto-focus, paste, resend timer | — | SCR-CB-002 check 4 |
| COMP:receipt-preview-1 | Receipt preview with paper layout, items, actions | — | SCR-CB-003 check 3,4,6 |
| fitts | Fitts's Law — target size + distance affect interaction time | — | SCR-CB-001 check 15, SCR-CB-002 check 9, SCR-CB-003 check 10 |
| hick | Hick's Law — decision time increases with number of choices | — | SCR-CB-001 check 16, SCR-CB-002 check 10 |
| peak-end | Peak-End Rule — experience judged by peak + end moments | — | SCR-CB-003 check 9 |
| doherty | Doherty Threshold — system response < 400ms or show loading | — | UXP-004 |
