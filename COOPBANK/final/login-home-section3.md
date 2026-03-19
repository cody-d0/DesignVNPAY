# 03 — Chi tiết phát hiện

> 7 vấn đề được xác định, sắp xếp theo mức độ ảnh hưởng

---

## UXP-001 · 🔴 Critical

### Form đăng nhập thiếu hoàn toàn trạng thái lỗi cho mật khẩu sai và tài khoản bị khóa

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Không có error state](ui/login-with-touch-id.png) |
| **Hiện trạng** | Form đăng nhập không hiển thị bất kỳ phản hồi lỗi nào: sai mật khẩu, tài khoản bị khóa, hoặc lỗi kết nối. Không có variant error trong 4 artboards. |
| **Tác động** | • Người dùng nhập sai mật khẩu không biết lý do — frustration cao |
| | • Tăng tải hỗ trợ khi người dùng không biết tài khoản bị khóa |
| **Heuristic vi phạm** | **Help Users Recognize, Diagnose, and Recover from Errors** (Nielsen #9) — Thông báo lỗi phải rõ ràng, chỉ ra nguyên nhân và gợi ý giải pháp. |
| **Đề xuất cải thiện** | **Thêm error state đầy đủ:** |
| | • Viền ô mật khẩu chuyển đỏ + helper text "Mật khẩu không đúng. Bạn còn X lần thử." |
| | • Banner cảnh báo khi tài khoản bị khóa + hướng dẫn gọi hotline |
| | • Toast thông báo lỗi kết nối mạng |
| **Tags** | `Đăng nhập` · `Error State` · `Bảo mật` |
| **Tham chiếu** | DDL: UXG-04 (Error Recovery), UXG-78 (Action Availability) · COMP: text-input-1 state.error · UX Law: Nielsen #9 |

---

## UXP-002 · 🔴 Critical

### Ô nhập liệu đăng nhập thiếu nhãn cố định — chỉ dùng placeholder text

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Placeholder thay label](ui/login-with-phone-number.png) |
| **Hiện trạng** | "Số điện thoại" và "Mật khẩu" là placeholder, biến mất khi người dùng bắt đầu nhập. Thiếu floating label hoặc nhãn cố định phía trên ô nhập liệu. |
| **Tác động** | • Accessibility fail — screen reader không đọc được label |
| | • Người dùng quên mình đang nhập gì khi placeholder biến mất |
| **Heuristic vi phạm** | **Visibility of System Status** (Nielsen #1) — Label phải luôn hiển thị để người dùng biết context nhập liệu. |
| **Đề xuất cải thiện** | **Thêm floating label:** |
| | • Floating label "Số điện thoại" và "Mật khẩu" trên mỗi ô nhập liệu |
| | • Font size nhãn: 12px medium — theo DDL text-input-1 spec |
| **Tags** | `Đăng nhập` · `Form` · `Accessibility` |
| **Tham chiếu** | DDL: UXG-10 (Form Label), UXG-07 (Accessibility) · COMP: text-input-1 overridable.label (required by schema) · UX Law: WCAG 2.1 AA, Fitts's Law |

---

## UXP-003 · 🟠 Major

### Trang chủ hiển thị hơn 20 dịch vụ cùng cấp gây quá tải nhận thức

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Quá tải lựa chọn](ui/homepage-expand-2.png) |
| **Hiện trạng** | 3 sections (Tài chính: 6, Mua sắm: 8, Tiện ích: 6) với tổng 20+ items đồng nhất kích thước và kiểu dáng — không phân biệt mức độ ưu tiên. |
| **Tác động** | • Quá tải nhận thức — thời gian quyết định tăng theo Hick's Law |
| | • Khó tìm dịch vụ thường dùng trong ma trận icons |
| **Heuristic vi phạm** | **Aesthetic & Minimalist Design** (Nielsen #8) — Giao diện nên chỉ hiển thị thông tin cần thiết, ẩn phần còn lại. |
| **Đề xuất cải thiện** | **Phân cấp dịch vụ:** |
| | • Hiển thị 6 dịch vụ "Hay dùng" mặc định + "Xem tất cả" |
| | • Thu gọn sections phụ, chỉ hiện 3 items + "Xem thêm (5)" |
| | • Cho phép tùy chỉnh quick actions theo nhu cầu cá nhân |
| **Tags** | `Trang chủ` · `Information Architecture` · `Navigation` |
| **Tham chiếu** | DDL: UXG-45 (Information Hierarchy), UXG-12 (Visual Feedback) · UX Law: Hick's Law — thời gian quyết định tăng logarithmic theo số lựa chọn |

---

## UXP-004 · 🟠 Major

### Thông tin cá nhân thiếu hoàn toàn khả năng yêu cầu cập nhật trực tuyến

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thiếu nút hành động](ui/basic-infor.png) |
| **Hiện trạng** | 6 trường thông tin hiển thị chỉ đọc. Ghi chú cuối trang hướng dẫn liên hệ chi nhánh — bắt người dùng phải đến trực tiếp để cập nhật email hoặc địa chỉ. |
| **Tác động** | • Ma sát cao — cần nỗ lực offline để cập nhật thông tin cơ bản |
| | • Dữ liệu khách hàng lỗi thời ảnh hưởng kênh liên lạc |
| **Heuristic vi phạm** | **Flexibility and Efficiency of Use** (Nielsen #7) — Cần cung cấp shortcut cho các tác vụ phổ biến. |
| **Đề xuất cải thiện** | **Thêm kênh cập nhật trực tuyến:** |
| | • Nút "Yêu cầu cập nhật thông tin" → form request online |
| | • Link "Gọi hotline" trực tiếp bên cạnh ghi chú |
| **Tags** | `Thông tin cá nhân` · `CTA` · `User Flow` |
| **Tham chiếu** | DDL: UXG-78 (Action Availability), UXG-55 (Privacy) · UX Law: Nielsen #7 (Flexibility and efficiency of use) |

---

## UXP-005 · 🟠 Major

### Mục "Thoát ứng dụng" thiếu phân biệt thị giác và hộp thoại xác nhận

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Thoát thiếu safeguard](ui/settings.png) |
| **Hiện trạng** | "Thoát ứng dụng" nằm cuối danh sách menu, cùng kiểu dáng với các mục thông thường. Không có phân cách, biểu tượng cảnh báo, hoặc hộp thoại xác nhận. |
| **Tác động** | • Chạm nhầm dẫn đến đăng xuất bất ngờ |
| | • Phải đăng nhập lại — lãng phí thời gian |
| **Heuristic vi phạm** | **Error Prevention** (Nielsen #5) — Hành động phá hủy cần xác nhận trước khi thực thi. |
| **Đề xuất cải thiện** | **Thêm safeguard cho hành động đăng xuất:** |
| | • Đổi màu text "Thoát" sang đỏ + icon khác biệt |
| | • Thêm đường phân cách trước mục cuối |
| | • Thêm hộp thoại xác nhận: "Bạn có chắc muốn thoát?" |
| **Tags** | `Cài đặt` · `Destructive Action` · `Confirmation` |
| **Tham chiếu** | DDL: UXG-04 (Error Recovery), UXG-36 (Destructive Action Safeguard) · UX Law: Nielsen #5 (Error Prevention) |

---

## UXP-006 · 🟡 Minor

### Ngôn ngữ không nhất quán: tiếng Anh xen lẫn tiếng Việt và viết tắt

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Ngôn ngữ không nhất quán](ui/popup-touch-id.png) |
| **Hiện trạng** | Popup hiển thị "Touch ID" (tiếng Anh) với nội dung tiếng Việt. Tab dưới cùng viết tắt "ATM/CN" thay vì "ATM/Chi nhánh". |
| **Tác động** | • Người dùng lớn tuổi có thể không hiểu thuật ngữ tiếng Anh hoặc viết tắt |
| **Heuristic vi phạm** | **Consistency & Standards** (Nielsen #4) — Sử dụng ngôn ngữ nhất quán xuyên suốt ứng dụng. |
| **Đề xuất cải thiện** | **Thống nhất ngôn ngữ:** |
| | • Thêm phụ đề "Xác thực vân tay" bên dưới "Touch ID" |
| | • Viết đầy đủ "ATM/Chi nhánh" thay vì viết tắt |
| **Tags** | `Đăng nhập` · `Ngôn ngữ` · `Inclusivity` |
| **Tham chiếu** | DDL: UXG-07 (Language Consistency) · UX Law: Jakob's Law — người dùng mong đợi trải nghiệm nhất quán |

---

## UXP-007 · 🟡 Minor

### Nút "Chi tiết" trên banner quảng cáo nhỏ hơn 44 pixel — khó chạm trên di động

| | |
|---|---|
| **Ảnh minh họa** | ![⚠️ Nút hành động nhỏ](ui/homepage-shorten.png) |
| **Hiện trạng** | Banner quảng cáo chiếm 30% viewport nhưng nút hành động "Chi tiết" có kích thước ước lượng 60×30 pixel — dưới ngưỡng 44×44 pixel của iOS HIG. |
| **Tác động** | • Khó nhấn chính xác trên di động, đặc biệt khi di chuyển |
| **Heuristic vi phạm** | **Error Prevention** (Nielsen #5) — Vùng chạm nhỏ tăng khả năng chạm nhầm. |
| **Đề xuất cải thiện** | **Tăng vùng chạm:** |
| | • Tăng kích thước nút lên tối thiểu 44×44 pixel |
| | • Thêm auto-scroll animation cho banner slider |
| **Tags** | `Trang chủ` · `Touch Target` · `Banner` |
| **Tham chiếu** | DDL: UXG-52 (Touch Target ≥ 44px) · UX Law: Fitts's Law — thời gian chạm tỉ lệ nghịch với kích thước mục tiêu |

---

## Tổng hợp Findings

| ID | Tên vấn đề | Severity | Heuristic |
|---|---|---|---|
| UXP-001 | Form đăng nhập thiếu hoàn toàn trạng thái lỗi cho mật khẩu sai và tài khoản bị khóa | 🔴 Critical | Help Users Recognize, Diagnose, and Recover from Errors |
| UXP-002 | Ô nhập liệu đăng nhập thiếu nhãn cố định — chỉ dùng placeholder text | 🔴 Critical | Visibility of System Status |
| UXP-003 | Trang chủ hiển thị hơn 20 dịch vụ cùng cấp gây quá tải nhận thức | 🟠 Major | Aesthetic & Minimalist Design |
| UXP-004 | Thông tin cá nhân thiếu hoàn toàn khả năng yêu cầu cập nhật trực tuyến | 🟠 Major | Flexibility and Efficiency of Use |
| UXP-005 | Mục "Thoát ứng dụng" thiếu phân biệt thị giác và hộp thoại xác nhận | 🟠 Major | Error Prevention |
| UXP-006 | Ngôn ngữ không nhất quán: tiếng Anh xen lẫn tiếng Việt và viết tắt | 🟡 Minor | Consistency & Standards |
| UXP-007 | Nút "Chi tiết" trên banner quảng cáo nhỏ hơn 44 pixel — khó chạm trên di động | 🟡 Minor | Error Prevention |
