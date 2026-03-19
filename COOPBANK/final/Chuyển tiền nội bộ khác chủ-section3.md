# 03 — Chi tiết phát hiện

> 8 vấn đề được xác định — 2 Critical · 3 Major · 3 Minor

---

## UXP-001 · 🔴 Critical

### Thiếu nút gửi lại mã OTP và đếm ngược thời gian

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu nút gửi lại mã OTP](ui/internal-transaction-6.png) |
| **Hiện trạng** | Giao diện xác thực OTP chỉ hiển thị 6 ô nhập tĩnh và nút "Xác nhận". Không có nút "Gửi lại mã" hay bộ đếm ngược — vi phạm component spec OTP tiêu chuẩn. |
| **Tác động** | • Nếu mã OTP không đến (chậm mạng, SMS nghẽn), người dùng bị kẹt và phải thoát ứng dụng làm lại từ đầu |
| | • Tỷ lệ bỏ dở giao dịch tại bước xác thực tăng cao |
| **Heuristic vi phạm** | **User Control & Freedom** (Nielsen #3) — Người dùng không có lối thoát khi OTP không đến. **Error Recovery** (Nielsen #9) — Không có cơ chế khắc phục khi xảy ra lỗi gửi mã. |
| **Đề xuất cải thiện** | **Bổ sung cơ chế gửi lại OTP:** |
| | • Thêm nút "Gửi lại mã OTP" (tắt trong 60 giây đầu) |
| | • Thêm bộ đếm ngược "Gửi lại sau 00:45" |
| | • Highlight ô đang nhập với viền focus |
| **Tags** | `Xác nhận giao dịch` · `OTP` |
| **Tham chiếu** | DDL: COMP:otp-input-1 (states: canResend, timeLeft, activeIndex) · UX Law: Doherty Threshold — phản hồi trong 400ms · UXG-184: Keyboard Navigation |

---

## UXP-002 · 🔴 Critical

### Thiếu hiển thị số tiền bằng chữ trên form nhập liệu

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu số tiền bằng chữ](ui/internal-transaction-2.png) |
| **Hiện trạng** | Trường "Số tiền" trên form chỉ hiển thị giá trị số (300,000) và đơn vị tiền tệ (VND). Không có dòng chữ viết thể hiện số tiền. Dòng chữ viết chỉ xuất hiện ở màn Xác nhận ("Hai mươi triệu đồng"). |
| **Tác động** | • Người dùng có thể nhập sai số tiền (nhầm số 0) mà không phát hiện sớm |
| | • Giao dịch sai số tiền dẫn đến yêu cầu hoàn tiền, khiếu nại |
| **Heuristic vi phạm** | **Error Prevention** (Nielsen #5) — Không có cơ chế xác nhận trực quan để ngăn lỗi nhập sai số tiền tại thời điểm nhập. |
| **Đề xuất cải thiện** | **Thêm dòng chữ viết số tiền theo thời gian thực:** |
| | • Hiển thị dòng "Ba trăm nghìn đồng" ngay dưới ô nhập số tiền |
| | • Cập nhật real-time khi người dùng thay đổi con số |
| **Tags** | `Form nhập thông tin` · `Số tiền` |
| **Tham chiếu** | DDL: UXG-165 (Input Validation — real-time feedback) · UXG-243 (Amount confirmation) · Banking best practice: amount text representation |

---

## UXP-003 · 🟠 Major

### Nút "Tiếp tục" bị đẩy khỏi vùng hiển thị khi bật đặt lịch

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Nút hành động bị ẩn](ui/internal-transaction-2.png) |
| **Hiện trạng** | Khi person dùng bật chế độ đặt lịch, form mở rộng xuống 1098px (vượt viewport thiết bị 812px). Nút "Tiếp tục" bị đẩy ra khỏi màn hình — người dùng phải cuộn xuống để tìm. |
| **Tác động** | • Người dùng điền xong thông tin nhưng không thấy nút hành động → hoang mang, bỏ dở |
| | • Giảm tỷ lệ hoàn thành giao dịch |
| **Heuristic vi phạm** | **Visibility of System Status** (Nielsen #1) — Nút hành động chính không nằm trong vùng nhìn thấy. **Fitts's Law** — Khoảng cách đến mục tiêu quá xa. |
| **Đề xuất cải thiện** | **Cố định nút hành động ở cuối màn hình:** |
| | • Chuyển nút "Tiếp tục" sang sticky footer — luôn hiển thị dù cuộn form |
| | • Thêm bóng đổ phía trên để phân tách với nội dung |
| **Tags** | `Form nhập thông tin` · `Đặt lịch` |
| **Tham chiếu** | DDL: UXG-180 (CTA visibility) · UX Law: Fitts's Law — touch targets & distance · Artboard 59:20803 height=1098px vs viewport 812px |

---

## UXP-004 · 🟠 Major

### Số tiền trên tiêu đề và chi tiết trong biên nhận không khớp

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Số tiền không nhất quán](ui/internal-transaction-7.png) |
| **Hiện trạng** | Phần tiêu đề thẻ biên nhận hiển thị "50,000 VND" nhưng phần chi tiết bên dưới ghi "Số tiền: 20,000,000 VND". Hai con số mâu thuẫn gây hoang mang. |
| **Tác động** | • Người dùng không biết số tiền thực tế là bao nhiêu → mất niềm tin vào hệ thống |
| | • Ấn tượng cuối cùng (Peak-End Rule) tiêu cực |
| **Heuristic vi phạm** | **Consistency & Standards** (Nielsen #4) — Cùng một thuộc tính (số tiền) hiển thị hai giá trị khác nhau trên cùng màn hình. |
| **Đề xuất cải thiện** | **Đồng bộ dữ liệu số tiền:** |
| | • Số tiền tiêu đề phải lấy cùng nguồn với chi tiết |
| | • Thêm dòng chữ viết dưới số tiền tiêu đề |
| **Tags** | `Kết quả giao dịch` |
| **Tham chiếu** | DDL: UXG-165 (Data consistency) · UX Law: Peak-End Rule — negative final impression |

---

## UXP-005 · 🟠 Major

### Dropdown phương thức xác thực chỉ có một lựa chọn duy nhất

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Dropdown 1 lựa chọn](ui/internal-transaction-5.png) |
| **Hiện trạng** | Dropdown "Chọn phương thức xác thực" hiển thị "SMS OTP" là lựa chọn duy nhất. Giao diện dropdown gợi ý có nhiều tùy chọn nhưng thực tế chỉ có một. |
| **Tác động** | • Người dùng nhấn vào dropdown mong đợi có nhiều lựa chọn → thất vọng khi chỉ thấy một |
| | • Thêm một bước tương tác không cần thiết → tăng thời gian hoàn thành |
| **Heuristic vi phạm** | **Aesthetic & Minimalist Design** (Nielsen #8) — Hiển thị dropdown khi không có lựa chọn thực sự. **Hick's Law** — Điểm quyết định không cần thiết. |
| **Đề xuất cải thiện** | **Hiển thị tĩnh khi chỉ có một phương thức:** |
| | • Nếu chỉ 1 phương thức: hiển thị dạng text tĩnh "Xác thực bằng SMS OTP" |
| | • Nếu có từ 2 phương thức trở lên: giữ dropdown |
| **Tags** | `Xác nhận giao dịch` |
| **Tham chiếu** | DDL: UXG-183 (ARIA Labels) · UX Law: Hick's Law — unnecessary decision point |

---

## UXP-006 · 🟡 Minor

### Lỗi chính tả trên banner hướng dẫn

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Lỗi chính tả](ui/internal-transaction-5.png) |
| **Hiện trạng** | Banner thông tin ghi "Qúy khách" thay vì "Quý khách" — lỗi dấu thanh tiếng Việt. |
| **Tác động** | • Giảm cảm nhận chuyên nghiệp của ứng dụng |
| | • Người dùng Việt Nam nhạy cảm với lỗi chính tả |
| **Heuristic vi phạm** | **Consistency & Standards** (Nielsen #4) — Lỗi nội dung ảnh hưởng đến uy tín thương hiệu. |
| **Đề xuất cải thiện** | **Sửa chính tả:** |
| | • Sửa "Qúy khách" → "Quý khách" |
| **Tags** | `Xác nhận giao dịch` |
| **Tham chiếu** | DDL: UXG-165 (Content accuracy) |

---

## UXP-007 · 🟡 Minor

### Nội dung giao dịch tự điền thiếu nhãn gợi ý

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Nội dung tự điền](ui/internal-transaction.png) |
| **Hiện trạng** | Nội dung giao dịch được tự điền dạng không dấu: "NGUYEN HOANG KHAI chuyen tien". Người dùng có thể không nhận ra đây là giá trị tự tạo và có thể chỉnh sửa. |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Thêm nhãn "[Tự động]":** |
| | • Gắn nhãn gợi ý người dùng biết nội dung có thể chỉnh sửa |
| **Tags** | `Form nhập thông tin` |
| **Tham chiếu** | DDL: UXG-181 (Alt Text — meaningful labels) |

