# 03 — Chi tiết phát hiện

> 8 vấn đề được xác định — 2 Critical · 3 Major · 3 Minor

---

## UXP-001 · 🔴 Critical

### Thiếu nút gửi lại mã OTP và bộ đếm ngược thời gian

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu nút gửi lại mã OTP](ui/chuyen-tien-nhanh-247-qua-tai-khoan-5.png) |
| **Hiện trạng** | Giao diện xác thực OTP chỉ hiển thị 6 ô nhập tĩnh và nút "Xác nhận". Không có nút "Gửi lại mã" hay bộ đếm ngược — vi phạm component spec OTP tiêu chuẩn. |
| **Tác động** | • Nếu mã OTP không đến, người dùng bị kẹt và phải thoát ứng dụng làm lại từ đầu |
| | • Tỷ lệ bỏ dở giao dịch tại bước xác thực tăng cao |
| **Heuristic vi phạm** | **User Control & Freedom** (Nielsen #3) — Không có lối thoát khi OTP không đến. **Error Recovery** (Nielsen #9) — Không có cơ chế khắc phục. |
| **Đề xuất cải thiện** | **Bổ sung cơ chế gửi lại OTP:** |
| | • Thêm nút "Gửi lại mã OTP" (tắt trong 60 giây đầu) |
| | • Thêm bộ đếm ngược "Gửi lại sau 00:45" |
| | • Highlight ô đang nhập với viền focus |
| **Tags** | `Xác nhận giao dịch` · `OTP` |
| **Tham chiếu** | DDL: COMP:otp-input-1 (states: canResend, timeLeft, activeIndex) · UX Law: Doherty Threshold — phản hồi trong 400ms · UXG-184: Keyboard Navigation · PRD: SCR-CB-002 NFR-001, NFR-002 |

---

## UXP-002 · 🔴 Critical

### Thiếu trạng thái lỗi và phản hồi xác thực cho các trường nhập liệu

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu trạng thái lỗi input](ui/chuyen-tien-nhanh-247-qua-tai-khoan.png) |
| **Hiện trạng** | Toàn bộ 6 artboards của form nhập không có variant nào hiển thị trạng thái lỗi: không viền đỏ, không thông báo lỗi dưới trường nhập khi người dùng nhập sai. |
| **Tác động** | • Người dùng không biết mình nhập sai ở đâu → phải đoán, thử lại nhiều lần |
| | • Tăng tỷ lệ thất bại giao dịch, tăng cuộc gọi hỗ trợ |
| **Heuristic vi phạm** | **Error Prevention** (Nielsen #5) — Không có cơ chế ngăn lỗi. **Help Users Recognize Errors** (Nielsen #9) — Không có phản hồi lỗi cụ thể. |
| **Đề xuất cải thiện** | **Thêm trạng thái lỗi cho input fields:** |
| | • Thêm variant viền đỏ + thông báo lỗi cụ thể dưới trường |
| | • Xác thực real-time: số tài khoản, số tiền |
| **Tags** | `Form nhập thông tin` · `Xác thực` |
| **Tham chiếu** | DDL: COMP:text-input-1 (variant: error state) · TOKEN:base.destructive = #dc2626 · UXG-187: Error Messages · PRD: SCR-CB-001 BR-001 (validate số dư) |

---

## UXP-003 · 🟠 Major

### Thiếu hiển thị số tiền bằng chữ real-time trên form nhập liệu

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Số tiền bằng chữ chỉ ở filled](ui/chuyen-tien-nhanh-247-qua-tai-khoan-3.png) |
| **Hiện trạng** | Dòng "Hai mươi triệu đồng" chỉ xuất hiện ở form đã điền và màn xác nhận. Form trống không có ám chỉ rằng dòng chữ viết sẽ xuất hiện. |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Hiển thị chữ viết số tiền real-time:** |
| | • Cập nhật real-time dòng chữ viết khi đang gõ số |
| **Tags** | `Form nhập thông tin` · `Số tiền` |
| **Tham chiếu** | DDL: UXG-165 (Input Validation) · Banking best practice: amount text representation |

---

## UXP-004 · 🟠 Major

### Dropdown phương thức xác thực chỉ có một lựa chọn duy nhất

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Dropdown 1 lựa chọn](ui/chuyen-tien-nhanh-247-qua-tai-khoan-4.png) |
| **Hiện trạng** | Dropdown "Chọn phương thức xác thực" hiển thị "SMS OTP" là lựa chọn duy nhất — thêm bước tương tác không cần thiết. |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Hiển thị tĩnh khi chỉ có một phương thức:** |
| | • Nếu chỉ 1 phương thức: text tĩnh "Xác thực bằng SMS OTP" |
| | • Nếu từ 2+ phương thức: giữ dropdown |
| **Tags** | `Xác nhận giao dịch` |
| **Tham chiếu** | DDL: UXG-183 (ARIA Labels) · UX Law: Hick's Law — unnecessary decision point · PRD: SCR-CB-002 NFR-002 |

