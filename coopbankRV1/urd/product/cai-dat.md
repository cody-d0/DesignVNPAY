# 📋 Nhóm cài đặt

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `product/`
> **Trích xuất:** 2026-03-28

---

## 19. URD_MB_COOPBANK_NHÓM CÀI ĐẶT

> **Page ID:** `29891071` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29891071

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*11 trang con:*

### 19.1. Các chức năng Cài đặt

> **Page ID:** `29900191` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29900191

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
22/02/2021  
 | A | HồngLT | 
 | 
Tạo mới
 | V.1.0
 | 
22/12/2023
 | M | ThuDM2 | V.1.0 | 
Bổ sung menu: Chia sẻ thông báo BĐSD
 | 

 | 
 
 | M | ThuDM2 | V.1.0 | 
Bổ sung menu: Thu thập sinh trắc học
 | 

1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: : KH, App Client, App Server.
• Điều kiện trước: 
• KH đăng nhập ứng dụng CoopBank MB thành công.
• Kết quả mong muốn:
• KH thao tác các chức năng trên màn hình cài đặt thành công.
#### 2/ Luồng màn hình

##### <MH1: Cài đặt>

##### MH2: Thông tin cá nhân

Mô tả màn hình

MH1: Cài đặt
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

 | 1 | Logo bank | Label | -- | -- | -- | 

 | 2 | Avatar | Label | -- | - | -- | 

 | 3 | Thông tin cá nhân | Label | -- | -- | -- | 

 | 4 | Quản lý thông báo | Label | -- | -- | -- | 

 | 5 | Chia sẻ thông báo BĐSD | Label | -- | -- | -- | 
Điều hướng đến <MH Đăng ký> của luồng Chia sẻ thông báo OTT BĐSD

Tham chiếu: 

 | 6 | Cài đặt vân tay/FaceID | Label | -- | -- | -- | 

 | 7 | Thu thập sinh trắc học | Label | -- | -- | -- | 

 | 8 | Quản lý danh bạ | Label | -- | -- | -- | 

 | 9 | Đổi mật khẩu | Label | -- | -- | -- | 

 | 10 | Cài đặt hạn mức chuyển tiền | Label | -- | -- | -- | 

 | 11 | Báo cáo giao dịch | Label | -- | -- | -- | 

 | 12 | Hỗ trợ | Label | -- | -- | -- | 

 | 13 | ATM chi nhánh | Label | -- | -- | -- | 

 | 14 | Thoát ứng dụng | Label | -- | -- | -- | 

3/ Mô tả xử lý
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhấn vào chức năng Thông tin cá nhân | Client | 
Hiển thị màn hình Thông tin cá nhân

 | 2 | Nhấn vào icon "Trợ lý ảo" | Client | 
Hiển thị màn hình chức năng trợ lý ảo sau đăng nhập

<Tham khảo tại chức năng "Trợ lý ảo">

 | 3 | Nhấn vào icon "Avatar" | 
Client

Server Media
 | 
Hiển thị popup với các lựa chọn:

• Đổi hình đại diện
• Đăng xuất
• Label text: Lần đăng nhập gần nhất: dd/mm/yyyy hh:mm:ss (thông tin do OMNI Server trả về)
 | 4 | Nhấn "Đổi hình đại diện" | Client | <Tham khảo logic xử lý tại chức năng "Đổi hình đại diện">

---

### 19.2. Cấu hình Soft OTP (GÓI 2)

> **Page ID:** `29896471` · **Version:** 6
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29896471

Bảng trạng thái soft

 | TT | Mã trạng thái | Tên trạng thái (VN) | Tên trạng thái (EN) | Mô tả case áp dụng
 | 1 | A | Chờ kích hoạt | Wait for active | KH đăng nhập kích hoạt tài khoản thành công nhưng chưa kích hoạt được SOFT OTP (kích hoạt Soft tự động lỗi)
 | 2 | 3 | Hoạt động (Kích hoạt) | Active | 
• KH đăng nhập kích hoạt tài khoản thành công và thực hiện kích hoạt SOFT OTP tự động thành công
• KH đăng ký Soft OTP trên app thành công (đăng ký chủ động)
• GDV chuyển trạng thái từ Khóa/Khóa tự động sang Hoạt động dưới backend
 | 3 | L | Khóa | Lock | GDV thực hiện chuyển trạng thái từ Hoạt động sang Khóa dưới backend
 | 4 | C | Khóa tự động | Auto lock | 
KH nhập xác thực SOFT PTP sai quá số lần quy định 

 | 5 | H | Hủy | Cancel | KH thực hiện hủy đăng ký SOFT OTP trên app (bỏ, giữ nguyên danh sách 4 trạng thái ban đầu)

---

*3 trang con:*

#### 19.2.1. Cài đặt Soft OTP

> **Page ID:** `29894854` · **Version:** 8
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29894854

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 | 
A
 | HongLT | 
 | 
Tạo mới
 | 

 | 
 
 | 
M
 | HongLT | 
 | 
Cập nhật:

• Bổ sung luồng Soft server lưu mã PIN
• Bổ sung logic Soft server check mã PIN mới không được trùng mã PIN cũ | 

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, MB Client, MB Server, Bank Server, Soft OTP Server.
• Điều kiện trước: 
• KH đã đăng nhập ứng dụng trên thiết bị di động thành công;
• Thiết bị của KH đủ điều kiện được phép kích hoạt SoftOTP:
• Không Root/Jaibreak/Hook hoặc Root/Jaibreak/Hook 
• Kết quả mong muốn:
• KH thực hiện cài đặt Soft OTP trong chức năng Cài đặt thành công.
2/ Luồng màn hình

<MH1> Các chức năng cài đặt

<MH2> Cài đặt Soft OTP

<MH3> Điều kiện, điều khoản

<MH4> Cài đặt PIN

<MH 4.1> Thông báo mã PIN mới không được trùng mã PIN cũ

<MH5> Xác thực cài đặt

<MH6.1> Kết quả cài đặt Soft OTP

<MH6.2> Kết quả cài đặt Soft OTP

3/ Mô tả màn hình

##### <MH1> Các chức năng cài đặt

##### <MH2> Cài đặt Soft OTP
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
Cài đặt Soft OTP

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn Back, hiển thị màn hình thao tác trước đó
 | 3 | Lưu ý 1 | Label | Read Only | -- | -- | 
Fix tại Client:

Soft OTP là phương thức xác thực đáp ứng yêu cầu của Ngân hàng nhà nước đối với các giao dịch trên ứng dụng Mobile Banking

 | 3 | Cài đặt Soft OTP | Label | Read Only | -- | -- | 
Hiển thị trạng thái ON/OFF tương ứng của khách hàng

 | 4 | Nội dung lưu ý 1 | Label | Read Only | -- | -- | 
Fix tại client:

"Để đảm bảo an toàn, ứng dụng chỉ cho phép sử dụng phương thức xác thực Soft OTP khi Quý khách đã thực hiện thành công {n} giao dịch tài chính bằng SMS OTP sau khi kích hoạt dịch vụ"

Lưu ý:

• n là tham số do MB Server trả về.
 | 5 | Nút "ON" | Button | Select | -- | -- | 
Được chọn khi trạng thái Soft OTP là "Chưa kích hoạt"

<Tham khảo logic xử lý>

 | 6 | Nút "OFF" | Button | Click | -- | -- | 
Được chọn khi trạng thái Soft OTP là "Đã kích hoạt"

<Tham khảo logic xử lý>

 | 7 | Quên PIN Soft OTP | Button Text | Click | -- | -- | 
Hiển thị nếu "Trạng thái Soft OTP = Active

Logic xử lý -->Tham khảo <>

##### MH3: Điều kiện, điều khoản sử dụng Soft OTP
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
##### Điều kiện, điều khoản sử dụng Soft OTP

 | 2 | 
Nội dung dạng html
 | HTML | Read Only | -- | -- | 
Hiển thị nội dung Bank cung cấp

 | 3 | Check box | Checkbox | Click | -- | -- | 
Nội dung "Tôi đã đọc, hiểu rõ, và cam kết tuân thủ các điều kiện, điều khoản sử dụng và thông tin hướng dẫn, quy định, lưu ý sử dụng phương thức xác thực dành cho khách hàng cá nhân của CoopBank"

Click để chọn

 | 4 | Đồng ý | Button | Click | -- | -- | Mặc định Disable. Khi Click vào check box Enable button Đồng ý. Mở đến MH Cài đặt mã PIN Soft OTP

##### MH4: Cài PIN
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

 | 1 | Tiêu đề | Label | Read Only | -- | -- | Cài mã PIN Soft OTP
 | 2 | 
Nhập mã PIN 
 | Textbox | Number | Yes | 6 | 
Mặc định trống;

Bàn phím số;

Hiển thị icon "Ẩn/Hiện" cho phép ẩn hiện ký tự PIN đã nhập. Mặc định Ẩn.

 | 3 | Nhập lại mã PIN  | Textbox | Number | Yes | 6 | 
Mặc định trống;

Bàn phím số;

Hiển thị icon "Ẩn/Hiện" cho phép ẩn hiện ký tự PIN đã nhập. Mặc định Ẩn.

Mã PIN nhập lại phải trùng với mã PIN

 | 4 | Label ghi chú | Label | Read Only | -- | -- | 
Hiển thị:

• Nhập mã PIN
• Quý khách ghi nhớ mã PIN Soft OTP đã đặt để thực hiện các giao dịch xác thực qua phương thức Soft OTP. Nếu quên PIN, vui lòng sử dụng chức năng "Quên PIN Soft OTP" trong cài đặt của ứng dụng để thực hiện đặt lại PIN mới.
 | 5 | Tiếp tục | Button | Click | -- | -- | <Tham khảo logic xử lý>

##### 
MH4: Xác thực cài đặt
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

 | 1 | Tiêu đề | Label | Read Only | -- | -- | Xác thực giao dịch
 | 2 | Ghi chú xác thực 1 | Label | Read Only | -- | -- | 
Hiển thị nội dung fix tại Client

• Quý khách vui lòng nhập mã OTP đã được gửi về số điện thoại 098*****23
 | 3 | Ô nhập OTP | Text | Number | Yes | 6 | 
Hiển thị 6 ô nhập ký tự OTP

Bàn phím số

Mặc định trống

 | 4 | Nút "Xác nhận" | Button | Link | -- | -- | 
Mặc định Enable

< Tham khảo logic xử lý>

##### MH5: Kết quả
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

 | 1 | Nội dung thông báo | Label | Read Only | -- | -- | 
• Giá trị tham số "Số lần sử dụng SMS trước khi sử dụng Soft OTP" của user nhỏ hơn tham số (n) đã cấu hình:
→ Hiển thị nội dung "Quý khách đã đăng ký phương thức xác thực Soft OTP thành công. Để đảm bảo an toàn, ứng dụng chỉ cho phép sử dụng phương thức xác thực Soft OTP khi Quý khách đã thực hiện thành công {n} giao dịch tài chính bằng SMS OTP sau khi kích hoạt dịch vụ"

• Giá trị tham số "Số lần sử dụng SMS trước khi sử dụng Soft OTP" của user lớn hoặc bằng tham số (n) đã cấu hình:
→ Hiển thị nội dung "Kích hoạt Soft OTP thành công. Các giao dịch tiếp theo của Quý khách sẽ được chuyển sang phương thức xác thực Soft OTP"

(Trường hợp KH Hủy cài đặt Soft OTP và cài đặt lại trên chính thiết bị cũ, số lần xác thực SMS OTP trước đó sẽ được kế thừa)

 | 2 | Icon thông báo | Label | Read Only | -- | -- | 

 | 3 | Nút Đóng | Button | Click | -- | -- | Click vào nút Đóng tắt Poup, 

4/ Luồng xử lý chi tiết

##### <MH1>Truy cập chức năng Cài đặt chọn Cài đặt Soft OTP
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn chọn chức năng Cài đặt Soft OTP tại mục cài đặt trên trang chủ
 | 
Client MB
 | 
Hiển thị màn hình Cài đặt Soft OTP

 (Trạng thái kích hoạt Soft OTP do MB Server trả về)

• Nếu server trả về trạng thái: "Khóa tự động" +"Đang bị khóa"+ "Kích hoạt" --> Hiển thị trạng thái cài đặt tại Client = ON 
• Nếu server trả về trạng thái: "Đã bị Hủy" + "Chờ kích hoạt" -->  Hiển thị Ttrạng thái cài đặt tại Client = OFF

##### <MH2>Cài đặt Soft OTP
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Tại màn hình Cài đặt Soft OTP, bật nút ON | Client | 
1/ Kiểm tra validate:

• Không hợp lệ: | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Chưa cài đặt mã bảo mật (Passcode) cho thiết bị | Quý khách chưa đặt mật khẩu mở điện thoại. Quý khách vui lòng đặt mật khẩu tại chức năng "Cài đặt" của điện thoại để tiếp tục sử dụng phương thức Soft OTP. | 

• Hợp lệ: Mở đến MH Điều kiện điều khoản, mặc định Disable nút Đồng ý. Khi Click vào check box Enable button Đồng ý. Mở đến MH Cài đặt mã PIN Soft OTP

##### MH4: Cài mã PIN Soft OTP
 | TT | Thao tác | Tác nhân | Mô tả
 | 1 | Nhập mã PIN/ Nhập lại mã PIN | Client | Hiển thị màn hình nhập mã PIN/ nhập lại mã PIN
 | 2

 | Nhập lại mã PIN, nhấn Tiếp tục

 | Client | 
1/ Kiểm tra validate:

• Không hợp lệ:  | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Mã PIN không trùng nhau | Mã PIN không trùng nhau. Quý khách vui lòng kiểm tra lại. | Ứng dụng hiển thị thông báo lỗi ở màn hình nhập mã PIN, mã PIN đã nhập vẫn được giữ nguyên
 | 2 | Không nhập mã PIN hoặc nhập mã PIN dưới 6 ký tự | Quý khách vui lòng nhập mã PIN bao gồm 6 ký tự số | Ứng dụng hiển thị thông báo lỗi ở màn hình nhập mã PIN, mã PIN đã nhập vẫn được giữ nguyên
 | 3 | Thiết bị Root/Jaibreak/Hook không cho phép kích hoạt | 
Kích hoạt Soft OTP không thành công do thiết bị của Quý khách không an toàn (Root/Jailbreak/Hook).
 | 

• Hợp lệ: Gửi yêu cầu khởi tạo kích hoạt Soft OTP sang Soft OTP Server thông qua MB Server
   (Client bổ sung truyền thêm mã PIN KH đặt dạng hash cho Server lưu mã PIN để mục đích Server Soft check mã PIN mới không được trùng với mã PIN cũ gần nhất)

 | Soft OTP Server | 
Kiểm tra điều kiện kích hoạt Soft OTP 

• Không hợp lệ: | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Soft OTP đang bị khóa (Auto Lock) | 
Sửa lại cấu hình nội dung câu thông báo → Bỏ câu Quý khách vui lòng thực hiện lại sau <dd/mm/yyyy hh:mm:ss>

Tài khoản của Quý khách bị khóa xác thực Soft OTP do nhập sai PIN quá số lần cho phép. Quý khách vui lòng thực hiện lại sau <dd/mm/yyyy hh:mm:ss>
 | 
• dd/mm/yyyy hh:mm:ss là tham số thời gian tự động mở khóa Soft OTP tại hệ thống Soft OTP. 
Trạng thái Soft OTP = Auto Lock không tự động mở lại cho đến khi được tác động mở khóa từ BE

 | 2 | Soft OTP đang bị khóa (Lock) | Tài khoản của Quý khách đang bị khóa xác thực Soft OTP. Quý khách vui lòng kiểm tra lại hoặc liên hệ tổng đài Co-op bank : xxxxx để được hỗ trợ. | 

 | 3 | 
Mã PIN mới trùng mã PIN cũ lưu gần nhất

(chỉ cần kiểm tra trùng PIN theo user, không cần kiểm tra trùng PIN theo cặp user+device)
 | Mã PIN mới không được trùng với mã PIN cũ. Quý khách vui lòng nhập lại mã PIN khác | 
• Soft server chỉ check được logic này nếu trước đó, KH đã upodate app và Client đã truyền mã PIN cho server lưu.
• Nếu KH chưa update app thì Client sẽ chưa truyền mã PIN cũ xuống cho Soft server lưu nên mã PIN cũ= Null → Khi KH đặt mã PIN mới sẽ không check được mã PIN mới trùng với mã PIN cũ, và sẽ không trả được thông báo này

• Hợp lệ:→ Lưu mã PIN Soft OTP (theo user) do Client truyền xuống→  Sinh OTP và gửi yêu cầu gửi SMS OTP tới hệ thống SMS gateway thông qua MB server
 | SMS gateway | 
• Hệ thống Gateway xử lý gửi SMS
• Trả phản hồi kết quả SMS OTP cho Soft OTP Server
 | Soft OTP Server | 
Nhận kết quả phản hồi từ SMS gateway

• Không nhận được phản hồi từ hệ thống Bank server: Trả về mã lỗi và nội dung thông báo lỗi timeout.
• Không thành công: Trả về mã lỗi và nội dung thông báo lỗi tương ứng để Client hiển thị popup thông báo lỗi.
• Thành công: Trả về kết quả để client hiển thị màn hình xác nhận OTP
 | Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng
• Thành công:
• Hiển thị màn hình xác nhận OTP cài đặt Soft OTP

##### MH5: Xác thực cài đặt Soft OTP bằng SMS OTP
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1

 | Nhấn "Xác nhận"

 | Client | 
1/ Kiểm tra validate:

• Không hợp lệ: | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Bỏ trống OTP | Mã OTP không được để trống | 

 | 2 | OTP nhỏ hơn 6 ký tự | Mã OTP phải bao gồm 6 ký tự | 

• Hợp lệ: Gửi yêu cầu xác nhận kích hoạt Soft OTP sang Soft OTP Server thông qua MB Server
 | Soft OTP Server | 
1/ Kiểm tra OTP:

• Không hợp lệ:  | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | OTP sai | Mã OTP không chính xác. Quý khách vui lòng kiểm tra lại. | Tắt thông báo giữ nguyên màn hình đang thao tác
 | 2 | OTP hết hiệu lực | Mã OTP đã hết hiệu lực. Quý khách vui lòng thực hiện lại. | Tắt thông báo hiển thị màn hình thao tác trước đó

• Hợp lệ: Chuyển bước 2
2/ Xử lý kích hoạt Soft OTP cho user theo thiết bị (lưu trạng thái cài PIN) và trả kết quả cho Client thông qua MB Server

 | Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng
• Thành công:
• Hiển thị thông báo kích hoạt Soft OTP thành công do Server trả về (Hiển thị MH 6.1 hoặc MH 6.2 tương ứng)
• Nhấn "Đóng" để tắt Popup

---

#### 19.2.2. Hủy cài đặt Soft OTP

> **Page ID:** `29894910` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29894910

