# 📋 Tài khoản

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `core/`
> **Trích xuất:** 2026-03-28

---

## 15. URD_MB_COOPBANK_TÀI KHOẢN

> **Page ID:** `29889759` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29889759

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*4 trang con:*

### 15.1. MB_Màn hình tài khoản

> **Page ID:** `29890398` · **Version:** 15
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29890398

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 | A | Vũ Thị Trang | 
 | Tạo mới tài liệu | 

 | 
 
 | M | Lê Thị Hồng | 
 | 
Cập nhật thêm thông tin về khoản vay tại Danh sách tài khoản vay:

• Ngày giải ngân
• Ngày đáo hạn | V2.0
 | 
 
 | M | Lê Thị Hồng | 
 | 
Cập nhật bổ sung thêm Alias của danh sách TKTT (nếu có)
 | V3.0
 | 
 
 | M | NhungNTH8 | 
 | 
Cập nhật bổ sung tài khoản có tiền gửi tích lũy
 | V4.0

##### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client, MB Server, Bank Server
• Điều kiện trước:
• KH đăng nhập ứng dụng thành công.
• Kết quả mong muốn:
• Hiển thị dach sách tài khoản: tài khoản thanh toán, tài khoản tiết kiệm, tài khoản vay
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

##### MH1.1: Màn hình danh sách tài khoản thanh toán - Không có Alias (Giữ nguyên)

##### MH1.2: Màn hình danh sách tài khoản thanh toán- Có Alias

##### MH2: Màn hình danh sách tài khoản tiết kiệm- Có tiền gửi tích lũy

##### MH3: Màn hình danh sách tài khoản vay

##### MH4:Màn hình tài khoản trường hợp chỉ có tài khoản thanh toán

##### MH5: Màn hình tài khoản trường hợp không có tài khoản tiết kiệm

##### MH6: Màn hình tài khoản trường hợp không có tài khoản vay

#### Mô tả màn hình:

###### a) Màn hình danh sách tài khoản thanh toán
 | 
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
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Tài khoản

 | 
2
 | 
Nút Back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn nút này, hiển thị màn hình đang thao tác trước đó.

 | 
3
 | 
Tài khoản thanh toán 
 | 
List
 | 
Click
 | 
--
 | 
--
 | 
Hiển thị gồm: 

• Số lượng tài khoản(Do Bank server trả về)
• Tổng số dư khả dụng(Do Bank server trả về)
• Danh sách tài khoản thanh toán
• Số tài khoản. Trường hợp tài khoản là mặc định hiển thị thêm label "Tài khoản mặc định"
• Alias: Hiển thị Alias hoạt động của số tài khoản nếu bank trả về (nếu có). Bank trả ra sẵn trong API Danh sách tài khoản thanh toán các Alias có trạng thái Hoạt động.
• Số dư khả dụng(Hiển thị số dư khả dụng theo theo đúng giá trị api bank trả về)
Mặc định: Hiển thị tài khoản mặc định trên cùng, nếu không có tài khoản mặc định (đã tất toán tài khoản thanh toán mặc định) hiển thị tài khoản đầu tiên trong danh sách server trả về.

Có icon cho phép sao chép số tài khoản

Có icon mũi tên: Click vào hiển thị màn hình chi tiết của tài khoản đã chọn

Icon thu gọn hiển thị khi đang mở rộng vùng hiển thị danh sách tài khoản

 | 
4
 | 
Tài khoản tiết kiệm 
 | 
Text
 | 
Click
 | 
--
 | 
--
 | 
Icon mở rộng hiển thị khi đang thu gọn vùng hiển thị danh sách tài khoản

 | 
5
 | 
Tài khoản tiền vay
 | 
Text
 | 
Click
 | 
--
 | 
--
 | 
Icon mở rộng hiển thị khi đang thu gọn vùng hiển thị danh sách tài khoản

 | 
6
 | 
Icon làm mới
 | 
Icon
 | 
click
 | 
--
 | 
--
 | 
Lấy lại danh sách tài khoản và cập nhật thông tin mới nhất

###### b) Màn hình danh sách tài khoản tiết kiệm
 | 
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
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Tài khoản

 | 
2
 | 
Nút Back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn nút này, hiển thị màn hình đang thao tác trước đó.

 | 
3
 | 
Tài khoản thanh toán 
 | 
List
 | 
Click
 | 
--
 | 
--
 | 
Hiển thị gồm: 

• Số lượng tài khoản(Do Bank server trả về)
Icon mở rộng hiển thị khi đang thu gọn vùng hiển thị danh sách tài khoản

 | 
4
 | 
Tài khoản tiết kiệm 
 | 
List
 | 
Click
 | 
--
 | 
--
 | 
Hiển thị gồm: 

• Số lượng tài khoản(do Bank server trả về)
• Tổng số dư gốc hiện tại(do Bank server trả về)
• Danh sách tài khoản tiết kiệm, gồm thông tin:
• Số tài khoản
• Ngày đáo hạn: dd/mm/yyyy
• Loại tiền gửi: productName
• Số dư gốc hiện tại
Mặc định hiển thị theo danh sách server trả về

Click vào tài khoản → hiển thị màn hình hình chi tiết tài khoản đã chọn

Trường hợp không có dữ liệu không hiển thị như màn hình 5(MH5)

Hiển thị danh sách tài khoản tiết kiệm chưa tất toán

Icon thu gọn hiển thị khi đang mở rộng vùng hiển thị danh sách tài khoản

 | 
5
 | 
Tài khoản tiền vay
 | 
Text
 | 
Click
 | 
--
 | 
--
 | 
Số lượng tài khoản (do bank server trả về)

Icon mở rộng hiển thị khi đang thu gọn vùng hiển thị danh sách tài khoản

 | 
6
 | 
Icon làm mới
 | 
Icon
 | 
click
 | 
--
 | 
--
 | 
Lấy lại danh sách tài khoản và cập nhật thông tin mới nhất

###### c) Màn hình danh sách tài khoản vay
 | 
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
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Tài khoản

 | 
2
 | 
Nút Back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn nút này, hiển thị màn hình đang thao tác trước đó.

 | 
3
 | 
Tài khoản thanh toán 
 | 
List
 | 
Click
 | 
--
 | 
--
 | 
Hiển thị gồm: 

• Số lượng tài khoản(Do Bank server trả về)
Icon mở rộng hiển thị khi đang thu gọn vùng hiển thị danh sách tài khoản

 | 
4
 | 
Tài khoản tiết kiệm 
 | 
Text
 | 
Click
 | 
--
 | 
--
 | 
Hiển thị gồm: 

• Số lượng tài khoản(Do Bank server trả về)
Icon thu gọn hiển thị khi đang mở rộng vùng hiển thị danh sách tài khoản

 | 
5
 | 
Tài khoản tiền vay 
 | 
List
 | 
Click
 | 
--
 | 
--
 | 
Hiển thị gồm:

• Số lượng tài khoản(do Bank server trả về)
• Tổng số dư nợ gốc hiện tại (do Bank server trả về)
• Danh sách tài khoản vay gồm (Dữ liệu Bank trả về)
• Số tài khoản
• Dư nợ gốc hiện tại
• Ngày giải ngân
• Ngày đáo hạn
Mặc định hiển thị tài khoản theo trong danh sách server trả về.

Có icon mũi tên: Click vào hiển thị màn hình hình chi tiết tài khoản đã chọn

Trường hợp không có dữ liệu không hiển thị như màn hình 6(MH6)

Icon thu gọn hiển thị khi đang mở rộng vùng hiển thị danh sách tài khoản

 | 
6
 | 
Icon làm mới
 | 
Icon
 | 
click
 | 
--
 | 
--
 | 
Lấy lại danh sách tài khoản và cập nhật thông tin mới nhất danh sách tài khoản đang xem

#### 4/ Luồng xử lý

###### a) Màn hình danh sách tài khoản thanh toán
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Chọn chức năng "Tài khoản" | Client MB | 
Gửi yêu cầu lấy danh sách tất cả các loại tài khoản (Thanh toán, Vay, Tiết kiệm)

 | 
MB Server
 | 
Gửi yêu cầu lấy danh sách tài khoản tương ứng đến Server bank

Gọi đồng thời 3 API danh sách bao gồm:

• DS tk thanh toán (bank trả sẵn luôn Alias hoạt động của TKTT trong API này- nếu có)
• DS tk tiết kiệm
• DS tk vay
 | 
Server bank
 | 
Xử lý và trả kết quả yêu cầu lấy danh sách tài khoản cho MB Server

Sắp xếp danh sách tài khoản và phản hồi lại kết quả.

 | 
MB Server
 | 