---

## UXP-008 · 🟡 Minor

### Biên nhận giao dịch không hiển thị phí và thuế

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu thông tin phí](ui/internal-transaction-7.png) |
| **Hiện trạng** | Biên nhận kết quả giao dịch không hiển thị phí giao dịch cụ thể và thuế giá trị gia tăng. Người dùng chỉ được thông báo "Phí theo quy định" ở form nhập mà không biết con số cụ thể. |
| **Tác động** | • Thiếu minh bạch về chi phí → giảm niềm tin |
| | • Người dùng phải kiểm tra lại qua kênh khác |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Hiển thị thông tin phí trên biên nhận:** |
| | • Thêm dòng "Phí giao dịch: X VND" và "Thuế giá trị gia tăng: Y VND" |
| | • Đảm bảo dữ liệu mẫu nhất quán về thời gian |
| **Tags** | `Kết quả giao dịch` |
| **Tham chiếu** | DDL: UXG-235 (Disclaimer/Transparency) · UX Law: Peak-End Rule |

---

## Tổng hợp Findings

| ID | Tên vấn đề | Severity | Heuristic |
|---|---|---|---|
| UXP-001 | Thiếu nút gửi lại mã OTP và đếm ngược thời gian | 🔴 Critical | User Control & Freedom |
| UXP-002 | Thiếu hiển thị số tiền bằng chữ trên form nhập liệu | 🔴 Critical | Error Prevention |
| UXP-003 | Nút "Tiếp tục" bị đẩy khỏi vùng hiển thị khi bật đặt lịch | 🟠 Major | Visibility of System Status |
| UXP-004 | Số tiền trên tiêu đề và chi tiết trong biên nhận không khớp | 🟠 Major | Consistency & Standards |
| UXP-005 | Dropdown phương thức xác thực chỉ có một lựa chọn duy nhất | 🟠 Major | Aesthetic & Minimalist Design |
| UXP-006 | Lỗi chính tả trên banner hướng dẫn | 🟡 Minor | Consistency & Standards |
| UXP-007 | Nội dung giao dịch tự điền thiếu nhãn gợi ý | 🟡 Minor |  |
| UXP-008 | Biên nhận giao dịch không hiển thị phí và thuế | 🟡 Minor |  |
