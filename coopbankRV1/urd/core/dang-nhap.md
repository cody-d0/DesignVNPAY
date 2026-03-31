# 📋 Đăng nhập

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `core/`
> **Trích xuất:** 2026-03-28

---

## 13. URD_MB_COOPBANK_ĐĂNG NHẬP

> **Page ID:** `29888725` · **Version:** 9
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29888725

#### 1/ Danh sách các chức năng đăng nhập
 | 
 | Chức năng | Mô tả
 | 1 | Màn hình Đăng nhập | 

 | 2 | Logic tổng quan luồng đăng nhập | 

 | 3 | Đăng nhập lần đầu | 

 | 4 | Đăng nhập trên thiết bị khác | 

 | 5 | Đăng nhập lần sau bằng mật khẩu | 

 | 6 | Đăng nhập lần sau bằng TouchID/FaceID | 

 | 7 | Đăng nhập khi hết hạn mật khẩu | 

 | 8 | Đăng nhập thông báo yêu cầu cập nhật phiên bản mới | 

 | 9 | Phiên đăng nhập Client/Server | 

#### 2/ Logic gọi mid 4 ( kích hoạt tự động OTT) trong các luồng đăng nhập

---

*14 trang con:*

### 13.1. MB_Mở ứng dụng

> **Page ID:** `64246062` · **Version:** 91
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/64246062

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 | A | HongLT | 
 | Tạo mới | V.1
 | 
 
 | M | TrangNH | V.1 | 
Bổ sung nghiệp vụ lấy ảnh background theo cấu hình ở server
 | V.2

 | 
 
 | M | ThuDM2 | V.2 | 
Bổ sung tham số Background cho đối tượng là thành viên của QTDND
 | V.2.1

Mục lục

### 1/ Tóm tắt Use Case
 | Use Case Name: | Mở ứng dụng 
 | Use Case ID: | Coop_MB_Open_App
 | Use Case Description: | 
Hiển thị màn hình đăng nhập của ứng dụng với thông tin background và danh sách tin tức được cấu hình tại BE theo màn hình đăng nhập lần đầu và đăng nhập lần sau

 | Actor: | 
KH, App Client, App Server

 | Priority: | 

 | Trigger: | 
KH thực hiện mở ứng dụng sau khi cài đặt thành công trên thiết bị

 | 
Pre-Condition:
 | 
KH tải ứng dụng thành công

 | Post-Condition: | 
• KH mở ứng dụng thành công
• Hiển thị thông tin dữ liệu tương ứng 
• Hiển thị màn hình (đăng nhập lần đầu/ đăng nhập lần sau) 
 | Config: | 
BACKGROUND_APP = {"listConfig": [{"login": "url1"},{"other": "url2"},{"home": "url3"},{"myqr": "url4"}]} 

BACKGROUND_QTDND_APP = {"listConfig": [{"login": "url5"},{"other": "url6"},{"home": "url7"},{"myqr": "url8"}]} 

FAV_ICON_APP = {"listConfig": {"account": "linkicon","transfer": "linkicon","qrpay": "linkicon",,"topup": "linkicon"}}

VERSION_BG = "version"

### 2/ Luồng sơ đồ

#### Sơ đồ

<Insert flowchart> 

#### Danh sách API

### 3/ Luồng màn hình

#### Danh sách màn hình

##### MH1: Splash

##### MH2: Đăng nhập lần đầu

##### MH3: Đăng nhập lần sau - đối tượng thường

##### MH4: Đăng nhập lần sau - đối tượng là thành viên QTDND

#### Mô tả màn hình

##### MH1: Splash
 | | 
 | 
Hạng mục
 | 
Kiểu hiểu thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | Logo | Picture | -- | -- | -- | Hiển thị Logo của Co-op Bank

##### MH2: Đăng nhập lần đầu
 | | 
 | 
Hạng mục
 | 
Kiểu hiểu thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | Background | 
Image
 | 
Read Only
 | 
Yes
 | 
--
 | 
• Hiển thị Background là theo giá trị cấu hình tại tham số "BACKGROUND_APP" (mid 393 )
• Trường hợp background nhận được bị lỗi (ảnh ko load được do tải hoặc domain ảnh lỗi) sẽ hiển thị background mặc định của app trên App Client
 | 2 | Số điện thoại | Textbox | Number | Yes | 10 | 
