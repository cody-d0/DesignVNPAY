# UX Review Report — Co-opBank KHCN · Thanh toán

## Tổng quan
- Folder: coopbank/final/thanh toán
- Số màn hình: 9 | Tổng check: 0
- Pass: 0 | Gap: 0 | Unverifiable: 0
- UX Score (Simple): 0% (0/0)
- UX Score (Weighted): 0%
- Proposals: 🔴 Critical: 3 | 🟡 Major: 5 | ⚪ Minor: 4 | Total: 12

## Đề xuất cải tiến (Priority)

### 🔴 Critical

#### UXP-001 · 🔴 Critical

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Thanh toán vé xem phim › Xác nhận giao dịch, Thanh toán vé tàu › Xác nhận giao dịch |
| **Mức độ** | 🔴 Critical |
| **DDL** | UXG-52 · COMP:otp-input-1 |
| **UX Law** | cognitive-load |

**🔍 Hiện trạng**

Từ ảnh 1001thanh-toan-ve-xem-phim.png và thanh-toan-ve-tau-3.png: Màn hình xác nhận giao dịch lặp lại gần như nguyên xi thông tin từ form trước đó (tài khoản nguồn, dịch vụ, mã thanh toán, số tiền). Từ deep-research: "Cognitive Overload" — 3 lần hiển thị cùng data (SDK → Form → Confirm) khiến user scan thay vì đọc kỹ, tăng nguy cơ bỏ qua lỗi. Banner "kiểm tra lại thông tin đặt lịch đã khởi tạo" dùng từ "đặt lịch" không khớp context "thanh toán".

> Evidence: Từ ảnh 1001thanh-toan-ve-xem-phim.png — 7 info rows identical với form. Banner text mismatch: "đặt lịch" ≠ "thanh toán vé xem phim".

**⚠️ Hậu quả**

- **User impact:** User "scan-and-skip" thay vì đọc kỹ → bỏ qua lỗi dữ liệu. Banner text sai tạo confusion.
- **Business impact:** Tăng tỷ lệ dispute giao dịch khi user claim "không thấy lỗi trên confirm".
- **Violation:** UXG-52 (Information Hierarchy), Cognitive Load theory — redundant data display.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Confirm screen | Áp dụng Smart Summary: chỉ hiện key fields (số tiền, TK nguồn, dịch vụ) + expandable "Xem chi tiết" | Content area |
| 2 | Banner | Sửa "đặt lịch" → context cụ thể: "thanh toán vé xem phim" | Banner text |
| 3 | Highlight | Tô sáng các giá trị thay đổi so với form (nếu có) | Changed values |

---

#### UXP-002 · 🔴 Critical

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Thanh toán Vietlott › Xác nhận giao dịch, Thanh toán vé xem phim › Xác nhận giao dịch, Thanh toán vé tàu › Xác nhận giao dịch |
| **Mức độ** | 🔴 Critical |
| **DDL** | COMP:otp-input-1 |
| **UX Law** | fitts |

**🔍 Hiện trạng**

Từ ảnh thanh-toan-vietlot.png (artboard 3/4): OTP bottom-sheet có 6 digit cells trống, nút close (×), và CTA "Xác nhận". Tuy nhiên KHÔNG có: (1) countdown timer đếm ngược thời gian OTP hết hạn, (2) nút "Gửi lại" khi hết thời gian chờ. DDL `otp-input-1` spec yêu cầu `canResend` state + `timeLeft` countdown + "Gửi lại" button. Từ deep-research: OTP timeout mà không có resend → user phải thoát và bắt đầu lại toàn bộ flow.

> Evidence: Từ ảnh thanh-toan-vietlot.png — OTP overlay: 6 static cells, text "...098****123", NO timer visible, NO resend button. DDL `otp-input-1.state.canResend` = missing.

**⚠️ Hậu quả**

- **User impact:** OTP hết hạn → không biết phải làm gì → thoát flow, mất giao dịch.
- **Business impact:** Drop-off rate tăng ở bước xác thực — cao nhất trong funnel.
- **Violation:** COMP:otp-input-1 requires `canResend`, `timeLeft`, resend button.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Timer | Hiển thị countdown "Còn 02:00" bên dưới digit cells | Dưới OTP cells |
| 2 | Resend | Nút "Gửi lại mã OTP" (disabled khi timer > 0, enabled khi = 0) | Dưới timer |
| 3 | Auto-submit | OTP auto-submit khi đủ 6 ký tự (giảm 1 tap) | OTP handler |

