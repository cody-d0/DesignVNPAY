# 📋 Thanh toán hóa đơn

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `core/`
> **Trích xuất:** 2026-03-28

---

## 5. Bảng mã lỗi Thanh toán hóa đơn chung

> **Page ID:** `210207958` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/210207958

1/ Lỗi hệ thống/kết nối
 | | 
TT
 | 
Case
 | 
Tác nhân
 | 
Nội dung thông báo (VN)

 | 
1
 | 
Time -out
 | 
Billing (08)
 | 
<Tham khảo tại Bảng mã lỗi chung>

Tại màn hình Khởi tạo:

Kết nối tới nhà cung cấp dịch vụ tạm thời bị gián đoạn. Quý khách vui lòng thử lại sau.

Tại màn hình xác nhận

Kết nối thông tin khách hàng tới nhà cung cấp dịch vụ đang được xử lý. Quý khách vui lòng tra cứu tài khoản trước khi thực hiện giao dịch mới hoặc hoặc liên hệ tổng đài Co-opBank 1900545554 để được hỗ trợ.

 | 
2
 | 
Mã khách hàng không tồn tại
 | 
Billing (50)
 | 
Hóa đơn không tồn tại hoặc đã thanh toán. Quý khách vui lòng kiểm tra lại.

 | 
3
 | 
Hệ thống nhà cung cấp đang bảo trì
 | 
Billing (01)
 | 
Giao dịch không thành công do nhà cung cấp dịch vụ không hỗ trợ. Quý khách vui lòng kiểm tra lại.

 | 4 | Hệ thống tạm ngừng phục vụ do lỗi đường truyền giữa VNPAY tới Ngân hàng hoặc VNPAY tới nhà cung cấp (05) | Billing (05) | Hệ thống tạm ngừng phục vụ do lỗi đường truyền giữa VNPAY tới Ngân hàng hoặc VNPAY tới nhà cung cấp. Quý khách vui lòng thử lại sau.
 | 
5
 | 
Không tìm thấy mã đối tác (80)

Không tìm thấy nhà cung cấp (82)

Không tìm thấy dịch vụ (84)

Mã đối tác không hợp lệ (81)
 | 
Billing (80, 81, 82, 84)
 | 
Giao dịch không thành công do không kết nối được với nhà cung cấp dịch vụ. Quý khách vui lòng thử lại.

 | 
6
 | 
Các lỗi khác
 | 
Billing (,07,87,89,90,96,99)
 | 
Giao dịch không thành công hoặc hóa đơn đã được thanh toán trước đó. Quý khách vui lòng kiểm tra lại.

---


## 21. URD_MB_COOPBANK_THANH TOÁN HÓA ĐƠN

> **Page ID:** `29890609` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29890609

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*4 trang con:*

### 21.1. Màn hình Quản lý danh bạ trên Cài đặt

> **Page ID:** `40658717` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/40658717

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, App Client
• Điều kiện trước: 

• KH cài đặt ứng dụng thành công
• KH đã đăng nhập thành công vào ứng dụng
• Kết quả mong muốn:
• KH chọn được loại Danh bạ mong muốn từ MH Cài đặt
#### 2/ Luồng màn hình

##### MH1: MH danh sách chức năng Quản lý danh bạ

3/ Mô tả màn hình

##### MH1: MH danh sách chức năng Quản lý danh bạ
 | | 

 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | Tiêu đề | Label | Read Only | -- | -- | 
QUẢN LÝ DANH BẠ

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn Back, hiển thị màn hình thao tác trước đó
 | 3 | Danh sách chức năng | Icon | Click | -- | -- | 
Gồm các chức năng:

• Danh bạ thụ hưởng
• Danh bạ hóa đơn

#### 4/ Luồng xử lý

##### Truy cập chức năng
 | | 

 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Click label Quản lý danh bạ ở MH Cài đặt | 
MB Client
 | 
Hiển thị MH1: MH danh sách chức năng Quản lý danh bạ

##### MH1: MH danh sách chức năng Quản lý danh bạ
 | | 

 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Click label chức năng: Danh bạ thụ hưởng hoặc Danh bạ hóa đơn | 
MB Client
 | 
Tham khảo chức năng tương ứng: Danh bạ thụ hưởng, Danh bạ hóa đơn

---

### 21.2. MB_Danh bạ hóa đơn

> **Page ID:** `29904385` · **Version:** 54
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29904385

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
23/08/2023 
 | A | Bùi Thanh Thảo | V.1.0.0 | 
Tạo mới
 | 

 | 
 
 | M | Lê Thị Hồng | V.2.0.0 | 
Cập nhật

• Bổ sung chức năng Đăng ký thanh toán tự động | 

 | 
 
 | M | Lê Thị Hồng | V.2.0.0 | 
Cập nhật : 

• Bổ sung logic chỉ hiển thị trường " Đăng ký nhận thông báo cước" nếu NCC TTHĐ được cấu hình cho phép đăng ký nhận cước từ BE
• Bổ sung logic check nếu nhà cung cấp của danh danh bạ đã lưu không được cấu hình cho phép đăng ký thanh toán tự động → Thì không cho phép đăng ký thanh toán tự động | 

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, App Client, App Server, Vnpay Billing system
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công.
• Kết quả mong muốn:
• KH có thể xem chi tiết, sửa, xóa, thanh toán hóa đơn được lưu trong danh bạ
#### 2/ Luồng sơ đồ

#### 2/ Luồng màn hình

MH1.1 Danh bạ hóa đơn trống

##### MH1.2: Danh bạ hóa đơn khi có danh bạ đã lưu - Bổ sung thêm chức năng Đăng ký thanh toán tự động

##### MH2.1: Thêm mới danh bạ

##### MH2.2: Thêm mới danh bạ (khi cấu hình ở BE module Dịch vụ có tích chọn icon danh bạ)

##### MH3: Xem chi tiết danh bạ hóa đơn

##### MH4.1: Xóa danh bạ

##### MH4.2: Thông báo xóa danh bạ

##### MH 5. Luồng Xác thực đăng ký thanh toán hóa đơn tự động

##### 3/ Mô tả màn hình

##### MH1: Danh sách danh bạ hóa đơn
 | | 
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: DANH BẠ HÓA ĐƠN

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | 
Icon Home
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Home, hiển thị màn hình chính của ứng dụng 

 | 4 | Xóa danh bạ | Label | Click | -- | -- | 
Click vào hiển thị ô tích chọn trên các danh bạ được lưu, cho phép khách hàng tích chọn để xóa một hoặc nhiều danh bạ 

Ẩn button "Thêm mới", thay bằng button "Xóa n danh bạ"

 | 5 | 
Ô tìm kiếm
 | 
Textbox
 | 
Text
 | -- | 200 | 
Nhập ký tự bất kỳ

Tìm kiếm gần đúng theo: Tên gợi nhớ, Mã khách hàng, Tên dịch vụ, Tên nhà cung cấp.

Khi fill text vào ô danh bạ, hiển thị icon x, cho phép xóa ký tự nhập

 | 6 | Tên dịch vụ  | Label | ReadOnly | -- | -- | Hiển thị label tên dịch vụ của các hóa đơn trong nhóm đã lưu
 | 7 | Danh sách danh bạ hóa đơn
 | 8 | 
Danh sách danh bạ
 | 
View
 | 
Click
 | -- | -- | 
Nếu danh sách trống: Hiển thị label “Danh bạ hóa đơn trống. Quý khách vui lòng nhấn vào đây để thêm mới.” trên màn hình.

Các danh bạ sắp xếp theo thời gian tạo từ mới tới cũ

Mỗi Danh bạ hóa đơn, hiển thị các thông tin:

• Icon Dịch vụ: Hiển thị Icon Dịch vụ đã lưu trên hệ thống
• Tên gợi nhớ của Danh bạ đã lưu
• Nhà cung cấp
• Mã khách hàng
• Icon biểu tượng đăng ký nhận cước hàng tháng: ReadOnly, Chỉ hiển thị nếu danh bạ có đăng ký nhận thông báo cước.
• Cho phép click vào 1 danh bạ để  xem chi tiết.
 | 9 | 
Đăng ký thanh toán tự động
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
• Hiển thị nút Đăng ký thanh toán tự động với các danh bạ hóa đơn chưa Đăng ký thanh toán tự động và dịch vụ được phép đăng ký tự động. Bấm vào "Đăng lý thanh toán tự động" → Hiển thị MH xác thực giao dịch <Tham khảo Logic xử lý>
• Hiển thị label "Đã đăng ký thanh toán tự động" với các hóa đơn đã đăng ký thanh toán tự động thành công
 | 10 | 
Nút Thêm mới
 | 
Button
 | 
Click
 | -- | -- | 
Hiển thị MH chức năng Thêm mới danh bạ hóa đơn khi nhấn button.

 (Tham khảo logic xử lý)

##### MH2: Thêm mới Danh bạ hóa đơn
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: THÊM MỚI DANH BẠ HÓA ĐƠN

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | 
Icon Home
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Home, hiển thị màn hình chính của ứng dụng

 | 4 | 
Dịch vụ
 | 
Combobox
 | 
List
 | Có | -- | 
Danh sách dịch vụ lấy từ bảng Dịch vụ ở BE

Hiển thị danh sách dịch vụ theo thứ tự do server trả về

Cho phép chọn 1 dịch vụ từ danh sách và lựa chọn thay đổi

 | 
5
 | 
Nhà cung cấp
 | 
Combobox
 | 
List
 | Có | -- | 
Chỉ hiển thị trường Nhà cung cấp sau khi khách hàng đã chọn Dịch vụ

Danh sách nhà cung cấp lấy từ Bảng Nhà cung cấp theo dịch vụ đã chọn ở BE

Hiển thị các Nhà cung cấp theo thứ tự do server trả về

Cho phép chọn 1 nhà cung cấp và lựa chọn thay đổi

 | 6 | Mã khách hàng | Textbox | Input | Có | 30 | 
Chỉ hiển thị Mã khách hàng với label tương ứng với NCC khi đã chọn xong nhà cung cấp

Cho phép nhập số, chữ không dấu, ký tự đặc biệt

Khi tại bảng Nhà cung cấp trên BE có tích chọn Icon Danh bạ, cấu hình danh bạ cho khách hàng lựa chọn

Hiển thị SĐT gợi ý theo danh bạ điện thoại, dạng list <Tham khảo mockup 2.2>

Sau khi nhập xong, hiển thị tên theo số điện thoại lưu tại danh bạ

 | 6 | Tên gợi nhớ | Textbox | Input | Có | 50 | Cho phép nhập tên gợi nhớ dạng Freetext, cho phép nhập có dấu
 | 7 | 
Nhận thông báo cước hàng tháng
 | 
ON/OFF
 | 
Switch
 | -- | -- | 
Chỉ hiển thị trường Nhận thông báo cước hàng tháng  sau khi chọn NCC, mà NCC này được cấu hình tại BE là " Cho phép đăng ký nhận thông báo nhắc nợ cước"

Mặc định ở trạng thái OFF

Cho phép chuyển trạng thái ON/OFF

 | 8 | 
Nút “THÊM MỚI”
 | 
Button
 | 
Click
 | -- | -- | 
 Mặc định Enable

Tham khảo logic xử lý

##### MH3: Xem Chi tiết Danh bạ hóa đơn
 | | TT | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: [Tên dịch vụ]

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | 
Icon Home
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Home, hiển thị màn hình chính của ứng dụng 

 | 4 | Nhà cung cấp | Textbox | ReadOnly | -- | -- | 
Hiển thị tên Nhà cung cấp của danh bạ hóa đơn đã chọn

 | 5 | Mã khách hàng | Textbox | ReadOnly | -- | -- | 
Hiển thị Mã khách hàng của danh bạ hóa đơn đã chọn

 | 6 | Tên gợi nhớ | Textbox | Input | -- | 50 | 
Hiển thị Tên gợi nhớ tương ứng của danh bạ hóa đơn đã chọn

Cho phép chỉnh sửa

Cho phép nhập Freetext, tiếng Việt có dấu

 | 7 | Nhận thông báo cước định kỳ | Toggle | Click | -- | -- | 
Hiển thị nút Switch ON/OFF theo thông tin server trả về tại mid 35- Lấy danh sách danh bạ thụ hưởng như sau:
 | 
 | Trường hợp | Hiển thị Switch nhận thông báo cước
 | 1 | 
receiveNotice = 0 + isReceiveNotice= 1

(KH chưa đăng ký nhắc nợ + Nhà cung cấp này có cho phép đăng ký nhắc nợ)
 | Hiển thị trường Nhận thông báo cước định kỳ = OFF
 | 2 | 
receiveNotice = 0 + isReceiveNotice= 0

(KH chưa đăng ký nhắc nợ + Nhà cung cấp này không cho phép đăng ký nhắc nợ)
 | Không hiển thị trường Nhận thông báo cước định kỳ
 | 3 | 
receiveNotice = 1+ isReceiveNotice= 1

(KH đã đăng ký nhắc nợ + Nhà cung cấp này có cho phép đăng ký nhắc nợ)
 | Hiển thị trường Nhận thông báo cước định kỳ = ON
 | 4 | 
