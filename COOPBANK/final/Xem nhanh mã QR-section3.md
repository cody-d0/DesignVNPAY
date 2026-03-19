# 03 — Chi tiết phát hiện

> 10 vấn đề được xác định — 1 Critical · 3 Major · 6 Minor

---

## UXP-001 · 🔴 Critical

### Thiếu trạng thái loading khi bật/tắt tính năng hiển thị nhanh mã QR

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu trạng thái loading](ui/xem-nhanh-ma-qr-3.png) |
| **Hiện trạng** | Khi người dùng nhấn nút "Đồng ý" trên popup xác nhận bật/tắt tính năng mã QR, không có trạng thái loading giữa lúc xác nhận và khi kết quả hiển thị. Đây là hành động bảo mật quan trọng — cho phép hiển thị mã QR mà không cần đăng nhập. |
| **Tác động** | • Người dùng có thể nhấn "Đồng ý" nhiều lần do không thấy phản hồi từ hệ thống |
| | • Vi phạm nguyên tắc "Security-first" trong ứng dụng ngân hàng — thao tác bảo mật phải có phản hồi rõ ràng |
| **Heuristic vi phạm** | **Visibility of System Status** (Nielsen #1) — Hệ thống không thông báo rằng yêu cầu đang được xử lý. |
| **Đề xuất cải thiện** | **Bổ sung loading indicator và ngăn double-tap:** |
| | • Thêm loading spinner trên nút "Đồng ý" sau khi nhấn |
| | • Vô hiệu hóa nút trong khi đang xử lý (ngăn double-tap) |
| | • Hiển thị tiến trình xử lý trước khi chuyển sang popup kết quả |
| **Tags** | `Cài đặt mã QR` · `Bảo mật` |
| **Tham chiếu** | DDL: UXG-165 (System Feedback) · UX Law: Fitts's Law — interactive elements cần phản hồi · Banking best practice: Security-first feedback |

---

## UXP-002 · 🟠 Major

### Popup xác nhận thiếu icon cảnh báo cho hành động bảo mật

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Title popup chung chung](ui/xem-nhanh-ma-qr-3.png) |
| **Hiện trạng** | Popup xác nhận bật/tắt tính năng mã QR chỉ có title "Thông báo" — quá chung chung cho hành động bảo mật quan trọng. Không có icon cảnh báo (shield/warning) để nhấn mạnh mức độ nghiêm trọng. |
| **Tác động** | • Người dùng không nhận ra mức độ quan trọng của hành động bảo mật |
| | • Title "Thông báo" không phân biệt được với thông báo thông thường |
| **Heuristic vi phạm** | **Consistency & Standards** (Nielsen #4) — Popup bảo mật cần visual hierarchy cao hơn notification bình thường. |
| **Đề xuất cải thiện** | **Tăng visual hierarchy cho popup bảo mật:** |
| | • Thêm icon shield/security phía trên title popup |
| | • Đổi title "Thông báo" → "Xác nhận bảo mật" |
| | • Highlight từ khóa "không cần đăng nhập" bằng màu cảnh báo |
| **Tags** | `Cài đặt mã QR` · `Popup` |
| **Tham chiếu** | DDL: UXG-243 (Warning Feedback) · UX Law: Peak-End Rule — confirmation quality affects memory |

---

## UXP-003 · 🟠 Major

### Mô tả bảo mật dạng khối văn bản dài, khó đọc trên di động

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Mô tả dài khó quét](ui/xem-nhanh-ma-qr-2.png) |
| **Hiện trạng** | Mô tả bảo mật phía trên danh sách tài khoản là một đoạn văn liên tục, chiếm nhiều diện tích trên viewport di động 375px. Nội dung quan trọng về bảo mật bị mất hiệu quả do wall of text. |
| **Tác động** | • Người dùng bỏ qua đọc thông tin bảo mật quan trọng do wall of text |
| | • Thông điệp "tuyệt đối không chia sẻ mã QR" bị giảm tác động |
| **Heuristic vi phạm** | **Aesthetic & Minimalist Design** (Nielsen #8) — Nội dung cần tối giản, dễ quét bằng mắt. |
| **Đề xuất cải thiện** | **Tách thành thẻ cảnh báo ngắn gọn:** |
| | • Tách thành 2 bullet points: tính năng + cảnh báo bảo mật |
| | • Dùng thẻ cảnh báo (warning card) với icon nổi bật |
| **Tags** | `Cài đặt mã QR` · `Nội dung` |
| **Tham chiếu** | DDL: UXG-78 (Content Scannability) |

---

## UXP-004 · 🟠 Major

### Nút "Cài đặt ngay" trên popup hướng dẫn không rõ luồng tiếp theo

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Flow không rõ ràng](ui/xem-nhanh-ma-qr-10.png) |
| **Hiện trạng** | Popup hướng dẫn bật tính năng mã QR có nút "Cài đặt ngay" nhưng người dùng chưa đăng nhập. Không rõ nhấn nút sẽ dẫn đến trang đăng nhập rồi mới mở cài đặt, hay mở trực tiếp. |
| **Tác động** | • Không biết hành trình sẽ trải qua bao nhiêu bước |
| | • Có thể mất bối cảnh ban đầu sau khi đăng nhập |
| **Heuristic vi phạm** | **User Control & Freedom** (Nielsen #3) — Người dùng cần kiểm soát và hiểu rõ luồng thao tác. |
| **Đề xuất cải thiện** | **Làm rõ luồng hành động:** |
| | • Đổi nhãn nút thành "Đăng nhập để cài đặt" |
| | • Sau đăng nhập tự động chuyển đến màn cài đặt mã QR |
| | • Thêm mô tả: "Bạn sẽ được hướng dẫn sau khi đăng nhập" |
| **Tags** | `Đăng nhập` · `Navigation` |
| **Tham chiếu** | DDL: UXG-52 (Navigation Clarity) · UX Law: Hick's Law — unclear decision path |

---

## UXP-005 · 🟡 Minor

### Popup kết quả thành công không tự động đóng sau vài giây

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Không tự đóng](ui/xem-nhanh-ma-qr-4.png) |
| **Hiện trạng** | Popup thông báo bật/tắt thành công chỉ có nút "Đóng" — người dùng phải chủ động nhấn để đóng sau mỗi lần thao tác. |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Tự động đóng popup thành công:** |
| | • Auto-dismiss sau 2-3 giây, giữ nút "Đóng" cho người dùng muốn đóng sớm |
| **Tags** | `Cài đặt mã QR` |
| **Tham chiếu** | DDL: UXG-10 (Auto-dismiss) · UX Law: Doherty Threshold |

