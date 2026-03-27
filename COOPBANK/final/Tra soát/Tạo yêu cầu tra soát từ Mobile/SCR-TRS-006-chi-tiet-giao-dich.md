# SCR-TRS-006 — Tạo yêu cầu tra soát › Chi tiết

## 1. Screen Identity
- **Screen ID:** SCR-TRS-006
- **Display Name:** Tạo yêu cầu tra soát › Chi tiết
- **Screen Type:** detail
- **Artboards:** Tra soát Mobile 7 (142:29720)
- **Wireframe:** `ui/tra-soat-mobile-7.png`

## 2. User Story
Là người dùng, tôi muốn xem đầy đủ chi tiết giao dịch (12 trường) để xác nhận đây đúng là giao dịch cần tra soát.

## 3. Screen Content (OCR)
| Element | Text | Role |
|:---|:---|:---|
| Header | Chi tiết giao dịch | header_title |
| Section | Thông tin giao dịch | section_header |
| Row | Thời gian giao dịch: 30/12/2020 10:20 | detail_row |
| Row | Mã giao dịch: 4153-87675 | detail_row |
| Row | Tài khoản nguồn: 123123132 | detail_row |
| Row | Tài khoản thụ hưởng: 123123132 | detail_row |
| Row | Tên người thụ hưởng: NGUYEN VAN A | detail_row |
| Row | Ngân hàng thụ hưởng: Ngân hàng Vietcombank | detail_row |
| Row | Số tiền giao dịch: 100,000 VND | detail_row |
| Row | Đối tượng chịu phí: Người chuyển trả | detail_row |
| Row | Phí giao dịch và thuế: 5,500 VND | detail_row |
| Row | Loại giao dịch: Chuyển tiền nhanh 24/7 qua tài khoản | detail_row |
| Row | Nội dung giao dịch: 123 | detail_row |
| Row | Trạng thái giao dịch: Giao dịch thành công | detail_row_status |

## 4. Functional Requirements
- Read-only detail view với 12 data fields
- Trạng thái: "Giao dịch thành công" (cần highlight màu xanh/green)
- Back navigation → quay lại form

## 5. Non-Functional Requirements
- Label-value layout: label gray, value dark
- Long text truncate với expand option nếu cần

## 6. Flow
- **Entry:** SCR-TRS-004 hoặc SCR-TRS-005 → link "Chi tiết giao dịch >"
- **Exit [Back]:** Quay lại form đã điền
