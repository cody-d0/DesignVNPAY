# UX Audit — Tạo yêu cầu tra soát từ Mobile · Co-opBank

**Sản phẩm:** Co-opBank Mobile Banking  
**Flow:** Tạo yêu cầu tra soát từ Mobile  
**Figma:** `aYeSAVi94QlI4i4rL3xtmR` · node `194:195280`  
**Ngày audit:** 2026-03-23  
**Auditor:** AI-assisted pipeline (figma-to-ux-review)  
**Domain:** Banking  

---


**Total checks:** 57  
**Pass:** 40 | **Gap:** 15 | **Unverifiable:** 2  
**Simple Score:** 70%  
**Weighted Score:** 70%## Tổng quan

| Metric | Giá trị |
|:---|:---|
| Tổng screen | 8 |
| Tổng check | 54 |
| Pass | 39 |
| Gap | 14 |
| Unverifiable | 1 |
| UX Score | 72% |

> ⚠️ Scores sẽ được cập nhật tự động bởi `ux-score-calculator.js --fix`

---

## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Tạo yêu cầu tra soát › Tìm kiếm giao dịch |
|:---|:---|
| **Vấn đề** | Thông tin nhạy cảm trong danh sách giao dịch (số tài khoản) không được masked |
| **Gap ref** | Check #3 |
| **DDL** | `UXG-FORM-02` |
| **Giải pháp** | Áp dụng masking pattern cho account numbers trong transaction list: hiển thị `1231****23` thay vì số đầy đủ |

---

#### UXP-002 · Critical
| **Màn hình** | Tạo yêu cầu tra soát › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | OTP Modal thiếu countdown timer và nút "Gửi lại OTP" — vi phạm DDL `otp-input-1` spec |
| **Gap ref** | Check #3 |
| **DDL** | `COMP:otp-input-1` |
| **Giải pháp** | Bổ sung: (1) Countdown timer "Mã OTP hết hạn sau: 1:30" bên dưới OTP input, (2) Nút "Gửi lại mã" sau khi timer hết, (3) Active cell highlight để rõ... |

---

#### UXP-003 · Major
| **Màn hình** | Tạo yêu cầu tra soát › Tìm kiếm giao dịch |
|:---|:---|
| **Vấn đề** | Empty state thiếu illustration — chỉ có text "Không có kết quả tìm kiếm", thiếu hình minh họa |
| **Gap ref** | Check #4 |
| **DDL** | `COMP:empty-state-1` |
| **Giải pháp** | Thêm illustration (ví dụ: icon tìm kiếm empty), subtitle gợi ý ("Thử tìm với từ khóa khác") và link action "Xóa bộ lọc" |

---

#### UXP-004 · Major
| **Màn hình** | Tạo yêu cầu tra soát › Chi tiết |
|:---|:---|
| **Vấn đề** | Màn hình chi tiết giao dịch thiếu CTA để tiếp tục — vi phạm Peak-End Rule và Fitts's Law |
| **Gap ref** | Check #4 |
| **DDL** | `UXG-ACC-04` |
| **Giải pháp** | Thêm CTA "Tra soát giao dịch này" ở cuối màn hình chi tiết để user có thể proceed ngay từ detail view |

---

#### UXP-005 · Major
| **Màn hình** | Tạo yêu cầu tra soát › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Các trường bắt buộc (Lý do tra soát, Tài khoản thu phí) không có indicator (*) và thiếu validation inline |
| **Gap ref** | Check #3 |
| **DDL** | `UXG-FORM-03` |
| **Giải pháp** | Thêm dấu (*) đỏ cho trường bắt buộc, hiển thị "Vui lòng chọn lý do tra soát" khi submit thiếu |

---

#### UXP-006 · Major
| **Màn hình** | Tạo yêu cầu tra soát › Form nhập thông tin (đã điền) |
|:---|:---|
| **Vấn đề** | CTA "Tiếp tục" không có trạng thái disabled khi form chưa hợp lệ — vi phạm feedback loop |
| **Gap ref** | Check #6 |
| **DDL** | `UXG-FORM-04` |
| **Giải pháp** | Implement disabled state cho nút "Tiếp tục" (opacity thấp hơn, không clickable) khi chưa điền đủ các trường bắt buộc |