####  1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, MB Client, MB Server, Bank Server, Soft OTP Server.
• Điều kiện trước: 
• KH đã đăng nhập ứng dụng trên thiết bị di động thành công;
• KH muốn Hủy cài đặt Soft OTP
• Kết quả mong muốn:
• KH thực hiện hủy cài đặt Soft OTP trong chức năng Cài đặt thành công.
#### 3/ Luồng màn hình

##### MH1: Cài đặt Soft OTP

##### MH2: Xác nhận Hủy

##### MH3: Nhập PIN

MH4: Kết quả cài đặt

MH1: Cài đặt Soft OTP

• Tham khảo tại chức năng 
##### MH2: Xác nhận Hủy
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

 | 1 | Icon thông báo | Lable | ReadOnly | -- | -- | Hiển thị icon thông báo 
 | 2 | Nội dung thông báo | Label | Read Only | -- | -- | 
Nội dung fix tại client:

Quý khách có chắc chắn vẫn muốn hủy phương thức xác thực bằng Soft OTP không? Và 2 lựa chọn:

• Không
• Có
 | 3 | Nút "Không" | Button | Click | -- | -- | Nhấn Không, hiển thị màn hình đang thao tác trước đó
 | 4 | Nút "Có" | Button | Click | -- | -- | 
Mặc định Enable

<Tham khảo logic xử lý>

##### MH3: Nhập PIN Soft OTP
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

 | 1 | Tiêu đề | Label | Read Only | -- | -- | Xác thực giao dịch
 | 2 | Ghi chú 1 | Label | Read Only | -- | -- | "Vui lòng nhập mã PIN của Soft OTP để xác thực giao dịch"
 | 3 | Nhập mã PIN | Textbox | Number | Yes | 6 | 
Mặc định trống

Bàn phím số

Cho phép nhập mã PIN Soft OTP tối đa 6 ký tự.

Mã hóa ký tự nhập vào bằng ký tự *

 | 4 | Ghi chú 2 | Label | Read Only | -- | -- | 
Lưu ý: Soft OTP sẽ bị khóa nếu Quý khách nhập sai PIN {n} lần liên tiếp

##### MH4: Poup Kết quả
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

 | 1 | Nội dung thông báo Hủy thành công | Label | Read Only | -- | -- | 
Hiển thị nội dung "Quý khách đã hủy phương thức xác thực bằng Soft OTP thành công. Vui lòng đăng nhập lại ứng dụng"

Và nút Đóng

 | 2 | Nút "Đóng" | Button | Click | -- | -- | Nhấn Đóng, tắt thông báo

#### 4/ Luồng xử lý chi tiết

##### MH1: Cài đặt Soft OTP
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Bật chức năng OFF để Hủy cài đặt Soft OTP | Client | 
Hiển thị thông báo xác nhận như mô tả

##### (MH2+MH3):  Xác nhận Hủy + Nhập mã PIN
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Nhấn xác nhận "Có" hủy Soft OTP (MH3) | Client | 
• Hiển thị màn hình nhập mã PIN Soft OTP (màn hình MH3) → Chuyển thao tác Nhập mã PIN
 | 2 | Nhập mã PIN

 | Client | 
1/ Kiểm tra validate:

• Không hợp lệ: Hiển thị trường hợp lỗi tương ứng tại  | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Mã PIN sai | 
Mã PIN không chính xác. Quý khách còn n lần thử

• n là số lần đếm ngược được phép sai PIN còn lại | Hiển thị dạng Popup
 | 2 | Sai 5 lần mã PIN liên tiếp | Quý khách đã nhập mã PIN sai quá số lần quy định. Quý khách vui lòng thực hiện giao dịch lại sau. | 

 | 3 | Nhập mã PIN sau khi bị khóa Soft OTP tự động | Tài khoản của Quý khách đang tạm thời bị khóa phương thức xác thực Soft OTP do nhập PIN sai quá số lần quy định. | 

 | 4 | Nhập mã PIN sau khi bị khóa Soft OTP trên BE | Tài khoản của Quý khách đang bị khóa xác thực Soft OTP. Quý khách vui lòng kiểm tra lại hoặc liên hệ tổng đài CoopBank <xxxxxx> để được hỗ trợ | 

• Hợp lệ: Gửi yêu cầu hủy Soft OTP sang Soft OTP Server thông qua MB Server
 | MB Server | 
 Gửi yêu cầu hủy Soft OTP sang Soft OTP Server

 | Soft OTP Server | 
Thực hiện hủy Soft OTP và trả kết quả cho MB Server. Lưu trạng thái Soft OTP = OFF

Lưu bản ghi Hủy Soft vào bảng History để thực hiện tra cứu lịch sử hủy Soft otp trên BE

 | MB Server | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng (gián đoạn/timeout)
• Thành công:Trả kết quả về cho Client
 | Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng
• Thành công:
• Hiển thị thông báo hủy Soft OTP thành công (MH5). Đóng thông báo, hiển thị màn hình Login, yêu cầu KH đăng nhập lại

---

#### 19.2.3. Quên PIN Soft OTP

> **Page ID:** `29894930` · **Version:** 8
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29894930

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 | 
A
 | HongLT | 
 | 
Tạo mới
 | 

 | 
 
 | 
M
 | HongLT | 
 | 
Cập nhật:

• Bổ sung luồng Soft server lưu mã PIN
• Bổ sung logic Soft server check mã PIN mới không được trùng mã PIN cũ | 

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, MB Client, MB Server, Bank Server, Soft OTP Server.
• Điều kiện trước: 
• KH đã đăng nhập ứng dụng thành công;
• KH đã kích hoạt Soft OTP thành công;
• KH thực hiện yêu cầu "Quên PIN Soft OTP" trong chức năng "Cài đặt".
• Kết quả mong muốn:
• KH được yêu cầu cài đặt lại SmartOTP và cài mã PIN mới theo thông báo tại trang chủ ứng dụng;
• KH thực hiện cài đặt lại SmartOTP và mã PIN mới thành công.
2/ Luồng màn hình

Đường dẫn tới chức năng:

• Home → Cài đặt Soft OTP → Quên PIN Soft OTP
• Home → Cài đặt → Cài đặt Soft OTP → Quên PIN Soft OTP
<MH1> Cài đặt

<MH2> Cài đặt Soft OTP

MH3: Nhập mật khẩu ứng dụng

<MH4> Cài đặt lại mã PIN

<MH5> Xác thực SMS OTP

<MH6.1 Kết quả>

<MH6.2> Kết quả

#### Mô tả:

##### MH1, MH2: Các chức năng Cài đặt. Chức năng Quên PIN Soft OTP nằm trong thư mục Cấu hình Soft OTP. Bấm vào Quên PIN Soft OTP mở đến MH2: Nhập mật khẩu ứng dụng để xác nhận Quên PIN

##### MH3: Nhập mật khẩu ứng dụng để xác nhận Quên PIN
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

 | 1 | Icon thông báo | Label | Read Only | -- | -- | Hiển thị icon 
 | 2 | Nội dung thông báo | Label | Read Only | -- | -- | 
Hiển thị nội dung:

Để thực hiện đặt lại PIN mới, Quý khách cần nhập lại mật khẩu đăng nhập ứng dụng và thực hiện cài đặt Soft OTP

 | 3 | 
Nhập mật khẩu ứng dụng
 | Textbox | Text | Yes | 20 | 
Mật khẩu hợp lệ: Từ 8 – 20 ký tự, còn các điều kiện khác tại server quy định.

Không cho nhập ký tự có dấu, dấu cách.

Mã hóa ký tự nhập vào bằng ký tự *

 | 4 | Nút Tiếp tục | Button | Click | -- | -- | 
Tiếp tục: <Tham khảo logic xử lý>

 | 5 | Nút Hủy | Button | Click | 
 | 
 | 
Nhấn "Hủy", tắt thông báo và hiển thị màn hình thao tác trước đó

##### 
MH4: Cài PIN
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

 | 1 | Tiêu đề | Label | Read Only | -- | -- | Cài mã PIN Soft OTP
 | 2 | 
Nhập mã PIN 
 | Textbox | Number | Yes | 6 | 
Mặc định trống;

Bàn phím số;

Hiển thị icon "Ẩn/Hiện" cho phép ẩn hiện ký tự PIN đã nhập. Mặc định Ẩn.

 | 3 | Nhập lại mã PIN  | Textbox | Number | Yes | 6 | 
Mặc định trống;

Bàn phím số;

Hiển thị icon "Ẩn/Hiện" cho phép ẩn hiện ký tự PIN đã nhập. Mặc định Ẩn.

Mã PIN nhập lại phải trùng với mã PIN

 | 4 | Label ghi chú | Label | Read Only | -- | -- | 
Hiển thị:

• Nhập mã PIN
• Quý khách ghi nhớ mã PIN Soft OTP đã đặt để thực hiện các giao dịch xác thực qua phương thức Soft OTP. Nếu quên PIN, vui lòng sử dụng chức năng "Quên PIN Soft OTP" trong cài đặt của ứng dụng để thực hiện đặt lại PIN mới.
 | 5 | Tiếp tục | Button | Click | -- | -- | <Tham khảo logic xử lý>

##### 
MH5: Xác thực SMS OTP
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

 | 1 | Tiêu đề | Label | Read Only | -- | -- | Xác thực giao dịch
 | 2 | Ghi chú xác thực 1 | Label | Read Only | -- | -- | 
Hiển thị nội dung fix tại Client

• Quý khách vui lòng nhập mã OTP đã được gửi về số điện thoại 098*****23
 | 3 | Ô nhập OTP | Text | Number | Yes | 6 | 
Hiển thị 6 ô nhập ký tự OTP

Bàn phím số

Mặc định trống

 | 4 | Nút "Xác nhận" | Button | Link | -- | -- | 
Mặc định Enable

<Tham khảo Logic xử lý>

##### 
MH.6.: Kết quả
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

 | 1 | Nội dung thông báo | Label | Read Only | -- | -- | 
• Giá trị tham số "Số lần sử dụng SMS trước khi sử dụng Soft OTP" của user nhỏ hơn tham số (n) đã cấu hình:
→ Hiển thị nội dung "Quý khách đã đăng ký phương thức xác thực Soft OTP thành công. Để đảm bảo an toàn, ứng dụng chỉ cho phép sử dụng phương thức xác thực Soft OTP khi Quý khách đã thực hiện thành công {n} giao dịch tài chính bằng SMS OTP sau khi kích hoạt dịch vụ"

• Giá trị tham số "Số lần sử dụng SMS trước khi sử dụng Soft OTP" của user lớn hoặc bằng tham số (n) đã cấu hình:
→ Hiển thị nội dung "Kích hoạt Soft OTP thành công. Các giao dịch tiếp theo của Quý khách sẽ được chuyển sang phương thức xác thực Soft OTP"

 | 2 | Icon thông báo | Label | Read Only | -- | -- | 

 | 3 | Nút Đóng | Button | Click | -- | -- | Click vào nút Đóng tắt Poup,

#### 4/ Luồng xử lý chi tiết

##### MH1: Các chức năng cài đặt

##### MH2: Thông báo xác nhận
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1

 | Nhập mật khẩu và "Tiếp tục"

 | Client | 
Kiểm tra

• Không hợp lệ: | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Bỏ trống mật khẩu | Mật khẩu không được để trống | 

 | 2 | Mật khẩu nhỏ hơn 8 ký tự | Mật khẩu là chuỗi tối thiểu 8 ký tự | 

• Hợp lệ: Gửi yêu cầu xác thực mật khẩu sang MB Server
 | MB Server | 
Xác thực mật khẩu

• Không hợp lệ: Trả kết quả cho Client nếu mật khẩu sai, hoặc sai quá n lần cho phép trong phiên giao dịch
• Hợp lệ: Trả kết quả cho Client
 | Client | 
Nhận kết quả:

• Thành công:
• Hiển thị màn hình Cài đặt PIN
• Không thành công: Hiển thị thông báo lỗi tương ứng server trả về | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Mật khẩu sai | Mật khẩu không đúng. Quý khách vui lòng thử lại | 

 | 2 | Mật khẩu  sai quá (n) lần cho phép trong phiên giao dịch (luồng xác thực) | Quý khách nhập mật khẩu sai quá [n] lần cho phép. Quý khách vui lòng nhập đăng nhập lại để thực hiện chức năng này.
 | Đóng Popup  điều hướng về MH login. KH login lại đúng thì vào MH Home

##### MH3: Xác nhận PIN
 | TT | Thao tác | Tác nhân | Mô tả
 | 2

 | Nhập mã PIN/ Xác nhận mã PIN bấm Tiếp tục

 | Client | 
1/ Kiểm tra validate:

• Không hợp lệ:  | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Mã PIN không trùng nhau | Mã PIN không trùng nhau. Quý khách vui lòng kiểm tra lại. | Ứng dụng hiển thị thông báo lỗi ở màn hình nhập mã PIN, mã PIN đã nhập vẫn được giữ nguyên
 | 2 | Không nhập mã PIN hoặc nhập mã PIN dưới 6 ký tự | Quý khách vui lòng nhập mã PIN bao gồm 6 ký tự số | Ứng dụng hiển thị thông báo lỗi ở màn hình nhập mã PIN, mã PIN đã nhập vẫn được giữ nguyên

• Hợp lệ: Gửi yêu cầu khởi tạo kích hoạt Soft OTP sang Soft OTP Server thông qua MB Server
(Client bổ sung truyền thêm mã PIN KH đặt dạng hash cho Server lưu mã PIN để mục đích Server Soft check mã PIN mới không được trùng với mã PIN cũ gần nhất)

 | Soft OTP Server | 
1/ Trạng thái Soft OTP ghi nhận = Chờ kích hoạt

2/ Kiểm tra điều kiện kích hoạt Soft OTP

• Không hợp lệ: | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Thiết bị Root/Jaibreak/Hook không cho phép kích hoạt | Kích hoạt Soft OTP không thành công do thiết bị của Quý khách không an toàn (Root/Jailbreak/Hook). | 

 | 2 | Soft OTP đang bị khóa (Auto Lock) | 
Sửa lại cấu hình nội dung câu thông báo → Bỏ câu Quý khách vui lòng thực hiện lại sau <dd/mm/yyyy hh:mm:ss>

Tài khoản của Quý khách bị khóa xác thực Soft OTP do nhập sai PIN quá số lần cho phép. Quý khách vui lòng thực hiện lại sau <dd/mm/yyyy hh:mm:ss>
 | 
• dd/mm/yyyy hh:mm:ss là tham số thời gian tự động mở khóa Soft OTP tại hệ thống Soft OTP. 
Trạng thái Soft OTP = Auto Lock không tự động mở lại cho đến khi được tác động mở khóa từ BE

 | 3 | Soft OTP đang bị khóa (Lock) | Tài khoản của Quý khách đang bị khóa xác thực Soft OTP. Quý khách vui lòng kiểm tra lại hoặc liên hệ tổng đài Co-op bank : xxxxx để được hỗ trợ. | 

 | 4 | 
Mã PIN mới trùng mã PIN cũ lưu gần nhất

(chỉ cần kiểm tra trùng PIN theo user, không cần kiểm tra trùng PIN theo cặp user+device)
 | Mã PIN mới không được trùng với mã PIN cũ. Quý khách vui lòng nhập lại mã PIN khác | 
• Soft server chỉ check được logic này nếu trước đó, KH đã upodate app và Client đã truyền mã PIN cho server lưu.
• Nếu KH chưa update app thì Client sẽ chưa truyền mã PIN cũ xuống cho Soft server lưu nên mã PIN cũ= Null → Khi KH đặt mã PIN mới sẽ không check được mã PIN mới trùng với mã PIN cũ, và sẽ không trả được thông báo này

• Hợp lệ: →  Lưu mã PIN Soft OTP (theo user) do Client truyền xuống → Chuyển bước 3
3/ Sinh OTP gửi tới số điện thoại KH thông qua Bank Server và trả kết quả về cho ứng dụng thông qua MB Server

 | Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng
• Thành công:
• Hiển thị màn hình xác nhận OTP

##### MH4: Xác nhận OTP
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1

 | Nhấn "Xác nhận"

 | Client | 
1/ Kiểm tra validate:

• Không hợp lệ: | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Bỏ trống OTP | Mã OTP không được để trống | 

 | 2 | OTP nhỏ hơn 6 ký tự | Mã OTP phải bao gồm 6 ký tự | 

• Hợp lệ: Gửi yêu cầu xác nhận kích hoạt Soft OTP sang Soft OTP Server thông qua MB Server
 | Soft OTP Server | 
1/ Kiểm tra OTP:

• Không hợp lệ:  | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | OTP sai | Mã OTP không chính xác. Quý khách vui lòng kiểm tra lại. | Tắt thông báo giữ nguyên màn hình đang thao tác
 | 2 | OTP hết hiệu lực | Mã OTP đã hết hiệu lực. Quý khách vui lòng thực hiện lại. | Tắt thông báo hiển thị màn hình thao tác trước đó

• Hợp lệ: Chuyển bước 2
2/ Xử lý kích hoạt Soft OTP cho user theo thiết bị (lưu trạng thái cài PIN) và trả kết quả cho Client thông qua MB Server

 | Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng
• Thành công:
• Hiển thị thông báo kích hoạt Soft OTP thành công do Server trả về.
Nhấn "Đóng": Hiển thị màn hình trang chủ ứng dụng.

#####

---

### 19.3. Quản lý thông báo OTT (GÓI 2)

> **Page ID:** `29896469` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29896469

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*4 trang con:*

#### 19.3.1. Hủy đăng ký OTT BĐSD

> **Page ID:** `29896478` · **Version:** 8
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29896478

| Phiên bản tài liệu
 | 
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 | A | Honglt | 
 | 
Tạo mới tài liệu
 | 
V.1.0.0

 |   | M | ThaoCY | V.1.0.0 | 
MB server: Khi hủy đăng ký OTT BĐSD tự động hủy Voice OTT
 | 
V.1.0.1

 | Mục lục
 | 

1. Tác nhân, điều kiện trước, kết quả mong muốn

- Tác nhân tham gia: KH, MB Client, MB Server, Gateway Server (Đăng ký OTTBĐSD)

- Điều kiện trước: 

• KH thực hiện đăng nhập ứng dụng thành công
• KH đang bật tính năng OTT Biến động số dư
- Kết quả mong muốn:

• Hệ thống Bank (Gateway Server) hủy đăng ký tính năng OTT Biến động số dư thành công cho user (theo CIF)
2. Luồng màn hình

<MH 1> Cài đặt

<MH 2> Quản lý thông báo

<MH3> Xác nhận hủy

<MH4> Xác thực bằng SMS OTP

<MH5.1> Nhập PIN Soft OTP

<MH5.2> Xác thực giao dịch

<MH6> Kết quả hủy

3. Mô tả màn hình

<MH1> Cài đặt Hủy OTT trong chức năng Cài đặt tại trang chủ

<MH2> Quản lý thông báo