---

#### UXP-003 · 🔴 Critical

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Thanh toán vé tàu › Form nhập thông tin |
| **Mức độ** | 🔴 Critical |
| **DDL** | UXG-52 |
| **UX Law** | cognitive-load |

**🔍 Hiện trạng**

Từ ảnh thanh-toan-ve-tau-2.png: Variant khứ hồi có tổng artboard height ~1407px, chứa ~20 info rows across 4 sections (Thông tin thanh toán + Chiều đi + Chiều về + Khách hàng). User phải cuộn >3 viewport để thấy CTA "Tiếp tục". Từ deep-research: cognitive fatigue khi cuộn form dài trên 2.5 viewport, tỷ lệ abandon tăng ~25%.

> Evidence: Từ ảnh thanh-toan-ve-tau-2.png — artboard 1407px, viewport 812px, cần ~1.7x cuộn. 20 info rows visible.

**⚠️ Hậu quả**

- **User impact:** Cuộn mệt mỏi → không review toàn bộ → miss lỗi dữ liệu, đặc biệt thông tin chiều về.
- **Business impact:** User abandon ở form quá dài → giảm conversion.
- **Violation:** UXG-52 (Long List Orientation) — form > 1200px cần collapsible sections.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Sections | Collapsible sections — mặc định expanded nhưng tap header thu gọn | All sections |
| 2 | Summary strip | Thêm sticky summary bar (tổng tiền + số vé) ở top khi cuộn | Sticky top |
| 3 | CTA | CTA "Tiếp tục" sticky bottom visible luôn | Bottom |

---

### 🟡 Major

#### UXP-004 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Thanh toán Vietlott › Xác nhận giao dịch, Thanh toán vé xem phim › Xác nhận giao dịch, Thanh toán vé tàu › Xác nhận giao dịch |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-78 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh 1001thanh-toan-ve-xem-phim.png: Banner cảnh báo "Quý khách vui lòng kiểm tra lại thông tin đặt lịch đã khởi tạo" — từ "đặt lịch" sử dụng cho cả Vietlott, vé xem phim, vé tàu. Không phải "đặt lịch" trong bất kỳ context nào. Copy banner generic, không contextualize theo dịch vụ.

> Evidence: Từ ảnh — cùng 1 banner text copy-paste 3 services: "đặt lịch" ≠ context thanh toán Vietlott/vé phim/vé tàu.

**⚠️ Hậu quả**

- **User impact:** Confusion — "đặt lịch gì?" → giảm attention vào banner.
- **Business impact:** Banner mất hiệu quả cảnh báo → user scan qua.
- **Violation:** UXG-78 (Content Quality) — copy phải khớp context.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Banner text | Context-specific: "kiểm tra lại thông tin thanh toán vé xem phim" | Banner |

---

#### UXP-005 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Thanh toán vé xem phim › Xác nhận giao dịch |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-165 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh 1001thanh-toan-ve-xem-phim.png: Dropdown "Chọn phương thức xác thực" hiện "SMS OTP" là option duy nhất. Dropdown với 1 option = UI redundant. User phải tap dropdown → thấy 1 option → chọn → đóng. Thêm 2 taps không cần thiết.

> Evidence: Từ ảnh — dropdown "SMS OTP" là single-option across all 3 flows. Trên cả Vietlott, vé phim, vé tàu.

**⚠️ Hậu quả**

- **User impact:** Tăng friction không cần thiết (2 taps thừa per transaction).
- **Business impact:** Nếu chỉ 1 method → auto-select + hiện text "Xác thực qua SMS OTP".
- **Violation:** Hick's Law — 1 option ≠ choice → không cần dropdown.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Dropdown → static | Nếu chỉ 1 option → hiện text tĩnh thay vì dropdown | Auth section |
| 2 | Future-proof | Nếu lộ trình có 2+ methods → giữ dropdown | Conditional |

