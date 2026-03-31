# 📋 OTT & Voice

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `messaging/`
> **Trích xuất:** 2026-03-28

---

## 25. URD_NHẬN TIN OTT QUẢNG CÁO, OTT BĐSD(GÓI 4)

> **Page ID:** `37659607` · **Version:** 22
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37659607

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới 
 | 
 
 | A | Lê Thị Hồng | V.1.0.0 | 
Tạo mới
 | 

 | 
 
 | M | Lê Thị Hồng | V.1.0.0 | 
Bổ sung mô tả mã hóa tin OTT BĐSD (force update)
 | 

 | 
 
 | M | Doãn Minh Thu | V.1.0.0 | 
Cập nhật MH Cài đặt thông báo:

• Bỏ tính năng: Xem thông báo nhanh
• Thêm tính năng: Quản lý chia sẻ thông báo BĐSD | 

 | 
 
 | M | Doãn Minh Thu | V.1.0.0 | 
Bổ sung

• 
Danh sách các loại tin OTT phân bổ theo Tab
 | 

 | 
 
 | M | Lê Viết Thành | V.1.0.0 | 
Cập nhật

• 
Thêm tin OTT thông báo kết quả xử lý yêu cầu tra soát vào Danh sách các loại tin OTT phân bổ theo Tab
 | 

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, MB Client, Server, GW OTT BĐSD (Bank), server OTT VNPAY
• Điều kiện trước: 
• KH đã cài đặt ứng dụng thành công và đã kích hoạt user trên thiết bị. 
• KH đã đăng ký nhận tin OTT BĐSD thành công
• Kết quả mong muốn:
• KH nhận được tin báo OTT quảng cáo, OTT BĐSD tại chức năng Thông báo
• KH có thể cài đặt chế độ xem tin Biến động số dư trước đăng nhập thành công.
#### 2/ Luồng màn hình

MH 1-  Tab Tất cả/ Thông báo khác

MH 2.1- Tab Biến động số dư - Giải mã thành công

MH 2.2: Không nhận được key giải mã 

• TH không update app nhưng KH cài đặt xem trước tin BĐSD trước đăng nhập
• Hoặc đã update app, đã nhận được key giải mã Client giải mã bị lỗi)

MH 4

MH 5

MH 6

MH 7

MH 8

MH 9

MH10

#### Mô tả màn hình

MH1
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
Read Only
 | 
--
 | 
--
 | 
Thông báo

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | 
 | 
 | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | 
Tab tin
 | 
Tab
 | 
Select
 | 
 | 
 | 
Hiển thị 3 tab tin fix tại client theo type tin OTT bao gồm:

• Tất cả
• Biến động số dư
• thông báo khác
Mặc định focus tại tab “Tất cả”

Mỗi tin có các chức năng: Xóa, Sao chép, Chia sẻ

 | 4 | 
Chức năng cài đặt xem thông báo
 | 
Button
 | 
Click
 | 
 | 
 | 
Nhấn vào hiển thị màn hình số 4: Cài đặt thông báo

Chỉ hiển thị icon này khi đã đăng nhập

 | 6 | 
Ô tìm kiếm
 | 
Text Search
 | 
Text
 | 
 | 
 | 
• Mặc định trống với label “Tìm kiếm”
• Cho phép tìm kiếm gần đúng tại Client với các bản tin đã lấy về theo các tiêu chí:
• Tiêu đề tin
• Nội dung tin
 | 7 | 
Danh sách tin
 | 
View List
 | 
Click
 | 
--
 | 
--
 | 
Danh sách tin thông báo được hiển thị theo quy định sau:

• Hiển thị danh sách tin OTT lấy từ hệ thống OTT về theo tab tin đang focus, được sắp xếp theo thứ tự từ mới nhất đến cũ nhất
• Tin được nhóm theo ngày tại client, với các giá trị quy định:
         - dd/mm/yyyy

         - Hôm qua

         - Hôm nay

• Mỗi lần cho phép lấy tin của 30 ngày gần nhất (vuốt lên để loadmore)
• Mỗi tin bao gồm các thông tin:
         - Nội dung tin: Hiển thị đầy đủ ( text, hình ảnh, video, link ...)

         - Thời gian gốc của tin: Định dạng hh:mm

         - Nút điều hướng (nếu có): Đối với các tin bao gồm: Đặt vé máy bay thành công, Đặt đơn hàng VnShop thành công; Tin nhắc nợ cước thì có nút “Thanh toán” cho phép khởi tạo giao dịch thanh toán từ các tin OTT này.

Thông báo BĐSD hiển thị theo fomat:

• Màu sắc text: Với biến động là ghi có: có đấu + và màu xanh
• Với biến động là ghi nợ: Có dấu – và màu đỏ
• Số tài khoản, Số tiền ở SDTT và SDKD được in đậm
• ND được lấy từ Bank
Nếu không có thông báo nào, hiển thị text "Quý khách không có thông báo từ hệ thống"

Click vào notify thông báo trên thiết bị ( Notify OTT BĐSD + các tin OTT Khuyến mại khác)

• HĐH Android→ Mở đến Tab Tất cả + Focus vào đúng tin OTT đã chọn)
• HĐH IOS → Mở đến Tab Tất cả + Focus vào tin OTT mới nhất trong tab Tất cả (Do hạn chế về HĐH, nếu focus đúng vào tin OTT đã chọn, IOS sẽ bị crash app)

MH4. Màn hình cài đặt thông báo
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
Read Only
 | 
--
 | 
--
 | 
Cài đặt thông báo

 | 2 | 
Quản lý chia sẻ thông báo BĐSD 
 | 
Label
 | 
Click
 | 
--
 | 
--
 | 
Hiển thị MH Quản lý chia sẻ thông báo BĐSD

Tham khảo mô tả tại: 

 | 3 | Quản lý thông báo | Label | Click | -- | -- | 
Hiển thị MH Quản lý thông báo

Tham khảo mô tả tại: 

 | 4 | Xóa tất cả thông báo | Label | Click | -- | -- | 
Click vào hiển thị thông báo "Quý khách có chắc chắn muốn xóa thông báo này không"

#### 3/ Luồng xử lý

Note: Hiện tại Coopbank không có luồng Bank mã hóa bản tin OTT BĐSD và trả key cho SDK OTT giải mã key (Mà chỉ mã hóa server)

a. Màn hình thông báo
 | TT | Thao tác | Tác nhân | Mô tả
 | Trường hợp chưa đăng nhập
 | 1 | Tại màn hình Login: Nhấn vào chức năng thông báo | 
MB Client
 | 
Gửi yêu cầu lấy danh sách tin OTT khuyến mại sang OTT Server (theo CIF)

 | 
OTT Server
 | 
Xử lý và trả kết quả tin OTT mới nhất (Trong vòng 30 ngày gần nhất) 

 | 
MB Client
 | 
Nhận kết quả:

• Thành công: Kiểm tra trạng thái ON/OFF của cài đặt thông báo
          - Nếu ON: Hiển thị đầy đủ tin nhận được tại tab Tất cả

          - Nếu OFF: Lọc và không hiển thị tin Biến động số dư tại tab “Tất cả”

• Không thành công: Hiển thị thông báo lỗi kết nối sang hệ thống OTT Server
 | 2 | 
Nhấn sang tab “Biến động số dư”
 | 
MB Client
 | 
Kiểm tra trạng thái ON/OFF của cài đặt thông báo:

-       Nếu ON: Gửi yêu cầu lấy danh sách tin OTT Biến động số dư sang OTT Server

-       Nếu OFF: Hiển thị thông báo: Quý khách cần đăng nhập ứng dụng để xem tin Biến động số dư. tại Tab Tất cả

Nút “Hủy”: Nhấn nút này, tắt thông báo và hiển thị màn hình đang thao tác.

Nút “Đồng ý”: Hiển thị màn hình đăng nhập ứng dụng → Thực hiện đăng nhập → Hiển thị màn hình thông báo (tab: Biến động số dư)

 | 
OTT Server
 | 
Xử lý và trả kết quả  tin OTT Biến động số dư (Trong vòng 30 ngày gần nhất) - Không bao gồm tin đã xóa

 | 
MB Client
 | 
Nhận kết quả:

- Giải mã tin thành công: Hiển thị màn hình nội dung OTT BĐSD đã giải mã

- Giải mã tin bị lỗi hoặc không nhận được key giải mã: 

• TH không update app nhưng KH cài đặt xem trước tin BĐSD trước đăng nhập nên không nhận được key giải mã
• Hoặc đã update app, đã nhận được key giải mã Client giải mã bị lỗi
→ Hiển thị nội dung " Quý khách nhận được thông báo mới. Vui lòng đăng nhập hoặc đăng nhập lại ứng dụng để đọc tin"

-  Không thành công: Hiển thị thông báo lỗi kết nối sang hệ thống OTT Server

 | 3 | 
Nhấn sang tab “thông báo khác”
 | 
MB Client
 | 
Gửi yêu cầu lấy danh sách tin OTT khác sang OTT Server

 | 
OTT Server
 | 
Xử lý và trả kết quả tin OTT khác (Trong vòng 30 ngày gần nhất) 

 | 
MB Client
 | 
Nhận kết quả:

-       Thành công: Hiển thị màn hình như đã mô tả

-       Không thành công: Hiển thị thông báo lỗi kết nối sang hệ thống OTT Server

 | 4 | Nhấn vào icon tổng hợp chức năng tại 1 tin | MB Client | Hiển thị các chức năng: Sao chép; Chia sẻ, Xóa
 | 4.1 | Nhấn vào Sao chép | MB Client | Thực hiện sao chép toàn bộ tin nhắn đã chọn
 | 4.2 | Nhấn vào Chia sẻ | MB Client | Tham khảo<>
 | 4.3

 | Nhấn vào Xóa

 | 
MB Client
 | 
Gửi yêu cầu xóa tin OTT sang OTT Server

 | 
OTT
 | 
Xử lý cập nhật trạng thái “Xóa” và trả kết quả về cho MB Client

 | 
MB Client
 | 
Nhận kết quả:

-       Thành công:

   Cập nhật danh sách tin đã xóa tin yêu cầu

-       Không thành công:

  Hiển thị thông báo lỗi giao tiếp (gián đoạn, timeout)

 | 5 | 
Vuốt lên hết và xem tin cuối cùng
 | 
App Client
 | 
Gửi yêu cầu đánh dấu tất cả các bản tin đã lấy về sang trạng thái đã xem lên OTT Server

 | 
OTT Server
 | 
Xử lý:

-       Cập nhật trạng thái đã xem tại DB của OTT Server

-       Trả kết quả về cho App Client

 | 
App Client
 | 
Nhận kết quả:

-       Thành công: Cập nhật tất cả các tin đã gửi lên về trạng thái “Đã xem”

-       Không thành công: Hiển thị thông báo lỗi giao tiếp (gián đoạn, timeout)

 | 6 | 
Nhấn nút điều hướng tại 1 tin thông báo (nếu có)
 | 
MB Client
 | 
Hiển thị màn hình đăng nhập ứng dụng --> đăng nhập → Mở đến tab Tất cả → Bấm Thanh toán trong tin OTT tại Tab Tất cả mở đến MH Khởi tạo chức năng tương ứng (TH QR ngược không có MH khởi tạo thì mở đến MH xác nhận thanh toán)

 | 7 | Tìm kiếm | MB Client | Thực hiện tìm kiếm tương đối theo tiêu đề hoặc nội dung tin
 | Trường hợp đã đăng nhập
 | 1 | Tại màn hình Trang chủ: Nhấn vào chức năng Thông báo | 
MB Client
 | 
Gửi yêu cầu lấy danh sách tin OTT Khuyến mại sang OTT Server (theo CIF)

 | 
OTT Server
 | 
Xử lý và trả kết quả  tin OTT khuyến mại mới nhất (Trong vòng 30 ngày gần nhất)

 | 
MB Client
 | 
Nhận kết quả:

• Thành công: Hiển thị màn hình Thông báo focus vào tab Tất cẩ
• Không thành công: Hiển thị thông báo lỗi kết nối sang hệ thống OTT Server
 | 2 | 
Nhấn sang tab “Biến động số dư”
 | 
MB Client
 | 
Gửi yêu cầu lấy danh sách tin OTT Biến động số dư sang OTT Server

 | 
OTT Server
 | 
Xử lý và trả kết quả  tin OTT Biến động số dư (Trong vòng 30 ngày gần nhất - Không bao gồm tin đã xóa)

 | 
MB Client
 | 
Nhận kết quả:

-       Thành công: Hiển thị màn hình như đã mô tả

-       Không thành công: Hiển thị thông báo lỗi kết nối sang hệ thống OTT Server

 | 3 | 
Nhấn sang tab “thông báo khác”
 | 
MB Client
 | 
Gửi yêu cầu lấy danh sách tin OTT khác sang OTT Server

 | 
OTT Server
 | 
Xử lý và trả kết quả  tin OTT khác (Trong vòng 30 ngày gần nhất)

 | 
MB Client
 | 
Nhận kết quả:

-       Thành công: Hiển thị màn hình như đã mô tả

-       Không thành công: Hiển thị thông báo lỗi kết nối sang hệ thống OTT Server

 | 4 | Nhấn vào icon tổng hợp chức năng tại 1 tin | MB Client  | Hiển thị các chức năng: Sao chép, Chia sẻ, Xóa
 | 4.1 | Nhấn vào Sao chép | MB Client | Thực hiện sao chép toàn bộ tin nhắn đã chọn
 | 4.3

 | Nhấn vào Xóa

 | 
MB Client
 | 
Gửi yêu cầu xóa tin OTT sang OTT Server

 | 
OTT
 | 
Xử lý cập nhật trạng thái “Xóa” và trả kết quả về cho MB Client

(Với các thông báo khác tin BĐSD chỉ xóa tại MB Client)

 | 
MB Client
 | 
Nhận kết quả:

-       Thành công:

 Cập nhật danh sách tin đã xóa tin yêu cầu

-       Không thành công:

Hiển thị thông báo lỗi giao tiếp (gián đoạn, timeout)

 | 5 | 
Nhấn nút điều hướng tại 1 tin thông báo (nếu có)
 | 
MB Client
 | 
Căn cứ theo loại tin để hiển thị màn hình khởi tạo tương ứng của chức năng

 | 6 | Tìm kiếm | MB Client | Thực hiện tìm kiếm tương đối theo tiêu đề hoặc nội dung tin
 | 7 | 
Nhấn icon Cài đặt thông báo
 | 
MB Client
 | 
Hiển thị màn hình Cài đặt thông báo (Chức năng này chỉ hiển thị khi đã đăng nhập)

b. Màn hình Cài đặt thông báo
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn sang chế độ OFF
 | 
MB Client
 | 
Cập nhật trạng thái xem tin Biến động số dư trước khi đăng nhập sang trạng thái OFF.

 | 2 | 
Nhấn sang chế độ ON
 | 
MB Client
 | 
Cập nhật trạng thái xem tin Biến động số dư trước khi đăng nhập sang trạng thái ON.

c. Xóa tất cả thông báo
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn xóa tất cả thông báo
 | 
MB Client
 | 
Hiển thị "Quý khách có chắc chắn muốn xóa tất cả thông báo này không"

• Bấm Không: Tắt Popup
• Bấm Đồng ý: Gửi yêu cầu Xóa tất cả tin sang hệ thống OTT
 | 
 | 
 | 
OTT
 | 
Xử lý xóa tất cả trả kết quả về cho MB Client