---

## UXP-006 · 🟡 Minor

### Thiếu chỉ báo phân trang khi xem mã QR nhiều tài khoản

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu phân trang](ui/xem-nhanh-ma-qr-16.png) |
| **Hiện trạng** | Bottom sheet "Mã QR của tôi" có nút mũi tên trái/phải để chuyển giữa các tài khoản, nhưng thiếu chỉ báo phân trang (dạng chấm tròn hoặc số thứ tự) để người dùng biết đang ở vị trí nào. |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Thêm chỉ báo phân trang:** |
| | • Thêm chấm phân trang (●○○) dưới mã QR |
| | • Hoặc hiển thị "1/3" bên cạnh tên tài khoản |
| **Tags** | `Mã QR của tôi` |
| **Tham chiếu** | DDL: UXG-32 (Pagination Indicator) · UX Law: Fitts's Law |

---

## UXP-007 · 🟡 Minor

### Thanh tab quét mã QR có quá nhiều badge đỏ gây nhiễu thị giác

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Badge đỏ mọi tab](ui/xem-nhanh-ma-qr-12.png) |
| **Hiện trạng** | Thanh tab dưới cùng của màn quét mã QR có 5 tab, tất cả đều hiển thị badge đỏ — tạo nhiễu thị giác đáng kể, đặc biệt trên nền camera tối. |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Giảm nhiễu badge:** |
| | • Chỉ hiển thị badge trên tab có thông tin mới thực sự |
| | • Ẩn thanh tab khi camera đang hoạt động |
| **Tags** | `Quét mã QR` |
| **Tham chiếu** | DDL: UXG-78 (Visual Noise) · UX Law: Hick's Law |