receiveNotice = 1 + isReceiveNotice= 0

(KH đã đăng ký nhắc nợ + Nhà cung cấp này không cho phép đăng ký nhắc nợ)
 | Không hiển thị trường Nhận thông báo cước định kỳ

 | 8 | 
Nút “THANH TOÁN”
 | 
Button
 | 
Click
 | -- | -- | 
Click vào button, tự động fill thông tin đã lưu danh bạ (Tên dịch vụ, tên nhà cung cấp, Mã khách hàng vào màn hình khởi tạo thanh toán hóa đơn

<Tham khảm logic xử lý>

 | 9 | Nút "CẬP NHẬT" | 
Button
 | 
Click
 | -- | -- | 
Tiến hành lưu thay đổi của Danh bạ hóa đơn

<Tham khảm logic xử lý>

##### MH4.1: Xóa Danh bạ hóa đơn
 | | 

 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: DANH BẠ HÓA ĐƠN

 | 2 | Label Hủy xóa danh bạ | Label | Click | -- | -- | Hiển thị lại màn hình Danh bạ hóa đơn (như trước khi nhấn Xóa danh bạ) khi nhấn Hủy xóa danh bạ
 | 3 | 
Ô tìm kiếm
 | 
Textbox
 | 
Text
 | -- | 200 | 
Nhập ký tự bất kỳ

Tìm kiếm gần đúng theo: Tên gợi nhớ, Mã khách hàng, Tên dịch vụ, Tên nhà cung cấp.

Khi fill text vào ô danh bạ, hiển thị icon x, cho phép xóa ký tự nhập

 | 4 | Tên dịch vụ  | Label | ReadOnly | -- | -- | Hiển thị label tên dịch vụ của các hóa đơn trong nhóm đã lưu
 | 5 | 
Danh sách danh bạ
 | 
View
 | 
Click
 | -- | -- | 
Nếu danh sách trống: Hiển thị label “Danh bạ hóa đơn trống. Quý khách vui lòng nhấn vào đây để thêm mới.” trên màn hình.

Các danh bạ sắp xếp theo thời gian tạo từ mới tới cũ

Mỗi Danh bạ hóa đơn, hiển thị các thông tin:

• Icon Dịch vụ: Hiển thị Icon Dịch vụ đã lưu trên hệ thống
• Tên gợi nhớ của Danh bạ đã lưu
• Nhà cung cấp
• Mã khách hàng
• Icon biểu tượng đăng ký nhận cước hàng tháng: ReadOnly, Chỉ hiển thị nếu danh bạ có đăng ký nhận thông báo cước.
• Cho phép click vào 1 danh bạ để  xem chi tiết.
 | 6 | 
Nút "Xóa [n] danh bạ thanh toán"
 | 
Button
 | 
Click
 | -- | -- | 
Hiển thị số lượng Danh bạ được tích chọn để xóa trên Nút Xóa

Tham khảo logic xử lý

##### MH4.2: Popup thông báo xóa danh bạ
 | | 

 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Thông báo

"Quý khách chắc chắn muốn xóa (x) danh bạ đã chọn khỏi danh bạ hóa đơn?"

 | 2 | Hủy | Button | Click | -- | -- | <Tham khảo logic xử lý>
 | 3 | Đồng ý | Button | Click | -- | -- | <Tham khảo logic xử lý>

#### 4/ Luồng xử lý

##### MH1: Danh sách Danh bạ hóa đơn
 | TT | Thao tác | Tác nhân | Mô tả
 | 
1
 | 
Truy cập chức năng “Danh bạ hóa đơn”
 | 
App Client
 | 
Gửi yêu cầu lấy danh sách Danh bạ hóa đơn đã lưu sang App server

 | 
App Server
 | 
Truy vấn thông tin Danh bạ hóa đơn, Sắp xếp theo thời gian tạo từ mới tới cũ

• Không thành công: Trả về mã lỗi tương ứng: | TT | Trường hợp lỗi | Tác nhân | Nội dung
 | 1 | TimeOut | App server | Yêu cầu tạm thời bị gián đoạn. Quý khách vui lòng thực hiện lại sau.

• Thành công: Trả về popup thông báo: "Danh bạ hóa đơn trống. Quý khách vui lòng nhấn vào đây để thêm mới." khi danh bạ trống
• Trả về danh sách danh bạ hóa đơn khi có danh bạ + Cờ đánh dấu danh bạ đã đăng ký tự động chưa?
 | 
App Client
 | 
Nhận kết quả:

• Thất bại: Hiển thị thông báo lỗi tương ứng (lỗi giao tiếp hệ thống).
• Thành công: 
• Nếu có danh bạ: Hiển thị MH danh sách danh bạ hóa đơn
- Nếu Danh bạ đã đăng ký hóa đơn tự động: Hiển thị Label "Đã đăng ký thanh toán tự động"

- Nếu Danh bạ chưa đăng ký hóa đơn tự động: Hiển thị nút "Đăng ký"

• 
• Nếu không có danh bạ: Hiển thị MH danh sách danh bạ trống với nội dung thông báo tương ứng
 | 
2
 | 
Nhấn 1 danh bạ
 | 
App Client
 | 
Hiển thị màn hình chi tiết thông tin danh bạ

 | 
3

 | 
Nhập từ khóa tìm kiếm
 | 
App Client
 | 
Thực hiện tìm kiếm theo từ khóa nhập. Tìm kiếm gần đúng theo: Tên danh bạ (Tên gợi nhớ), Mã khách hàng, Tên dịch vụ, Tên nhà cung cấp:

• Nếu có kết quả hợp lệ: Hiển thị đúng kết quả theo từ khóa nhập.
• Nếu không có kết quả hợp lệ: Hiển thị label thông báo "Không có kết quả tìm kiếm. Quý khách vui lòng kiểm tra lại"
 | 
Nhấn “x” tại form tìm kiếm sau khi nhập
 | 
App Client
 | 
Thực hiện xóa toàn bộ các ký tự đã nhập. Hiển thị tất cả các Danh bạ thanh toán

 | 
3
 | 
Nhấn Icon Thêm mới
 | 
App Client
 | 
Hiển thị màn hình Thêm mới danh bạ hóa đơn (MH2)

 | 
4
 | 
Nhấn label "Xóa danh bạ"
 | 
App Client
 | 
Hiển thị ô tích chọn trong mỗi danh bạ trên danh sách danh bạ, đồng thời hiển thị:

• Label Hủy xóa danh bạ
• Button Xóa n danh bạ
(tham khảo MH4)

Sau khi nhấn button Xóa n danh bạ, hiển thị thông báo: "Quý khách chắc chắn muốn xóa (x) danh bạ đã chọn khỏi danh bạ hóa đơn?" và 2 button "Hủy" và "Đồng ý".

• Nhấn Hủy, quay lại màn hình Danh bạ hóa đơn ban dầu
• Nhấn Đồng ý, thực hiện quay lại MH Danh bạ hóa đơn với danh sách danh bạ mới được cập nhật từ App server

 | 5

 | Nhấn label "Xóa danh bạ" | App Client | 
Hiển thị ô tích chọn tại mỗi danh bạ trên MH Danh bạ hóa đơn, với label "Hủy xóa danh bạ" và button "Xóa n danh bạ"

 | Nhấn chọn "Hủy xóa danh bạ" | App Client | Hiển thị MH Danh bạ thanh toán như MH1
 | Nhấn chọn button "Xóa n danh bạ" | App Client | 
1/ Thực hiển kiểm tra:

• Không hợp lệ: Cấu hình và hiển thị popup thông báo: | TT | Trường hợp lỗi | Tác nhân | Nội dung
 | 1 | Không có danh bạ nào được chọn | App Client | Quý khách vui lòng chọn danh bạ cần xóa

• Hợp lệ: Hiển thị popup thông báo: "Quý khách chắc chắn muốn xóa (x) danh bạ đã chọn khỏi danh bạ hóa đơn?" và hai button "Hủy" và "Đồng ý"
• Nút Hủy: Nhấn nút này, tắt thông báo và hiển thị màn hình đang thao tác trước đó.
• Nút Đồng ý: Nhấn nút này, ứng dụng gửi yêu cầu Xóa danh sách danh bạ sang MB Server.
 | App server | 
1/ Thực hiện xóa danh bạ:

• Không thành công: Trả về mã lỗi tương ứng: | TT | Trường hợp lỗi | Tác nhân | Nội dung
 | 1 | TimeOut | App server | Yêu cầu tạm thời bị gián đoạn. Quý khách vui lòng thực hiện lại sau.

• Thành công: Thực hiện xóa n danh bạ và cấu hình hiển thị popup thông báo: "Đã xóa danh bạ hóa đơn thành công" hiển thị trong n giây và trả kết quả xóa thành công cho Client
 | App Client | 
1/ Nhận kết quả từ MB server:

• Không thành công: Hiển thị thông báo lỗi tương ứng
• Thành công: Thực hiện xóa danh bạ tại Client và Hiển thị thông báo xóa danh bạ thành công.
 | 6 | Nhấn chọn Đăng ký thanh toán tự động | App Client | 
Gửi yêu cầu truy vấn danh sách tài khoản nguồn tới MB Server

 | 
 |   | MB Server | 
Nhận và gửi yêu cầu truy vấn danh sách tài khoản nguồn sang Bank server

 | 
 |   | Bank | 
Xử lý truy vấn danh sách tài khoản nguồn hợp lệ và trả kết quả

 | 
 |   | MB Server | 
Nhận kết quả từ Bank và phản hồi cho MB Client

 | 
 |   | MB Client | 
Nhận kết quả từ MB Server

• Timeout: Hiển thị thông báo timeout
• Không thành công:  |   | Trường hợp | Mô tả | Xử lý
 | 1 | Lỗi không lấy được danh sách tài khoản từ Bank | Hiển thị thông báo " Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại sau" | Đóng câu thông báo, giữ nguyên màn hình
 | 2 | Trường hợp không có tài khoản thanh toán (đã tất toán hết tài khoản thanh toán) | 
Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại
 | Đóng câu thông báo, giữ nguyên màn hình

• Thành công: Điều hướng sang màn hình khởi tạo Đăng ký thanh toán tự động (của cách 1): 
- Thông tin tài khoản nguồn hợp lệ (Mặc định là tài khoản thanh toán - Nếu không phải là tài khoản thanh toán thì lấy tài khoản đầu tiên trong danh sách trả về), bao gồm: số tài khoản, số dư khả dụng + đơn vị tiền tệ VNĐ.

- Đồng thời fill sẵn thông tin từ danh bạ hóa đơn đã lưu sang MH khởi tạo đăng ký thanh toán tự động bao gồm:

+ Dịch vụ (Không cho phép sửa)

+ Nhà cung cấp (Không cho phép sửa)

+ Mã khách hàng (Không cho phép sửa)

 | 
 |   | MB Server | 
Kiểm tra dịch vụ thanh toán hóa đơn tại danh bạ có được đăng ký thanh toán tự động không

• Không thành công: Trả kết quả cho Client |   | Trường hợp | Mô tả | Xử lý
 | 1 | Dich vụ thanh toán hóa đơn của danh bạ đã lưu không được cấu hình cho phép đăng ký thanh toán tự động | Dịch vụ này không được phép đăng ký thanh toán tự động | Đóng câu thông báo, giữ

> ⚠️ *Nội dung đã cắt ngắn (19139 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 21.3. MB_Thanh toán hóa đơn

> **Page ID:** `29889388` · **Version:** 131
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29889388

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
2020 
 | A | Bùi Thị Thanh Thảo | 
 | 
Tạo mới
 |  V.1.0.0
 | 
 
 | M | Lê Thị Hồng |  V.1.0.0 | 
Bổ sung logic tại Popup Lưu danh bạ hóa đơn ở MH kết quả giao dịch:

• Toggle đăng ký Nhận thông báo cước hàng tháng (Chỉ hiển thị nếu Nhà cung cấp cấu hình trên BE là : Có cho phép đăng ký nhận thông báo nhắc nợ) |  V.1.0.1
 | 
 
 | M | ThaoCY |  V.1.0.1 | 
Bổ sung logic tính phí giao dịch từ nhà cung cấp (do billing truyền sang)
 |  V.1.0.2

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, App Client, App server, Bank server, Vnpay Billing system
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công.
• KH thuộc gói dịch vụ được phép sử dụng chức năng này.
• KH có tài khoản nguồn hợp lệ để thực hiện chức năng này.
• Kết quả mong muốn:
• KH thực hiện giao dịch thành công. 
• Tài khoản nguồn được trừ tiền đúng bằng số tiền sau Phí giao dịch và thuế
• Thông tin hóa đơn của KH được thanh toán/ gạch nợ thành công.
• Remark: TTHD [Tên dịch vụ] của [Nhà cung cấp] với mã KH[Số mã KH] cho kỳ cước[kỳ cước]. Cụm "cho kỳ cước[kỳ cước]" không có không hiển thị
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

##### MH0: MH Danh sách dịch vụ thanh toán hóa đơn

##### 

##### MH1: Khởi tạo (Thanh toán tổng tiền)

##### MH2: Xác nhận giao dịch

##### MH3: Xác thực giao dịch

##### MH4.1: Kết quả giao dịch

##### MH4.2: Nhập tên gợi nhớ khi lưu danh bạ

##### Nhóm màn hình khởi tạo đặc biệt

##### MH5: MH khởi tạo nhập số tiền

##### 

##### MH6: MH khởi tạo tổng tiền + Nhập số tiền

##### MH7.1: MH khởi tạo chọn gói cước từ các gói cước trả về sau khi nhập thông tin label Mã khách hàng - K+

##### MH7.2: MH khởi tạo chọn gói cước từ các gói cước trả về sau khi nhập thông tin label Mã khách hàng - Mobi TV

##### Nhóm màn hình xác nhận đặc biệt + kết quả đặc biệt

##### MH8: MH Xác nhận tổng tiền + Nhập số tiền (khi chọn Nhập số tiền)

##### MH9: MH Xác nhận tổng tiền + Nhập số tiền (khi chọn Tổng tiền)

##### MH10.1: MH Xác nhận (chọn gói cước từ các gói cước trả về sau khi nhập thông tin label Mã khách hàng ở MH khởi tạo) - K+

##### MH10: MH Xác nhận (chọn gói cước từ các gói cước trả về sau khi nhập thông tin label Mã khách hàng ở MH khởi tạo) - MobiTV

##### MH11.1: Màn hình Xác nhận thanh toán vé máy bay

##### MH11.2: Màn hình Xác nhận thanh toán vé máy bay (popup thông tin)

##### MH12: MH kết quả tổng tiền + Nhập số tiền 

##### MH13.1: MH kết quả (chọn gói cước từ các gói cước trả về sau khi nhập thông tin label Mã khách hàng ở MH khởi tạo)

##### MH13.2: MH kết quả (chọn gói cước từ các gói cước trả về sau khi nhập thông tin label Mã khách hàng ở MH khởi tạo) - MobiTV

##### MH14: MH kết quả (Thanh toán vé máy bay)

##### MH 15.1: MH Chọn danh bạ khi có cả Danh bạ hóa đơn và Danh bạ điện thoại (Khi chọn Danh bạ hóa đơn)

##### MH 15.2: MH Chọn danh bạ khi có cả Danh bạ hóa đơn và Danh bạ điện thoại (Khi chọn danh bạ điện thoại)

##### MH0: MH Danh sách dịch vụ Thanh toán
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: THANH TOÁN HÓA ĐƠN

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | Dịch vụ thanh toán hóa đơn | Icon | Click | -- | -- | 
Hiển thị danh sách dịch vụ do server trả về

Thứ tự sắp xếp theo Mockup

Thông tin bản ghi gồm: Icon các dịch vụ, Tên dịch vụ

Cho phép click vào từng dịch vụ để hiển thị màn hình khởi tạo thanh toán hóa đơn của dịch vụ tương ứng

 | 4 | Danh bạ hóa đơn | Icon | Click | -- | -- | Hiển thị Danh bạ hóa đơn 

##### MH1: Khởi tạo
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: [Tên dịch vụ]

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | 
Icon Danh bạ hóa đơn
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Icon Danh bạ hóa đơn, hiển thị màn hình danh bạ hóa đơn với các danh bạ đã lưu thuộc dịch vụ đã chọn

Nếu ở BE phần Dịch vụ TTHĐ có tích chọn Gợi ý số điện thoại, hiển thị danh bạ điện thoại

Nếu ở BE có tích chọn cả Lưu danh bạ và Gợi ý số điện thoại thì hiển thị cả hai danh bạ, khi click vào icon danh bạ ở MH 

 | 4 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | Yes | -- | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

Mặc định TK khách hàng đang xem vấn tin, khi KH chọn TTHĐ từ chức năng Vấn tin TK

 | 6 | 
Nhà cung cấp
 | 
Combobox
 | 
List
 | Yes | -- | 
• Hiển thị danh sách nhà cung cấp theo Dịch vụ đã chọn, nếu khách hàng không chọn, mặc định nhà cung cấp đầu tiên trả về từ server
• Hiển thị bổ sung cụm tìm kiếm nếu danh sách NCC > 5 Cho phép tìm kiếm nhà cung cấp trong danh sách
Lưu ý: Nếu nhà cung cấp chỉ có 1 giá trị, fill sẵn giá trị vào ô Nhà cung cấp

 | 8 | 
Các trường dữ liệu tiếp theo sau khi chọn Nhà cung cấp được hiển thị theo nguyên tắc:

1/ Label textbox Mã khách hàng: Mặc định label Mã khách hàng tương ứng với nhà cung cấp trả về đầu tiên theo danh sách, cho phép thay đổi khi KH chọn lại NCC

2/ Các trường dữ liệu tiếp theo dựa vào Hình thức thanh toán của nhà cung cấp đã cấu hình trên BE module Nhà cung cấp:

• Thanh toán tất cả: Texbox Mã khách hàng: Là một trong các nội dung sau: Mã khách hàng, Số điện thoại, Mã đặt chỗ, Mã thanh toán, Mã học viên,...
• Thanh toán nhập số tiền: Textbox Mã khách hàng, Textbox Số tiền
• Thanh toán tất cả + nhập số tiền: Textbox Số điện thoại, icon Danh bạ điện thoại, Combobox Hình thức thanh toán, Textbox Số tiền (nếu có)
 | 
##### Thanh toán Tất cả

 | Mã khách hàng | Textbox | Input | Yes | 30 | 
Lấy từ trường Label mã khách hàng trên DB, bảng Nhà cung cấp TTHĐ

Cho phép nhập chữ, số, các ký tự đặc biệt

Icon danh bạ điện thoại: Hiển thị khi bảng Dịch vụ trên BE có cấu hình chọn Gợi ý SĐT

Sau khi nhập từ 2 số trở lên khi chức năng có gợi ý danh bạ, hiển thị gợi ý

Sau khi nhập/ chọn xong số điện thoại, hiển thị tên theo danh bạ (nếu có) nếu có gợi ý số điện thoại

 | 
##### Thanh toán tất cả - Chọn gói cước (nếu có)

 | Gói cước (nếu có) | 
Collapse
 | 
Select
 | 
--
 | 
--
 | 
Hiển thị tất cả các gói cước NCC DV trả về

Mặc định chọn kỳ hạn cước đầu của gói cước đầu, hiển thị mặc định mở rộng gói cước đầu.

Có thể nhấn chọn để mở rộng hoặc thu hẹp lại 1 gói cước, các gói còn lại để dạng thu gọn

 | Chi tiết gói cước | 
Checkbox
 | 
Check
 | 
--
 | 
--
 | 
Hiển thị danh sách kỳ hạn chi tiết theo từng gói cước với các thông tin như sau:

• [Thời gian][Đơn vị; ngày/ tuần/ tháng]
• Số tiền tương ứng với kỳ hạn của gói cước
• Loại tiền
• Hiển thị ô tích chọn tại đầu mỗi thời hạn cước, cho phép khách hàng tích chọn và thay đổi.
Quy định về diễn giải đơn vị của kỳ hạn cước:

• AD/ RD: Ngày
• AW/ RW: Tuần
• AM/ RM hoặc để trống: Tháng
Tại một thời điểm chỉ được phép chọn một thời hạn cước tại một gói, khi khách hàng chọn thời hạn mới, thời hạn cũ bị hủy tích chọn.

 | Ngày hết hạn dịch vụv (nếu có) | Label | ReadOnly | -- | -- | Hiển thị Ngày hết hạn của gói cước khách hàng, theo dữ liệu NCC trả về
 | 
##### Thanh toán nhập số tiền

 | Mã khách hàng | Textbox | Input | Yes | 30 | <Như trên>
 | Số tiền | Textbox | Number | Yes | 12 | 
Nhập số, có gợi ý số tiền nhập theo nguyên tắc: Hiển thị 3 gợi ý, các số sau hơn số trước 10 lần. Số tiền gợi ý đầu được cấu trúc như sau:

Khi nhập một số: Thêm 4 số 0 phía sau

Khi nhập 2 số: Thêm 3 số 0 phía sau

Khi nhập 3 số: Thêm 2 số 0 phía sau

Khi nhập 4 số thêm 1 số 0 phía sau

Nhập từ [5;7]: Thêm 1 số 0 phía sau

Từ 8 số chở lên: Không hiển thị gợi ý số tiền.

Lưu ý: Khi nhập 6 số chỉ hiện thị 2 gợi ý, khi nhập 7 số hiển thị 1 gợi ý duy nhất.

 | 
##### Thanh toán tất cả + nhập số tiền

 | Mã khách hàng | Textbox | Input | Yes | 30 | <Như trên>
 | Hình thức thanh toán | Combobox | Click | Yes | -- | 
Hiển thị trường này khi trường Hình thức thanh toán trên DB bảng Nhà cung cấp TTHĐ quy định được chọn gồm cả 2 giá trị: Toàn bộ cước, Nhập số tiền

Khi KH chọn từ combobox Hình thức thanh toán là Nhập số tiền, hiển thị thêm textbox Số tiền

Mặc đinh hiển thị: Toàn bộ cước

Cho phép chọn giá trị khác

 | Số tiền (Khi chọn hình thức thanh toán là Nhập số tiền) | Textbox | Number | Yes | 12 | 
<Như trên>

 | 9 | 
Tiếp tục
 | 
Button
 | 
Click
 | Yes | -- | 
Mặc định ở trạng thái Enable

<Tham khảo logic xử lý>

##### MH2: MH Xác nhận
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: XÁC NHẬN GIAO DỊCH

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó với các giá trị giữ nguyên.

 | 3 | 
Icon Home
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Home, hiển thị màn hình chính của ứng dụng (landing page 1)

 | 
 | Ghi chú | Label | ReadOnly | -- | -- | Hiển thị: "Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo"
 | 4 | 
Tài khoản nguồn
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Dữ liệu từ màn hình trước

 | 5 | 
Dịch vụ
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Dữ liệu từ màn hình trước

 | 6 | 
Các thông tin đã nhập/chọn tại màn hình Khởi tạo
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Dữ liệu từ màn hình trước (Chi tiết xem trên mockup)

• Nhà cung cấp
• Mã khách hàng
• Số tiền thanh toán (nếu có)
• Hình thức thanh toán
• Gói cước (nếu có)
(Các thông tin tùy theo từng Loại dịch vụ  - Tham khảo tại mô tả màn hình Khởi tạo)

 | 7 | 
Các thông tin hóa đơn truy vấn được từ hệ thống Billing
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Dữ liệu do Vnpay Billing system trả về (Chi tiết xem trên mockup):

• Tên khách hàng (Nếu có): Với DV Thanh toán vé máy bay, hiển thị tên người đặt vé
• Số tiền thanh toán (Nếu có): Che thông tin số tiền khi KH có hình thức thanh toán là tất cả và ncc có cấu hình tích chọn che cước ở BE
• Phí giao dịch và thuế (Nếu có):
• Chỉ hiển thị khi số tiền >0
• MB Server trả về theo công thức = (Phí giao dịch theo nhà cung cấp, do hệ thống Billing trả về) + Phí theo dịch vụ của gói dịch vụ khai báo tại BackOffice
• Ngày hết hạn dịch vụ (nếu có)
• Thông tin chuyến bay: Xem thêm: (Áp dụng với MH Thanh toán vé máy bay), Click Xem thêm hiển thị popup MH 11.2. Lưu ý: Thông tin nào không có không hiển thị)
• Popup Thông tin chuyến bay: Gồm Icon Đóng để quay lại MH Xác nhận giao dịch 11.1, Nội dung "Thông tin chuyến bay" (Tương tự MH Mockup)
 | 12 | 
Hình thức xác thực:

<Tham khảo  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)>

 | 13 | 