---

#### UXP-006 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Thanh toán vé xem phim › Kết quả giao dịch, Thanh toán vé tàu › Kết quả giao dịch |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-78 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh 1003thanh-toan-ve-xem-phim.png: Lưu ý section bao gồm "liên hệ tổng đài XXXXX" — số tổng đài là placeholder raw, không phải số thật. Hiện diện trên cả kết quả vé phim và vé tàu. User đọc thấy "XXXXX" sẽ mất trust.

> Evidence: Từ ảnh — "tổng đài XXXXX" visible rõ ở dưới result card. OCR confirms "XXXXX".

**⚠️ Hậu quả**

- **User impact:** Không thể liên hệ hỗ trợ khi cần thiết → frustration critical nếu không nhận mã đặt chỗ.
- **Business impact:** Mất trust, tăng in-app complaints.
- **Violation:** UXG-78 (Content Quality) — placeholder text trong production design.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Hotline | Thay XXXXX bằng số tổng đài thật (1900xxxx) | Notice text |
| 2 | Action | Số tổng đài clickable (tel: link) | Notice |

---

#### UXP-007 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Thanh toán vé xem phim › Form nhập thông tin |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-78 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh 1000thanh-toan-ve-xem-phim.png: Thông tin khách hàng chứa "[Customer name]", "[Phone number]", "email@examplemail.com" — đây là placeholder text raw từ SDK. User thấy brackets + email giả → confusion. Design cần dùng data thật hoặc ghi rõ "Sẽ lấy từ thông tin đăng ký".

> Evidence: Từ ảnh — OCR: "[Customer name]", "[Phone number]" với square brackets. Raw placeholder visible.

**⚠️ Hậu quả**

- **User impact:** Confusion — "Tên tôi là [Customer name]?" → doubt accuracy.
- **Business impact:** Design unrealistic → dev hiểu nhầm spec → ship placeholder.
- **Violation:** UXG-78 (Content Quality) — design phải dùng realistic sample data.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Customer data | Dùng realistic sample: "Nguyễn Văn A", "098****123" | Form |

---

#### UXP-008 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Thanh toán vé tàu › Form nhập thông tin |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-243 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh thanh-toan-ve-tau-1.png: "Tổng tiền: 20,000 VND" và "Số tiền giảm: 100,000 VND", "Tổng số tiền thanh toán: 80,000 VND". Logic: 20K - 100K = -80K (impossible). Thực tế nên là tổng 120K - giảm 40K = 80K hoặc tương tự. Data sai logic. Từ ảnh thanh-toan-ve-tau-2.png (khứ hồi): "Thông tin chiều về" có "Ga khởi hành: Sài Gòn", "Ga đến: Sài Gòn" — cùng ga = lỗi copy data.

> Evidence: Từ ảnh — math error: 20K < 100K discount. Chiều về: ga đi = ga đến = Sài Gòn.

**⚠️ Hậu quả**

- **User impact:** Trust erosion — bank không tính đúng? → lo sợ bị trừ nhầm tiền.
- **Business impact:** Data error trong design → dev ship lỗi logic.
- **Violation:** UXG-243 (Error Prevention) — data validation at design level.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Sample data | Fix: Tổng tiền > Giảm. VD: Tổng 120K, Giảm 40K, TT 80K | Thông tin TT |
| 2 | Return trip | Fix: Ga đến chiều về = Hà Nội (inverse chiều đi) | Chiều về section |

---

### ⚪ Minor

#### UXP-009 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Thanh toán vé xem phim › Kết quả, Thanh toán vé tàu › Kết quả |
| **Mức độ** | ⚪ Minor |
| **DDL** | COMP:receipt-preview-1 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh: Nút "Lưu ảnh" lưu screenshot — không phải PDF biên nhận. DDL `receipt-preview-1` spec có print/share actions nhưng thiếu PDF generation option cho archive. Banking app cần biên nhận PDF cho mục đích chứng từ.

> Evidence: Từ ảnh 1003thanh-toan-ve-xem-phim.png — "Lưu ảnh" = screenshot only. Không có "Tải biên nhận PDF".

**⚠️ Hậu quả**