• Mặc định trống.
• Cho phép nhập số điện thoại đã đăng ký dịch vụ (bàn phím số)
• Không cho phép Copy/ cho phép Paste
 | 3 | Mật khẩu | Textbox | Text | Yes | 8 - 20 | 
• Cho phép nhập ký tự số, chữ không dấu và các ký tự đặc biệt không bao gồm dấu cách.
• Mã hóa ký tự nhập vào bằng ký tự *
• Hiển thị icon "Ẩn/Hiện" mật khẩu đã nhập.
• Không cho phép Copy/ cho phép Paste
 | 4 | Đăng nhập | Button | Click | -- | -- | 
< Tham khảo logic xử lý luồng đăng nhập>

 | 5 | Vân tay/ Face ID | Icon | Click | -- | -- | 
Chỉ hiển thị đối với thiết bị có hỗ trợ vân tay hoặc hỗ trợ face id với phiên bản hệ điều hành tương ứng.

Cho phép click để đăng nhập bằng vân tay/face id

<Tham khảo logic xử lý tại MB_Đăng nhập lần sau bằng TouchID/FaceID>

 | 6 | Quên mật khẩu | Text | Click | -- | -- | <Tham khảo tại chức năng "Quên mật khẩu">
 | 7 | Tin tức | Slide | Swipe | -- | -- | 
Chỉ hiển thị tin tức có:

-Trạng thái: Hoạt động

-Loại tin: Đặc biệt

+ Ưu tiên các tin tức có cấp độ là "Đặc biệt" lên phần Nổi bật. Không giới hạn số lượng bản ghi

+ Nếu các tin có cùng cấp độ, xếp theo thứ tự thời gian từ mới đến cũ (mới hiển thị trước)

Hiển thị theo cấu trúc:

• Ảnh tin tức
• Tiêu đề
• Button xem Chi tiết
 | 8 | Chức năng khác | View List | Click | -- | -- | 
Bao gồm:

• Thông báo
• Hỗ trợ
• ATM/CN
• HDSD
Cho phép click để truy cập chức năng tương ứng.

##### MH3: Đăng nhập lần sau - đối tượng thường; MH4: Đăng nhập lần sau - đối tượng là thành viên QTDND
 | | 
 | 
Hạng mục
 | 
Kiểu hiểu thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | Background | 
Image
 | 
Read Only
 | 
Yes
 | 
--
 | 
• Hiển thị Background là theo giá trị cấu hình tương ứng với đối tượng:
• Đối tượng thường: tham số "BACKGROUND_APP
• Đối tượng là thành viên QTDND: tham số "BACKGROUND_QTDND_APP
• Trường hợp background nhận được bị lỗi (ảnh ko load được do tải hoặc domain ảnh lỗi) sẽ hiển thị background mặc định của app trên App Client
 | 2 | Logo Co-opBank | Picture | -- | -- | -- | 

 | 3 | Logo QTDND | Picture | -- | -- | -- | Chỉ hiển thị với đối tượng là thành viên QTDND
 | 4 | Tên QTDND | Label | Read Only | -- | -- | Chỉ hiển thị với đối tượng là thành viên QTDND
 | 5 | Avatar | Label | Read Only | -- | -- | 
Hiển thị:

• Avatar của KH (nếu có)
• Tên khách hàng tại Bank
• Số điện thoại đăng nhập (mask theo quy định: 3 số đầu ***** 2 số cuối)
• Icon: Đổi đăng nhập tài khoản khác, cho phép thoát tài khoản đang đăng nhập để đăng nhập với tài khoản khác.
 | 6 | Đổi tài khoản | Icon | Click | -- | -- | 
Click vào icon Đổi tài khoản. Ứng dụng hiển thị thông báo: Quý khách sẽ thoát ra khỏi tài khoản hiện tại. Quý khách có thực sự muốn đăng nhập tài khoản khác?

• Nút "Không": Nhấn nút này, tắt thông báo và hiển thị màn hình đang thao tác trước đó.
• Nút "Có": Nhấn nút này, ứng dụng thực hiện thoát tài khoản hiện tại và hiển thị màn hình với các thông tin như đăng nhập lần đầu.
-  Nếu tài khoản khác là tài khoản chưa kích hoạt lần đầu <Tham khảo logic xử lý tại luồng kích hoạt lần đầu>