Nút “Xác nhận”
 | 
Button
 | 
Click
 | -- | -- | 
Mặc định Enable
<Tham khảo logic xử lý>

##### MH3: Xác thực giao dịch

Tham khảo URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH4.1: Kết quả giao dịch
 | | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | Tiêu đề màn hình | Label | ReadOnly | -- | -- | Hiển thị: Kết quả giao dịch
 | 2 | Logo Bank | Label  | ReadOnly | -- | -- | Hiển thị Logo Co-opBank
 | 3 | Tên ngân hàng | Label | ReadOnly | -- | -- | Hiển thị tên Ngân hàng Co-opBank bên cạnh logo Bank
 | 4 | Icon giao dịch thành công | Label | ReadOnly | -- | -- | Hiển thị icon giao dịch thành công
 | 5 | Tiêu đề | Label | ReadOnly | -- | -- | Tiêu đề: Thanh toán hóa đơn thành công
 | 6 | Số tiền giao dịch | Label | ReadOnly | -- | -- | Hiển thị số tiền thanh toán gốc (không bao gồm thuế phí) 
 | 7 | Thời gian giao dịch | Label | ReadOnly | -- | -- | Dữ liệu do App server trả về, định dạng: dd/mm/yyyy hh:mm
 | 8 | Dịch vụ | Label | ReadOnly | -- | -- | Hiển thị dịch vụ đã chọn thanh toán
 | 9 | Nhà cung cấp | Label | ReadOnly | -- | -- | Hiển thị Tên nhà cung cấp đã chọn thanh toán
 | 10 | Hình thức thanh toán (Hiển thị với các dịch vụ Cước di động trả sau của Viettel) (nếu có) | Label | ReadOnly | -- | -- | Hiển thị Hình thức thanh toán đã chọn
 | 11 | Label mã khách hàng | Label | ReadOnly | -- | -- | Hiển thị Nội dung Label mã khách hàng đã nhập chọn
 | 12 | Tên khách hàng | Label | ReadOnly | -- | -- | Hiển thị Tên khách hàng tương ứng
 | 13 | Gói cước (nếu có) | Label | ReadOnly | -- | -- | Hiển thị gói cước của KH đã mua
 | 14 | Mã giao dịch | Label | ReadOnly | -- | -- | Hiển thị mã giao dịch được sinh bởi Bank server khi thực hiện trừ tiền thành công tại Bank
 | 15 | Lưu danh bạ hóa đơn | Icon | Click | -- | -- | 
