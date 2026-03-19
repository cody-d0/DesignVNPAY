# 03 — Chi tiết phát hiện

> 8 vấn đề được xác định, sắp xếp theo mức độ ảnh hưởng

---

## UXP-001 · 🔴 Critical

### Trạng thái giao dịch chỉ phân biệt bằng màu chữ, thiếu biểu tượng hỗ trợ

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Trạng thái chỉ dùng màu](ui/calendar.png) |
| **Hiện trạng** | Bốn trạng thái giao dịch (Hoạt động, Đã hủy, Hết hạn, Tạm dừng) chỉ được phân biệt bằng màu chữ mà không có biểu tượng hoặc badge kèm theo. Người dùng có rối loạn nhận biến màu sắc sẽ không phân biệt được. |
| **Tác động** | • Người dùng dalto không phân biệt được Hoạt động (xanh lá) với Tạm dừng (cam) hoặc Đã hủy (đỏ) |
| | • Vi phạm WCAG 2.1 AA — Tiêu chuẩn Sử dụng Màu sắc (1.4.1) |
| | • Rủi ro: thao tác nhầm trên giao dịch đã hủy hoặc hết hạn |
| **Heuristic vi phạm** | **Visibility of System Status** (Nielsen #1) — Trạng thái hệ thống cần hiển thị rõ ràng với nhiều kênh thị giác, không chỉ dựa vào một tín hiệu duy nhất. |
| **Đề xuất cải thiện** | **Thêm biểu tượng trước trạng thái:** |
| | • Hoạt động: biểu tượng ✓ xanh lá + badge nền nhạt |
| | • Tạm dừng: biểu tượng ⏸ cam + badge nền nhạt |
| | • Đã hủy: biểu tượng ✕ đỏ + badge nền nhạt |
| | • Hết hạn: biểu tượng ⏰ xám + badge nền nhạt |
| **Tags** | `Danh sách` · `Accessibility` · `Color Only` |
| **Tham chiếu** | DDL: UXG-180 (Color Only — Don't convey information by color alone) · WCAG 2.1 AA: 1.4.1 Use of Color |

---

## UXP-002 · 🔴 Critical

### Hộp thoại xác nhận tạm dừng thiếu thông tin giao dịch cụ thể

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Xác nhận thiếu context](ui/popup.png) |
| **Hiện trạng** | Hộp thoại "Thông báo" chỉ hỏi "Quý khách có muốn Tạm dừng giao dịch đặt lịch chuyển tiền không?" mà không hiển thị mã đặt lịch, tên người thụ hưởng hay số tiền. Người dùng dễ xác nhận nhầm khi quản lý nhiều giao dịch. |
| **Tác động** | • Xác nhận nhầm → tạm dừng hoặc hủy giao dịch sai |
| | • Giao dịch tài chính → trễ lịch chuyển tiền, ảnh hưởng tài chính |
| | • Đặc thù ngân hàng: hộp thoại xác nhận phải cung cấp đủ ngữ cảnh |
| **Heuristic vi phạm** | **Error Prevention** (Nielsen #5) — Hệ thống cần giúp người dùng tránh sai lầm bằng cách hiển thị đủ thông tin trước hành động không thể hoàn tác. |
| **Đề xuất cải thiện** | **Bổ sung thông tin giao dịch vào hộp thoại:** |
| | • Hiển thị: Tên thụ hưởng + Số tiền + Mã đặt lịch |
| | • Thêm cảnh báo "Hành động này không thể hoàn tác" cho luồng Hủy |
| | • Phân biệt rõ nút Không (viền) và Đồng ý (nền đặc) |
| **Tags** | `Chi tiết` · `Confirmation` · `Error Prevention` |
| **Tham chiếu** | DDL: UXG-35 (Confirmation Dialogs — Confirm before destructive actions) · UX Law: Peak-End Rule — xác nhận là điểm cuối flow, ấn tượng quyết định trải nghiệm tổng thể |

---

## UXP-003 · 🟠 Major

### Màn hình xác thực Soft OTP không ghi rõ hành động đang xác nhận

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ OTP thiếu ngữ cảnh hành động](ui/popup-2.png) |
| **Hiện trạng** | Bottom sheet "Xác thực giao dịch" chỉ hiển thị "Quý khách vui lòng nhập mã PIN của Soft OTP để xác thực giao dịch" mà không nêu rõ đang xác nhận Tạm dừng hay Hủy. |
| **Tác động** | • Nhầm lẫn: người dùng không biết OTP xác nhận hành động nào |
| | • Nếu nhập sai 5 lần → khóa Soft OTP, tổn hại trải nghiệm nghiêm trọng |
| **Heuristic vi phạm** | **Visibility of System Status** (Nielsen #1) — Người dùng phải biết rõ hệ thống đang xử lý gì trước khi xác nhận. |
| **Đề xuất cải thiện** | **Cung cấp ngữ cảnh trong OTP:** |
| | • Tiêu đề: "Xác thực Tạm dừng giao dịch" hoặc "Xác thực Hủy giao dịch" |
| | • Hiển thị mã đặt lịch và số tiền bên dưới tiêu đề |
| **Tags** | `Chi tiết` · `OTP` · `Context` |
| **Tham chiếu** | DDL: UXG-33 (Error Feedback — Clear error messages near problem) · Banking security best practice: OTP context must match action |

---

## UXP-004 · 🟠 Major

### Trạng thái trống thiếu hình minh họa và nút hành động trực tiếp

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Trạng thái trống thiếu hướng dẫn](ui/manage-2.png) |
| **Hiện trạng** | Khi không có giao dịch Hoạt động, màn hình chỉ hiển thị một đoạn văn bản dài centered: "Quý khách không có giao dịch đặt lịch chuyển tiền nào đang Hoạt động. Vui lòng sử dụng bộ lọc...". Không có hình minh họa, không có nút hành động trực tiếp. |
| **Tác động** | • Người dùng không biết phải làm gì tiếp theo (thiếu nút hành động rõ ràng) |
| | • Văn bản dài căn giữa khó đọc trên điện thoại |
| | • Trạng thái trống thiếu hình minh họa → cảm giác lỗi hoặc trống rỗng |
| **Heuristic vi phạm** | **Help & Documentation** (Nielsen #10) — Trạng thái trống cần hướng dẫn rõ ràng cho bước tiếp theo, không chỉ giải thích tại sao trống. |
| **Đề xuất cải thiện** | **Thiết kế trạng thái trống hoàn chỉnh:** |
| | • Thêm hình minh họa lịch hoặc biểu tượng 48×48 pixel |
| | • Rút ngắn văn bản, tách tiêu đề và mô tả |
| | • Thêm nút hành động "Mở bộ lọc" để người dùng thao tác trực tiếp |
| **Tags** | `Quản lý` · `Empty State` · `Onboarding` |
| **Tham chiếu** | DDL: UXG-19 (Content Jumping — Reserve space for content) · Component Spec: empty-state requires icon + title + description + optional CTA |

---

## UXP-005 · 🟠 Major

### Bộ lọc theo thời gian thiếu giá trị mặc định và kiểm tra hợp lệ

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Bộ lọc thiếu giá trị mặc định](ui/filter-2.png) |
| **Hiện trạng** | Chế độ lọc "Theo thời gian" có 2 trường chọn ngày (Từ ngày, Đến ngày) nhưng để trống mặc định. Không có kiểm tra hợp lệ khi Từ ngày lớn hơn Đến ngày. Chú thích giải thích logic truy vấn có cỡ chữ nhỏ, khó đọc. |
| **Tác động** | • Người dùng có thể chọn khoảng thời gian không hợp lệ → lỗi từ máy chủ |
| | • Chú thích nhỏ → người dùng bỏ qua → truy vấn sai kỳ vọng |
| | • Trường ngày trống → không biết bắt đầu từ đâu |
| **Heuristic vi phạm** | **Error Prevention** (Nielsen #5) — Hệ thống cần ngăn ngừa lỗi trước khi xảy ra thông qua giá trị mặc định và kiểm tra đầu vào. |
| **Đề xuất cải thiện** | **Bổ sung giá trị mặc định và kiểm tra:** |
| | • Giá trị mặc định: Từ ngày = 30 ngày trước, Đến ngày = hôm nay |
| | • Kiểm tra inline khi Từ ngày lớn hơn Đến ngày |
| | • Tăng cỡ chữ chú thích hoặc dùng biểu tượng thông tin (i) |
| **Tags** | `Bộ lọc` · `Validation` · `Date Picker` |
| **Tham chiếu** | DDL: UXG-33 (Error Feedback), UXG-43 (Form Labels) · UX Law: Doherty Threshold — phản hồi kiểm tra phải rõ ràng trong 400 mili giây |

---

## UXP-006 · 🟡 Minor

### Biểu tượng lọc trên thanh header có vùng chạm nhỏ hơn chuẩn

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Vùng chạm biểu tượng nhỏ](ui/calendar.png) |
| **Hiện trạng** | Biểu tượng lọc ở góc phải header chỉ 24×24 pixel, vùng chạm có thể nhỏ hơn chuẩn 44×44 pixel tối thiểu cho thiết bị di động. |
| **Tác động** | • Khó chạm trên điện thoại, đặc biệt người dùng lớn tuổi (đối tượng mục tiêu ngân hàng) |
| **Heuristic vi phạm** | **Flexibility & Efficiency of Use** (Nielsen #7) — Vùng chạm cần đủ lớn cho mọi nhóm người dùng. |
| **Đề xuất cải thiện** | **Tăng vùng chạm:** |
| | • Thêm padding cho biểu tượng lọc lên tối thiểu 44×44 pixel (giữ kích thước trực quan 24×24) |
| **Tags** | `Danh sách` · `Touch Target` |
| **Tham chiếu** | DDL: UXG-22 (Touch Target Size — Minimum 44×44px) · UX Law: Fitts's Law — kích thước mục tiêu tỉ lệ thuận với tốc độ thao tác |

---

## UXP-007 · 🟡 Minor

### Hộp thoại thành công không hiển thị thông tin giao dịch đã thay đổi

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Phản hồi thành công thiếu chi tiết](ui/manage.png) |
| **Hiện trạng** | Sau khi hoàn tất xác thực OTP, hộp thoại thành công chỉ hiện "Tạm dừng lệnh chuyển tiền thành công" mà không nêu giao dịch cụ thể nào (mã đặt lịch, tên người thụ hưởng). |
| **Tác động** | • Không xác nhận được đúng giao dịch nào đã bị tạm dừng khi có nhiều giao dịch |
| **Heuristic vi phạm** | **Visibility of System Status** (Nielsen #1) — Phản hồi thành công cần cụ thể, giúp người dùng xác nhận hành động đã thực hiện đúng. |
| **Đề xuất cải thiện** | **Bổ sung thông tin vào phản hồi thành công:** |
| | • Hiển thị: Mã đặt lịch + Tên thụ hưởng + Trạng thái mới |
| | • Duy trì thời gian hiển thị đủ để đọc (tối thiểu 3 giây) |
| **Tags** | `Quản lý` · `Success Feedback` |
| **Tham chiếu** | DDL: UXG-34 (Success Feedback — Confirm successful actions to users) |

---

## UXP-008 · 🟡 Minor

### Danh sách giao dịch đã thực hiện hiển thị dữ liệu không nhất quán giữa các trạng thái

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Dữ liệu lịch sử thiếu nhất quán](ui/list.png) |
| **Hiện trạng** | Các mục "Thành công" hiển thị đầy đủ (ngày, mã giao dịch, phí); trong khi "Không thành công", "Tạm dừng", "Hủy" chỉ hiện ngày và trạng thái — thiếu mã giao dịch và phí. |
| **Tác động** | • Thiếu mã giao dịch khi tra cứu giao dịch thất bại để liên hệ tổng đài |
| **Heuristic vi phạm** | **Consistency & Standards** (Nielsen #4) — Cùng loại dữ liệu phải hiển thị cấu trúc nhất quán bất kể trạng thái. |
| **Đề xuất cải thiện** | **Thống nhất cấu trúc hiển thị:** |
| | • Hiển thị mã giao dịch cho tất cả mục (nếu không có → hiện "—") |
| | • Thống nhất cấu trúc: ngày, trạng thái, mã giao dịch, phí (nếu có) |
| **Tags** | `Chi tiết` · `Consistency` · `Data Display` |
| **Tham chiếu** | DDL: UXG-19 (Content Jumping — Reserve space for content) · Banking UX: transaction references critical for support calls |

---

## Tổng hợp Findings

| ID | Tên vấn đề | Severity | Heuristic |
|---|---|---|---|
| UXP-001 | Trạng thái giao dịch chỉ phân biệt bằng màu chữ, thiếu biểu tượng hỗ trợ | 🔴 Critical | Visibility of System Status |
| UXP-002 | Hộp thoại xác nhận tạm dừng thiếu thông tin giao dịch cụ thể | 🔴 Critical | Error Prevention |
| UXP-003 | Màn hình xác thực Soft OTP không ghi rõ hành động đang xác nhận | 🟠 Major | Visibility of System Status |
| UXP-004 | Trạng thái trống thiếu hình minh họa và nút hành động trực tiếp | 🟠 Major | Help & Documentation |
| UXP-005 | Bộ lọc theo thời gian thiếu giá trị mặc định và kiểm tra hợp lệ | 🟠 Major | Error Prevention |
| UXP-006 | Biểu tượng lọc trên thanh header có vùng chạm nhỏ hơn chuẩn | 🟡 Minor | Flexibility & Efficiency of Use |
| UXP-007 | Hộp thoại thành công không hiển thị thông tin giao dịch đã thay đổi | 🟡 Minor | Visibility of System Status |
| UXP-008 | Danh sách giao dịch đã thực hiện hiển thị dữ liệu không nhất quán giữa các trạng thái | 🟡 Minor | Consistency & Standards |