1/ Nhận kết quả từ Server bank và trả về cho client danh sách tài khoản (bank sẽ sử lý lọc danh sách tài khoản theo HMTC, TK phong tỏa,.. rule cấu hình tại core bank trước khi trả về đầu app)

 | Client MB | 
Nhận kết quả:

•  Nếu thành công: Focus vào màn hình danh sách tài khoản thanh toán, hiển thị màn hình danh sách tài khoản (lưu danh sách tài khoản tại phiên đăng nhập)
•  Nếu không thành công, hiển thị thông báo lỗi tương ứng của hệ thống trả về.
 | 2 | Nhấn button hoặc icon mở rộng tài khoản thanh toán | Client MB | 
Hiển thị danh sách tài khoản thanh toán

Nhấn icon sao chép:

• Thực hiện sao chép tài khoản đã chọn vào bộ nhớ tạm
• Hiển thị thông báo dạng label "Đã sao chép số tài khoản thành công", tắt/ẩn sau 5 giây
Nhấn vào số tài khoản, chuyển sang màn hình chi tiết tài khoản: 

• Gửi yêu cầu lấy chi tiết tài khoản được yêu cầu 
• Hiển thị màn hình chi tiết tài khoản<Tham chiếu logic xử lý màn hình >
 | 3 | Nhấn "Tài khoản tiết kiệm" hoặc icon mở rộng | Client MB | 
Chuyển sang màn hình danh sách tài khoản tiết kiệm

<Tham chiếu logic màn hình danh sach tài khoản tiết kiệm>

 | 4 | Nhấn "Tài khoản vay" hoặc icon mở rộng | Client MB | 
Chuyển sang màn hình danh sách tài khoản vay

<Tham chiếu logic màn hình danh sach tài khoản vay>

 | 5 | Nhấn back | Client MB | Hiển thị màn hình đang thao tác trước đó.
 | 6 | 
Nhấn vào icon làm mới
 | 
Client MB
 | 
Gửi yêu cầu lấy lại danh sách loại tài khoản

###### b) Màn hình danh sách tài khoản tiết kiệm
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 
1
 | 
Nhấn button hoặc icon mở rộng tài khoản tiết kiệm
 | 
Client MB
 | 
Hiển thị danh sách tài khoản tiết kiệm

Nhấn vào số tài khoản, chuyển sang màn hình chi tiết tài khoản: 

• Gửi yêu cầu lấy chi tiết tài khoản được yêu cầu 
• Hiển thị màn hình chi tiết tài khoản<Tham chiếu logic xử lý màn hình >
 | 
2
 | 
Nhấn Back
 | 
Client MB
 | 
Hiển thị màn hình đang thao tác trước đó.

 | 
3
 | 
Nhấn Chọn 1 tài khoản tiết kiệm
 | 
Client MB
 | 
Gửi yêu cầu lấy chi tiết tài khoản được yêu cầu 

Hiển thị màn hình chi tiết tài khoản

<Tham chiếu logic xử lý màn hình >

 | 
4
 | 
Nhấn vào icon làm mới
 | 
Client MB
 | 
Gửi yêu cầu lấy lại danh sách loại tài khoản

 | 5 | Nhấn icon Thu gọn/mở rộng | Client MB | Xử lý thu gọn/mở rộng vùng hiển thị danh sách tài khoản
 | 6 | Nhấn "Tài khoản thanh toán" hoặc icon mở rộng | Client MB | 
Chuyển sang màn hình danh sách tài khoản thanh toán

<Tham chiếu logic màn hình danh sach tài khoản thanh toán>

 | 7 | Nhấn "Tài khoản vay" hoặc icon mở rộng | Client MB | 
Chuyển sang màn hình danh sách tài khoản vay

<Tham chiếu logic màn hình danh sach tài khoản vay>

###### c) Màn hình danh sách tài khoản vay
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn button hoặc icon mở rộng tài khoản vay
 | 
Client MB
 | 
Hiển thị danh sách tài khoản vay

Nhấn vào số tài khoản, chuyển sang màn hình chi tiết tài khoản: 

• Gửi yêu cầu lấy chi tiết tài khoản được yêu cầu 
• Hiển thị màn hình chi tiết tài khoản<Tham chiếu logic xử lý màn hình >
 | 
2
 | 
Nhấn Back
 | 
Client MB
 | 
Hiển thị màn hình đang thao tác trước đó.

 | 
3
 | 
Nhấn Chọn 1 tài khoản vay
 | 
Client MB
 | 
Gửi yêu cầu lấy chi tiết tài khoản được yêu cầu 

Hiển thị màn hình chi tiết tài khoản

<Tham chiếu logic xử lý màn hình >

 | 
4
 | 
Nhấn vào icon làm mới
 | 
Client MB
 | 
Gửi yêu cầu lấy lại danh sách loại tài khoản 

 | 5 | Nhấn icon Thu gọn/mở rộng | Client MB | Xử lý thu gọn/mở rộng vùng hiển thị danh sách tài khoản
 | 6 | Nhấn "Tài khoản thanh toán" hoặc icon mở rộng | Client MB | 
Chuyển sang màn hình danh sách tài khoản thanh toán

<Tham chiếu logic màn hình danh sach tài khoản thanh toán>

 | 7 | Nhấn "Tài khoản tiết kiệm" hoặc icon mở rộng | Client MB | 
Chuyển sang màn hình danh sách tài khoản tiết kiệm

<Tham chiếu logic màn hình danh sach tài khoản tiết kiệm>

---

### 15.2. MB_Tài khoản thanh toán

> **Page ID:** `29889763` · **Version:** 8
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29889763

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 | A | Vũ Thị Trang | 
 | Tạo mới tài liệu | 

 | 
 
 | M | Lê Thị Hồng | 
 | 
Cập nhật bổ sung thêm Alias và trạng thái Alias của TKTT (nếu có)
 | V3.0

##### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

•  Tác nhân tham gia: KH, Client, MB Server, Bank Server
• Điều kiện trước:
• KH đăng nhập ứng dụng thành công.
• Kết quả mong muốn:
• KH truy vấn thông tin tài khoản, lịch sử giao dịch của tài khoản thanh toán thành công.
##### 2/ Luồng màn hình MB

##### MH1: Màn hình danh sách tài khoản thanh toán

##### 

##### MH2: Màn hình thông tin tài khoản - Không có Alias (Giữ nguyên)

##### MH 3.1- MH chi tiết tài khoản thanh toán- Trạng thái Alias = Khóa (MH danh sách không hiển thị Alias nhưng MH chi tiết có hiển thị)

##### MH 3.2- MH chi tiết tài khoản thanh toán- Trạng thái Alias = Chờ hậu kiểm (MH danh sách không hiển thị Alias nhưng MH chi tiết có hiển thị)

##### MH4: Màn hình lịch sử giao dịch

##### 

##### MH5: Màn hình lịch sử giao dịch - Tìm kiếm theo ngày

##### MH6: Chi tiết giao dịch

Mô tả màn hình

###### a) Màn hình danh sách tài khoản thanh toán

Xem mô tả tại 

###### b) Màn hình Thông tin tài khoản
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
Readonly
 | 
--
 | 
--
 | 
Thông tin tài khoản thanh toán

 | 3 | 
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
Quay trở lại màn hình trang chủ

 | 4 | 
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
Quay trở lại màn hình thao tác trước đó

 | 5 | 
Tên chủ tài khoản
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị tên chủ tài khoản tương ứng

 | 6 | 
Số tài khoản
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị số tài khoản tương ứng

 | 7 | 
Tài khoản Alias
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị tài khoản Alias của TKTT- nếu có (Dữ liệu cho Bank trả về trong API chi tiết queryCurrentAcc)

 | 8 | 
Trạng thái Alias
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị trạng thái của tài khoản Alias của TKTT- nếu có (Dữ liệu cho Bank trả về trong API chi tiết queryCurrentAcc)

Các trạng thái bao gồm:

• A: Hoạt động
• P: Chờ hậu kiểm
• B: Khóa
 | 9 | 
Chi nhánh  mở
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị tên chi nhánh mở tài khoản

 | 10 | 
Số dư thực tế
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị số dư hiện tại của tài khoản

 | 11 | 
Số dư khả dụng
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị số dư khả dụng của tài khoản

 | 12 | 
Số tiền phong tỏa
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị số tiền phong tỏa tương ứng của tài khoản

 | 13 | 
Lãi cộng dồn
 | 
Label
 | 
Readonly
 | 
 --
 | 
 --
 | 

 | 14 | Lãi suất TKTT | Label | Readonly | 
 | 
 | 

 | 15 | 
Hạn mức thấu chi
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 16 | 
Lãi thấu chi
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 17 | 
Lãi suất thấu chi
 | 
Label
 | 
Readonly
 | 
 
 | 
 
 | 
 

 | 18 | 