- Nếu tài khoản khác là tài khoản đã kích hoạt lần đầu rồi <Tham khảo logic xử lý tại luồng đăng nhập trên thiết bị khác)

 | 7 | Mật khẩu | Textbox | Text | Yes | 8 - 20 | 
• Cho phép nhập ký tự số, chữ không dấu và các ký tự đặc biệt không bao gồm dấu cách.
• Mã hóa ký tự nhập vào bằng ký tự *
• Hiển thị icon "Ẩn/Hiện" mật khẩu đã nhập.
• Cho phép Copy/ không cho Paste
 | 8 | Đăng nhập | Button | Click | -- | -- | 
< Tham khảo logic xử lý luồng đăng nhập>

 | 9 | Vân tay/ Face ID | Icon | Click | -- | -- | 
• Chỉ hiển thị đối với thiết bị có hỗ trợ vân tay hoặc hỗ trợ face id với phiên bản hệ điều hành tương ứng.
• Cho phép click để đăng nhập bằng vân tay/face id
• <Tham khảo logic xử lý tại MB_Đăng nhập lần sau bằng TouchID/FaceID>
 | 10 | Quên mật khẩu | Text | Click | -- | -- | <Tham khảo tại chức năng "Quên mật khẩu">
 | 11 | Tin tức | Slide | Swipe | -- | -- | 
Chỉ hiển thị tin tức có:

-Trạng thái: Hoạt động

-Loại tin: Đặc biệt

+ Ưu tiên các tin tức có cấp độ là "Đặc biệt" lên phần Nổi bật. Không giới hạn số lượng bản ghi

+ Nếu các tin có cùng cấp độ, xếp theo thứ tự thời gian từ mới đến cũ (mới hiển thị trước)

Hiển thị theo cấu trúc:

• Ảnh tin tức
• Tiêu đề
• Button xem Chi tiết
 | 12 | Chức năng khác | View List | Click | -- | -- | 
Bao gồm:

• Thông báo
• Hỗ trợ
• ATM/CN
• HDSD
Cho phép click để truy cập chức năng tương ứng.

#### 4/ Luồng xử lý

##### MH2 <Đăng nhập lần đầu>
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 
1

 | 
KH mở ứng dụng

 | 
App Client
 | 
Ứng dụng hiển thị màn hình Splash (MH chờ) đồng thời gửi yêu cầu lấy cấu hình background và danh sách tin tức của app đến App Server (Mid 393: ko cần truyền "usename")

 | App Server | 
Xử lý và trả kết quả cho App Client:

• Lấy thông tin background theo giá trị cấu hình tại tham số "BACKGROUND_APP"
• Lấy 1 tham số config danh sách icon nổi bật dùng ở Home tham số " FAV_ICON_APP"
• Lấy danh sách tin tức theo điều kiện: 
• Loại tin: Đặc biệt
• Trạng thái: Hoạt động
 | App Client | 
1/ Nhận kết quả:

• TimeOut: Không hiển thị danh sách tin tức và Hiển thị background và icon mặc định của app trên App Client
• Không thành công: Không hiển thị danh sách tin tức và Hiển thị background và icon mặc định của app trên App Client
• Thành công: | TT | Trường hợp | Xử lý
 | 1 | Không có dữ liệu danh sách tin tức | Không hiển thị danh sách tin tức
 | 2 | Có dữ liệu danh sách tin tức | Hiển thị danh sách tin tức như mô tả
 | 3 | Không có dữ liệu background cấu hình | 
Hiển thị background mặc định và icon của app trên App Client

 | 4 | Có dữ liệu background cấu hình | Chuyển tiếp bước 2

2/ Check version background được cache tại client và version background được cấu hình tại server
 | TT | Trường hợp | Xử lý
 | 1 | version cache chính # version server  | 
Hiển thị background theo giá trị cấu hình tại tham số "BACKGROUND_APP" do App Server trả về

 | 2 | version cache chính = version server  | Hiển thị background đang được cache của app trên App Client

##### MH3: Đăng nhập lần sau - đối tượng thường; MH4: Đăng nhập lần sau - đối tượng là thành viên QTDND
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 
1

 | 
KH mở ứng dụng

 | 
App Client
 | 
Gửi yêu cầu lấy cấu hình background và danh sách tin tức của app đến App Server (Mid 393: truyền "usename")

 | App Server | 