---

## UXP-008 · 🟡 Minor

### Banner quảng cáo trên màn đăng nhập bị cắt và nút khó nhấn

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Banner bị cắt](ui/xem-nhanh-ma-qr-9.png) |
| **Hiện trạng** | Banner quảng cáo "Gói vay hỗ trợ mua nhà" bị cắt ở bên phải. Nút "Chi tiết" nằm ở sát mép màn hình, giảm diện tích nhấn. |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Đảm bảo nội dung trong vùng an toàn:** |
| | • Đảm bảo nút hành động có khoảng đệm ít nhất 16px từ cạnh màn hình |
| **Tags** | `Đăng nhập` |
| **Tham chiếu** | DDL: UXG-32 (Touch Target Spacing) |

---

## UXP-009 · 🟡 Minor

### Thiếu thiết kế trạng thái trống cho tài khoản không đủ điều kiện

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu trạng thái trống](ui/xem-nhanh-ma-qr-2.png) |
| **Hiện trạng** | Thiết kế chỉ thể hiện trường hợp có 2 tài khoản. Không có giao diện cho trường hợp không có tài khoản đủ điều kiện — người dùng sẽ thấy màn hình trống không rõ nguyên nhân. |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Thiết kế trạng thái trống:** |
| | • Thêm icon minh họa 48×48 + title + mô tả + nút mở tài khoản |
| **Tags** | `Cài đặt mã QR` |
| **Tham chiếu** | DDL: COMP:empty-state-1 (icon + title + description + CTA) |

---

## UXP-010 · 🟡 Minor

### Không nhất quán trong microcopy giữa các popup — "Hủy" và "Đóng"

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Wording không nhất quán](ui/popup-touch-id.png) |
| **Hiện trạng** | Popup Touch ID dùng nút "Hủy" cho hành động đóng, trong khi tất cả popup khác trong cùng luồng đều dùng "Đóng". Sự thiếu nhất quán gây nhầm lẫn. |
| **Heuristic vi phạm** |  |
| **Đề xuất cải thiện** | **Thống nhất microcopy:** |
| | • Dùng "Đóng" cho hành động dismiss, hoặc "Hủy xác thực" cho rõ ý hơn |
| **Tags** | `Đăng nhập` · `Touch ID` |
| **Tham chiếu** | DDL: UXG-88 (Consistent Microcopy) |

---

## Tổng hợp Findings

| ID | Tên vấn đề | Severity | Heuristic |
|---|---|---|---|
| UXP-001 | Thiếu trạng thái loading khi bật/tắt tính năng hiển thị nhanh mã QR | 🔴 Critical | Visibility of System Status |
| UXP-002 | Popup xác nhận thiếu icon cảnh báo cho hành động bảo mật | 🟠 Major | Consistency & Standards |
| UXP-003 | Mô tả bảo mật dạng khối văn bản dài, khó đọc trên di động | 🟠 Major | Aesthetic & Minimalist Design |
| UXP-004 | Nút "Cài đặt ngay" trên popup hướng dẫn không rõ luồng tiếp theo | 🟠 Major | User Control & Freedom |
| UXP-005 | Popup kết quả thành công không tự động đóng sau vài giây | 🟡 Minor |  |
| UXP-006 | Thiếu chỉ báo phân trang khi xem mã QR nhiều tài khoản | 🟡 Minor |  |
| UXP-007 | Thanh tab quét mã QR có quá nhiều badge đỏ gây nhiễu thị giác | 🟡 Minor |  |
| UXP-008 | Banner quảng cáo trên màn đăng nhập bị cắt và nút khó nhấn | 🟡 Minor |  |
| UXP-009 | Thiếu thiết kế trạng thái trống cho tài khoản không đủ điều kiện | 🟡 Minor |  |
| UXP-010 | Không nhất quán trong microcopy giữa các popup — "Hủy" và "Đóng" | 🟡 Minor |  |
