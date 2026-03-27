# SCR-TK4-001 — Thông tin tài khoản tiết kiệm › Danh sách

**Screen ID:** SCR-TK4-001  
**Flow:** Thay đổi phương thức tất toán/ rút gốc  
**Product:** CoopBank Mobile Banking  
**Domain:** Banking  
**Screen Type:** list  
**Artboards:** 1500, 1501 (overlay), 1506 (overlay)  
**Wireframes:** `ui/1500-yoi-phuong-thuc-tat-toan.png`, `ui/1501-yoi-phuong-thuc-tat-toan.png`, `ui/1506-yoi-phuong-thuc-tat-toan.png`

---

## 1. Overview

Màn hình hiển thị chi tiết thông tin tài khoản tiết kiệm tích luỹ. Người dùng xem đầy đủ thông tin về số dư, lãi suất, chu kỳ gửi tiền và trạng thái tài khoản. Từ đây, user có thể truy cập vào **Đổi phương thức tất toán/ rút gốc** thông qua bottom-menu "Chức năng khác".

**Mục tiêu người dùng:**
- Xem thông tin chi tiết tài khoản tiết kiệm tích luỹ
- Truy cập nhanh chức năng Đổi phương thức tất toán/ rút gốc

**Màn hình liên quan:**
- → SCR-TK4-002 (khi chọn "Đổi phương thức tất toán/ rút gốc" từ bottom-menu)

---

## 2. User Story

> Là **khách hàng Co-opBank**, tôi muốn **xem thông tin tài khoản tiết kiệm và truy cập nhanh chức năng đổi phương thức tất toán** để **quản lý tài khoản tiết kiệm của mình**.

**Acceptance Criteria:**
- Hiển thị đầy đủ: tên chủ tài khoản, số tài khoản, loại sản phẩm, kỳ hạn, số dư gốc, lãi suất, trạng thái
- Bottom-menu "Chức năng khác" chứa đúng danh sách chức năng
- Popup thành công hiển thị sau khi thay đổi hoàn tất

---

## 3. Screen Content (OCR)

| Element | Text |
|:--------|:-----|
| Header | Thông tin tài khoản |
| Account type | Tài khoản tiết kiệm |
| Owner name | Tên chủ tài khoản: HA NGUYEN QUANG |
| Account number | Số tài khoản tiền gửi: 012547288 |
| Branch | Chi nhánh/ PGD mở: CN Lang Ha |
| Product type | Loại sản phẩm: Tiền gửi tích luỹ |
| Term | Kỳ hạn: 1 tháng |
| Open date | Ngày mở ban đầu: 15/03/2024 |
| Effective date | Ngày hiệu lực: 15/03/2024 |
| Maturity date | Ngày đáo hạn: 15/03/2025 |
| Initial principal | Số dư gốc ban đầu: 10,000,000 VND |
| Current principal | Số dư gốc hiện tại: 10,000,000 VND |
| Blocked amount | Số tiền phong tỏa: 0 VND |
| Accrued interest | Lãi cộng dồn: 213 VND |
| Saving method | Hình thức tích luỹ: Tích luỹ định kỳ tự động |
| Saving cycle | Chu kỳ tích luỹ: 1 tháng |
| Next saving date | Ngày tích luỹ tiếp theo: 15/05/2024 |
| Periodic amount | Số tiền tích luỹ định kỳ: 213 VND |
| Debit account | Tài khoản trích tiền: 1231231232 |
| Interest rate | Lãi suất: 0.1% |
| Status | Trạng thái tích luỹ: Hoạt động |
| CTA 1 | Tất toán tiền gửi trực tuyến |
| CTA 2 | Thay đổi thông tin tích lũy |
| CTA 3 | Lịch sử giao dịch |
| CTA 4 | Chức năng khác |
| Bottom-menu title | Chức năng khác |
| Menu item 1 | Giấy xác nhận |
| Menu item 2 | Đổi phương thức tất toán/ rút gốc |
| Success message | Quý khách đã thay đổi phương thức tất toán/ rút gốc thành công |
| Success CTA | Đóng |

---

## 4. Flow & Navigation

```
[Thông tin tài khoản]
  ↓ tap "Chức năng khác"
  → [Bottom-menu overlay: Giấy xác nhận | Đổi phương thức tất toán/ rút gốc]
    ↓ tap "Đổi phương thức tất toán/ rút gốc"
    → SCR-TK4-002

[Success popup ← sau khi thay đổi thành công từ SCR-TK4-002]
  → Đóng → [Thông tin tài khoản] (refresh state)
```

---

## 5. Non-Functional Requirements

- **Performance:** Màn hình load dữ liệu tài khoản trong < 2 giây
- **Security:** Không hiển thị số tài khoản đầy đủ (nên mask một phần)
- **Accessibility:** Labels đọc được bởi VoiceOver/TalkBack
- **Typography:** Số tiền hiển thị định dạng VND chuẩn (có dấu phẩy phân cách nghìn)

---

## 6. UX Signal Analysis (Phase 4e)

**Signals detected:**
- `"Chức năng khác"` → bottom-menu pattern → trigger: other functions
- `"Tất toán tiền gửi trực tuyến"` → primary CTA nhiều nhất → user journey: settlement
- `"10,000,000 VND"` × 2 → financial data display → clarity requirement high
- `"Hoạt động"` → status badge → visual differentiation needed
- `"0.1%"` → very low interest rate → information hierarchy

**UX Laws triggered:**
- **Hick's Law:** 4 CTAs visible + bottom-menu items → decision overload risk
- **Miller's Law:** 20+ data fields on one screen → chunking needed
- **Fitts' Law:** CTA buttons at bottom require scroll → accessibility issue
