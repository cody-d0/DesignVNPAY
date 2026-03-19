# 03 — Chi tiết phát hiện

> 7 vấn đề được xác định, sắp xếp theo mức độ ảnh hưởng

---

## UXP-001 · 🔴 Critical

### Overlay xác thực OTP thiếu hoàn toàn nút gửi lại mã và bộ đếm thời gian hết hạn

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu nút gửi lại OTP](ui/chuyen-tien-nhanh-247-qua-the-5.png) |
| **Hiện trạng** | Overlay OTP hiển thị 6 ô nhập mã nhưng thiếu: nút "Gửi lại mã OTP" với đếm ngược, thông báo thời gian hết hạn, và trạng thái loading khi xác thực. Người dùng không nhận được mã sẽ bị kẹt. |
| **Tác động** | • Nếu mã OTP không đến hoặc hết hạn, người dùng bị kẹt — phải thoát và làm lại toàn bộ luồng chuyển tiền |
| | • Tỷ lệ bỏ dở giao dịch tăng cao tại bước cuối cùng |
| **Heuristic vi phạm** | **Help Users Recognize, Diagnose, and Recover from Errors** (Nielsen #9) — Hệ thống phải hỗ trợ người dùng khi gặp vấn đề, ví dụ OTP không nhận được. |
| **Đề xuất cải thiện** | **Thêm cơ chế gửi lại mã OTP:** |
| | • Text link "Gửi lại mã OTP" với đếm ngược "Gửi lại sau 60 giây" |
| | • Hiển thị "Mã hết hạn sau: 02:00" dưới dòng hướng dẫn |
| | • Spinner + "Đang xác thực..." khi nhấn nút xác nhận |
| **Tags** | `Xác thực` · `OTP` · `Error Recovery` |
| **Tham chiếu** | DDL: COMP:otp-input-1 — states: canResend, timeLeft (required) · UX Law: Doherty Threshold — response feedback absent · UXG-235: Action availability |

---

## UXP-002 · 🔴 Critical

### Form nhập thông tin chuyển tiền thiếu hoàn toàn trạng thái lỗi và validation feedback

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu error state](ui/chuyen-tien-nhanh-247-qua-the.png) |
| **Hiện trạng** | Tất cả ô nhập liệu (số thẻ, số tiền, nội dung) chỉ có 2 trạng thái: trống và đã điền. Không có variant lỗi: viền đỏ, biểu tượng cảnh báo, hay dòng gợi ý sửa lỗi. |
| **Tác động** | • Nhập sai số thẻ 16 chữ số — không biết lỗi ở đâu, phải đoán |
| | • Tăng tỷ lệ giao dịch thất bại, tăng cuộc gọi hỗ trợ |
| **Heuristic vi phạm** | **Error Prevention** (Nielsen #5) — Thiết kế nên ngăn lỗi xảy ra trước khi người dùng gửi form. |
| **Đề xuất cải thiện** | **Thêm inline validation đầy đủ:** |
| | • Viền đỏ + biểu tượng cảnh báo + dòng gợi ý lỗi dưới mỗi ô nhập |
| | • Kiểm tra thời gian thực: số thẻ 16 chữ số, số tiền lớn hơn 0 |
| | • Banner tổng hợp lỗi khi nhấn "Tiếp tục" mà còn lỗi |
| **Tags** | `Form nhập` · `Validation` · `Error State` |
| **Tham chiếu** | DDL: COMP:text-input-1 — states: error, errorMessage (required) · UXG-180: Form validation feedback · Nielsen #5: Error Prevention |

---

## UXP-003 · 🟠 Major

### Hai variant xác nhận giao dịch hiển thị thông tin và nhãn không nhất quán

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Label không nhất quán](ui/chuyen-tien-nhanh-247-qua-the-4.png) |
| **Hiện trạng** | Variant 1 dùng "Số thẻ thụ hưởng" trong khi variant 2 dùng "Số tài khoản thụ hưởng" kèm thêm "Số điện thoại". Nhãn và dữ liệu khác nhau giữa 2 biến thể gây nhầm lẫn. |
| **Tác động** | • Người dùng không chắc chắn đang xác nhận chuyển tiền qua thẻ hay qua tài khoản |
| | • Giao dịch sai lầm dẫn đến tranh chấp và chi phí hoàn tiền |
| **Heuristic vi phạm** | **Consistency & Standards** (Nielsen #4) — Cùng một khái niệm phải dùng cùng từ ngữ xuyên suốt ứng dụng. |
| **Đề xuất cải thiện** | **Phân biệt rõ loại chuyển tiền:** |
| | • Thêm phụ đề: "Chuyển tiền qua thẻ" hoặc "Chuyển tiền qua số điện thoại" dưới tiêu đề |
| | • Giữ nhãn "Số thẻ thụ hưởng" nhất quán cho luồng qua thẻ |
| **Tags** | `Xác nhận` · `Consistency` · `Label` |
| **Tham chiếu** | DDL: UXG-183 — Confirmation screen consistency · Nielsen #4: Consistency and Standards |

---

## UXP-004 · 🟠 Major

### Biên nhận giao dịch hiển thị mã giao dịch ngắn và định dạng thời gian thiếu múi giờ

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Mã giao dịch thiếu chuẩn](ui/chuyen-tien-nhanh-247-qua-the-6.png) |
| **Hiện trạng** | Mã giao dịch "0982312" chỉ có 7 ký tự, thiếu tiền tố ngân hàng. Thời gian "22:00 15/02/2020" không ghi múi giờ, gây khó khăn khi tra soát. |
| **Tác động** | • Khó tra cứu giao dịch sau này — mã ngắn dễ trùng lặp |
| | • Tăng thời gian xử lý khi liên hệ hỗ trợ tra soát |
| **Heuristic vi phạm** | **Recognition Rather Than Recall** (Nielsen #6) — Thông tin quan trọng phải đầy đủ và rõ ràng để người dùng không cần nhớ thêm. |
| **Đề xuất cải thiện** | **Chuẩn hóa thông tin biên nhận:** |
| | • Mã giao dịch chuẩn: "COOP-20200215-0982312" (tiền tố + ngày + mã) |
| | • Thời gian: "22:00 — 15/02/2020 (GMT+7)" |
| **Tags** | `Kết quả` · `Biên nhận` · `Data Format` |
| **Tham chiếu** | DDL: COMP:receipt-preview-1 — transaction code + timestamp format · UX Law: Peak-End Rule — kết thúc flow nên tạo ấn tượng tích cực |

---

## UXP-005 · 🟠 Major

### Overlay danh bạ thụ hưởng thiếu trạng thái khi không tìm thấy kết quả

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu empty state](ui/chuyen-tien-nhanh-247-qua-the-2.png) |
| **Hiện trạng** | Danh bạ hiển thị danh sách dài nhưng không có trạng thái trống khi tìm kiếm không có kết quả. Mục cuối bị cắt nửa chữ, không có chỉ báo cuộn thêm. |
| **Tác động** | • Tìm kiếm không ra kết quả — người dùng không biết phải làm gì tiếp |
| | • Bỏ cuộc, không hoàn thành chuyển tiền |
| **Heuristic vi phạm** | **Help & Documentation** (Nielsen #10) — Hệ thống phải hướng dẫn bước tiếp theo khi không tìm thấy kết quả. |
| **Đề xuất cải thiện** | **Thêm trạng thái trống và chỉ báo cuộn:** |
| | • "Không tìm thấy người hưởng. Bạn có thể nhập trực tiếp số thẻ." + nút "Nhập thủ công" |
| | • Hiệu ứng mờ dần ở cuối danh sách khi còn mục chưa hiển thị |
| **Tags** | `Form nhập` · `Empty State` · `Search` |
| **Tham chiếu** | DDL: COMP:empty-state-1, UXG-184 — empty state guidance · UX Law: Hick's Law — danh sách dài thiếu navigation rõ ràng |

---

## UXP-006 · 🟡 Minor

### Nội dung giao dịch mặc định hiển thị kiểu chữ không nhất quán giữa các biến thể

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Kiểu chữ không nhất quán](ui/chuyen-tien-nhanh-247-qua-the-3.png) |
| **Hiện trạng** | Variant 1 hiển thị nội dung mặc định toàn chữ hoa không dấu, trong khi variant 3 lại dùng chữ thường có dấu — thiếu nhất quán về phong cách trình bày. |
| **Tác động** | • Giảm cảm giác premium và chuyên nghiệp của ứng dụng ngân hàng |
| **Heuristic vi phạm** | **Consistency & Standards** (Nielsen #4) — Kiểu trình bày văn bản phải đồng nhất trong cùng luồng. |
| **Đề xuất cải thiện** | **Thống nhất kiểu chữ:** |
| | • Tự động tạo nội dung mặc định: "{Tên} chuyển tiền" với chữ thường có dấu |
| **Tags** | `Form nhập` · `Text Style` · `Consistency` |
| **Tham chiếu** | DDL: UXG-181 — text formatting consistency · Nielsen #4: Consistency and Standards |

---

## UXP-007 · 🟡 Minor

### Tên người thụ hưởng hiển thị kiểu chữ khác nhau giữa xác nhận và biên nhận

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Tên viết hoa/thường khác nhau](ui/chuyen-tien-nhanh-247-qua-the-6.png) |
| **Hiện trạng** | Màn xác nhận hiển thị "NGUYEN TUNG" (chữ hoa) nhưng biên nhận hiển thị "nguyen tung" (chữ thường). Tên ngân hàng dài bị xuống 3 dòng trên thẻ biên nhận. |
| **Tác động** | • Thiếu tự tin về tính chính xác khi thông tin hiển thị khác nhau giữa 2 màn hình liền kề |
| **Heuristic vi phạm** | **Consistency & Standards** (Nielsen #4) — Cùng một dữ liệu phải hiển thị nhất quán. |
| **Đề xuất cải thiện** | **Đồng nhất kiểu chữ tên:** |
| | • Luôn hiển thị tên chữ hoa cả trên biên nhận lẫn xác nhận |
| | • Viết tắt tên ngân hàng trên biên nhận: "BIDV" (đã rõ từ màn xác nhận) |
| **Tags** | `Kết quả` · `Biên nhận` · `Name Casing` |
| **Tham chiếu** | DDL: COMP:receipt-preview-1, UXG-181 · UX Law: Peak-End Rule — biên nhận nên tạo ấn tượng tích cực |

---

## Tổng hợp Findings

| ID | Tên vấn đề | Severity | Heuristic |
|---|---|---|---|
| UXP-001 | Overlay xác thực OTP thiếu hoàn toàn nút gửi lại mã và bộ đếm thời gian hết hạn | 🔴 Critical | Help Users Recognize, Diagnose, and Recover from Errors |
| UXP-002 | Form nhập thông tin chuyển tiền thiếu hoàn toàn trạng thái lỗi và validation feedback | 🔴 Critical | Error Prevention |
| UXP-003 | Hai variant xác nhận giao dịch hiển thị thông tin và nhãn không nhất quán | 🟠 Major | Consistency & Standards |
| UXP-004 | Biên nhận giao dịch hiển thị mã giao dịch ngắn và định dạng thời gian thiếu múi giờ | 🟠 Major | Recognition Rather Than Recall |
| UXP-005 | Overlay danh bạ thụ hưởng thiếu trạng thái khi không tìm thấy kết quả | 🟠 Major | Help & Documentation |
| UXP-006 | Nội dung giao dịch mặc định hiển thị kiểu chữ không nhất quán giữa các biến thể | 🟡 Minor | Consistency & Standards |
| UXP-007 | Tên người thụ hưởng hiển thị kiểu chữ khác nhau giữa xác nhận và biên nhận | 🟡 Minor | Consistency & Standards |
