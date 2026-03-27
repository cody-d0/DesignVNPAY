# SCR-THE-002 · Thông tin thẻ › Chi tiết thẻ

## Screen Identity
- **screen_id**: SCR-THE-002
- **screen_name**: thong-tin-the
- **screen_type**: detail (card_detail)
- **product**: CoopBank Mobile Banking
- **module**: Dịch Vụ Thẻ / Thẻ
- **flow_stage**: detail
- **wireframe_images**: [`ui/danh-sach-the-thong-tin-the.png`](ui/danh-sach-the-thong-tin-the.png)

---

## Screen Purpose
Màn hình hiển thị chi tiết thông tin tài khoản thẻ tín dụng và trạng thái dư nợ. Screen này là informational — không có CTA chính. Phục vụ nhu cầu tra cứu của khách hàng về hạn mức, dư nợ, và ngày đến hạn thanh toán.

---

## User Story
> "Là khách hàng thẻ tín dụng, tôi muốn xem đầy đủ thông tin tài khoản thẻ và tình trạng dư nợ để quản lý tài chính hiệu quả."

---

## Information Architecture

### Header
- **Back navigation**: `←` arrow → quay lại SCR-THE-001
- **Screen title**: "Thông tin thẻ"

### Section 1: Thông tin thẻ
| Field | Value Example |
|-------|--------------|
| Số tài khoản thẻ | `0319384918` |
| Sản phẩm thẻ | `Thẻ tín dụng nội địa` |
| Đơn vị quản lý | `Chi nhánh Ba Đình` |

### Section 2: Thông tin dư nợ (`ic_money_tit` icon)
| Field | Value Example | Note |
|-------|--------------|------|
| Hạn mức khả dụng tín dụng | `80,000,000 VND` | Max credit limit |
| Hạn mức khả dụng còn lại hiện tại | `78,000,000 VND` | Remaining available |
| Dư nợ hiện tại | `1,500,000 VND` | Current outstanding debt |
| Dư nợ tại kỳ sao kê gần nhất | `1,200,000 VND` | Last statement balance |
| Số tiền thanh toán tối thiểu trên sao kê | `150,000 VND` | Minimum payment due |
| Số tiền phải trả còn lại trên sao kê | `50,000 VND` | Remaining from min payment |
| Ngày đến hạn thanh toán | `29/12/2025` | Payment deadline |
| Ngày sao kê gần nhất | `29/12/2025` | Last statement date |

---

## Screen States & Variants
- **State duy nhất** (cho thẻ chính, hoạt động): Hiển thị đầy đủ 2 sections

---

## Navigation Flows
- `back` → SCR-THE-001 (Danh sách thẻ)

---

## Missing Data / Gaps
- ⚠️ **Không có CTA**: Màn hình này chỉ hiển thị thông tin, không có nút Thanh toán nhanh hay Đặt lịch thanh toán → Missed opportunity để cross-sell
- ⚠️ **Thiếu trực quan hóa**: Hạn mức sử dụng (1.5M / 80M = 1.87%) có thể hiển thị bằng progress bar
- ⚠️ **Thiếu cảnh báo ngày đến hạn**: Ngày 29/12/2025 gần không có highlight/warning nếu gần hạn
- ⚠️ **Không có lịch sử sao kê**: Chỉ hiện kỳ gần nhất, không có xem sao kê trước
- ⚠️ **Không có nút "Thanh toán ngay"**: Bỏ lỡ conversion opportunity khi user đang xem thông tin dư nợ