Hiển thị Popup Lưu danh bạ

Hiển thị với dịch vụ có chức năng Lưu danh bạ được cấu hình trên BE

 | 16 | 
Icon Chia sẻ
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn Chia sẻ, Hiển thị popup lựa chọn kênh chia sẻ của thiết bị đã cài đặt

<Logic Tham khảo tính năng Chia sẻ của ứng dụng>

 | 17 | 
Icon Lưu ảnh
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn Image, Lưu ảnh về thư viện hình ảnh của thiết bị

 | 18 | 
Nút “Tạo giao dịch mới”
 | 
Button
 | 
Click
 | -- | -- | 
Nhấn Tạo giao dịch mới, hiển thị màn hình khởi tạo giao dịch mới của thanh toán hóa đơn tương ứng (tài khoản nguồn được cập nhật số dư).

##### MH4.2: Popup lưu danh bạ hóa đơn
 | | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | Tiêu đề màn hình | Label | ReadOnly | -- | -- | Hiển thị: Lưu danh bạ hóa đơn
 | 2 | Tên gợi nhớ | Textbox | Input | Có | 50 | Cho phép nhập Freetext
 | 3 | Nhận thông báo cước hàng tháng | Toggle | Click | -- | -- | On/ Off chức năng 
 | 4 | Hoàn thành | Button | Click | -- | -- | <Tham khảo logic xử lý>

##### MH 15: MH Chọn danh bạ
 | | 

 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | 
Tiêu đề
 | 
Icon
 | 
Click
 | -- | -- | 
Tùy thuộc cấu hình ở BE có lựa chọn "Gợi ý số điện thoại"  và "Lưu danh bạ". Hiển thị gồm 1/2 tab hoặc cả 2 tab sau:

• Danh bạ hóa đơn
• Danh bạ điện thoại
 | 2 | Icon Hủy | Icon | Click | -- | -- | Quay lại MH trước
 | 3 | 
Ô tìm kiếm
 | 
Textbox
 | 
Text
 | -- | 200 | 
Nhập ký tự bất kỳ

Tìm kiếm gần đúng theo: Tên gợi nhớ, Mã khách hàng, Tên dịch vụ, Tên nhà cung cấp.

Khi fill text vào ô danh bạ, hiển thị icon x, cho phép xóa ký tự nhập

 | 4 | 
Danh sách danh bạ
 | 
View
 | 
Click
 | -- | -- | 
Nếu danh sách trống: Hiển thị label “Quý khách chưa có danh bạ hóa đơn” hoặc “Quý khách chưa có danh bạ điện thoại” trên màn hình.

Các danh bạ sắp xếp theo thời gian tạo từ mới tới cũ

Mỗi Danh bạ điện thoại, hiển thị các thông tin:

• Icon
• Tên gợi nhớ của Danh bạ đã lưu
• Số điện thoại
Mỗi danh bạ hóa đơn hiển thị:

• Icon
• Tên gợi nhớ
• Nhà cung cấp
• Số điện thoại
Cho phép click vào 1 danh bạ để  chọn danh bạ

#### 4/ Luồng xử lý

##### MH0: MH Danh sách dịch vụ thanh toán hóa đơn
 | TT | Thao tác | Tác nhân | Mô t

