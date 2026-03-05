# Đặt lịch chuyển tiền — Tổng quan tính năng

Tài liệu PRD mô tả tính năng quản lý danh sách đặt lịch chuyển tiền trong ứng dụng Co-op Bank KHCN.

---

## Mục lục

1. [Chân dung khách hàng](#1-chân-dung-khách-hàng)
2. [Tổng quan tính năng](#2-tổng-quan-tính-năng)
3. [Tính năng chính](#3-tính-năng-chính)
4. [Phạm vi](#4-phạm-vi)
5. [Hệ thống tích hợp](#5-hệ-thống-tích-hợp)
6. [Success Metrics](#6-success-metrics)
7. [User Flow chính](#7-user-flow-chính)
8. [Cấu trúc tài liệu PRD](#8-cấu-trúc-tài-liệu-prd)

---

## 1. Chân dung khách hàng

> **`🤖 by AI`** | Nguồn: Suy luận từ Figma | Độ tin cậy: Medium
>
> **Persona:** Khách hàng cá nhân Co-op Bank, sử dụng ứng dụng mobile banking, có nhu cầu đặt lịch chuyển tiền tự động (trả tiền thuê nhà, gửi tiền định kỳ cho người thân, thanh toán hàng tháng). Ưu tiên sự tiện lợi, muốn thiết lập một lần và quản lý linh hoạt (tạm dừng, hủy, tiếp tục).

---

## 2. Tổng quan tính năng
**Đặt lịch chuyển tiền** là tính năng cho phép khách hàng cá nhân thiết lập giao dịch chuyển tiền tự động theo lịch (1 lần, hàng ngày, hàng tuần, hàng tháng) trong ứng dụng Co-op Bank KHCN.
- **Đơn vị tham khảo:** Co-op Bank, các ngân hàng TMCP Việt Nam.
- **Giá trị cốt lõi:** Tự động hóa chuyển tiền định kỳ, giảm thao tác thủ công, quản lý trạng thái linh hoạt.

---

## 3. Tính năng chính

| STT | Tên tính năng | Mô tả |
|:---:|---|---|
| 1 | Danh sách đặt lịch chuyển tiền | Hiển thị danh sách các lệnh đặt lịch với thông tin tóm tắt và trạng thái |
| 2 | Bộ lọc tìm kiếm | Lọc danh sách theo trạng thái lệnh hoặc khoảng thời gian |
| 3 | Quản lý đặt lịch chuyển tiền | Quản lý các lệnh đặt lịch: tạm dừng, hủy, tiếp tục |
| 4 | Chi tiết giao dịch đặt lịch | Xem chi tiết thông tin lệnh đặt lịch với các hành động theo trạng thái |
| 5 | Lịch sử giao dịch | Xem danh sách các giao dịch đã thực hiện của một lệnh đặt lịch |
| 6 | Xác nhận hành động | Dialog xác nhận trước khi tạm dừng hoặc hủy lệnh |
| 7 | Xác thực Soft OTP | Xác thực giao dịch bằng mã PIN Soft OTP |
| 8 | Trạng thái trống | Hiển thị thông báo khi không có dữ liệu phù hợp |

---

## 4. Phạm vi

### 4.1. In Scope (MVP)
- Hiển thị danh sách lệnh đặt lịch chuyển tiền nội bộ (cùng chủ, khác chủ)
- Lọc theo trạng thái lệnh và khoảng thời gian
- Xem chi tiết giao dịch đặt lịch
- Tạm dừng / Tiếp tục / Hủy lệnh đặt lịch
- Xác thực Soft OTP cho hành động quản lý
- Xem lịch sử giao dịch đã thực hiện

### 4.2. Out of Scope & Roadmap

> **`🤖 by AI`** | Nguồn: Case study banking apps | Độ tin cậy: Low
>
> Các hạng mục dưới đây suy luận từ thực tế các app ngân hàng Việt Nam; cần PM xác nhận roadmap.

- **Tạo mới đặt lịch:** Tạo lệnh đặt lịch mới (screen riêng).
- **Chuyển tiền liên ngân hàng:** Đặt lịch chuyển tiền ngoài hệ thống.
- **Thông báo push:** Nhắc nhở trước khi giao dịch thực hiện.

---

## 5. Hệ thống tích hợp
- **Core Banking System (CBS):** Xử lý giao dịch chuyển tiền, quản lý tài khoản.
- **Soft OTP Service:** Xác thực giao dịch bằng mã PIN.
- **Notification Service:** Gửi thông báo kết quả giao dịch.

---

## 6. Success Metrics
- **Tỷ lệ sử dụng:** Số lượng khách hàng sử dụng tính năng đặt lịch / tổng KH active.
- **Tỷ lệ thành công:** Số giao dịch đặt lịch thực hiện thành công / tổng số lệnh.
- **Tỷ lệ hủy:** Số lệnh bị hủy trước khi hoàn thành / tổng lệnh tạo.

> **UNSPECIFIED** — Cần BA/PM xác nhận target values cụ thể cho từng chỉ tiêu.

---

## 7. User Flow chính
1. **Xem danh sách:** KH vào màn Danh sách đặt lịch, xem các lệnh đang hoạt động.
2. **Lọc tìm kiếm:** KH sử dụng bộ lọc theo trạng thái hoặc thời gian để tìm lệnh cụ thể.
3. **Xem chi tiết:** KH chọn một lệnh để xem thông tin chi tiết.
4. **Quản lý lệnh:** KH chọn Tạm dừng / Hủy / Tiếp tục lệnh đặt lịch.
5. **Xác nhận:** Hệ thống hiển thị dialog xác nhận hành động.
6. **Xác thực OTP:** KH nhập mã PIN Soft OTP để xác thực.
7. **Kết quả:** Hệ thống thông báo kết quả (thành công / thất bại).

---

## 8. Cấu trúc tài liệu PRD

Bộ tài liệu PRD bao gồm 8 file tính năng chi tiết:

| STT | Tài liệu | Mô tả chức năng |
|:---:|---|---|
| 1 | [Danh sách đặt lịch chuyển tiền](./danh-sach-dat-lich.md) | Hiển thị danh sách các lệnh đặt lịch với trạng thái |
| 2 | [Bộ lọc tìm kiếm](./bo-loc-tim-kiem.md) | Bộ lọc theo trạng thái lệnh hoặc khoảng thời gian |
| 3 | [Quản lý đặt lịch chuyển tiền](./quan-ly-dat-lich.md) | Quản lý lệnh: tạm dừng, hủy, xem kết quả |
| 4 | [Chi tiết giao dịch đặt lịch](./chi-tiet-dat-lich.md) | Chi tiết thông tin lệnh với hành động theo trạng thái |
| 5 | [Lịch sử giao dịch](./lich-su-giao-dich.md) | Danh sách giao dịch đã thực hiện |
| 6 | [Xác nhận hành động](./xac-nhan-hanh-dong.md) | Dialog xác nhận tạm dừng / hủy lệnh |
| 7 | [Xác thực Soft OTP](./xac-thuc-soft-otp.md) | Nhập mã PIN Soft OTP để xác thực |
| 8 | [Trạng thái trống](./trang-thai-trong.md) | Hiển thị khi không có kết quả |

---

## Các mục cần bổ sung (UNSPECIFIED)

| # | File | Section | Mục | Lý do |
|---|------|---------|-----|-------|
| 1 | overview | 6. Success Metrics | Target values | Cần BA/PM xác nhận chỉ tiêu cụ thể |

---

## Tổng hợp nội dung AI đề xuất (🤖 by AI)

### Overview
| # | Section | Loại đề xuất | Độ tin cậy | Nguồn |
|---|---------|-------------|-----------|-------|
| 1 | 1. Chân dung KH | Persona đề xuất | Medium | Suy luận từ Figma |
| 2 | 4.2 Out of Scope | Roadmap | Low | Case study banking apps |

**Thống kê:**
- Tổng số 🤖 by AI blocks: ~40
- High confidence: ~15 | Medium: ~18 | Low: ~7
- Nguồn: Figma (~20) | UX guidelines (~10) | INFERRED (~10)

---

## Kết quả chạy pipeline (Phase Report)

| Phase | Kết quả |
|-------|---------|
| 0 | Bỏ qua (node section 5199:5931). |
| 1 | file_key: kPft93N2A3gYOC3YwuXpQR, node_id: 5199:5931; 15 artboards; 15 ảnh lưu; variables: không. |
| 2 | 8 screens (screen_boundaries: 8); components tổng: ~65; OCR: đã chạy 2 round vision cho 8 màn (15 ảnh); flow_graph: 12 edges. |
| 3 | feature_file_plan: 8; 1 overview + 8 feature files. |
| 4 | Augment: UX guidelines + frontend-design. 4e: đã suy luận UX cho 8 màn. |
| 5 | 9 file .md đã ghi; validation: pass; output_dir: co-op-bank-khcn/co-op-bank-khcn/package-2/danh-sach-yat-lich-chuyen-tien. |

---
*Generated by VNPAY Agentic Framework*