- **User impact:** Screenshot quality thấp hơn PDF cho chứng từ ngân hàng.
- **Business impact:** Minor — users vẫn có screenshot.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Actions | Thêm "Tải biên nhận PDF" cạnh "Lưu ảnh" | Action row |

---

#### UXP-010 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Thanh toán Vietlott › Xác nhận giao dịch, Thanh toán vé xem phim › Xác nhận giao dịch, Thanh toán vé tàu › Xác nhận giao dịch |
| **Mức độ** | ⚪ Minor |
| **DDL** | COMP:app-header-1 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh: Confirm screens thiếu home icon ở header — chỉ có back arrow. Form screens (SCR-TT-001/004/007) có cả back + home. Inconsistent navigation affordances giữa form vs confirm.

> Evidence: Từ ảnh — form headers: back + home (2 icons). Confirm headers: back only (1 icon).

**⚠️ Hậu quả**

- **User impact:** Muốn về home từ confirm → phải back → exit SDK. Thêm bước.
- **Violation:** COMP:app-header-1 consistency — header actions nên nhất quán.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Header | Thêm home icon cho confirm screens | Header right |

---

#### UXP-011 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Thanh toán Vietlott › Kết quả, Thanh toán vé xem phim › Kết quả, Thanh toán vé tàu › Kết quả |
| **Mức độ** | ⚪ Minor |
| **DDL** | — |
| **UX Law** | peak-end |

**🔍 Hiện trạng**

Từ ảnh: Result screens chỉ có CTA "Tạo giao dịch mới" (outlined). Không có CTA primary "Về trang chủ" — home chỉ là icon nhỏ ở header. User mới hoàn thành GD thường muốn exit (không phải tạo GD mới). CTA secondary bias dẫn sang flow mới.

> Evidence: Từ ảnh — CTA "Tạo giao dịch mới" prominent. Home icon ~24px. Peak-End Rule: kết thúc cần clear exit.

**⚠️ Hậu quả**

- **User impact:** Phải tìm home icon nhỏ → friction khi muốn exit.
- **Violation:** Peak-End Rule — ending action cần direct, không indirect.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | CTA primary | "Về trang chủ" (filled) + "Tạo giao dịch mới" (outlined) | Bottom |

---

#### UXP-012 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Thanh toán Vietlott › Xác nhận giao dịch, Thanh toán vé xem phim › Xác nhận giao dịch, Thanh toán vé tàu › Xác nhận giao dịch |
| **Mức độ** | ⚪ Minor |
| **DDL** | COMP:otp-input-1 |
| **UX Law** | fitts |

**🔍 Hiện trạng**

Từ ảnh thanh-toan-vietlot.png (OTP overlay): 6 digit cells có spacing tight — cells gần nhau, nút X close ở trên bên phải. Bottom sheet có padding nhỏ giữa cells và CTA. OTP spec `otp-input-1` nên có cellGap ≥ 8px.

> Evidence: Từ ảnh — OTP cells spacing compact, CTA "Xác nhận" gần sát cells.

**⚠️ Hậu quả**

- **User impact:** Mis-tap giữa các cells nếu spacing quá nhỏ.
- **Violation:** Fitts's Law — target spacing.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | OTP cells | Tăng cellGap lên 12px | Bottom sheet |
| 2 | Padding | Thêm 24px padding giữa cells và CTA | Bottom sheet |

---

## Chi tiết theo màn hình

### 1. Thanh toán Vietlott › Form nhập thông tin
> `SCR-TT-001` · form · 1 artboard
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: thanh-toan-vietlot.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header hiển thị title + back + home | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: "Thanh toán mua xổ số Vietlott" + back + home icon |
| 2 | Account card hiển thị TK + số dư | Skill C | — | ✅ Pass | Từ ảnh: TK 9099798712313123, 20,000,000 VND visible |
| 3 | Thông tin dịch vụ read-only | Skill B | — | ✅ Pass | Từ ảnh: 3 info rows (Dịch vụ, Mã TT, Số tiền) read-only |
| 4 | CTA "Tiếp tục" full-width sticky | Skill C | — | ✅ Pass | Từ ảnh: CTA navy full-width ở bottom |
| 5 | Section header có icon cảnh báo | Skill C | — | ✅ Pass | Từ ảnh: icon đỏ bên trái "Thông tin thanh toán" |
| 6 | Account chevron dropdown | Skill C | — | ✅ Pass | Từ ảnh: chevron down visible = chọn TK khác |
| 7 | Fitts's Law — CTA ≥44px | Skill A | fitts | ✅ Pass | Từ ảnh: CTA 48px height full-width |
| 8 | Hick's Law — limited actions | Skill A | hicks | ❌ Gap | Từ ảnh: chỉ 1 CTA nhưng icon cảnh báo đỏ gây confusion — không rõ cảnh báo gì |

