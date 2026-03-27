# SCR-THE-004 · Lịch sử GD thẻ › Chi tiết GD

## Screen Identity
- **screen_id**: SCR-THE-004
- **screen_name**: chi-tiet-gd-the
- **screen_type**: detail (transaction_detail)
- **product**: CoopBank Mobile Banking
- **module**: Dịch Vụ Thẻ / Thẻ
- **flow_stage**: detail
- **wireframe_images**: [`ui/lsgd-the-3.png`](ui/lsgd-the-3.png)

---

## Screen Purpose
Màn hình chi tiết một giao dịch thẻ tín dụng cụ thể. Hiển thị thông tin cơ bản về giao dịch đã chọn từ danh sách lịch sử. 

**Quan sát quan trọng**: Màn hình hiện chỉ có 4 trường — ít hơn đáng kể so với tiêu chuẩn ngành banking (thường 8-12 trường).

---

## User Story
> "Là khách hàng thẻ tín dụng, tôi muốn xem chi tiết một giao dịch cụ thể để xác nhận tính hợp lệ và đối soát với hoá đơn thực tế."

---

## Information Architecture

### Header
- **Back navigation**: `←` → quay lại SCR-THE-003
- **Screen title**: "Chi tiết giao dịch"
- **Home navigation**: `home` icon (right) → Home

### Detail Card (Label-Value layout)
| Field | Value Example | Type |
|-------|--------------|------|
| Mã giao dịch | `123123` | Transaction ID |
| Ngày giao dịch | `30/12/2020 10:20` | DateTime |
| Số tiền giao dịch | `2,000,000 VND` | Currency |
| Nội dung giao dịch | `QUET THE` | Description |

---

## Screen States & Variants
- **State duy nhất**: 4 fields hiển thị, không có state variants

---

## Navigation Flows
- `back` → SCR-THE-003 (Danh sách GD)
- `home` → Home screen

---

## UX Analysis: Critical Gaps

### 🔴 Critical Missing Features
Theo tiêu chuẩn ngành (Techcombank, VPBank, ACB, MB Bank), màn hình chi tiết GD thẻ cần:

| Field thiếu | Lý do quan trọng |
|-------------|-----------------|
| **Loại giao dịch** (Mua hàng / ATM / Online) | Phân loại giúp đối soát |
| **Địa điểm / Đơn vị chấp nhận thẻ** | Critical cho dispute |
| **Trạng thái giao dịch** (Thành công / Pending / Từ chối) | User cần biết status |
| **Kênh giao dịch** (POS / Online / Contactless) | Context rõ hơn |
| **Số thẻ thực hiện** (cho multi-card) | Biết GD từ thẻ nào |
| **Điểm thưởng tích lũy** | Loyalty program hook |
| **Nút "Khiếu nại GD"** | Required by banking regulation |
| **Nút "Chia sẻ" / "Tải biên lai"** | Common banking UX |

### 🟡 Usability Issues
- **"QUET THE"**: Nội dung GD toàn chữ hoa viết tắt — user khó hiểu (nên là "Quẹt thẻ tại POS" hoặc merchant name)
- **Mã GD "123123"**: Placeholder data — không rõ định dạng thực tế dài bao nhiêu ký tự
- **Không có color coding**: Số tiền không phân biệt màu đỏ/xanh theo credit/debit
- **Page quá trống**: ~80% màn hình trắng — thiết kế chưa hoàn thiện