Ngày mở tài khoản
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 19 | Đặt tài khoản thanh toán mặc định | Checkbox | Select | 
 | 
 | 
Tài khoản thanh toán mặc định là tài khoản đăng ký dịch vụ Mobile banking tại quầy → Mặc định tích vào ô checkbox của tài khoản và không cho bỏ.

Đối với các tài khoản thanh toán không phải là tài khoản mặc định, cho phép tích chọn làm tài khoản mặc đinh <Tham khảo logic xử lý chọn tài khoản mặc đinh tại màn hình Thông tin tài khoản>

 | 20 | 
Nút thao tác nhanh
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Bao gồm:

• Lịch sử giao dịch
• Chuyển tiền
• Nạp tiền điện thoại
• Thanh toán hóa đơn
• Trả nợ tiền vay. (đã chốt chức năng Trả nợ vay để phase sau)
Mặc định hiển thị 4 nút thao tác nhanh trên màn hình, cho phép khách hàng vuốt sang trái để xem thêm các nút thao tác nhanh.

Nếu nhấn vào các nút thao tác nhanh, hiển thị màn hình khởi tạo hoặc chọn loại dịch vụ con tương ứng theo chức năng.

###### d) Màn hình Lịch sử giao dịch
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | 
Label
 | 
Readonly
 | 
--
 | 
--
 | Lịch sử giao dịch
 | 2 | Nút back | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước đó

 | 3 | 
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
Quay trở lại màn hình trang chủ

 | 4 | 
Thông tin tài khoản
 | 
Label
 | 
Readonly
 | 

 | 

 | 
Hiển thị bao gồm:

• Số tài khoản 
• Số dư khả dụng
Nếu là tài khoản mặc định hiển thị thêm text "Tài khoản mặc định" sau số tài khoản:

• Số tài khoản - Tài khoản mặc định
• Số dư khả dụng
 | 5 | Icon  | Icon | Click | 
 | 
 | Logo ngân hàng Co-opBanK
 | 6 | Khoảng thời gian | Label | ReadOnly | 
 | 
 | 

 | 7 | Ghi chú | Label | ReadOnly | -- | -- | Khoảng thời gian tìm kiếm giới hạn trong vòng 03 tháng và thời gian tối đa cho phép tìm kiếm trong vòng 1 năm
 | 8 | Dữ liệu thời gian | Button | Click | -- | -- | 
Bao gồm:

• 1 tuần
• 2 tuần
• 1 tháng
• Khác
Nhấn "Khác": Hiển thị vùng tìm kiếm, cho phép chọn khoảng thời gian từ ngày, đến ngày

 | 9 | Vùng tìm kiếm từ ngày - đến ngày
 | 10 | Từ ngày | Calendar | Textbox | -- | -- | 
Chỉ cho chọn những ngày trong quá khứ đến ngày hiện tại

Từ ngày phải nhỏ hơn hoặc bằng Đến ngày

Khoảng thời gian tìm kiếm: Từ ngày... đến ngày không được quá 3 tháng

Định dạng dd/MM/yyyy

Mặc định ngày T-1 

 | 11 | Đến ngày | Calendar | Textbox | -- | -- | 
Chỉ cho chọn những ngày trong quá khứ đến ngày hiện tại

Đến ngày phải lớn hơn hoặc bằng Từ ngày

Khoảng thời gian tìm kiếm: Từ ngày... đến ngày không được quá 3 tháng

Định dạng dd/MM/yyyy

Mặc định ngày T

 | 12 | Tìm kiếm | Button | Click | -- | -- | Nhấn button Tìm kiếm sẽ ẩn/đóng vùng tìm kiếm theo ngày
 | 13 | Lịch sử | Label | Readonly | 
 | 
 | 

 | 14 | 
Tab dữ liệu
 | 
Tab
 | 
Select
 | 
--
 | 
--
 | 
Có 3 tab: Toàn bộ, Tiền vào, Tiền ra. Dữ liệu hiển thị gồm các thông tin sau:

• Thời gian giao dịch: Hiển thị thời gian tương ứng thực hiện giao dịch. Định dạng hiển thị dd/mm/yyyy hh:mm
• Nội dung giao dịch: Hiển thị cắt chuỗi trong nội dung giao dịch (Hiển thị đảm bảo trên 1 dòng dữ liệu, dữ liệu thiếu hiển thị bằng dấu “…”)
• Số tiền giao dịch: Tương ứng với số tiền thực hiện trong giao dịch. Định dạng tiền vào: màu xanh và hiển thị dấu cộng đằng trước; Định dạng tiền ra: màu đỏ và hiển thị dấu trừ đằng trước.
• Khi nhấn vào 1 giao dịch bất kì, hiển thị màn hình chi tiết giao dịch
Mặc định tại tab: Toàn bộ.

Cho phép chọn tab khác.

 | 15 | 
Danh sách giao dịch
 | 
List
 | 
View
 | 
--
 | 
--
 | 
Mặc định hiển thị danh sách giao dịch trong 1 tuần gần nhất(7 ngày gần nhất)

Hiển thị danh sách các giao dịch sắp xếp dữ liệu mới nhất lên đầu. Phân trang 10 bản ghi/ trang, cho phép KH xem dữ liệu dạng loadmore (chi tiết tham khảo logic xử lý)

Cho phép chọn lại khoảng thời gian hiển thị lịch sử giao dịch.

Trường hợp không có giao dịch nào, hiển thị label thông báo: Không có giao dịch nào gần đây

e) Màn hình Chi tiết giao dịch
 | 

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
Quay trở lại màn hình trang chủ

 | 2 | 
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
Quay trở lại màn hình lịch sử giao dịch

 | 3 | 
Mã giao dịch
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 4 | 
Ngày giao dịch
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 5 | 
Số tiền giao dịch
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 6 | 
Nội dung giao dịch
 | 
Label
 | 
Readonly
 | 

 | 

 | 

3/ Logic xử lý

###### a) Màn hình danh sách tài khoản 

Xem mô tả tại 

###### b) Màn hình thông tin tài khoản
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Lấy thông tin chi tiết tài khoản | Client MB | Gửi yêu cầu lấy thông tin chi tiết tài khoản thanh toán (API queryCurrentAcc)
 | 
MB Server
 | 
Nhận và gửi yêu cầu lấy thông tin chi tiết tài khoản thanh toán

 | 
Bank server
 | 
Xử lý và trả về kết quả, bao gồm: thông tin TKTT, Alias + trạng thái Alias của TKTT tương ứng

Các trạng thái Alias bao gồm:

• A: Hoạt động
• P: Chờ hậu kiểm
• B: Khóa
 | 
MB server
 | 
Nhận kết quả lấy thông tin tài khoản thanh toán từ Bank server

• Thành công: cập nhật trạng thái giao dịch thành công và gửi kết quả đến Client.
• · Không thành công: Trả về mã lỗi tương ứng
 | 
Client MB
 | 
Nhận kết quả:

•  Nếu không thành công, hiển thị thông báo lỗi tương ứng của hệ thống trả về:
•  Nếu thành công, hiển thị màn hình chi tiết của tài khoản thanh toán (bổ sung hiển thị Alias như đã mô tả)
 | 2 |   Bấm chọn Đặt làm tài khoản thanh toán mặc định | 
Client MB
 | 
Gửi yêu cầu xuống server đặt tài khoản đã chọn làm tài khoản thanh toán mặc định

 | 
MB Server 
 | 
Xử lý yêu cầu và trả kết quả cho client (Nếu đã có tài khoản mặc định trước đó, tài khoản mới chọn sẽ làm tài khoản mặc định thay thế tài khoản cũ)

 | 
Client MB
 | 
Nhận kết quả:

• Không thành công hiển thị thông báo lỗi tương ứng do server trả về:
• Thành công: Hiển thị ô check được chọn và không cho bỏ chọn. Hiển thị thông báo dạng popup "Quý khách đã cài đặt Tài khoản thanh toán mặc định thành công"
 | 3 | Nhấn button "Lịch sử giao dịch"    | Client MB | 
Hiển thị màn hình Lịch sử giao dịch

Gửi yêu cầu lấy lịch sử giao dịch trong 1 tuần gần nhất (7 ngày gần nhất) cho MB Server

<Tham khảo logic xử lý tại màn hình Lịch sử giao dịch>

 | 4 | Nhấn button "Chuyển tiền" | Client MB | Hiển thị màn hình chuyển tiền
 | 5 | Nhấn button "Nạp tiền điện thoại" | Client MB | Hiển thị màn hình nạp tiền điện thoại
 | 6 | Nhấn button 'Thanh toán hóa đơn' | Client MB | Hiển thị màn hình thanh toán hóa đơn
 | 7 | Nhấn button "Trả nợ tiền vay" | Client MB | Hiển thị màn hình Trả nợ tiền vay