(Với các thông báo khác tin BĐSD chỉ xóa tại MB Client)

 | 
 | 
 | 
MB Client
 | 
Nhận kết quả:

-       Thành công:

 Cập nhật danh sách tin đã xóa tin yêu cầu

-       Không thành công:

Hiển thị thông báo lỗi giao tiếp (gián đoạn, timeout)

#### 4/ Danh sách các loại tin OTT phân bổ theo Tab
 | Loại tin | GroupType | TypeID | Mô tả  | Tab hiển thị
 | Tin chào mừng | G_NOTIFY | 1 |   | Tất cả, Tin khác
 | Biến động số dư | G_BALANCER | 16 | Là tin biến động số dư tài khoản gửi từ hệ thống bank | Tất cả, Biến động
 | Tin khuyến mại |  G_PREFER | 13 | Là tin từ BE OTT | Tất cả, Tin khác
 | Tin nhắc nợ |  G_NOTIFY | 19 | 
• Tin nhắc nợ nộp tiền điện
• Tin nhắc nợ nộp tiền nước
• Tin nhắc nợ nộp cước viễn thông
•  Tin nhắc nợ nộp cước truyền hình | Tất cả, Tin khác
 | 
Tin chia sẻ BĐSD | G_NOTIFY | 304 | Tin được chia sẻ | Tất cả, Tin khác
 | 305 | Tin thông báo khi có thay đổi về đăng ký chia sẻ & nhận tin chia sẻ OTT BĐSD | Tất cả, Tin khác
 | Tin nhắc giấy tờ sắp hết hạn (Thông tư 17) | G_NOTIFY | 29 | Tin nhắc GTTT sắp hết hạn do MB server gửi | Tất cả, Tin khác
 | Tin thông báo kết quả xử lý yêu cầu tra soát | G_NOTIFY | 30 | Tin thông báo kết quả xử lý yêu cầu tra soát gửi từ BO Server | Tất cả, Tin khác

To

---


## 26. URD_MÃ HÓA TIN OTT BĐSD

> **Page ID:** `341838123` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/341838123

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*1 trang con:*

### 26.1. SOW - Luồng nhận/gửi tin OTT BĐSD có mã hóa - Bank

> **Page ID:** `343608033` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/343608033

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
  
 | A | Doãn Minh Thu | 
 | 
Tạo mới tài liệu
 | V1.0 | Quách Thị Lệ
 | 
 
 | M | Lê Thị Hồng | 
 | 
Cập nhật
 | 
 | 

Mục lục
none

### 1/ Mục đích & ý nghĩa

Tuân thủ Nghị định 13/2023/NĐ-CP bảo vệ dữ liệu cá nhân. Không lưu các thông tin nhạy cảm của khách hàng như: Số tài khoản, số dư ...

### 2/ Hiện trạng và đề xuất

2.1. Hiện trạng

• Bank gửi tin trực tiếp → OTT Server (ko mã hóa tin) → Mobile Client
• Bank có thể check trạng thái tin OTT trên OTT Server
2.2. Đề xuất

• Bank gửi tin → Hệ thống MB (mã hóa tin) → OTT Server → Mobile Client (Giải mã)
• Phương án: Bổ sung Job mã hóa tin ở Hệ thống MB, SDK OTT giải mã tin và hiển thị tại Client

### 3/ Phạm vi thực hiện
 | Nhóm chức năng | Chức năng | Loại | Mô tả cơ bản | Độ khó | Phạm vi tác nhân thực hiện | Link tài liệu
 | Đăng nhập | 
• Kích hoạt lần đầu
• Kích hoạt trên thiết bị khác
• Đăng nhập lần sau bằng mật khẩu
• Đăng nhập lần sau bằng FaceID/TouchID | 
GreenCập nhật
 | 
Gen key giải mã, trả key giải mã, nhận key giải mã
 | 
BlueTrung Bình
 | Client, Server | 

 | Đăng ký OTT BĐSD | Đăng ký OTT BĐSD | 
GreenCập nhật
 | 
Gen key giải mã, trả key giải mã, nhận và giải mã key tại các chức năng đăng nhập/ Đăng ký
 | 
BlueTrung Bình

 | Nhận thông báo | Nhận tin OTT BĐSD | 
GreenCập nhật
 | 
Giải mã key
 | 
BlueTrung Bình
 | Client | 

 | Báo cáo trạng thái OTT BĐSD | 
 | 
BlueThêm mới
 | 

 | 

 | BO | 

### 4/ Đánh giá ảnh hưởng

Ngân hàng Co-opBank đã chốt sẽ chọn PA Force Update chức năng Mã hóa tin BĐSD
 | Hệ thống | Chức năng | Ảnh hưởng
 | App | 
• Kích hoạt lần đầu
• Kích hoạt trên thiết bị khác
• Đăng nhập lần sau bằng mật khẩu
• Đăng nhập lần sau bằng FaceID/TouchID
• Đăng ký OTT BĐSD | Cần test lại việc server trả key giải mã có ảnh hưởng đến chức năng hiện tại không?
 | App | Nhận thông báo | 
• Tin cũ đã nhận từ trước thời điểm golive mã hóa: KH vẫn nhận tin và đọc được, xem được lịch sử của các tin BĐSD cũ ở dạng không mã hóa
• Tin mới nhận được sau thời điểm golive: Nhận tin và giải mã được tin.
• Các tin khác như tin quảng cáo, tin nhắc nợ có nhận được tin theo nghiệp vụ hiện tại không?

---


## 27. URD_CHIA SẺ THÔNG BÁO OTT BĐSD

> **Page ID:** `306020713` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/306020713

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*5 trang con:*

### 27.1. Luồng Chia sẻ tin OTT BĐSD - VNPAY

> **Page ID:** `295371205` · **Version:** 20
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/295371205

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
   
 | A | Doãn Minh Thu | 
 | 
Tạo mới tài liệu
 | V1.0.0 | Quách Thị Lệ
 | 
 
 | M | Doãn Minh Thu | V1.0.0 | 
Cập nhật:

• Luồng nghiệp vụ
• Luồng màn hình mockup | 
 | Quách Thị Lệ
 | 
 
 | M | Doãn Minh Thu | V1.0.0 | 
Cập nhật các thông tin Bank cung cấp thêm:

• Số lượng tối đa STK thanh toán được chia sẻ và SĐT nhận chia sẻ
• Điều kiện KH(B, C, ..) nhận được tin chia sẻ OTT BĐSD
• API | 
 | Quách Thị Lệ

Mục lục
none

### 1/Mục đích, ý nghĩa chức năng

• FE: Cung cấp cho KH tiện ích chia sẻ thông báo BĐSD của các stk thanh toán đến một hoặc nhiều KH khác trong cùng hệ thống Co-opBank
• KH(A) đăng ký chia sẻ thông báo BĐSD của 1 hoặc nhiều stk cho một hoặc nhiều KH (B, C, D, ...)
• KH(B, C, D, ..) nhận được thông báo BĐSD từ các stk được KH(A) chia sẻ
• BE: Cung cấp cho Bank tiện ích báo cáo thống kê
• Quản lý đăng ký chia sẻ OTT
• Quản lý giao dịch chia sẻ OTT
• Quản lý giao dịch nhận chia sẻ OTT
• Quản lý nội dung chia sẻ OTT
• ...
### 2/ Phương án

• KH(A) chủ động đăng ký dịch vụ chia sẻ tin BĐSD của mình với KH(B,C,D,...) → KH(B,C,D,...) có thể Đồng ý hoặc Từ chối. Nếu đồng ý thì mới được chia sẻ tin BĐSD của KH(A) & không có quyền dừng chia sẻ.
• KH(A) được lựa chọn 1 hoặc nhiều stk thanh toán hợp lệ của mình để chia sẻ tin OTT BĐSD: → Chia sẻ bao nhiêu STK thì KH(B,C,D ...) nhận được tin chia sẻ của bấy nhiêu STK
• KH(A) được lựa chọn 1 hoặc nhiều KH để nhận tin chia sẻ OTT BĐSD: KH(B, C, D) => 3 KH(B, C, D) nhận được tin chia sẻ OTT BĐSD từ các STK mà KH(A) chia sẻ với Nội dung giống nhau (Bank có trường phân biệt tin BĐSD gốc & tin chia sẻ) | TT | Nội dung | Mô tả nguyên tắc
 | 1 | Trạng thái của các đối tượng | 
• KH(A): Trạng thái đăng ký chia sẻ tin OTT BĐSD của TKTT: Đã đăng ký / Hủy đăng ký
• KH(B): Trạng thái nhận tin chia sẻ: Chờ xác nhận, Đang chia sẻ, Dừng chia sẻ, Từ chối
 | 2 | Điều kiện KH(A) được đăng ký dịch vụ chia sẻ tin OTT BĐSD  | 
• Trạng thái đăng ký Mobile Banking: Active
• Có tài khoản thanh toán hợp lệ (accountType = U)
 | 3 | Điều kiện để tin OTT BĐSD của KH(A) được chia sẻ | 
• Trạng thái chia sẻ tin OTT BĐSD của STK thanh toán: Đã đăng ký
 | 4 | Điều kiện KH(B, C, ..) nhận được tin chia sẻ OTT BĐSD | 
• Trạng thái đăng ký Mobile Banking: Đã kích hoạt, Sai mật khẩu quá số lần, Chờ duyệt cập nhật thông tin, Chờ duyệt cấp lại mật khẩu
• Trạng thái chia sẻ của STK mà KH(A) chọn chia sẻ: Đã đăng ký
• Trạng thái nhận tin chia sẻ: Đang chia sẻ
 | 6 | Số lượng tối đa STK thanh toán được chia sẻ tin thông báo BĐSD | 10
 | 7 | Số lượng tối đa SĐT được nhận tin chia sẻ thông báo BĐSD | 30
 | 8 | Type tin  | 
• Tin BĐSD = 16
• Tin BĐSD được chia sẻ = 304
• Tin thông báo từ chức năng Quản lý chia sẻ OTT BĐSD = 305

### 3/ Phạm vi thực hiện

### 4/ Đánh giá ảnh hưởng

### 5/ Luồng nghiệp vụ

#### 5.1/ KH đăng ký mới dịch vụ

 

#### 5.2/ KH được chia sẻ thông báo BĐSD

 

#### 5.3/ KH cập nhật chia sẻ thông báo BĐSD

 

#### 5.4/ KH hủy dịch vụ

 

### 6/ Luồng màn hình

Xem chi tiết tại Đường dẫn này

---

### 27.2. Tổng hợp nội dung OTT theo thao tác người dùng

> **Page ID:** `345214209` · **Version:** 6
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/345214209

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 

 | A | 
Doãn Minh Thu
 | 
 | 
Tạo mới
 | V1.0.0

 | STT | Thao tác | Thông báo đến người thao tác | Thông báo đến người ảnh hưởng
 | 
A
 | 
KH đăng ký dịch vụ chia sẻ thông báo BDSD trên ứng dụng

 | 1 | Đăng ký dịch vụ thành công (Đăng ký lần đầu), có thông tin TKTT chia sẻ & SĐT nhận chia sẻ | Hiển thị MH Kết quả giao dịch | 
Thực hiện bắn tin OTT về SĐT được nhận chia sẻ trong danh sách, theo rule như sau:
 | Thông tin | Mô tả
 | Type OTT | 
305

 | Tab hiển thị | 
Tin khác

 | Nội dung | 
Khách hàng {Tên khách hàng} muốn chia sẻ thông báo BĐSD trên ứng dụng với bạn. Vui lòng truy cập chức năng Quản lý chia sẻ BĐSD để xác nhận.

 | Button | 
Quản lý chia sẻ BĐSD

→ Nhấn Button điều hướng đến màn hình Chia sẻ với tôi (RoutingID = 111020)

 | 2 | 
Thêm thông tin chia sẻ thành công (Đăng ký lần sau), có thông tin TKTT chia sẻ hoặc/và SĐT nhận chia sẻ
 | Hiển thị MH Kết quả giao dịch | 
Thực hiện bắn tin OTT về người được chia sẻ có trạng thái "Đang chia sẻ" theo rule bên dưới

 | 
 | 
• Thêm STK chia sẻ | 
 | | Thông tin | Mô tả
 | Type OTT | 
305

 | Tab hiển thị | 
Tin khác

 | Nội dung | 
"Khách hàng {Tên khách hàng} đã cập nhật chia sẻ thông báo BĐSD trên ứng dụng với bạn. Vui lòng truy cập chức năng Quản lý chia sẻ BĐSD để kiểm tra."

 | Button | 
Không có

 | 
 | 
• Thêm SĐT chia sẻ (Tương tự case đăng ký lần đầu) | 
 | | Thông tin | Mô tả
 | Type OTT | 
305

 | Tab hiển thị | 
Tin khác

 | Nội dung | 
Khách hàng {Tên khách hàng} muốn chia sẻ thông báo BĐSD trên ứng dụng với bạn. Vui lòng truy cập chức năng Quản lý chia sẻ BĐSD để xác nhận.

 | Button | 
Quản lý chia sẻ BĐSD

→ Nhấn Button điều hướng đến màn hình Chia sẻ với tôi (RoutingID = 111020)

 | 3 | Dừng chia sẻ thành công | 
 | 

 | 
 | 
• Bớt STK chia sẻ (còn ít nhất 1 STK) | Hiển thị MH Kết quả giao dịch | | Thông tin | Mô tả
 | Type OTT | 
305

 | Tab hiển thị | 
Tin khác

 | Nội dung | 
"Khách hàng {Tên khách hàng} đã cập nhật chia sẻ thông báo BĐSD trên ứng dụng với bạn. Vui lòng truy cập chức năng Quản lý chia sẻ BĐSD để kiểm tra."

 | Button | 
Không có

 | 
 | 
• Bớt SĐT chia sẻ | | Thông tin | Mô tả
 | Type OTT | 
305

 | Tab hiển thị | 
Tin khác

 | Nội dung | 
"Khách hàng {Tên khách hàng} đã dừng chia sẻ thông báo BĐSD trên ứng dụng với bạn."

 | Button | 
Không có

 | 
 | 
• Bớt STK chia sẻ (Còn 0 STK) | Hiển thị thông báo trên MH: Hủy dịch vụ thành công | | Thông tin | Mô tả
 | Type OTT | 
305

 | Tab hiển thị | 
Tin khác

 | Nội dung | 
"Khách hàng {Tên khách hàng} đã dừng chia sẻ thông báo BĐSD trên ứng dụng với bạn."

 | Button | 
Không có

 | 3 | 
Hủy dịch vụ thành công

(= Dừng chia sẻ cho toàn bộ SĐT Đang chia sẻ )
 | Hiển thị thông báo trên MH: Hủy dịch vụ thành công | | Thông tin | Mô tả
 | Type OTT | 
305

 | Tab hiển thị | 
Tin khác

 | Nội dung | 
"Khách hàng {Tên khách hàng} đã dừng chia sẻ thông báo BĐSD trên ứng dụng với bạn."

 | Button | 
Không có

 | 
 B
 | 
KH được chia sẻ BĐSD trên ứng dụng

 | 1 | Đồng ý nhận chia sẻ thành công | Hiển thị thông báo trên MH: Đồng ý nhận chia sẻ thành công | 
Thực hiện bắn tin về SĐT của người chia sẻ theo rule:
 | Thông tin | Mô tả
 | Type OTT | 
305

 | Tab hiển thị | 
Tin khác

 | Nội dung | 
Khách hàng {Tên khách hàng} - {SĐT khách hàng} đồng ý nhận tin thông báo BĐSD được chia sẻ từ bạn.

 | Button | 