> ⚠️ *Nội dung đã cắt ngắn (29212 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 21.4. Nhận thông báo cước hóa đơn

> **Page ID:** `29904600` · **Version:** 17
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29904600

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, App Client, App server, Vnpay Billing system, OTT server
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công.
• KH thuộc gói dịch vụ được phép sử dụng chức năng này.
• KH có tài khoản nguồn hợp lệ (cấu hình rule tại Backend) để thực hiện chức năng này.
• Kết quả mong muốn:
• KH có thể đăng ký, hủy đăng ký Nhận thông báo cước hóa đơn cho các loại hóa đơn thanh toán định kỳ (trừ thanh toán vé máy bay)
• KH nhận được thông báo cước hóa đơn đã đăng ký qua OTT
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

##### MH1: Đăng ký nhận thông báo cước

##### MH2.1: Đăng ký nhận thông báo cước (sau khi đk xong tại MH Xem chi tiết)

##### MH2.2: Màn hình danh bạ sau khi nhận thông báo cước

##### MH3: Xác nhận hủy đăng ký nhận thông báo cước

##### MH4: Thông báo OTT hóa đơn đến hạn

#### Mô tả:

##### MH1,2: Màn hình chi tiết hóa đơn

Xem thêm mô tả phần Danh bạ thanh toán hóa đơn Thanh toán hóa đơn - Coopbank

##### MH3: Xác nhận hủy đăng ký nhận thông báo cước
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | Popup thông báo hủy nhận thông báo cước
 | 
1
 | 
Tiêu đề
 | 
Label
 | 
Read Only
 | -- | -- | 
Thông báo

 | 2 | 
Nội dung thông báo
 | 
Label
 | 
Read Only
 | -- | -- | 
Fix tại client: "Quý khách có muốn hủy đăng ký nhận thông báo cước tự động hàng tháng?"

(Lưu ý: Quý khách đăng ký nhận thông báo cước tự động từ danh bạ đã lưu)

 | 3 | 
Nút “Đóng”
 | 
Button
 | 
Click
 | -- | -- | 
<Tham khảo logic xử lý>

 | 4 | 
Nút “Hủy đăng ký”
 | 
Button
 | 
Click
 | -- | -- | 
<Tham khảo logic xử lý>

MH4: Thông báo OTT hóa đơn đến hạn
 | | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Nội dung thông báo cước qua OTT
 | 
Label
 | 
ReadOnly
 | 
--

 | -- | 
Hiển thị nội dung tin thông báo cước kèm button "Thanh toán":

• Có kỳ cước: Cước dịch vụ {Tên dịch vụ}{Nhà cung cấp} {Mã khách hàng/hóa đơn} của Quý khách trong kỳ {Giá trị kỳ} là {số tiền cước} VND. Cảm ơn Quý khách đã sử dụng dịch vụ.
• Không có kỳ cước: Cước dịch vụ {Tên dịch vụ}{Nhà cung cấp}{Mã khách hàng/hóa đơn} của Quý khách là {Số tiền cước} VND. Cảm ơn Quý khách đã sử dụng dịch vụ.
 | 2 | Thanh toán | Button | Click | -- | -- | <Tham khảo logic xử lý>

#### 4/ Luồng xử lý

 | TT | Thao tác | Tác nhân | Mô tả
 | Đăng ký nhận thông báo cước
 | 
1

 | 
Click chọn ON tại toggle Nhận thông báo cước hàng tháng

 | 
App Client
 | 
1/ Gửi yêu cầu đăng ký nhận thông báo cước tới server

 | 
App Server
 | 
1/ Cập nhật trạng thái đăng ký nhận thông báo cước về ON, trả kết quả về cho Client

• Không hợp lệ: Trả kết quả lỗi tương ứng về cho Client (Lỗi gián đoạn hệ thống)
• Hợp lệ: Cập nhật trạng thái đăng ký nhận thông báo cước về ON và trả kết quả thành công về cho Client
 | 
Client
 | 
1/ Nhận kết quả:

• Không thành công: Hiển thị popup thông báo lỗi tương ứng (Lỗi gián đoạn hệ thống)
• Thành công: Hiển thị Toggle ở trạng thái ON
 | Đăng ký hủy nhận thông báo cước
 | 3 | 
Click chọn OFF tại toggle Nhận thông báo cước hàng tháng
 | 
Client
 | 
1/ Hiển thị poup Thông báo và hai button: Không và Đồng ý

Nội dung: "Quý khách có muốn hủy đăng ký nhận thông báo cước tự động hàng tháng?" 

 | 
4

 | 
Nhấn nút “Không”
 | 
Client
 | 
1/ Tắt thông báo và hiển thị màn hình đang thao tác

 | 
Nhấn nút “Đồng ý””
 | 
Client
 | 
Thực hiện gạt toggle sang off (thông tin sẽ được chuyển sang server xử lý lưu như các thông tin khác khi KH nhấn cập nhật tại MH Đăng ký nhập thông báo cước - Chi tiết danh bạ

Nhận thông báo cước hàng tháng
 | TT | Thao tác | Tác nhân | Mô tả
 | 
Quét cước và trả thông báo cước

 | 
1
 | 
Quét truy vấn cước
 | 
App server
 | 
1/ Thực hiện lấy danh sách hóa đơn đã đăng ký nhận thông báo cước và gửi danh sách sang hệ thống Vnpay Billing system → Nhà cung cấp để kiểm tra hóa đơn

 | 
Vnpay Billing system → NCC
 | 
1/ Vnpay Billing system gửi yêu cầu quét cước sang NCC để check thông tin cước và trả kết quả về MB server

 | 
App Server
 | 
1/ Nhận kết quả:

• Không thành công: Hiện thị popup thông báo lỗi tương ứng: | TT | Trường hợp lỗi | Tác nhân | Nội dung
 | 1 | Thông tin danh bạ hóa đơn không hợp lệ | NCC | Thông tin hóa đơn không hợp lệ. Vui lòng kiểm tra lại
 | 2 | Hóa đơn không có nợ cước | NCC | Hóa đơn không nợ cước. Vui lòng kiểm tra lại.

• Thành công: 
• Ghi nhận giao dịch lấy cước thành công và chuyển sang bước gửi thông báo cước cho khách hàng
 | 
2
 | 
Gửi thông báo cước
 | 
App Server
 | 
1/ Gửi thông báo cước hàng tháng (nội dung thông báo được cấu hình tại hệ thống MB) sang OTT server (theo thời gian quy định trên BE) gồm: 

• Dịch vụ
• Nhà cung cấp
• Mã khách hàng/hóa đơn
• Nội dung thông báo:
• Gửi OTT có hiển thị nút “Thanh toán”. Nội dung OTT:
• Có kỳ cước: Cước dịch vụ {Tên dịch vụ}{Nhà cung cấp} {Mã khách hàng/hóa đơn} của Quý khách trong kỳ {Giá trị kỳ} là {số tiền cước} VND. Cảm ơn Quý khách đã sử dụng dịch vụ.
• Không có kỳ cước: Cước dịch vụ {Tên dịch vụ}{Nhà cung cấp}{Mã khách hàng/hóa đơn} của Quý khách là {Số tiền cước} VND. Cảm ơn Quý khách đã sử dụng dịch vụ.
 | 
OTT Server
 | 
Gửi nội dung thông báo đến số điện thoại đăng ký OTT.

 | 
App Client
 | 
Hiển thị thông báo cước trên màn hình chức năng Thông tin ngân hàng.

Nếu Dịch vụ được phép thanh toán trên kênh MB, hiển thị nút “Thanh toán”, nhấn vào nút này hiển thị màn hình thanh toán hóa đơn tương ứng.

 | Màn hình: Thông tin ngân hàng
 | 
1
 | 
Nhấn “Thanh toán” tại 1 tin thông báo cước
 | 
App Client
 | 
Kiểm tra KH thực hiện chức năng:

Trước đăng nhập: hiển thị thông báo: "Quý khách vui lòng đăng nhập để thực hiện thanh toán"

• Nút Hủy: Nhấn nút này, tắt thông báo và hiển thị màn hình đang thao tác
• Nút Đồng ý: Nhấn nút này, ứng dụng hiển thị màn hình Đăng nhập. Sau khi đăng nhập xong thực hiện như luồng sau đăng nhập phía dươi.
Sau đăng nhập:

Hiển thị MH tin OTT, focus tin OTT tương ứng vừa lick (tab Tất cả), nhấn thanh toán tại tin OTT hiển thị màn hình khởi tạo thanh toán hóa đơn với các nội dung về: Gọi server lấy ds tài khoản nguồn. Dịch vụ, nhà cung cấp, mã khách hàng đã được fill sẵn,

---


## 22. URD_AUTO DEBIT- Thanh toán hóa đơn tự động

> **Page ID:** `306709025` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/306709025

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*4 trang con:*

### 22.1. (Bank) SOW_ Auto Bill

> **Page ID:** `306709060` · **Version:** 8
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/306709060

### 1/ Mục đích & ý nghĩa chức năng

a. Auto Debit là gì?

Là hình thức mà khi khách hàng có đồng ý đăng ký Thanh toán hóa đơn tự động trên ứng dụng MB, Ngân hàng sẽ tự động trích nợ từ tài khoản nguồn mà KH đã đăng ký để thanh toán giúp khách hàng số tiền theo hóa đơn nhà cung cấp thông báo

b. Mục đích của chức năng

• Giúp KH không bị quên thanh toán các loại hóa đơn, dẫn đến tình trạng bị cắt dịch vụ
• Tiết kiệm thời gian
### 2/ Luồng quy trình thanh toán tự động

trueQuy trình AutoDebitfalseautotoptrue133818

### 3/ Phạm vi

#### 2.1/ Phạm vi FrontEnd
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | Phạm vi tác nhân thực hiện | Link tài liệu
 | Đăng ký thanh toán hóa đơn tự động | 
• Thêm mới đăng ký | 
RedThêm mới
 | MB | 
B1: KH chọn chức năng Đăng ký thanh toán tự động

B2: KH chọn dịch vụ, NCC, mã hóa đơn, tài khoản nguồn trích nợ và bấm Tiếp tục

B3: Hệ thống truy vấn mã đơn sang nhà cung cấp nếu hợp lệ thì cho phép lưu yêu cầu đăng ký thanh toán tự động
 | 
BlueTrung Bình
 | Client, Server | 
Đăng ký thanh toán hóa đơn tự động

 | 
• Hủy đăng ký | 
RedThêm mới
 | MB | 
Cho phép KH Hủy đăng ký thanh toán tự động để ngừng việc trích nợ tự động
 | 
BlueTrung Bình
 | Client, Server | 

Danh sách hóa đơn tự động

 | 
• Thay đổi đăng ký | 
RedThêm mới
 | MB | 
Cho phép đổi tài khoản nguồn trích nợ?
 | 
BlueTrung Bình
 | Client, Server
 | 
• Danh sách giao dịch thanh toán tự động | 
RedThêm mới
 | MB | 
Cho phép xem lại kết quả quét Job thanh toán

(Thành công, không thành công + lý do ...)

 
 | 
BlueTrung Bình
 | Client, Server
 | Danh bạ hóa đơn | Đăng ký thanh toán hóa đơn tự động | 
GreenCập nhật
 | MB | 
Cho phép đăng ký thanh toán hóa đơn tự động từ danh bạ hóa đơn
 | 
BlueTrung Bình
 | Client, Server | 
MB_Danh bạ hóa đơn

####  2.2/ Phạm vi Server
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | Phạm vi tác nhân thực hiện | Link tài liệu
 | Job nhắc nợ/ thanh toán hóa đơn tự động | 
Job nhắc nợ/ thanh toán hóa đơn tự động

(Nâng cấp từ Job nhắc nợ đã có)
 | 
GreenCập nhật
 | MB | 
• Đến kỳ quét cước theo cấu hình, Job truy vấn thông tin cước sang NCC
• NCC trả thông tin có nợ cước, Job kiểm tra KH có đăng ký Auto Bill không?
• Nếu có đăng ký Auto Bill → Job tự động gọi hạch toán sang Bank
• Nếu không đăng ký Auto Bill → Job gửi yêu cầu thông báo nhắc nợ sang hệ thống OTT để push cho KH ( Và không gọi hạch toán) | 
BlueTrung Bình
 | Server | 
(Bank) Job thanh toán hóa đơn tự động

2.3/ Phạm vi BackOffice
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | Phạm vi tác nhân thực hiện | Link tài liệu
 | Báo cáo | Báo cáo thanh toán hóa đơn | 
GreenCập nhật
 | 
 | Bổ sung thêm type Chủ động/ Tự động để đánh dấu giao dịch nào thanh toán chủ động bởi KH, giao dịch nào thanh toán tự động bởi Job | 
 YellowDễ
 | BackOffice | 
Báo cáo chi tiết giao dịch TTHĐ, SDK Vé xem phim, vé máy bay

 | Báo cáo KH đăng ký Auto Bill | 
RedThêm mới
 | 
 | Báo cáo ghi nhận các bản ghi KH đăng ký/ Hủy đăng ký/ Thay đổi tài khoản nguồn của chức năng Đăng ký thanh toán tự động | 
 BlueTrung Bình
 | BackOffice | 
Báo cáo chi tiết đăng ký thanh toán tự động

 | Danh mục | Dịch vụ thanh toán hóa đơn | 
GreenCập nhật
 | 
 | Bổ sung thêm 1 checkbox "Dịch vụ cho phép thanh toán tự động" | 
YellowDễ
 | BackOffice | 
Dịch vụ TTHĐ

---

### 22.2. (Bank) Job thanh toán hóa đơn tự động

> **Page ID:** `331351595` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/331351595

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Thời gian cập nhật
 | 
 
 | A | HongLT | 
 | 
Tạo mới
 | V.1 | 

greywhitewhite1greysolidMục lục

### 1/ Tác nhân, điều kiện trước, kết quả mong muốn
greywhitewhite1greysolidTác nhân, điều kiện, kết quả mong muốn

 | 1. Tác nhân tham gia: | 
MB server, HT bank, HT Billing VNpay

 | 2. Điều kiện trước: | 
Bao gồm tất cả các điều kiện sau:

• KH đã đăng ký thanh toán hóa đơn tự động
• Dịch vụ thanh toán hóa đơn mà KH đăng ký đã đến kỳ quét cước
• Ngày KH đăng ký bắt đầu thực hiện thanh toán hóa đơn tự động nhỏ hơn hoặc bằng ngày quét Job
 | 3. Kết quả mong muốn: | 
• Khách hàng được thanh toán tự động dịch vụ hóa đơn đã đăng ký

### 2/ Luồng xử lý Job

trueJob autobill gui bankfalseautotoptrue13382

### 4/Mô tả Job

JOB Truy vấn/ Hạch toán/ Gạch nợ

 | 
Xử lý với các bản ghi có trạng thái Đã đăng ký Auto Bill, Đăng ký nhắc nợ

 | 1 
 | 
HT MB
 | 
1/ Bắt đầu đến ngày/giờ quét cước đã cấu hình theo NCC trong BE

2/ MB server truy vấn Billing với các hóa đơn đã đăng ký  Auto Bill và có ngày đăng ký thanh toán tự động =< Ngày thực hiện Job 

3/ Truy vấn hóa đơn thành công --> Gửi yêu cầu hạch toán sang Bank theo đúng số tiền đã truy vấn hóa đơn

 |  
 2 | HT Bank | Hệ thống Bank hạch toán và trả kết quả
 | HT MB | HT MB nhận kết quả do Bank trả
• Không thành công: Ghi nhận lỗi tương ứng
• Thành công → Gửi yêu cầu Gạch nợ tới HT Billing 
 | 3 | HT Billing | Thực hiện gạch nợ và trả kết quả
 | HT MB | 
MB Server nhận kết quả do Bank HT Billing trả:

• Không thành công: Ghi nhận trạng thái = Gạch nợ thất bại → Và gửi yêu cầu Đảo tiền sang HT Bank (API  reversePayment)
HT Bank
• Thành công → Ghi nhận trạng thái = Giao dịch thành công
 | 4 | HT Bank | Thực hiện Đảo tiền và trả kết quả
 | HT MB | 
Nhận kết quả Đảo tiền do Bank trả về và Dừng quy trình quét Job của kỳ cước này (Kỳ cước sau thực hiện quét lại)

• Không thành công: Ghi nhận trạng thái = Hoàn tiền thất bại
• Timeout: Ghi nhận trạng thái = Hoàn tiền timeout
• Thành công: Ghi nhận trạng thái = Hoàn tiền thành công

---

### 22.3. Đăng ký thanh toán hóa đơn tự động

> **Page ID:** `326730433` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/326730433

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

#### 22.3.1. Flow & Action Screen_Đăng ký thanh toán hóa đơn tự động

> **Page ID:** `321293286` · **Version:** 16
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/321293286

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | Lê Thị Hồng | V.1.0.0 | 
Tạo mới
 | 

 | 
 
 | M | Lê Thị Hồng | 
 | 

 | 

Mục lục
none

### 1/ Danh sách màn hình

<Luồng di chuyển màn hình → https://kpmah3.axshare.com/>

##### <MH1.1: Truy cập chức năng Đăng ký thanh toán tự động- Cách 1>

##### <MH1.2: Truy cập chức năng Đăng ký thanh toán tự động- Cách 2>

Tham khảo luồng đăng ký của cách 2 tại <>

##### <MH2 Khởi tạo- Đăng ký>

##### <MH2.1: Thông báo lỗi kết quả truy vấn>

##### <MH 3 Xác nhận đăng ký>

##### <MH4: Xác thực đăng ký>

##### <MH5: Kết quả giao dịch>

##### <MH6: Danh sách đăng ký thanh toán tự động>

MH7: Thông báo lỗi thông tin hóa đơn đã tồn tại đăng ký trước đó

#### 3/ Mô tả màn hình

##### <MH1: Truy cập chức năng>

Cách 1: Tại MH danh sách Thanh toán hóa đơn →  Bổ sung chức năng "Đăng ký thanh toán tự động" → Bấm chọn chức năng "Đăng ký thanh toán tự động" → Mở ra MH "Danh sách hóa đơn đăng ký tự động"→ Bám nút "Đăng ký" mở ra MH "Đăng ký thanh toán tự động"

Cách 2: Tại MH danh sách Thanh toán hóa đơn → Bấm chọn chức năng "Danh bạ hóa đơn" (Đã triển khai trước đó)→ Đối với danh bạ chưa đăng ký thanh toán hóa đơn tự động → Hiển thị nút "Đăng ký thanh toán tự động" → Bấm vào nút "Đăng ký thanh toán tự động" để đăng ký  <Tham khảo tại tài liệu >

##### <MH2: Đăng ký thanh toán tự động>
 | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu thao tác
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Đăng ký thanh toán tự động

 | 
3
 | 
Tài khoản nguồn
 | 
Combobox
 | 
Select
 | 
Có
 | 
--
 | 
• 
Mặc định: Hiển thị tài khoản thanh toán mặc định

• 
Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do Bank trả về

• 
Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.

• 
Popup chọn tài khoản: Hiển thị:

       - Số tài khoản + icon đánh dấu Tài khoản mặc định (nếu có)

       - Số dư

• 
Cho phép chọn 1 tài khoản. Nếu chọn lại tài khoản khác tài khoản mặc định thì khi mở lại Popup tài khoản nguồn, sẽ hiển thị sẽ tích vào số tài khoản vừa chọn

 | 

 | 
Thông tin đăng ký
 | 

 | 

 | 

 | 

 | 

 | 
4
 | 
Dịch vụ
 | 
Combobox
 | 
Select
 | 
Có
 | 
--
 | 
• 
Lấy lên các dịch vụ được đánh dấu "Cho phép thanh toán tự động" tại bảng Dịch vụ thanh toán hóa đơn  () → Bổ sung thêm 1 cấu hình "Cho phép thanh toán tự động" theo dịch vụ TTHĐ tại bảng Dịch vụ thanh toán hóa đơn

• 
Hiển thị danh sách dịch vụ theo thứ tự do server trả về

• 
Cho phép chọn 1 dịch vụ từ danh sách và lựa chọn thay đổi

• 
Hiển thị bổ sung chức năng tìm kiếm nếu danh sách dịch vụ> 5

• 
Lưu ý: Nếu dịch vụ chỉ có 1 giá trị, fill sẵn giá trị vào ô Dịch vụ

 | 
5
 | 
Nhà cung cấp
 | 
Combobox
 | 
Select
 | 
Có
 | 
--
 | 
• 
Chỉ hiển thị trường Nhà cung cấp sau khi khách hàng đã chọn Dịch vụ 

• 
Lấy lên Danh sách nhà cung cấp được đánh dấu "Cho phép thanh toán tự động" (  Bổ sung thêm 1 cấu hình "Cho phép thanh toán tự động" theo NCC tại bảng Nhà cung cấp_

• 
Hiển thị bổ sung cụm tìm kiếm nếu danh sách NCC > 5 Cho phép tìm kiếm nhà cung cấp trong danh sách

• 
Lưu ý: Nếu nhà cung cấp chỉ có 1 giá trị, fill sẵn giá trị vào ô Nhà cung cấp

 | 
6
 | 
Mã thanh toán
 | 
Textbox
 | 
Input
 | 
 | 
20
 | 
• 
Chỉ hiển thị khi đã chọn xong NCC

• 
Hiển thị Label Mã thanh toán tương ứng với label đã cấu hình tại bảng quản lý NCC

• 
Cho phép nhập số, chữ không dấu, ký tự đặc biệt

 | 
7
 | 
Ngày đăng ký
 | 

Datetime

 | 

Select

 | 

Có

 | 

--

 | 
• 
Mặc định ngày hiện tại

• 
Chỉ cho phép chọn ngày hiện tại và ngày tương lai

 | 
8
 | 
Tiếp tục
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mở đến MH <Xác nhận đăng ký>

##### <MH3: Xác nhận giao dịch>
 | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu thao tác
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Icon Back
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Quay trở lại màn hình trước

 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Xác nhận đăng ký

 | 
3
 | 
Ghi chú
 | 
Label
 | 
Read Only
 | 
 | 
 | 
Quý khách vui lòng kiểm tra thông tin đăng ký

 | 
5
 | 
Tài khoản nguồn
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị thông tin tài khoản nguồn

 | 
7
 | 
Dịch vụ
 | 
Label
 | 
Read Only
 | 

 | 

 | 
Hiển thị dịch vụ TTHĐ đã chọn

 | 
8
 | 
Nhà cung cấp
 | 
Label
 | 
Read Only
 | 

 | 

 | 
Hiển thị tên NCC đã chọn

 | 
9
 | 
Mã khách hàng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị mã KH đã nhập

 | 
9
 | 
Tên khách hàng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị tên khách hàng truy vấn được từ Hệ thống Billing trả về (nếu có)

 | 
10
 | 
Ngày đăng ký
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Ngày đăng ký của KH đã chọn

 | 
11
 | 
Tiếp tục
 | 
Button
 | 
--
 | 
--
 | 
--
 | 
Mở đến MH <Xác thực giao dịch>

##### <MH4: Xác thực giao dịch>

Đi theo luồng xác thực không có số tiền Tham khảo Logic xử lý tại 

##### <MH5: Kết quả giao dịch>
 | TT | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | 
Tiêu đề màn hình
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Kết quả giao dịch

 | 2 | 
Logo Bank
 | 
Label 
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Logo + Co-opBank

 | 3 | 
Câu thông báo thành công
 | 
Label 
 | 
ReadOnly
 | 
--
 | 
--
 | 
Đăng ký thanh toán tự động thành công

 | 4 | 
Icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Bấm icon Home back về MH Home

 | 5 | 
Thông tin giao dịch
 | 

 | 

 | 

 | 

 | 

 | 6 | 
Thời gian đăng ký
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Thời gian đăng ký Hiển thị theo định dạng dd/mm/yyyy hh:mm

 | 7 | 
Tài khoản nguồn
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 8 | 
Mã đăng ký
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Mã giao dịch do MB server sinh

 | 9 | 
Dịch vụ
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 10 | 
Nhà cung cấp
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 11 | 
Tên khách hàng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 12 | 
Mã khách hàng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 13 | 
Chia sẻ
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon → Tham khảo logic xử lý

 | 14 | 
Lưu ảnh
 | 
icon
 | 
click
 | 
 | 
 | 
Nhấn icon → Tham khảo logic xử lý

 | 15 | 
Tạo giao dịch mới
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon → Tham khảo logic xử lý

---

#### 22.3.2. User Action Flow_Đăng ký thanh toán hóa đơn tự động

> **Page ID:** `322111607` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/322111607

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
  
 | A | HongLT | 
 | 
Tạo mới
 | V.1

### 1/ Luồng xử lý

### 1/ Truy cập chức năng
 | TT | Tác nhân | Mô tả
 | 
##### 1
 | 
##### Thao tác 1: Tại màn hình Danh sách thanh toán hóa đơn, KH nhấn chọn "Đăng ký thanh toán tự động"

 | 1 | HT MB | 
1/ Truy vấn danh sách hóa đơn đăng ký tự động đã lưu

• Không thành công: hiển thị thông báo lỗi/ timeout tương ứng
• Thành công: 
- Không có danh sách: Hiển thị câu ghi chú như mô tả màn hình

- Có danh sách: Hiển thị danh sách hóa đơn đã đăng ký như mô tả màn hình

 | 
##### 2
 | 
##### Thao tác 2: Tại màn hình Danh sách hóa đơn đăng ký tự động, bấm Đăng ký

 |   | HT MB | 
Gửi yêu cầu truy vấn danh sách tài khoản nguồn sang Bank

 |   | Bank | 
Xử lý truy vấn danh sách tài khoản nguồn hợp lệ và trả kết quả:

• Timeout: Trả kết quả timeout cho MB
• Không thành công: Trả kết quả cho MB
•  Thành công: Trả kết quả cho MB
 |   | HT MB | 
Nhận kết quả:

• Timeout: Hiển thị thông báo timeout
• Không thành công: Hiển thị thông báo lỗi tương ứng theo mã lỗi Bank trả về
• Thành công: Hiển thị màn hình khởi tạo Đăng ký thanh toán tự động : Thông tin tài khoản nguồn hợp lệ (Mặc định là tài khoản thanh toán - Nếu không phải là tài khoản thanh toán thì lấy tài khoản đầu tiên trong danh sách trả về), bao gồm: số tài khoản, số dư khả dụng + đơn vị tiền tệ VNĐ.

### 2/ Khởi tạo giao dịch đăng ký
 | TT | Tác nhân | Mô tả
 | 1 | 
##### Thao tác 1: Chọn dịch vụ TTHĐ

 | 2 | HT MB | 
Hiển thị Popup chọn dịch vụ TTHĐ:

• Nếu không có dịch vụ TTHĐ được đăng ký tự động: Hiển thi Popup "Không có dịch vụ thanh toán hóa đơn tự động"
• Nếu chỉ có 1 dịch vụ TTHĐ: Hiển thị luôn dịch vụ đó
• Nếu có > 1 dịch vụ TTHĐ: Hiển thị Popup dịch vụ TTHĐ cho khách hàng lựa chọn. Nếu có trên 5 bản ghi, hiển thị ô tìm kiếm.
 | 3 | 
##### Thao tác 2: Chọn NCC TTHĐ

 | 4 | HT MB | 
Hiển thị Popup chọn NCC:

• Nếu không có NCC: Hiển thi Popup "Không có nhà cung cấp dịch vụ thanh toán hóa đơn tự động"
• Nếu chỉ có 1 NCC: Hiển thị luôn thông tin NCC
• Nếu có > 1 NCC: Hiển thị Popup NCC cho khách hàng lựa chọn. Nếu có trên 5 NCC, hiển thị ô tìm kiếm.
 | 5 | 
##### Thao tác 3: Nhập các thông tin còn lại và bấm Tiếp tục

 | 6 | HT MB | 
Validate thông tin

• Không hợp lệ | 
 | Trường hợp lỗi | Nội dung
 | 2 | Bỏ trống dịch vụ | Quý khách vui lòng chọn Dịch vụ
 | 3 | Bỏ trống Nhà cung cấp | Quý khách vui lòng chọn Nhà cung cấp
 | 4 | Bỏ trống Mã khách hàng | Quý khách vui lòng nhập [Label mã khách hàng]
 | 5 | Mã khách hàng tương ứng với dịch vụ và nhà cung cấp đã đăng ký trước đó rồi | Quý khách đã đăng ký thanh toán tự động cho hóa đơn này. Vui lòng kiểm tra lại
 | 7 | Mã khách hàng không hợp lệ | [Label mã khách hàng] không hợp lệ. Quý khách vui lòng kiểm tra lại.

• Hợp lệ : Hiển thị màn hình xác nhận giao dịch

### 3/ Xác nhận giao dịch đăng ký
 | TT | Tác nhân | Mô tả
 | 
 | 
##### Thao tác 1: Bấm xác nhận

 | 1 | HT MB | 
Chuyển sang màn hình xác thực giao dịch theo ptxt của luồng xác thực phi tài chính (KH không phải chọn PTXT, mà server chọn ra 1 PTXT phù hợp)

• Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)
• Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)

### 4/ Xác thực giao dịch
 | TT | Tác nhân | Mô tả
 | 
 | 
##### Thao tác 2: Bấm xác nhận

 | 1 | HT MB | 
1/ Validate thông tin mã xác thực SMS/ Soft OTP tương ứng

2/ Lưu bản ghi đăng ký thanh toán hóa đơn tự động của KH và hiển thị MH kết quả

### 5/ Kết quả giao dịch
 | TT | Tác nhân | Mô tả
 | 
 | 
##### Thao tác 1: Tại màn hình Kết quả giao dịch, KH chọn nút "Chia sẻ"

 | 1 | HT MB | 
Ứng dụng truy cập camera thiết bị và chụp ảnh màn hình kết quả giao dịch và hiển thị chế độ chia sẻ ảnh mặc định của hệ điều hành để chia sẻ.

Tham khảo cơ chế xử lý chung liên quan cấp quyền truy cập trên thiết bị: Client_Quy tắc nghiệp vụ chung

 | 
 | 
##### Thao tác 2: Tại màn hình Kết quả giao dịch, KH chọn nút "Lưu ảnh"

 | 1 | Client | 
Ứng dụng truy cập camera thiết bị và chụp ảnh màn hình kết quả giao dịch vào thư viện ảnh (Kiểm tra quyền lưu ảnh của thiết bị với ứng dụng)

Tham khảo cơ chế xử lý chung liên quan cấp quyền truy cập trên thiết bị: Client_Quy tắc nghiệp vụ chung

 | 
 | 
##### Thao tác 3: Tại màn hình Kết quả giao dịch, KH chọn nút "Tạo giao dịch mới"

 | 1 | Client | 
• Gửi yêu cầu lấy số dư khả dụng mới nhất
• Quay trở về màn hình khởi tạo

---

### 22.4. Danh sách hóa đơn tự động

> **Page ID:** `326730435` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/326730435

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

#### 22.4.1. Flow & Action Screen_Danh sách hóa đơn tự động

> **Page ID:** `326730444` · **Version:** 12
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/326730444

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | Lê Thị Hồng | V.1.0.0 | 
Tạo mới
 | 

 | 
 
 | M | Lê Thị Hồng | V.1.0.0 | 
Cập nhật:

Bổ sung bộ lọc tìm kiếm theo ngày tại MH danh sách giao dịch\
 | 

Mục lục
none

### 1/ Danh sách màn hình

<Luồng di chuyển màn hình → https://kpmah3.axshare.com/>

##### <MH1: Danh sách đăng ký thanh toán tự động>

 <MH2: Xem chi tiết đăng ký>

 <MH3: Danh sách giao dịch> 

#####  <MH4.1: Chi tiết giao dịch>  -Thành công

 <MH4.2: Chi tiết giao dịch> - Thất bại

<MH4.3: Chi tiết giao dịch> - Nghi vấn

##### <MH5.1: Thay đổi tài khoản nguồn - DS có 1 TK>

##### <MH5.2: Thay đổi tài khoản nguồn - DS có > 1 TK>

##### <MH6: Hủy đăng ký tự động>

#### 3/ Mô tả màn hình

##### <MH1: Danh sách đăng ký thanh toán tự động>
 | 
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu thao tác
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Tiêu đề
 | 

Lable

 | 

Read Only

 | 

--

 | 

--

 | 
Danh sách hóa đơn đăng ký tự động

 | 
2
 | 
Icon Back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Trở về màn hình đang thao tác trước đó

 | 
4
 | 
Ô tìm kiếm
 | 
Textbox
 | 
Input
 | 
--
 | 
200
 | 
Hiển thị khi có từ 5 bản ghi trở lên

Nhập ký tự bất kỳ

Tìm kiếm gần đúng theo: Tên gợi nhớ (Nếu có), Tên khách hàng, Mã thanh toán, Tên dịch vụ, Tên nhà cung cấp

Khi fill text vào ô danh bạ, hiển thị icon x, cho phép xóa ký tự nhập

 | 
5
 | 
Tên dịch vụ 
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Tên dịch vụ + icon dịch vụ của các dịch vụ thanh toán hóa đơn đã đăng ký

 | 
6
 | 
Thông tin đăng ký

 | 
View
 | 
Click
 | 
--
 | 
--
 | 
• 
Khi chưa có hóa đơn đăng ký, hiển thị text "Quý khách chưa có hóa đơn đăng ký tự động. Vui lòng nhấn Đăng ký để hệ thống tự động thanh toán hóa đơn khi đến kỳ cước!"

• 
Group các bản ghi hóa đơn đăng ký theo từng dịch vụ, sắp xếp theo thời gian tạo từ mới tới cũ

Mỗi hóa đơn đăng ký hiển thị các thông tin:

• 
Icon Dịch vụ: Hiển thị Icon Dịch vụ đã lưu trên hệ thống

• 
Nhà cung cấp:

• 
Mã thanh toán

• 
Tên khách hàng:  Tên KH truy vấn được từ HT Billing

• 
Cho phép click vào 1 hóa đơn để  xem chi tiết.

 | 
7
 | 
Đăng ký
 | 
Button
 | 
Click
 | 
---
 | 
--
 | 
Bấm Đăng ký, mở đến MH đăng ký thanh toán tự động 

##### <MH2: Xem chi tiết đăng ký>
 | 
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu thao tác
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Tiêu đề
 | 

Lable

 | 

Read Only

 | 

--

 | 

--

 | 
Hiển thị: Chi tiết hóa đơn đăng ký

 | 
2
 | 
Icon Back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Trở về màn hình đang thao tác trước đó

 | 
3
 | 
Icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Trở về màn hình trang chủ

 | 
4
 | 
Dịch vụ
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Tên dịch vụ đã lưu đăng ký thanh toán hóa đơn tự động tương ứng

 | 
5
 | 
Nhà cung cấp
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Tên nhà cung cấp đã lưu đăng ký thanh toán hóa đơn tự động tương ứng

 | 
6
 | 
Mã thanh toán
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Mã KH đã lưu đăng ký thanh toán hóa đơn tự động tương ứng

 | 
7
 | 
Tên khách hàng
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Tên khách hàng đã lưu đăng ký thanh toán hóa đơn tự động tương ứng

 | 
8
 | 
Tài khoản nguồn
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Tài khoản nguồn đã lưu đăng ký thanh toán hóa đơn tự động tương ứng

 | 
9
 | 
Ngày đăng ký
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Ngày đăng ký hóa đơn đã đã đăng ký thanh toán hóa đơn tự động tương ứng

 | 
11
 | 
Danh sách giao dịch thanh toán tự động
 | 
Icon Button
 | 
Click
 | 
--
 | 
--
 | 
Click mở đến MH Danh sách giao dịch

 | 
12
 | 
Thay đổi tài khoản thanh toán
 | 
Icon Button
 | 
Click
 | 
--
 | 
--
 | 
Click vào chức năng mở lên Popup Chọn lại tài khoản nguồn → KH chọn lại TK khác, đóng Poup Chọn tài khoản nguồn, và hiển thị Popup thông báo "Quý khách có muốn thay đổi tài khoản thanh toán?"

• Chọn Hủy: Đóng thông báo, giữ nguyên MH hiện tại
• Chọn Đồng ý: Mở đến MH xác thực giao dịch <Tham khảo logic xử lý>
 | 
13
 | 
Hủy đăng ký tự động
 | 
Icon Button
 | 
Click
 | 
--
 | 
--
 | 
Click mở đến Popup thông báo Quý khách có muốn Hủy đăng ký thanh toán hóa đơn tự động không?"

• Chọn Hủy: Đóng thông báo, giữ nguyên MH hiện tại
• Chọn Đồng ý: Mở đến MH xác thực giao dịch <Tham khảo logic xử lý>

##### <MH3: Danh sách giao dịch>
 | 
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu thao tác
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Tiêu đề
 | 

Label

 | 

Read Only

 | 

--

 | 

--

 | 
Hiển thị: Danh sách giao dịch

 | 
2
 | 
Icon Back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Trở về màn hình đang thao tác trước đó

 | 
3
 | 
Icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Trở về màn hình trang chủ

 | 
4
 | 
Từ ngày
 | 
Calendar
 | 
Select/Input
 | 
--
 | 
--
 | 
• Mặc định Ngày T-60
• Cho phép chọn/ nhập ngày quá khứ và hiện tại
• Từ ngày nhỏ hơn hoặc bằng đến ngày
• Khoảng thời gian tìm kiếm giữa Từ ngày ... Đến ngày không quá 3 tháng tính theo lịch
→ Hiển thị thông báo "Khoảng thời gian tối đa cho phép tìm kiếm là 3 tháng. Quý khách vui lòng chọn lại thời gian tra cứu.". Đóng câu thông báo, giữ nguyên màn hình hiện tại và không reset các giá trị đã chọn.

• Thời gian tối đa cho phép tìm kiếm trong vòng 1 năm
 | 
5
 | 
Đến ngày
 | 

 | 
Select/Input
 | 
--
 | 
--
 | 
• Mặc định Ngày T (Today)
• Cho phép chọn/ nhập ngày quá khứ và hiện tại
• Đến ngày lớn hơn hoặc bằng từ ngày
• Khoảng thời gian tìm kiếm lớn hơn 3 tháng (tính theo thời gian trên lịch)
• Thời gian tối đa cho phép tìm kiếm trong vòng 1 năm
 | 
6
 | 
Câu ghi chú
 | 

 | 

 | 

 | 

 | 
Danh sách các giao dịch được thanh toán tự động trong khoảng thời gian tìm kiếm 

 | 
7
 | 
Dịch vụ
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Tên dịch vụ đã lưu đăng ký thanh toán hóa đơn tự động tương ứng

 | 
8
 | 
Mã khách hàng
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 
9
 | 
Số tiền thanh toán
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Là số tiền nợ cước được truy vấn thành công. Hiển thị định dạng số tiền + VND

 | 
10
 | 
Ngày thực hiện quét Job thanh toán hóa đơn tự động
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị theo định dạng hh:mm:ss dd/mm/yyyy 

 | 11 | 
Trạng thái
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Bao gồm trạng thái:
 | 
 | 
Trạng thái gốc từ phase giao dịch
 | 
Trạng thái hiển thị lên Danh sách
 | 
Trạng thái thái hiển thị tại MH chi tiết

 | 
2
 | 
Hạch toán thành công + Gạch nợ thành công
 | 
Thành công → Hiển thị text màu xanh
 | 
Giao dịch thành công→ Hiển thị text màu xanh

 | 
3
 | 
Hạch toán timeout
 | 
Nghi vấn → Hiển thị text màu cam
 | 
Giao dịch nghi vấn → Hiển thị text màu cam

 | 
4
 | 
Gạch nợ timeout
 | 
Nghi vấn → Hiển thị text màu cam
 | 
Giao dịch nghi vấn → Hiển thị text màu cam

 | 
5
 | 
Hạch toán thất bại
 | 
Thất bại -->Hiển thị text màu đỏ
 | 
Hạch toán thất bại-->Hiển thị text màu đỏ

 | 
6
 | 
Gạch nợ thất bại (Hoàn tiền thành công)
 | 
Thất bại -->Hiển thị text màu đỏ
 | 
 Hoàn tiền thành công-->Hiển thị text màu đỏ

 | 
7
 | 
Gạch nợ thất bại (Hoàn tiền thất bại)
 | 
Thất bại → Hiển thị text màu đỏ
 | 
 Hoàn tiền thất bại → Hiển thị text màu đỏ

 | 
8
 | 
Gạch nợ thất bại (Hoàn tiền time-out)
 | 
Nghi vấn → Hiển thị text màu cam
 | 
 Giao dịch nghi vấn→ Hiển thị text màu cam

 | 
 | 
Bấm vào 1 bản ghi mở lên Popup Chi tiết giao dịch

##### <MH4: Popup Chi tiết giao dịch>
 | 
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu thao tác
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Tiêu đề
 | 

Label

 | 

Read Only

 | 

--

 | 

--

 | 
Hiển thị: Chi tiết giao dịch

 | 
2
 | 
Icon đóng
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Đóng Popup

 | 
3
 | 
Thông tin giao dịch
 | 
Label
 | 

Read Only

 | 

--

 | 

--

 | 
Hiển thị các thông tin:

• 
Ngày thực hiện: Ngày thực hiện quét Job thanh toán hóa đơn tự động. Hiển thị theo định dạng hh:mm:ss dd/mm/yyyy 

• 
Mã giao dịch: Là mã giao dịch hạch toán thành công Bank trả (Chỉ hiển thị nếu trạng thái = Thành công, Hoàn tiền thất bại, Hoàn tiền thành công)

• 
Tài khoản nguồn

• 
Dịch vụ

• 
Nhà cung cấp

• 
Mã thanh toán: Hiển thị theo label tương ứng đã cấu hình tại NCC

• Số tiền thanh toán: Là số tiền nợ cước được truy vấn khi khởi tạo GD thành công. Hiển thị định dạng số tiền + VND
• Phí giao dịch và thuế: Hiển thị nếu có phí + VNĐ (Chỉ hiển thị nếu trạng thái = Thành công, Hoàn tiền thất bại, Hoàn tiền thành công)
• 
Tên khách hàng: Tên KH truy vấn được, khi khởi tạo GD thành công

• 
Trạng thái: Hiển thị trạng thái như mô tả bên trên

• 
Lý do: Chỉ hiển thị nếu trạng thái = Thành công, Hoàn tiền thất bại, Hoàn tiền thành công

---

#### 22.4.2. User Action Flow_Danh sách hóa đơn tự động

> **Page ID:** `327418955` · **Version:** 5
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/327418955

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
  
 | A | HongLT | 
 | 
Tạo mới
 | V.1

### 1/ Luồng xử lý

### 1/ Danh sách giao dịch thanh toán tự động
 | TT | Tác nhân | Mô tả
 | 
##### 1
 | 
##### Thao tác 1: Tại màn hình Danh sách thanh toán hóa đơn, KH nhấn vào 1 bản ghi hóa đơn đã lưu

 | 1 | HT MB | 
 Hiển thị MH chi tiết giao dịch như đã mô tả

 | 
##### 2
 | 
##### Thao tác 2: Tại màn hình Chi tiết hóa đơn bấm chọn chức năng Danh sách giao dịch thanh toán tự động

 |   | HT MB | 
• Thực hiện lấy danh sách và chi tiết giao dịch thanh toán tự động đã được Job thanh toán tự động thực hiện (Không lấy danh sách thanh toán hóa đơn chủ động)
• Các thông tin giao dịch trả về Client bao gồm: | 
 | Trường thông tin | Mô tả
 | 
1
 | Ngày thực hiện | Ngày thực hiện quét Job
 | 
2
 | 
Dịch vụ thanh toán hóa đơn
 | 

 | 
3
 | 
Nhà cung cấp
 | 

 | 
4
 | 
Mã thanh toán
 | 

 | 
5
 | 
Số tiền thanh toán
 | 
•  Số tiền gạch nợ thành công (Chỉ trả ra số tiền với trạng thái Gạch nợ thành công)
 | 
6
 | 
Tài khoản nguồn
 | Tài khoản nguồn thanh toán KH đã đăng ký
 | 
7
 | 
Tên khách hàng
 | Chỉ ra với trạng thái Gạch nợ thành công
 | 
8
 | 
Trạng thái giao dịch
 | 
• Hạch toán thất bại
• Hạch toán timeout 
• Gạch nợ thành công
• Hoàn tiền time-out
• Hoàn tiền thất bại
• Hoàn tiền thành công
• Gạch nợ timeout
 | 
9
 | 
Lý do
 | 
Hiển thị lý do của 2 trạng thái Thất bại dưới đây:

• Hạch toán thất bại
+ Mã lỗi: xx do Bank trả về → Trả lý do: "Tài khoản nguồn đã tất toán"

+ Mã lỗi: xx  do Bank trả về → Trả lý do "Không đủ số dư"

+ Mỗi lỗi: khác 2 mã lỗi trên → Trả lý do "Lỗi khác"

• Gạch nợ thất bại
+ Mã lỗi: "50" do Billing trả về → Trả lý do "Mã khách hàng không tồn tại"

+ Mã lỗi: khác 50 do Billing trả về → Trả lý do "Lỗi khác"

Hiển thị MH Danh sách giao dịch như đã mô tả

 | 3 | 
##### Thao tác 3: Tại màn hình Danh sách giao dịch thanh toán tự động bấm chọn 1 giao dịch

 | 
 | HT MB | 
Hiển thị MH chi tiết giao dịch như đã mô tả

### 2/ Thay đổi tài khoản thanh toán/ Hủy đăng ký hóa đơn tự động
 | TT | Tác nhân | Mô tả
 | 1 | 
##### Thao tác 1: Tại màn hình Chi tiết hóa đơn bấm chọn chức năng Thay đổi tài khoản thanh toán

 | 2 | HT MB | | 
 | Trường hợp | Mô tả | Xử lý
 | 1 | 
KH bấm vào chức năng "Thay đổi tài khoản thanh toán"
 | 
• Nếu chỉ có 1 TKTT chỉ cho hiển thị Popup TK nguồn và không hiển thị thông báo dưới đây
• Nếu KH > 1 TKTT, cho phép chọn thay đổi sang TKTT khác, đồng thời Hiển thị thông báo " Quý khách có muốn thay đổi tài khoản thanh toán?" | 
• Bấm Hủy → Giữ nguyên MH hiện tại
• Bấm Đồng ý → Hiển thị MH Xác thực giao dịch Tham khảo tại Logic kiểm tra chung Hạn mức, PTXT, Phí dịch vụ
 | 2 | 
KH bấm vào chức năng Hủy đăng ký tự động
 | Hiển thị thông báo " Quý khách có muốn Hủy đăng ký thanh toán hóa đơn tự động không?" | 
• Bấm Hủy → Giữ nguyên MH hiện tại
• Bấm Đồng ý → Hiển thị MH Xác thực giao dịch Tham khảo tại Logic kiểm tra chung Hạn mức, PTXT, Phí dịch vụ

 | 3 | HT MB | 
Gửi yêu cầu truy vấn danh sách tài khoản nguồn tới MB Server

 | 4 | Bank | 
Xử lý truy vấn danh sách tài khoản nguồn hợp lệ và trả kết quả

 | 5 | HT MB | 
Nhận kết quả từ Bank

• Timeout: Hiển thị thông báo timeout
• Không thành công:  | 
 | Trường hợp | Mô tả | Xử lý
 | 1 | Lỗi không lấy được danh sách tài khoản từ Bank | Hiển thị thông báo " Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại sau" | Đóng câu thông báo, giữ nguyên màn hình
 | 2 | Trường hợp không có tài khoản thanh toán (đã tất toán hết tài khoản thanh toán) | 
Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại
 | Đóng câu thông báo, giữ nguyên màn hình

• Thành công:
- Nếu KH > 1 TKTT, cho phép chọn thay đổi sang TKTT khác, đồng thời Hiển thị thông báo " Quý khách có muốn thay đổi tài khoản thanh toán?"

          + Bấm Hủy → Giữ nguyên MH hiện tại

          + Bấm Đồng ý → Hiển thị MH Chọn PTXT theo luồng xác thực phi tài chính. < Logic kiểm tra chung Hạn mức, PTXT, Phí dịch vụ>

- Nếu chỉ có 1 TKTT  → Chỉ hiển thị Popup TK nguồn

 | 6 | 
##### Thao tác 2: Tại màn hình Chi tiết hóa đơn bấm chọn chức năng Hủy đăng ký tự động

 | 7 | HT MB | 
Hiển thị thông báo "Quý khách có muốn Hủy đăng ký thanh toán hóa đơn tự động không?"

• Bấm Hủy → Giữ nguyên MH hiện tại
• Bấm Đồng ý →  Hiển thị MH Chọn PTXT theo luồng xác thực phi tài chính. < Logic kiểm tra chung Hạn mức, PTXT, Phí dịch vụ>

### 3/ Xác thực giao dịch
 | TT | Tác nhân | Mô tả
 | 
 | 
##### Thao tác 1: Bấm xác nhận

 | 1 | HT MB | 
Chuyển sang màn hình xác thực giao dịch theo ptxt của luồng xác thực phi tài chính (KH không phải chọn PTXT, mà server chọn ra 1 PTXT phù hợp)

• Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)
• Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)