<MH3>: Xác nhận Hủy
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

 | 1 | Icon thông báo | Lable | ReadOnly | -- | -- | Hiển thị icon thông báo 
 | 2 | Nội dung thông báo | Label | Read Only | -- | -- | 
Nội dung fix tại client:

Quý khách có chắc chắn vẫn muốn hủy dịch vụ nhận tin Biến động số dư trên ứng dụng? Và 2 lựa chọn:

• Không
• Có
 | 3 | Nút "Không" | Button | Click | -- | -- | Nhấn Không, hiển thị màn hình đang thao tác trước đó
 | 4 | Nút "Có" | Button | Click | -- | -- | 
Mặc định Enable

<Tham khảo logic xử lý>

<MH4> Xác thực bằng SMS OTP

Hiển thị màn hình xác thực bằng SMS OTP với trường hợp:

• KH chưa cài đặt kích hoạt Soft OTP
• KH đã cài đặt kích hoạt Soft OTP nhưng chưa thực hiện đủ (n ) giao dịch bằng SMS OTP
<MH5.1> Nhập mã PIN

<MH5.2>Xác thực bằng Soft OTP 

Hiển thị màn hình xác thực bằng Soft OTP với trường hợp:

• KH đã đăng ký Soft OTP và đã thực hiện đủ (n ) giao dịch bằng SMS OTP
<MH 6> Kết quả đăng ký
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

 | 1 | Icon | Icon | Readonly | -- | -- | Thành công
 | 2 | 
Nội dung
 | Lable | Readonly | -- | -- | 
Quý khách đã Hủy dịch vụ nhận tin Biến động số dư trên ứng dụng thành công

 | 3 | Nút Đóng | Button | 
Click
 | -- | -- | Tắt popup

4. Luồng xử lý chi tiết

<MH1+MH2> Cài đặt
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn chọn chức năng Cài đặt > Quản lý thông báo trên trang chủ
 | 
MB Client
 | 
Hiển thị màn hình Quản lý thông báo

Trạng thái đăng ký OTT BĐSD (Đã đăng ký/ Chưa đăng ký) do MB Server trả về

<MH2> Màn hình Quản lý thông báo
 | TT | Thao tác | Tác nhân | Mô tả
 | 1

 | 
Nhấn Hủy đăng ký
 | 
Client
 | 
Hiển thị thông báo xác nhận hủy như mô tả.

• Chọn "Không" → Tắt thông báo và về màn hình trước
• Chọn "Có" → Gửi yêu cầu Hủy OTT BĐSD cho MB Server
 | MB Server | 
1/ Kiểm tra trạng thái Soft OTP của user

• Nếu KH đã kích hoạt Soft OTP → Chuyển bước 2
• Nếu KH chưa kích hoạt Soft OTP → Server xác định PTXT là SMS OTP
2/ Kiểm tra số lần giao dịch xác thực bằng SMS OTP thành công trước đó

• 
Nếu số lần xác thực SMS OTP < (n ) → Server xác định PTXT là SMS OTP  → Chuyển bước 3

• Nếu số lần xác thực SMS OTP >= (n ) → Server xác định PTXT ưu tiên nhất do Server trả về là Soft OTP → Chuyển bước xác thực bằng Soft OTP
• Nếu trạng thái Soft OTP = Lock/ AutoLock → Server xác định PTXT là SMS OTP → Chuyển bước 3
(Tham khảo Logic xác định PTXT của GD phi tài chính tại )

3/ MB Server thực hiện sinh OTP và gửi yêu cầu cho SMS gateway VNPAY để gửi SMS OTP cho KH

4/ Hệ thống SMS gateway VNPAY trả kết quả phản hồi gửi SMS OTP cho MB server

5/ MB Server nhận phản hồi:

• Không nhận được phản hồi từ hệ thống Bank server: Trả về mã lỗi và nội dung thông báo lỗi timeout.
• Không thành công: Trả về mã lỗi và nội dung thông báo lỗi tương ứng để Client hiển thị popup thông báo lỗi.
• Thành công: Trả về kết quả để client hiển thị màn hình xác 
{n} là số lần xác thực SMS OTP trước khi xác thực bằng Soft OTP

 | 
 Client
 | 
Nhận kết quả thông qua MB Server:

•    Thành công: Hiển thị màn hình xác nhận OTP để đăng ký dịch vụ
•    Không thành công: Hiển thị thông báo lỗi theo quy tắc chung

<MH4.1>  Xác thực bằng SMS OTP
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1

 | Nhấn "Xác nhận"

 | Client | 
1/ Kiểm tra validate:

• Không hợp lệ: | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Bỏ trống OTP | Mã OTP không được để trống | 

 | 2 | OTP nhỏ hơn 6 ký tự | Mã OTP phải bao gồm 6 ký tự | 

• Hợp lệ: Gửi yêu cầu xác nhận đăng ký OTT BĐSD sang MB Server
 | MB Server | 
1/ Kiểm tra OTP:

• Không hợp lệ:  | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | OTP sai | Mã OTP không chính xác. Quý khách vui lòng kiểm tra lại. | Tắt thông báo giữ nguyên màn hình đang thao tác
 | 2 | OTP hết hiệu lực | Mã OTP đã hết hiệu lực. Quý khách vui lòng thực hiện lại. | Tắt thông báo hiển thị màn hình thao tác trước đó

• Hợp lệ: Chuyển bước 2
2/ Gửi yêu cầu hủy đăng ký OTT BĐSD tới hệ thống quản lý OTT của Bank

 | Gateway Bank (OTT) | Xử lý hủy đăng ký OTT BĐSD cho KH và trả KQ cho MB Server
 | MB Server | 
Nhận kết quả và trả về cho Client

• Thành công: Cập nhật trạng thái OTT BĐSD = Hủy đăng ký (OFF) và trả KQ hủy thành công cho MB Client
• Không thành công: Trả về thông báo lỗi cho Client
 | MB Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng
• Thành công:
• Hiển thị thông báo "Quý khách đã Hủy dịch vụ nhận tin Biến động số dư trên ứng dụng thành công"

<MH4.2> Xác thực bằng Soft OTP
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn "Xác nhận"
 | 
 | 
Tham khảo logic xử lý tại < Xác thực bằng Soft OTP>. 

Soft OTP Server trả kết quả xác thực cho MB Server

 | 
 | 
 | MB Server | Gửi yêu cầu hủy đăng ký OTT BĐSD tới hệ thống quản lý OTT của Bank
 | 
 | 
 | Gateway Bank (OTT) | Xử lý hủy đăng ký OTT BĐSD cho KH và trả KQ cho MB Server
 | 
 | 
 | MB Server | 
Nhận kết quả và trả về cho Client

• Thành công:
• Cập nhật trạng thái OTT BĐSD = Hủy đăng ký (OFF)
• Xóa dữ liệu khỏi bảng OMNI_VOICE_OTT_ACC, insert dữ liệu vào bảng OMNI_VOICE_OTT_ACC_HIS với  trạng thái Voice OTT = Hủy tự động (2)
• Trả KQ hủy thành công cho MB Client
• Không thành công: Trả về thông báo lỗi cho Client
 | 
 | 
 | MB Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng
• Thành công:
• Hiển thị thông báo "Quý khách đã Hủy dịch vụ nhận tin Biến động số dư trên ứng dụng thành công"

<MH5>  Màn hình thông báo kết quả
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn “Đóng” tại màn hình kết quả thành công
 | 
MB Client
 | 
Hiển thị màn hình Quản lý thông báo trên ứng dụng với trạng thái hủy đăng ký

---

#### 19.3.2. Đăng ký OTT BĐSD

> **Page ID:** `29896476` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29896476

1. Tác nhân, điều kiện trước, kết quả mong muốn

- Tác nhân tham gia: KH, MB Client, MB Server, Gateway Server (Đăng ký OTTBĐSD)

- Điều kiện trước: 

• KH đang sử dụng bản ứng dụng có tính năng OTT Biến động số dư
• KH thực hiện đăng nhập ứng dụng thành công
• KH đang tắt tính năng OTT Biến động số dư
- Kết quả mong muốn:

• Hệ thống Bank (Gateway Server) đăng ký tính năng OTT Biến động số dư thành công cho user (theo CIF)
2. Luồng màn hình

MH 1: Cài đặt

MH 2: Đăng ký OTT BĐSD

MH3.1: Nhập PIN

MH 3.2 Xác thực bằng Soft OTP

MH4: Xác thực bằng SMS OTP

MH 5: Kết quả đăng ký

<MH2> Đăng ký OTT BĐSD
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
Quản lý thông báo

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn Back, hiển thị màn hình thao tác trước đó
 | 3 | Lưu ý 1 | Label | Read Only | -- | -- | 
Fix tại Client:

"Khi đăng ký dịch vụ, Quý khách có thể nhận thông báo biến động số dư ngay trên ứng dụng"

 | 3 | Nhận thông báo BĐSD trên ứng dụng (miễn phí) | Label | Read Only | -- | -- | 
Hiển thị trạng thái ON/OFF tương ứng của khách hàng

 | 4 | Nút "ON" | Button | Select | -- | -- | 
Được chọn khi trạng thái OTTBĐSD là "Chưa đăng ký"

<Tham khảo logic xử lý>

 | 5 | Nút "OFF" | Button | Click | -- | -- | 
Được chọn khi trạng thái OTTBĐSD là "Đã đăng ký"

<Tham khảo logic xử lý>

<MH3.1> Nhập PIN
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

 | 1 | Tiêu đề | Label | Read Only | -- | -- | Xác thực giao dịch
 | 2 | Ghi chú 1 | Label | Read Only | -- | -- | "Vui lòng nhập mã PIN của Soft OTP để xác thực giao dịch"
 | 3 | Nhập mã PIN | Textbox | Number | Yes | 6 | 
Mặc định trống

Bàn phím số

Cho phép nhập mã PIN Soft OTP tối đa 6 ký tự.

Mã hóa ký tự nhập vào bằng ký tự *

 | 4 | Ghi chú 2 | Label | Read Only | -- | -- | 
Lưu ý: Soft OTP sẽ bị khóa nếu Quý khách nhập sai PIN {n} lần liên tiếp

<MH3.2> Xác thực bằng Soft OTP

Hiển thị màn hình xác thực bằng Soft OTP với trường hợp:

• KH đã đăng ký Soft OTP và đã thực hiện đủ (n ) giao dịch bằng SMS OTP
<MH4> Xác thực bằng SMS OTP

Hiển thị màn hình xác thực bằng SMS OTP với trường hợp:

• KH chưa cài đặt kích hoạt Soft OTP
• KH đã cài đặt kích hoạt Soft OTP nhưng chưa thực hiện đủ (n ) giao dịch bằng SMS OTP
<MH 5> Kết quả đăng ký
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

 | 1 | Icon | Icon | Readonly | -- | -- | Thành công
 | 2 | 
Nội dung
 | Lable | Readonly | -- | -- | 
Quý khách đã Đăng ký dịch vụ nhận tin Biến động số dư trên ứng dụng thành công

 | 3 | Nút Đóng | Button | 
Click
 | -- | -- | Tắt popup

#### 3. Luồng xử lý chi tiết

<MH1+MH2> Cài đặt
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn chọn chức năng Cài đặt > Quản lý thông báo trên trang chủ
 | 
MB Client
 | 
Hiển thị màn hình Quản lý thông báo

Trạng thái đăng ký OTT BĐSD (Đã đăng ký/ Chưa đăng ký) do MB Server trả về

<MH2> Quản lý thông báo
 | TT | Thao tác | Tác nhân | Mô tả
 | 1

 | 
Nhấn đăng ký dịch vụ
 | 
Client
 | 
Kiểm tra cài đặt thông báo trên thiết bị

• Không hợp lệ: Trường hợp: Thiết bị đang tắt tính năng nhận thông báo trên ứng dụng: Client HIển thị thông báo: "Để thực hiện tính năng này. Quý khách vui lòng vào mục cài đặt tại thiết bị bật tính năng nhận thông báo trên ứng dụng" 
• Nút đồng ý: Mở màn hình cài đặt cho phép bật tính năng nhận thông báo trên ứng dụng
• Nút Hủy: Thoát khỏi popup hiển thị màn hình thông báo BĐSD trên ứng dụng
• Hợp lệ: Gửi yêu cầu kích hoạt OTT Biến động số dư sang MB Server ,
 | MB Server | 
 1/ Kiểm tra trạng thái Soft OTP của user

• Nếu KH đã kích hoạt Soft OTP → Chuyển bước 2
• Nếu KH chưa kích hoạt Soft OTP → Server xác định PTXT là SMS OTP
2/ Kiểm tra số lần giao dịch xác thực bằng SMS OTP thành công trước đó

• 
Nếu số lần xác thực SMS OTP < (n ) → Server xác định PTXT là SMS OTP  → Chuyển bước 3

• Nếu số lần xác thực SMS OTP >= (n ) → Server xác định PTXT ưu tiên nhất do Server trả về là Soft OTP → Chuyển bước xác thực bằng Soft OTP
• Nếu trạng thái Soft OTP = Lock/ AutoLock → Server xác định PTXT là SMS OTP → Chuyển bước 3
(Tham khảo logic chung <>)

3/ MB Server thực hiện sinh OTP và gửi yêu cầu cho hệ thống SMS gateway VNPahy để gửi SMS OTP cho KH

4/ Hệ thống SMS gateway trả kết quả phản hồi gửi SMS OTP cho MB server

5/ MB Server nhận phản hồi:

• Không nhận được phản hồi từ hệ thống Bank server: Trả về mã lỗi và nội dung thông báo lỗi timeout.
• Không thành công: Trả về mã lỗi và nội dung thông báo lỗi tương ứng để Client hiển thị popup thông báo lỗi.
• Thành công: Trả về kết quả để client hiển thị màn hình xác 
{n} là số lần xác thực SMS OTP trước khi xác thực bằng Soft OTP

 | 
 Client
 | 
Nhận kết quả thông qua MB Server:

•    Thành công: Hiển thị màn hình xác nhận OTP để đăng ký dịch vụ
•    Không thành công: Hiển thị thông báo lỗi theo quy tắc chung

<MH3.1> Xác thực bằng Soft OTP
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn "Xác nhận"
 | 
 | 
Tham khảo logic xử lý tại < >. 

Soft OTP Server trả kết quả xác thực cho MB Server

 | 
 | 
 | MB Server | Gửi yêu cầu đăng ký OTT BĐSD tới hệ thống quản lý OTT của Bank
 | 
 | 
 | Gateway Bank (OTT) | Xử lý đăng ký OTT BĐSD cho KH và trả KQ cho MB Server
 | 
 | 
 | MB Server | 
Nhận kết quả và trả về cho Client

• Thành công: Cập nhật trạng thái OTT BĐSD = Đã đăng ký và trả KQ thành công cho MB Client
• Không thành công: Trả về thông báo lỗi cho Client
 | 
 | 
 | MB Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng
• Thành công:
• Hiển thị thông báo "Quý khách đã Đăng ký dịch vụ nhận tin Biến động số dư trên ứng dụng thành công"

<MH3.2>  Xác thực bằng SMS OTP
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1

 | Nhấn "Xác nhận"

 | Client | 
1/ Kiểm tra validate:

• Không hợp lệ: | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Bỏ trống OTP | Mã OTP không được để trống | 

 | 2 | OTP nhỏ hơn 6 ký tự | Mã OTP phải bao gồm 6 ký tự | 

• Hợp lệ: Gửi yêu cầu xác nhận đăng ký OTT BĐSD sang MB Server
 | MB Server | 
1/ Kiểm tra OTP:

• Không hợp lệ:  | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | OTP sai | Mã OTP không chính xác. Quý khách vui lòng kiểm tra lại. | Tắt thông báo giữ nguyên màn hình đang thao tác
 | 2 | OTP hết hiệu lực | Mã OTP đã hết hiệu lực. Quý khách vui lòng thực hiện lại. | Tắt thông báo hiển thị màn hình thao tác trước đó

• Hợp lệ: Chuyển bước 2
2/ Gửi yêu cầu đăng ký OTT BĐSD tới hệ thống quản lý OTT của Bank

 | Gateway Bank (OTT) | Xử lý đăng ký OTT BĐSD cho KH và trả KQ cho MB Server
 | MB Server | 
Nhận kết quả và trả về cho Client

• Thành công: Cập nhật trạng thái OTT BĐSD = Đã đăng ký và trả KQ thành công cho MB Client
• Không thành công: Trả về thông báo lỗi cho Client
 | MB Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng
• Thành công:
• Hiển thị thông báo "Quý khách đã Đăng ký dịch vụ nhận tin Biến động số dư trên ứng dụng thành công"

<MH4>  Màn hình thông báo kết quả
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn “Đóng” tại màn hình kết quả thành công
 | 
MB Client
 | 
Hiển thị màn hình Quản lý thông báo trên ứng dụng với trạng thái đã đăng ký

---

#### 19.3.3. Hủy đăng ký OTT BĐSD (SMS)

> **Page ID:** `37682030` · **Version:** 7
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37682030

1. Tác nhân, điều kiện trước, kết quả mong muốn

- Tác nhân tham gia: KH, MB Client, MB Server, Gateway Server (Đăng ký OTTBĐSD)

- Điều kiện trước: 

• KH thực hiện đăng nhập ứng dụng thành công
• KH đang bật tính năng OTT Biến động số dư (SMS)
- Kết quả mong muốn:

• Hệ thống Bank (Gateway Server) hủy đăng ký tính năng OTT Biến động số dư (SMS) thành công cho user (theo CIF)
2. Luồng màn hình

<MH 1> Cài đặt

<MH 2> Quản lý thông báo

<MH3> Xác nhận hủy

<MH4> Xác thực bằng SMS OTP

<MH5.1> Nhập mã PIN Soft OTP

<MH5.2> Xác thực giao dịch

<MH6> Kết quả hủy

3. Mô tả màn hình

<MH1> Quản lý thông báo tại chức năng Cài đặt

<MH2> Quản lý thông báo
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

 | 1 | Tiêu đề | Lable | Read Only | -- | -- | Quản lý thông báo
 | 2 | Nhận thông báo BĐSD qua ứng dụng (miễn phí) | Yes/No Button | Switch | -- | -- | Tham khảo mô tả và logic xử lý ở phần <<Hủy đăng ký OTT BĐSD>>
 | 3 | Lưu ý | Label | Read Only | -- | -- | 
Khi đăng ký dịch vụ, Quý khách có thể nhận thông báo biến động số dư qua ứng dụng

 | 4 | Nhận thông báo BĐSD qua tin nhắn SMS (có phí) | Yes/No Button | Switch | -- | -- | 

 | 5 | Lưu ý | Label | Read Only | -- | -- | 
Khi đăng ký dịch vụ, Quý khách có thể nhận thông báo biến động số dư qua tin nhắn tới số điện thoại đã đăng ký

 | 6 | Nút "Quay lại" | Icon | Click | -- | -- | 
