# UX Audit — Tạo yêu cầu tra soát khác · Co-opBank

**Sản phẩm:** Co-opBank Mobile Banking  
**Flow:** Tạo yêu cầu tra soát khác  
**Figma:** `aYeSAVi94QlI4i4rL3xtmR` · node `194:195713`  
**Ngày audit:** 2026-03-23  
**Auditor:** AI-assisted pipeline (figma-to-ux-review)  
**Domain:** Banking  

---


**Total checks:** 47  
**Pass:** 32 | **Gap:** 14 | **Unverifiable:** 1  
**Simple Score:** 68%  
**Weighted Score:** 68%## Tổng quan

| Metric | Giá trị |
|:---|:---|
| Tổng screen | 5 |
| Tổng check | 0 |
| Pass | 0 |
| Gap | 0 |
| Unverifiable | 0 |
| UX Score | 0% |

> ⚠️ Scores sẽ được cập nhật tự động bởi `ux-score-calculator.js --fix`

---

## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Xác nhận yêu cầu tra soát › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | OTP bottom sheet thiếu countdown timer và nút "Gửi lại OTP" — vi phạm DDL `otp-input-1` spec (`canResend`, `timeLeft` states) |
| **Gap ref** | Check #6 |
| **DDL** | `COMP:otp-input-1` |
| **Giải pháp** | Bổ sung: (1) Countdown timer "Mã OTP hết hạn sau: 1:00" bên dưới 6 cells, (2) Nút "Gửi lại mã" (disabled trong countdown, active sau 60s), (3) Acti... |

---

#### UXP-002 · Critical
| **Màn hình** | Xác nhận yêu cầu tra soát › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | Trường "Loại giai dịch" có typo — đúng là "Loại giao dịch". Lỗi chính tả trên màn xác nhận gây mất tin tưởng (Trust paramount) |
| **Gap ref** | Check #4 |
| **DDL** | `UXG-CONTENT-01` |
| **Giải pháp** | Sửa "giai" → "giao" trong label trường. Audit toàn bộ labels trong flow để phát hiện typo tương tự |

---

#### UXP-003 · Critical
| **Màn hình** | Xác nhận yêu cầu tra soát › Chi tiết giao dịch (bottom sheet) |
|:---|:---|
| **Vấn đề** | "Trạng thái giao dịch: Label 2" — giá trị placeholder chưa được thay thế bằng trạng thái thực. Hiển thị "Label 2" trên màn client-facing là lỗi nghiêm trọng |
| **Gap ref** | Check #10 |
| **DDL** | `UXG-CONTENT-01` |
| **Giải pháp** | Map "Label 2" sang giá trị thực: "Thành công" / "Đang xử lý" / "Thất bại" với badge màu semantic tương ứng (green/orange/red) |

---

