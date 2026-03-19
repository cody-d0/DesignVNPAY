# 03 — Chi tiết phát hiện

> 7 vấn đề được xác định, sắp xếp theo mức độ ảnh hưởng

---

## UXP-001 · 🔴 Critical

### Form nhập thiếu trạng thái hiển thị lỗi cho các trường dữ liệu

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu trạng thái lỗi](ui/internal-transaction.png) |
| **Hiện trạng** | Tất cả 4 trạng thái của form nhập (cơ bản, popup cảnh báo, đặt lịch hàng tháng, đặt lịch không lặp lại) đều không có artboard nào thể hiện trạng thái validation error inline cho các trường nhập liệu. |
| **Tác động** | • Người dùng nhập sai số tiền (vượt số dư, ký tự không hợp lệ) nhưng không biết lỗi ở đâu |
| | • Tăng tỷ lệ giao dịch thất bại và chi phí hỗ trợ khách hàng |
| **Heuristic vi phạm** | **Help users recognize, diagnose, and recover from errors** (Nielsen #9) — Hệ thống phải hiển thị thông báo lỗi rõ ràng, gần vị trí gây lỗi, với ngôn ngữ dễ hiểu. |
| **Đề xuất cải thiện** | **Thêm trạng thái lỗi cho tất cả trường nhập:** |
| | • Thêm artboard error state: viền đỏ, helper text "Số tiền vượt quá số dư khả dụng" |
| | • Thêm error state cho trường "Tài khoản thụ hưởng": "Vui lòng chọn tài khoản" |
| | • Nút "Tiếp tục" ở trạng thái vô hiệu khi form chưa hợp lệ (opacity 0.5) |
| **Tags** | `Form nhập` · `Validation` · `Error State` |
| **Tham chiếu** | DDL: UXG-10 (Error Message Visibility), UXG-78 (Form Input Affordance) · Component: text-input-1 → state.error + errorBorderColor: {base.destructive} (#dc2626) · UX Law: Fitts's Law |

---

## UXP-002 · 🔴 Critical

### Thiếu bước xác thực bảo mật (OTP/PIN) trước khi thực hiện giao dịch

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu xác thực bảo mật](ui/internal-transaction-5.png) |
| **Hiện trạng** | Màn xác nhận chỉ hiển thị thông tin giao dịch và nút "Xác nhận". Không có bước xác thực 2 yếu tố (OTP hoặc PIN) — giao dịch tài chính được thực hiện chỉ bằng một nút nhấn. |
| **Tác động** | • Rủi ro bảo mật nghiêm trọng: nếu thiết bị bị đánh cắp, kẻ gian có thể chuyển tiền mà không cần xác thực |
| | • Vi phạm nguyên tắc "Security-first" của ứng dụng ngân hàng |
| **Heuristic vi phạm** | **Error Prevention** (Nielsen #5) — Thiết kế phải ngăn ngừa các vấn đề nghiêm trọng, đặc biệt giao dịch tài chính không thể hoàn tác, bằng cách yêu cầu xác nhận bổ sung. |
| **Đề xuất cải thiện** | **Thêm bottom sheet OTP sau khi nhấn "Xác nhận":** |
| | • OTP 6 ô (kích thước 48 pixel), tự động chuyển focus, hỗ trợ dán |
| | • Bộ đếm gửi lại mã sau 60 giây |
| | • Nút đóng ở góc phải trên |
| **Tags** | `Xác nhận` · `Bảo mật` · `OTP` |
| **Tham chiếu** | DDL: UXG-45 (Transaction Verification) · Component: otp-input-1 → 6-digit, auto-focus, resend timer 60s · UX Law: Doherty Threshold |

---

## UXP-003 · 🟠 Major

### Lỗi chính tả trên màn hình xác nhận giao dịch tài chính

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Lỗi chính tả](ui/internal-transaction-5.png) |
| **Hiện trạng** | Dòng hướng dẫn viết "Qúy khách" thay vì "Quý khách" — dấu sắc đặt sai vị trí. Đây là lỗi ngữ pháp tiếng Việt trên màn hình quan trọng nhất (xác nhận chuyển tiền). |
| **Tác động** | • Giảm niềm tin vào ứng dụng ngân hàng — nếu viết sai chính tả trên màn xác nhận, người dùng nghi ngờ tính chuyên nghiệp |
| | • Đặc biệt nhạy cảm với ứng dụng tài chính do yêu cầu uy tín cao |
| **Heuristic vi phạm** | **Aesthetic and minimalist design** (Nielsen #8) — Nội dung phải chính xác, ngắn gọn, không chứa lỗi gây nhiễu. |
| **Đề xuất cải thiện** | **Sửa chính tả:** |
| | • Sửa "Qúy khách" → "Quý khách vui lòng kiểm tra lại thông tin đặt lịch đã khởi tạo" |
| **Tags** | `Xác nhận` · `Nội dung` · `Chính tả` |
| **Tham chiếu** | DDL: UXG-165 (Content Quality) |

---

## UXP-004 · 🟠 Major

### Thiếu trạng thái loading khi nhấn nút "Tiếp tục"

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu phản hồi xử lý](ui/internal-transaction.png) |
| **Hiện trạng** | Nút "Tiếp tục" chỉ có trạng thái mặc định — không có trạng thái loading (spinner + vô hiệu hóa) khi hệ thống đang xử lý giao dịch. |
| **Tác động** | • Người dùng nhấn nhiều lần vì không biết ứng dụng đang xử lý hay bị treo |
| | • Nguy cơ tạo giao dịch trùng lặp (double-charge) |
| **Heuristic vi phạm** | **Visibility of system status** (Nielsen #1) — Hệ thống phải luôn thông báo cho người dùng biết đang xảy ra gì, qua phản hồi kịp thời. |
| **Đề xuất cải thiện** | **Thêm trạng thái loading cho nút hành động:** |
| | • Spinner + vô hiệu hóa + text "Đang xử lý..." khi nhấn "Tiếp tục" |
| | • Loading overlay toàn màn hình khi gửi yêu cầu |
| **Tags** | `Form nhập` · `Loading State` |
| **Tham chiếu** | DDL: UXG-12 (Loading Feedback) · UX Law: Hick's Law, Doherty Threshold (phản hồi < 400ms hoặc hiển thị loading) |

---

## UXP-005 · 🟠 Major

### Dữ liệu mẫu không nhất quán giữa các màn hình trong flow

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Dữ liệu không nhất quán](ui/internal-transaction-6.png) |
| **Hiện trạng** | Số tài khoản nguồn hiển thị khác nhau trên 3 màn hình: form nhập, xác nhận, và kết quả — mỗi màn dùng một số tài khoản mẫu khác nhau hoàn toàn. |
| **Tác động** | • Trong prototype review, stakeholder nghi ngờ chất lượng thiết kế |
| | • Nếu xảy ra trong thực tế, người dùng hoảng loạn vì nghĩ tiền chuyển sai tài khoản |
| **Heuristic vi phạm** | **Consistency and standards** (Nielsen #4) — Dữ liệu phải nhất quán xuyên suốt flow. Người dùng không nên tự hỏi liệu các giá trị khác nhau có cùng ý nghĩa không. |
| **Đề xuất cải thiện** | **Đồng nhất dữ liệu mẫu xuyên suốt flow:** |
| | • Sử dụng cùng một bộ số tài khoản mẫu cho cả 3 màn hình |
| | • Tài khoản nguồn, tài khoản thụ hưởng, số tiền phải giống nhau từ form → xác nhận → kết quả |
| **Tags** | `Cross-Screen` · `Data Consistency` |
| **Tham chiếu** | DDL: UXG-243 (Data Consistency) · UX Law: Peak-End Rule — kết quả là ấn tượng cuối cùng |

---

## UXP-006 · 🟡 Minor

### Nội dung giao dịch mặc định không có dấu tiếng Việt

| | |
|---|---|
| **Ảnh minh họa** | ![ℹ️ Nội dung thiếu dấu](ui/internal-transaction.png) |
| **Hiện trạng** | Trường "Nội dung giao dịch" hiển thị text mặc định viết hoa toàn bộ, không có dấu: "NGUYEN HOANG KHAI chuyen tien". |
| **Tác động** | • Gây ấn tượng ứng dụng không hỗ trợ tiếng Việt có dấu, dù đây chỉ là giá trị mặc định |
| **Heuristic vi phạm** | **Match between system and the real world** (Nielsen #2) — Hệ thống nên sử dụng ngôn ngữ mà người dùng quen thuộc, bao gồm tiếng Việt có dấu. |
| **Đề xuất cải thiện** | **Cập nhật giá trị mặc định:** |
| | • Đổi thành "NGUYEN HOANG KHAI chuyển tiền" hoặc cho phép nhập Unicode |
| **Tags** | `Form nhập` · `Nội dung` |
| **Tham chiếu** | DDL: UXG-78 (Localization Quality) |

---

## UXP-007 · 🟡 Minor

### Biên lai giao dịch thiếu đường phân cách giữa các nhóm thông tin

| | |
|---|---|
| **Ảnh minh họa** | ![ℹ️ Thiếu phân nhóm](ui/internal-transaction-6.png) |
| **Hiện trạng** | Biên lai hiển thị 10 dòng thông tin liên tục, không có đường phân cách giữa các nhóm (thông tin tài khoản, thông tin lịch trình, thông tin tham chiếu). |
| **Tác động** | • Quét thông tin biên lai chậm hơn — phải đọc tuần tự thay vì quét nhanh theo nhóm |
| **Heuristic vi phạm** | **Aesthetic and minimalist design** (Nielsen #8) — Nội dung cần được nhóm và phân cách rõ ràng để hỗ trợ quét nhanh. |
| **Đề xuất cải thiện** | **Thêm đường phân cách giữa các nhóm:** |
| | • Đường phân cách giữa nhóm "Số tiền" và "Tần suất" (tài chính và lịch trình) |
| | • Đường phân cách trước "Mã đặt lịch" (thông tin tham chiếu) |
| **Tags** | `Kết quả` · `Visual Hierarchy` |
| **Tham chiếu** | DDL: UXG-12 (Visual Hierarchy) · Component: receipt-preview-1 → layout.children includes Separator |

---

## Tổng hợp Findings

| ID | Tên vấn đề | Severity | Heuristic |
|---|---|---|---|
| UXP-001 | Form nhập thiếu trạng thái hiển thị lỗi cho các trường dữ liệu | 🔴 Critical | Help users recognize, diagnose, and recover from errors |
| UXP-002 | Thiếu bước xác thực bảo mật (OTP/PIN) trước khi thực hiện giao dịch | 🔴 Critical | Error Prevention |
| UXP-003 | Lỗi chính tả trên màn hình xác nhận giao dịch tài chính | 🟠 Major | Aesthetic and minimalist design |
| UXP-004 | Thiếu trạng thái loading khi nhấn nút "Tiếp tục" | 🟠 Major | Visibility of system status |
| UXP-005 | Dữ liệu mẫu không nhất quán giữa các màn hình trong flow | 🟠 Major | Consistency and standards |
| UXP-006 | Nội dung giao dịch mặc định không có dấu tiếng Việt | 🟡 Minor | Match between system and the real world |
| UXP-007 | Biên lai giao dịch thiếu đường phân cách giữa các nhóm thông tin | 🟡 Minor | Aesthetic and minimalist design |