Quay về màn hình trước đó

<MH3> Xác nhận hủy
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

 | 1 | Title | Icon | Readonly | -- | -- | Thông báo
 | 2 | 
Nội dung
 | Lable | Readonly | -- | -- | 
Quý khách có muốn hủy cài đặt nhận thông báo biến động số dư qua tin nhắn SMS?

 | 3 | Nút Không | Button | 
Click
 | -- | -- | Tắt popup
 | 4 | Nút Đồng ý | Button | 
Click
 | -- | -- | Xác nhận hủy dịch vụ

<MH4> Xác thực bằng SMS OTP

Hiển thị màn hình xác thực bằng SMS OTP với trường hợp:

• KH chưa cài đặt kích hoạt Soft OTP
• KH đã cài đặt kích hoạt Soft OTP nhưng chưa thực hiện đủ (n ) giao dịch bằng SMS OTP
<MH5.1> Nhập mã PIN Soft OTP 

<MH5.2> Xác thực bằng Soft OTP 

Hiển thị màn hình xác thực bằng Soft OTP với trường hợp:

• KH đã đăng ký Soft OTP và đã thực hiện đủ (n ) giao dịch bằng SMS OTP
<MH6> Kết quả hủy
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

 | 1 | Icon | Icon | Readonly | -- | -- | Thành công
 | 2 | 
Nội dung
 | Lable | Readonly | -- | -- | 
Quý khách đã hủy dịch vụ nhận thông báo biến động số dư qua tin nhắn SMS thành công.

 | 3 | Nút Đóng | Button | 
Click
 | -- | -- | Tắt popup

4. Luồng xử lý 

<MH1> Cài đặt
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn chọn chức năng Cài đặt > Quản lý thông báo trên trang chủ
 | 
MB Client
 | 
Hiển thị màn hình Quản lý thông báo

Trạng thái đăng ký OTT BĐSD (SMS) (Đã đăng ký/ Chưa đăng ký) do MB Server trả về

<MH2> Quản lý thông báo
 | TT | Thao tác | Tác nhân | Mô tả
 | 1

 | 
Nhấn Hủy đăng ký
 | 
KH

Client
 | 
Khách hàng tắt chức năng nhận thông báo BĐSD qua SMS

Client gửi yêu cầu hủy đăng ký nhận tin BĐSD qua SMS cho MB Server

 | MB Server | 
1/ Kiểm tra trạng thái Soft OTP của user

• Nếu KH đã kích hoạt Soft OTP → Chuyển bước 2
• Nếu KH chưa kích hoạt Soft OTP → Server xác định PTXT là SMS OTP
2/ Kiểm tra số lần giao dịch xác thực bằng SMS OTP thành công trước đó

• 
Nếu số lần xác thực SMS OTP < (n ) → Server xác định PTXT là SMS OTP  → Chuyển bước 3

• Nếu số lần xác thực SMS OTP >= (n ) → Server xác định PTXT ưu tiên nhất do Server trả về là Soft OTP → Chuyển bước xác thực bằng Soft OTP
• Nếu trạng thái Soft OTP = Lock/ AutoLock → Server xác định PTXT là SMS OTP → Chuyển bước 3
(Tham khảo Logic xác định PTXT của GD phi tài chính tại )

3/ MB Server thực hiện sinh OTP và gửi yêu cầu cho hệ thống Bank gửi SMS OTP cho KH

4/ Hệ thống Bank trả kết quả phản hồi gửi SMS OTP cho MB server

5/ MB Server nhận phản hồi:

• Không nhận được phản hồi từ hệ thống Bank server: Trả về mã lỗi và nội dung thông báo lỗi timeout.
• Không thành công: Trả về mã lỗi và nội dung thông báo lỗi tương ứng để Client hiển thị popup thông báo lỗi.
• Thành công: Trả về kết quả để client hiển thị màn hình xác 
{n} là số lần xác thực SMS OTP trước khi xác thực bằng Soft OTP

 | 
 Client
 | 
Nhận kết quả thông qua MB Server:

•    Thành công: Hiển thị màn hình xác nhận OTP để đăng ký dịch vụ
•    Không thành công: Hiển thị thông báo lỗi theo quy tắc chung

<MH3>  Xác thực bằng SMS OTP
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1

 | Nhấn "Xác nhận"

 | Client | 
1/ Kiểm tra validate:

• Không hợp lệ: | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Bỏ trống OTP | Mã OTP không được để trống | 

 | 2 | OTP nhỏ hơn 6 ký tự | Mã OTP phải bao gồm 6 ký tự | 

• Hợp lệ: Gửi yêu cầu xác nhận hủy đăng ký OTT BĐSD (SMS) sang MB Server
 | MB Server | 
1/ Kiểm tra OTP:

• Không hợp lệ:  | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | OTP sai | Mã OTP không chính xác. Quý khách vui lòng kiểm tra lại. | Tắt thông báo giữ nguyên màn hình đang thao tác
 | 2 | OTP hết hiệu lực | Mã OTP đã hết hiệu lực. Quý khách vui lòng thực hiện lại. | Tắt thông báo hiển thị màn hình thao tác trước đó

• Hợp lệ: Chuyển bước 2
2/ Gửi yêu cầu hủy đăng ký OTT BĐSD (SMS) tới hệ thống quản lý OTT của Bank

 | Gateway Bank (OTT) | Xử lý hủy đăng ký OTT BĐSD (SMS) cho KH và trả KQ cho MB Server
 | MB Server | 
Nhận kết quả và trả về cho Client

• Thành công: Cập nhật trạng thái OTT BĐSD (SMS) = Hủy đăng ký (OFF) và trả KQ hủy thành công cho MB Client
• Không thành công: Trả về thông báo lỗi cho Client
 | MB Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng
• Thành công:
• Hiển thị thông báo "Quý khách đã hủy dịch vụ nhận thông báo biến động số dư qua tin nhắn SMS thành công."

<MH4.1> Nhập mã PIN Soft OTP

<MH4.2> Xác thực bằng Soft OTP
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn "Xác nhận"
 | 
 | 
Tham khảo logic xử lý tại < Xác thực bằng Soft OTP>. 

Soft OTP Server trả kết quả xác thực cho MB Server

 | 
 | 
 | MB Server | Gửi yêu cầu hủy đăng ký OTT BĐSD (SMS) tới hệ thống quản lý OTT của Bank
 | 
 | 
 | Gateway Bank (OTT) | Xử lý hủy đăng ký OTT BĐSD (SMS) cho KH và trả KQ cho MB Server
 | 
 | 
 | MB Server | 
Nhận kết quả và trả về cho Client

• Thành công: Cập nhật trạng thái OTT BĐSD (SMS) = Hủy đăng ký (OFF) và trả KQ hủy thành công cho MB Client
• Không thành công: Trả về thông báo lỗi cho Client
 | 
 | 
 | MB Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng
• Thành công:
• Hiển thị thông báo "Quý khách đã Hủy dịch vụ nhận tin Biến động số dư qua tin nhắn SMS thành công"

<MH5>  Màn hình thông báo kết quả
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn “Đóng” tại màn hình kết quả thành công
 | 
MB Client
 | 
Hiển thị màn hình Quản lý thông báo trên ứng dụng với trạng thái hủy đăng ký thành công

---

#### 19.3.4. Đăng ký nhận BĐSD qua tin nhắn SMS

> **Page ID:** `37682179` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37682179

1. Tác nhân, điều kiện trước, kết quả mong muốn

- Tác nhân tham gia: KH, MB Client, MB Server, Gateway Server 

- Điều kiện trước: 

• KH thực hiện đăng nhập ứng dụng thành công
• KH đang tắt tính năng nhận tin Biến động số dư qua SMS
• KH được phép ON tính năng SMS BĐSD trên App nếu KH thực hiện OFF tính năng SMS BĐSD trên App trước đó
• Chức năng đăng ký nhận BĐSD không dành cho KH đã chủ động khóa SMS BĐSD tại quầy Bank
- Kết quả mong muốn:

• Hệ thống Bank (Gateway Server) đăng ký tính năng nhận tin Biến động số dư qua SMS thành công cho user (theo CIF)
2. Luồng màn hình

MH1: Cài đặt

MH2: Quản lý thông báo

MH3: Xác thực bằng SMS OTP

MH4.1: Nhập mã pin Soft OTP

MH4.2: Xác thực giao dịch bằng Soft OTP

MH5: Kết quả đăng ký

<MH1> Cài đặt

<MH2> Quản lý thông báo
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

 | 1 | Tiêu đề | Lable | Read Only | -- | -- | Quản lý thông báo
 | 2 | Nhận thông báo BĐSD qua ứng dụng (miễn phí) | Yes/No Button | Switch | -- | -- | Tham khảo mô tả và logic xử lý ở phần <<Đăng ký OTT BĐSD>>
 | 3 | Lưu ý | Label | Read Only | -- | -- | 
Khi đăng ký dịch vụ, Quý khách có thể nhận thông báo biến động số dư qua ứng dụng

 | 4 | Nhận thông báo BĐSD qua tin nhắn SMS (có phí) | Yes/No Button | Switch | -- | -- | Mặc định không chọn
 | 5 | Lưu ý | Label | Read Only | -- | -- | 
Khi đăng ký dịch vụ, Quý khách có thể nhận thông báo biến động số dư qua tin nhắn tới số điện thoại đã đăng ký

 | 6 | Nút "Quay lại" | Icon | Click | -- | -- | 
Quay về màn hình trước đó

<MH3> Xác thực bằng SMS OTP

Hiển thị màn hình xác thực bằng SMS OTP với trường hợp:

• KH chưa cài đặt kích hoạt Soft OTP
• KH đã cài đặt kích hoạt Soft OTP nhưng chưa thực hiện đủ (n ) giao dịch bằng SMS OTP
<MH4.1> Nhập mã PIN Soft OTP

<MH4.2> Xác thực bằng Soft OTP 

Hiển thị màn hình xác thực bằng Soft OTP với trường hợp:

• KH đã đăng ký Soft OTP và đã thực hiện đủ (n ) giao dịch bằng SMS OTP
<MH5> Kết quả đăng ký
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

 | 1 | Icon | Icon | Readonly | -- | -- | Thành công
 | 2 | 
Nội dung
 | Lable | Readonly | -- | -- | 
Quý khách đã Đăng ký dịch vụ nhận tin Biến động số dư qua tin nhắn SMS thành công

 | 3 | Nút Đóng | Button | 
Click
 | -- | -- | Tắt popup

#### 3. Luồng xử lý chi tiết

<MH1> Cài đặt
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn chọn chức năng Cài đặt > Quản lý thông báo trên trang chủ
 | 
MB Client
 | 
Gửi yêu cầu lấy trạng thái nhận tin BĐSD qua SMSt ới MB server

 | 
 | 
 | MB Server | Gửi yêu cầu lấy trạng thái nhận tin BĐSD qua SMS tới HT Bank
 | 
 | 
 | Bank | Truy vấn và trả kết quả cho MB Server
 | 
 | 
 | MB Server | Trả kết quả trạng thái đăng ký nhận tin BĐSD qua SMS (Đã đăng ký/ Chưa đăng ký)
 | 
 | 
 | MB Client | Hiển thị trạng thái ON/OFF tương ứng

<MH2> Quản lý thông báo
 | TT | Thao tác | Tác nhân | Mô tả
 | 1 | Trạng thái SMS BĐSD | MB Client | Trạng thái SMS BĐSD đang là OFF
 | 1

 | 
Nhấn đăng ký dịch vụ
 | 
KH

Client
 | 
Khách hàng bật chức năng thông báo bđsd qua sms = ON

Client gửi yêu cầu đăng ký SMS BĐSD tới MB Server

 | MB Server | 
 1/ Kiểm tra trạng thái Soft OTP của user

• Nếu KH đã kích hoạt Soft OTP → Chuyển bước 2
• Nếu KH chưa kích hoạt Soft OTP → Server xác định PTXT là SMS OTP
2/ Kiểm tra số lần giao dịch xác thực bằng SMS OTP thành công trước đó

• 
Nếu số lần xác thực SMS OTP < (n ) → Server xác định PTXT là SMS OTP  → Chuyển bước 3

• Nếu số lần xác thực SMS OTP >= (n ) → Server xác định PTXT ưu tiên nhất do Server trả về là Soft OTP → Chuyển bước xác thực bằng Soft OTP
• Nếu trạng thái Soft OTP = Lock/ AutoLock → Server xác định PTXT là SMS OTP → Chuyển bước 3
(Tham khảo logic chung <>)

3/ MB Server thực hiện sinh OTP và gửi yêu cầu cho hệ thống Bank gửi SMS OTP cho KH

4/ Hệ thống Bank trả kết quả phản hồi gửi SMS OTP cho MB server

5/ MB Server nhận phản hồi:

• Không nhận được phản hồi từ hệ thống Bank server: Trả về mã lỗi và nội dung thông báo lỗi timeout.
• Không thành công: Trả về mã lỗi và nội dung thông báo lỗi tương ứng để Client hiển thị popup thông báo lỗi.
• Thành công: Trả về kết quả để client hiển thị màn hình xác 
{n} là số lần xác thực SMS OTP trước khi xác thực bằng Soft OTP

 | 
 Client
 | 
Nhận kết quả thông qua MB Server:

•    Thành công: Hiển thị màn hình xác nhận OTP để đăng ký dịch vụ
•    Không thành công: Hiển thị thông báo lỗi theo quy tắc chung

<MH3> Xác thực bằng SMS OTP
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1

 | Nhấn "Xác nhận"

 | Client | 
1/ Kiểm tra validate:

• Không hợp lệ: | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Bỏ trống OTP | Mã OTP không được để trống | 

 | 2 | OTP nhỏ hơn 6 ký tự | Mã OTP phải bao gồm 6 ký tự | 

• Hợp lệ: Gửi yêu cầu xác nhận đăng ký nhận tin BĐSD qua SMS sang MB Server
 | MB Server | 
1/ Kiểm tra OTP:

• Không hợp lệ:  | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | OTP sai | Mã OTP không chính xác. Quý khách vui lòng kiểm tra lại. | Tắt thông báo giữ nguyên màn hình đang thao tác
 | 2 | OTP hết hiệu lực | Mã OTP đã hết hiệu lực. Quý khách vui lòng thực hiện lại. | Tắt thông báo hiển thị màn hình thao tác trước đó

• Hợp lệ: Chuyển bước 2
2/ Gửi yêu cầu đăng ký nhận tin BĐSD qua SMS tới hệ thống quản lý của Bank

 | HT SMS BĐSD (Bank)  | Xử lý đăng ký nhận tin BĐSD qua SMS cho KH và trả KQ cho MB Server
 | MB Server | 
Nhận kết quả và trả về cho Client

• Không hợp lệ: Trả về thông báo lỗi cho Client | 
 | Trường hợp | Thông báo | Xử lý nếu có
 | 1 | 
• KH bị nợ phí SMS BĐSD và đầu Bank chủ động Khóa SMS BĐSD của KH
• KH chủ động khóa SMS BĐSD tại Quầy
(Bank trả mã lỗi 416)
 | Yêu cầu của Quý khách không thực hiện được. Vui lòng ra quầy giao dịch Ngân hàng gần nhất để được hỗ trợ | Đóng thông báo, trạng thái SMS BĐSD vẫn = OFF

• Hợp lệ: Cập nhật trạng thái nhận tin BĐSD qua SMS = Đăng ký (ON) và trả KQ đăng ký thành công cho MB Client
 | MB Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng do server trả về
• Thành công:
• Hiển thị thông báo "Quý khách đã Đăng ký dịch vụ nhận thông báo biến động số dư qua tin nhắn SMS thành công."

<MH4.1> Nhập mã PIN Soft OTP

<MH4.2> Xác thực bằng Soft OTP
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn "Xác nhận"
 | 
 | 
Tham khảo logic xử lý tại < Xác thực bằng Soft OTP>. 

Soft OTP Server trả kết quả xác thực cho MB Server

 | 
 | 
 | MB Server | Gửi yêu cầu đăng ký nhận tin BĐSD qua SMS tới hệ thống quản lý của Bank
 | 
 | 
 | Gateway Bank  | 
Xử lý đăng ký nhận tin BĐSD qua SMS cho KH và trả KQ cho MB Server

 | 
 | 
 | MB Server | 
Nhận kết quả và trả về cho Client

• Không thành công: Trả về thông báo lỗi cho Client | 
 | Trường hợp | Thông báo | Xử lý nếu có
 | 1 | 
• KH bị nợ phí SMS BĐSD và đầu Bank chủ động Khóa SMS BĐSD của KH
• KH chủ động khóa SMS BĐSD tại Quầy
(Bank trả mã lỗi 416)
 | Yêu cầu của Quý khách không thực hiện được. Vui lòng ra quầy giao dịch Ngân hàng gần nhất để được hỗ trợ | Đóng thông báo, trạng thái SMS BĐSD vẫn = OFF

• Thành công: Cập nhật trạng thái nhận tin BĐSD qua SMS = Đăng ký (ON) và trả KQ đăng ký thành công cho MB Client
 | 
 | 
 | MB Client | 
Nhận kết quả:

• Không thành công:
• Hiển thị thông báo lỗi tương ứng do server trả về
• Thành công:
• Hiển thị thông báo "Quý khách đã Đăng ký dịch vụ nhận thông báo biến động số dư qua tin nhắn SMS thành công."

<MH5>  Màn hình thông báo kết quả
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn “Đóng” tại màn hình kết quả thành công
 | 
MB Client
 | 
Hiển thị màn hình Quản lý thông báo trên ứng dụng với trạng thái đã đăng ký thành công

---

### 19.4. Đổi mật khẩu

> **Page ID:** `29891629` · **Version:** 14
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29891629

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
03/2021 
 | A | HongLT | 
 | 
Tạo mới
 | V.1
 | 
 
 | M | HongLT | 
 | 
Bổ sung tham số quy định thêm rule mật khẩu
 | 

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, App Client, App server
• Điều kiện trước: 

• KH cài đặt ứng dụng thành công
• KH đã đăng nhập thành công vào ứng dụng
• Kết quả mong muốn:
• KH thực hiện đổi mật khẩu thành công
#### 2/ Luồng màn hình

MH Cài đặt

##### MH1: MH đổi mật khẩu

2/ Mô tả màn hình

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
ĐỔI MẬT KHẨU

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn Back, hiển thị màn hình thao tác trước đó
 | 3 | Mật khẩu cũ | 
Textbox
 | 
Text
 | Yes | 8 - 20 | 
• Cho phép nhập tất cả các ký tự không bao gồm dấu cách;
• Mã hóa ký tự nhập vào bằng ký tự * 
• Cho phép ẩn/hiện ký tự nhập bằng cách nhấn icon "eye".
• Mặc định: Ẩn.
 | 4 | Mật khẩu mới | 
Textbox
 | 
Text
 | Yes | 8 - 20 | 