#### UXP-004 · Major
| **Màn hình** | Tạo yêu cầu tra soát › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | 9 fields trong 1 màn không có grouping — Hick's Law: quá nhiều lựa chọn visual cùng lúc gây cognitive overload |
| **Gap ref** | Check #7 |
| **DDL** | `UXG-FORM-03` |
| **Giải pháp** | Chia form thành 2 sections: (1) "Thông tin giao dịch" (Ngày, Loại, Số TK, Số tiền, Số thẻ nhận, Mã GD) và (2) "Thông tin tra soát" (Lý do, Nội dung... |

---

#### UXP-005 · Major
| **Màn hình** | Tạo yêu cầu tra soát › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Các fields không có placeholder text gợi ý format — người dùng không biết nhập gì. Đặc biệt: "Ngày giao dịch" thiếu hint "DD/MM/YYYY", "Mã giao dịch" thiếu "Ví dụ: #123456" |
| **Gap ref** | Check #3, Check #4 |
| **DDL** | `COMP:text-input-1` |
| **Giải pháp** | Thêm placeholder cho mỗi field. Ngày GD: "DD/MM/YYYY". Mã GD: "Xem trong lịch sử giao dịch". Nội dung: "Mô tả chi tiết vấn đề..." |

---

#### UXP-006 · Major
| **Màn hình** | Xác nhận yêu cầu tra soát › Chi tiết giao dịch (bottom sheet) |
|:---|:---|
| **Vấn đề** | Close button "×" trong bottom sheet có size 20×20px — dưới ngưỡng touch target 44×44px (Fitts's Law). User khó dismiss bottom sheet |
| **Gap ref** | Check #9 |
| **DDL** | `UXG-ACC-01` |
| **Giải pháp** | Tăng hit area của "×" lên 44×44px (có thể giữ icon nhỏ với padding). Hoặc thêm drag handle ở top của bottom sheet để dismiss bằng swipe |

---

#### UXP-007 · Major
| **Màn hình** | Kết quả giao dịch › Kết quả tra soát |
|:---|:---|
| **Vấn đề** | "trong thời gian tra soát quy định" — quá mơ hồ, không có SLA cụ thể. User không biết phải chờ bao lâu (Doherty Threshold: user cần feedback về khi nào kết quả đến) |
| **Gap ref** | Check #7 |
| **DDL** | `COMP:receipt-preview-1` |
| **Giải pháp** | Thêm SLA cụ thể: "Co-opBank sẽ xử lý và thông báo kết quả trong vòng **5-7 ngày làm việc**" |

---

#### UXP-008 · Minor
| **Màn hình** | Kết quả giao dịch › Kết quả tra soát |
|:---|:---|
| **Vấn đề** | "Mã tra soát: UT123123" không có tap-to-copy. User cần mã này để follow-up với ngân hàng |
| **Gap ref** | Check #4 |
| **DDL** | `UXG-DATA-01` |
| **Giải pháp** | Thêm copy icon bên cạnh UT123123. Tap → toast "Đã sao chép mã tra soát" |

---

#### UXP-009 · Minor
| **Màn hình** | Tạo yêu cầu tra soát › Form nhập thông tin (đã điền) |
|:---|:---|
| **Vấn đề** | Character counter "6/500" cho Nội dung tra soát có màu gray nhạt (~#999999) trên nền trắng — est. contrast 2.3:1, dưới ngưỡng WCAG AA 4.5:1 |
| **Gap ref** | Check #3 |
| **DDL** | `TOKEN:base.muted-foreground` |
| **Giải pháp** | Dùng màu counter ≥ #767676 (contrast 4.54:1 vs white). Hoặc dùng token `base.muted-foreground` đã pass WCAG |

---

#### UXP-010 · Minor
| **Màn hình** | Tra soát khiếu nại › Danh sách |
|:---|:---|
| **Vấn đề** | Tab "Tra cứu yêu cầu" không có badge count — người dùng không biết có bao nhiêu yêu cầu đang xử lý |
| **Gap ref** | Check #6 |
| **DDL** | `UXG-NAV-01` |
| **Giải pháp** | Thêm badge số (VD "2") vào tab "Tra cứu yêu cầu" khi có yêu cầu đang chờ xử lý |

---

## Chi tiết theo màn hình

### 1. Tra soát khiếu nại › Danh sách

> `SCR-TRK-001` · list · 1 artboard

**Score: 83% | Pass: 5 | Gap: 1**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:---|:---|:---|:---|:---|
| 1 | Tab navigation visible và active state rõ | Skill B | UXG-NAV-01 | Pass | From ảnh tra-soat-khac-0.png: Tab "Tạo yêu cầu" có underline active màu primary blue, phân biệt rõ với tab inactive |
| 2 | Touch target menu items ≥ 44px | Skill C | UXG-ACC-01 | Pass | From ảnh: Menu rows chiều cao ~56px, vượt chuẩn 44px |
| 3 | Menu items có icon phân biệt | Skill C | UXG-UI-04 | Pass | From ảnh: Icon mobile (Mobilebanking) và icon calendar-like (Tra soát khác) — phân biệt 2 loại |
| 4 | Chevron-right navigation indicator | Skill C | UXG-NAV-01 | Pass | From ảnh: Chevron right cuối mỗi item — chuẩn disclosure navigation pattern |
| 5 | Header title mô tả đúng context | Skill B | UXG-UI-04 | Pass | From ảnh: "Tra soát khiếu nại" — mô tả đúng section, user biết mình đang ở đâu |
| 6 | Empty area bên dưới 2 items có guidance | Skill B | UXG-EMPTY-01 | Gap | From ảnh: Vùng dưới 2 items = gray trống, không có micro-copy guidance "Chọn loại tra soát để bắt đầu" |

---

### 2. Tạo yêu cầu tra soát › Form nhập thông tin (empty)

> `SCR-TRK-002` · form · 1 artboard

**Score: 67% | Pass: 6 | Gap: 3**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:---|:---|:---|:---|:---|
| 1 | Labels visible cho tất cả fields | Skill B | COMP:text-input-1 | Pass | From ảnh tra-soat-khac-1.png: 9 labels rõ ràng cho 9 fields |
| 2 | Calendar icon cho "Ngày giao dịch" | Skill C | COMP:text-input-1 | Pass | From ảnh: Calendar icon top-right của field Ngày giao dịch — trigger date picker |
| 3 | Placeholder text gợi ý format | Skill A | COMP:text-input-1 | Gap | From ảnh: Không có placeholder text trong bất kỳ field nào — fields trống không có hint |
| 4 | Helper text/context cho Mã giao dịch | Skill B | COMP:text-input-1 | Gap | From ảnh: Không có helper text "Xem trong lịch sử GD" — user không biết lấy mã ở đâu |
| 5 | VND suffix cho Số tiền giao dịch | Skill C | UXG-FORM-02 | Pass | From ảnh: "VND" suffix bên phải field số tiền — rõ ràng đơn vị tiền tệ |
| 6 | Dropdown indicator cho Tài khoản thu phí | Skill C | UXG-FORM-02 | Pass | From ảnh: Chevron down (▼) bên cạnh field Tài khoản thu phí — trigger dropdown selector |
| 7 | Form grouping — 9 fields có section header | Skill B | UXG-FORM-03 | Gap | From ảnh: Chỉ có 1 section "Thông tin tra soát" cho tất cả 9 fields — thiếu chunking theo nhóm |
| 8 | CTA "Tra soát" kích thước đủ lớn | Skill C | UXG-ACC-02 | Pass | From ảnh: Button full-width, height ~54px — vượt chuẩn 44px |
| 9 | Header navigation (back + home) | Skill C | UXG-NAV-01 | Pass | From ảnh: Back arrow trái + Home icon phải — đủ navigation options |

---

### 3. Tạo yêu cầu tra soát › Form nhập thông tin (filled)

> `SCR-TRK-003` · form · 1 artboard

**Score: 71% | Pass: 5 | Gap: 2**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:---|:---|:---|:---|:---|
| 1 | Giá trị filled hiển thị đậm hơn placeholder | Skill C | COMP:text-input-1 | Pass | From ảnh tra-soat-khac-2.png: Values màu đậm hơn labels gray — visual distinction tốt |
| 2 | Character counter "6/500" visible | Skill C | COMP:text-input-1 | Pass | From ảnh: "6/500" hiển thị bên phải textarea Nội dung tra soát |
| 3 | Character counter contrast đủ WCAG | Skill C | TOKEN:base.muted-foreground | Gap | From ảnh: Counter gray (~#999999) est. contrast 2.3:1 vs white — FAIL WCAG AA (4.5:1 required) |
| 4 | Số tiền format với dấu phẩy ngàn | Skill C | UXG-FORM-02 | Pass | From ảnh: "20,000,000" hiển thị đúng format với dấu phẩy ngàn |
| 5 | Dropdown Tài khoản thu phí có value | Skill C | UXG-FORM-02 | Pass | From ảnh: "12312331" hiển thị trong field dropdown — đã chọn |
| 6 | Inline validation state (valid indicator) | Skill B | COMP:text-input-1 | Gap | From ảnh: Không có checkmark/indicator nào show field valid sau khi điền — user không biết field ok |
| 7 | CTA active khi form đầy đủ | Skill B | UXG-FORM-04 | Pass | From ảnh: Button "Tra soát" có màu solid — enabled state khi form đầy đủ |

---

### 4. Xác nhận yêu cầu tra soát › Xác nhận giao dịch

> `SCR-TRK-004` · confirm · 3 artboards (base + 2 overlays)

**Score: 58% | Pass: 7 | Gap: 5**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:---|:---|:---|:---|:---|
| 1 | 2 sections review rõ ràng | Skill C | UXG-FORM-03 | Pass | From ảnh tra-soat-khac-3.png: Section "Thông tin giao dịch" và "Thông tin tra soát" với badge S đỏ |
| 2 | Link "Chi tiết giao dịch >" accessible | Skill C | UXG-NAV-01 | Pass | From ảnh: Chevron right + blue text — rõ là link tương tác |
| 3 | Phí tra soát hiển thị trước confirm | Skill B | UXG-TRUST-01 | Pass | From ảnh: "Phí tra soát: 5,500 VND" visible — user aware of cost |
| 4 | Label typo "Loại giai dịch" | Skill C | UXG-CONTENT-01 | Gap | From ảnh: Rõ ràng thấy "Loại giai dịch" thay vì "Loại giao dịch" — typo trên màn xác nhận |
| 5 | OTP 6-cell input visible | Skill C | COMP:otp-input-1 | Pass | From ảnh tra-soat-khac-5.png: 6 ô digit-input trong OTP bottom sheet |
| 6 | OTP countdown timer | Skill A | COMP:otp-input-1 | Gap | DDL `otp-input-1` spec: `timeLeft` state required. From ảnh: Không có countdown timer trong OTP sheet |
| 7 | OTP resend button | Skill A | COMP:otp-input-1 | Gap | DDL `otp-input-1` spec: `canResend` + resend button required. From ảnh: Chỉ có 6 cells + CTA "Xác nhận" |
| 8 | Phone number PII masked | Skill B | UXG-SEC-01 | Pass | From ảnh: "098****123" — masking đúng chuẩn bảo mật |
| 9 | Bottom sheet close button size | Skill C | UXG-ACC-01 | Gap | From ảnh tra-soat-mobile-11.png: Close "×" icon 20×20px — dưới ngưỡng 44px touch target |
| 10 | "Trạng thái giao dịch" có giá trị thực | Skill C | UXG-CONTENT-01 | Gap | From ảnh tra-soat-mobile-11.png: "Label 2" - placeholder chưa map sang status thực |
| 11 | Bottom sheet dimmed background | Skill C | COMP:otp-input-1 | Pass | From ảnh: Background mờ (blur) toàn màn khi bottom sheet mở — focus rõ ràng |
| 12 | CTA "Tiếp tục" visible và kích thước đủ | Skill C | UXG-ACC-02 | Pass | From ảnh: Button "Tiếp tục" full-width bottom, height đủ lớn |

---

### 5. Kết quả giao dịch › Kết quả tra soát

> `SCR-TRK-005` · result · 1 artboard

**Score: 80% | Pass: 8 | Gap: 2**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:---|:---|:---|:---|:---|
| 1 | Success message rõ ràng và prominent | Skill C | UXG-UI-06 | Pass | From ảnh tra-soat-khac-6.png: "Quý khách đã lập yêu cầu tra soát thành công!" bold, dưới success icon |
| 2 | Success icon (checkmark circle) | Skill C | COMP:receipt-preview-1 | Pass | From ảnh: ✓ checkmark circle center card — Peak-End Rule: positive memorable ending |
| 3 | Mã tra soát hiển thị đầy đủ | Skill C | COMP:receipt-preview-1 | Pass | From ảnh: "Mã tra soát: UT123123" — visible và không bị truncate |
| 4 | Mã tra soát tap-to-copy | Skill B | UXG-DATA-01 | Gap | From ảnh: Không có copy icon/action cho UT123123 — user cần mã này để follow-up |
| 5 | Lý do tra soát hiển thị trong receipt | Skill C | COMP:receipt-preview-1 | Pass | From ảnh: "Lý do tra soát: Chưa nhận được tiền" — confirmation của nội dung đã submit |
| 6 | Thời gian tra soát hiển thị | Skill C | COMP:receipt-preview-1 | Pass | From ảnh: "Thời gian tra soát: 29/09/2025 12:30" |
| 7 | SLA thời gian xử lý cụ thể | Skill B | COMP:receipt-preview-1 | Gap | From ảnh: "trong thời gian tra soát quy định" — mơ hồ, không có SLA ngày cụ thể |
| 8 | Share/Save secondary actions | Skill C | COMP:receipt-preview-1 | Pass | From ảnh: "Chia sẻ" và "Lưu ảnh" với icon visible |
| 9 | CTA "Tạo yêu cầu mới" không bị nhầm primary | Skill B | UXG-UI-06 | Pass | From ảnh: Button outline/secondary style — không bị nhầm với primary action |
| 10 | Co-opBank logo ở top card | Skill C | UXG-TRUST-01 | Pass | From ảnh: Co-opBank logo trong card — brand trust signal |

---

## DDL References

| Ref | Full Name | Source |
|:---|:---|:---|
| `COMP:otp-input-1` | OTP/PIN input with auto-focus, paste support, resend timer | DDL Component Spec |
| `COMP:text-input-1` | Enhanced text input with label, helper text, error, char count | DDL Component Spec |
| `COMP:receipt-preview-1` | Receipt preview with paper-style layout, share/print actions | DDL Component Spec |
| `UXG-NAV-01` | Tab navigation active state + badge indicator | DDL Guidelines (Navigation) |
| `UXG-FORM-02` | Input suffix/prefix and format indicators | DDL Guidelines (Form) |
| `UXG-FORM-03` | Required field indicators and section grouping | DDL Guidelines (Form) |
| `UXG-FORM-04` | CTA disabled state until form valid | DDL Guidelines (Form) |
| `UXG-ACC-01` | Touch target minimum 44×44px | DDL Guidelines (Accessibility) |
| `UXG-ACC-02` | CTA button minimum sizing | DDL Guidelines (Accessibility) |
| `UXG-UI-04` | Information grouping and scannability | DDL Guidelines (UI) |
| `UXG-UI-06` | Visual hierarchy for status/result screens | DDL Guidelines (UI) |
| `UXG-CONTENT-01` | Content accuracy and typo prevention | DDL Guidelines (Content) |
| `UXG-SEC-01` | PII masking for phone/account in OTP context | DDL Guidelines (Security) |
| `UXG-TRUST-01` | Cost/fee visibility before confirmation | DDL Guidelines (Trust) |
| `UXG-DATA-01` | Copyable reference data (order IDs, ref numbers) | DDL Guidelines (Data) |
| `UXG-EMPTY-01` | Empty state guidance text | DDL Guidelines (Empty State) |
| `TOKEN:base.muted-foreground` | Muted text color token for WCAG-compliant gray | DDL Token |

**UX Laws Auto-Triggered:**
- **Fitts's Law** (SCR-TRK-002, 003, 004): Touch target sizing, CTA placement, close button size
- **Hick's Law** (SCR-TRK-002, 003, 004): 9 fields cognitive load, choice complexity
- **Doherty Threshold** (SCR-TRK-005): SLA expectation, response time feedback
- **Peak-End Rule** (SCR-TRK-005): Memorable ending — success state quality

**Banking Product Context:** Security-first · Trust paramount · Accessibility critical  
**Palette:** `#0F172A` / `#1E3A8A` / bg `#F8FAFC`  
**DDL DB:** 1,106 tokens | 69 guidelines | 60 UX laws  
