# 📋 Trang chủ

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `core/`
> **Trích xuất:** 2026-03-28

---

## 14. URD_MB_COOPBANK_TRANG CHỦ

> **Page ID:** `29890753` · **Version:** 17
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29890753

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 | A | HongLT | 
 | Tạo mới | 

 | 
 
 | M | ThuDM2 | V1.0.1 | 
Bổ sung mô tả MH cho đối tượng là thành viên của QTDND
 | V1.0.2
 | 
 
 | M | Hong |   | 
Bổ sung logic ẩn hiện chức năng Vietlot SMS tại trạng chủ
 |  

Mục lục

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: : KH, App Client, App Server.
• Điều kiện trước: 
• KH đăng nhập ứng dụng CoopBank MB thành công.
• Kết quả mong muốn:
• KH thao tác các chức năng trên màn hình trang chủ ứng dụng thành công.
#### 2/ Luồng màn hình

##### MH1: Trang chủ - đối tượng thường

##### MH2: Trang chủ - đối tượng là thành viên QTDND

##### MH3: Cài đặt

##### MH4: Thông tin cá nhân

##### MH5: Thay đổi ảnh đại diện

#### Mô tả:

##### MH1: Trang chủ - đối tượng thường,  MH2: Trang chủ - đối tượng là thành viên QTDND
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

 | Vùng 1: Thông tin ngân hàng + thông tin khách hàng
 | 1 | Background | 
Image
 | 
Read Only
 | 
Yes
 | 
--
 | 
Hiển thị background do server trả về tương ứng với đối tượng đăng nhập:

• Đối tượng thường: tham số "BACKGROUND_APP
• Đối tượng là thành viên QTDND: tham số "BACKGROUND_QTDND_APP
Trường hợp background nhận được bị lỗi (ảnh ko load được do tải hoặc domain ảnh lỗi) sẽ hiển thị bacground mặc định 

 | 2 | Logo Co-opBank | Picture | -- | -- | -- | 

 | 3 | Logo QTDND | Picture | -- | -- | -- | Chỉ hiển thị với đối tượng là thành viên QTDND
 | 4 | Tên QTDND | Label | Read Only | -- | -- | Chỉ hiển thị với đối tượng là thành viên QTDND
 | 5 | Avatar | Picture | Read Only | -- | -- | 
Hiển thị ảnh avatar mặc định hoặc avatar KH đã cài đặt (lưu tại server).

Click vào biểu tượng Avatar hiển thị MH4: Thay đổi ảnh đại diện

<Tham khảo logic xử lý MH thay đổi ảnh đại diện>

 | 6 | Thông tin tài khoản | Label | Reead Only | -- | -- | 
Hiển thị thông tin tài khoản thanh toán mặc định do Server trả về sau khi đăng nhập.

Thông tin hiển thị bao gồm:

• Tên KH tại Bank
• Số tài khoản mặc định (đã chọn khi đăng ký khách hàng tại BE)
• Số dư khả dụng của tài khoản mặc định (do bank trả về, mặc định chế độ ẩn con mắt)
• 
• Nếu "Ẩn": Số tiền hiển thị dạng mask với 3 ký tự: ***
• Nếu "Hiện": Số tiền hiển thị đầy đủ
• < Tham khảo logic xử lý tại Trang chủ>
 | Vùng 2: Chức năng truy cập nhanh
 | 1 | Các chức năng nổi bật | View List | Click | -- | -- | 
Bao gồm các chức năng theo thứ tự hiển thị như sau:

• Tài khoản
• Chuyển tiền
• Dịch vụ QR
• Nạp tiền điện thoại
Cho phép click để truy cập chức năng tương ứng.

 | Vùng 3: banner quảng cáo
 | 1 | Vùng banner quảng cáo | Slide | Swipe | -- | -- | 
Hiển thị:

• Hiển thị danh sách ảnh banner được lấy từ Server.
• Hiển thị 5 banner quảng cáo nổi bật theo thứ tự hiển thị đã cấu hình tại BE
• Cho phép vuốt sang trái/phải để hiển thị banner trước/sau, cho phép vuốt quay vòng;
• Cho phép click để mở link url tương ứng với banner đã cấu hình (nếu có).
• Nếu không có banner nào được cấu hình, vùng banner sẽ biến mất và đẩy các vùng phía dưới lên
 | Vùng 4: Chức năng theo nhóm
 | 1 | Nhóm chức năng Tài chính | View List | Click | -- | -- | 
Bao gồm:

• Tài khoản
• Thanh toán hóa đơn
• Nạp tiền điện thoại
• Đặt vé máy bay
• Đặt vé xem phim
• Trả nợ vay
Cho phép click để truy cập chức năng tương ứng < Tham khảo logic xử lý tại trang chủ>

 | 2 | Nhóm Tiện ích | View List | Click | -- | -- | 
Bao gồm:

• Quản lý danh bạ
• Quản lý mẫu thanh toán
• Cài đặt Soft OTP
• Cài đặt vân tay/Cài đặt Face ID (hiển thị tương ứng theo loại thiết bị có hỗ trợ vân tay hoặc Face ID)
• Báo cáo giao dịch
• ATM/Điểm giao dịch
 | Vùng 5: Menu chức năng tại Footer
 | 1 | Chức năng tại footer bar | View List | Click | -- | 

 | 
Bao gồm:

• Trang chủ
• Tin tức
• Dịch vụ QR
• Thông báo
• Cài đặt → Chọn Cài đặt hiển thị Màn hình Cài đặt (MH2) <Tham khảo Logic xử lý MH cài đặt>
Mặc định select sau khi đăng nhập tại "Trang chủ", cho phép click để truy cập tab chức năng tương ứng.

