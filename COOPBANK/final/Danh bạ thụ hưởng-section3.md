# 03 — Chi tiết phát hiện

> 8 vấn đề được xác định, sắp xếp theo mức độ ảnh hưởng

---

## UXP-001 · 🔴 Critical

### Toast hướng dẫn xóa thiếu khả năng dismiss và có lỗi chính tả

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Toast không dismiss được](ui/contact.png) |
| **Hiện trạng** | Toast "Chọn danh bạ mà Quý khách muốn xóa" hiện cố định, không có nút đóng (×) hay swipe-to-dismiss. Ngoài ra có lỗi chính tả "Qúy" (dấu sắc sai vị trí). |
| **Tác động** | • Toast che khuất thanh tìm kiếm, gây khó thao tác |
| | • Lỗi chính tả giảm sự tin cậy trong ứng dụng ngân hàng |
| **Heuristic vi phạm** | **User Control & Freedom** (Nielsen #3) — Người dùng không có cách tắt thông báo, mất kiểm soát giao diện. |
| **Đề xuất cải thiện** | **Cải thiện toast component:** |
| | • Thêm nút đóng (×) bên phải toast |
| | • Auto-dismiss sau 5 giây |
| | • Sửa lỗi chính tả "Qúy" → "Quý" |
| **Tags** | `Danh sách` · `Toast` · `Chính tả` |
| **Tham chiếu** | DDL: UXG-10 (Dismissible Notifications), UXG-78 (Content Quality) · UX Law: Fitts's Law — dismiss target cần tồn tại và đủ lớn |

---

## UXP-002 · 🔴 Critical

### Label và giá trị bị chồng text trên màn hình chi tiết danh bạ

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Text bị chồng lấp](ui/contact-details.png) |
| **Hiện trạng** | Label "Loại chuyển tiền" bị cắt ngắn, chồng lên với giá trị "Chuyển tiền nhanh 24/7 qua tài khoản" trên cùng hàng, khiến nội dung không đọc được. |
| **Tác động** | • Không xác minh được loại giao dịch → rủi ro chuyển nhầm |
| | • Giảm tín nhiệm ứng dụng ngân hàng khi thông tin hiển thị lỗi |
| **Heuristic vi phạm** | **Aesthetic & Minimalist Design** (Nielsen #8) — Text chồng lấp phá vỡ tính dễ đọc và thẩm mỹ giao diện. |
| **Đề xuất cải thiện** | **Chuyển layout thông tin:** |
| | • Sử dụng layout 2 dòng: label trên, giá trị dưới (stacked) |
| | • Full text "Loại chuyển tiền" — không cắt ngắn |
| **Tags** | `Chi tiết` · `Layout` · `Text Readability` |
| **Tham chiếu** | DDL: UXG-165 (Text Legibility) · UX Law: Peak-End Rule — chi tiết là điểm cuối trước giao dịch, ấn tượng xấu ảnh hưởng quyết định |

---

## UXP-003 · 🟠 Major

### Trạng thái lỗi validation chưa đầy đủ theo component spec

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Error state chưa đầy đủ](ui/add-new-3.png) |
| **Hiện trạng** | Thông báo lỗi "Số tài khoản/Số thẻ không tồn tại" hiện chữ đỏ nhưng viền ô nhập liệu vẫn màu mặc định. Thiếu icon cảnh báo bên cạnh thông báo lỗi. |
| **Tác động** | • Người dùng có thể bỏ lỡ thông báo lỗi vì thiếu tín hiệu thị giác |
| | • Nhập liệu sai nhiều lần → tăng tải hệ thống call center |
| **Heuristic vi phạm** | **Error Prevention** (Nielsen #5) — Phản hồi lỗi thiếu nổi bật khiến người dùng không nhận ra vấn đề. |
| **Đề xuất cải thiện** | **Hoàn thiện error state:** |
| | • Viền ô nhập chuyển sang màu đỏ khi có lỗi |
| | • Thêm icon ⚠️ trước thông báo lỗi |
| | • Vô hiệu hóa nút "Thêm mới" khi form chưa hợp lệ |
| **Tags** | `Form` · `Validation` · `Error State` |
| **Tham chiếu** | DDL: UXG-243 (Error Feedback), COMP:text-input-1 errorBorderColor: {base.destructive} · UX Law: Doherty Threshold — phản hồi lỗi phải rõ ràng trong 400ms |

---

## UXP-004 · 🟠 Major

### Empty state không tuân thủ component spec — thiếu icon và nút hành động

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Empty state thiếu hướng dẫn](ui/search-3.png) |
| **Hiện trạng** | Khi chưa có danh bạ nào, màn hình chỉ hiển thị 1 dòng text. Theo DDL component spec empty-state-1: cần icon 48px, tiêu đề, mô tả, và nút hành động tùy chọn. |
| **Tác động** | • Người dùng mới không biết phải làm gì → mất cơ hội chuyển đổi |
| | • Empty state nhạt nhẽo → trải nghiệm thiếu chuyên nghiệp |
| **Heuristic vi phạm** | **Help & Documentation** (Nielsen #10) — Empty state cần hướng dẫn rõ ràng cho bước tiếp theo. |
| **Đề xuất cải thiện** | **Thiết kế empty state hoàn chỉnh:** |
| | • Thêm icon minh họa danh bạ (48×48 pixel) |
| | • Tiêu đề: "Chưa có danh bạ thụ hưởng" |
| | • Mô tả: "Thêm người thụ hưởng để chuyển tiền nhanh hơn" |
| | • Nút hành động: "Thêm mới" → chuyển đến form thêm |
| **Tags** | `Tìm kiếm` · `Empty State` · `Onboarding` |
| **Tham chiếu** | DDL: COMP:empty-state-1 requires icon (48px) + ctaLabel + description |

---

## UXP-005 · 🟠 Major

### Chế độ chỉnh sửa chi tiết danh bạ thiếu tùy chọn hủy

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu nút hủy chỉnh sửa](ui/contact-details-2.png) |
| **Hiện trạng** | Khi chỉnh sửa tên gợi nhớ, chỉ có 1 nút "Cập nhật". Không có nút "Hủy" hoặc xác nhận khi nhấn quay lại với thay đổi chưa lưu. |
| **Tác động** | • Lo lắng khi vô tình sửa nhầm — không có cách hoàn tác |
| | • Phải thoát và quay lại để hủy — tăng số bước thao tác |
| **Heuristic vi phạm** | **User Control & Freedom** (Nielsen #3) — Cần cung cấp "lối thoát khẩn cấp" rõ ràng cho mọi hành động chỉnh sửa. |
| **Đề xuất cải thiện** | **Thêm khả năng hủy chỉnh sửa:** |
| | • Thêm nút "Hủy" (viền outline) bên trái nút "Cập nhật" |
| | • Hiện hộp thoại xác nhận khi nhấn quay lại với thay đổi chưa lưu |
| **Tags** | `Chi tiết` · `Edit Mode` · `Navigation` |
| **Tham chiếu** | DDL: UXG-4 (Undo/Cancel Support) |

---

## UXP-006 · 🟡 Minor

### Danh sách dài thiếu section headers cố định khi cuộn

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Không có section cố định](ui/contact-2.png) |
| **Hiện trạng** | Khi mở rộng tất cả các nhóm, danh sách dài hơn 1200 pixel. Không có tiêu đề nhóm cố định (sticky) khi cuộn xuống. |
| **Tác động** | • Mất phương hướng — không biết đang xem nhóm nào khi cuộn |
| **Heuristic vi phạm** | **Recognition Rather Than Recall** (Nielsen #6) — Section context bị mất khi cuộn. |
| **Đề xuất cải thiện** | **Sticky section headers:** |
| | • Tiêu đề nhóm cố định khi cuộn qua section đó |
| | • Mặc định thu gọn sections, chỉ mở khi người dùng chạm |
| **Tags** | `Danh sách` · `Navigation` |
| **Tham chiếu** | DDL: UXG-52 (Long List Orientation), Hick's Law |

---

## UXP-007 · 🟡 Minor

### Tên chủ tài khoản tự động điền thiếu nhãn và không nhất quán kiểu chữ

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Tên viết hoa toàn bộ, thiếu label](ui/add-new-2.png) |
| **Hiện trạng** | "NGUYEN HOANG HIEU" hiện viết hoa toàn bộ không có nhãn giải thích. Bên dưới "Nguyen Hoang Hieu" có nhãn "Tên gợi nhớ" — 2 cách viết tên khác nhau gây nhầm lẫn. |
| **Tác động** | • Nhầm lẫn giữa tên chủ tài khoản và tên gợi nhớ |
| **Heuristic vi phạm** | **Consistency & Standards** (Nielsen #4) — Cùng loại dữ liệu phải thống nhất kiểu hiển thị. |
| **Đề xuất cải thiện** | **Thống nhất hiển thị tên:** |
| | • Thêm label "Tên chủ tài khoản" phía trên tên tự động điền |
| | • Thêm ghi chú "(theo ngân hàng)" nếu cần giữ chữ hoa |
| **Tags** | `Form` · `Typography` |
| **Tham chiếu** | DDL: UXG-88 (Consistent Text Formatting) |

---

## UXP-008 · 🟡 Minor

### Nút hành động nổi chồng lên thanh điều hướng dưới cùng

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Nút thêm chồng thanh điều hướng](ui/contact-3.png) |
| **Hiện trạng** | Nút hành động nổi (+) ở góc phải dưới nằm sát thanh điều hướng — 2 vùng chạm chồng lấp nhau. |
| **Tác động** | • Có thể chạm nhầm giữa nút thêm và thanh điều hướng |
| **Heuristic vi phạm** | **Error Prevention** (Nielsen #5) — Khoảng cách vùng chạm cần tối thiểu 8px để tránh chạm nhầm. |
| **Đề xuất cải thiện** | **Tăng khoảng cách:** |
| | • Nâng nút hành động nổi lên 16 pixel phía trên thanh điều hướng |
| **Tags** | `Danh sách` · `Touch Target` |
| **Tham chiếu** | DDL: UXG-32 (Touch Target Spacing), Fitts's Law |

---

## Tổng hợp Findings

| ID | Tên vấn đề | Severity | Heuristic |
|---|---|---|---|
| UXP-001 | Toast hướng dẫn xóa thiếu khả năng dismiss và có lỗi chính tả | 🔴 Critical | User Control & Freedom |
| UXP-002 | Label và giá trị bị chồng text trên màn hình chi tiết danh bạ | 🔴 Critical | Aesthetic & Minimalist Design |
| UXP-003 | Trạng thái lỗi validation chưa đầy đủ theo component spec | 🟠 Major | Error Prevention |
| UXP-004 | Empty state không tuân thủ component spec — thiếu icon và nút hành động | 🟠 Major | Help & Documentation |
| UXP-005 | Chế độ chỉnh sửa chi tiết danh bạ thiếu tùy chọn hủy | 🟠 Major | User Control & Freedom |
| UXP-006 | Danh sách dài thiếu section headers cố định khi cuộn | 🟡 Minor | Recognition Rather Than Recall |
| UXP-007 | Tên chủ tài khoản tự động điền thiếu nhãn và không nhất quán kiểu chữ | 🟡 Minor | Consistency & Standards |
| UXP-008 | Nút hành động nổi chồng lên thanh điều hướng dưới cùng | 🟡 Minor | Error Prevention |