### 2. Thanh toán Vietlott › Xác nhận giao dịch
> `SCR-TT-002` · confirm · 2 artboards
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: thanh-toan-vietlot.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Banner cảnh báo kiểm tra thông tin | Skill B | UXG-78 | ❌ Gap | Từ ảnh: banner "đặt lịch" không khớp context "Vietlott" → UXP-004 |
| 2 | Info rows hiển thị đầy đủ | Skill C | — | ✅ Pass | Từ ảnh: TK, Dịch vụ, Mã TT, Số tiền, Phí — 5 rows visible |
| 3 | Số tiền bằng chữ đỏ | Skill C | — | ✅ Pass | Từ ảnh: "Năm mươi nghìn đồng" red text visible |
| 4 | OTP timer + resend button | Skill C | COMP:otp-input-1 | ❌ Gap | Từ ảnh: OTP overlay — 6 cells, NO timer, NO resend → UXP-002 |
| 5 | OTP close (×) button | Skill C | COMP:otp-input-1 | ✅ Pass | Từ ảnh: × close visible top-right |
| 6 | Auth dropdown single-option | Skill C | — | ❌ Gap | Từ ảnh: SMS OTP là option duy nhất → dropdown redundant → UXP-005 |
| 7 | Cognitive load — redundant confirm | Skill A | UXG-52 | ❌ Gap | Từ ảnh: 5 rows duplicate từ form → UXP-001 |
| 8 | Header consistency | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: "Xác nhận giao dịch" + back arrow |

### 3. Thanh toán Vietlott › Kết quả giao dịch
> `SCR-TT-003` · result · 1 artboard
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: thanh-toan-vietlot.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Success card — checkmark + amount green | Skill C | — | ✅ Pass | Từ ảnh: CoopBank logo, checkmark, "50,000 VND" green |
| 2 | Detail rows — 4 fields | Skill C | — | ✅ Pass | Từ ảnh: Thời gian, Dịch vụ, Mã TT, Mã GD visible |
| 3 | Actions — chia sẻ + lưu ảnh | Skill C | COMP:receipt-preview-1 | ✅ Pass | Từ ảnh: share + save icons + labels |
| 4 | CTA "Tạo giao dịch mới" | Skill C | — | ✅ Pass | Từ ảnh: outlined CTA bottom |
| 5 | PDF receipt option | Skill B | COMP:receipt-preview-1 | ❌ Gap | Từ ảnh: chỉ "Lưu ảnh" — thiếu PDF → UXP-009 |
| 6 | Primary exit CTA — "Về trang chủ" | Skill C | — | ❌ Gap | Từ ảnh: chỉ "Tạo giao dịch mới" + home icon nhỏ → UXP-011 |
| 7 | Peak-End Rule — positive ending | Skill A | peak-end | ✅ Pass | Từ ảnh: success prominent, green amount |
| 8 | Header home icon visible | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: home icon top-left |