### 4/ Xác thực giao dịch
 | TT | Tác nhân | Mô tả
 | 
 | 
##### Thao tác 2: Nhập mã SMS OTP hoặc Soft OTP và Bấm xác nhận

 | 1 | HT MB | 
1/ Thực hiện xác thực Soft OTP/SMS OTP tương ứng

2/ Xác thực thành công, hiển thị thông báo thành công tương ứng và lưu lại cập nhật cho hóa đơn đã đăng ký

• Quý khách đã đổi tài khoản thanh toán thành công
• Quý khách đã hủy đăng ký thanh toán hóa đơn tự động thành công
Đóng thông báo, quay về MH Danh sách hóa đơn đăng ký tự động

---


## 28. URD_MB_COOPBANK_CÀI ĐẶT HẠN MỨC CHUYỂN TIỀN_GÓI 4

> **Page ID:** `37681368` · **Version:** 17
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37681368

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client MB, Server MB
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công
• KH có gói dịch vụ được phép sử dụng chức năng này
• KH có tài khoản hợp lệ để thực hiện chức năng này
• Kết quả mong muốn:
• KH thực hiện cài đặt hạn mức theo loại dịch vụ chuyển tiền thành công.
#### 3/ Luồng màn hình

##### MH1: Màn hình khởi tạo