• Mật khẩu mới hợp lệ: Từ 8 – 20 ký tự, chứa ít nhất 1 ký tự số, 1 ký tự chữ (check tại client) + các điều kiện khác tại server quy định.
• Không cho nhập ký tự có dấu, dấu cách.
• Mã hóa ký tự nhập vào bằng ký tự *
• Hiển thị icon “Ẩn/Hiện" ký tự mật khẩu nhập. Mặc định: Ẩn
• 
Quy định check mật khẩu:

• Client: Từ 8 – 20 ký tự,
• Client: Các ký tự đặc biệt cho phép nhập là: # & @ ! ? % * $ [ ] { } _ \ | ~ < > . , ( ) " ' ^ + = - / : ; 
• Server: Các điều kiện khác
 | 5 | Nhập lại mật khẩu mới | 
Textbox
 | 
Text
 | Yes | 8 - 20 | 
• Trùng với mật khẩu mới;
• Không cho nhập ký tự có dấu, dấu cách;
• Mã hóa ký tự nhập vào bằng ký tự *;
• Hiển thị icon “Ẩn/Hiện" ký tự mật khẩu nhập. Mặc định: Ẩn.
 | 6 | Ghi chú hướng dẫn đặt mật khẩu | Label | Read Only | -- | -- | 
Hiển thị ghi chú hướng dẫn đặt mật khẩu theo cấu hình Quản lý thông báo tại BE do MB server trả về tại mid Login (Mã thông báo: PASS_NOTE)

<Tham khảo logic xử lý>

 | 7 | Xác nhận | Button | Click | -- | -- | Tham khảo logic xử lý

#### 4/ Luồng xử lý

 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhấn Đổi mật khẩu tại MH Cài đặt | 
MB Client
 | 
Hiển thị màn hình Đổi mật khẩu

 | 2 | Nhập các thông tin và Nhấn Xác nhận | 
MB Client
 | 
1/ Kiểm tra validate:

• Không hợp lệ: Hiển thị popup thông báo lỗi: | 
 | Trường hợp lỗi | Thông báo | Xử lý (nếu có)
 | 1 | Bỏ trống mật khẩu cũ | Mật khẩu cũ không được để trống | 

 | 2 | Bỏ trống mật khẩu mới | Mật khẩu mới không được để trống | 

 | 3 | Bỏ trống Nhập lại mật khẩu mới | Nhập lại mật khẩu mới không được để trống | 

 | 4 | Mật khẩu mới nhỏ hơn 8 ký tự | 
Mật khẩu mới chưa đúng quy định
 | 

 | 5 | Mật khẩu cũ nhỏ hơn 8 ký tự | Mật khẩu cũ chưa đúng quy định | 

 | 6 | Mật khẩu mới không trùng với Nhập lại mật khẩu mới | Mật khẩu mới không trùng nhau | 

 | 7 | Mật khẩu mới trùng với mật khẩu cũ | Mật khẩu mới không được trùng với mật khẩu cũ. Quý khách vui lòng kiểm tra lại | 

• Hợp lệ: Gửi yêu cầu đổi mật khẩu sang MB Server
 | MB server | 
1/ Kiểm tra thông tin mật khẩu:

• Mật khẩu mới đúng định dạng là:
- Gồm một chuỗi từ 8 đến 20 ký tự, chứa ít nhất 01 ký tự số, 01 ký tự chữ thường, 01 ký tự chữ viết hoa (Rule cố định)