### 4. Thanh toán vé xem phim › Form nhập thông tin
> `SCR-TT-004` · form · 1 artboard
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: 1000thanh-toan-ve-xem-phim.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header hiển thị title + nav | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: "Thanh toán vé xem phim" + back + home |
| 2 | Account card | Skill C | — | ✅ Pass | Từ ảnh: TK + 20M VND + chevron |
| 3 | Thông tin thanh toán 3 rows | Skill C | — | ✅ Pass | Từ ảnh: Tổng tiền 150K, Giảm 20K, Tổng GD 100K |
| 4 | Thông tin KH placeholder raw | Skill C | UXG-78 | ❌ Gap | Từ ảnh: "[Customer name]", "[Phone number]" → placeholder raw → UXP-007 |
| 5 | CTA "Tiếp tục" sticky | Skill C | — | ✅ Pass | Từ ảnh: CTA navy bottom |
| 6 | Fitts's Law — CTA size | Skill A | fitts | ✅ Pass | Từ ảnh: CTA 48px full-width |
| 7 | Email realistic | Skill C | — | ❌ Gap | Từ ảnh: "email@examplemail.com" — placeholder → UXP-007 |
| 8 | Hick's Law — simple form | Skill A | hicks | ✅ Pass | Từ ảnh: read-only, 1 CTA |

### 5. Thanh toán vé xem phim › Xác nhận giao dịch
> `SCR-TT-005` · confirm · 2 artboards
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: 1001thanh-toan-ve-xem-phim.png, 1002thanh-toan-ve-xem-phim.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Banner contextualization | Skill B | UXG-78 | ❌ Gap | Từ ảnh: "đặt lịch" ≠ "vé xem phim" → UXP-004 |
| 2 | Info rows 7 fields complete | Skill C | — | ✅ Pass | Từ ảnh: TK, DV, NCC, MaTT, TenKH, Tiền, Phí |
| 3 | Nhà cung cấp placeholder | Skill C | UXG-78 | ❌ Gap | Từ ảnh: "[provider name]" placeholder visible → UXP-007 |
| 4 | OTP timer + resend | Skill C | COMP:otp-input-1 | ❌ Gap | Từ ảnh 1002: OTP overlay no timer → UXP-002 |
| 5 | OTP close × | Skill C | COMP:otp-input-1 | ✅ Pass | Từ ảnh: × close visible |
| 6 | Auth dropdown | Skill C | — | ❌ Gap | Từ ảnh: single-option SMS OTP dropdown → UXP-005 |
| 7 | Amount bằng chữ | Skill C | — | ✅ Pass | Từ ảnh: "Một trăm nghìn đồng" red |
| 8 | Fitts's Law — OTP cells | Skill A | fitts | ✅ Pass | Từ ảnh: 6 cells adequately sized |

### 6. Thanh toán vé xem phim › Kết quả giao dịch
> `SCR-TT-006` · result · 1 artboard
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: 1003thanh-toan-ve-xem-phim.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Success card prominent | Skill C | — | ✅ Pass | Từ ảnh: checkmark + "100,000 VND" green |
| 2 | Detail rows 6 fields | Skill C | — | ✅ Pass | Từ ảnh: Thời gian, DV, NCC(CGV), MaTT, TenKH, MaGD |
| 3 | Customer name placeholder | Skill C | UXG-78 | ❌ Gap | Từ ảnh: "[Customer name]" in result → UXP-007 |
| 4 | Hotline placeholder XXXXX | Skill C | UXG-78 | ❌ Gap | Từ ảnh: "tổng đài XXXXX" → UXP-006 |
| 5 | Actions — chia sẻ + lưu ảnh | Skill C | — | ✅ Pass | Từ ảnh: icons + labels visible |
| 6 | Primary exit CTA | Skill C | — | ❌ Gap | Từ ảnh: chỉ "Tạo giao dịch mới" outlined → UXP-011 |
| 7 | Peak-End Rule | Skill A | peak-end | ✅ Pass | Từ ảnh: success prominent = positive |
| 8 | Lưu ý mã đặt chỗ rõ ràng | Skill C | — | ✅ Pass | Từ ảnh: notice yellow box visible |