MH 3.  Thay đổi ảnh đại diện

Bấm vào biểu tượng Avatar tại Trang chủ hiển thị Màn hình Thay đổi ảnh đại diện và các Action:
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

 | 1 | Tiêu đề | Label | Read Only | -- | -- | Thay đổi ảnh đại diện
 | 2 | Action | Button | Click | -- | -- | 
Bao gồm các action:

• Từ Camera
• Từ Thư viện ảnh
 | 3 | Đóng (Tắt màn hình) | Icon | Click | -- | -- | Bấm vào icon "X" tắt màn hình Thay đổi ảnh đại diện

#### 3/ Logic xử lý 

MH trang chủ
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | KH Login thành công | MB server | 
Trả cờ ẩn/ hiện chức năng Mua sổ xố Vietlott SMS theo tham số cấu hình tại BE: 

VIETLOTT_SMS_CONFIG và 2 giá trị : 0= OFF, 1= ON

 | 
 | 
 | Client MB | 
Hiển thị ON/OFF chức năng Mua sổ xố Vietlott SMS tại Home theo giá trị server trả:

• 0: OFF không hiển thị chức năng
• 1: ON có hiển thị chức năng
 | 2 | Tài khoản hiển thị tại Home | Server MB | 
Trả về Tài khoản thanh toán mặc định của KH sau khi Login thành công

 | Client MB | 
Hiển thị background do server trả về tương ứng với đối tượng đăng nhập:

• Đối tượng thường: tham số "BACKGROUND_APP
• Đối tượng là thành viên QTDND: tham số "BACKGROUND_QTDND_APP
Hiển thị Tài khoản mặc định tại Trang chủ

 | 3 | KH click vào các chức năng "Eye" của tài khoản mặc định | Client MB | 
Gửi yêu cầu tra cứu số dư của Tài khoản mặc định đang hiển thị sang Bank thông qua MB Server

 | 
 | 
 | Server MB | 
Nhận kết quả từ Bank:

• Không thành công: Trả kết quả lỗi cho client
• Timeout: Trả kết quả timeout cho client
• Thành công: Trả kết qủa trạng thái tài khoản thanh toán mặc định và số dư của tài khoản thanh toán mặc định. Với trạng thái tài khoản mặc định đã bị đóng trả kết quả "Quý khách không có tài khoản thanh toán hợp lệ để thực hiện chức năng này. Vui lòng kiểm tra lại"
 | 
 | 
 | Client MB | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi gián đoạn
• Timeout: Hiển thị thông báo lỗi timeout
• Thành công:
• Tài khoản thanh toán mặc định của KH đã bị đóng. Hiển thị thông báo server trả: Quý khách không có tài khoản thanh toán hợp lệ để thực hiện chức năng này. Vui lòng kiểm tra lại. Đóng thông báo, con mắt show = 0 VNĐ
• Tài khoản thanh toán mặc định của KH hợp lệ → Show số dư
 | 4 | KH Click vào vùng các chức năng Tài chính | Server MB | Trả về về thông tin Gói dịch vụ và dịch vụ thuộc gói dịch vụ tương ứng của Khách hàng khi Login thành công
 | 
 | 
 | Client MB | 
• Không hợp lệ: Hiển thị thông báo "Gói dịch vụ không bao gồm dịch vụ đang thực hiện". Đóng Popup giữ nguyên ở MH đang thực hiện
• Hợp lệ : Cho phép truy cập chức năng đã chọn

MH thay đổi ảnh đại diện
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhấn "Từ camera" | Client | 
Ứng dụng kiểm tra quyền truy cập camera:

• Chưa cấp quyền truy cập: Hiển thị thông báo: Quý khách vui lòng cho phép ứng dụng truy cập Camera để thực hiện chức năng cập nhật ảnh đại diện.
• Nút "Hủy": Nhấn Hủy, tắt thông báo và hiển thị màn hình đang thao tác
• Nút "Đồng ý": Nhấn Đồng ý, ứng dụng mở màn hình cài đặt của thiết bị với các quyền truy cập của ứng dụng
• Đã cấp quyền truy cập: Ứng dụng mở camera của thiết bị và cho phép chụp ảnh. Sau khi chọn ảnh chụp, Client gửi yêu cầu cập nhật ảnh sang Server Media và nhận kết quả cập nhật ảnh mới.
 | 2 | Nhấn "Từ thư viện ảnh" | Client | 
Ứng dụng kiểm tra quyền truy cập thư viện ảnh:

• Chưa cấp quyền truy cập: Hiển thị thông báo: Quý khách vui lòng cho phép ứng dụng truy cập thư viện ảnh để thực hiện chức năng cập nhật ảnh đại diện.
• Nút "Hủy": Nhấn Hủy, tắt thông báo và hiển thị màn hình đang thao tác
• Nút "Đồng ý": Nhấn Đồng ý, ứng dụng mở thư viện ảnh của thiết bị và cho phép chọn ảnh. Sau khi chọn ảnh, Client gửi yêu cầu cập nhật ảnh sang Server Media và nhận kết quả cập nhật ảnh mới.
• Đã cấp quyền truy cập: Ứng dụng mở thư viện ảnh của thiết bị và cho phép chọn ảnh. Sau khi chọn ảnh, Client gửi yêu cầu cập nhật ảnh sang Server Media và nhận kết quả cập nhật ảnh mới.
 | 3 | Nhấn "Xóa ảnh" | Client | 
Client gửi yêu cầu xóa ảnh sang Server Media và nhận kết quả xóa ảnh.

• Thành công: Client cập nhật avatar của khách hàng về avatar trống
• Không thành công: Hiển thị thông báo: "Xóa ảnh không thành công, Quý khách vui lòng thử lại"

---