Không có

 | 2 | Từ chối nhận chia sẻ thành công | Hiển thị thông báo trên MH: Từ chối nhận chia sẻ thành công | 
Thực hiện bắn tin về SĐT của người chia sẻ theo rule:
 | Thông tin | Mô tả
 | Type OTT | 
305

 | Tab hiển thị | 
Tin khác

 | Nội dung | 
Khách hàng {Tên khách hàng} - {SĐT khách hàng} từ chối nhận tin thông báo BĐSD được chia sẻ từ bạn.

 | Button | 
Không có

---

### 27.3. Usecase_Đăng ký chia sẻ thông báo OTT BĐSD

> **Page ID:** `350259496` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/350259496

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
 
 | A | ThuDM | 
 | 
Tạo mới tài liệu
 | V.1.0 | 

Mục lục
none

### 1/ Tóm tắt Use Case

 | Use Case Name | Đăng ký chia sẻ OTT Biến động số dư (BĐSD) cho số điện thoại khác
 | Use Case ID | uc-dkcsottbdsd-01
 | Use Case Description | 
Là Khách hàng (KH), tôi muốn đăng ký chia sẻ OTT BĐSD của một hoặc nhiều tài khoản cho một hoặc nhiều người khác (Qua SĐT) thành công

 | Actor | 
KH, App MB, MB Server, Bank, OTT server

 | Priority | 
MEDIUM

 | Trigger | 
KH muốn thực hiện đăng ký chia sẻ OTT BDSD cho người khác (Qua SĐT)

 | 
Pre-Condition
 | 
• KH chia sẻ truy cập chức năng "Cài đặt chia sẻ OTT BĐSD"
• KH chia sẻ có gói dịch vụ được sử dụng chức năng này
• KH chia sẻ có tài khoản thanh toán hợp lệ đã đăng ký nhận OTT BĐSD (Theo CIF+SĐT)
• KH nhận chia sẻ đã đăng ký MB và có trạng thái: Đã kích hoạt, Sai mật khẩu quá số lần, Chờ duyệt cập nhật thông tin, Chờ duyệt cấp lại mật khẩu
 | Post-Condition | 
• KH thực hiện đăng ký chia sẻ OTT BĐSD cho SĐT thành công
• KH được chia sẻ nhận được thông báo yêu cầu xác nhận đồng ý.
• KH được chia sẻ "Đồng ý" nhận tin chia sẻ.
• Hệ thống MB ghi nhận đăng ký chia sẻ của KH
• Hệ thống MB ghi nhận log đăng ký của KH
 | Basic Flow | 
• KH truy cập chức năng "Cài đặt chia sẻ OTT BĐSD"
• KH chọn tài khoản nhận OTT BĐSD
• KH nhập/chọn thông tin SĐT muốn chia sẻ
• KH thực hiện khởi tạo đăng ký
• KH thực hiện xác thực đăng ký
• KH nhận được kết quả đăng ký thành công
• KH được chia sẻ truy cập chức năng "Cài đặt chia sẻ OTT BĐSD"
• KH được chia sẻ thực hiện "Đồng ý" yêu cầu xác nhận
• KH được chia sẻ nhận được kết quả "Đồng ý" thành công
 | Alternative Flow | 

 | Exception Flow | 
• KH hủy giao dịch
• Thông tin SĐT không hợp lệ, không tồn tại ở MB Server
 | Bussiness Rules | 
• br-01-01: KH được phép đăng ký chia sẻ cho nhiều SĐT
• br-01-02: KH được phép nhận chia sẻ từ nhiều STK của nhiều KH khách
 | Non-Funtional Requirement | 
• nfr-01-01: <nhập nội dung>

---

### 27.4. Flow & Action Screen_Chia sẻ thông báo OTT BĐSD

> **Page ID:** `350259530` · **Version:** 9
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/350259530

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
 
 | A | Doãn Minh Thu | 
 | 
Tạo mới tài liệu
 | V1.0.0 | Quách Thị Lệ
 | 
 
 | M | Doãn Minh Thu | V1.0.0 | 
Điều chỉnh lại theo thiết kế đã thống nhất với Bank tại cuộc họp sáng 20/12/2023
 | V1.0.1 | 

Mục lục
none

### 1/ Luồng di chuyển màn hình

### 2/ Danh sách màn hình

#### 2.1/ Truy cập tính năng

##### <MH: Thông báo>

##### <MH: Cài đặt thông báo>

##### <MH: Giới thiệu>

##### <MH: Đăng ký>

        

##### <MH: Thêm TKTT chia sẻ>

   

##### <MH: Thêm thành viên - Chọn từ danh bạ>

   

         

##### <MH: Xác nhận giao dịch - đăng ký chia sẻ>

##### <MH: Xác thực giao dịch>

   

##### <MH: Kết quả giao dịch - đăng ký chia sẻ>

##### <MH: Kết quả giao dịch - đăng ký chia sẻ - chi tiết>

   

##### <MH: Đang chia sẻ>

1  2   3        

##### <MH: Đang chia sẻ - Chọn TKTT & SĐT muốn dừng chia sẻ>

1   2

##### <MH: Xác nhận giao dịch - dừng chia sẻ>

Có thực hiện xác thực, MH xác thực tương tự <MH: Xác thực giao dịch> ở bước đăng ký

##### <MH: Kết quả giao dịch - dừng chia sẻ>                    <MH: Kết quả giao dịch - dừng chia sẻ - chi tiết>

         

##### <MH: Chia sẻ với tôi>

 1   2

##### <MH: Chia sẻ với tôi - Chi tiết>

1   2

### 3/ Mô tả màn hình

#### 3.1/ Truy cập tính năng

##### <MH: Thông báo> 

Tham khảo mô tả tại: 

##### <MH: Cài đặt thông báo> 

Tham khảo mô tả tại: URD_NHẬN TIN OTT QUẢNG CÁO, OTT BĐSD(GÓI 4)

##### <MH: Giới thiệu> 
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Nội dung giới thiệu
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Mặc định hiển thị với KH lần đầu đăng ký dịch vụ chia sẻ thông báo BĐSD

• Tiêu đề popup: Thông tin dịch vụ
• icon x: Tắt pop up, về <MH: Đăng ký>
• Nội dung: 
      Chia sẻ Biến động số dư (BĐSD): Là dịch vụ cho phép Quý khách chia sẻ thông báo BĐSD của tài khoản thanh toán trên ứng dụng tới thành viên đã đăng ký sử dụng Co-opBank Mobile Banking thông qua số điện thoại.

• 
• Miễn phí dịch vụ
• Tối đa 10 tài khoản thanh toán
• Tối đa 30 thành viên

#### 3.2/ Quản lý chia sẻ thông báo OTT BĐSD

##### <MH: Đăng ký>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
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
Hiển thị: Quản lý chia sẻ thông báo BĐSD

 | 
3
 | 
Icon thông tin dịch vụ
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Điều hướng đến <MH: Giới thiệu>

 | 

 | 
Tab Đăng ký: Mặc định khi truy cập chức năng sẽ focus vào Tab này, cho phép KH thêm thông tin chia sẻ (bao gồm STK chia sẻ & SĐT nhận chia sẻ)

Nếu đang thêm dữ liệu ở tab này mà chuyển sang tab khác, khi quay lại thì dữ liệu đang nhập sẽ bị mất, có cảnh bảo cho ND → Xem logic xử lý

 | 
4
 | 
Tiêu đề tab
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị: Đăng ký

 | 
5
 | 
TKTT chia sẻ
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị: {icon} Tài khoản thanh toán chia sẻ (N/X)

Trong đó: N là số TKTT KH đã chọn, X là số TKTT tối đa KH được phép đăng ký chia sẻ tại thời điểm đăng ký

* Nếu đăng ký lần đầu, X = Số lượng TKTT tối đa KH được phép đăng ký - đã cấu hình trong BO

* Nếu đăng ký lần sau, X = Số đã cấu hình - số đã đăng ký ở (những) lần đăng ký trước đó

 | 
6
 | 
Thêm tài khoản
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định hiển thị Enable.

• Nếu không có TKTT hợp lệ: Chọn nút → mở popup thông báo: Quý khách không có tài khoản thanh toán hợp lệ để thực hiện chức năng này. Vui lòng kiểm tra lại.
• Nếu có TKTT hợp lệ: Chọn nút → mở <MH: Thêm TKTT chia sẻ>
 | 
7
 | 
Chi tiết TKTT
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Mỗi 1 tài khoản hiển thị 1 dòng: 

• Logo + Số tài khoản: [Số tài khoản chọn trong danh sách] + icon xóa TKTT đã chọn
• Nếu truy vấn không thành công: Box hiển thị highlight
 | 
8
 | 
Thành viên nhận chia sẻ
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị: {icon} Thành viên nhận chia sẻ (M/Y)

Trong đó: M là số SĐT KH đã chọn, Y là số SĐT tối đa được nhận chia sẻ tại thời điểm đăng ký

* Nếu đăng ký lần đầu, Y = Số lượng SĐT tối đa KH được phép chia sẻ - đã cấu hình trong BO

* Nếu đăng ký lần sau, Y = Số đã cấu hình - số đã chia sẻ ở (những) lần đăng ký trước đó

 | 
9
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
Hiển thị: Chỉ thêm số điện thoại đã đăng ký dịch vụ Co-opBank Mobile Banking.

 | 
10
 | 
Số điện thoại
 | 
Textbox
 | 
Number
 | 
X
 | 
11
 | 
• Placeholder: Nhập số điện thoại
• Nếu dán chuỗi số vào ô số điện thoại có khoảng trống ở đầu hoặc/và cuối thì hệ thống xử lý xóa khoảng trống đó.
• Hiển thị disable nếu số thành viên nhận chia sẻ đã đạt mức tối đa cho phép
 | 
11
 | 
Lưu ý
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Hiển thị: Lưu ý: Thành viên được thêm dưới đây sẽ nhận được thông báo BĐSD từ tất cả tài khoản thanh toán đã đăng ký chia sẻ.
 | 
12
 | 
Danh bạ điện thoại
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
• Nếu không có danh bạ: Chọn icon → hiển thị popup thông báo: Quý khách không có danh bạ để thực hiện chức năng này. Vui lòng kiểm tra lại
• Nếu có danh bạ: Chọn icon → hiển thị <MH: Thêm thành viên - Chọn từ danh bạ>
 | 
13
 | 
Chi tiết thành viên
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị khi nhập thành công hoặc thêm từ danh bạ thành công:

• Lưu ý: Thành viên được thêm dưới đây sẽ nhận được thông báo BĐSD từ tất cả tài khoản thanh toán đã đăng ký chia sẻ. (Hiển thị khi có ít nhất 1 thành viên ngoài danh sách)
• Danh sách thành viên: Tên Tài khoản + SĐT + Icon xóa SĐT đã chọn
• Nếu truy vấn SĐT không thành công: Box hiển thị highlight 
 | 
14
 | 
Nút "Đăng ký"
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
• Đối với đăng ký lần đầu: 
• Mặc định Disable
• Chỉ Enable khi KH đã chọn ít nhất 1 TKTT và 1 SĐT.
• Đối với đăng ký lần sau: 

• Mặc định Disable
• Chỉ Enable khi KH đã chọn ít nhất 1 TKTT hoặc 1 SĐT.
• Chọn nút → hiển thị <MH: Xác nhận giao dịch - đăng ký chia sẻ>

##### <MH: Thêm TKTT chia sẻ>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
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
Hiển thị: Danh sách tài khoản thanh toán

 | 
2
 | 
Icon X
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Tắt popup, quay trở lại màn hình thao tác trước

 | 
3
 | 
Ô tìm kiếm
 | 
Textbox
 | 
Input
 | -- | 200 | 
• Placeholder: icon kính lúp, Tìm kiếm
• Hiển thị khi có từ 6 TKTT trở lên
• Tìm kiếm theo số tài khoản
• Cho phép nhập text, dán text, khi có text ô tìm kiếm xuất hiện icon "x": xóa nhanh toàn bộ nội dung đang có
 | 
4
 | 
Danh sách TKTT
 | 

 | 

 | 

 | 

 | 
Hiển thị các TKTT với thông tin sau:

• Logo bank 
• Số tài khoản: [Số TKTT hợp lệ]
• Số dư: Số sư khả dụng + Đơn vị tiền tệ VNĐ
• Tích chọn (hiển thị khi ND bấm chọn vào TKTT, được chọn nhiều)
 | 
5
 | 
Số TKTT đã chọn
 | Label | Read only | 
--
 | 
--
 | 
Hiển thị: Số tài khoản đã chọn: N / tối đa X

Trong đó:

• N = số lượng TKTT đã tích chọn trong danh sách; N tăng/giảm khi ND tích/bỏ tích TKTT trên danh sách
• X là tham số cấu hình số TKTT tối đa được đăng ký chia sẻ tại thời điểm đăng ký
 | 
6
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
• Mặc định Disable khi: N = 0
• Enable khi: 1 < N =< X

##### <MH: Thêm thành viên - Chọn từ danh bạ>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
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
Hiển thị: Danh bạ điện thoại

 | 
2
 | 
Icon X
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Tắt popup, quay trở lại màn hình thao tác trước

 | 
3
 | 
Ô tìm kiếm
 | 
Textbox
 | 
Input
 | -- | 200 | 
• Placeholder: icon kính lúp, Tìm kiếm
• Hiển thị khi có từ 6 SĐT trở lên
• Tìm kiếm theo số điện thoại
• Cho phép nhập text, dán text, khi có text ô tìm kiếm xuất hiện icon "x": xóa nhanh toàn bộ nội dung đang có
 | 
4
 | 
Danh sách SĐT
 | 

 | 

 | 

 | 

 | 
Hiển thị danh bạ với các thông tin sau:

• icon user
• Tên danh bạ
• Số điện thoại
• Tích chọn (hiển thị khi ND bấm chọn vào danh bạ, được chọn nhiều)
 | 
5
 | 
Số thành viên đã chọn
 | Label | Read only | 
--
 | 
--
 | 
Hiển thị: Số thành viên đã chọn: M / tối đa Y

Trong đó: 

• M = số lượng SĐT đã tích chọn trong danh bạ; M tăng/giảm khi ND tích/bỏ tích SĐT trên danh bạ
• Y là tham số cấu hình số lượng SĐT tối đa được đăng ký chia sẻ tại thời điểm đăng ký
 | 
6
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
• Mặc định Disable khi: M = 0
• Enable khi: 1 < M =< Y

##### <MH: Xác nhận giao dịch - đăng ký chia sẻ>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
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
Hiển thị: Xác nhận giao dịch

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
Hiển thị: Quý khách vui lòng kiểm tra thông tin đăng ký đã khởi tạo

 | 
4
 | 
TKTT chia sẻ
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị: {icon} Tài khoản thanh toán chia sẻ (N/X)

Trong đó: N là số TKTT KH đã chọn, X là số TKTT tối đa KH được phép đăng ký chia sẻ tại thời điểm đăng ký

 | 
5
 | 
Danh sách tài khoản chia sẻ
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị 1 hàng 1 TKTT đã chọn, bao gồm thông tin: Logo + Số tài khoản: [Số TKTT đã chọn]

 | 
6
 | 
Thành viên nhận chia sẻ
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị: {icon} Thành viên nhận chia sẻ (M/Y)

Trong đó: M là số SĐT KH đã chọn, Y là số SĐT tối đa được đăng ký nhận chia sẻ.

 | 