Xử lý và trả kết quả cho App Client:

• Lấy thông tin background theo giá trị cấu hình tương ứng với đối tượng truy cập:
• 
• Đối tượng thường: tham số "BACKGROUND_APP"
• Đối tượng là thành viên QTDND: tham số "BACKGROUND_QTDND_APP"
• Lấy 1 tham số config danh sách icon nổi bật dùng ở Home tham số " FAV_ICON_APP"
• Lấy danh sách tin tức theo điều kiện: 
• Loại tin: Đặc biệt
• Trạng thái: Hoạt động
 | App Client | 
1/ Nhận kết quả:

• TimeOut: Không hiển thị danh sách tin tức và Hiển thị background và icon mặc định của app trên App Client
• Không thành công: Không hiển thị danh sách tin tức và Hiển thị background và icon mặc định của app trên App Client
• Thành công: | TT | Trường hợp | Xử lý
 | 1 | Không có dữ liệu danh sách tin tức | Không hiển thị danh sách tin tức
 | 2 | Có dữ liệu danh sách tin tức | Hiển thị danh sách tin tức như mô tả
 | 3 | Không có dữ liệu background cấu hình | 
Hiển thị background mặc định và icon của app trên App Client

 | 4 | Có dữ liệu background cấu hình | Chuyển tiếp bước 2

2/ Check version background được cache tại client và version background được cấu hình tại server
 | TT | Trường hợp | Xử lý
 | 1 | version cache chính # version server  | 
Hiển thị background theo giá trị cấu hình tương ứng với đối tượng truy cập do App Server trả về:

• Đối tượng thường: tham số "BACKGROUND_APP"
• Đối tượng là thành viên QTDND: tham số "BACKGROUND_QTDND_APP"
 | 2 | version cache chính = version server  | Hiển thị background đang được cache của app trên App Client

#### 5/ Lưu ý

Danh sách các màn hình hiển thị ảnh background:
 | 
 | Màn hình | Chi tiết - Đối tượng thường | Chi tiết - Đối tượng có QTDND quản lý
 | 1 | 
Đăng nhập lần đầu, Đăng nhập lần sau
 | 
{"login": "url1"}
 | 
{"login": "url5"}

 | 2 | 
Trang chủ
 | 
{"home": "url3"}

Tham số FAV_ICON_APP = {"listConfig": {"account": "linkicon","transfer": "linkicon","qrpay": "linkicon",,"topup": "linkicon"}}
 | 
{"home": "url7"}

Tham số FAV_ICON_APP = {"listConfig": {"account": "linkicon","transfer": "linkicon","qrpay": "linkicon",,"topup": "linkicon"}}

 | 3 | 
Mã QR của tôi
 | {"myqr": "url4"} | {"myqr": "url8"}
 | 4 | 
Màn hình khác:

• Xác thực (mã OTP - luồng Đăng nhập)
• Đổi mật khẩu lần đầu
• Quên mật khẩu
• Đổi mật khẩu lần sau
• Tin tức
• Cài đặt | {"other": "url2"} | {"other": "url6"}

---

### 13.2. MB_Logic tổng quan luồng đăng nhập

> **Page ID:** `29889726` · **Version:** 11
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29889726

1/ Lịch sử cập nhật
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
03/03/2021 
 | A | Lê Thị Hồng | 
 | 
Tạo mới
 | V1.0
 | 
//19/02/2025
 | M | Lê Thị Hồng | 
 | 
Điều chỉnh theo yêu cầu của TT50. Sau khi duyệt mở khóa, cập nhật trạng thái như sau

• Nếu trạng thái trước là Lock, sau khi mở khóa về Active
• Nếu trạng thái trước là Auto Lock, sau khi mở khóa về Active Standby (Cũ là không phân biệt trước đó là Lock hay AutoLock đều đang về Active)
• Nếu trạng thái trước là Auto Lock, sau khi mở khóa nếu Từ chối về Auto Lock (Cũ là đang về Lock) | V2.0
 | 
 
 | M | ThaoCY | V2.0 | 
Bổ sung trạng thái: Active 2 và Active Standby 2