##### MH2: Màn hình chọn hạn mức

##### MH3: Màn hình xác nhận thông tin

##### MH5: Màn hình kết quả

##### Mô tả màn hình

##### MH1: Màn hình khởi tạo
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Icon back | Icon | Click | 
 | 
 | Nhấn nút, hiển thị màn hình thao tác trước đó
 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị text: Cài đặt hạn mức chuyển tiền

 | 
3
 | 
Ghi chú
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Fix tại client: Quý khách vui lòng lựa chọn tổng hạn mức giao dịch chuyển tiền tối đa có thể thực hiện trong 01 ngày trên Co-opbank mobile banking

 | 
4
 | 
Hạn mức hiện tại
 | 
Label
 | 
Read Only
 | 

 | 
--
 | 
Hiển thị giá trị do server trả về

 | 
5
 | 
Hạn mức thay đổi
 | 
Combobox
 | 
select
 | 
--
 | 
--
 | 
Giá trị hiển thị cho chọn: Là danh sách hạn mức do server trả về (sắp xếp thứ tự hiển thị tăng dần)

Mặc định hiển thị giá trị nhỏ nhất trong danh sách

 | 
6
 | 
Tiếp tục
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn nút, thao khảo logic xử lý

##### MH3: Màn hình xác nhận thông tin
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Icon back | Icon | Click | 
 | 
 | Nhấn nút, hiển thị màn hình thao tác trước đó
 | 