###### d) Màn hình Lịch sử giao dịch
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Lấy lịch sử giao dịch

 | Client MB | 
Nếu nhấn button "1 tuần" → Gửi yêu cầu truy vấn 10 giao dịch trong 1 tuần gần nhất (7 ngày gần nhất)

Nếu nhấn button "2 tuần" → Gửi yêu cầu truy vấn 10 giao dịch trong 2 tuần gần nhất(14 ngày gần nhất)

Nếu nhấn button "1 tháng" → Gửi yêu cầu truy vấn 10 giao dịch trong 1 tháng gần nhất(30 ngày gần nhất)

Nếu nhấn button "Khác" → Hiển thị vùng tìm kiếm, cho chọn thời gian tìm kiếm → chuyển sang bước 2: Nhấn button "Tìm kiếm"

Mặc định hiển thị 20 giao dịch gần nhất trong khoảng thời gian là 1 tuần gần nhất.

Request gửi đi bao gồm các thông tin:

• systemID: Ứng dụng gửi tin điện
• requestId : ID tin điện
• accountNo : Số tài khoản
• fromDate : Từ ngày
• toDate : Đến ngày
• pos  = 0 (Từ bản ghi)
• limitRecord = pos + 20 (Đến bản ghi)
 | 
MB Server
 | 
Nhận và gửi yêu cầu lấy dịch sử giao dịch sang Bank server

 | 
Bank server
 | 
Nhận và xử lý lấy dữ liệu: Sắp xếp dữ liệu theo thời gian tăng dần và trả về cho MB server

 | 
MB Server
 | 
Nhận kết quả và trả về cho client.

Dữ liệu trả về cho client đảm bảo đủ các trường thông tin như đã mô tả hiển thị.

 | 
Client MB
 | 
Nhận kết quả:

• Nếu không thành công: Hiển thị thông báo lỗi tương ứng của hệ thống trả về.
• Nếu thành công: Hiển thị màn hình lịch sử giao dịch của tài khoản thanh toán như đã mô tả. 
 | 2 | Vuốt lên tại vùng lịch sử giao dịch | Client MB | 
1/ Kiểm tra giá trị totalRecord nhận tại yêu cầu lấy lịch sử 20 giao dịch gần nhất server trả về:

• Nếu limitRecord >= totalRecord  : Hiển thị dưới giao dịch cuối cùng thông báo "Đã xem hết giao dịch"
• Nếu limitRecord < totalRecord : chuyển bước 2
2/ Hiển thị icon loading, đồng thời gửi yêu cầu sang MB Server lấy 20 giao dịch tiếp theo gồm các  thông tin:

• systemID: Ứng dụng gửi tin điệ
• requestId: ID tin điện
• accountNo : Số tài khoản
• fromDate : Từ ngày
• toDate: Đến ngày
• pos = limitRecord (Giá trị từ bản ghi sẽ bằng giá trị Đến bản ghi của lần lấy lịch sử gần nhất trước đó)
• limitRecord = pos + 20
 | 
MB Server
 | 
Nhận và gửi yêu cầu lấy dịch sử giao dịch sang Bank server

 | 
Bank server
 | 
Nhận và xử lý lấy dữ liệu: Sắp xếp dữ liệu theo thời gian tăng dần và trả về cho MB server

 | 
MB Server
 | 
Nhận kết quả và trả về cho client.

Dữ liệu trả về cho client đảm bảo đủ các trường thông tin như đã mô tả hiển thị.

 | 
Client MB
 | 
Nhận kết quả:

• Nếu không thành công: Hiển thị thông báo lỗi tương ứng của hệ thống trả về.
• Nếu thành công: Hiển thị 10 giao dịch tiếp theo.
 | 3

 | Nhấn button "Tìm kiếm"

 | 
Client MB
 | 
Ẩn hoặc đóng vùng tìm kiếm cho chọn thời gian tìm kiếm vừa hiển thị.

Kiểm tra validate:

• Nếu không hợp lệ: Hiển thị thông báo lỗi: | Case | Tác nhân | Nội dung thông báo | Ghi chú
 | Từ ngày lớn hơn Đến ngày | Client MB | Khoảng thời gian tìm kiếm không hợp lệ. Quý khách vui lòng kiểm tra lại! | 

 | 
Khoảng thời gian lớn hơn 03 tháng
 | 
Client MB
 | 
Quý khách vui lòng nhập khoảng thời gian nhỏ hơn 03 tháng!
 | 

• Nếu hợp lệ: Gửi yêu cầu tìm kiếm lịch sử giao dịch sang MB server
 | MB server | Nhận và gửi yêu cầu sang Bank server
 | Bank server | 
Nhận và xử lý lấy dữ liệu: Sắp xếp dữ liệu theo thời gian tăng dần và trả về cho MB server

 | MB server | Nhận thông tin và trả kết quả cho client
 | Client MB | 
Nhận kết quả:

• Nếu thành công:  Hiển thị dữ liệu như màn hình mô tả. Nếu không có dữ liệu, hiển thị thống báo "Khồng tồn tại giao dịch trong khoảng thời gian yêu cầu!"
• Nếu không thành công: Hiển thị thông báo lỗi tương ứng mã lỗi trả về
 | 4 | Nhấn vào 1 giao dịch | Client MB | 
Hiển thị màn hình Chi tiết giao dịch

Gửi yêu cầu lấy chi tiết giao dịch theo mã giao dịch

<Tham khảo logic tại màn hình Chi tiết giao dịch>

###### e) Màn hình Chi tiết giao dịch
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Lấy thông tin chi tiết giao dịch | Client MB | Gửi yêu cầu lấy chi tiết giao dịch theo mã giao dịch
 | MB server | Nhận và gửi yêu cầu sang Bank server
 | Bank server | Nhận và xử lý yêu cầu, lấy dữ liệu trả về cho MB server
 | MB server | Nhận thông tin trả về và gửi lại cho client
 | Client MB | 
Nhận kết quả:

• Thành công: Hiển thị dữ liệu như mô tả
• Không thành công: Hiển thị thông báo lỗi tương ứng mã lỗi nhận được

---

### 15.3. MB_Tài khoản tiết kiệm

> **Page ID:** `29890482` · **Version:** 31
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29890482

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 

 | A | 
 | 
 | 
Tạo mới tài liệu 
 | V.1.0.0
 | 
23/12/2022
 | M | TuanVN1 | 
 | 
MH Tài khoản tiết kiệm bổ sung chức năng Tất toán tiền gửi trực tuyến, Rút gốc một phần, Giấy xác nhận.

Hiển thị thêm thông tin: Loại sản phẩm, Phương thức đáo hạn, Tài khoản nhận gốc lãi
 | V1.1.0
 | 
17/03/2023
 | M | TuanVN1 | 
 | 
MH danh sách tài khoản tiết kiệm, bổ sung Ngày hiệu lực
 | V1.1.1
 | 
 
 | M | NhungNTH8 | 
 | 
Bổ sung thông tin xem chi tiết tài khoản ( cập nhật tiền gửi tích lũy )
 | 

 | 
 
 | M | HongLT | 
 | 
MH xem chi tiết TKTK tích lũy linh động → Đổi tên trường Lãi suất thành Lãi suất của kỳ hạn gốc (Do bank thay đổi công thức tính lãi của gửi gốc thêm)
 | 

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client, MB Server, Bank Server
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công.
• Kết quả mong muốn:
• KH xem chi tiết tài khoản tiết kiệm, lịch sử giao dịch tài khoản tiết kiệm thành công.
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

##### MH1: Màn hình danh sách tài khoản tiết kiệm

##### MH2: Thông tin tài khoản tiết kiệm ( Tiền gửi thường )

MH2.1: Thông tin tài khoản ( TH Tích lũy linh động ) → Đổi tên trường Lãi suất = Lãi suất của kỳ hạn gốc

MH:2.2: Thông tin tài khoản ( TH Tích lũy tự động )

##### MH3: Màn hình Lịch sử giao dịch

##### MH4: Màn hình lịch sử giao dịch - Tìm kiếm theo ngày

##### MH5: Chi tiết giao dịch

#### Mô tả màn hình:

###### a) Màn hình danh sách tài khoản tiết kiệm

Xem mô tả tại 

###### b) Màn hình Thông tin tài khoản tiết kiệm
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

 | 1 | Tiêu đề  | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Thông tin tài khoản
 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | Icon Home | Icon | Click | -- | -- | Quay về màn hình trang chủ
 | 4 | 
Tên chủ tài khoản
 | 
Label
 | 
ReadOnly
 | -- | -- | 
accountName

 | 5 | Số tài khoản Tiền gửi | Label | ReadOnly | -- | -- | 
accountType