• Nếu trạng thái trước là Auto Lock, sau khi mở khóa về Active 2 (Cũ đang về Active Standby)
• Từ Acitve 2:
• Nếu GDV thực hiện reset password và gửi duyệt → Pending reset password
• KH thực hiện quên mật khẩu trên app và được cấp lại mật khẩu mặc định thành công qua SMS → Active Standby
• Nếu trạng thái trước đó là Auto Lock Active Standby, sau khi mở khóa về Active Standby 2
• Từ Active Standby 2 → GDV thực hiện reset password và gửi duyệt  → Pending reset password. Sau khi được duyệt sẽ chuyển thành trạng thái Active Standby | 

2/ Sơ đồ trạng thái user Mobile Banking

 | # | Màn hình | Trạng thái trước | Thao tác | Tác nhân | Trạng thái sau | Ghi chú
 | 1 | Đăng ký dịch vụ | 
 | Gửi duyệt | GDV | Pending Approval | 

 | 2 | Duyệt | Pending Approval | Đồng ý | KSV | Active StandBy | 

 | Từ chối | KSV | Initial | 

 | Pending Reset Password | Đồng ý | KSV | Active StandBy | 

 | Từ chối | KSV | 
• Active (nếu trạng thái trước là Active)
• Active stanby (nếu trạng thái trước đó là Active standby)
• Active 2 (nếu trạng thái trước là Active 2)
• Active Standby 2 (nếu trạng thái trước là Active Standby 2) | 

 | Pending Update | Đồng ý/ Từ chối | KSV | 
• Active (nếu trạng thái trước là Active)
• Active stanby (nếu trạng thái trước đó là Active standby) | 
Đồng ý duyệt →Thông tin cập nhật được update vào DB

Từ chối duyệt → Thông tin cập nhật không được update vào DB

 | Pending Cancel service | Đồng ý | KSV | Cancelled | 

 | Từ chối | KSV | 
• Active (nếu trạng thái trước là Active)
• Active stanby (nếu trạng thái trước đó là Active standby) | 

 | Pending Unlock | Đồng ý | KSV | 
• Nếu trạng thái là Lock, nếu đồng ý về Active
• Nếu trạng thái là Auto Lock, nếu đồng ý về Active 2 | 

 | Từ chối | KSV | 
• Nếu trạng thái trước là Lock nếu Từ chối về Lock
• Nếu trạng thái trước là Auto Lock, nếu Từ chối Auto Lock (Cũ là đang về Lock) | 

 | Pending Unlock Active Standby | Đồng ý | KSV | Active Standby 2 | 

 | Từ chối | KSV | Auto lock Active Standby | 

 | Pending Lock | Đồng ý | KSV | Locked | 

 | Từ chối | KSV | Active | 

 | 3 | Đăng nhập lần đầu | Active 2 | KH thực hiện quên mật khẩu trên app và được cấp lại mật khẩu mặc định thành công qua SMS | KH | Active Standby | 

 | Active StandBy | Nhập đúng mât khẩu | KH | Active | 

 | Nhập sai OTP/Mật khẩu quá số lần quy định | KH | Auto lock Active Standby | 

 | 4 | Đăng nhập lần sau | Active | Nhập sai mật khẩu quá số lần quy định | KH | Auto lock | 

 | 5 | Cập nhật dịch vụ | Active | Cập nhật dịch vụ | KSV | Pending Update | 

 | Hủy dịch vụ | KSV | Pending Cancel | 

 | Active StandBy | Cập nhật dịch vụ | KSV | Pending Update | 

 | Hủy dịch vụ | KSV | Pending Cancel | 

 | 6 | Quản lý khách hàng | Active | Lock | GDV | Pending Lock | 

 | Reset Password | GDV | Pending Reset Password | 

 | Active StandBy | Reset Password | GDV | Pending Reset Password | Nếu mật khẩu lần đầu quá hạn 24h (có thể cấu hình thời gian hiệu lực của mật khẩu lần đầu)
 | Lock | Unlock | GDV | Pending Unlock | 

 | Auto Lock | Unlock | GDV | Active | 

 | Auto Lock ActiveStandby | Unlock | GDV | Pending Unlock Active Standby | 

 | Active 2 | Reset Password | GDV | Pending Reset Password | 

 | 
 | 
 | Active Standby 2 | Reset Password | GDV | Pending Reset Password |

---

### 13.3. TT50_ Đăng nhập kiểm tra mật khẩu và mã PIN Soft OTP sắp hết hạn