7
 | 
Danh sách thành viên nhận chia sẻ
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị 1 hàng 1 thành viên đã chọn, bao gồm thông tin: icon user + Tên tài khoản + SĐT

 | 
8
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
Mặc định Enable

##### <MH: Xác thực giao dịch>

Tham khảo màn hình tại 

##### <MH: Kết quả giao dịch - đăng ký chia sẻ>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay về màn hình Trang chủ

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
Kết quả giao dịch

 | 
3
 | 
Kết quả chi tiết
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị kết quả bao gồm các thông tin:
 | Nội dung | Hiển thị
 | 
Logo Co-opbank
 | Logo Co-opbank
 | Icon thành công | Icon thành công
 | Thông báo | Đăng ký thành công
 | Thời gian giao dịch | dd/mm/yyy hh:mm
 | 
Tài khoản thanh toán chia sẻ

(Chỉ hiển thị nếu số lượng TKTT chia sẻ > 0)
 | 
Số lượng TKTT chia sẻ + icon >

Chọn icon > → hiển thị <MH: Kết quả giao dịch - đăng ky chia sẻ - chi tiết>

 | 
Thành viên nhận chia sẻ

(Chỉ hiển thị nếu số lượng thành viên nhận chia sẻ > 0)
 | 
Số lượng Thành viên nhận chia sẻ + icon >

Chọn icon > → hiển thị <MH: Kết quả giao dịch - đăng ky chia sẻ - chi tiết>

 | 
Chia sẻ
 | icon chia sẻ màn hình kết quả đăng ký 
 | 
Lưu ảnh
 | icon lưu ảnh màn hình kết quả đăng ký 

 | 
4
 | 
Quản lý chia sẻ thông báo BĐSD
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Hiển thị: Quản lý chia sẻ thông báo BĐSD

Chọn nút → Hiển thị <MH: Tab Đang chia sẻ> (Có dữ liệu đã đăng ký)

##### <MH: Kết quả giao dịch - đăng ký chia sẻ - chi tiết>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 

 | 
Chi tiết Tài khoản thanh toán chia sẻ

 | 
1
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
Hiển thị: Tài khoản thanh toán chia sẻ

 | 
2
 | 
Icon X
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Tắt popup, quay trở lại màn hình thao tác trước

 | 
3
 | 
Danh sách tài khoản chia sẻ
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị 1 hàng 1 TKTT đang chia sẻ, bao gồm thông tin: Logo + Số tài khoản: [Số TKTT đang chia sẻ]

 | 

 | 
Chi tiết Thành viên nhận chia sẻ

 | 
1
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
Hiển thị: Thành viên nhận chia sẻ

 | 
2
 | 
Icon X
 | 
Icon
 | 
--
 | 
--
 | 
--
 | 
Tắt popup, quay trở lại màn hình thao tác trước

 | 
3
 | 
Danh sách thành viên nhận chia sẻ
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị 1 hàng 1 SĐT nhận chia sẻ, bao gồm thông tin: icon user + Tên tài khoản + SĐT

##### <MH: Đang chia sẻ>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
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
Hiển thị: Chia sẻ thông báo BĐSD

 | 

 | 
Tab Đang chia sẻ: Hiển thị thông tin TKTT đang chia sẻ và SĐT nhận chia sẻ

 | 

 | 
Nếu chưa có thông tin chia sẻ

 | 

 | 
Thông báo
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị: Quý khách chưa có thông tin đang chia sẻ BĐSD.

 | 

 | 
Nếu có thông tin chia sẻ → Hiển thị các các thông tin bao gồm:

 | 

 | 
TKTT chia sẻ
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị: {icon} Tài khoản thanh toán chia sẻ (N/X)

Trong đó: N là số TKTT KH đã đăng ký chia sẻ, X là số TKTT tối đa KH được phép đăng ký chia sẻ, cấu hình trong BO

 | 

 | 
Chi tiết TKTT
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Mỗi 1 tài khoản hiển thị 1 dòng: 

• Logo + Số tài khoản: [Số tài khoản chọn trong danh sách] + icon xóa TKTT đã chọn
• Ô tích chọn - Chỉ hiển thị khi ND chọn button Hủy chia sẻ
 | 

 | 
Icon group nhóm thông tin TKTT
 | 
icon
 | 
click
 | 
--
 | 
--
 | 
Mặc định hiển thị đầy đủ thông tin

Click chọn → Thu gọn danh sách TKTT

 | 
 | 
Thành viên nhận chia sẻ
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị: {icon} Thành viên nhận chia sẻ (M/Y)

Trong đó: M là số SĐT KH đã đăng ký chia sẻ, Y là số SĐT tối đa được nhận chia sẻ, cấu hình trong BO

 | 
 | 
Lưu ý
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Hiển thị: Lưu ý: Thành viên được thêm dưới đây sẽ nhận được thông báo BĐSD từ tất cả tài khoản thanh toán đã đăng ký chia sẻ.
 | 
 | 
Chi tiết thành viên
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị các thông tin của 1 thành viên bao gồm:

• Trạng thái:
• Chờ xác nhận - (Khi thành viên chưa chấp nhận đề nghị chia sẻ)
• Đang chia sẻ - (Khi thành viên đã chấp nhận đề nghị chia sẻ)
• Người nhận chia sẻ: [Tên tài khoản]
• Số điện thoại: [Số điện thoại của người nhận chia sẻ]
• Ô tích chọn - Chỉ hiển thị khi ND chọn button Hủy chia sẻ
 | 
 | 
Icon group nhóm thông tin Thành viên
 | 
icon
 | 
click
 | 
--
 | 
--
 | 
Mặc định hiển thị đầy đủ thông tin

Click chọn → Thu gọn danh sách thành viên nhận chia sẻ

 | 
 | 
Dừng chia sẻ
 | 
Button
 | 
click
 | 
--
 | 
--
 | 
Mặc định Enable

Hiển thị ô tích cho phép chọn TKTT hoặc/và SĐT trong danh sách Đang chia sẻ để dừng chia sẻ thông báo BĐSD

 | 
 | 
Xóa
 | 
Button
 | 
click
 | 
--
 | 
--
 | 
Mặc định Disable

Hiển thị khi ND chọn nút Dừng chia sẻ, và ở trường hợp: Chưa chọn bất kìa TKTT hoặc SĐT nào trong danh sách Đang chia sẻ

 | 
 | 
Xóa (n)
 | 
Button
 | 
click
 | 
--
 | 
--
 | 
Mặc định Enable

Hiển thị khi ND chọn nút Dừng chia sẻ, và đã chọn ít nhất 1 TKTT hoặc SĐT trong danh sách Đang chia sẻ, n = số lượng TKTT & SĐT đã tích chọn (Còn lại ít nhất 1 TKTT và 1 SĐT)

 | 
 | 
Hủy
 | 
Button
 | 
click
 | 
-

