# Trạng thái trống — PRD (Trạng thái trống)

Màn hình hiển thị khi danh sách đặt lịch chuyển tiền không có dữ liệu: không có giao dịch đang hoạt động hoặc không tìm thấy kết quả tìm kiếm.

---

## Mục lục
1. [User Flow](#1-user-flow)
2. [User Story](#2-user-story)
3. [Wireframe](#3-wireframe)
4. [Thiết kế Database](#4-thiết-kế-database)
5. [Non-functional requirement](#5-non-functional-requirement)

---

## 1. User Flow

### 1.1. Luồng hiển thị trạng thái trống — không có giao dịch hoạt động
| Bước | Tên màn hình | Tên hành động | Kết quả |
|:---:|---|---|---|
| 1 | Danh sách đặt lịch chuyển tiền | Mở màn hình | Hệ thống gọi API lấy danh sách lệnh đặt lịch theo trạng thái mặc định "Hoạt động". |
| 2 | Danh sách đặt lịch chuyển tiền | API trả về danh sách rỗng | Hiển thị trạng thái trống: thông báo "Quý khách không có giao dịch đặt lịch chuyển tiền nào đang Hoạt động. Vui lòng sử dụng bộ lọc để truy vấn các giao dịch đặt lịch chuyển tiền có trạng thái khác." |
| 3 | Danh sách đặt lịch chuyển tiền | Chạm icon bộ lọc (header) | Mở màn hình Bộ lọc tìm kiếm để thay đổi trạng thái hoặc khoảng thời gian. |
| 4 | Danh sách đặt lịch chuyển tiền | Chạm mũi tên back (header) | Quay lại màn hình trước. |

### 1.2. Luồng hiển thị trạng thái trống — không có kết quả tìm kiếm
| Bước | Tên màn hình | Tên hành động | Kết quả |
|:---:|---|---|---|
| 1 | Bộ lọc tìm kiếm | Áp dụng bộ lọc | Hệ thống gọi API với điều kiện lọc (trạng thái, khoảng thời gian). |
| 2 | Danh sách đặt lịch chuyển tiền | API trả về danh sách rỗng | Hiển thị trạng thái trống: thông báo "Không có kết quả tìm kiếm". |
| 3 | Danh sách đặt lịch chuyển tiền | Chạm icon bộ lọc (header) | Mở lại Bộ lọc tìm kiếm để thay đổi điều kiện. |
| 4 | Danh sách đặt lịch chuyển tiền | Chạm mũi tên back (header) | Quay lại màn hình trước. |

---

## 2. User Story

| Epic chung | Mã US | Tiêu đề | Mô tả chi tiết | Business Rule | Acceptance Criteria |
|---|---|---|---|---|---|
| Đặt lịch chuyển tiền | US-371 | Hiển thị trạng thái trống khi không có giao dịch hoạt động | Là người dùng, tôi muốn thấy thông báo rõ ràng khi không có lệnh đặt lịch nào đang hoạt động, để biết cần sử dụng bộ lọc xem trạng thái khác. | Khi API trả về danh sách rỗng với trạng thái mặc định "Hoạt động", hiển thị empty-state variant "no active schedules". Thông báo gợi ý sử dụng bộ lọc. | - Hiển thị thông báo: "Quý khách không có giao dịch đặt lịch chuyển tiền nào đang Hoạt động. Vui lòng sử dụng bộ lọc để truy vấn các giao dịch đặt lịch chuyển tiền có trạng thái khác."<br>- Header vẫn hiển thị đầy đủ: mũi tên back, tiêu đề, icon bộ lọc.<br>- Icon bộ lọc có thể chạm để mở Bộ lọc tìm kiếm.<br>- Không hiển thị loading indicator sau khi đã nhận response rỗng. |
| Đặt lịch chuyển tiền | US-372 | Hiển thị trạng thái trống khi không có kết quả tìm kiếm | Là người dùng, tôi muốn thấy thông báo khi bộ lọc không tìm thấy kết quả nào, để biết cần thay đổi điều kiện lọc. | Khi API trả về danh sách rỗng sau khi áp dụng bộ lọc (trạng thái lệnh hoặc khoảng thời gian), hiển thị empty-state variant "no search results". | - Hiển thị thông báo: "Không có kết quả tìm kiếm".<br>- Header vẫn hiển thị đầy đủ: mũi tên back, tiêu đề, icon bộ lọc.<br>- Icon bộ lọc có thể chạm để thay đổi điều kiện lọc.<br>- Thông báo ngắn gọn, không chứa gợi ý bổ sung. |
| Đặt lịch chuyển tiền | US-373 | Quay lại từ màn hình trạng thái trống | Là người dùng, tôi muốn quay lại màn hình trước khi đang ở trạng thái trống. | Chạm mũi tên back trên header. Hệ thống quay lại màn hình trước đó (stack navigation). | - Chạm back quay lại màn hình trước.<br>- Không mất data hoặc trạng thái của màn hình trước. |

> **`🤖 by AI`** | Nguồn: figma_inferred:kPft93N2A3gYOC3YwuXpQR/5199:5931 | Độ tin cậy: High
>
> US-371, US-372 suy luận từ OCR hai biến thể empty-state trên manage-2.png và manage-3.png. Nội dung thông báo trích nguyên văn từ thiết kế. US-373 suy luận từ icon back trên header.

---

## 3. Wireframe

### Hình ảnh minh họa
![Trạng thái trống — không có giao dịch hoạt động](ui/manage-2.png)
![Trạng thái trống — không có kết quả tìm kiếm](ui/manage-3.png)

---

### Mô tả màn hình
| STT | Tên màn hình | Loại thành phần | Mô tả |
|:---:|---|---|---|
| 1 | Header | Header | Thanh trên: mũi tên back (chevron trái), tiêu đề "Danh sách đặt lịch chuyển tiền", icon bộ lọc (góc phải). |
| 2 | Icon Back | Icon Button | Mũi tên trái trên header, chạm để quay lại màn hình trước. Touch target ≥ 44px. |
| 3 | Icon Bộ lọc | Icon Button | Icon filter trên header, chạm để mở màn hình Bộ lọc tìm kiếm. Touch target ≥ 44px. |
| 4 | Empty State — Không có giao dịch hoạt động | Empty State | Vùng nội dung trống, hiển thị thông báo dài: "Quý khách không có giao dịch đặt lịch chuyển tiền nào đang Hoạt động. Vui lòng sử dụng bộ lọc để truy vấn các giao dịch đặt lịch chuyển tiền có trạng thái khác." Căn giữa theo chiều ngang, đặt ở vùng trung tâm màn hình. |
| 5 | Empty State — Không có kết quả tìm kiếm | Empty State | Vùng nội dung trống, hiển thị thông báo ngắn: "Không có kết quả tìm kiếm". Căn giữa theo chiều ngang, đặt ở vùng trung tâm màn hình. |
| 6 | Helper Text | Text | Văn bản mô tả / gợi ý sử dụng bộ lọc, phong cách body text, màu neutral/gray. |

> **`🤖 by AI`** | Nguồn: figma_inferred:kPft93N2A3gYOC3YwuXpQR/5199:5931 | Độ tin cậy: High
>
> Hai biến thể empty-state được xác định từ OCR manage-2.png (no active schedules) và manage-3.png (no search results). Cấu trúc header nhất quán với các màn hình khác trong luồng.

---

### Ngữ cảnh màn hình (từ OCR)

**manage-2.png:** Header "Danh sách đặt lịch chuyển tiền" với mũi tên back và icon bộ lọc. Vùng nội dung trống, hiển thị thông báo: "Quý khách không có giao dịch đặt lịch chuyển tiền nào đang Hoạt động. Vui lòng sử dụng bộ lọc để truy vấn các giao dịch đặt lịch chuyển tiền có trạng thái khác."

**manage-3.png:** Cùng header. Vùng nội dung trống, hiển thị thông báo ngắn: "Không có kết quả tìm kiếm".

---

## 4. Thiết kế Database

> **`🤖 by AI`** | Nguồn: figma_inferred:kPft93N2A3gYOC3YwuXpQR/5199:5931 | Độ tin cậy: Medium
>
> Màn hình trạng thái trống không yêu cầu entity riêng. Trạng thái trống được xác định bởi kết quả truy vấn từ entity chính (ScheduledTransfer). Dưới đây liệt kê các field liên quan đến logic hiển thị empty-state.

### Entity liên quan: ScheduledTransfer (Lệnh đặt lịch chuyển tiền)
| Field | Data Type | Constraint | Description |
|---|---|---|---|
| `id` | UUID | Primary Key | Mã lệnh đặt lịch |
| `user_id` | UUID | Foreign Key | Liên kết tài khoản người dùng |
| `status` | Enum | Not Null | Trạng thái lệnh: ACTIVE \| PAUSED \| CANCELLED \| EXPIRED \| COMPLETED |
| `created_at` | DateTime | Not Null | Thời gian tạo lệnh |
| `updated_at` | DateTime | Not Null | Thời gian cập nhật lệnh |

### Logic hiển thị Empty State
| Điều kiện | Variant hiển thị |
|---|---|
| `SELECT ... WHERE user_id = ? AND status = 'ACTIVE'` trả về 0 bản ghi | Empty State — Không có giao dịch hoạt động |
| `SELECT ... WHERE user_id = ? AND [filter_conditions]` trả về 0 bản ghi | Empty State — Không có kết quả tìm kiếm |

---

## 5. Non-functional requirement

- **Hiệu năng:**
    - Thời gian phản hồi API ≤ 2 giây cho truy vấn danh sách rỗng.
    - Chuyển đổi từ loading sang empty-state mượt mà, không nhấp nháy.
- **Trải nghiệm:**
    - Touch target tối thiểu 44px cho mũi tên back và icon bộ lọc.
    - Thông báo empty-state căn giữa màn hình, dễ đọc trên các kích thước màn hình khác nhau.
    - Phông chữ và màu sắc thông báo nhất quán với design system (body text, màu neutral/gray).
- **Khả năng tiếp cận (Accessibility):**
    - Thông báo empty-state có thể đọc bởi screen reader.
    - Icon bộ lọc và back có label mô tả (aria-label hoặc tương đương trên mobile).

> **`🤖 by AI`** | Nguồn: UX guidelines, WCAG 2.1 | Độ tin cậy: Medium
>
> Các yêu cầu accessibility và touch target suy luận từ best practice mobile banking. Cần BA/QA xác nhận SLA thời gian phản hồi.

---
*Generated by VNPAY Agentic Framework*