- Y: tài khoản có kỳ hạn
- S: tài khoản không kỳ hạn

 | 6 | Chi nhánh/PGD mở | Label | ReadOnly | -- | -- | branchName
 | 7 | 
Số sổ
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiện thị đối với tài khoản Tiền gửi tại quầy (nếu có)

Hiển thị số sổ tiết kiệm do bank server trả về

passbook_no

 | 8 | Loại sản phẩm | Label | 
ReadOnly
 | -- | -- | 
productName

 | 
9
 | Kỳ hạn | Label | ReadOnly | -- | -- | termdesc
 | 
10
 | Ngày mở ban đầu | Label | ReadOnly | -- | -- | accOpenDate
 | 11 | Ngày hiệu lực | Label | ReadOnly | -- | -- | 
effectiveDate

 | 12 | Ngày đáo hạn  | Label | ReadOnly | -- | -- | 
marturityDate

 | 13 | Số tiền gốc ban đầu | Label | ReadOnly | -- | -- | 
balance

 | 12 | Số dư gốc hiện tại | Label | ReadOnly | -- | -- | availBalance
 | 14 | Số tiền phong tỏa | 
Label
 | 
ReadOnly
 | -- | -- | 
amountBlock

 | 15 | 
Lãi suất

Với Tài khoản tiết kiệm tích lũy linh động → Hiển thị tên trường = Lãi suất của kỳ hạn gốc
 | 
Label
 | 
ReadOnly
 | -- | -- | 
interestRate 

 | 16 | Lãi cộng dồn | Label | ReadOnly | -- | -- | accrued_cr
 | 17 | Số tiền lãi đã lĩnh | Label | ReadOnly | -- | -- | Chỉ hiển thị đối với loại sản phẩm lĩnh lãi định kỳ và số tiền lãi đã lĩnh  > 0 (liqd_amt)

 | 18 | Hình thức tích lũy | Label | ReadOnly | -- | -- | 
rdType:

- 0: Tích lũy linh động
- 1: Tích lũy theo chu kỳ

( Chỉ hiển thị với loại sản phẩm Tiền gửi tích lũy)

 | 18.1 | Chu kỳ tích lũy | Label | ReadOnly | -- | -- | 
rdFrequency

(Hiển thị nếu hình thức tích lũy là tích lũy định kỳ tự động)

 | 18.2 | Ngày tích lũy tiếp theo | Label | ReadOnly | -- | -- | 
rdNextSche

( Hiển thị ngày tích lũy kỳ tiếp theo nếu hình thức tích lũy là tích lũy định kỳ tự động )

 | 18.3 | Số tiền tích lũy định kỳ | Label | ReadOnly | -- | -- | 
rdAmount

(Hiển thị nếu hình thức tích lũy là tích lũy định kỳ tự động)

 | 18.4 | Tài khoản trích tiền | Label | ReadOnly | -- | -- | 
rdPaymentAcount

(Hiển thị nếu hình thức tích lũy là tích lũy định kỳ tự động)

 | 18.5 | Trạng thái tích lũy | Label | ReadOnly | -- | -- | 
rdScheStatus

(Hiển thị nếu hình thức tích lũy là tích lũy định kỳ tự động)

 | 19 | Phương thức đáo hạn | Label | ReadOnly | -- | -- | 
Hiển thị phương thức đáo hạn (setType)

• setType = 0, fix tại client "Chuyển gốc và lãi sang kỳ hạn mới"
• setType = 1, fix tại client "Gốc sang kỳ hạn mới, nhận lãi về TKTT"
• setType = 2, fix tại client "Tự động tất toán, nhận gốc và lãi về TKTT"
 | 19 | Phương thức tất toán/rút gốc | 
Label
 | ReadOnly | -- | -- | 
tellerStatus

Hiển thị phương thức tất toán/ rút gốc tương ứng KH đã chọn tại thời điểm mới nhất

 | 20 | Tài khoản nhận gốc lãi | Label | ReadOnly | -- | -- | 
Hiển thị tài khoản nhận gốc lãi (reciprocalAccount)

nếu phương thức đáo hạn setType = 0 (Chuyển gốc và lãi sang kỳ hạn mới) thì ẩn Tài khoản nhận gốc lãi

 | 21 | Tất toán tiền gửi trực tuyến | Label | ReadOnly | -- | -- | 
Chỉ hiển thị với tài khoản Tiền gửi trực tuyến 

Kiểm tra nếu Bank đang chạy batch thì HT chặn ngay sau khi click

Nếu bank không chạy batch thì điều hướng sang màn hình chức năng Tất toán tiền gửi trực tuyến

Điều kiện Server lọc hiển thị nút chức năng < Tham khảo logic xử lý >
Trường hợp | 
Cấu hình tại BE 