> ⚠️ *Nội dung đã cắt ngắn (21389 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 27.5. User Action Flow_Chia sẻ thông báo OTT BĐSD

> **Page ID:** `356483631` · **Version:** 8
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/356483631

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
 
 | A | Doãn Minh Thu | 
 | 
Tạo mới tài liệu
 | V1.0.0 | Quách Thị Lệ
 | 
 
 | M | Doãn Minh Thu | V1.0.0 | 
Điều chỉnh lại logic theo luồng nghiệp vụ thay đổi (Theo thiết kế mới bank confirm)
 | V1.0.1 | 

Mục lục
none

#### * Luồng thay đổi trạng thái

→ Bối cảnh: 

• KH.A chia sẻ thông báo OTT BĐSD của TKTT.1,2,3 (Chia sẻ mức CIF) cho KH.B (thông qua SĐT.B), KH.C (thông qua SĐT.C), ...
• Nếu KH.B đồng ý nhận chia sẻ → Khi TKTT.1,2,3 có BĐSD, thì SĐT.B sẽ nhận được tin BĐSD của TKTT.1,2,3
• Nếu KH.C không đồng ý nhận chia sẻ → Khi TKTT.1,2,3 có BĐSD, thì SĐT.C không nhận được tin BĐSD của TKTT.1,2,3
→ Trạng thái:

#### 1/ Truy cập chức năng
 |   | Thao tác 1 | Tại <MH: Thông báo> hoặc <MH: Cài đặt thông báo>, KH chọn "Chia sẻ thông báo BĐSD"
 | 
 | Hệ thống MB | 
Kiểm tra danh sách chia sẻ thông báo BĐSD của KH (danh sách TKTT đang chia sẻ, danh sách SĐT nhận chia sẻ, ds KH khác chia sẻ cho mình)

• Timeout: Hiển thị thông báo timeout
• Không hợp lệ: Hiển thị thông báo lỗi | TT | Trường hợp | Nội dung thông báo | Xử lý (Nếu có)
 | 1 | Không lấy được danh sách chia sẻ thông báo BĐSD | Lỗi gián đoạn. Vui lòng kiểm tra thông tin và thử lại! | Đóng thông báo quay về màn hình Thao tác trước đó

• Hợp lệ: 
• 
Nếu là đăng ký lần đầu, hiển thị popup <MH: Giới thiệu>, tắt popup hiển thị <MH: Đăng ký>: Số lượng TKTT chia sẻ & SĐT nhận chia sẻ = số tối đa cấu hình trong BO

• Nếu không phải đăng ký lần đầu, hiển thị <MH: Đăng ký>: Số lượng TKTT chia sẻ & SĐT nhận chia sẻ = số tối đa cấu hình trong BO - Số lượng đang chia sẻ
 |   | Thao tác 2 | Tại <MH: Đăng ký>, KH chọn tab "Đang chia sẻ"
 | 
 | Hệ thống MB | 
Tại tab Đang chia sẻ:

• Nếu không có thông tin đăng ký chia sẻ (danh sách TKTT đang chia sẻ, danh sách SĐT nhận chia sẻ trống) → Hiển thị <MH: Đang chia sẻ>-1
• Nếu có thông tin đăng ký chia sẻ → Hiển thị <MH: Đang chia sẻ>-2, số lượng TKTT chia sẻ & thành viên nhận chia sẻ tương ứng với danh sách chi tiết
 |   | Thao tác 3 | Tại <MH: Đăng ký>, KH chọn tab "Chia sẻ với tôi"
 | 
 | Hệ thống MB | 
Tại Tab Chia sẻ với tôi:

• Nếu không có thông tin chia sẻ (danh sách các KH chia sẻ cho mình) → Hiển thị <MH Chia sẻ với tôi>-1
• Nếu có thông tin chia sẻ → Hiển thị <MH Chia sẻ với tôi>-2, danh sách KH chia sẻ với trạng thái tương ứng
• Trạng thái = Chờ xác nhận, chọn "Chi tiết" → hiển thị <MH: Chia sẻ với tôi - Chi tiết>-1
• Trạng thái = Đang chia sẻ, chọn "Chi tiết" → hiển thị <MH: Chia sẻ với tôi - Chi tiết>-2

#### 2/ Khởi tạo đăng ký
 |   | Thao tác 1 | Tại <MH: Đăng ký>, KH chọn nút "Thêm tài khoản"
 | 
 | Hệ thống MB | 
Gửi yêu cầu truy vấn danh sách TKTT sang Bank

• API queryCurrentAccSum - Truy vấn danh sách tài khoản
• Truyền accountType = U
 | 
 | Bank | 
Xử lý truy vấn danh sách TKTT hợp lệ và trả kết quả:

• Timeout: Trả kết quả timeout cho Hệ thống MB
• Không thành công: Trả kết quả cho Hệ thống MB | TT | Trường hợp | Mẫ lỗi cấu hình | Xử lý (Nếu có)
 | 1 | Danh sách tài khoản trống | 
 | 

 | 2 | Không lấy được danh sách tài khoản | 
 | 

• Thành công: Trả kết quả cho Hệ thống MB
 | 
 | Hệ thống MB | 
Nhận kết quả từ Bank:

• 
Timeout: Trả kết quả timeout cho Client

• Không thành công: Hiển thị thông báo lỗi | TT | Trường hợp | Nội dung thông báo | Xử lý (Nếu có)
 | 1 | Danh sách tài khoản trống | Quý khách không có tài khoản thanh toán hợp lệ để thực hiện chức năng này. Vui lòng kiểm tra thông tin và thử lại! | Đóng thông báo quay về màn hình thao tác trước đó
 | 2 | Không lấy được danh sách tài khoản | Lỗi gián đoạn. Vui lòng kiểm tra thông tin và thử lại! | Đóng thông báo quay về màn hình thao tác trước đó

• Thành công: Hiển thị <MH: Thêm TKTT chia sẻ>, số lượng TKTT được chia sẻ tối đa lấy bằng số hiển thị ở ngoài MH đăng ký
 |   | Thao tác 2 | Tại <MH: Thêm TKTT>, KH thực hiện
 | 
 | Hệ thống MB | 
• 
Nhập dữ liệu tìm kiếm (ô tìm kiếm chỉ hiển thị khi danh sách có từ 6 bản ghi trở lên):

• 
Cho tìm kiếm tương đối theo số TKTT có trong danh sách

• 
Nếu không có kết quả, hiển thị: Không có kết quả tìm kiếm.

• 
Hiển thị nút "x" cho phép xóa toàn bộ ký tự trong ô

• 
Nhấn chọn/Bỏ chọn 1 hoặc nhiều TKTT:

• Chỉ được chọn số lượng TKTT ứng với số tối đa cho phép
• 
Số lượng TKTT đã chọn thay đổi theo thao tác của KH, +1 khi chọn thêm 1 TKTT, -1 khi bỏ chọn 1 TKTT

• 
Nếu số lượng TKTT đã tối đa thì không cho tích chọn thêm nữa

• 
Nhấn icon "X" → Đóng màn hình popup, về màn hình trước đó → những TKTT được chọn/bỏ chọn vừa thao tác sẽ không có ở màn đăng ký

• 
Nhấn Xác nhận, quay về màn hình đăng ký và thực hiện (dựa trên các TKTT đã chọn trong danh sách)

• 
Nếu trong danh sách chọn có TKTT đã được thêm trước đó: → giữ nguyên thông tin TKTT ở MH Đăng ký

• 
Nếu trong danh sách chọn không có TKTT đã được thêm trước đó: → xóa thông tin TKTT ở MH Đăng ký

• 
Nếu trong danh sách chọn có TKTT chưa được thêm trước đó: → thêm thông tin TKTT ở MH đăng ký

 |   | Thao tác 3 | Tại <MH: Đăng ký>, KH thêm thành viên nhận chia sẻ bằng cách nhập vào SĐT
 | 
 | 
Hệ thống MB
 | 
1/ Thoát focus, validate thông tin

• 
Không hợp lệ:
 | 
STT
 | 
Trường hợp
 | 
Mô tả
 | 
Xử lý

 | 1 | 
Chuỗi ký tự nhập vào khác trường hợp sau: là số, bắt đầu bằng số 0 và có độ dài = 10 hoặc 11 ký tự
 | 
Hiển thị thông báo: "Số điện thoại không đúng định dạng. Quý khách vui lòng kiểm tra lại!"
 | 
Đóng thông báo quay về màn hình thao tác trước đó, clear SĐT đã nhập

 | 2 | 
Chuỗi ký tự nhập vào trùng với SĐT đã nhập vào trước đó
 | 
Hiển thị thông báo: "Số điện thoại này đã được thêm vào danh sách nhận thông báo BĐSD. Vui lòng kiểm tra thông tin và thử lại!"
 | 
Đóng thông báo quay về màn hình thao tác trước đó, clear SĐT đã nhập

• 
Hợp lệ:
 | 
STT
 | 
Trường hợp
 | 
Mô tả
 | 
Xử lý

 | 
1
 | 
Chuỗi ký tự nhập vào là số, bắt đầu bằng số 0 và có độ dài = 10 ký tự
 | 
 | 
Truy vấn thông tin KH đăng ký dv Mobile Banking bằng SĐT nhập vào

2/ Hiển thị kết quả truy vấn

• 
Timeout: Trả kết quả timeout cho Client

• Không thành công:  | TT | Trường hợp | Nội dung thông báo | Xử lý (Nếu có)
 | 1 | Không có thông tin khách hàng hợp lệ = Trạng thái đăng ký MB khác các giá trị sau: Đã kích hoạt, Sai mật khẩu quá số lần, Chờ duyệt cập nhật thông tin, Chờ duyệt cấp lại mật khẩu | Không tìm thấy thông tin khách hàng sử dụng Co-opbank Mobile Banking bằng số điện thoại đã nhập. Vui lòng kiểm tra thông tin và thử lại! | Đóng thông báo quay về màn hình thao tác trước đó, giữ nguyên SĐT đã nhập
 | 2 | Không lấy được thông tin khách hàng | Lỗi gián đoạn. Vui lòng kiểm tra thông tin và thử lại! | Đóng thông báo quay về màn hình thao tác trước đó

• Thành công: Hiển thị thông tin Tên tài khoản+SĐT được nhận chia sẻ ra MH Đăng ký
 |   | Thao tác 4 | Tại <MH: Đăng ký>, KH chọn icon Danh bạ điện thoại
 | 
 | 
Hệ thống MB
 | 
1/ Kiểm tra quyền truy cập danh bạ của thiết bị. Tham khảo: . Nếu hợp lệ, truy cập vào danh bạ của thiết bị

2/ Kiểm tra danh bạ:

• Nếu danh bạ trống, hiển thị thông báo: Quý khách không có danh bạ để thực hiện chức năng này. Vui lòng kiểm tra thông tin và thử lại!
• Nếu danh bạ có dữ liệu: hiển thị <MH: Thêm thành viên - Chọn từ danh bạ>
3/ KH thực hiện:

• 
Nhập dữ liệu tìm kiếm (ô tìm kiếm chỉ hiển thị khi danh sách có từ 6 bản ghi trở lên)

• 
Cho tìm kiếm tương đối theo tên và SĐT có trong danh bạ

• 
Nếu không có kết quả, hiển thị: Không có kết quả tìm kiếm.

• 
Hiển thị nút "x" cho phép xóa toàn bộ ký tự trong ô

• 
Nhấn chọn/Bỏ chọn 1 hoặc nhiều danh bạ:

• Chỉ được chọn số lượng SĐT ứng với số tối đa cho phép
• 
Số lượng danh bạ đã chọn thay đổi theo thao tác của KH, +1 khi chọn thêm 1 danh bạ, -1 khi bỏ chọn 1 danh bạ

• Nếu số lượng SĐT đã tối đa thì không cho tích chọn thêm nữa
• 
Nhấn icon "X" → Đóng màn hình popup, về màn hình trước đó → những danh bạ được chọn/bỏ chọn vừa thao tác sẽ không có ở màn đăng ký

• 
Nhấn Xác nhận: Truy vấn thông tin KH đăng ký dv Mobile Banking từ các SĐT đã chọn

 |   | Thao tác 5 | Tại <MH: Thêm thành viên - Chọn từ danh bạ>, KH thực hiện
 | 
 | 
Hệ thống MB
 | 
• 
Nhập dữ liệu tìm kiếm (ô tìm kiếm chỉ hiển thị khi danh sách có từ 6 bản ghi trở lên)

• 
Cho tìm kiếm tương đối theo tên và SĐT có trong danh bạ

• 
Nếu không có kết quả, hiển thị: Không có kết quả tìm kiếm.

• 
Hiển thị nút "x" cho phép xóa toàn bộ ký tự trong ô

• 
Nhấn chọn/Bỏ chọn 1 hoặc nhiều danh bạ:

• Chỉ được chọn số lượng SĐT ứng với số tối đa cho phép
• 
Số lượng danh bạ đã chọn thay đổi theo thao tác của KH, +1 khi chọn thêm 1 danh bạ, -1 khi bỏ chọn 1 danh bạ

• Nếu số lượng SĐT đã tối đa thì không cho tích chọn thêm nữa
• 
Nhấn icon "X" → Đóng màn hình popup, về màn hình trước đó → những danh bạ được chọn/bỏ chọn vừa thao tác sẽ không có ở màn đăng ký

• 
Nhấn Xác nhận: Truy vấn thông tin KH đăng ký dv Mobile Banking từ các SĐT đã chọn

→ Hiển thị kết quả:

• 
Timeout: Trả kết quả timeout cho Client

• 
Không thành công: 
 | 
TT
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (Nếu có)

 | 
1
 | 
Thông tin khách hàng không hợp lệ = Trạng thái đăng ký MB khác các giá trị sau: Đã kích hoạt, Sai mật khẩu quá số lần, Chờ duyệt cập nhật thông tin, Chờ duyệt cấp lại mật khẩu
 | 
Không tìm thấy thông tin X/Y khách hàng sử dụng Co-opbank Mobile Banking bằng số điện thoại đã chọn. Vui lòng kiểm tra thông tin và thử lại!

(Có ít nhất 1 SĐT ko hợp lệ thì hiển thị thông báo chung như thế này, X = số lượng SĐT ko hợp lệ, Y = số lượng các SĐT đã chọn từ danh bạ)
 | 
Đóng thông báo quay về màn hình thao tác trước đó; Highlight các SĐT lỗi

 | 
2
 | 
Không lấy được thông tin khách hàng
 | 
Lỗi gián đoạn. Vui lòng kiểm tra thông tin và thử lại!
 | 
Đóng thông báo quay về màn hình thao tác trước đó

• 
Thành công: Hiển thị thông tin Tên tài khoản+SĐT hợp lệ được nhận chia sẻ ra <MH: Đăng ký>

 |   | Thao tác 6 | Tại <MH: Đăng ký>, KH chọn icon xóa ở các box TKTT & SĐT đã thêm
 | 
 | 
Hệ thống MB
 | 
Mất thông tin TKTT chia sẻ & SĐT nhận chia sẻ trên danh sách

 | 
 | 
Thao tác 7
 | 
Tại <MH: Đăng ký>, KH chọn sang tab khác (Đang chia sẻ, Chia sẻ với tôi)

 | 
 | 
Hệ thống MB
 | 
Hiển thị thông báo: Nếu quý khách rời khỏi tab này, thông tin đã thêm sẽ không được lưu lại!

• 
Chọn "Hủy": Quay về bước thao tác trước đó

• 
Chọn "Đồng ý": Clear dữ liệu đã nhập & hiển thị Tab KH đã chọn

 |   | Thao tác 8 | Tại <MH: Đăng ký>, KH chọn nút "Đăng ký"
 | 
 | 
Hệ thống MB
 | 
Kiểm tra thông tin đăng ký theo các nội dung sau:

• Không hợp lệ:  | 
TT
 | 
Trường hợp (Check riêng theo tưng trường hợp)
 | 
Nội dung thông báo (Thông báo chung)
 | 
Xử lý (Nếu có)

 | 
1
 | 
TKTT không hợp lệ
 | 
Tài khoản thanh toán không hợp lệ
 | 
Đóng thông báo quay về màn hình thao tác trước đó; Highlight các STK, SĐT lỗi

 | 
2
 | 
SĐT (nhập hoặc chọn từ danh bạ) trùng với SĐT của user đăng nhập
 | 
Số điện thoại của chủ tài khoản

 | 
3
 | 
SĐT chưa đăng ký dịch vụ Co-opBank Mobile Banking (Đã check được ở bước trước nhưng KH ko xóa đi)
 | 
Số điện thoại chưa đăng ký dịch vụ Co-opBank Mobile Banking

 | 
4
 | 
SĐT nhập vào trùng với SĐT chọn từ danh bạ
 | 
Số điện thoại bị trùng trong danh sách nhận chia sẻ

 | 
5
 | 
SĐT nhập vào trùng với SĐT đã được đăng ký nhận chia sẻ thông báo BĐSD (Trạng thái Đang chia sẻ hoặc Chờ xác nhận)
 | 
Số điện thoại đã được đăng ký nhận chia sẻ thông báo BĐSD

• Hợp lệ: Hiển thị <MH: Xác nhận giao dịch - đăng ký chia sẻ>

#### 3/ Xác nhận & xác thực giao dịch đăng ký chia sẻ
 | TT | Tác nhân | Mô tả
 | 
 | Thao tác 1 | Tại màn hình xác nhận đăng ký, KH kiểm tra thông tin đăng ký đã khởi tạo
 | 1 | Hệ thống MB | Hiển thị MH xác nhận như mô tả
 | 
 | Thao tác 2 | Tại màn hình xác nhận đăng ký, KH chọn nút "Xác nhận"
 | 2 | Hệ thống MB | 
1/ Xác thực giao dịch theo phương thức xác thực tương ứng: → Tham khảo logic xử lý tại Xác thực bằng Soft OTP, Xác thực GD bằng SMS OTP)

(Nếu xác thực bằng SMS OTP, nội dung SMS = Xac thuc dang ky chia se thong bao BDSD tren ung dung co ma OTP la 123456, co hieu luc trong 1 phut)

→ Nếu kết quả xác thực thành công: chuyển bước 2

2/ Kiểm tra danh sách chia sẻ thông báo BĐSD của KH 

• Nếu danh sách SĐT nhận chia sẻ trống:
• Cập nhật trạng thái chia sẻ của TKTT chia sẻ = Đã đăng ký (Lưu lại thao tác phục vụ báo cáo)
• Cập nhật trạng thái nhận tin chia sẻ của SĐT nhận chia sẻ = Chờ xác nhận (Lưu lại thao tác phục vụ báo cáo)
• Trả kết quả về cho Client 
• Nếu danh sách SĐT nhận chia sẻ có ít nhất 1 SĐT nhận chia sẻ:
• 
Gửi yêu cầu cập nhật trạng thái đăng ký chia sẻ nhận thông báo BĐSD của TKTT = Đã đăng ký sang Bank (Truyền accountNo ; primary_number - SĐT KH; record_stat=O - Trạng thái Mở)

• 
API: SMS_BankingSecnumber - Đăng ký chia sẻ thông tin biến động số dư 

 | 3 | Bank | 
• 
Cập nhật trạng thái đăng ký chia sẻ nhận thông báo BĐSD của TKTT = Đã đăng ký (accountNo - STK; primary_number - SĐT.A ; record_stat=O - Trạng thái Mở)

• 
Trả kết quả về cho App Server

 | 4 | Hệ thống MB | 
1/ Nhận kết quả từ Bank & xử lý: Cập nhật trạng thái chia sẻ của TKTT chia sẻ = Đã đăng ký (Lưu lại thao tác phục vụ báo cáo)

2/Trả kết quả về cho Client 

3/ Gửi yêu cầu bắn tin đến OTT Server cho SĐT nhận chia sẻ (Tham khảo: Tổng hợp nội dung OTT theo thao tác người dùng)

 | 5 | OTT Server | 
Gửi OTT cho SĐT được nhận chia sẻ

#### 4/ Kết quả đăng ký chia sẻ
 | TT | Tác nhân | Mô tả
 | 
 | Thao tác 1 | Tại <MH: Kết quả giao dịch - đăng ký chia sẻ>, KH chọn nút "Chia sẻ"
 | 1 | Hệ thống MB | Ứng dụng truy cập camera thiết bị và chụp ảnh màn hình kết quả và hiển thị chế độ chia sẻ ảnh mặc định của hệ điều hành để chia sẻ.Tham khảo cơ chế xử lý chung liên quan cấp quyền truy cập trên thiết bị: Client_Quy tắc nghiệp vụ chung
 | 
 | Thao tác 2 | Tại <MH: Kết quả giao dịch - đăng ký chia sẻ>, KH chọn nút "Lưu ảnh"
 | 1 | Hệ thống MB | Ứng dụng truy cập camera thiết bị và chụp ảnh màn hình kết quả giao dịch vào thư viện ảnh (Kiểm tra quyền lưu ảnh của thiết bị với ứng dụng)Tham khảo cơ chế xử lý chung liên quan cấp quyền truy cập trên thiết bị: Client_Quy tắc nghiệp vụ chung
 | 
 | Thao tác 3 | Tại <MH: Kết quả giao dịch - đăng ký chia sẻ>, KH chọn nút "Quản lý chia sẻ thông báo BĐSD"
 | 1 | Hệ thống MB | 
Điều hướng đến <MH: Đang chia sẻ>

#### 5/ Quản lý thông tin chia sẻ với tôi
 | TT | Tác nhân | Mô tả
 | 
 | 
Thao tác 1
 | 
Tại <MH: Chia sẻ với tôi - Chi tiết>-2, KH chọn nút "Từ chối"

 | 
1
 | 
Hệ thống MB
 | 
Hiển thị thông báo xác nhận: Quý khách có chắc chắn muốn từ chối nhận thông báo BĐSD được chia sẻ từ khách hàng [Tên tài khoản] ?

• 
Chọn "Hủy": Quay về bước thao tác trước đó

• 
Chọn "Đồng ý": cập nhật trạng thái nhận tin chia sẻ cho SĐT nhận chia sẻ = Từ chối 

• Không thành công: Hiển thị thông báo lỗi 
• | 
TT
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (Nếu có)

 | 
1
 | 

 | 
Từ chối nhận thông báo BĐSD được chia sẻ từ khách hàng [Tên tài khoản] không thành công.Vui lòng kiểm tra thông tin và thử lại!
 | 
Đóng thông báo quay về màn hình thao tác trước đó

• 
Thành công:

• Danh sách bản ghi ở Tab "Chia sẻ với tôi" được cập nhật
• 
G

> ⚠️ *Nội dung đã cắt ngắn (22082 ký tự gốc). Xem đầy đủ trên Confluence.*


---


## 34. VOICE OTT

> **Page ID:** `668209537` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/668209537

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*4 trang con:*

### 34.1. SOW chức năng Voice OTT

> **Page ID:** `668209553` · **Version:** 14
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/668209553

## 1/ Ý nghĩa chức năng

Tính năng Voice OTT sẽ phát thông báo bằng giọng nói qua loa điện thoại khi có BĐSD, giúp người dùng nhận thông tin ngay mà không cần mở màn hình điện thoại. 

Trong môi trường ồn ào hoặc khi cần âm lượng lớn, người dùng có thể kết nối với loa hoặc tai nghe Bluetooth để nhận thông báo rõ ràng hơn.

Để sử dụng tính năng này, người dùng cần tắt chế độ im lặng và cho phép ứng dụng gửi thông báo.

## 2/ Tóm tắt Usecase
 | Use Case Name | Voice OTT (Nhận biến động số dư bằng âm thanh)
 | Use Case ID | --
 | Use Case Description | 
Là người dùng, tôi muốn nhận thông báo biến động số dư của chính mình hoặc thông báo biến động số dư của người đã chia sẻ cho tôi trên ứng dụng CoopBank bằng âm thanh

 | Actor | 
KH, MB App, MB server, OTT server, OTT SDK voice

 | Priority | Medium
 | 
Trigger

(Sự kiện kích hoạt)
 | 