> **Page ID:** `637831805` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/637831805

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*1 trang con:*

#### 13.3.1. URD_Thông báo nhắc sắp hết hạn mật khẩu, mã PIN Soft OTP

> **Page ID:** `637831955` · **Version:** 22
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/637831955

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | Tạo mới | V.1 | 

 | 

Mục lục
none

## 1/ Tóm tắt Usecase
 | Use Case Name | Kiểm tra mật khẩu, mã PIN Soft OTP sắp hết hạn tại chức năng Login
 | Use Case ID | --
 | Use Case Description | 
Điều 7. Phần mềm ứng dụng Online Banking khoản 6. Các chức năng bắt buộc của phần mềm ứng dụng Online Banking của Thông tư 50

(ii) Thông báo cho khách hàng khi mã PIN hoặc mã khóa bí mật sắp hết hiệu lực sử dụng

 | Actor | 
KH, MB App, MB server

 | Priority | Hight
 | Trigger | 
KH có MK sắp hết hạn, mã PIN Soft sắp hết hạn, mã PIN Soft đã hết hạn

 | 
Pre-Condition
 | 
• KH đã update app mới
• KH có MK sắp hết hạn, mã PIN Soft đã/ sắp hết hạn theo cấu hình thời hạn hiệu lực của từng loại như sau: | 
 | Tham số | Giá trị | Mô tả | Ghi chú
 | 1 | FIRST_PASS_WORD_EXPIRY | 7 | Thời gian hết hạn mật khẩu cấp lần đầu theo ngày | Nghiệp vụ cũ đã có
 | 2 | PASS_WORD_EXPIRY | 180 | Thời gian hết hạn mật khẩu theo ngày | Nghiệp vụ cũ đã có
 | 4 | PASS_WARNING_EXPIRY | 10 | Số ngày sắp hết hạn mật khẩu được nhận cảnh báo tại chức năng Login | Bổ sung mới
 | 5 | PIN_SOFT_EXPIRY | 365 | Thời gian hết hạn mã PIN Soft OTP theo ngày | Bổ sung mới
 | 6 | PIN_SOFT_WARNING_EXPIRY | 10 | Số ngày sắp hết hạn mã PIN Soft OTP được nhận cảnh báo tại chức năng Login | Bổ sung mới
 | 7 | LOGIN_WARNING_EXPIRY_VERSION | 1.2.6 | 
Check version app nhận thông báo sắp hết hạn mật khẩu, sắp/ đã hết hạn mã PIN Soft tại chức năng Login. Nếu ver app của KH nhỏ hơn ver cấu hình sẽ không nhận được các loại thông báo trên tại chức năng Login

(Bỏ do server không trả thông báo lỗi hết hạn dạng message code mà trả trường mới ""expiryNotices" tại mid 1 nên không ảnh hưởng đến App cũ
 | Bổ sung mới
 | 8 | TRANS_WARNING_EXPIRY_VERSION | 1.2.6 | Check version app yêu cầu KH force update app khi mã PIN Soft OTP đã hết hạn tại chức năng Giao dịch Soft | Bổ sung mới

 | Post-Condition | 
KH nhận được thông báo mật khẩu sắp hết hạn, mã PIN Soft sắp hết hạn, mã PIN Soft đã hết hạn tại chức năng Login

Note:

• Thông báo hết hạn mật khẩu tại Login - Logic cũ đã có
• Thông báo GTTT hết hạn tại Login- Logic cũ đã có
 | 
Bussiness Rule

(Quy tắc nghiệp vụ)
 | 
• Đối với KH cũ chưa update app → Chỉ nhận được thông báo GTTT đã hết hạn như luồng cũ đã golive và không check: Ngày sắp hết hạn mật khẩu, Ngày hết hạn PIN Soft, Ngày sắp hết hạn PIN Soft để tránh yêu cầu KH update app
• KH đã update app mới nhận được thông báo theo thứ tự ưu tiên: MK sắp hết hạn (mới) → PIN Soft sắp/đã hết hạn (mới)→ GTTT đã hết hạn (cũ- đã golive)
            - Đối với KH Login type 1: KH có thể nhận được đủ tất cả các thông báo trên

            - Đối với KH Login type khác 1: Chỉ nhận được đươc thông báo GTTT đã hết hạn (cũ- đã golive)


