# SCR-TRK-002 — Tạo yêu cầu tra soát › Form nhập thông tin (empty)

**Screen ID:** SCR-TRK-002  
**Figma node:** 142:29396  
**Screen type:** form  
**Flow:** Tạo yêu cầu tra soát khác  
**Wireframe:** `ui/tra-soat-khac-1.png`

---

## 1. Flow & Navigation

- **Entry:** SCR-TRK-001 (menu item "Tra soát khác")
- **Next:** SCR-TRK-003 (sau khi điền form → nhấn CTA)
- **Back:** Quay về SCR-TRK-001
- **Home:** Quay về màn hình chính

### User Story

> Là người dùng Co-opBank, tôi muốn điền thông tin giao dịch cần tra soát để gửi yêu cầu tra soát khác tới ngân hàng.

---

## 2. UX Signal Inference (Phase 4e · scope=screen)

**Signals detected:**
- 9 text-field labels → long form, cần chunking strategy
- "VND" suffix → currency field cần input mask số
- Calendar icon → date picker trigger
- Dropdown chevron → selector/picker cho tài khoản thu phí
- "Nội dung tra soát" → textarea (free-text)

**Inferred UX:**
- **Pattern:** Single-page long form → cân nhắc section grouping để giảm visual overload
- **Component:** TextField (×7), DatePicker (×1), Dropdown/Selector (×1), Textarea (×1), Button Primary
- **State:** Empty (all fields), focused, filled, error
- **DDL ref:** ux-guidelines.csv#31 (Form Field Grouping), ux-guidelines.csv#44 (Input Validation), ux-laws.csv#hick

---

## 3. Mô tả màn hình

| Element | Mô tả | Ghi chú |
|---------|-------|---------|
| Header | "Tạo yêu cầu tra soát" | Back trái, Home icon phải |
| Section badge | "S Thông tin tra soát" | Màu primary, badge đỏ |
| Ngày giao dịch | Text field + calendar icon | Date picker, required |
| Loại giao dịch | Text field | Text input hoặc dropdown, required |
| Số tài khoản/ Số thẻ giao dịch | Text field | Số tài khoản, required |
| Số tiền giao dịch | Text field + suffix "VND" | Currency input, required |
| Số thẻ tài khoản/ Số thẻ nhận | Text field | Optional? |
| Mã giao dịch | Text field | Transaction ID, required |
| Lý do tra soát | Text field | Dropdown hoặc free text |
| Nội dung tra soát | Textarea | Free text, có counter |
| Tài khoản thu phí tra soát | Dropdown selector | Chọn từ danh sách tài khoản |
| CTA | Button "Tra soát" | Full-width, bottom fixed |

### NFR

- Field height ≥ 44px (touch target)
- Validation: required fields phải có error state rõ ràng
- Calendar picker: ngôn ngữ tiếng Việt
- Currency field: format 1,000,000 khi typed
- Textarea: hiển thị character counter (max 500)

---

## 4. UX Improvements (từ signal inference)

- **[Improvement 1]** Form 9 fields không có progress indicator — người dùng không biết còn bao nhiêu bước. Cân nhắc section grouping (Thông tin giao dịch / Thông tin tra soát). DDL ref: ux-guidelines.csv#31
- **[Improvement 2]** Field "Ngày giao dịch" không có placeholder hint format (DD/MM/YYYY) — UX friction khi người dùng không biết format cần nhập. DDL ref: ux-guidelines.csv#29 (Input Placeholder)
- **[Improvement 3]** Field "Số tiền giao dịch" thiếu format helper — nên tự format số với dấu phẩy ngàn khi nhập. DDL ref: ux-guidelines.csv#44 (Input Formatting)
- **[Improvement 4]** Không có tooltip/helper text cho "Mã giao dịch" — người dùng có thể không biết lấy mã này ở đâu (thường trong lịch sử giao dịch). DDL ref: ux-guidelines.csv#32 (Contextual Help)