- Và ký tự đặc biệt (Rule theo cấu hình tại tham số  PASS_HAVE_SPECIAL_CHAR = 1 (Bắt buộc mật khẩu chứa ít nhất 1 ký tự đặc biệt),  PASS_HAVE_SPECIAL_CHAR = 0 (Không bắt buộc mật khẩu chứa ký tự đặc biệt)

• Không hợp lệ: Hiển thị popup thông báo lỗi | 
 | Trường hợp lỗi | Thông báo | Xử lý (nếu có)
 | 1 | Mật khẩu cũ không đúng | Mật khẩu cũ chưa đúng. Quý khách vui lòng kiểm tra lại. | 

 | 2 | Mật khẩu cũ sai quá (n) lần cho phép trong phiên giao dịch (luồng xác thực) | 
Quý khách nhập mật khẩu sai quá [n] lần cho phép. Quý khách vui lòng đăng nhập lại để thực hiện chức năng này.
 | Đóng Popup  điều hướng về MH login. KH login lại đúng thì quay lại MH Home
 | 3 | 
Nếu tham số PASS_HAVE_SPECIAL_CHAR = 1

Mật khẩu mới thiếu 1 trong 5 yếu tố:

• Không chứa từ 8 đến 20 ký tự
• Không có ít nhất 1 ký tự số (1,2,3,...)
• Không có ít nhất 1 chữ hoa (A,B,C...)
• Không có ít nhất 1 chữ thường (a,b,c...)
• Không có ít nhất 1 ký tự đặc biệt (@, #, $, %, &...) | Mật khẩu mới phải là một chuỗi từ 8 đến 20 ký tự, chứa ít nhất 01 ký tự số, 01 ký tự chữ thường, 01 ký tự chữ viết hoa và 01 ký tự đặc biệt. | 

 | 4 | 
Nếu tham số PASS_HAVE_SPECIAL_CHAR = 0

Mật khẩu mới thiếu 1 trong 4 yếu tố:

• Không chứa từ 8 đến 20 ký tự
• Không có ít nhất 1 ký tự số (1,2,3,...)
• Không có ít nhất 1 chữ hoa (A,B,C...)
• Không có ít nhất 1 chữ thường (a,b,c...) | Mật khẩu mới phải là một chuỗi từ 8 đến 20 ký tự, chứa ít nhất 01 ký tự số, 01 ký tự chữ thường, 01 ký tự chữ viết hoa | 

• Hợp lệ: Thực hiện xử lý:
• Cập nhật mật khẩu mới cho user
• Trả kết quả cho client hiển thị
 | 
MB Client
 | 
Hiển thị màn hình Thông báo đổi mật khẩu thành công: "Đổi mật khẩu thành công. Quý khách vui lòng đăng nhập lại ứng dụng.". Yêu cầu Đăng nhập lại trên MH đăng nhập lần sau

---

### 19.5. Bật đăng nhập/ xác thực Vân tay/ Face ID

> **Page ID:** `29891073` · **Version:** 22
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29891073

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 

 | A | ThaoBT | 
 | 
Tạo mới tài liệu
 | 

 | 
 
 | M | HongLT | 
 | 
Bổ sung nội dung thông báo cần thực hiện n SMS OTP trước khi xác thực giao dịch bằng FaceID/TouchID
 | 

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client, MB Server
• Điều kiện trước: 
• KH đã đăng nhập ứng dụng trên thiết bị di động thành công;
• Thiết bị của KH đủ điều kiện được phép phép kích hoạt Vân tay/Face ID
• Vân tay:
• Face ID:
• KH đã cài Vân tay/Face ID trên thiết bị ở chế độ Bật.
• Kết quả mong muốn:
• KH thực hiện cài đặt Bật đăng nhập/xác thực Vân tay/Face ID thành công.
#### 2/ Luồng màn hình

##### 2.1 Đăng nhập/ xác thực bằng Vân tay

MH1: Cài đặt vân tay

MH2: Quét vân tay

MH3: Xác nhận cài đặt bằng mật khẩu đăng nhập

MH4: Kết quả bật đăng nhập Vân tay

MH5: Kết quả bật xác thực giao dịch bằng Vân tay

##### 2.2 Đăng nhập/ xác thực bằng Face ID

MH1: Cài đặt Face ID

MH2: Quét Face ID

MH3: Xác nhận cài đặt bằng mật khẩu đăng nhập

MH4: Kết quả bật đăng nhập Face ID

MH5: Kết quả bật xác thực giao dịch bằng Face ID

#### 3/ Mô tả:

##### a. Cài đặt Vân tay/Face ID
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | Cài đặt Vân tay
 | 1 | Tiêu đề | Label | Read Only | -- | -- | 
CÀI ĐẶT VÂN TAY

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn Back, hiển thị màn hình thao tác trước đó
 | 3 | Đăng nhập bằng vân tay | Toggle | ON/OFF | -- | -- | 
Mặc định: OFF

Cho phép ON/OFF

Label ghi chú:

• Cài đặt để sử dụng vân tay khi đăng nhập.
 | 4 | Xác thực giao dịch bằng vân tay | Toggle | ON/OFF | -- | 
 | 
Mặc định: OFF

Cho phép ON/OFF

Label ghi chú:

• Cài đặt để sử dụng vân tay khi xác thực giao dịch.
 | Cài đặt Face ID
 | 1 | Tiêu đề | Label | Read Only | -- | -- | 
CÀI ĐẶT FACE ID

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn Back, hiển thị màn hình thao tác trước đó
 | 3 | Đăng nhập bằng Face ID | Toggle | ON/OFF | -- | -- | 
Mặc định: OFF

Cho phép ON/OFF

Label ghi chú:

• Cài đặt để sử dụng Face ID khi đăng nhập.
 | 4 | Xác thực giao dịch bằng Face ID | Toggle | ON/OFF | -- | -- | 
Mặc định: OFF

Cho phép ON/OFF

Label ghi chú:

• Cài đặt để sử dụng Face ID khi xác thực giao dịch. 

b. Quét Vân tay/Face ID
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | Quét Vân tay
 | 1 | Tiêu đề | Label | Read Only | -- | -- | Vân tay cho "Cài đặt vân tay cho Mobile Banking"
 | 2 | Nội dung thông báo | Icon | Click | -- | -- | 
Fix tại client:

• Quý khách vui lòng quét vân tay để tiếp tục.
 | 3 | Nút "Hủy" | Button | Click | -- | -- | Nhấn Hủy, tắt thông báo và hiển thị màn hình đang thao tác trước đó
 | Quét Face ID
 | 1 | Tiêu đề | Label | Read Only | -- | -- | Cài đặt Face ID cho Mobile Banking
 | 2 | Nội dung thông báo | Icon | Click | -- | -- | 
Hiển thị popup cấp quyền của hệ điều hành iOS: 

"Bạn có muốn cho phép "Mobile Banking" sử dụng Face ID không?" 

và 2 button "Từ chối", "OK"

Nhấn từ chối: Quay lại màn hình cài đặt

Nhấn OK: Hiển thị thông báo: "Quý khách vui lòng nhận diện khuôn mặt để tiếp tục." và button "Hủy"

 | 3 | Nút "Hủy" | Button | Click | -- | -- | Nhấn Hủy, tắt thông báo và hiển thị màn hình đang thao tác trước đó
 | 
 | 
 | 
 | 
 | 
 | 
 | 

##### c. Xác nhận cài đặt bằng mật khẩu đăng nhập (Pop-up)
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

 | 1 | Tiêu đề | Label | Read Only | -- | -- | XÁC NHẬN
 | 2 | Nội dung thông báo | Icon | Click | -- | -- | 
Fix tại Client: Quý khách vui lòng nhập mật khẩu đăng nhập để xác nhận cài đặt

 | 3 | Nút "Hủy" | Button | Click | -- | -- | 
Nhấn "Hủy" thông báo và hiển thị màn hình đang thao tác trước đó

 | 4 | Nút "Tiếp tục" | Button | Click | -- | -- | 
Nhấn "Tiếp tục" để tiến hành xác minh mật khẩu nhập

##### d. Kết quả
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | Vân tay
 | 1 | Nội dung thông báo | Label | Read Only | -- | -- | 
Hiển thị đối với bật đăng nhập:

• Tiêu đề: Thành công
• Nội dung: Quý khách đã cài đặt đăng nhập bằng vân tay thành công. 
• Nút "Đóng": Nhấn nút này, hiển thị màn hình cài đặt vân tay
---

Hiển thị đối với bật xác thực:

• Tiêu đề: Thành công
• Nội dung (do MB server trả): Quý khách đã cài đặt xác thực giao dịch bằng $2 thành công. Để đảm bảo an toàn, ứng dụng chỉ cho phép sử dụng phương thức xác thực $2 khi Quý khách đã thực hiện thành công $1 giao dịch tài chính bằng SMS OTP sau khi cài đặt.
  (n cấu hình theo tham số OTP_FOR_BIOMETRIC)

• Nút "Đóng": Nhấn nút này, hiển thị màn hình cài đặt vân tay
 | Face ID
 | 1 | Nội dung thông báo | Label | Read Only | -- | -- | 
Hiển thị đối với bật đăng nhập:

• Tiêu đề: Thành công
• Nội dung: Quý khách đã cài đặt đăng nhập bằng Face ID thành công. 
• Nút "Đóng": Nhấn nút này, hiển thị màn hình cài đặt Face ID
---

Hiển thị đối với bật xác thực:

• Tiêu đề: Thành công
• Nội dung (do MB server trả: Quý khách đã cài đặt xác thực giao dịch bằng $2 thành công. Để đảm bảo an toàn, ứng dụng chỉ cho phép sử dụng phương thức xác thực $2 khi Quý khách đã thực hiện thành công $1 giao dịch tài chính bằng SMS OTP sau khi cài đặt.
(n cấu hình theo tham số OTP_FOR_BIOMETRIC)

• Nút "Đóng": Nhấn nút này, hiển thị màn hình cài đặt Face ID

#### 4/ Luồng xử lý

##### a. Cài đặt Vân tay/Face ID
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Tại màn hình Cài đặt vân tay/ Face ID, gạt sang chế độ ON tại:

• Đăng nhập bằng vân tay
• Xác thực bằng vân tay
• Đăng nhập bằng Face ID
• Xác thực bằng Face ID | Client | 
1/ Kiểm tra thiết bị có hỗ trợ Vân tay/ FaceID:

• Không hỗ trợ: | | 
ID
 | 
Case
 | 
Thông báo

 | 01 | 
Thiết bị không hỗ trợ Vân tay
 | 
Thiết bị không hỗ trợ xác thực vân tay. Quý khách vui lòng kiểm tra lại.

 | 02 | Thiết bị không hỗ trợ Face ID | Thiết bị không hỗ trợ xác thực khuôn mặt. Quý khách vui lòng kiểm tra lại.

• Có hỗ trợ: Chuyển bước tiếp theo
2/ Kiểm tra trạng thái cài đặt Vân tay/FaceID trên thiết bị:

• Không hợp lệ: | | 
ID
 | 
Case
 | 
Thông báo

 | 03 | 
KH chưa cài Vân tay/FaceID trên thiết bị
 | 
Vân tay:

Thiết bị chưa cài đặt vân tay. Quý khách vui lòng cài đặt vân tay trên thiết bị trước.

FaceID:

Thiết bị chưa cài đặt nhận diện khuôn mặt. Quý khách vui lòng cài đặt nhận diện khuôn mặt trên thiết bị trước.

• Hợp lệ: Hiển thị thông báo quét Vân tay/FaceID như mô tả

##### b. Quét Vân tay/Face ID
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1

 | KH thực hiện quét Vân tay/Face ID

 | Client | 
1/ Kiểm tra Vân tay/Face ID đã quét so với Vân tay/ Face ID đã cài đặt:

• Không hợp lệ: | | 
ID
 | 
Case
 | 
Thông báo/ Hiển thị

 | 03 | 
Vân tay/Face ID không hợp lệ
 | 
Vân tay:

Dấu vân tay không hợp lệ. Quý khách vui lòng thử lại.

FaceID:

Nhận diện khuôn mặt không hợp lệ. Quý khách vui lòng thử lại.

 | 04 | 
Quét sai số lần cho phép theo từng hệ điều hành (iOS: 5 lần; Android: 5 lần)
 | 
iOS:

Hiển thị màn hình nhập mật mã của thiết bị 

Android:

Hiển thị thông báo: "Quý khách đã nhập sai vân tay quá số lần cho phép của thiết bị" khi quét vân tay

Hiển thị thông báo: "Quý khách đã nhập sai Face ID quá số lần cho phép của thiết bị" khi quét Face ID

Trong [n] giây hiển thị thông báo như trên nếu tiếp tục click Toggle cài đặt lại Vân tay/ Face ID

• Hợp lệ: Hiển thị MH Xác nhận cài đặt bằng mật khẩu

c. Xác nhận cài đặt bằng mật khẩu đăng nhập 
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1

 | Nhấn "Tiếp tục"

 | Client | 
1/ Kiểm tra validate:

• Không hợp lệ: | | 
ID
 | 
Case
 | 
Thông báo

 | 01 | Bỏ trống mật khẩu | Mật khẩu không được bỏ trống. Quý khách vui lòng kiểm tra lại.
 | 02 | Mật khẩu nhỏ hơn 8 ký tự | Mật khẩu là chuỗi tối thiểu 8 ký tự.

• Hợp lệ: Gửi yêu cầu xác nhận kích hoạt Vân tay/Face ID sang MB Server (mid 16)
Đồng thời client truyền loại sinh trắc thiết bị cho MB server để MB server detect câu thông báo theo loại sinh trắc tương ứng để trả về cho client

biometrictType : "String"  1 vân tay , 2 faceid 

 | MB Server | 
1/  Tiến hành xác thực mật khẩu đăng nhập được nhập vào.

Không hợp lệ: Cấu hình hiển thị popup thông báo:
 | TT | Trường hợp lỗi | Nội dung | Xử lý (nếu có)
 | 1 | Mật khẩu sai | Mật khẩu không đúng. Quý khách vui lòng thử lại | 

 | 2 | Mật khẩu sai quá (n) lần cho phép trong phiên giao dịch (luồng xác thực) | 
Quý khách nhập mật khẩu sai quá [n] lần cho phép. Quý khách vui lòng nhập đăng nhập lại để thực hiện chức năng này.
 | Đóng Popup  điều hướng về MH login. KH login lại đúng thì quay lại MH Home

Hợp lệ: Trả thông báo cài đặt thành công <Nội dung xem trên mockup>, với nút Toggle ở trạng thái ON

 | Client | 
1/ Nhận kết quả từ server:

Không thành công: Hiển thị thông báo tương ứng

Thành công: Hiển thị thông báo thành công và nút Toggle ở trạng thái ON

---

### 19.6. Hủy đăng nhập/ xác thực Vân tay/ Face ID

> **Page ID:** `29891451` · **Version:** 14
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29891451

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client, MB Server
• Điều kiện trước: 
• KH đã đăng nhập ứng dụng trên thiết bị di động thành công;
• KH đã cài bật Vân tay/Face ID đăng nhập/xác thực trên ứng dụng.
• Kết quả mong muốn:
• KH thực hiện hủy đăng nhập/xác thực Vân tay/Face ID thành công.
#### 2/ Luồng màn hình

##### 2.1/ Tắt đăng nhập/ xác thực vân tay

##### MH1: Cài đặt vân tay

##### MH2A: Xác nhận hủy đăng nhập vân tay

##### MH2B: Xác nhận hủy xác thực vân tay

MH3A: Kết quả đăng nhập bằng vân tay

MH3B: Kết quả xác thực bằng vân tay

##### 2.2 Tắt đăng nhập/ xác thực Face ID

MH1: Cài đặt Face ID

MH2A: Xác nhận hủy đăng nhập Face ID

MH2B: Xác nhận hủy xác thực Face ID

MH3A: Kết quả đăng nhập bằng Face ID

MH3B: Kết quả xác thực bằng Face ID

#### Mô tả:

##### a. Cài đặt Vân tay/Face ID

##### b. Thông báo xác nhận hủy đăng nhập/xác thực Vân tay/Face ID
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | Vân tay
 | 1 | Thông báo | Icon | ReadOnly | -- | -- | 
Hiển thị đối với hủy đăng nhập:

• Tiêu đề: Hủy đăng nhập bằng vân tay
• Nội dung: Quý khách muốn hủy cài đặt đăng nhập bằng vân tay?
• Nút thao tác: 
• Không: Nhấn Không, tắt thông báo và hiển thị màn hình đang thao tác trước đó
• Đồng ý: <Tham khảo logic xử lý>
---

Hiển thị đối với hủy xác thực:

• Tiêu đề: Hủy xác thực bằng vân tay
• Nội dung: Quý khách muốn hủy cài đặt xác thực giao dịch bằng vân tay?
• Nút thao tác: 
• Không: Nhấn Không, tắt thông báo và hiển thị màn hình đang thao tác trước đó
• Đồng ý: <Tham khảo logic xử lý>
 | Quét Face ID
 | 1 | Thông báo | Icon | Click | -- | -- | 
Hiển thị đối với hủy đăng nhập:

• Tiêu đề: Hủy đăng nhập bằng Face ID
• Nội dung: Quý khách muốn hủy cài đặt đăng nhập bằng Face ID?
• Nút thao tác: 
• Không: Nhấn Không, tắt thông báo và hiển thị màn hình đang thao tác trước đó
• Đồng ý: <Tham khảo logic xử lý>
---

Hiển thị đối với hủy xác thực:

• Tiêu đề: Hủy xác thực bằng Face ID
• Nội dung: Quý khách muốn hủy cài đặt xác thực giao dịch bằng Face ID?
• Nút thao tác: 
• Không: Nhấn Không, tắt thông báo và hiển thị màn hình đang thao tác trước đó
• Đồng ý: <Tham khảo logic xử lý>

##### c. Kết quả
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | Vân tay
 | 1 | Nội dung thông báo | Label | Read Only | -- | -- | 
Hiển thị đối với hủy đăng nhập:

• Tiêu đề: Thành công
• Nội dung: Quý khách đã hủy cài đặt đăng nhập bằng vân tay thành công
• Nút "Đóng": Nhấn nút này, hiển thị màn hình cài đặt vân tay
---

Hiển thị đối với hủy xác thực:

• Tiêu đề: Thành công
• Nội dung: Quý khách đã hủy cài đặt xác thực giao dịch bằng vân tay thành công
• Nút "Đóng": Nhấn nút này, hiển thị màn hình cài đặt vân tay
 | Face ID
 | 1 | Nội dung thông báo | Label | Read Only | -- | -- | 
Hiển thị đối với hủy đăng nhập:

• Tiêu đề: Thành công
• Nội dung: Quý khách đã hủy cài đặt đăng nhập bằng Face ID thành công
• Nút "Đóng": Nhấn nút này, hiển thị màn hình cài đặt Face ID
---

Hiển thị đối với hủy xác thực:

• Tiêu đề: Thành công
• Nội dung: Quý khách đã hủy cài đặt xác thực giao dịch bằng Face ID thành công
• Nút "Đóng": Nhấn nút này, hiển thị màn hình cài đặt Face ID

#### 4/ Luồng xử lý

##### a. Cài đặt Vân tay/Face ID
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Tại màn hình Cài đặt Vân tay/ Face ID, gạt sang chế độ OFF tại:

• Đăng nhập bằng vân tay
• Xác thực giao dịch bằng vân tay
• Đăng nhập bằng Face ID
• Xác thực giao dịch bằng Face ID | Client | 
Hiển thị thông báo xác nhận hủy đăng nhập/ xác thực bằng Vân tay/ Face ID như mô tả

##### b. Thông báo xác nhận hủy đăng nhập/xác thực Vân tay/Face ID
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1

 | Nhấn "Đồng ý"

 | Client | 
Gửi yêu cầu hủy đăng nhập/xác thực bằng Vân tay/Face ID sang MB Server

 | MB Server | Xử lý hủy đăng nhập/xác thực bằng Vân tay/Face ID và trả kết quả cho Client
 | Client | 
Nhận kết quả: 

• Không thành công: Hiển thị thông báo lỗi tương ứng: | TT | Trường hợp lỗi | Tác nhân | Nội dung
 | 1 | Thời gian của một phiên đăng nhập là tham số này được cài đặt trên MB Server, hết phiên đang nhập | Client | Hết phiên đăng nhập. Quý khách vui lòng đăng nhập lại
 | 2 | Tại các màn hình có kiểm tra kết nối Internet, nếu xảy ra lỗi kết nối | Client | Quý khách vui lòng kiểm tra kết nối Internet/3G/Wifi
 | 3 | Các trường hợp lỗi timeout do hết thời gian chờ tại Client/Server và không nhận được kết quả cho các yêu cầu tra cứu | Client | Yêu cầu tạm thời bị gián đoạn. Quý khách vui lòng thực hiện lại sau.
 | 4 | Các trường hợp lỗi khác do hệ thống xử lý và trả về không thuộc các trường hợp đã mô tả trong tài liệu nghiệp vụ | Client | Yêu cầu không thực hiện được trong lúc này. Quý khách vui lòng thực hiện lại sau.

• Thành công: Hiển thị kết quả hủy đăng nhập/xác thực bằng Vân tay/Face ID thành công (Nút Toggle ở trạng thái OFF)

---

### 19.7. Danh bạ thụ hưởng

> **Page ID:** `29893232` · **Version:** 73
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29893232

| 
Ngày thay đổi
 | Lý do | Người thay đổi | Phiên bản cũ | 
Nội dung thay đổi
 | Phiên bản mới
 | 

 | A | Bùi Thị Thanh Thảo | 
 | 
Tạo mới
 | V1.0
 | 
 
 | M | Lê Thị Hồng | 
 | 
Cập nhật: 

• Chuyển tiền nội bộ: Bổ sung thêm logic validate số tài khoản/ thẻ cho phép nhập ký tự chữ | V2.0

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client, MB Server, Bank server, 247 system
• Điều kiện trước: 
• KH đã tải & cài đặt ứng dụng thành công
• KH có gói dịch vụ được phép truy cập chức năng này
• Kết quả mong muốn:
• KH có thể tra cứu danh sách, xem chi tiết, xóa, chỉnh sửa danh sách danh bạ thụ hưởng, Thêm mới danh bạ thành công.
#### 2/ Luồng màn hình

##### MH1A: Danh bạ thụ hưởng (Khi có Danh bạ đã lưu)

##### MH1B: Danh bạ thụ hưởng (Khi có Danh bạ đã lưu) (Khi input tìm kiếm)

##### MH1C: Danh bạ thụ hưởng (Khi Danh bạ trống)

##### MH2A: Chi tiết + cập nhật Danh bạ

##### MH2B: Chi tiết + cập nhật Danh bạ (Chuyển tiền qua GTTT)

##### MH3D: Thêm mới danh bạ thụ hưởng (Loại chuyển tiền qua GTTT) (chưa điền các trường chọn)

##### MH3D: Thêm mới danh bạ thụ hưởng (Loại chuyển tiền qua GTTT) (đã điền các trường chọn

##### MH3A: Thêm mới danh bạ thụ hưởng (Loại chuyển tiền nội bộ) (chưa điền các trường chọn)

##### MH3A: Thêm mới danh bạ thụ hưởng (Loại chuyển tiền nội bộ) (đã điền các trường chọn

##### MH3B: Thêm mới danh bạ thụ hưởng (Loại chuyển tiền nhanh 24/7 qua tài khoản) (chưa điền các trường chọn)

##### MH3B: Thêm mới danh bạ thụ hưởng (Loại chuyển tiền nhanh 24/7 qua tài khoản) (đã điền các trường chọn)

##### MH3C: Thêm mới danh bạ thụ hưởng (Loại chuyển tiền nhanh 24/7 qua thẻ) (chưa điền các trường chọn)

##### MH3C: Thêm mới danh bạ thụ hưởng (Loại chuyển tiền nhanh 24/7 qua thẻ) (đã điền các trường chọn)

##### MH4A: Chọn xóa nhiều danh bạ

##### MH4B: Thông báo xác nhận xóa danh bạ

##### MH5: Thay đổi bàn phím

Yes
#### Mô tả:

a. Màn hình danh bạ thụ hưởng
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

 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: DANH BẠ THỤ HƯỞNG

 | 2 | Icon Back | Icon | Click | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | 
Danh sách danh bạ
 | 
View
 | 
Click
 | -- | -- | 
• Nếu danh sách trống: Hiển thị thông báo
• Quý khách chưa có danh bạ thụ hưởng. Nhấn vào đây để thêm mới danh bạ thụ hưởng.  Có chức năng thêm mới danh bạ
• Nếu có, danh bạ sẽ hiển thị theo phân loại theo nhóm, và sắp xếp theo thứ tự: (Chuyển tiền nội bộ → Chuyển tiền nhanh 24/7 qua tài khoản → Chuyển tiền nhanh 24/7 qua thẻ → Chuyển tiền qua GTTT). Các danh bạ trong mỗi nhóm sẽ được sắp theo mức độ thường xuyên sử dụng của danh bạ, khi thực hiện (từ cao tới thấp)
• Các nhóm danh bạ khi chạm vào cho phép thu hẹp và mở rộng để xem các danh bạ chi tiết. Mặc định hiển thị ở dạng thu gọn khi truy cập chức năng.
• Danh bạ hiển thị gồm các thông tin:
• Logo bank 
• Tên người thụ hưởng (hiển thị tên gợi nhớ, khi có tên gợi nhớ được lưu; nếu không, hiển thị tên được lưu tại bank)
• Số tài khoản thụ hưởng/ Số thẻ thụ hưởng
• Ngân hàng thụ hưởng 
• Danh bạ chuyển tiền qua GTTT gồm các thông tin:
• Tên người thụ hưởng (hiển thị tên gợi nhớ, khi có tên gợi nhớ được lưu; nếu không, hiển thị tên người thụ hưởng)
• Số GTTT
• Loại GTTT
• Logo = in hoa ký tự đầu tiên của từ đầu tiên và từ cuối cùng trong tên hiển thị. Nếu tên chỉ có 1 từ sẽ in hoa 2 ký tự đầu tiên trong tên hiển thị
Lưu ý: Lấy danh bạ thụ hưởng dịch vụ chuyển tiền theo serviceCode tương ứng dịch vụ như sau:
 | # | Dịch vụ | ServiceCode
 | 1 | Chuyển tiền nội bộ cùng chủ | 0210
 | 2 | Chuyển tiền nộ bộ khác chủ | 0211
 | 3 | Chuyển tiền nhanh 247 qua tài khoản | 0212, 0215
 | 4 | Chuyển tiền nhanh 247 qua thẻ | 0213, 0216
 | 5 | Chuyển tiền qua GTTT | 0214

 | 4 | Xóa danh bạ | Label | Click | -- | -- | 
Nhấn button Xóa danh bạ, hiển thị ô tích chọn trên mỗi danh bạ chi tiết

Sau khi chọn Xóa danh bạ, hiển thị chức năng hủy xóa danh bạ

 | 5 | 
Ô tìm kiếm danh bạ
 | 
Textbox
 | 
Input
 | -- | 200 | 
• Cho nhập Freetext
• Tìm kiếm tương đối theo:  tên thụ hưởng (tên gợi nhớ và tên lưu tại Bank), tài khoản/ số thẻ thụ hưởng, Ngân hàng thụ hưởng, số GTTT, Loại GTTT
• Trường hợp không có danh bạ sẽ không hiển thị chức năng này
• Ô danh bạ có Icon "x": xóa nhanh toàn bộ nội dung nhập tìm kiếm, khi có nội dung nhập vào.
 | 6 | 
Thêm mới danh bạ
 | 
Button
 | 
Click
 | -- | -- | 
Click vào hiển thị màn hình thêm mới danh bạ

b/ Thêm mới danh bạ thụ hưởng
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả | 

 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: THÊM MỚI DANH BẠ THỤ HƯỞNG
 | 

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó
 | 

 | 3 | 
Icon Home
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Home, hiển thị màn hình chính của ứng dụng (quay lại màn hình Home)
 | 

 | 4 | Thông tin thêm mới  | 

 | 
4.1
 | 
Loại chuyển tiền
 | 
Combobox
 | 
List
 | Yes | -- | 
• Mặc định là Chuyển tiền nội bộ
• Cho phép chọn 1 loại từ danh sách gồm:
• Chuyển tiền nội bộ
• Chuyển tiền nhanh 24/7 qua tài khoản
• Chuyển tiền nhanh 24/7 qua thẻ
• Chuyển tiền qua GTTT | 

 | 
4.2
 | 
Tên gợi nhớ (Tùy chọn)
 | Textbox | Text | -- | 20 | 
• Mặc định trống; không bắt buộc nhập
• Nhập ký tự tiếng Việt có dấu | 

 | Trường hợp thêm Danh bạ thụ hưởng (Loại chuyển tiền nội bộ) | 

 | 

5.1 | 
Số tài khoản/ Số thẻ
 | Textbox | Text | Yes | 
2-21
 | 
Mặc định trống

Placeholder: Số tài khoản/số thẻ/số điện thoại

Cho phép nhập/chọn:

• 
Nếu nhập:

• 
Cho phép nhập tối thiểu 2 và tối đa 21 ký tự số và chữ cái, không bao gồm ký tự đặc biệt (Hiển thị bàn phím số và chữ cái IN HOA) (Cho phép nhập số tài khoản Alias)

• Nếu dán vào ô tài khoản/số thẻ/số điện thoại mà có khoảng trống ở đầu hoặc/và cuối thì hệ thống tự xóa khoảng trống ở đầu hoặc/và cuối
• Nếu điền số điện thoại mà:
• Số điện thoại là alias đã gán với 1TK: Chỉ hiển thị tên khách hàng
• Số điện thoại của khách hàng đang sử dung mobile banking nhưng không là alias: Hiển thị như cũ (tên KH + số TK mặc định)
• Khi focus vào ô tài khoản thụ hưởng, hệ thống hiển thị bàn phím dạng số có icon bàn phím chữ ở phía trên góc trái, cho phép chuyển đổi giữa bàn phím số sang bàn phím chữ và ngược lại. Khi hiển thị bàn phím chữ thì có icon bàn phím số ở phía trên góc trái (MH5)
• 
Thoát focus kiểm tra thông tin thụ hưởng  → Tham khảo logic xử lý

• 
Nếu chọn danh bạ thụ hưởng → Tham khảo logic xử lý
 | 

 | Trường hợp thêm Danh bạ thụ hưởng (Loại chuyển tiền nhanh 24/7 qua tài khoản) | 

 | 

5.2 | 
Ngân hàng thụ hưởng
 | Combobox | Click | Yes | -- | 
Hiển thị danh sách các ngân hàng thụ hưởng (Chỉ bao gồm các bank chuyển tiền nhanh 247) theo kết quả BE trả ra, có ưu tiên các ngân hàng lớn.

Khi điền tên ngân hàng thụ hưởng hiển thị tên Viết tắt kèm logo bên trên, bên dưới là tên đầy đủ của Ngân hàng
 | 

 | Số tài khoản thụ hưởng | Textbox | Input | Yes | 30 | 
Mặc định trống 

Placeholder: Tài khoản thụ hưởng

Cho phép nhập/chọn:

• Nếu nhập:
• Cho phép nhập tối đa 30 ký tự số và chữ
• Nếu dán vào ô tài khoản/số thẻ/số điện thoại mà có khoảng trống ở đầu hoặc/và cuối thì hệ thống tự xóa khoảng trống ở đầu hoặc/và cuối
• Khi focus vào ô tài khoản thụ hưởng, hệ thống hiển thị bàn phím dạng số có icon bàn phím chữ ở phía trên góc trái, cho phép chuyển đổi giữa bàn phím số sang bàn phím chữ và ngược lại. Khi hiển thị bàn phím chữ thì có icon bàn phím số ở phía trên góc trái (MH5)
• Nếu chọn danh bạ thụ hưởng → Tham khảo logic xử lý | 

 | Trường hợp thêm Danh bạ thụ hưởng (Loại chuyển tiền nhanh 24/7 qua thẻ)
 | 
5.3 | Số thẻ thụ hưởng | Textbox | Text | Yes | 30 | 
Mặc định bàn phím số. Cho phép chuyển sang bàn phím chữ

Sau khi thoát focus, kiểm tra thông tin và hiển thị Tên người thụ hưởng - Ngân hàng thụ hưởng
 | 

 | Trường hợp thêm Danh bạ thụ hưởng (Loại chuyển tiền qua GTTT) | 

 | 5.4 | 
Loại GTTT
 | 
Combobox
 | 
Select
 | 
Yes
 | 
--
 | 
Placeholder: Loại GTTT

Mặc định trống

Giá trị hiển thị cho chọn, fix tại client gồm:

• Chứng minh nhân dân
• Hộ chiếu
• CMT quân đội
• Thẻ căn cước công dân
Chỉ cho chọn 1 giá trị
 | 

 | 5.5 | 
Số GTTT
 | 
Textbox
 | 
Text
 | 
Yes
 | 
20
 | 
Placeholder: Số GTTT

Mặc định trống

Chỉ cho phép nhập ký tự số và chữ không dấu

Khi nhập, hiển thị dấu x cho phép xóa bỏ toàn bộ kỹ tự đã nhập

Trường hợp nhập số  CMND (Giấy tờ tùy thân chọn CMND), kiểm tra nếu khác 9 hoặc 12 ký tự -> thông báo "Số CMND không hợp lệ. Quý khách vui lòng kiểm tra lại."
 | 

 | 5.6 | 
Ngày cấp
 | 
Calendar
 | 
Select
 | 
Yes
 | 

 | 
Chỉ hiển thị khi chọn Loại giấy tờ

Placeholder: Ngày cấp

Mặc định trống

Định dạng: dd/mm/yyyy

Không cho chọn những ngày tương lai
 | 

 | 5.7 | 
Nơi cấp
 | Textbox/Combobx | Input/Select | Yes | 50 | 
Chỉ hiển thị khi chọn Loại giấy tờ

Chỉ cho phép KH nhập ký tự chữ tiếng Việt có dấu, có khoảng trắng và số. Hệ thống tự động bỏ dấu khi truyền sang server.

Hiển thị theo Loại GTTT:

• Nếu KH chon CMT quân đội, hiển thị dạng textbox cho KH tự nhập
• Nếu KH chọn Hộ chiếu, hiển thị giá trị "Cục Quản lý Xuất nhập cảnh" và có dấu "x" cho phép xóa toàn bộ ký tự để nhập lại.
• Nếu chọn CMND thị mặc định: "Cục CSĐKQL cư trú và DLQG về dân". KH có thể xóa đi nhâp lại nếu muốn nhập công an tỉnh/thành phố khác.
• Nếu chọn CCCD thi ra 2 lựa chọn: "Cục CSQLHC về TTXH" và "Cục CSĐKQL cư trú và DLQG về dân cư". Chỉ được chọn 1 trong 2 giá trị và không cho nhập sửa lại giá trị.
Lưu ý: Tại trường này sẽ có dấu "x" cho phép xóa toàn bộ ký tự hiện có nhé | 

 | 5.8 | 
Số điện thoại
 | 
Textbox
 | 
Number
 | 
--
 | 
10
 | 
Chỉ cho phép nhập số

Bắt đầu bằng số 0

Nếu chuỗi số nhập vào có độ dài khác 10 và không bắt đầu bằng số 0, hiển thị thông báo "Số điện thoại không đúng định dạng. Quý khách vui lòng kiểm tra lại."
 | 

 | 6 | 
Nút “Thêm mới”
 | 
Button
 | 
Click
 | -- | -- | 
 Mặc định Enable

Tham khảo logic xử lý
 | 

d/ Chi tiết danh bạ thụ hưởng
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

 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: CHI TIẾT DANH BẠ

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
 Nhấn Home, hiển thị màn hình chính của ứng dụng (Quay lại màn hình Home)

 | 4 | 
Chi tiết danh bạ thụ hưởng
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Các thông tin gồm:

• Loại chuyển tiền
• Thông tin thụ hưởng: (Với các loại chuyển tiền trừ chuyển tiền qua GTTT)
• Tên người thụ hưởng: Tên người thụ hưởng theo dữ liệu lưu tại Bank
• Tên gợi nhớ: Hiển thị trường này, cho phép chỉnh sửa
• Số tài khoản/ số thẻ thụ hưởng: Tương ứng với loại chuyển tiền
• Ngân hàng thụ hưởng
• Thông tin thụ hưởng: (Với các loại chuyển tiền trừ chuyển tiền qua GTTT):
• Loại GTTT
• Số GTTT
• Ngày cấp
• Nơi cấp
• Số điện thoại
• Tên gợi nhớ
 | 
5
 | 
Nút “Thực hiện giao dịch”
 | 
Button
 | 
Click
 | -- | -- | 
<Tham khảm logic xử lý>

 | 
6
 | 
Nút "Cập nhật"
 | 
Button
 | 
Click
 | -- | -- | 
<Tham khảm logic xử lý>

#### 4/ Luồng xử lý

MH1: Màn hình danh bạ
 | TT | Thao tác | Tác nhân | Mô tả
 | 
1
 | 
Truy cập chức năng “Danh bạ thụ hưởng”, 
 | 
MB Client
 | 
Gửi yêu cầu lấy danh sách danh bạ thụ hưởng chuyển tiền sang MB Server

 | 
MB Server
 | 
Truy vấn thông tin danh bạ thụ hưởng chuyển tiền, trả kết quả về cho MB client 

Server sắp xếp dữ liệu trả về cho client:

• Danh bạ: (Chuyển tiền nội bộ → Chuyển tiền nhanh 24/7 qua tài khoản → Chuyển tiền nhanh 24/7 qua thẻ). Các danh bạ trong mỗi nhóm sẽ được sắp theo mức độ thường xuyên sử dụng của danh bạ, khi thực hiện (từ cao tới thấp)
 | 
MB Client
 | 
Nhận kết quả:

1/ Nếu thành công và có danh sách: Hiển thị màn hình danh sách danh bạ như mô tả màn hình:  Danh sách danh bạ được phân theo các nhóm

• Chuyển tiền nội bộ
• Chuyển tiền nhanh 24/7 qua tài khoản
• Chuyển tiền nhanh 24/7 qua thẻ
Và có khả năng thu hẹp hoặc mở rộng các nhóm danh bạ này.

2/ Nếu không thành công: Hiển thị thông báo lỗi TimeOut: Yêu cầu tạm thời bị gián đoạn. Quý khách vui lòng thực hiện lại sau., và có chức năng Thử lại. Nhấn vào Thử lại gọi lấy lại danh sách danh bạ.

3/ Nếu thành công và không có danh sách: Hiển thị màn hình thông báo như mô tả màn hình

 | 
2
 | 
Nhấn vào một danh bạ thụ hưởng
 | 
MB Client
 | 
Hiển thị màn hình chi tiết thông tin danh bạ như đã mô tả

 | 
3

 | 
Thực hiện tìm kiếm
 | 
MB Client
 | 
Thực hiện tìm kiếm theo từ khóa nhập. Tìm kiếm gần đúng theo: Số tài khoản/ Số thẻ, Tên thụ hưởng (Tên theo Bank và tên gợi nhớ), Ngân hàng thụ hưởng, Số GTTT, Loại GTTT

• Nếu không có kết quả hợp lệ: Hiển thị thông báo "Không có kết quả tìm kiếm. Quý khách vui lòng kiểm tra lại."
• Nếu có kết quả hợp lệ: Hiển thị đúng kết quả theo từ khóa nhập.
 | 
6
 | 
Nhấn Thêm mới
 | 
MB Client
 | 
Hiển thị màn hình thêm mới danh bạ thụ hưởng 

 | 7.1 | 
Nhấn Xóa danh bạ
 | 
MB Client

 | 
Hiển thị chức năng Xóa nhiều danh bạ, hiển thị ô tích chọn những danh bạ muốn xóa.

Hiển thị Label cho click chọn chức năng "Hủy xóa danh bạ" để thay thế cho label tích chọn "Xóa danh bạ"

 | 7.2 | Nhấn Hủy xóa danh bạ | MB Client | Hiển thị MH danh bạ ban đầu
 | 7.3 | 
Chọn xóa nhiều danh bạ
 | 
MB Client
 | 
1/ Thực hiển kiểm tra:

• Không hợp lệ: Cấu hình và hiển thị popup thông báo: | | 
TT
 | 
Trường hợp lỗi
 | 
Tác nhân
 | 
Nội dung

 | 1 | Không có danh bạ nào được chọn | App Client | Quý khách vui lòng chọn danh bạ cần xóa

• Hợp lệ: Hiển thị thông báo: "Quý khách chắn chắn muốn xóa {số danh bạ KH đã chọn} danh bạ khỏi danh sách danh bạ?"

• Nút Hủy: Nhấn nút này, tắt thông báo và hiển thị màn hình đang thao tác trước đó.
• Nút Đồng ý: Nhấn nút này, ứng dụng gửi yêu cầu Xóa danh sách danh bạ sang MB Server.
 | 
MB Server
 | 
Thực hiện xóa danh sách danh bạ đã yêu cầu xóa khỏi danh sách và trả kết quả về cho client

 | 
MB Client
 | 
Nhận kết quả:

• Thành công: hiển thị thông báo: "Đã xóa danh bạ thụ hưởng thành công". Nút Đóng: Nhấn nút này, tắt thông báo và hiển thị màn hình danh bạ đã cập nhật lại danh sách. 
• Không thành công: hiển thị thông báo lỗi TimeOut: Yêu cầu tạm thời bị gián đoạn. Quý khách vui lòng thực hiện lại sau.
 | 8 | Nhấn vào phần thông tin danh bạ thụ hưởng | MB Client | Hiển thị màn hình chi tiết danh bạ thụ hưởng

MH3: Thêm mới danh bạ
 | TT | Thao tác | Tác nhân | Mô tả
 | 
1
 | 
Chon chức năng Thêm mới tại màn hình danh sách danh bạ
 | 
MB Client
 | 
Hiển thị màn hình THÊM MỚI DANH BẠ THỤ HƯỞNG mặc định loại chuyển tiền là Chuyển tiền nội bộ

 | 2 | 
Chọn loại chuyển tiền
 | 
MB Client
 | 
• Hiển thị danh sách các loại chuyển tiền gồm:
• Chuyển tiền nội bộ
• Chuyển tiền nhanh 24/7 qua tài khoản
• Chuyển tiền nhanh 24/7 qua thẻ
• Cho phép chọn 1 giá trị trong các giá trị trên. Giá trị đã được chọn sẽ được đánh dấu phân biệt
 | Trường hợp thêm mới danh bạ thụ hưởng chuyển tiền nội bộ
 | 
1
 | 
Nhập tài khoản/ số thẻ và thoát focus
 | 
MB Client
 | 
Kiểm tra validate:

1/ Không hợp lệ: 

• Nếu không thuộc 1

> ⚠️ *Nội dung đã cắt ngắn (27607 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 19.8. Câu hỏi thường gặp

> **Page ID:** `37675506` · **Version:** 10
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37675506

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, App Client
• Điều kiện trước: 

• KH cài đặt ứng dụng thành công
• KH đã đăng nhập thành công vào ứng dụng
• Kết quả mong muốn:
• KH xem được danh sách câu hỏi thường gặp và câu trả lời
#### 2/ Luồng màn hình

##### MH1: MH danh sách chức năng Hỗ trợ

##### MH2: MH Danh sách Câu hỏi thường gặp

##### MH3: MH Xem chi tiết câu trả lời

3/ Mô tả màn hình

##### MH1: MH danh sách chức năng Hỗ trợ
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
HỖ TRỢ

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn Back, hiển thị màn hình thao tác trước đó
 | 3 | Icon Home | Icon | Click | -- | -- | Quay lại MH Home
 | 4 | Danh sách chức năng | Icon | Click | -- | -- | 
Gồm các chức năng:

• Câu hỏi thường gặp
• Liên hệ - thông tin ứng dụng

##### MH2: MH Danh sách Câu hỏi thường gặp + MH3: MH Xem chi tiết câu trả lời
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
CÂU HỎI THƯỜNG GẶP

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn Back, hiển thị màn hình thao tác trước đó
 | 3 | Tìm kiếm | Textbox | Input | -- | 200 | Cho phép tìm kiếm tương đối trên Client theo nội dung input vào
 | 4 | Danh sách câu hỏi | Icon | Click | -- | -- | 
Hiển thị nhóm câu hỏi và danh sách câu hỏi tương ứng với mỗi nhóm

Có Icon thu gọn/ mở rộng tại mỗi câu hỏi để mở/ đóng câu trả lời

#### 4/ Luồng xử lý

 | | 

 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Click Icon Câu hỏi thường gặp tại MH1: MH Hỗ trợ | 
MB Client
 | 
Hiển thị MH2: MH Danh sách Câu hỏi thường gặp

 | 2 | Click mở rộng/ thu hẹp tại mỗi câu hỏi tại 
##### MH2: MH Danh sách Câu hỏi thường gặp
 | 
MB Client
 | 
Hiển thị câu trả lời tương ứng

Đóng câu trả lời, trở về danh sách ban đầu

 | 3 | Nhập nội dung tìm kiếm | App Client | 
Tìm kiếm tương đối trên DS câu hỏi và hiển thị danh sách câu hỏi theo kết quả tìm kiếm

• Không có danh sách: Thông báo: "Quý khách vui lòng liên hệ Hotline 1900545554 hoặc CN/PGD gần nhất để được giải đáp"
• Có danh sách: Hiển thị danh sách tương ứng theo nội dung tìm kiếm.

---

### 19.9. Địa điểm ATM/ Chi nhánh

> **Page ID:** `37675544` · **Version:** 28
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37675544

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Thời gian cập nhật
 | 
 | A | HongLT | 
 | 
Tạo mới
 | V1.0.0 | 

 | 
 
 | M | ThaoCY | V1.0.0 | 
Bỏ tìm kiếm địa điểm ATM/Chi nhánh theo Quận/Huyện. 

Cho phép tìm kiếm địa điểm ATM/Chi nhánh theo 1 phường xã cụ thể hoặc tất cả Phường xã
 | V1.0.1 | 

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, App Client, App server
• Điều kiện trước: 

• KH cài đặt ứng dụng thành công
• Kết quả mong muốn:
• KH thực hiện tra cứu được ATM chi nhánh của ngân hàng thành công
• hiển thị đầy đủ
#### 2/ Luồng màn hình

##### MH0: MH danh sách chức năng Hỗ trợ

##### MH1: MH địa điểm ATM/ Chi nhánh gần nhất

##### MH2: MH Lọc tìm kiếm theo Tỉnh thành

##### MH3: MH Lọc tìm kiếm theo Phường/Xã

2/ Mô tả màn hình

##### MH0: MH danh sách chức năng Hỗ trợ

Tham khảo tại URD chức năng câu hỏi thường gặp

##### MH1: MH địa điểm ATM/Chi nhánh gần nhất
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
Tiêu đề: ĐỊA ĐIỂM ATM/ CHI NHÁNH

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | Icon Home | Icon | Click | -- | -- | Quay lại MH Home
 | 4 | Chọn Tỉnh/ Thành phố | Combobox | Click | -- | -- | Focus hiển thị MH2: MH Lọc tìm kiếm theo Tỉnh thành
 | 5 | Chọn Quận/ Huyện | Combobox | Click | -- | -- | 
Focus hiển thị MH3: MH Lọc tìm kiếm theo Quận huyện

KH cần chọn Tỉnh/ Thành phố trước khi chọn Quận/ Huyện.

 | 6 | Chọn Phường/xã | Combobox | Click | -- | -- | 
Focus hiển thị MH3: MH Lọc tìm kiếm theo Phường/Xã

KH cần chọn Tỉnh/ Thành phố trước khi chọn Phường xã

Bắt buộc nếu chọn Tỉnh thành

 | 7 | 
Map bản đồ
 | 
Map
 | 
View/ Click
 | -- | -- | 
• Hiển thị vị trí của người dùng (nếu KH đã bật định vị của ứng dụng)
• Mặc định hiển thị tối đa 15 vị trí ATM/CN/PGD gần nhất với vị trí người dùng (bán kính 20KM) hoặc hiển thị các vị trí theo tiêu chí tìm kiếm/lọc.
• Cho phép thao tác vào mỗi vị trí và hiển thị các thông tin:
• Tên địa điểm ATM/CN
• Địa chỉ chi tiết
• Khoảng cách tới vị trí hiện tại của KH
• Khi thao tác vào mỗi vị trí trên bản đồ thì tên vị trí trong danh sách dưới cũng được focus highlight.
• Có Icon cho phép người dùng chọn lại vị trí gần nhất. Khi đã chọn các vị trí khác, mặc định về giá trị có hinttext như default  "Chọn Tỉnh/ Thành phố" và "Chọn Quận/ Huyện" 
 | 8 | Chọn loại địa điểm  | Label | Click | -- | -- | 
Gồm các giá trị:

• ATM: Giá trị mặc đinh
• Chi nhánh/ PGD
 | 9 | 
Danh sách vị trí
 | 
List
 | 
View
 | -- | -- | 
• Mặc định hiển thị tối đa 15 vị trí ATM/CN gần nhất với vị trí người dùng (bán kính 20KM) hoặc hiển thị các vị trí theo tiêu chí tìm kiếm/lọc, sắp xếp theo khoảng cách tới KH từ gần nhất tới xa nhất nếu KH đã bật định vị của ứng dụng. Trường hợp chưa bật định vị hoặc chưa nhập vị trí muốn tìm kiếm, hiển thị trống.
• Mỗi vị trí hiển thị các thông tin bao gồm:
• Tên địa điểm ATM/CN
• Địa chỉ chi tiết
• Khoảng cách (do Server trả về)
• Icon loại vị trí: ATM, Chi nhánh, PGD, Hội sở (fix tại client theo type)
• Chỉ đường: Click hiển thị google map dẫn đường tới vị trí địa điểm
• Cho phép vuốt lên xuống trong danh sách.
Lưu ý: Khoảng cách chỉ hiển thị khi lấy theo “Địa điểm gần đây”

##### MH2: MH Lọc tìm kiếm theo Tỉnh thành
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
Tiêu đề: Chọn Tỉnh/ Thành phố

 | 2 | Icon đóng | Icon | Click | -- | -- | Đóng popup, quay lại MH Địa điểm ATM/ Chi nhánh
 | 3 | Icon Home | Icon | Click | -- | -- | Quay lại MH Home
 | 4 | Danh sách Tỉnh/ Thành phố | ListView | 
Click
 | -- | -- | 
Danh sách Tỉnh/Thành phố do Server trả về, có ưu tiên 4 Tỉnh/ Thành phố lớn: Hà Nội, Hồ Chí Minh, Đà Nẵng, Hải Phòng, Cần thơ, các Tỉnh/ Thành phố khác theo thức tự A-Z

Click chọn một Tỉnh/ Thành phố để chọn fill Tỉnh/ Thành phố

<Tham khảo logic xử lý>

 | 5 | Tìm kiếm | Textbox | Click | -- | -- | 
Cho phép tìm kiếm tương đối theo ký tự nhập vào

<Tham khảo logic xử lý>

 | 6 | 
Thao tác
 | 
Action
 | 
Click
 | -- | -- | 
Click vào điểm ngoài popup để đóng popup

##### MH3: Mh Lọc tìm kiếm theo Phường/ Xã
 | | 
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
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Chọn Phường/ Xã

 | Icon đóng | Icon | Click | -- | -- | Đóng popup, quay lại MH Địa điểm ATM/ Chi nhánh
 | Icon Home | Icon | Click | -- | -- | Quay lại MH Home
 | Danh sách Phường/Xã | ListView | 
Click
 | -- | -- | 
Danh sách Phường/Xã theo Tỉnh/Thành phố người dùng lựa chọn trước đó do Server trả về. Sắp xếp theo thứ tự Server trả về

Click chọn 1 giá trị để fill Phường/Xã

Có giá trị mặc định là "Tất cả"

<Tham khảo logic xử lý>

 | Tìm kiếm | Textbox | Click | -- | -- | 
Cho phép tìm kiếm tương đối theo ký tự nhập vào

<Tham khảo logic xử lý>

 | 
Thao tác
 | 
Action
 | 
Click
 | -- | -- | 
Click vào điểm ngoài popup để đóng popup

##### MH3: MH Lọc tìm kiếm theo Quận huyện
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
Tiêu đề: Chọn Quận huyện

 | 2 | Icon đóng | Icon | Click | -- | -- | Đóng popup, quay lại MH Địa điểm ATM/ Chi nhánh
 | 3 | Danh sách Quận/Huyện | ListView | 
Click
 | -- | -- | 
Danh sách Quận/Huyện theo Tỉnh/Thành phố người dùng lựa chọn trước đó do Server trả về. Sắp xếp thứ tự server trả về.

Click chọn một Quận/ Huyện để chọn fill Quận/ Huyện

<Tham khảo logic xử lý>

 | 4 | 
Thao tác
 | 
Action
 | 
Click
 | -- | -- | 
Click vào điểm ngoài popup để đóng popup

#### 4/ Luồng xử lý

##### Truy cập chức năng: ĐỊA ĐIỂM ATM/ CHI NHÁNH
 | TT | Thao tác | Tác nhân | Mô tả
 | 1 | 
Từ MH Home, chọn Cài đặt, chọn Hỗ trợ

Từ MH đăng nhập trước login, chọn Hỗ trợ
 | 
App Client
 | 
Hiển thị MH0: MH danh sách chức năng Hỗ trợ

##### MH1: MH địa điểm ATM/ Chi nhánh gần nhất
 | TT | Thao tác | Tác nhân | Mô tả
 | 1 | 
Khởi tạo màn hình Địa điểm ATM/Chi nhánh

Hoặc click chọn Tỉnh/Thành phố > nhấn "Địa điểm gần nhất"

 | 
App Client
 | 
Kiểm tra trạng thái định vị của thiết bị:

• Nếu chưa bật hoặc không cho phép sử dụng, hiển thị thông báo: "Bật định vị để cho phép ứng dụng xác định vị trí của Quý khách"
• Nút "Đóng": Nhấn nút, đóng thông báo hiển thị màn hình địa điểm ATM/chi nhánh với hình ảnh bản đồ ko có thông tin định vị của người dùng (xem tại mô tả màn hình).
• Nút "Đồng ý": Nhấn nút này, truy cập tính năng cài đặt định vị tương ứng của thiết bị.
• Nếu đã bật, gửi yêu cầu lấy danh sách địa điểm ATM gần nhất sang App Server
 | 
App Server
 | 
Căn cứ vào tọa độ vị trí người dùng và vị trí tọa độ của địa điểm ATM để tính khoảng cách và trả kết quả về cho Client theo quy định bán kính tối đa là 20 KM.

 | 
App Client
 | 
Hiển thị màn hình ATM/CN với kết quả danh sách đã trả về.

 | 2 | Bấm chọn tìm kiếm Loại địa điểm là PGD | App Client | 
Gửi yêu cầu sang App Server lấy danh sách PGD thỏa mãn các điều kiện tìm kiếm theo Gần đây nhất/Khu vực (Tỉnh/Thành phố, Quận huyện)

 | 
App Server
 | 
Xử lý và trả kết quả về cho client

 | App Client | 
Hiển thị màn hình kết quả trên Danh sách và đánh dấu các vị trí ATM trên bản đồ

 | 3 | Bấm chọn tìm kiếm Loại địa điểm là Chi nhánh | App Client | 
Gửi yêu cầu sang App Server lấy danh sách Chi nhánh thỏa mãn các điều kiện tìm kiếm theo Gần đây nhất/Khu vực (Tỉnh/Thành phố, Quận huyện)

 | 
App Server
 | 
Xử lý và trả kết quả về cho client

 | App Client | 
Hiển thị màn hình kết quả trên Danh sách và đánh dấu các vị trí Chi nhánh trên bản đồ

 | Logic xử lý riêng khi tìm kiếm ATM/Chi nhánh trên MB
 | 4 | 
Focus vào ô Tỉnh thành phố

 | 
MB Client
 | 
Gửi yêu cầu lấy danh sách tỉnh thành sang app server

 | 
App Server
 | 
Xử lý và trả kết quả về cho client

• Không thành công: Trả thông báo lỗi tương ứng
• Thành công: Trả danh sách tương ứng
 | 
MB Client
 | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng
• 
##### Thành công: Hiển thị popup danh sách tương ứng như MH2: MH Lọc tìm kiếm theo Tỉnh thành

 | 
 | 
Chọn 1 tỉnh thành
 | 
MB Client
 | 
Hiển thị tên tỉnh thành đã chọn

 | 
 | 
Focus vào ô Phường/Xã
 | 
MB Client
 | 
Kiểm tra:

• Chưa chọn Tỉnh/ Thành phố: Hiển thị thông báo: "Quý khách vui lòng chọn Tỉnh/ Thành phố"
• Đã chọn Tỉnh/ Thành phố: Gửi yêu cầu lấy danh sách Phường/Xã tương ứng với Tỉnh/ Thành phố đã chọn qua mid 379 (mid mới)
 | 
 | 
 
 | 
MB server
 | 
Xử lý và trả kết quả về cho client:

• Không thành công: Trả thông báo lỗi tương ứng
• Thành công: Trả danh sách tương ứng
 | 
 | 
 
 | 
MB Client
 | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng
• 
Thành công: Hiển thị popup danh sách tương ứng như MH3: MH Lọc tìm kiếm theo Phường xã

 | 
 | 
Chọn 1 Phường/Xã
 | 
MB Client
 | 
Gửi yêu cầu lấy danh sách ATM, CN,PGD tương ứng với Tỉnh thành đã chọn đến MB server qua mid 390

Input cập nhật: 

• thay vì truyền districtCode thì truyền wardCode
• Nếu người dùng chọn "Tất cả" → Truyền Null
 | 
 | 
 
 | 
MB server
 | 
Truy vấn và trả kết quả cho MB client

• Không thành công: Trả thông báo lỗi tương ứng
• Thành công: Trả danh sách
• Nếu wardCode=Null → Trả giá trị danh sách tất cả ATM/Phòng giao dịch thuộc cityCode tương ứng
 | 
 | 
 
 | 
MB Client
 | 
Hiển thị danh sách ATM/ PGD/ Chi nhánh tương ứng theo tiêu chi tìm kiếm

 | 5 | 
Focus vào ô Quận huyện

 | 
MB Client
 | 
Kiểm tra:

• Chưa chọn Tỉnh/ Thành phố: Hiển thị thông báo: "Quý khách vui lòng chọn Tỉnh/ Thành phố"
• Đã chọn Tỉnh/ Thành phố: Gửi yêu cầu lấy danh sách Quận huyện tương ứng với Tỉnh/ Thành phố đã chọn
 | 
App Server
 | 
Xử lý và trả kết quả về cho client:

• Không thành công: Trả thông báo lỗi tương ứng
• Thành công: Trả danh sách tương ứng
 | 
MB Client
 | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng
• 
Thành công: Hiển thị popup danh sách tương ứng như MH3: MH Lọc tìm kiếm theo Quận huyện

 | 6 | Chọn một Quận huyện | MB Client | Xử lý hiển thị danh sách ATM, CN, PGD tương ứng ở Tỉnh/ Thành phố và Quận huyện đã chọn theo thứ tự do server trả về
 | 7 | Chọn PGD/ Chi nhánh | MB Client | Hiển thị danh sách ATM/ PGD/ Chi nhánh tương ứng theo tiêu chi tìm kiếm
 | 8 | Nhấn chọn Icon vị trí gần nhất | MB client | Thực hiện hiển thị vị trí các ATM/ PGD/ Chi nhánh tương ứng, hiển thị Combobox "Chọn Tỉnh/ Thành phố" và "Chọn Quận/ Huyện" về giá trị mặc định với hinttext như giá trị default.

---

### 19.10. Liên hệ

> **Page ID:** `37675707` · **Version:** 15
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37675707

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, App Client
• Điều kiện trước: 

• KH cài đặt ứng dụng thành công
• KH đã đăng nhập thành công vào ứng dụng
• Kết quả mong muốn:
• KH xem được nội dung Liên hệ
#### 2/ Luồng màn hình

##### MH0: MH danh sách chức năng Hỗ trợ

##### MH1.1: MH Liên hệ (thu gon)

##### MH1.2: MH Liên hệ (Mở rộng)

MH2: MH Popup hotline

##### MH3: MH Liên hệ (thu gon) - Đi từ màn hình login

##### MH3.1: MH Liên hệ (Mở rộng) - Đi từ màn hình login

3/ Mô tả màn hình

##### MH0: MH danh sách chức năng Hỗ trợ

Xem chi tiết tại chức năng Câu hỏi thường gặp

##### MH1.1, 1.2, 3, 3.1: MH Liên hệ (thu gọn - mở rộng)
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
LIÊN HỆ

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn Back, hiển thị màn hình thao tác trước đó
 | 3 | Icon Home | Icon | Click | -- | -- | Nhấn Home, quay về MH Trang chủ (không hiển thị ở màn hình 3 và 3.1)
 | 4 | Logo + Tên app | Label | Read Only | -- | -- | Hiển thị Logo bank + "Co-opBank Mobile Banking"
 | 5 | Danh sách thông tin | Icon | Click | -- | -- | 
Gồm các thông tin: 

• Câu hướng dẫn: Co-opbank Online là ứng dụng tương thích với điện thoại thông minh chạy hệ điều hành IOS và Android. Ứng dụng này mang đến cho Quý khách trải nghiệm các dịch vụ ngân hàng tiện lợi nhất.
• Trụ sở chính: Hiển thị vị trí dạng đường link của Bank, nhấn vào link đến google map hiển thị vị trí: Tầng 4 - Tòa nhà N04 - Hoàng Đạo Thúy - P. Yên Hòa - TP Hà Nội

• Hotline: Nhấn vào, hiển thị popup thông báo như MH2
• Email: Hiển thị Email, nhấn vào cho phép dùng các ứng dụng hiện tại của App để gửi mail tới bank
• Website: Nhấn vào, mở link tới Website của bank
• Thông tin ứng dụng: Icon Mở rộng/ thu hẹp hiển thị chi tiên thông tin. Gồm:
• Phiên bản
• Cập nhật
• Dung lượng
• Ngôn ngữ

##### MH2: MH Popup hotline
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
Gọi tổng đài hỗ trợ

 | 2 | Nội dung | Label | ReadOnly | -- | -- | Fix tại Client: 1900545554
 | 3 | Gọi | Icon | Click | -- | -- | Thực hiện gọi tới hotline bằng ứng dụng Gọi điện của thiết bị
 | 4 | Hủy | Icon | Click | -- | -- | Quay lại MH trước đó

#### 4/ Luồng xử lý

##### Truy cập chức năng: Tạo điện chuyển tiền trong hệ thống
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | Từ MH danh sách chức năng Hỗ trợ
 | 
1

 | 
Tại màn hình Hỗ trợ chọn chức năng Liên hệ - Thông tin ứng dụng
 | 
App Client
 | 
Hiển thị MH1: MH Liên hệ - Thông tin ứng dụng

 | Từ MH login, chọn chức năng Hỗ trợ
 | 2 | Tại màn hinh đăng nhập > click chọn "Hỗ trợ" | App Client | Hiển thị màn hình Liên hệ (MH3/3.1)

##### MH1.1, 1.2: MH Liên hệ
 | | 

 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Click vào địa chỉ Trụ sở chính | App Client | Mở ứng dụng hiển thị google map vị trí Trụ sở chính
 | 2 | Click link SĐT | 
App Client
 | 
Hiển thị ứng dụng thiết bị cho phép gọi điện

 | 3 | Click vào Email Bank | 
App Client
 | 
Cho phép mở ứng dụng mail tạo mail mới đươc fill sắn thông tin người nhận và người gửi

 | 4 | Click vào Website | App Client | Hiển thị thông tin website của bank
 | 5 | Click Mở rộng/ Thu gọn thông tin ứng dụng | App Client | Hiển thị thông tin chi tiết như MH 1.2 khi mở rộng, MH 1.1 khi thu gọn

##### MH2: MH Popup hotline
 | | 

 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhấn Gọi | 
App Client
 | 
Hiển thị ứng dụng thiết bị cho phép gọi điện

 | 2 | Nhấn Hủy | 
App Client
 | 
Quay lại MH 1.1

---

### 19.11. Cài đặt - Xem nhanh mã QR

> **Page ID:** `881722476` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/881722476

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*1 trang con:*

#### 19.11.1. (Bank) User Action Flow - Xem nhanh mã QR

> **Page ID:** `879855956` · **Version:** 9
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/879855956

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Thời gian cập nhật
 | 
 
 | A | ThaoCY | 
 | 
Tạo mới
 | V1.0.0 | 

Mục lục
none

### 1/ Usecase Summary
 | Use Case Name | Cài đặt - Xem nhanh mã QR
 | Use Case ID | --
 | Use Case Description | 
Khách hàng cài đặt ON/OFF hiển thị mã QR tại màn hình login

 | Actor | 
KH, Hệ thống MB

 | Priority | --
 | 
Trigger
 | 
Khách hàng chọn "Xem nhanh mã QR" tại chức năng Cài đặt

 | 
Pre-Condition
 | 
• Khách hàng đã cập nhật lên phiên bản mới
• Khách hàng đã đăng nhập Mobile Banking thành công.
 | 
Post-Condition
 | 
• Khách hàng cài đặt số tài khoản xem nhanh thành công
• KH xem nhanh được QR tài khoản đã cài đặt tại MH login <tham chiếu >
 | 
Basic Flow
 | 
1/ KH chọn "Xem nhanh mã QR" tại chức năng Cài đặt

2/ Hiển thị màn hình Xem nhanh mã QR

3/ Người dùng ON/OFF toggle button để Bật/Tắt hiển thị nhanh mã QR

4/ Hệ thống hiển thị poup xác nhận 

5/ Người dùng chọn "Đồng ý"

6/ Hệ thống hiển thị popup thông báo bật/tắt thành công

 | 
Alternative Flow
 | 
1/ KH chưa cài đặt xem nhanh mã QR và chọn "Mã QR của tôi" tại màn hình Home

2/ Hệ thống hiển thị popup thông báo → KH chọn "Cài đặt ngay"

3/ Hệ thống điều hướng vào màn hình đăng nhập:

• Với KH đã cài Face ID: yêu cầu quét khuôn mặt luôn
• Với KH cài Touch ID: yêu cầu hiển thị màn hình quét vân tay
• Với KH ko cài Face/ Touch: yêu cầu zoom vào dòng nhập mật khẩu, hiển thị sẵn bàn phím
 | 
Business Rules
 | 
1/ Trạng thái bật/tắt tính năng "Xem nhanh mã QR" chỉ được lưu tại MB Client

2/ Trạng thái ON/OFF chỉ áp dụng trên đúng thiết bị nơi người dùng thiết lập, không đồng bộ sang thiết bị khác của cùng KH

3/ Khi người dùng gỡ ứng dụng, cài lại → Trạng thái mặc định = OFF

#### 2/ Danh sách màn hình

##### MH1: Cài đặt

##### MH2: Xem nhanh mã QR

##### MH3: Xác nhận ON

##### MH4: Thông báo ON thành công

##### MH5: Xác nhận OFF

##### MH6: Thông báo OFF thành công

### 3/ Mô tả màn hình

##### MH1: Cài đặt

Bổ sung chức năng: Xem nhanh mã QR

##### MH2: Xem nhanh mã QR
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | - | - | Xem nhanh mã QR
 | 2 | Icon Back | Icon | Click | - | - | Click để quay về màn hình trước đó
 | 3 | Icon Home | Icon | Click | - | - | Click để điều hướng đến màn hình trang chủ
 | 4 | Lưu ý | Label | ReadOnly | - | - | Lưu ý: 
Sau khi bật tính năng, Mã QR của Quý khách sẽ hiển thị nhanh chóng ngay từ màn hình đăng nhập. Để đảm bảo an toàn tài chính, Quý khách tuyệt đối không chia sẻ Mã QR và thông tin cá nhân cho người lạ.
 | 5 | Danh sách tài khoản thanh toán | Toggle | Click | - | - | 
 Hiển thị danh sách tài khoản thanh toán của khách hàng, gồm các thông tin:

• Tài khoản: Hiển thị số tài khoản của KH
• Tên Alias: Hiển thị tên alias của tài khoản <nếu có>
• Số dư khả dụng: hiển thị số tiền + VND
• Toggle: Hiển thị theo dữ liệu lưu tại client
• Hiển thị ON các tài khoản đã cài đặt
• Hiển thị OFF các tài khoản chưa cài đặt
• Mặc định: OFF

##### MH3: Xác nhận ON
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | - | - | Thông báo
 | 2 | Nội dung | Label | ReadOnly | - | - | Quý khách đang thực hiện BẬT tính năng hiển thị nhanh mã QR của tôi mà không cần đăng nhập ứng dụng. Quý khách có muốn BẬT tính năng này không?
 | 3 | Đóng | Button | Click | - | - | Click để đóng popup
 | 4 | Đồng ý | Button | Click | - | - | <tham chiếu logic xử lý>

##### MH5: Xác nhận OFF
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | - | - | Thông báo
 | 2 | Nội dung | Label | ReadOnly | - | - | Quý khách có muốn TẮT tính năng hiển thị nhanh mã QR của tôi mà không cần đăng nhập không?
 | 3 | Đóng | Button | Click | - | - | Click để đóng popup
 | 4 | Đồng ý | Button | Click | - | - | <tham chiếu logic xử lý>

### 4/ Logic xử lý

##### MH1: Cài đặt
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn "Xem nhanh mã QR" | Hệ thống MB | Gửi yêu cầu truy vấn danh sách tài khoản thanh toán đến MB server
 | Bank server | 
1/ Nhận yêu cầu và lấy danh sách tài khoản thanh toán

2/ Kiểm tra và xác định rule được phép thực hiện các loại giao dịch của mỗi tài khoản đến Hệ thống MB

 | 
Hệ thống MB
 | 
1/ Nhận kết quả:

• Không thành công:Hiển thị thông báo lỗi " Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại sau.",  button "Đóng".
• Nhấn "Đóng:  Đóng câu thông báo, quay lại màn hình cài đặt
• Thành công: Chuyển bước 2
 2/  Kết quả trả về:

• Nếu có tài khoản thanh toán: Kiểm tra trạng thái ON/OFF xem nhanh mã QR cho từng tài khoản và hiển thị trạng thái ON/OFF tương ứng
• Nếu không có tài khoản thanh toán, hiển thị thông báo dạng popup "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!"

##### MH2: Xem nhanh mã QR
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Nhấn toggle OFF → ON | Hệ thống MB | 
Hiển thị thông báo "Quý khách đang thực hiện BẬT tính năng hiển thị nhanh mã QR của tôi mà không cần đăng nhập ứng dụng. Quý khách có muốn BẬT tính năng này không?"

• Đóng: Tắt popup thông báo
• Đồng ý: Hệ thống MB lưu lại STK của KH cài đặt  và hiển thị thông báo "Quý khách đã bật tính năng xem nhanh mã QR của tôi tại màn hình đăng nhập ứng dụng thành công!"
• Nhấn "Đóng": Tắt popup, giữ nguyên màn hình hiện tại
 | 2 | Nhấn toggle ON → OFF | Hệ thống MB | 
Hiển thị thông báo "Quý khách có muốn TẮT tính năng hiển thị nhanh mã QR của tôi mà không cần đăng nhập không?" 

• Đóng: Tắt popup thông báo
• Đồng ý: MB Client hủy bỏ số tài khoản của KH cài đặt và hiển thị thông báo "Quý khách đã tắt tính năng xem nhanh mã QR của tôi tại màn hình đăng nhập ứng dụng thành công!"
• Nhấn "Đóng": Tắt popup, giữ nguyên màn hình hiện tại

---