---

## UXP-005 · 🟠 Major

### Biên nhận giao dịch không hiển thị phí giao dịch

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu phí trên biên nhận](ui/chuyen-tien-nhanh-247-qua-tai-khoan-6.png) |
| **Hiện trạng** | Biên nhận hiển thị 6 dòng chi tiết nhưng không có phí. Phí 2,000 VND có ở màn xác nhận nhưng biến mất khỏi biên nhận. |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Hiển thị phí trên biên nhận:** |
| | • Thêm "Phí giao dịch: 2,000 VND" trên biên nhận kết quả |
| **Tags** | `Kết quả giao dịch` |
| **Tham chiếu** | DDL: UXG-235 (Disclaimer/Transparency) · COMP:receipt-preview-1 (totals section) · UX Law: Peak-End Rule · PRD: SCR-CB-003 BR-004 |

---

## UXP-006 · 🟡 Minor

### Nội dung giao dịch tự điền thiếu nhãn gợi ý

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Nội dung tự điền](ui/chuyen-tien-nhanh-247-qua-tai-khoan.png) |
| **Hiện trạng** | Nội dung "NGUYEN HOANG KHAI chuyen tien" — dạng không dấu, không nhãn cho biết giá trị có thể chỉnh sửa. |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Thêm nhãn "[Tự động]":** |
| | • Gắn nhãn gợi ý người dùng biết nội dung có thể chỉnh sửa |
| **Tags** | `Form nhập thông tin` |
| **Tham chiếu** | DDL: UXG-181 (Alt Text — meaningful labels) |

---

## UXP-007 · 🟡 Minor

### Tên người thụ hưởng không nhất quán giữa các màn hình

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Tên không nhất quán](ui/chuyen-tien-nhanh-247-qua-tai-khoan-6.png) |
| **Hiện trạng** | Form auto-fill "NGUYEN HOANG HIEU" nhưng xác nhận và kết quả hiển thị "NGUYEN TUNG" — dữ liệu mẫu không đồng nhất. |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Đồng nhất dữ liệu mẫu:** |
| | • Đảm bảo tên xuyên suốt flow nhất quán |
| **Tags** | `Kết quả giao dịch` · `Xác nhận giao dịch` |
| **Tham chiếu** | DDL: UXG-165 (Data consistency) · Nielsen #4: Consistency & Standards · PRD: SCR-CB-003 BR-002 |

---

## UXP-008 · 🟡 Minor

### Trường nhập thông tin thụ hưởng thiếu helper text

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu helper text](ui/chuyen-tien-nhanh-247-qua-tai-khoan.png) |
| **Hiện trạng** | Trường thụ hưởng không có helper text giải thích có thể nhập số tài khoản, số thẻ, hoặc số điện thoại. |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Thêm helper text:** |
| | • "Nhập số tài khoản, số thẻ hoặc số điện thoại người nhận" |
| **Tags** | `Form nhập thông tin` |
| **Tham chiếu** | DDL: UXG-186 (Form Labels) · COMP:text-input-1 (prop: helperText) · PRD: SCR-CB-001 BR-002 |

---

## Tổng hợp Findings

| ID | Tên vấn đề | Severity | Heuristic |
|---|---|---|---|
| UXP-001 | Thiếu nút gửi lại mã OTP và bộ đếm ngược thời gian | 🔴 Critical | User Control & Freedom |
| UXP-002 | Thiếu trạng thái lỗi và phản hồi xác thực cho các trường nhập liệu | 🔴 Critical | Error Prevention |
| UXP-003 | Thiếu hiển thị số tiền bằng chữ real-time trên form nhập liệu | 🟠 Major |  |
| UXP-004 | Dropdown phương thức xác thực chỉ có một lựa chọn duy nhất | 🟠 Major |  |
| UXP-005 | Biên nhận giao dịch không hiển thị phí giao dịch | 🟠 Major |  |
| UXP-006 | Nội dung giao dịch tự điền thiếu nhãn gợi ý | 🟡 Minor |  |
| UXP-007 | Tên người thụ hưởng không nhất quán giữa các màn hình | 🟡 Minor |  |
| UXP-008 | Trường nhập thông tin thụ hưởng thiếu helper text | 🟡 Minor |  |