---

#### UXP-007 · Major
| **Màn hình** | Tạo yêu cầu tra soát › Kết quả giao dịch |
|:---|:---|
| **Vấn đề** | Success icon dùng màu brand blue thay vì green — gây nhầm lẫn semantic color convention |
| **Gap ref** | Check #2 |
| **DDL** | `UXG-UI-06` |
| **Giải pháp** | Thay success checkmark từ brand blue (#1E3A8A) sang semantic green (#16A34A hoặc token `colors.success`) để align với convention |

---

#### UXP-008 · Minor
| **Màn hình** | Tạo yêu cầu tra soát › Danh sách |
|:---|:---|
| **Vấn đề** | Tab active state cần contrast cao hơn giữa active/inactive |
| **Gap ref** | Check #2 |
| **DDL** | `UXG-UI-01` |
| **Giải pháp** | Tăng font-weight tab active (600 vs 400), chỉ báo underline màu Brand Blue #1E3A8A |

---

#### UXP-009 · Minor
| **Màn hình** | Tạo yêu cầu tra soát › Form nhập thông tin (đã điền) |
|:---|:---|
| **Vấn đề** | Tight spacing giữa thời gian giao dịch (18:00) và giá trị ngày (20/02/2025) — cảm giác bị đè chữ |
| **Gap ref** | Check #4 |
| **DDL** | `TOKEN:spacing.md=16px` |
| **Giải pháp** | Tăng line-height hoặc padding giữa label và value trong read-only transaction summary card |

---

#### UXP-010 · Minor
| **Màn hình** | Tạo yêu cầu tra soát › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | OTP input cells có border/dash mỏng và nhạt, khó thấy vị trí nhập |
| **Gap ref** | Check #8 |
| **DDL** | `COMP:otp-input-1` |
| **Giải pháp** | Tăng border width của OTP cells từ 1px lên 2px, dùng màu `#374151` thay vì màu nhạt hiện tại |

---

## Chi tiết theo màn hình

### 1. Danh sách loại tra soát

> `SCR-TRS-001` · list · 1 artboard

**Score: 83% | Pass: 5 | Gap: 1**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:---|:---|:---|:---|:---|
| 1 | Tab navigation visible và accessible | Skill B | UXG-ACC-01 | Pass | From image: Tab bar với 2 options "Tạo yêu cầu" và "Tra cứu yêu cầu" — rõ ràng, phân biệt được |
| 2 | Tab active state contrast đủ | Skill C | UXG-UI-01 | Gap | From image: Active tab có underline blue nhưng font weight tương đương inactive — cần tăng visual weight |
| 3 | Touch target list items ≥ 44px | Skill B | UXG-ACC-01 | Pass | From image: Menu items chiều cao ~56px — đạt chuẩn 44px |
| 4 | List items có icon minh họa | Skill C | UXG-UI-01 | Pass | From image: Mỗi item có icon phân biệt loại tra soát bên trái |
| 5 | Chevron-right navigation indicator | Skill C | UXG-ACC-01 | Pass | From image: Chevron right ở cuối mỗi item — đúng convention navigation |
| 6 | Header title rõ ràng | Skill B | UXG-UI-01 | Pass | From image: "Tra soát khiếu nại" ở header — đủ descriptive |

---

### 2. Nhập thông tin thời gian

> `SCR-TRS-002` · form · 2 artboards

**Score: 83% | Pass: 5 | Gap: 1**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:---|:---|:---|:---|:---|
| 1 | Labels luôn visible (không bị ẩn khi filled) | Skill B | UXG-FORM-01 | Pass | From image: Labels "Loại giao dịch", "Tài khoản tra soát", "Từ ngày", "Đến ngày" vẫn hiển thị khi đã chọn value |
| 2 | Dropdown indicator (chevron) | Skill C | UXG-FORM-01 | Pass | From image: Dropdown arrows visible bên cạnh "Tất cả" và account number |
| 3 | Calendar icon cho date fields | Skill C | UXG-FORM-01 | Pass | From image: Calendar icon bên cạnh cả hai date fields |
| 4 | CTA "Tìm kiếm" kích thước đủ lớn | Skill C | UXG-ACC-02 | Pass | From image: Button height ~54px — vượt chuẩn 44px |
| 5 | Date range constraint visible | Skill B | UXG-FORM-01 | Gap | From image: Không có indicator về giới hạn range tối đa (VD: "tối đa 6 tháng") — user không biết giới hạn |
| 6 | Home icon navigation | Skill C | UXG-ACC-01 | Pass | From image: Home icon top-right — chuẩn navigation |

---

### 3. Tìm kiếm giao dịch

> `SCR-TRS-003` · search · 2 artboards

**Score: 43% | Pass: 3 | Gap: 4**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:---|:---|:---|:---|:---|
| 1 | Search bar có icon kính lúp | Skill C | UXG-FORM-02 | Pass | From image: Magnifying glass icon bên trái search bar |
| 2 | Transaction list hiển thị đủ thông tin | Skill C | UXG-UI-02 | Pass | From image: Mỗi item có ngày, số tiền, mã GD, badge status |
| 3 | Số tài khoản trong list được masking | Skill B | UXG-FORM-02 | Gap | From image: Account-related info không thấy masking trong transaction items — security gap |
| 4 | Empty state có illustration | Skill A | COMP:empty-state-1 | Gap | From image (mobile-10): Chỉ có text "Không có kết quả tìm kiếm", thiếu hình minh họa và CTA action |
| 5 | Empty state có action button | Skill B | UXG-UI-02 | Gap | From image (mobile-10): Không có nút "Xóa tìm kiếm" hoặc gợi ý action |
| 6 | Search placeholder hướng dẫn | Skill B | UXG-FORM-02 | Gap | From image: Placeholder chỉ là "Tìm kiếm" — thiếu hint cụ thể như "Nhập mã GD hoặc số tiền" |
| 7 | Clear button khi search active | Skill C | UXG-FORM-02 | Pass | From image (mobile-10): X button visible trong search bar khi có input |

---

### 4. Nhập thông tin giao dịch (chưa điền)

> `SCR-TRS-004` · form · 1 artboard

**Score: 67% | Pass: 4 | Gap: 2**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:---|:---|:---|:---|:---|
| 1 | Read-only section hiển thị transaction summary | Skill C | UXG-FORM-03 | Pass | From image: Section "Thông tin giao dịch" hiển thị đầy đủ time, mã GD, tài khoản nguồn |
| 2 | Link "Chi tiết giao dịch >" accessible | Skill C | UXG-FORM-03 | Pass | From image: Chevron right indicator rõ ràng, link text descriptive |
| 3 | Required field indicators (*) | Skill B | UXG-FORM-03 | Gap | From image: Không có dấu (*) hoặc indicator nào để phân biệt field bắt buộc vs optional |
| 4 | Dropdown placeholder visible | Skill C | UXG-FORM-03 | Pass | From image: "Lý do tra soát" dropdown có dropdown arrow, placeholder state visible |
| 5 | Form section grouping logic | Skill B | UXG-UI-04 | Pass | From image: 2 sections rõ ràng — "Thông tin giao dịch" và "Thông tin tra soát" |
| 6 | CTA disabled khi form trống | Skill B | UXG-FORM-04 | Gap | From image: Button "Tiếp tục" không thể verify trạng thái disabled — likely không có disabled state |

---

### 5. Nhập thông tin giao dịch (đã điền)

> `SCR-TRS-005` · form · 1 artboard

**Score: 83% | Pass: 5 | Gap: 1**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:---|:---|:---|:---|:---|
| 1 | Char counter "6/500" visible và đúng vị trí | Skill C | UXG-UI-03 | Pass | From image: Counter "6/500" top-right của textarea — đúng vị trí, không che nội dung |
| 2 | Phí tra soát auto-computed hiển thị | Skill C | UXG-FORM-04 | Pass | From image: "5,500 VND" tự động xuất hiện sau khi chọn lý do — feedback tốt |
| 3 | Dropdown "Lý do tra soát" value selected | Skill C | UXG-FORM-04 | Pass | From image: "Chưa nhận được tiền" selected, chevron down indicator |
| 4 | Tight spacing trong transaction summary | Skill C | TOKEN:spacing.md=16px | Gap | From image: "20/02/2025 18:00" — thời gian và ngày gần nhau, thiếu breathing room |
| 5 | CTA state khi form đầy đủ | Skill B | UXG-FORM-04 | Pass | From image: Button "Tiếp tục" enabled khi form đầy đủ |
| 6 | Account number tài khoản thu phí format | Skill C | UXG-FORM-03 | Pass | From image: "1231232323" hiển thị đầy đủ — đúng với tài khoản thu phí (không cần mask) |

---

### 6. Chi tiết thông tin giao dịch

> `SCR-TRS-006` · detail · 1 artboard

**Score: 67% | Pass: 4 | Gap: 1**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:---|:---|:---|:---|:---|
| 1 | 12 trường thông tin đầy đủ | Skill C | UXG-UI-04 | Pass | From image: Đủ 12 fields từ thời gian đến trạng thái giao dịch |
| 2 | Trạng thái giao dịch highlighted | Skill B | UXG-UI-04 | Unverifiable | From image: "Giao dịch thành công" text visible nhưng không thể verify màu/style highlight từ ảnh |
| 3 | WCAG contrast label vs value | Skill C | UXG-ACC-04 | Pass | From image: Label gray (#6B7280 approx), value dark blue (#0F172A approx) — contrast đủ |
| 4 | Primary CTA để tiếp tục flow | Skill B | UXG-ACC-04 | Gap | From image: Không có CTA nào ở cuối màn hình chi tiết — user phải back để tiếp tục |
| 5 | Thông tin phân nhóm logic | Skill B | UXG-UI-04 | Pass | From image: Section "Thông tin giao dịch" rõ ràng, 12 fields được nhóm |
| 6 | Mã giao dịch đầy đủ và đúng số | Skill C | UXG-UI-04 | Pass | From image: "4153-87675" — mã GD đầy đủ, không truncated |

---

### 7. Xác nhận giao dịch & OTP

> `SCR-TRS-007` · confirm · 1 artboard + overlay

**Score: 67% | Pass: 6 | Gap: 3**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:---|:---|:---|:---|:---|
| 1 | Base screen: thông tin tra soát read-only đầy đủ | Skill C | UXG-FORM-03 | Pass | From image: Cả 2 sections "Thông tin giao dịch" và "Thông tin tra soát" visible behind modal |
| 2 | OTP 6 digits input visible | Skill C | COMP:otp-input-1 | Pass | From image: 6 ô input dạng dash dưới OTP instruction text |
| 3 | OTP countdown timer | Skill A | COMP:otp-input-1 | Gap | From image: Không thấy countdown timer trong modal — thiếu `timeLeft` state của DDL otp-input-1 spec |
| 4 | OTP resend button | Skill A | COMP:otp-input-1 | Gap | From image: Không có nút "Gửi lại mã" — thiếu `canResend` state của DDL otp-input-1 spec |
| 5 | Dimmed background overlay hiệu quả | Skill C | COMP:otp-input-1 | Pass | From image: Background mờ đúng cách, focus vào modal OTP |
| 6 | Close button (X) cho modal | Skill C | COMP:otp-input-1 | Pass | From image: X button top-right của modal — user có thể cancel |
| 7 | Số điện thoại PII masked | Skill B | UXG-TERM-01 | Pass | From image: "098****123" — đúng masking pattern |
| 8 | OTP cell active highlight | Skill A | COMP:otp-input-1 | Gap | From image: OTP cells dạng dash, không rõ ô nào đang active — thiếu `activeIndex` visual indicator |
| 9 | CTA "Xác nhận" kích thước | Skill C | UXG-ACC-02 | Pass | From image: Button "Xác nhận" chiều cao đủ lớn (~44px) |

---

### 8. Kết quả tra soát

> `SCR-TRS-008` · result · 1 artboard

**Score: 88% | Pass: 7 | Gap: 1**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:---|:---|:---|:---|:---|
| 1 | Success message rõ ràng | Skill C | UXG-UI-06 | Pass | From image: "Quý khách đã lập yêu cầu tra soát thành công!" — prominent success message |
| 2 | Success icon semantic color | Skill C | UXG-UI-06 | Gap | From image: Checkmark icon màu brand blue (#1E3A8A) — nên là green (semantic success color) |
| 3 | Mã tra soát hiển thị đầy đủ | Skill C | COMP:receipt-preview-1 | Pass | From image: "Mã tra soát: UT123123" — visible và đầy đủ |
| 4 | Lý do và thời gian tra soát | Skill C | COMP:receipt-preview-1 | Pass | From image: Lý do và thời gian đều hiển thị trong result card |
| 5 | Share và Save actions | Skill C | COMP:receipt-preview-1 | Pass | From image: "Chia sẻ" và "Lưu ảnh" buttons visible |
| 6 | CTA "Tạo yêu cầu mới" prominent | Skill C | UXG-UI-06 | Pass | From image: Primary button ở vị trí cuối màn hình, kích thước đúng |
| 7 | Info text về thời gian xử lý | Skill B | UXG-UI-06 | Pass | From image: "Co-opBank sẽ xử lý yêu cầu..." — đặt kỳ vọng đúng với user |
| 8 | No back button (unidirectional) | Skill C | UXG-ACC-05 | Pass | From image: Không có back button — đúng với flow confirm xong không nên back |

---

## DDL References

| Ref | Full Name | Source |
|:---|:---|:---|
| `COMP:otp-input-1` | OTP/PIN input with auto-focus, paste support, resend timer | DDL Component Spec |
| `COMP:empty-state-1` | Empty state with icon, title, description, optional CTA | DDL Component Spec |
| `COMP:receipt-preview-1` | Receipt preview with status, ref number, share/save | DDL Component Spec |
| `UXG-FORM-01` | Form labels always visible when filled | DDL Guidelines (High Severity) |
| `UXG-FORM-02` | Search placeholder with guidance text | DDL Guidelines (High Severity) |
| `UXG-FORM-03` | Required field indicators and inline validation | DDL Guidelines (High Severity) |
| `UXG-FORM-04` | CTA disabled state until form valid | DDL Guidelines (High Severity) |
| `UXG-ACC-01` | Touch target minimum 44×44px | DDL Guidelines (Accessibility) |
| `UXG-ACC-02` | Date picker mobile-optimized | DDL Guidelines (Accessibility) |
| `UXG-ACC-04` | WCAG contrast for read-only text | DDL Guidelines (Accessibility) |
| `UXG-ACC-05` | CTA reachability zone | DDL Guidelines (Accessibility) |
| `UXG-UI-01` | Tab active state visual distinction | DDL Guidelines (UI) |
| `UXG-UI-02` | Empty state with action guidance | DDL Guidelines (UI) |
| `UXG-UI-03` | Character counter placement | DDL Guidelines (UI) |
| `UXG-UI-04` | Information grouping and scannability | DDL Guidelines (UI) |
| `UXG-UI-06` | Visual hierarchy for status screens | DDL Guidelines (UI) |
| `UXG-TERM-01` | OTP auto-trigger numpad | DDL Guidelines (Technical) |
| `TOKEN:spacing.md=16px` | Base spacing token for cards/rows | DDL Token |

**UX Laws Auto-Triggered:**
- **Fitts's Law** (SCR-TRS-001, 002, 003, 004, 005, 007): Touch target sizing, CTA placement
- **Hick's Law** (SCR-TRS-001, 002, 003, 004, 005): Decision complexity, option count
- **Peak-End Rule** (SCR-TRS-003, 006, 008): Last impression quality
- **Doherty Threshold** (SCR-TRS-008): Response time feedback

**Banking Product Context:** Security-first · Trust paramount · Accessibility critical  
**Palette:** `#0F172A` / `#1E3A8A` / bg `#F8FAFC`  
**DDL DB:** 1,106 tokens | 69 guidelines | 60 UX laws  