KH nhận được BĐSD cộng tiền vào tài khoản mình hoặc thông báo BĐSD cộng tiền vào tài khoản được được chia sẻ với mình

 | 
Pre-Condition

(Điều kiện trước)
 | 
• KH đã đăng ký dịch vụ nhận thông báo OTT BĐSD
• KH đã đăng ký nhận Voice OTT BĐSD cho số tài khoản có phát sinh BĐSD
• Thời gian nhận thông báo BĐSD nằm trong khoảng thời gian đăng ký nhận Voice OTT BĐSD
• Thiết bị của KH ở chế độ bình thường ( Không phải chế độ im lặng, không làm phiền)
 | 
Post-Condition

(Kết quả mong muốn)
 | 
KH nhận được Voice OTT BĐSD (Mỗi tin OTT BĐSD được phát 1 lần)

 | 
Bussiness Rule

(Quy tắc nghiệp vụ)
 | 
• KH cần phải đăng ký nhận thông báo OTT BĐSD trước khi đăng ký Voice OTT
• KH Hủy nhận thông báo OTT BĐSD sẽ tự động hủy đăng ký Voice OTT
• Chỉ phát Voice OTT cho loại giao dịch là Ghi có (cộng tiền)
• Với KH đã đăng ký Voice OTT, ngoài việc được nhận Voice OTT cộng tiền vào tài khoản của mình, KH còn nhận được Voice OTT cộng tiền vào tài khoản người khác đã chia sẻ với mình
• Mẫu template phát tin BĐSD chia sẻ và mẫu template  BĐSD của chính KH là 2 mẫu khác nhau 

## 3/ Luồng đăng ký Voice OTT

## Luồng hủy đăng ký

## Luồng push và phát tin Voice

### 4/ Mockup

### 5/ Phạm vi chức năng
 | 
 | Nhóm chức năng | Chức năng | Loại | Tác nhân | Mô tả cơ bản | Assign | Link
 | 1 | Thông báo OTT | 
Đăng ký Voice OTT
 | 
RedThêm mới
 | App/ MB server | 
Cho phép KH đăng ký nhận thông báo BĐSD bằng giọng nói. Thông tin đăng ký bao gồm:

• Tài khoản thanh toán đăng ký nhận Voice
• Khung giờ nhận Voice | 
Thảo Cy
 | 
 | 2 | 
Hủy đăng ký Voice OTT
 | 
RedThêm mới
 | App/ MB server | 
Cho phép KH hủy đăng ký nhận thông báo BĐSD bằng giọng nói.
 | 
Thảo Cy

 | 3 | 
 | 
Push  thông báo Voice
 | 
BlueCập nhật
 | MB server | 
MB server bổ sung logic:

- Kiểm tra loại giao dịch của KH: Ghi có mới phát Voice

- Kiểm tra KH đang đăng ký Voice OTT để truyền thêm thông tin đánh dấu KH đang đăng ký Voice cho Client
 | 
Thảo Cy
 | 
 | 4 | 
 | 
Phát thông báo Voice
 | 
RedThêm mới
 | App/ SDK OTT | 

 | 
Thảo Cy

 | 5 | Báo cáo | 
Báo cáo đăng ký Voice OTT
 | 
RedThêm mới
 | BO | 
Bổ sung sau
 | 

 | 

 | 6 | Quản lý user | 
Hủy đăng ký user
 | 
BlueCập nhật
 | BO | 
Hủy đăng ký user MB thì cập nhật Hủy tự động Voice OTT
 | 

 | 

 | 7 | Quản lý thông báo | 
Hủy đăng ký OTT BĐSD
 | 
BlueCập nhật
 | MB server | 
Hủy đăng ký OTT BĐSD thì cập nhật Hủy tự động Voice OTT
 | 

 |

---

### 34.2. Flow&Action screen - Đăng ký/Hủy đăng ký Voice OTT BĐSD

> **Page ID:** `679514265` · **Version:** 18
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/679514265

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThaoCY | 
 | 
Tạo mới tài liệu
 | 
V1.0.0

 | 
 
 | M | ThaoCY | V1.0.0 | 
Bổ sung chức năng Chỉnh sửa: Cho phép sửa tài khoản nhận voice và thời gian phát voice
 | 
V1.0.1

Mục lục

### 1/ Luồng màn hình

 

### 2/ Danh sách màn hình

#### 2.1/ Luồng đăng ký dịch vụ Voice OTT

##### MH1.1: Trang chủ

##### MH1.2: Cài đặt thông báo

##### MH1.3: Cài đặt

##### MH2.1: Cài đặt Voice OTT <trường hợp KH chưa đăng ký OTT BĐSD>

##### MH2.2: Cài đặt Voice OTT <trường hợp KH đã đăng ký OTT BĐSD, chưa đăng ký Voice OTT>

##### MH2.3: Cài đặt Voice OTT <chọn TK đọc thông báo>

##### MH2.4: Cài đặt Voice OTT <sau khi nhập đủ thông tin>

##### MH3.1: Xác thực bằng SMS OTP

##### MH3.2: Xác thực bằng Soft OTP

##### MH4: Đăng ký dịch vụ Voice OTT thành công

##### MH5: Cài đặt Voice OTT <trường hợp đã đăng ký Voice OTT>

#### 2.2/ Luồng hủy dịch vụ Voice OTT

##### MH5: Cài đặt Voice OTT <trường hợp đã đăng ký Voice OTT>

##### MH6: Popup xác nhận hủy dịch vụ Voice OTT

##### MH7.1: Xác thực bằng SMS OTP

##### MH7.2: Xác thực bằng Soft OTP

##### MH8: Hủy dịch vụ Voice OTT thành công

#### 2.3/ Luồng cập nhật cài đặt voice OTT BĐSD

##### MH9: Cập nhật cài đặt voice OTT

##### MH10.1: Xác thực bằng SMS OTP

##### MH10.2: Xác thực bằng Soft OTP

##### MH11: Cập nhật cài đặt voice OTT thành công

### 3/ Mô tả màn hình

##### MH1.1: Trang chủ

<Tham chiếu tài liệu >

##### MH1.2: Cài đặt thông báo
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Cài đặt thông báo
 | 2 | 
Cài đặt Voice OTT
 | Label | ReadOnly | -- | -- | 
<Mới bổ sung>

Hiển thị MH Cài đặt Voice OTT 

Tham khảo logic xử lý 

 | 3 | 
Quản lý chia sẻ thông báo BĐSD 
 | 
Label
 | 
Click
 | 
--
 | 
--
 | 
Hiển thị MH Quản lý chia sẻ thông báo BĐSD

Tham khảo mô tả tại: Flow & Action Screen_Chia sẻ thông báo OTT BĐSD

 | 4 | Quản lý thông báo | Label | Click | -- | -- | 
Hiển thị MH Quản lý thông báo

Tham khảo mô tả tại: Quản lý thông báo OTT (GÓI 2)

 | 5 | Xóa tất cả thông báo | Label | Click | -- | -- | 
Click vào hiển thị thông báo "Quý khách có chắc chắn muốn xóa thông báo này không"

##### MH1.3: Cài đặt

<Tham chiếu tài liệu , bổ sung thêm chức năng Cài đặt Voice OTT>

##### MH2.1: Cài đặt Voice OTT <trường hợp KH chưa đăng ký OTT BĐSD>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Thông báo
 | 2 | Nội dung | Label | ReadOnly | -- | -- | 
Fix tại client

Nội dung: "Quý khách vui lòng đăng ký nhận thông báo BĐSD trước đăng ký nhận thông báo BĐSD bằng giọng nói"

 | 3 | Đóng | Button | Click | -- | -- | 
Luôn enable

Click đóng popup, quay lại màn hình thao tác trước đó

 | 4 | Đồng ý | Button | Click | -- | -- | 
Điều hướng sang màn hình Quản lý thông báo 

<tham chiếu logic xử lý>

##### MH2.2: Cài đặt Voice OTT <trường hợp KH đã đăng ký OTT BĐSD, chưa đăng ký Voice OTT>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Cài đặt Voice OTT
 | 2 | Icon Back | Icon | Click | -- | -- | Click để quay lại màn hình trước đó
 | 3 | Giới thiệu | Label + Icon | ReadOnly | -- | -- | 
Fix tại client:

• Nội dung giới thiệu:
• Voice OTT là tính năng phát loa đọc thông báo BĐSD bằng giọng nói trên thiết bị di động khi tài khoản đã đăng ký của Quý khách được cộng tiền hoặc tài khoản chia sẻ của Quý khách được cộng tiền.
• Lưu ý: KHÔNG để thiết bị ở chế độ im lặng.
• Phí dịch vụ: Miễn phí
• Icon nghe thử, click phát voice nghe thử
 | 4 | Tài khoản đọc loa thông báo
 | 5 | Tiêu đề | Label | ReadOnly | -- | -- | 
Tài khoản đọc loa thông báo

 | 6 | Chọn tài khoản | Icon | Click | Yes | -- | 
Mặc định hiển thị Enable.

• Nếu không có TKTT hợp lệ: Chọn nút → mở popup thông báo: Quý khách không có tài khoản thanh toán hợp lệ để thực hiện chức năng này. Vui lòng kiểm tra lại.
• Nếu có TKTT hợp lệ: Chọn nút → mở popup Danh sách tài khoản đọc thông báo
 | 7 | Popup danh sách tài khoản đọc thông báo | 
 | 
 | 
 | -- | 