### 7. Thanh toán vé tàu › Form nhập thông tin
> `SCR-TT-007` · form · 2 artboards
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: thanh-toan-ve-tau-1.png, thanh-toan-ve-tau-2.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header + nav | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: "Thanh toán vé tàu" + back + home |
| 2 | Account card | Skill C | — | ✅ Pass | Từ ảnh: TK + 20M VND |
| 3 | Data logic — sum correct | Skill C | UXG-243 | ❌ Gap | Từ ảnh: 20K tổng < 100K giảm = impossible → UXP-008 |
| 4 | Long scroll form | Skill C | UXG-52 | ❌ Gap | Từ ảnh tau-2: artboard 1407px, 20 rows → UXP-003 |
| 5 | Chiều đi info complete | Skill C | — | ✅ Pass | Từ ảnh: 7 rows chiều đi — ga, ngày, tàu, ghế, SL |
| 6 | Chiều về data copy error | Skill C | UXG-243 | ❌ Gap | Từ ảnh tau-2: "Ga đến: Sài Gòn" = ga đi → UXP-008 |
| 7 | CTA "Tiếp tục" visible | Skill C | — | ✅ Pass | Từ ảnh: CTA bottom |
| 8 | Fitts's Law — CTA | Skill A | fitts | ✅ Pass | Từ ảnh: CTA 48px full-width |

### 8. Thanh toán vé tàu › Xác nhận giao dịch
> `SCR-TT-008` · confirm · 2 artboards
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: thanh-toan-ve-tau-3.png, thanh-toan-ve-tau-4.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Banner text mismatch | Skill B | UXG-78 | ❌ Gap | Từ ảnh: "đặt lịch" ≠ "vé tàu" → UXP-004 |
| 2 | Info rows complete | Skill C | — | ✅ Pass | Từ ảnh: TK, DV, MaTT, TenKH, Tiền, Phí |
| 3 | Amount bằng chữ | Skill C | — | ✅ Pass | Từ ảnh: "Một trăm nghìn đồng" red |
| 4 | OTP timer + resend | Skill C | COMP:otp-input-1 | ❌ Gap | Từ ảnh tau-4: no timer, no resend → UXP-002 |
| 5 | OTP close × | Skill C | — | ✅ Pass | Từ ảnh: × visible |
| 6 | Auth single-option | Skill C | — | ❌ Gap | Từ ảnh: SMS OTP single dropdown → UXP-005 |
| 7 | OTP spacing tight | Skill C | COMP:otp-input-1 | ❌ Gap | Từ ảnh: cells compact, CTA close → UXP-012 |
| 8 | Header consistency | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: "Xác nhận giao dịch" + back |

### 9. Thanh toán vé tàu › Kết quả giao dịch
> `SCR-TT-009` · result · 1 artboard
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: thanh-toan-ve-tau-5.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Success card | Skill C | — | ✅ Pass | Từ ảnh: checkmark + "100,000 VND" green |
| 2 | Detail rows 4 fields | Skill C | — | ✅ Pass | Từ ảnh: Thời gian, DV, MaTT, MaGD |
| 3 | Actions | Skill C | — | ✅ Pass | Từ ảnh: chia sẻ + lưu ảnh |
| 4 | Hotline XXXXX | Skill C | UXG-78 | ❌ Gap | Từ ảnh: "tổng đài XXXXX" → UXP-006 |
| 5 | Primary exit CTA | Skill C | — | ❌ Gap | Từ ảnh: chỉ "Tạo giao dịch mới" → UXP-011 |
| 6 | PDF receipt | Skill B | COMP:receipt-preview-1 | ❌ Gap | Từ ảnh: chỉ "Lưu ảnh" → UXP-009 |
| 7 | Peak-End Rule | Skill A | peak-end | ✅ Pass | Từ ảnh: success = positive ending |
| 8 | Header home icon | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: home icon visible top-left |

---

## DDL References sử dụng

| ddl_ref | Rule | UX Law | Áp dụng |
|---------|------|--------|---------|
| UXG-52 | Long List / Information Hierarchy | cognitive-load | SCR-TT-002,005,008 confirm redundancy; SCR-TT-007 long scroll |
| UXG-78 | Content Quality | — | Banner "đặt lịch", placeholder text, hotline XXXXX |
| UXG-165 | Text Legibility | — | SCR-TT-005 provider placeholder |
| UXG-243 | Error Prevention / Data Validation | — | SCR-TT-007 math + copy errors |
| COMP:otp-input-1 | OTP input with resend timer | fitts | All confirm screens — missing timer, resend |
| COMP:app-header-1 | App header consistency | — | All screens — form has home, confirm doesn't |
| COMP:receipt-preview-1 | Receipt with PDF option | — | Result screens — only screenshot, no PDF |