2
 | 
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị text: Xác nhận giao dịch

 | 
3
 | 
Ghi chú
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Fix tại client: Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo

 | 
4
 | 
Hạn mức hiện tại
 | 
Label
 | 
Read Only
 | 

 | 
--
 | 
Hiển thị giá trị như màn hình trước

 | 
5
 | 
Hạn mức thay đổi
 | 
Combobox
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị giá trị như KH đã chọn tại màn hình trước

 | 6 | Chọn PTXT | Combobox | Select | 
 | 
 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 
7
 | 
Xác nhận
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn nút, thao khảo logic xử lý

##### MH4: Màn hình xác thực giao dịch

Xem tại màn hình xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH5: Màn hình kết quả
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
2
 | 
Icon Home
 | 
Icon
 | 
Click
 | 

 | 

 | 
Nhấn Icon, quay trở lại màn hình Home

 | 
3
 | 
Thông tin giao dịch
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị thông tin giao dịch thành công bao gồm các thông tin:

• Tên ứng dụng ngân hàng điện tử (logo+co-opbank)
•  Icon thành công (nút tích trog nền tròn xanh)
• Text:
• CÀI ĐẶT HẠN MỨC GIAO DỊCH THÀNH CÔNG
• Tổng hạn mức chuyển tiền thay đổi là “hiển thị số tiền+ đơn vị tiền tệ)
 | 
4
 | 
Đóng
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn nút, hiển thị màn hình chọn truy cập chức năng trước đó

4/ Luồng xử lý

##### Truy cập chức năng:
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1 | 
Có 2 hướng truy cập chức năng: 1/ từ màn hình chuyển tiền hoặc 2/ từ màn hình cài đặt:

1/ Tại màn hình chuyển tiền, nhấn button "Cài đặt hạn mức chuyển tiền"

2/ Chọn chức năng Cài đặt trên app, tại màn hình cài đặt chọn chức năng "Cài đặt hạn mức chuyển tiền"
 | Client MB | 
Gửi yêu cầu lấy thông tin hạn mức theo gói dịch vụ và số CIF tương ứng, bao gồm: Hạn mức hiện tại và danh sách hạn mức thay đổi sang Serverr

 | MB Server | 
Thực hiện truy vấn thông tin và phản hồi lại client. Thông tin phản hồi về bao gồm:

• Hạn mức hiện tại: lấy theo trường thông tin "Hạn mức chuyển tiền" theo số CIF của KH tại bảng thông tin customer. Nếu trường thông tin "Hạn mức chuyển tiền" tại bảng customer trống (KH chưa thực hiện cài đặt lại hạn mức chuyển tiền), lấy theo giá trị "Hạn mức chuyển tiền" đã cấu hình theo gói dịch vụ của KH.
• Danh sách hạn mức thay đổi: bao gồm danh sách hạn mức của gói dịch vụ tương ứng của KH được cấu hình tại bảng Hạn mức loại dịch vụ, chỉ lấy những mức hạn mức có giá trị nhỏ hơn hoặc bằng hạn mức gói dịch vụ tương ứng của KH, bao gồm cả giá trị "Hạn mức chuyển tiền" mặc định của gói dịch vụ -> Loại bỏ các giá trị trùng nhau (không bao gồm giá trị Hạn mức hiện tại) và sắp xếp danh sách theo thứ tự tăng dần.
 | Client MB | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo "Lấy thông tin hạn mức chuyển tiền không thành công. Quý khách vui lòng thử lại sau." Đóng thông báo, xử lý quay về màn hình thao tác trước đó.
• Time-out: Hiển thị thông báo "Hệ thống tạm thời bị gián đoạn. Quý khách vui lòng thử lại sau." Đóng thông báo, xử lý quay về màn hình thao tác trước đó.
• Thành công: hiển thị màn hình khởi tạo như mô tả

MH1: Màn hình khởi tạo
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1 | Chọn hạn mức thay đổi | Client MB | 
Hiển thị màn hình chọn hạn mức (MH2): Đánh dấu nổi bật giá trị hạn mức trong danh sách là giá trị hạn mức hiện tại.

 | 2 | Nhấn "Tiếp tục" | 
Client MB
 | 
Validate thông tin:

• Không hợp lệ: trường Hạn mức thay đổi trống, hiển thị thông báo "Giá trị hạn mức thay đổi không được bỏ trống. Quý khách vui lòng kiểm tra lại."
• Hợp lệ: Gửi yêu cầu khời tạo giao dịch sang MB server. Số tiền GD là giá trị hạn mức thay đổi đã chọn.
 | 
Server MB
 | 
1/ Nhận yêu cầu, thực hiện so sánh giá trị hạn mức thay đổi đã chọn với giá trị tham số TRANSFER_LIMIT_METHOD (cấu hình giá trị ký tự số, không chứa khoảng trắng và ký tự đặc biệt) đã được cấu hình trên hệ thống để đưa ra danh sách PTXT phù hợp:

•  Nếu Số tiền (giá trị hạn mức thay đổi) lớn hơn hoặc bằng giá trị tham số TRANSFER_LIMIT_METHOD -> thực hiện kiểm tra PTXT của user: 
• TH1:  Đã cài đặt Soft OTP và xác thực đủ (n) GD SMS: Chuyển sang bước 2 với PTXT trả về là Soft OTP
• TH2: Chưa cài đặt Soft OTP hoặc đã cài đặt nhưng chưa xác thực đủ (n) giao dịch SMS: Trả về thông báo "Quý khách chưa đăng ký phương thức xác thực hợp lệ với hạn mức này. Vui lòng cài đặt SOFT OTP và thực hiện (n) giao dịch tài chính bằng SMS OTP để kích hoạt phương thức xác thực hợp lệ với các giao dịch có hạn mức cao". 
• Nếu Số tiền (giá trị hạn mức thay đổi) nhỏ hơn giá trị tham số TRANSFER_LIMIT_METHOD -> thực hiện kiểm tra PTXT của user: 
• TH1:  Đã cài đặt Soft OTP và xác thực đủ (n) GD SMS: Chuyển sang bước 2 với PTXT trả về là Soft OTP và SMS OTP
• TH2: Chưa cài đặt Soft OTP hoặc đã cài đặt nhưng chưa xác thực đủ (n) giao dịch SMS: Chuyển sang bước 2 với PTXT trả về là: SMS OTP
2/ Phản hồi lại kết quả cho client

 | Client MB | 
Nhận kết quả phản hồi từ server:

• Hợp lệ: Chuyển sang màn hình Xác nhận giao dịch
• Không hợp lệ: Hiển thị thông báo lỗi tương ứng do server trả về: | STT | Case | Thông báo | Xử lý
 | 1 | Chưa cài soft hoặc đã cài nhưng chưa thực hiện đủ n gd sms | Trả về thông báo "Quý khách chưa đăng ký phương thức xác thực hợp lệ với hạn mức này. Vui lòng cài đặt SOFT OTP và thực hiện (n) giao dịch tài chính bằng SMS OTP để kích hoạt phương thức xác thực hợp lệ với các giao dịch có hạn mức cao | 
Hiển thị thông báo với button Đóng:

• Nhấn "Đóng": Đóng thông báo và giữ nguyên màn hình hiện tại
 | 2 | time-out | Hiển thị thông báo lỗi time-out chung như hệ thống hiện tại | 

##### MH3: Màn hình xác nhận giao dịch 
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhấn "Xác nhận"

 | Client MB | 
Chuyển sang màn hình xác thực giao dịch theo phương thức xác thực tương ứng đã chọn:

• Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)
• Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)

##### MH4: Xác thực giao dịch
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Nhập thông tin xác thực và nhấn "Tiếp tục"

 | Client MB | Validate thông tin  (xem tại logic màn hình xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)) và gửi yêu cầu xác thực sang server
 | MB server | 
Nhận và thực hiện cập nhật thông tin "Hạn mức hiện tại" của KH tại bảng customer.

Phản hồi lại kết quả cho client.

 | Client MB | 
Nhận kết quả:

• Thành công: Chuyển sang màn hình kết quả giao dịch
• Không thành công: Hiển thị thông báo lỗi "Cập nhật hạn mức chuyển tiền không thành công. Quý khách vui lòng thử lại." Đóng thông báo, xử lý quay lại màn hình khởi tạo
• Time-out: Hiển thị thông báo lỗi "Hệ thống tạm thời gián đoạn. Quý khách vui lòng thử lại sau.". Đóng thông báo, xử lý quay lại màn hình khởi tạo.

##### 
MH3: Màn hình kết quả
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1 | Nhấn icon home | Client MB | 
Hiển thị màn hình home

 | 2 | Nhấn "Đóng" | CLient MB | 
Hiển thị màn hình tại truy cập chức năng tương ứng:

• Nếu truy cập chức năng từ màn hình chuyển tiền -> Hiển thị màn hình chuyển tiền
• Nếu truy cập chức năng từ màn hình cài đặt -> Hiển thị màn hình cài đặt

---