• Tiêu đề: Danh sách tài khoản đọc thông báo
• Ghi chú: "Quý khách có thể chọn nhiều tài khoản để nhận tin BĐSD bằng giọng nói"
• Danh sách tài khoản, bao gồm:
• Logo bank
• Số tài khoản
• Số dư: Số sư khả dụng + Đơn vị tiền tệ VNĐ
• Tích chọn (hiển thị khi ND bấm chọn vào TKTT, được chọn nhiều, mặc định chưa chọn
• Button: Xác nhận
 | 8 | Sau khi chọn tài khoản | Label+Icon | Click | -- | -- | 
Hiển thị danh sách tài khoản đã chọn, bao gồm:

• Logo bank
• Số tài khoản
Hiển thị icon cho phép loại bỏ tài khoản đã chọn khỏi danh sách

 | 9 | Khung giờ đọc loa thông báo
 | 10 | Tiêu đề | Label | ReadOnly | -- | -- | 
Khung giờ đọc loa thông báo

 | 11 | Ghi chú 1 | Label | ReadOnly | -- | -- | 
Fix tại client

Nội dung: "Ngoài khung giờ này, loa sẽ không phát thông báo BĐSD"

 | 12 | Từ  | Textbox | Number | No | -- | 
Mặc định để trống 

Cho phép chọn giờ

Định dạng: hh:mm

 | 13 | Đến | Textbox | Number | No | -- | 
Mặc định để trống 

Cho phép chọn giờ

Định dạng: hh:mm

 | 14 | Ghi chú 2 | Label | ReadOnly | -- | -- | 
Fix tại client

Nội dung: "Nếu bỏ trống khung giờ đọc loa, Quý khách sẽ được phát loa thông báo BĐSD không bị giới hạn thời gian."

 | 15 | 
Thao tác

 | 16 | Đăng ký | Button | Click | -- | --  | 
<tham chiếu logic xử lý>

##### MH3.1: Xác thực bằng SMS OTP

Hiển thị màn hình xác thực bằng SMS OTP với trường hợp:

• KH chưa cài đặt kích hoạt Soft OTP
• KH đã cài đặt kích hoạt Soft OTP nhưng chưa thực hiện đủ (n ) giao dịch bằng SMS OTP
<Tham chiếu tài liệu >

##### MH3.2: Xác thực bằng Soft OTP

Hiển thị màn hình xác thực bằng Soft OTP với trường hợp:

• KH đã đăng ký Soft OTP và đã thực hiện đủ (n ) giao dịch bằng SMS OTP
<Tham chiếu tài liệu >

##### MH4: Đăng ký dịch vụ Voice OTT thành công
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Thông báo
 | 2 | Nội dung | Label | ReadOnly | -- | -- | Quý khách đã đăng ký nhận thông báo BĐSD bằng giọng nói thành công
 | 3 | Đóng | Button | Click | -- | -- | 
Click hiển thị MH5: Cài đặt Voice OTT <trường hợp đã đăng ký Voice OTT>

<Tham khảo logic xử lý>

##### MH5: Cài đặt Voice OTT <trường hợp đã đăng ký Voice OTT>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Cài đặt Voice OTT
 | 2 | Icon Back | Icon | Click | -- | -- | Click để quay lại màn hình trước đó
 | 3 | Giới thiệu | Label + Icon | ReadOnly | -- | -- | 
Fix tại client:

• Nội dung giới thiệu:
• Voice OTT là tính năng phát loa đọc thông báo BĐSD bằng giọng nói trên thiết bị di động khi tài khoản đã đăng ký của Quý khách được cộng tiền hoặc tài khoản chia sẻ của Quý khách được cộng tiền.
• Lưu ý: KHÔNG để thiết bị ở chế độ im lặng.
• Phí dịch vụ: Miễn phí
• Icon nghe thử, click phát voice nghe thử
 | 4 | Nhận thông báo BĐSD bằng giọng nói | Toggle button | Click | -- | -- | 
Hiển thị trạng thái Đã đăng ký

Cho phép off button

Có ghi chú "Đã đăng ký" 

 | 5 | Thông tin cài đặt
 | 6 | Tiêu đề | Label | ReadOnly | -- | -- | 
Thông tin cài đặt

 | 7 | Danh sách tài khoản đăng ký | Label | ReadOnly | -- | -- | 
Hiển thị danh sách tài khoản đăng ký phát voice OTT

 | 8 | Thời gian thông báo | Label | ReadOnly | -- | -- | 
Hiển thị thời gian phát voice OTT

Định dạng: Từ hh:mm đến hh:mm

 | 9 | Thay đổi | Button | Click | - | - | 
Click để chỉnh sửa thông tin cài đặt voice OTT

<tham khảo logic xử lý>

##### MH8: Hủy dịch vụ Voice OTT thành công
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Thông báo
 | 2 | Nội dung | Label | ReadOnly | -- | -- | Nội dung: "Quý khách đã Hủy đăng ký nhận thông báo BĐSD bằng giọng nói thành công."
 | 3 | Đóng | Button | Click | -- | -- | 
Click hiển thị MH2: Cài đặt Voice OTT <trường hợp chưa đăng ký Voice OTT>

<Tham khảo logic xử lý>

##### MH9: Chỉnh sửa cài đặt voice OTT
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Cài đặt Voice OTT
 | 2 | Icon Back | Icon | Click | -- | -- | Click để quay lại màn hình trước đó
 | 3 | Giới thiệu | Label + Icon | ReadOnly | -- | -- | 
Fix tại client:

• Nội dung giới thiệu:
• Voice OTT là tính năng phát loa đọc thông báo BĐSD bằng giọng nói trên thiết bị di động khi tài khoản đã đăng ký của Quý khách được cộng tiền hoặc tài khoản chia sẻ của Quý khách được cộng tiền.
• Lưu ý: KHÔNG để thiết bị ở chế độ im lặng.
• Icon nghe thử, click phát voice nghe thử
 | 4 | Tài khoản đọc loa thông báo
 | 5 | Tiêu đề | Label | ReadOnly | -- | -- | 
Tài khoản đọc loa thông báo

 | 6 | Chọn tài khoản | Icon | Click | Yes | -- | 
Mặc định hiển thị Enable.

• Nếu không có TKTT hợp lệ: Chọn nút → mở popup thông báo: Quý khách không có tài khoản thanh toán hợp lệ để thực hiện chức năng này. Vui lòng kiểm tra lại.
• Nếu có TKTT hợp lệ: Chọn nút → mở popup Danh sách tài khoản đọc thông báo
 | 7 | Popup danh sách tài khoản đọc thông báo | 
 | 
 | 
 | -- | 
• Tiêu đề: Danh sách tài khoản đọc thông báo
• Ghi chú: "Quý khách có thể chọn nhiều tài khoản để nhận tin BĐSD bằng giọng nói"
• Danh sách tài khoản, bao gồm:
• Logo bank
• Số tài khoản
• Số dư: Số sư khả dụng + Đơn vị tiền tệ VNĐ
• Tích chọn (hiển thị khi ND bấm chọn vào TKTT, được chọn nhiều, mặc định chưa chọn
• Button: Xác nhận
 | 8 | Danh sách tài khoản đã chọn | Label+Icon | Click | -- | -- | 
Hiển thị danh sách tài khoản đã chọn, bao gồm:

• Logo bank
• Số tài khoản
Hiển thị icon cho phép loại bỏ tài khoản đã chọn khỏi danh sách

 | 9 | Khung giờ đọc loa thông báo
 | 10 | Tiêu đề | Label | ReadOnly | -- | -- | 
Khung giờ đọc loa thông báo

 | 11 | Ghi chú 1 | Label | ReadOnly | -- | -- | 
Fix tại client

Nội dung: "Ngoài khung giờ này, loa sẽ không phát thông báo BĐSD"

 | 12 | Từ  | Textbox | Number | No | -- | 
Mặc định hiển thị khung giờ đọc loa hiện tại, cho phép chỉnh sửa

Cho phép chọn giờ

Định dạng: hh:mm

 | 13 | Đến | Textbox | Number | No | -- | 
Mặc định hiển thị khung giờ đọc loa hiện tại, cho phép chỉnh sửa

Cho phép chọn giờ

Định dạng: hh:mm

 | 14 | Ghi chú 2 | Label | ReadOnly | -- | -- | 
Fix tại client

Nội dung: "Nếu bỏ trống khung giờ đọc loa, Quý khách sẽ được phát loa thông báo BĐSD không bị giới hạn thời gian."

 | 15 | 
Thao tác

 | 16 | Hủy | Button | Click | -- | --  | 
Luôn enable

<tham chiếu logic xử lý>

 | 17 | Lưu thay đổi | Button | Click | -- | --  | 
Luôn enable

<tham chiếu logic xử lý>

##### MH11: Cập nhật cài đặt voice OTT thành công
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Thông báo
 | 2 | Nội dung | Label | ReadOnly | -- | -- | Nội dung: "Quý khách đã cập nhật cài đặt nhận thông báo BĐSD bằng giọng nói thành công."
 | 3 | Đóng | Button | Click | -- | -- | 
Click hiển thị MH5: Cài đặt Voice OTT <trường hợp đã đăng ký Voice OTT>

<Tham khảo logic xử lý>

---

### 34.3. URD_Đăng ký/hủy đăng ký Voice OTT

> **Page ID:** `681279583` · **Version:** 26
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/681279583

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Thời gian cập nhật
 | 
  
 | A | ThảoCY | 
 | 
Tạo mới
 | V1.0.1 | 

 | 
 
 | M | ThaoCY | V1.0.1 | 
• Bỏ logic cache trạng thái voiceOTT tại client khi truy cập chức năng, khi đăng ký và hủy đăng ký
• MB server trả thêm trường autoRegisOtt tại mid 530 | V1.0.1 | 

 | 
 
 | M | ThaoCY | V1.0.1 | Bổ sung chức năng Chỉnh sửa: Cho phép chỉnh sửa tài khoản nhận voice và thời gian phát voice | V1.0.2 | 

Mục lục

### 1/ Mô tả Usecase
 | Use Case Name: | Đăng ký/hủy đăng ký dịch vụ Voice OTT (Nhận biến động số dư bằng âm thanh)
 | Use Case ID: | UC_VOICEOTT_01
 | Use Case Description: | 
Là người dùng, tôi muốn đăng ký/ hủy đăng ký dịch vụ nhận thông báo biến động số dư bằng âm thanh (Voice OTT)

 | Actor: | 
KH, MB Client MB server, Bank

 | Priority: | Medium 
 | Trigger: | 
Khách hàng đăng ký/Hủy đăng ký Voice OTT

 | Pre-Condition | 
1/ KH đã đăng ký dịch vụ nhận thông báo OTT BĐSD

 | Post-Condition: | 
KH đăng ký thành công/ hủy thành công dịch vụ Voice OTT

 | Basic Flow: | 
1/ KH đăng nhập thành công ứng dụng 

2/ KH nhấn chọn icon "Thông báo" tại màn hình Home, sau đó chọn "Cài đặt" tại màn hình Thông báo → Ứng dụng hiển thị popup Cài đặt

3/ Chọn "Cài đặt Voice OTT" → Ứng dụng hiển thị màn hình Cài đặt Voice OTT (với điều kiện KH đã đăng ký nhận tin OTT BĐSD)

Luồng đăng ký dịch vụ Voice OTT BĐSD:

4.1/ KH chọn/nhập các thông tin, sau đó chọn "Đăng ký ngay"

5/1/ KH thực hiện xác thực  → Ứng dụng cập nhật trạng thái đăng ký Voice OTT BĐSD của KH, quay lại màn hình Cài đặt Voice OTT với trạng thái Đã đăng ký

Luồng hủy dịch vụ Voice OTT BĐSD:

4.2/ KH chọn off toggle button tại màn hình Cài đặt Voice OTT

5.2/ KH thực hiện xác thực → Ứng dụng cập nhật trạng thái đăng ký Voice OTT BĐSD của KH và hiển thị màn hình đăng ký Voice OTT BĐSD

 | Alternative Flow: | 
1/ KH đăng nhập thành công ứng dụng 

2/ KH chọn chức năng "Cài đặt" tại màn hình Home → Ứng dụng hiển thị màn hình Cài đặt

3/ Chọn "Cài đặt Voice OTT" → Ứng dụng hiển thị màn hình Cài đặt Voice OTT (với điều kiện KH đã đăng ký nhận tin OTT BĐSD)

Luồng đăng ký dịch vụ Voice OTT BĐSD:

4.1/ KH chọn/nhập các thông tin, sau đó chọn "Đăng ký ngay"

5/1/ KH thực hiện xác thực  → Ứng dụng cập nhật trạng thái đăng ký Voice OTT BĐSD của KH, quay lại màn hình Cài đặt Voice OTT với trạng thái Đã đăng ký

Luồng hủy dịch vụ Voice OTT BĐSD:

4.2/ KH chọn off toggle button tại màn hình Cài đặt Voice OTT

5.2/ KH thực hiện xác thực → Ứng dụng cập nhật trạng thái đăng ký Voice OTT BĐSD của KH và hiển thị màn hình đăng ký Voice OTT BĐSD

 | Exception Flow: | 
1/ KH chưa đăng ký dịch vụ OTT BĐSD trước đó

 | Bussiness Rules: | 
1/ KH cần phải đăng ký nhận thông báo OTT BĐSD trước khi đăng ký Voice OTT

2/ KH Hủy nhận thông báo OTT BĐSD sẽ tự động hủy đăng ký Voice OTT

3/ Khi hủy user MB sẽ tự động hủy đăng ký Voice OTT

 | Non-Funtional Requiremnt: | 
 --

### 2/ Luồng sơ đồ

#### 2.1/ Luồng đăng ký Voice OTT BĐSD

#### 2.2/ Luồng hủy đăng ký Voice OTT

### 3/ Luồng xử lý

#### 3.1/ Luồng đăng ký Voice OTT BĐSD

##### Truy cập chức năng (MH1.2: Cài đặt thông báo/ MH1.3: Cài đặt)
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn "Cài đặt Voice OTT" | MB Client | 
1/ Kiểm tra trong bộ nhớ Cache của MB Client có lưu thông tin cài đặt Voice OTT không?

• Nếu đã có thông tin → Hiển thị MH Cài đặt Voice OTT tùy trạng thái đăng ký 
• Nếu đã đăng ký: Hiển thị MH5
• Nếu chưa đăng ký: Hiển thị MH2.2
• Nếu chưa có thông tin → Chuyển sang 3
Gửi yêu cầu kiểm tra trạng thái đăng ký Voice OTT đến MB server qua mid530
Input
• mobileNo
 | 2 | 
 | MB server | 
Truy vấn trạng thái Voice OTT và và trả kết quả về cho CLient
Output
• mobileNo
• ottVoiceStatus: Trạng thái Voice OTT
• account: Tài khoản đọc thông báo 
• startTime: giá trị "Từ" của khung thời gian đọc thông báo 
• endTime: giá trị "Đến" của khung thời gian đọc thông báo
• autoRegisOtt: Trạng thái đăng ký OTT BĐSD 
 | 3 | 
 | MB Client | 
1/ Nhận kết quả

• Không thành công: Hiển thị thông báo lỗi tương ứng do MB server trả
• Thành công:
• 
• 
1/ Kiểm tra trạng thái đăng ký dịch vụ OTT (dựa vào trường autoRegisOtt do MB server trả về tại mid530)

• Nếu autoRegisOtt=OFF → Hiển thị thông báo: "Quý khách vui lòng đăng ký nhận thông báo BĐSD trước đăng ký nhận thông báo BĐSD bằng giọng nói"
• Chọn "Đóng": Tắt popup, hiển thị màn hình thao tác trước đó
• Chọn "Đồng ý": Điều hướng đến màn hình Quản lý thông báo với trạng thái đăng ký dịch vụ OTT tương ứng <tham chiếu tài liệu >. Sau khi đăng ký dịch vụ OTT BĐSD thành công, hiển thị màn hình Quản lý thông báo với trạng thái Đã đăng ký (Lưu ý: Không điều hướng đến luồng đăng ký Voice OTT)
• Nếu autoRegisOtt=ON → Chuyển sang 2
• 2/ Hiển thị MH Cài đặt Voice OTT tùy trạng thái đăng ký 
• Nếu đã đăng ký: Hiển thị MH5
• Nếu chưa đăng ký: Hiển thị MH2.2
• 3/ Thực hiện lưu cache thông tin cài đặt Voice OTT BĐSD vào bộ nhớ của Client, các thông tin lưu bao gồm:

• mobileNo
• ottVoiceStatus
• account
• startTime
• endTime

##### MH2.1+2.2+2.3: Cài đặt Voice OTT 
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Click Icon Back | MB Client | Quay lại màn hình thao tác trước đó
 | 2 | Click icon "Nghe thử" | MB Client | Phát audio đã fix sẵn (Do SDK gửi nội dung)
 | 3 | Chọn Tài khoản đọc loa thông báo | MB Client | Gửi yêu cầu lấy danh sách tài khoản thanh toán đến MB server qua mid7
 | 4 | 
 | MB server | Gửi yêu cầu lấy danh sách tài khoản thanh toán sang Bank
 | 5 | 
 | Bank | Truy vấn danh sách tài khoản thanh toán và trả MB server
 | 6 | 
 | MB server | Nhận kết quả lấy danh sách tài khoản thanh toán và phản hồi lại Client
 | 7 | 
 | MB Client | 
1/ Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng 
• Thành công: Hiển thị popup Danh sách tài khoản đọc thông báo
 | 8 | Chọn 1 hoặc nhiều tài khoản đọc thông báo, sau đó chọn "Xác nhận"  | MB Client | 
Tắt popup Danh sách tài khoản đọc thông báo

Hiển thị danh sách tài khoản được chọn, bao gồm

• Logo bank
• Số tài khoản
• Icon "-" cho phép loại bỏ tài khoản
 | 9 | Nhập giá trị Từ và Đến tại ô Khung giờ đọc loa thông báo | MB Client | 
Hiển thị đúng giá trị KH đã nhập tại mỗi ô

 | 10 | Nhấn "Đăng ký ngay" | MB Client | 
1/ Thực hiện kiểm tra giá trị KH đã nhập

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | Bỏ trống Tài khoản đọc loa thông báo | Quý khách vui lòng chọn Tài khoản đọc loa thông báo. | 

 | Chỉ nhập Từ/ Đến (bỏ trống 1 trong 2 trường) | Quý khách vui lòng nhập đủ thông tin khung giờ đọc loa thông báo hoặc để trống cả 2 trường. | 

 | Nếu giá trị thời gian tại ô Từ lớn hơn giá trị thời gian tại ô Đến | Thời gian đọc thông báo không hợp lệ, giá trị Đến phải lớn hơn giá trị Từ. Quý khách vui lòng thực hiện lại. | 

• Hợp lệ: Gửi yêu cầu đăng ký dịch vụ Voice OTT BĐSD đến MB server qua mid531Input
• mobileNo
• ottVoiceStatus: ON/OFF
• listAccount
• startTime: Nếu không nhập thì truyền null
• endTime: Nếu không nhập thì truyền null
• type: 1-đăng ký, 0-Hủy, 3-Cập nhật
 | 11 | 
 | MB server | 
1/ Kiểm tra trạng thái Soft OTP của user

• Nếu KH đã kích hoạt Soft OTP → Chuyển sang 2
• Nếu KH chưa kích hoạt Soft OTP → Server xác định PTXT là SMS OTP 
2/ Kiểm tra số lần giao dịch xác thực bằng SMS OTP thành công trước đó

• Nếu số lần xác thực SMS OTP < (n ) → Server xác định PTXT là SMS OTP
• Nếu số lần xác thực SMS OTP >= (n ) → Server xác định PTXT ưu tiên nhất so Server trả về là Soft OTP → Chuyển bước xác thực bằng Soft OTP 
• Nếu trạng thái Soft OTP = Lock/AutoLock → Server xác định PTXT là SMS OTP 
(Tham khảo Logic xác định PTXT của GD phi tài chính tại Logic kiểm tra chung Hạn mức, PTXT, Phí dịch vụ)

{n} là số lần xác thực SMS OTP trước khi xác thực bằng Soft OTP

 | 12 | 
 | MB Client | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng
• Thành công: Hiển thị màn hình xác thực với PTXT tương ứng do MB server trả

##### MH: Xác thực giao dịch (MH3.1: Xác thực bằng SMS OTP + MH3.2: Xác thực bằng Soft OTP)
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Nhập OTP và chọn "Xác nhận" | MB client | 
Thực hiện xác thực giao dịch

• Nếu PTXT là SMS OTP: tham chiếu tài liệu 
(Nếu xác thực bằng SMS OTP, nội dung SMS = Xac thuc dang ky voice OTT co ma OTP là 123456, co hieu luc trong 1 phut)

• Nếu PTXT là Soft OTP: tham chiếu tài liệu 
Validate thông tin:

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng 
• Hợp lệ: Gửi yêu cầu xác nhận đăng ký Voice OTT đến MB server qua mid532
 | 2 | 
 | MB server | 
Kiểm tra OTP:

• Không hợp lệ: Trả kết quả lỗi cho MB Client
• Nếu PTXT là SMS OTP: tham chiếu tài liệu 
• Nếu PTXT là Soft OTP: tham chiếu tài liệu 
• Hợp lệ: 
• 1/ Thực hiện cập nhật giá trị đăng ký thông báo Voice OTT BĐSD của khách hàng 
• Nếu trong bảng đã có thông tin userID của KH → thực hiện update thông tin cài đặt và chuyển 2
• Nếu trong bảng chưa có thông tin userID của KH → thực hiện insert thông tin cài đặt và chuyển 2
• 2/ Trả kết quả cho MB client
 | 3 | 
 | MB Client | 
1/ Nhận kết quả

• Không thành công: Hiển thị thông báo lỗi do MB server trả về
• Thành công: Chuyển sang 2
2/ Lưu thông tin vào cache của client và chuyển sang 3

2/ Hiển thị popup thông báo đăng ký dịch vụ thành công: "Quý khách đã đăng ký nhận thông báo BĐSD bằng giọng nói thành công."

##### MH4: Đăng ký dịch vụ Voice OTT thành công
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn "Đóng" | MB Client | Đóng popup, hiển thị MH5

#### 3.2/ Luồng hủy đăng ký Voice OTT BĐSD

##### Truy cập chức năng

<Tương tự luồng đăng ký Voice OTT BĐSD>

##### MH5: Cài đặt Voice OTT <trường hợp đã đăng ký Voice OTT>
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Click off toggle button và chọn Đồng ý | MB Client | 
Gửi yêu cầu hủy đăng ký dịch vụ Voice OTT đến MB server qua mid531 (chung mid với mid đăng ký Voice OTT)
Input
• mobileNo
• ottVoiceStatus: ON/OFF
• account: Không truyền với trường hợp hủy cài đặt
• startTime: Không truyền với trường hợp hủy cài đặt
• endTime: Không truyền với trường hợp hủy cài đặt
• type: 1-đăng ký, 0-Hủy, 3-Cập nhật
 | 2 | 
 | MB server | 
1/ Kiểm tra trạng thái Soft OTP của user

• Nếu KH đã kích hoạt Soft OTP → Chuyển sang 2
• Nếu KH chưa kích hoạt Soft OTP → Server xác định PTXT là SMS OTP 
2/ Kiểm tra số lần giao dịch xác thực bằng SMS OTP thành công trước đó

• Nếu số lần xác thực SMS OTP < (n ) → Server xác định PTXT là SMS OTP
• Nếu số lần xác thực SMS OTP >= (n ) → Server xác định PTXT ưu tiên nhất so Server trả về là Soft OTP → Chuyển bước xác thực bằng Soft OTP 
• Nếu trạng thái Soft OTP = Lock/AutoLock → Server xác định PTXT là SMS OTP 
(Tham khảo Logic xác định PTXT của GD phi tài chính tại Logic kiểm tra chung Hạn mức, PTXT, Phí dịch vụ)

{n} là số lần xác thực SMS OTP trước khi xác thực bằng Soft OTP

 | 3 | 
 | MB Client | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng
• Thành công: Hiển thị màn hình xác thực với PTXT tương ứng do MB server trả

##### MH: Xác thực giao dịch (MH7.1: Xác thực bằng SMS OTP + MH7.2: Xác thực bằng Soft OTP)
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Nhập OTP và chọn "Xác nhận" | MB client | 
Thực hiện xác thực giao dịch

• Nếu PTXT là SMS OTP: tham chiếu tài liệu 
(Nếu xác thực bằng SMS OTP, nội dung SMS = Xac thuc huy dang ky voice OTT co ma OTP là 123456, co hieu luc trong 1 phut)

• Nếu PTXT là Soft OTP: tham chiếu tài liệu 
Validate thông tin:

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng 
• Hợp lệ: Gửi yêu cầu xác nhận hủy đăng ký Voice OTT đến MB server qua mid532 (chung mid với mid xác nhận đăng ký Voice OTT)
 | 2 | 
 | MB server | 
Kiểm tra OTP:

• Không hợp lệ: Trả kết quả lỗi cho MB Client
• Nếu PTXT là SMS OTP: tham chiếu tài liệu 
• Nếu PTXT là Soft OTP: tham chiếu tài liệu 
• Hợp lệ: 
• 1/ Thực hiện cập nhật trạng thái đăng ký thông báo Voice OTT BĐSD của khách hàng 
• 2/ Trả kết quả cho MB client
 | 3 | 
 | MB Client | 
1/ Nhận kết quả

• Không thành công: Hiển thị thông báo lỗi do MB server trả về
• Thành công: Chuyển sang 2
2/ Lưu thông tin vào cache của client và chuyển sang 3

2/ Hiển thị popup thông báo đăng ký dịch vụ thành công: "Quý khách đã Hủy đăng ký nhận thông báo BĐSD bằng giọng nói thành công."

##### MH8: Hủy dịch vụ Voice OTT thành công
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn "Đóng" | MB Client | Đóng popup, hiển thị MH2.2

#### 3.3/ Luồng cập nhật cài đặt voice OTT BĐSD

##### Truy cập chức năng

<Tương tự luồng đăng ký Voice OTT BĐSD>

##### MH5: Cài đặt Voice OTT <trường hợp đã đăng ký Voice OTT>
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn "Thay đổi" | MB Client | Hiển thị màn hình Cập nhật cài đặt voice OTT

##### MH9: Cập nhật cài đặt voice OTT
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Click Icon Back | MB Client | Quay lại màn hình thao tác trước đó
 | 2 | Click icon "Nghe thử" | MB Client | Phát audio đã fix sẵn (Do SDK gửi nội dung)
 | 3 | Chọn Tài khoản đọc loa thông báo | MB Client | Gửi yêu cầu lấy danh sách tài khoản thanh toán đến MB server qua mid7
 | MB server | Gửi yêu cầu lấy danh sách tài khoản thanh toán sang Bank
 | Bank | Truy vấn danh sách tài khoản thanh toán và trả MB server
 | MB server | Nhận kết quả lấy danh sách tài khoản thanh toán và phản hồi lại Client
 | MB Client | 
1/ Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng 
• Thành công: Hiển thị popup Danh sách tài khoản đọc thông báo
 | 4 | Chọn 1 hoặc nhiều tài khoản đọc thông báo, sau đó chọn "Xác nhận"  | MB Client | 
Tắt popup Danh sách tài khoản đọc thông báo

Hiển thị danh sách tài khoản được chọn, bao gồm

• Logo bank
• Số tài khoản
• Icon "-" cho phép loại bỏ tài khoản
 | 5 | Chỉnh sửa giá trị Từ và Đến tại ô Khung giờ đọc loa thông báo | MB Client | 
Hiển thị đúng giá trị KH đã nhập tại mỗi ô

 | 6 | Nhấn "Hủy" | MB Client | 
Không lưu các thông tin vừa cập nhật 

Quay lại màn hình MH5

 | 7 | Nhấn "Lưu thay đổi" | MB Client | 
1/ Thực hiện kiểm tra giá trị KH đã nhập

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | Bỏ trống Tài khoản đọc loa thông báo | Quý khách vui lòng chọn Tài khoản đọc loa thông báo. | 

 | Chỉ nhập Từ/ Đến (bỏ trống 1 trong 2 trường) | Quý khách vui lòng nhập đủ thông tin khung giờ đọc loa thông báo hoặc để trống cả 2 trường. | 

 | Nếu giá trị thời gian tại ô Từ lớn hơn giá trị thời gian tại ô Đến | Thời gian đọc thông báo không hợp lệ, giá trị Đến phải lớn hơn giá trị Từ. Quý khách vui lòng thực hiện lại. | 

 | Nếu thông tin không thay đổi gì so với thông tin hiện tại | Thông tin không thay đổi so với thông tin hiện tại. Quý khách vui lòng kiểm tra lại.  | 

• Hợp lệ: Gửi yêu cầu cập nhật cài đặt  Voice OTT BĐSD đến MB server qua mid531Input
• mobileNo
• ottVoiceStatus: ON/OFF
• listAccount
• startTime: Nếu không nhập thì truyền null
• endTime: Nếu không nhập thì truyền null
• type: 1-đăng ký, 0-Hủy, 3-Cập nhật
 | MB server | 
1/ Kiểm tra trạng thái Soft OTP của user

• Nếu KH đã kích hoạt Soft OTP → Chuyển sang 2
• Nếu

> ⚠️ *Nội dung đã cắt ngắn (17111 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 34.4. User Action Flow_Push tin Voice OTT (Bank)

> **Page ID:** `682103334` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/682103334

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Thời gian cập nhật
 | 
  
 | A | ThảoCY | 
 | 
Tạo mới
 | V1.0.0 | 

Mục lục

### 1/ Mô tả Usecase
 | Use Case Name: | Voice OTT (Nhận biến động số dư bằng âm thanh)
 | Use Case ID: | UC_VOICEOTT_01
 | Use Case Description: | 
Là người dùng, tôi muốn nhận thông báo biến động số dư của chính mình hoặc thông báo biến động số dư của người đã chia sẻ cho tôi trên ứng dụng CoopBank bằng âm thanh

 | Actor: | 
KH, Bank, MB server, Hệ thống OTT, MB client

 | Priority: | Medium 
 | Trigger: | 
KH nhận được BĐSD cộng tiền vào tài khoản mình hoặc thông báo BĐSD cộng tiền vào tài khoản được được chia sẻ với mình

 | Pre-Condition | 
1/ KH đã đăng ký dịch vụ nhận thông báo OTT BĐSD

2/ KH đã đăng ký nhận Voice OTT BĐSD cho số tài khoản có phát sinh BĐSD

3/ Thời gian nhận thông báo BĐSD nằm trong khoảng thời gian đăng ký nhận Voice OTT BĐSD

4/ Thiết bị của KH ở chế độ bình thường ( Không phải chế độ im lặng, không làm phiền)

 | Post-Condition: | 
KH nhận được Voice OTT BĐSD (Mỗi tin OTT BĐSD được phát 1 lần)

 | Basic Flow: | 
1/ KH có phát sinh BĐSD

2/ Bank kiểm tra trạng thái đăng ký nhận thông báo OTT BĐSD và trạng thái chia sẻ BĐSD của KH, thực hiện bắn tin OTT BĐSD theo nghiệp vụ hiện tại

3/ MB server MB kiểm tra loại giao dịch

• Nếu là giao dịch ghi nợ/ KH không đăng ký Voice OTT: Thực hiện theo luồng hiện tại 
• Nếu là giao dịch ghi có và KH có đăng ký Voice OTT: Thực hiện như luồng hiện tại + truyền thêm rawdata sang OTT server
4/ Hệ thống OTT truyền tin đến hệ thống MB

5/ MB Client kiểm tra thông tin đọc voice và thực hiện phát voice theo quy định

 | Alternative Flow: | 
--

 | Exception Flow: | 
1/ KH chưa đăng ký dịch vụ OTT thành công trước đó

2/ KH thực hiện lấy thông tin đăng ký Dịch OTT không thành công

 | Bussiness Rules: | 
1/ KH cần phải đăng ký nhận thông báo OTT BĐSD trước khi đăng ký Voice OTT

2/ KH Hủy nhận thông báo OTT BĐSD sẽ tự động hủy đăng ký Voice OTT

3/ Khi hủy user MB sẽ tự động hủy đăng ký Voice OTT

4/ Chỉ phát Voice OTT cho loại giao dịch là Ghi có (cộng tiền)

5/ Với KH đã đăng ký Voice OTT, ngoài việc được nhận Voice OTT cộng tiền vào tài khoản của mình, KH còn nhận được Voice OTT cộng tiền vào tài khoản người khác đã chia sẻ với mình

6/ Mẫu template phát tin BĐSD chia sẻ và mẫu template  BĐSD của chính KH giống nhau: Bạn đã nhận [số tiền] đồng

7/ Điều kiện thiết bị: Thiết bị đã bật thông báo bằng âm thanh

 | Non-Funtional Requiremnt: | 
 --

### 2/ Luồng sơ đồ

trueUntitled Diagram-1742294365273falseautotoptrue157111411

### 3/ Luồng xử lý
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Khi có phát sinh BĐSD | Bank | 
Kiểm tra trạng thái đăng ký OTT BĐSD và trạng thái đăng ký chia sẻ BĐSD của KH và thực hiện push tin OTT theo nghiệp vụ hiện tại

• KH không đăng ký OTT BĐSD → Không push tin OTT BĐSD
• KH có đăng ký OTT BĐSD và không đăng ký chia sẻ BĐSD → Push 1 bản tin gốc
• KH có đăng ký OTT BĐSD và đăng ký chia sẻ BĐSD → Push 1 bản tin gốc và 1 bản tin chia sẻ
 | 2 | 
 | MB server | 
1/ Kiểm tra loại giao dịch (ghi nợ/ghi có) ở cả Bản tin gốc và Bản tin chia sẻ (nếu có)

• Nếu là giao dịch ghi nợ: Push tin OTT BĐSD theo nghiệp vụ hiện tại (không phát Voice OTT)
• Nếu là giao dịch ghi có: Chuyển sang 2
2/  Kiểm tra: Kiểm tra trạng thái đăng ký voice OTT

Với bản tin gốc (type=16): 

• Nếu không đăng ký Voice OTT→ Push tin OTT BĐSD theo nghiệp vụ hiện tại
• Nếu có đăng ký voice OTT → Push tin BĐSD theo nghiệp vụ hiện tại và bổ sung truyền thêm thông tin vào rawdata sang hệ thống OTT. Rawdata truyền theo cấu trúc:
• typeVoice: mặc định giá trị = 1
• text: Truyền vào số tiền
• templateID: Mã của Template đọc tin 
• timeperiod (startTime; endTime): khoảng thời gian đọc tin
Với bản tin chia sẻ (type=304): 

• Dựa vào mobile trong tin OTT bank trả, truy vấn lấy danh sách số điện thoại được được chia sẻ OTT <tham chiếu tài liệu >
• Kiểm tra các số điện thoại đó có được đăng ký voice OTT không
• Nếu không đăng ký Voice OTT→ Push tin OTT BĐSD theo nghiệp vụ hiện tại
• Nếu có đăng ký voice OTT → Push tin BĐSD theo nghiệp vụ hiện tại và bổ sung truyền thêm thông tin vào rawdata sang hệ thống OTT (tương tự với bản tin gốc)
 | 3 | 
 | Hệ thống OTT | Nhận và thực hiện push tin theo nghiệp vụ hiện tại
 | 4 | 
 | MB Client | 
Nhận và check cài đặt để xử lý đọc tin theo cấu trúc đã fix (prefix: Bạn đã nhận; subfix: rỗng)

• Nếu cài đặt của thiết bị là Im lặng/Không làm phiền → Không đọc voice
• Nếu cài đặt của thiết bị là bình thường → Xử lý check thời gian hiện tại có nằm trong khung giờ của timeperiod (startTime; endTime) không (Trường hợp không có Timeperiod hoặc giá trị = null/ rỗng → Luôn đọc tin, không cần check thời gian)
• Nếu thời gian hiện tại nằm ngoài khung giờ đọc tin → Không đọc voice
• Nếu thời gian hiện tại nằm trong khung giờ đọc tin: Thực hiện đọc voice
• Đọc voice theo âm lượng cài đặt của thiết bị (Lưu ý đối với HĐH IOS trường hợp outapp không check được âm lượng của thiết bị, nên sẽ đọc theo âm lượng mặc định)
• Đọc trường Text → Đọc số tiền + Đơn vị là "đồng". Dựa vào thông tin prefix và subfix để thực hiện ghép audio theo cấu trúc: "prefix"  (Nếu có) + text  + "suffix"  (Nếu có). Ví dụ:
• prefix = audio "Bạn đã nhận"
• Text = 50000
• subfix = rỗng
• Câu đầy đủ: Bạn đã nhận năm mươi nghìn đồngLưu ý
Hệ thống đánh dấu tin nào là tin load lại sẽ không thực hiện tạo và phát voice OTT nữa

---