(chỉ check với những chức năng có phát sinh GD tài chính
 | Đặc tính sản phẩm | Trường hợp | Trạng thái GD | Hình Thức tích lũy | Hiện thị chức năng
 | 

Có cấu hình các chức năng

• Tất toán tiền gửi
• Rút gốc 1 phần
• Gửi gốc thêm
(cấu hình thiếu chức năng nào thì chức năng đó không hiển thị trên app)
 | 
Tích lũy

(productType=4)

 | 
Mở tại app

(passbook_no = Null)

 | 
GD tại app(tellerStatus=1)

 
 | 
Linh động

(rdType = 0)
 | 
Tất toán tiền gửi

 | 
Tự  động (rdType = 1)
 | 
Tất toán tiền gửi

 | 
Thường

(productType ≠4)
 | 
Mở tại app

(passbook_no = Null)

 | 
GD tại app

(tellerStatus=1)
 | 

 | 
Tất toán tiền gửi

=> Kết quả Server trả về client hiển thị ( usedFor=CTA)

 | 22 | Thay đổi thông tin tích lũy định kỳ | icon | Click | -- | -- | 
Click → chuyển sang màn hình Thay đổi thông tin tích lũy định kỳ

Chỉ hiển thị với Tài khoản mở trực tuyến có Hình thức tích lũy 

Điều kiện Server lọc hiển thị nút chức năng < Tham khảo logic xử lý >
Trường hợp | Đặc tính sản phẩm | Trường hợp | Trạng thái GD | Hình Thức tích lũy | Hiện thị chức năng
 | 
Tích lũy

(productType=4)

 | 
Mở tại quầy

(passbook_no ≠ Null)

 | GD tại quầy(tellerStatus=0) | 
Tự động

( rdType =1 )
 | 
Thay đổi thông tin tích lũy định kỳ

• Thay đổi trạng thái
 | 
Mở tại app

(passbook_no = Null)

 | GD tại quầy(tellerStatus=0)

 | 
Tự động

(rdType=1)
 | 
Thay đổi thông tin tích lũy định kỳ

• Thay đổi trạng thái
• Thay đổi số tiền
• Thay đổi tài khoản trích tiền
 | 
GD tại app

(tellerStatus=1)
 | 
Tự động

(rdType=1)
 | 
Thay đổi thông tin tích lũy định kỳ

• Thay đổi trạng thái
• Thay đổi số tiền
• Thay đổi tài khoản trích tiền

=> Kết quả Server trả về client hiển thị ( usedFor=CAI)

 | 22.1 | Gửi gốc thêm  | icon | click | -- | -- | 
Click → Chuyển sang màn hình  Gửi gốc thêm tiền

Chỉ hiển thị với tích lũy linh động 

Điều kiện Server lọc hiển thị nút chức năng < Tham khảo logic xử lý >
Trường hợp | 
Cấu hình tại BE 

(chỉ check với những chức năng có phát sinh GD tài chính
 | Đặc tính sản phẩm | Trường hợp | Trạng thái GD | Hình Thức tích lũy | Hiện thị chức năng
 | 
Có cấu hình các chức năng

• Tất toán tiền gửi
• Rút gốc 1 phần
• Gửi gốc thêm
(cấu hình thiếu chức năng nào thì chức năng đó không hiển thị trên app)
 | 
Tích lũy

(productType=4)
 | 
Mở tại app

(passbook_no = Null)

 | GD tại quầy(tellerStatus=0)

 | 
Linh  động

(rdType=0)
 | 
Gửi gốc thêm

 | 
GD tại app

(tellerStatus=1)
 | 
Linh động

(rdType=0)
 | 
Gửi gốc thêm

=> Kết quả Server trả về client hiển thị ( usedFor=SPA)

 

 | 20 | Rút gốc một phần | Icon | Click | -- | -- | 
Chỉ hiển thị với tài khoản Tiền gửi trực tuyến ( Hiển thị với Tiền gửi thường) được phép rút gốc một phần

Kiểm tra nếu Bank đang chạy batch thì HT chặn ngay sau khi click

Nếu bank không chạy batch thì điều hướng sang màn hình chức năng Rút gốc một phần

Điều kiện Server lọc hiển thị nút chức năng < Tham khảo logic xử lý >
Trường hợp | 
Cấu hình tại BE

 (chỉ check với những chức năng có phát sinh GD tài chính)
 | Đặc tính sản phẩm | Trường hợp | Trạng thái GD | Hiện thị chức năng
 | 
Có cấu hình các chức năng

• Tất toán tiền gửi
• Rút gốc 1 phần
• Gửi gốc thêm
(cấu hình thiếu chức năng nào thì chức năng đó không hiển thị trên app)
 | 
Thường

(productType ≠4)
 | 
Mở tại app

(passbook_no = Null)

 | 
GD tại app

(tellerStatus=1)
 | 
Rút gốc 1 phần

=> Kết quả Server trả về client hiển thị ( usedFor=SPW)

 | 23 | Lịch sử giao dịch  | Icon | Click | -- | -- | 
Điều hướng sang màn hình chức năng Lịch sử giao dịch <luồng xử lý chi tiết>

 | 24 | Chức năng khác | Icon | Click | -- | -- | 
Click → Hiển thị popup chức năng khác bao gồm:

• Giấy xác nhận
• Thay đổi phương thức tất toán/rút gốc

###### c) Màn hình Lịch sử giao dịch
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

 | 1 | Tiêu đề | 
Label
 | 
Readonly
 | 
--
 | 
--
 | Lịch sử giao dịch
 | 2 | Nút back | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước đó

 | 3 | 
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
Quay trở lại màn hình trang chủ

 | 4 | 
Thông tin tài khoản
 | 
Label
 | 
Readonly
 | 

 | 

 | 
Icon logo ngân hàng Co-opBank

Hiển thị bao gồm:

• Tài khoản tiết kiệm
• Số dư gốc hiện tại
 | 5 | Khoảng thời gian | Label | ReadOnly | 
 | 
 | 

 | 6 | Ghi chú | Label | ReadOnly | -- | -- | Khoảng thời gian tìm kiếm giới hạn trong vòng 1 năm
 | 7 | 1 tháng | Button | Click | -- | -- | 

 | 8 | 6 tháng | Button | Click | -- | -- | 

 | 9 | 1 năm | Button | Click | -- | -- | 

 | 11 | Vùng tìm kiếm Từ ngày... đến ngày
 | 12 | Từ ngày | Calendar | Textbox | -- | -- | 
Chỉ cho chọn những ngày trong quá khứ đến ngày hiện tại

Từ ngày phải nhỏ hơn hoặc bằng Đến ngày

Khoảng thời gian tìm kiếm: Từ ngày... đến ngày không được quá 3 tháng

Định dạng dd/MM/yyyy

Mặc định ngày T-1 

 | 13 | Đến ngày | Calendar | Textbox | -- | -- | 
Chỉ cho chọn những ngày trong quá khứ đến ngày hiện tại

Đến ngày phải lớn hơn hoặc bằng Từ ngày

Khoảng thời gian tìm kiếm: Từ ngày... đến ngày không được quá 3 tháng

Định dạng dd/MM/yyyy

Mặc định ngày T

 | 14 | Tìm kiếm | Button | Click | -- | - | 

 | 15 | Lịch sử | Label | Readonly | 
 | 
 | 

 | 16 | 
Tab dữ liệu
 | 
Tab
 | 
Select
 | 
--
 | 
--
 | 
Có 3 tab: Toàn bộ, Tiền vào, Tiền ra. Dữ liệu hiển thị gồm các thông tin sau:

• Thời gian giao dịch: Hiển thị thời gian tương ứng thực hiện giao dịch. Định dạng hiển thị dd/mm/yyyy hh:mm
• Nội dung giao dịch: Hiển thị cắt chuỗi trong nội dung giao dịch (Hiển thị đảm bảo trên 1 dòng dữ liệu, dữ liệu thiếu hiển thị bằng dấu “…”)
• Số tiền giao dịch: Tương ứng với số tiền thực hiện trong giao dịch. Định dạng tiền vào: màu xanh và hiển thị dấu cộng đằng trước; Định dạng tiền ra: màu đỏ và hiển thị dấu trừ đằng trước.
• Khi nhấn vào 1 giao dịch bất kì, hiển thị màn hình chi tiết giao dịch
Mặc định tại tab: Toàn bộ.

Cho phép chọn tab khác.

 | 17 | 
Danh sách giao dịch
 | 
List
 | 
View
 | 
--
 | 
--
 | 
Mặc định hiển thị danh sách giao dịch trong 1 tháng gần nhất 

Hiển thị danh sách các giao dịch sắp xếp dữ liệu mới nhất lên đầu. Phân trang 10 bản ghi/ trang, cho phép KH xem dữ liệu dạng loadmore (chi tiết tham khảo logic xử lý)

Cho phép chọn lại khoản thời gian hiển thị lịch sử giao dịch.

Trường hợp không có giao dịch nào, hiển thị label thông báo: Không có giao dịch nào gần đây

###### d) Màn hình Chi tiết giao dịch
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

 | 
2
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
Quay trở lại màn hình trang chủ

 | 
3
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
Quay trở lại màn hình lịch sử giao dịch

 | 
4
 | 
Mã giao dịch
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị thông tin mã giao dịch

 | 
5
 | 
Ngày giao dịch
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị theo định dạng dd/mm/yyyy hh:mm

 | 
6
 | 
Số tiền giao dịch
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
transAmount 

 | 
7
 | 
Nội dung giao dịch
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
transRemark

#### 4/ Luồng xử lý

###### a) Màn hình danh sách tài khoản tiết kiệm

Xem mô tả tại 

###### b) Màn hình Thông tin tài khoản tiết kiệm
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Lấy thông tin tài khoản

 | Client MB | Gửi yêu cầu lấy thông tin chi tiết tài khoản tiết kiệm sang MB server
 | 
MB Server
 | 
Nhận và gửi yêu cầu lấy thông tin chi tiết tài khoản tiết kiệm sang Bank server 

 | 
Bank server
 | 
Xử lý và trả về kết quả yêu cầu chi tiết tài khoản đến MB Server

 | 
MB Server
 | 
Nhận kết quả từ Bank server:

• Thành công: cập nhật trạng thái thành công và trả kết quả về cho client gồm các thông tin như mô tả màn hình
• Không thành công: Trả về mã lỗi tương ứng
 | Client MB | 
Nhận kết quả:

• Nếu không thành công, hiển thị thông báo lỗi tương ứng của hệ thống trả về
• Nếu thành công, hiển thị màn hình chi tiết của Tài khoản tiết kiệm” như mô tả: | 
Label trả về cho client hiển thị
 | 
Giá trị API bank trả về
 | 
Mô tả

 | Tên chủ tài khoản | 
 | 

 | Số tài khoản | 
 | 

 | Chi nhánh mở | 
 | 

 | Số sổ | 
 | 

 | Lãi suất | 
 | 

 | Kỳ hạn | 
 | 

 | Ngày mở | 
 | Định dạng dd/mm/yyyy
 | Ngày đến hạn | 
 | Định dạng dd/mm/yyyy
 | Số dư gốc hiện tại | 
 | 
Định dạng xxx,xxx VND

 | Số tiền phong tỏa | 
 | 
Định dạng xxx,xxx VND

 | Lãi cộng dồn | 
 | 
Định dạng xxx,xxx VND

 | 
Phương thức đáo hạn
 | 
 | 

 | 
Tài khoản nhận gốc lãi
 | 
 | 

 | 2 | Nhấn lấy "Lịch sử giao dịch" | Client MB | 
Hiển thị màn hình Lịch sử giao dịch

Gửi yêu cầu lấy danh sách giao dịch trong 1 tháng gần nhất  cho MB Server

<Tham khảo logic xử lý tại màn hình Lịch sử giao dịch>

 | 3 | Nhấn Tất toán tiền gửi trực tuyến | Client MB | 
Điều hướng sang màn hình chức năng Tất toán tiền gửi trực tuyến

Kiểm tra nếu Bank đang chạy batch thì HT chặn ngay sau khi click vào button

 | 4 | Nhấn Rút gốc một phần | Client MB | 
Điều hướng sang màn hình chức năng Rút gốc một phần

Kiểm tra nếu Bank đang chạy batch thì HT chặn ngay sau khi click vào button

 | 5 | Nhấn Giấy xác nhận | Client MB | 
HIển thị màn hình show file PDF theo hỗ trợ của thiết bị 

Cho phép KH thực hiện tải file PDF về thiết bị theo hỗ trợ của trình duyệt.

###### c) Màn hình Lịch sử giao dịch
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Lấy lịch sử giao dịch

 | Client MB | 
Nếu nhấn button "1 tháng" → Gửi yêu cầu lấy lịch sử giao dịch trong 1 tháng gần nhất (30 ngày gần nhất)

Nếu nhấn button "6 tháng" → Gửi yêu cầu lấy lịch sử giao dịch trong 6 tháng gần nhất (180 ngày gần nhất)

Nếu nhấn button "1 năm" → Gửi yêu cầu lấy lịch sử giao dịch trong 1 năm gần nhất (365 ngày gần nhất)

Nếu nhấn button "Khác" → Hiển thị vùng tìm kiếm, 

> ⚠️ *Nội dung đã cắt ngắn (18945 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 15.4. MB_Tài khoản vay

> **Page ID:** `29890492` · **Version:** 52
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29890492

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 | A | Vũ Thị Trang | 
 | Tạo mới tài liệu | 

 | 
 
 | M | Lê Thị Hồng | 
 | 
Lịch sử giao dịch:

• Thay đổi khoảng thời gian tìm kiếm: 1 tháng, 2 tháng, 3 tháng
• Mặc định hiển thị dữ liệu 1 tháng gần nhất
• Sửa label mô tả tại mục Lịch sử giao dịch ""
Thông tin tài khoản

Đổi text icon Trả nợ vay = Tạo lệnh thanh toán khoản vay chính chủ
 | V2.0
 | 
 
 | M | Lê Thị Hồng | 
 | 
Đổi text Tổng lãi cộng dồn = Lãi đến ngày hiện tại
 | 

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client, MB Server, Bank Server
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công
• Kết quả mong muốn:
• KH xem chi tiết tài khoản vay, lịch sử giao dịch tài khoản vay thành công.
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

##### MH1: Màn hình danh sách tài khoản vay

##### MH2: Màn hình thông tin tài khoản vay

##### MH3: Màn hình lịch sử giao dịch

##### MH4: Màn hình lịch sử giao dịch - Tìm kiếm theo ngày

##### MH5: Màn hình Thông tin giao dịch

#### Mô tả màn hình:

###### a) Màn hình danh sách tài khoản vay

Xem mô tả lại 

###### b) Màn hình Thông tin tài khoản vay
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

 | 
1
 | 
Tiêu đề màn hinh
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Thông tin tài khoản

 | 2 | 
Tài khoản vay
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 
3
 | 
Nút “Back”
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn nút này, tắt màn hình và hiển thị màn hình đang thao tác trước đó.

 | 
4
 | 
Icon Home
 | 
Icon
 | 
CLick
 | 
--
 | 
--
 | 
Hiển thị màn hình trang chủ

 | 
5
 | 
Tên chủ tài khoản
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị tên chủ tài khoản tương ứng

 | 6 | 
Chi nhánh mở
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị tên chi nhánh mở  tài khoản vay

 | 7 | 
Số tài khoản
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị số tài khoản tương ứng

 | 8 | 
Số Hợp đồng
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị số hợp đồng vay do bank server trả về

 | 9 | 
Lãi suất
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
 

 | 10 | 
Lãi suất quá hạn
 | 

 | 

 | 

 | 

 | 

 | 11 | 
 Loại khoản vay
 | 
Label
 | 
Readonly
 | 

 | 

 | 
(sản phẩm vay)

 | 12 | 
Ngày giải ngân
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 13 | 
Ngày đáo hạn
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 14 | 
Số tiền đã giải ngân
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 15 | 
Tổng dư nợ gốc hiện tại
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 16 | 
Dư nợ trong hạn
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 
17
 | 
Dư nợ quá hạn
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 
18
 | 
Tổng lãi cộng dồn
 | 
Label
 | 
Readonly
 | 

 | 

 | 
Đổi tên trường Tổng lãi cộng dồn = Lãi đến ngày hiện tại

 | 19 | Lãi phạt trên lãi chậm trả | Label | Readonly | 
 | 
 | 

 | 20 | Ngày trả nợ gốc tiếp theo | Label | Readonly | 
 | 
 | Ngày trả nợ gốc tiếp theo
 | 21 | Ngày trả nợ lãi tiếp theo | Label | Readonly | 
 | 
 | Ngày trả nợ lãi tiếp theo
 | 22 | 
Nút thao tác nhanh
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Bao gồm:

• Lịch sử giao dịch
• Tạo lệnh trả nợ vay chính chủ
Nếu nhấn vào các nút thao tác nhanh, hiển thị màn hình khởi tạo tương ứng của chức năng với tài khoản nguồn là tài khoản đang truy vấn.

###### c) Màn hình Lịch sử giao dịch
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

 | 1 | Tiêu đề | 
Label
 | 
Readonly
 | 
--
 | 
--
 | Lịch sử giao dịch
 | 2 | Nút back | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước đó

 | 3 | 
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
Quay trở lại màn hình trang chủ

 | 4 | 
Thông tin tài khoản
 | 
Label
 | 
Readonly
 | 

 | 

 | 
Icon - Logo ngân hàng Co-opBank

Hiển thị bao gồm:

• Tài khoản vay
• Số dư nợ gốc
 | 5 | Khoảng thời gian | Label | ReadOnly | 
 | 
 | 

 | 6 | Ghi chú | Label | ReadOnly | -- | -- | Khoảng thời gian tìm kiếm giới hạn trong vòng 1 năm
 | 7 | 1 tháng | Button | Click | -- | -- | 

 | 8 | 2 tháng | Button | Click | -- | -- | 

 | 9 | 3 tháng | Button | Click | -- | -- | 

 | 10 | Khác | Button | Click | 
 | 
 | Nhấn vào button khác sẽ hiện ra vùng tìm kiếm, cho phép chọn từ ngày ... đến ngày muốn tìm kiếm
 | 11 | Vùng tìm kiếm Từ ngày... đến ngày
 | 12 | Từ ngày | Calendar | Textbox | -- | -- | 
Chỉ cho chọn những ngày trong quá khứ đến ngày hiện tại

Từ ngày phải nhỏ hơn hoặc bằng Đến ngày

Khoảng thời gian tìm kiếm: Từ ngày... đến ngày không được quá 1 năm

Định dạng dd/MM/yyyy

Mặc định ngày T-1 

 | 13 | Đến ngày | Calendar | Textbox | -- | -- | 
Chỉ cho chọn những ngày trong quá khứ đến ngày hiện tại

Đến ngày phải lớn hơn hoặc bằng Từ ngày

Khoảng thời gian tìm kiếm: Từ ngày... đến ngày không được quá 1 năm

Định dạng dd/MM/yyyy

Mặc định ngày T

 | 14 | Tìm kiếm | Button | Click | -- | - | 

 | 15 | Lịch sử | Label | Readonly | 
 | 
 | 

 | 16 | 
Tab dữ liệu
 | 
Tab
 | 
Select
 | 
--
 | 
--
 | 
Gồm các thông tin hiển thị như sau:

• Thời gian giao dịch: Hiển thị thời gian tương ứng thực hiện giao dịch. Định dạng hiển thị dd/mm/yyyy hh:mm
• Nội dung giao dịch: Hiển thị cắt chuỗi trong nội dung giao dịch (Hiển thị đảm bảo trên 1 dòng dữ liệu, dữ liệu thiếu hiển thị bằng dấu “…”)
• Số tiền giao dịch: tổng số tiền đã trả (đối với giao dịch trả nợ gốc lãi)/ số tiền giải ngân (đối với giao dịch giải ngân)
 | 17 | 
Danh sách giao dịch
 | 
List
 | 
View
 | 
--
 | 
--
 | 
Mặc định hiển thị danh sách giao dịch trong 1 tháng gần nhất (30 ngày gần nhất).

Hiển thị danh sách các giao dịch sắp xếp dữ liệu mới nhất lên đầu. Phân trang 10 bản ghi/ trang, cho phép KH xem dữ liệu dạng loadmore (chi tiết tham khảo logic xử lý)

Cho phép chọn lại khoản thời gian hiển thị lịch sử giao dịch.

Trường hợp không có giao dịch nào, hiển thị label thông báo: Không có giao dịch nào gần đây

###### d) Màn hình Chi tiết giao dịch
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

 | 
2
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
Quay trở lại màn hình trang chủ

 | 
3
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
Quay trở lại màn hình lịch sử giao dịch

 | 
4
 | 
Mã giao dịch
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 
5
 | 
Ngày giao dịch
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 
6
 | 
Số tiền gốc
 | 
Label
 | 
Readonly
 | 

 | 

 | 

 | 7 | Số tiền lãi | Label | Readonly | 
 | 
 | Bao gồm cả lãi vay và lãi phạt
 | 8 | Nội dung giao dịch | Label | Readonly | 
 | 
 | 

#### 4/ Luồng xử lý

###### a) Màn hình danh sách tài khoản vay

Xem mô tả tại 

###### b) Màn hình Thông tin tài khoản vay
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Lấy thông tin chi tiết tài khoản vay

 | Client MB | Gửi yêu cầu lấy chi tiết tài khoản vay đến MB server
 | 
MB Server
 | 
Nhận và gửi yêu cầu lấy chi tiết tài khoản vay đến bank server

 | 
Bank server
 | 
Xử lý và trả về kết quả yêu cầu lấy thông tin chi tiết tài khoản vay 

 | 
MB Server
 | 
Nhận kết quả từ Bank server

• Thành công: cập nhật trạng thái thành công và trả kết quả về cho client gồm các thông tin như mô tả màn hình
• Không thành công: cập nhật trạng thái lỗi tương ứng và trả mô tả lỗi tương ứng về cho client
 | 
Client MB
 | 
Nhận kết quả:

• Nếu không thành công, hiển thị thông báo lỗi tương ứng của hệ thống trả về.
• Nếu thành công, hiển thị màn hình chi tiết của tài khoản vay như mô tả: | 
Label trả về cho client hiển thị
 | 
Giá trị API Bank trả về
 | 
Mô tả

 | 
Chủ tài khoản
 | 

 | 

 | 
Số tài khoản
 | 

 | 

 | Chi nhánh mở | 
 | 

 | Số hợp đồng | 
 | 

 | Lãi suất vay | 
 | 

 | Lãi suất quá hạn | 
 | 

 | Loại khoản vay | 
 | 

 | Ngày giải ngân | 
 | Định dạng dd/mm/yyyy
 | Ngày đáo hạn | 
 | Định dạng dd/mm/yyyy
 | Số tiền đã giải ngân | 
 | 
Định dạng xxx, xxx VND

 | Tổng dư nợ gốc hiện tại | 
 | 
Định dạng xxx, xxx VND

 | Dư nợ trong hạn | 
 | 
Định dạng xxx, xxx VND

 | Dư nợ quá hạn | 
 | 
Định dạng xxx, xxx VND

 | Tổng lãi cộng dồn | 
 | 
Định dạng xxx, xxx VND

 | Lãi phạt | 
 | 
Định dạng xxx, xxx VND

 | Ngày trả nợ gốc tiếp theo | 
 | Định dạng dd/mm/yyyy
 | 
Ngày trả nợ lãi tiếp theo
 | 

 | 
Định dạng dd/mm/yy

 | 2 | Nhấn lấy "Lịch sử giao dịch" | Client MB | 
Hiển thị màn hình Lịch sử giao dịch

Gửi yêu cầu lấy lịch sử giao dịch trong 1 tháng gần nhất (30 ngày gần nhất) cho MB Server

<Tham khảo logic xử lý tại màn hình Lịch sử giao dịch>

 | 3 | Nhấn "Tạo lệnh trả nợ vay chính chủ" | Client MB | Hiển thị màn hình chức năng "Tạo lệnh trả nợ vay chính chủ"

###### c) Màn hình Lịch sử giao dịch
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Lấy lịch sử giao dịch

 | Client MB | 
Nếu nhấn button "1 tháng" → Gửi yêu cầu lấy lịch sử giao dịch trong 1 tháng gần nhất (30 ngày gần nhất)

Nếu nhấn button "2 tháng" → Gửi yêu cầu lấy lịch sử giao dịch trong 2 tháng gần nhất (60 ngày gần nhất)

Nếu nhấn button "3 tháng" → Gửi yêu cầu lấy lịch sử giao dịch trong 3 tháng gần nhất (90 ngày gần nhất)

Nếu nhấn button "Khác" → Hiển thị vùng tìm kiếm, cho chọn thời gian tìm kiếm → chuyển sang bước 2: Nhấn button "Tìm kiếm"

Mặc định hiển thị lịch sử giao dịch trong 1 tháng gần nhất.

Request gửi đi bao gồm các thông tin:

• systemID: Ứng dụng gửi tin điện
• requestId : ID tin điện
• accountNo : Số tài khoản
• fromDate : Từ ngày
• toDate : Đến ngày
• pos  = 0 (Từ bản ghi)
• limitRecord = pos + 10 (Đến bản ghi)
 | 
MB Server
 | 
Nhân và gửi yêu cầu lấy dịch sử giao dịch sang Bank server

 | 
Bank server
 | 
Nhận và xử lý lấy dữ liệu: Sắp xếp dữ liệu theo thời gian tăng dần và trả về cho MB server

 | 
MB Server
 | 
Nhận kết quả và trả về cho client.

Dữ liệu trả về cho client đảm bảo đủ các trường thông tin như đã mô tả hiển thị.

 | 
Client MB
 | 
Nhận kết quả:

• Nếu không thành công: Hiển thị thông báo lỗi tương ứng của hệ thống trả về.
• Nếu thành công: Hiển thị màn hình lịch sử giao dịch của tài khoản thanh toán như đã mô tả
 | 2 | Vuốt lên tại vùng lịch sử giao dịch | Client MB | 
1/ Kiểm tra giá trị totalRecord nhận tại yêu cầu lấy lịch sử 10 giao dịch gần nhất server trả về:

• Nếu limitRecord >= totalRecord  : Hiển thị dưới giao dịch cuối cùng thông báo "Đã xem hết giao dịch"
• Nếu limitRecord < totalRecord : chuyển bước 2
2/ Hiển thị icon loading, đồng thời gửi yêu cầu sang MB Server lấy 10 giao dịch tiếp theo gồm các  thông tin:

• systemID: Ứng dụng gửi tin điệ
• requestId: ID tin điện
• accountNo : Số tài khoản
• fromDate : Từ ngày
• toDate: Đến ngày
• pos = limitRecord (Giá trị từ bản ghi sẽ bằng giá trị Đến bản ghi của lần lấy lịch sử gần nhất trước đó)
• limitRecord = pos + 10
 | 
MB Server
 | 
Nhận và gửi yêu cầu lấy dịch sử giao dịch sang Bank server

 | 
Bank server
 | 
Nhận và xử lý lấy dữ liệu: Sắp xếp dữ liệu theo thời gian tăng dần và trả về cho MB server

 | 
MB Server
 | 
Nhận kết quả và trả về cho client.

Dữ liệu trả về cho client đảm bảo đủ các trường thông tin như đã mô tả hiển thị.

 | 
Client MB
 | 
Nhận kết quả:

• Nếu không thành công: Hiển thị thông báo lỗi tương ứng của hệ thống trả về.
• Nếu thành công: Hiển thị 10 giao dịch tiếp theo.
 | 2

 | Nhấn button "Tìm kiếm"

 | 
Client MB
 | 
Ẩn hoặc đóng vùng tìm kiếm, cho chọn thời gian tìm kiếm vừa hiển thị.

Kiểm tra validate:

• Nếu không hợp lệ: Hiển thị thông báo lỗi: | Case | Tác nhân | Nội dung thông báo | Ghi chú
 | Từ ngày lớn hơn Đến ngày | Client MB | Khoảng thời gian tìm kiếm không hợp lệ. Quý khách vui lòng kiểm tra lại! | 

 | 
Khoảng thời gian lớn hơn 01 năm
 | 
Client MB
 | 
Quý khách vui lòng nhập khoảng thời gian nhỏ hơn 01 năm!
 | 

• Nếu hợp lệ: Gửi yêu cầu tìm kiếm lịch sử sang MB server
 | MB server | Nhận và gửi yêu cầu sang Bank server
 | Bank server | 
Nhận và xử lý lấy dữ liệu: Sắp xếp dữ liệu theo thời gian tăng dần và trả về cho MB server

 | MB server | Nhận thông tin và trả kết quả cho client
 | Client MB | 
Nhận kết quả:

• Nếu thành công: Hiển thị như màn hình mô tả. Nếu không có dữ liệu, hiển thị thống báo "Khồng tồn tại giao dịch trong khoảng thời gian yêu cầu!"
• Nếu không thành công: Hiển thị thông báo tương ứng mã lỗi trả về
 | 3 | Nhấn vào 1 giao dịch | Client MB | 
Hiển thị màn hình Chi tiết giao dịch

Gửi yêu cầu lấy chi tiết giao dịch theo mã giao dịch

<Tham khảo logic tại màn hình Chi tiết giao dịch>

###### d) Màn hình Chi tiết giao dịch
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Lấy thông tin chi tiết giao dịch | Client MB | Gửi yêu cầu lấy chi tiết giao dịch theo mã giao dịch
 | MB server | Nhận và gửi yêu cầu sang Bank server
 | Bank server | Nhận và xử lý yêu cầu, lấy dữ liệu trả về cho MB server
 | MB server | Nhận thông tin trả về và gửi lại cho client
 | Client MB | 
Nhận kết quả:

• Thành công: Hiển thị dữ liệu như mô tả
• Không thành công: Hiển thị thông báo lỗi tương ứng mã lỗi nhận được

---


