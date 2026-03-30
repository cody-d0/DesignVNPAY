# SCR-TRK-003 — Tạo yêu cầu tra soát › Form nhập thông tin (filled)

**Screen ID:** SCR-TRK-003  
**Figma node:** 142:29411  
**Screen type:** form  
**Flow:** Tạo yêu cầu tra soát khác  
**Wireframe:** `ui/tra-soat-khac-2.png`

---

## 1. Flow & Navigation

- **State:** Filled state của form SCR-TRK-002 (variant)
- **Next:** SCR-TRK-004 (nhấn "Tra soát" → xác nhận)
- **Back:** Giữ nguyên dữ liệu đã nhập

### User Story

> Là người dùng Co-opBank, sau khi điền đầy đủ thông tin giao dịch tra soát, tôi muốn xem lại và submit để chuyển sang bước xác nhận.

---

## 2. UX Signal Inference (Phase 4e · scope=screen)

**Signals detected (filled state):**
- "12/02/2025" → date field filled, format DD/MM/YYYY
- "Chuyển tiền nội bộ" → loại giao dịch là text filled (or từ dropdown)
- "20,000,000" → số tiền format 1,000,000 style ✅
- "6/500" → character counter cho textarea — MAX 500 chars
- "Sai số tiền" → lý do tra soát là dropdown/preset value
- "12312331" → tài khoản thu phí đã chọn từ dropdown

**Inferred UX:**
- **CTA active:** Khi tất cả required fields filled → button "Tra soát" active
- **Character counter:** `6/500` visible, cần tiếp tục visible khi typing
- **Field filled style:** Text màu đậm hơn placeholder (primary vs secondary)
- **DDL ref:** ux-guidelines.csv#44 (Filled State), ux-guidelines.csv#46 (CTA Active State)

---

## 3. Mô tả màn hình

| Element | Giá trị mẫu | Ghi chú |
|---------|-------------|---------|
| Ngày giao dịch | 12/02/2025 | Format DD/MM/YYYY, bold |
| Loại giao dịch | Chuyển tiền nội bộ | Text bold |
| Số tài khoản/ Số thẻ GD | 12312323213 | Account number |
| Số tiền giao dịch | 20,000,000 VND | Formatted số, suffix VND |
| Số thẻ TK/ Số thẻ nhận | 1213123123 | |
| Mã giao dịch | #123123 | Transaction ID |
| Lý do tra soát | Sai số tiền | Preset value |
| Nội dung tra soát | abc123 | 6/500 counter |
| Tài khoản thu phí | 12312331 | Dropdown filled |
| CTA | "Tra soát" | Active (enabled) |

### NFR

- CTA phải disable khi có field required chưa điền
- "Sai số tiền" phải là preset options (không free-text) → UX nhất quán
- Số tiền format: dấu phẩy ngàn, không decimal

---

## 4. UX Improvements (từ signal inference)

- **[Improvement 1]** Không có inline validation real-time — người dùng chỉ biết lỗi khi nhấn submit. Nên validate on-blur từng field. DDL ref: ux-guidelines.csv#44
- **[Improvement 2]** "Lý do tra soát: Sai số tiền" — cần verify đây là dropdown preset, không phải free text, để đảm bảo data quality cho backend. DDL ref: ux-guidelines.csv#36 (Constrained Input)
- **[Improvement 3]** Field "Nội dung tra soát" đang hiển thị "6/500" nhưng không có helper text về nội dung cần ghi — nên có placeholder "Mô tả chi tiết vấn đề bạn gặp phải…". DDL ref: ux-guidelines.csv#29
