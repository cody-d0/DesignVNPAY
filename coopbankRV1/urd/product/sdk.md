# 📋 Mobile SDK

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `product/`
> **Trích xuất:** 2026-03-28

---

## 18. URD_MB_SDK

> **Page ID:** `83866103` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/83866103

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*11 trang con:*

### 18.1. QUY TẮC CHUNG TÍCH HỢP JSON CHO CÁC DỊCH VỤ SDK (CLIENT)

> **Page ID:** `633800845` · **Version:** 15
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/633800845

#### I/ Quy tắc chung

#### 1. Mục đích

Do 1 App Client có thể tích hợp nhiều dịch vụ SDK, nên nhằm chuẩn hóa Output của tất cả các SDK trả cho App Client → Các SDK sẽ quy định, và trả về cho App Clien theo format chung dạng chuỗi Json

• Ưu điểm: Các thông tin hiển thị hiển thị động theo cấu hình SDK trả về. Khi có sự thay đổi về việc thêm/ bớt trường thông tin của SDK chỉ cần cấu hình thêm/ bớt tương ứng tại SDK mà không cần phải Update App
• Nhược điểm: Hạn chế về việc hiển thị icon theo các trường thông tin ( do icon khó trả về trong Json)
#### 2. Mô tả

 Các SDK trả về Format Json chung như sau:

• Nhóm 1 - bankInput: Thông tin dùng cho Client truyền cho MB server trong API khởi tạo thanh toán, gồm: Service code, Provide Code, Customer Code 
          (Note: Đối với các SDK ko tích hợp Json thì các thông tin này đang phải fix tại Client khi truyền cho MB server)

• Nhóm 2 - payment: Thông tin dùng ở màn hình Kết quả giao dịch thành công Hoặc những giá trị nhỏ ở màn hình khởi tạo thanh toán ngoài các trường trong nhóm 3 OrderInfor
Lưu ý: Với các trường có value số tiền = 0, SDK JSON trả về = 0 →  App client vẫn hiển thị = 0 (App Client không xử lý ẩn được do Json tương ứng theo biến title, value và type nên Client không xác định được trường nào để ẩn)

Ví dụ: 

        - Nội dung câu ghi chú nhắc KH nếu trong vòng 30p không nhận được vé thì gọi tổng đài xxxx hiển thị tại MH kết quả giao dịch

        - Tên nhà cung cấp hiển thị tại MH kết quả giao dịch (theo yêu cầu của từng dịch vụ SDK)

• Nhóm 3 - orderInfor: Thông tin đơn hàng hiển thị màn hình khởi tạo thanh toán của App Client gồm:
       - Tên nhóm trường (Type = GROUP): VD nhóm Thông tin thanh toán, Thông tin khách hàng, Thông tin hành trình

       - Tên trường (Type = TITLE_VALUE, title )

       - Tên trường (Type = value)

 | 1 | Vé xem phim | MidnightJson VI - TEMPLATEtruetrue không hiển thị button xuất hóa đơn tại bank
 "customerName": "Nguyễn Văn A",// Tên khách hàng
 "serviceName": "Đặt vé xem phim",// Client bank lấy để hiển thị tại màn hình kết quả thanh toán
 "supplierName": "Công ty TNHH CJ CGV Việt Nam"// Tên rạp chiếu phim theo ngôn ngữ main app, Client bank lấy để hiển thị tại màn hình kết quả thanh toán
    "note": "Lưu ý: Mã xác nhận sẽ được gửi về email và số điện thoại liên hệ đăng ký khi đặt dịch vụ. Trong 30 phút sau khi thanh toán thành công Qúy khách hàng không nhận được thông tin vui lòng liên hệ tổng đài *6789 để được hỗ trợ.",// Câu note để hiển thị tại màn hình kết quả thanh toán 
 "hotline": "*6789",// Số hotline của dịch vụ 
 "expireDate": "2023-08-29 18:45:00",// thời gian hết hạn thanh toán sinh ra tại SDK 
 "description": "Thanh toán đơn hàng đặt vé xem phim"
 },
 "orderInfo": [
 {
 "title": "Thông tin thanh toán",
 "type": "GROUP",
 "values": [
 {
 "title": "Tổng tiền gốc",
 "value": "860,000 VND",// Giá trị là tổng tiền đơn hàng trước khuyến mại SDK, có format dấu phẩy và đơn vị tiền tệ = VND 
 "type": "TITLE_VALUE"
 },
 {
 "title": "Số tiền được giảm",
 "value": "60,000 VND",// Giá trị là số tiền khuyến mại SDK, có format dấu phẩy và đơn vị tiền tệ = VND, trường hợp không có khuyến mại trả giá trị = 0
 "type": "TITLE_VALUE"
 },
 {
 "title": "Tổng tiền thanh toán",
 "value": "800,000 VND",// Giá trị là tổng tiền đơn hàng sau khuyến mại SDK, có format dấu phẩy và đơn vị tiền tệ = VND 
 "type": "TITLE_VALUE"
 }
 ]
 },
 {
 "title": "Thông tin khách hàng",
 "type": "GROUP",
 "values": [
 {
 "title": "Tên khách hàng",
 "value": "Nguyễn Văn A",// Giá trị là tên của người liên hệ 
 "type": "TITLE_VALUE"
 },
 {
 "title": "Số điện thoại",
 "value": "01234567899",// Giá trị là số điện thoại của người liên hệ 
 "type": "TITLE_VALUE"
 }
 ]
 }
 ]
}]]> | 

 | 2 | Tàu hỏa | MidnightJson VI - TEMPLATEtruetrue không hiển thị button xuất hóa đơn tại bank
 "customerName": "Nguyễn Văn A" --> Tên khách hàng
 "serviceName": "Đặt vé tàu",// Client bank lấy để hiển thị tại màn hình kết quả thanh toán
    "note": "Lưu ý: Mã xác nhận sẽ được gửi về email và số điện thoại liên hệ đăng ký khi đặt dịch vụ. Trong 30 phút sau khi thanh toán thành công Qúy khách hàng không nhận được thông tin vui lòng liên hệ tổng đài *6789 để được hỗ trợ.",// Câu note để hiển thị tại màn hình kết quả thanh toán 
 "expireDate": "2023-08-29 18:45:00",// thời gian hết hạn thanh toán sinh ra tại SDK 
 "description": "Thanh toán đơn hàng đặt vé tàu"
 },
 "orderInfo": [
 {
 "title": "Thông tin thanh toán",
 "type": "GROUP",
 "values": [
 {
 "title": "Tổng tiền gốc",
 "value": "860,000 VND",// Giá trị là tổng tiền đơn hàng trước khuyến mại SDK, có format dấu phẩy và đơn vị tiền tệ = VND 
 "type": "TITLE_VALUE"
 },
 {
 "title": "Số tiền được giảm",
 "value": "60,000 VND",// Giá trị là số tiền khuyến mại SDK, có format dấu phẩy và đơn vị tiền tệ = VND, trường hợp không có khuyến mại trả giá trị = 0
 "type": "TITLE_VALUE"
 },
 {
 "title": "Tổng tiền thanh toán",
 "value": "800,000 VND",// Giá trị là tổng tiền đơn hàng sau khuyến mại SDK, có format dấu phẩy và đơn vị tiền tệ = VND 
 "type": "TITLE_VALUE"
 }
 ]
 },
 {
 "title": "Thông tin chiều đi",
 "type": "GROUP",
 "values": [
 {
 "title": "Ga khởi hành",
 "value": "Ga Hà Nội",// Giá trị là tên ga khởi hành
 "type": "TITLE_VALUE"
 },
 {
 "title": "Ga đến",
 "value": "Ga Hải Phòng",// Giá trị là tên ga đến
 "type": "TITLE_VALUE"
 },
 {
 "title": "Ngày giờ khởi hành",
 "value": "10/02/2025 19:30",// Giá trị là thời gian khởi hành
 "type": "TITLE_VALUE"
 }, 
 {
 "title": "Mã chuyến tàu",
 "value": "SE091",// Giá trị là mã chuyến tàu
 "type": "TITLE_VALUE"
 }, 
 {
 "title": "Số ghế",
 "value": "Ghế 6 - Toa 3, Ghế 7 - Toa 2",// Giá trị là số ghế. Mỗi cặp ghế - toa cách nhau bởi dấu ","
 "type": "TITLE_VALUE"
 }, 
 {
 "title": "Số lượng vé",
 "value": "1",// Giá trị là số lượng vé
 "type": "TITLE_VALUE"
 }
 ]
 }, 
 {
 "title": "Thông tin chiều về",
 "type": "GROUP",
 "values": [
 {
 "title": "Ga khởi hành",
 "value": "Ga Hà Nội",// Giá trị là tên ga khởi hành
 "type": "TITLE_VALUE"
 },
 {
 "title": "Ga đến",
 "value": "Ga Hải Phòng",// Giá trị là tên ga đến
 "type": "TITLE_VALUE"
 },
 {
 "title": "Ngày giờ khởi hành",
 "value": "10/02/2025 19:30",// Giá trị là thời gian khởi hành
 "type": "TITLE_VALUE"
 }, 
 {
 "title": "Mã chuyến tàu",
 "value": "SE091",// Giá trị là mã chuyến tàu
 "type": "TITLE_VALUE"
 }, 
 {
 "title": "Số ghê",
          "value": "Ghế 6 - Toa 3, Ghế 7 - Toa 2",// Giá trị là số ghế. Mỗi cặp ghế - toa cách nhau bởi dấu "," 
          "type": "TITLE_VALUE"
 }, 
 {
 "title": "Số lượng vé",
 "value": "1",// Giá trị là số lượng vé
 "type": "TITLE_VALUE"
 }
 ]
 },    
    {
 "title": "Thông tin khách hàng",
 "type": "GROUP",
 "values": [
 {
 "title": "Tên khách hàng",
 "value": "Nguyễn Văn A",// Giá trị là tên của người liên hệ 
 "type": "TITLE_VALUE"
 },
 {
 "title": "Số điện thoại",
 "value": "01234567899",// Giá trị là số điện thoại của người liên hệ 
 "type": "TITLE_VALUE"
 },
 {
 "title": "email",
 "value": "quanap@gmail.com",// Giá trị là email của khách hàng
 "type": "TITLE_VALUE"
 }, 
      ]
 }
 ]
}]]> |

---

### 18.2. URD_MB_COOPBANK_ THANH TOÁN VÉ MÁY BAY

> **Page ID:** `29890192` · **Version:** 5
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29890192

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*4 trang con:*

#### 18.2.1. Đặt vé máy bay

> **Page ID:** `37662039` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37662039

### Phạm vi chức năng:

 | 
 | Phạm vi chức năng | Chức năng cấp 2 | Ghi chú
 | 1 | Đặt vé máy bay nội địa | 
 | 
Luồng đặt vé thuộc phạm vi URD SDK Đặt vé máy bay <Tham khảo tài liệu tham khảo bên dưới>

Luồng thanh toán (từ MH Thanh toán vé máy bay) thuộc phạm vi URD - Thanh toán ngay - Vé máy bay 

 | 2 | Đặt vé máy bay quốc tế | 
 | 
Luồng đặt vé thuộc phạm vi URD SDK Đặt vé máy bay (Tham khảo tài liệu tham khảo bên dưới)

Luồng thanh toán (từ MH Thanh toán vé máy bay) thuộc phạm vi URD - Thanh toán ngay - Vé máy bay 

 | 3 | Quản lý chuyến bay | 
Lịch sử đặt, thay đổi vé máy bay

Đổi tên hành khách

Đổi chuyển bay

Mua hành lý, suất ăn

Mua chỗ ngồi
 | <Tham khảo URD SDK bên dưới>
 | 4 | Làm thủ tục trực tuyến | 
 | <Tham khảo URD SDK bên dưới>
 | 5 | Theo dõi chuyến bay | 
 | <Tham khảo URD SDK bên dưới>
 | 6 | Thanh toán vé máy bay | 
 | 
Sau khi nhập Mã đặt chỗ/ mã thanh toán hiển thị MH đầu thuộc URD SDK Đặt vé máy bay <Tham khảo tài liệu bên dưới>

MH sau thuộc luồng URD Thanh toán ngay - Vé máy bay

### Tài liệu tham khảo: 

 | 
 | Tài liệu | Version | Ghi chú
 | 1 | <Upload tài liệu SDK Đặt vé máy bay> | 1.0.8 |

---

#### 18.2.2. Thanh toán ngay - Vé máy bay

> **Page ID:** `37657303` · **Version:** 34
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37657303

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 

 | A | Bùi Thanh Thảo | 
 | 
Tạo mới
 | 

 | 
 
 | M | HongLT | 
 | 
Map lại trường cho Client theo SDK vé máy bay version mới (v3)
 | 

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, App Client, App Server, Bank server, Billing system, VNPAY Ticket server
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công.
• Số dư khả dụng của tài khoản thanh toán lớn hơn số tiền vé phải thanh toán.
• KH thực hiện đặt vé và chọn Thanh toán tại màn hình Xác nhận đặt vé.
• Kết quả mong muốn:
• KH thanh toán vé máy bay thành công.
• VNPAY Ticket xuất vé tự động thành công cho KH và thực hiện gửi SMS, Email, OTT cho KH.
• Tài khoản nguồn được trừ tiền đúng bằng số tiền sau Thuế và phí, giảm giá
•  Remark GD: [Tên KH] TT [Tên dịch vụ] của [Vnticket] với mã thanh toán[Số mã thanh toán]
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

#### MB:

##### MH0: MH Xác nhận thanh toán vé máy bay

##### MH1: MH khởi tạo thanh toán vé máy bay

##### MH2: Xác nhận thanh toán 

##### MH3: MH Xác thực thanh toán

##### MH4: MH kết quả thanh toán

#### Mô tả màn hình:

##### MH0: MH Xác nhận thanh toán vé máy bay

Xem chi tiết tại URD_TICKET_SDK_1.0.8.docx

##### MH1: MH khởi tạo thanh toán vé máy bay
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
Tiêu đề: THANH TOÁN VÉ MÁY BAY

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị MH chọn chuyến bay của sdk

 | 3 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | Yes | -- | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 4 | 
Thông tin thanh toán
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị lại thông tin thanh toán gồm:

• Mã thanh toán (pay_code)
• Tổng tiền thanh toán (amount)
 | 5 | Thông tin hành trình | Label | ReadOnly | -- | -- | 
Hiển thị lại thông tin hành trình gồm:

1/ Chiều đi (Object departFlights )

• Điểm đi: original_name
• Điểm đến: destination_name 
• Số hiệu chuyến bay: nằm trong thuộc tính con của Object departFlights:   FlightSegment  → flightNumber
• Logo hãng bay: logo thu gọn
• Thời gian cất cánh (Ngày/giờ/thứ): depart_date (Format sdk trả: yyyy-MM-dd HH:mm:ss)
• Thời lượng bay: duration
2/ Chiều về (Object returnFlights )

• Điểm đi: original_name
• Điểm đến: destination_name 
• Số hiệu chuyến bay: nằm trong thuộc tính con của Object departFlights:   FlightSegment  → flightNumber
• Logo hãng bay: logo thu gọn
• Thời gian cất cánh (Ngày/giờ/thứ): depart_date (Format sdk trả: yyyy-MM-dd HH:mm:ss)
• Thời lượng bay: duration
 | 6 | Thông tin hành khách | Label | ReadOnly | -- | -- | 
Hiển thị lại thông tin hành khách gồm:

• Họ và tên hành khách: fullName 
• Giới tính: title 
 | 7 | 
Nút Tiếp tục
 | 
Button
 | 
Click
 | -- | -- | 
• Mặc định ở trạng thái Enable<Tham khảo logic xử lý>

##### MH2: Xác nhận thanh toán 
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: XÁC NHẬN GIAO DỊCH

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó với các giá trị giữ nguyên.

 | 3 | Ghi chú | Label | ReadOnly | -- | -- | Fix tại client: Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo
 | 4 | 
Thông tin xác nhận
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị thông tin xác nhận giao dịch truy vấn từ SDK Vé máy bay về:

• Tài khoản nguồn
• Dịch vụ: Fix tại Client: Đặt vé máy bay
• Mã thanh toán: Hiển thị theo kết quả tra cứu 
• Số tiền
• Phí giao dịch và thuế: Hiển thị kết quả tính toán do App server trả về theo dữ liệu tại BE (hiển thị khi khác 0 và rỗng)
 | 5 | 
Hình thức xác thực:

<Tham khảo  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)>

 | 6 | 
Nút “Xác nhận”
 | 
Button
 | 
Click
 | -- | -- | 
Mặc định Enable
<Tham khảo logic xử lý>

##### MH3: MH Xác thực thanh toán

Tham khảo URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH4: MH kết quả thanh toán
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

 | 1 | Icon Home | Icon | Click | -- | -- | Quay lại MH Home
 | 2 | Tiêu đề màn hình | Label | ReadOnly | -- | -- | Hiển thị: Kết quả giao dịch
 | 3 | Logo Bank | Label  | ReadOnly | -- | -- | Hiển thị Logo Co-opBank
 | 4 | Tên ngân hàng | Label | ReadOnly | -- | -- | Hiển thị tên Ngân hàng Co-opBank bên cạnh logo Bank
 | 5 | Icon giao dịch thành công | Label | ReadOnly | -- | -- | Hiển thị icon giao dịch thành công
 | 6 | Tiêu đề | Label | ReadOnly | -- | -- | Tiêu đề: Thanh toán vé máy bay thành công
 | 7 | Số tiền giao dịch | Label | ReadOnly | -- | -- | Hiển thị số tiền đã giao dịch 
 | 8 | Thời gian giao dịch | Label | ReadOnly | -- | -- | Dữ liệu do App server trả về, định dạng: dd/mm/yyyy hh:mm
 | 9 | Dịch vụ | Label | ReadOnly | -- | -- | Hiển thị dịch vụ đã chọn thanh toán
 | 10 | Mã thanh toán | Lablel | ReadOnly | -- | -- | Hiển thị Mã thanh toán do Vnticket sinh
 | 11 | Mã giao dịch | Label | ReadOnly | -- | -- | Mã do Bank server sinh khi trừ tiền thành công
 | 12 | Thông báo | Label | ReadOnly | -- | -- | 
Fix tại Client: "Mã đặt chỗ sẽ được gửi về email, số điện thoại đăng ký khi đặt vé. Trong vòng 30 phút sau khi thanh toán thành công Quý khách không nhận được mã đặt chỗ vui lòng liên hệ tổng đài 1900555520 để được hỗ trợ."

"Nếu Quý khách có nhu cầu lấy hóa đơn GTGT, vui lòng chọn Lấy hóa đơn thanh toán tại MH này hoặc liên hệ tổng đài 1900555520 để được hỗ trợ."

 | 13 | Lấy hóa đơn | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn Lấy hóa đơn, hiển thị màn hình SDK Lấy hóa đơn

<Logic Tham khảo URD SDK Thanh toán vé máy bay>

Do ver mới của SDK vé máy bay ko hỗ trợ KH lấy hóa đơn sau khi thanh toán nên bỏ chức năng này (KH muốn xuất hóa đơn thì nhập thông tin xuất hóa đơn ngay trong MH của chức năng  Đặt vé

 | 14 | 
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

 | 15 | 
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

 | 16 | 
Nút “Tạo giao dịch mới”
 | 
Button
 | 
Click
 | -- | -- | 
Nhấn Tạo giao dịch mới, hiển thị màn hình khởi tạo giao dịch mới của thanh toán hóa đơn tương ứng (tài khoản nguồn được cập nhật số dư).

#### 4/ Luồng xử lý

##### MH0: Truy cập chức năng: Thực hiện thanh toán vé máy bay của chức năng Đặt vé máy bay.
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | TH1: Thanh toán ngay sau khi đặt xong vé máy bay
 | 
1
 | 
Tại màn hình Xác nhận chuyển bay, nhấn chọn Thanh toán
 | 
App Client
 | 
1/ Xử lý yêu cầu đặt và hold vé sang Ticket system (Tham khảo xử lý tại URD SDK Ticket)

2/ Check thông tin gói dịch vụ của KH:

• Không hợp lệ: Hiển thị thông báo tương ứng: | | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung
 | 
Xử lý (nếu có)

 | 1 | Gói dịch vụ không bao gồm dịch vụ đã lựa chọn | Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ. | 

• Hợp lệ: Gửi yêu cầu lấy thông tin tài khoản nguồn tới Bank server qua App server
 | App Server | 
Chuyển tiếp yêu cầu sang Bank server

 | Bank server | 
Truy vấn thông tin và trả kết quả danh sách TK thanh toán

 | App server | 
Nhận kết quả:

• Không thành công: Trả kết quả lỗi tương ứng | | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 

• Thành công: Kiểm tra theo rule quy định tại BE và cấu hình hiển thị các tài khoản được phép thanh toán hóa đơn tới App Client; Trả kết quả MH khởi tạo thanh toán
 | App Client | 
Nhận kết quả:

• Không thành công: Hiển thị MH popup thông báo lỗi tương ứng
• Thành công: Hiển thị MH Khởi tạo thanh toán vé máy bay với thông tin về tk nguồn và thông tin về đặt vé do SDK Ticket chuyền sang

##### MH1: MH Khởi tạo thanh toán
 | TT | Thao tác | Tác nhân | Mô tả
 | 
1
 | 
Bấm chọn “Tài khoản nguồn”
 | 
Client
 | 
Kiểm tra đã lấy danh sách tài khoản thanh toán thành công chưa?

• Đã lấy thành công trước đó: Hiển thị popup chọn tài khoản nguồn gồm danh sách các tài khoản nguồn do server trả về
• Tiêu đề: Tài khoản nguồn
• Hiển thị. Hiển thị gồm:
• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
• Chưa thành công: Gửi yêu cầu lấy danh sách tài khoản thanh toán đến MB server
 | MB server | Gửi yêu cầu lấy danh sách tài khoản thanh toán đến Bank server
 | Bank server | Xử lý và phản hồi kết quả lấy danh sách tài khoản thanh toán đến MB server
 | MB server | 
1/ Nhận phản hồi kết quả lấy danh sách tài khoản thanh toán

• Không thành công: Trả kết quả thông báo lỗi: | | 
TT
 | 
Trường hợp lỗi
 | 
Thông báo
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.

• Thành công: Kiểm tra theo rule quy định tại BE và cấu hình hiển thị các tài khoản được phép thanh toán hóa đơn tới App Client
 | App Client | 
Nhận kết quả:

• Không thành công: Hiển thị MH popup thông báo lỗi tương ứng
• Thành công: 
• Hiển thị danh sách TK cho KH lựa chọn, với tk mặc định theo mô tả MH
 | 
Chọn 1 “Tài khoản nguồn”
 | 
Client
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
Lưu ý: Chỉ được phép chọn 1 tài khoản

 | 
2

 | 
Nhấn Tiếp tục

 | 
Client
 | 
Gửi yêu cầu khởi tạo giao dịch

 | 
MB Server
 | 
Gửi yêu cầu truy vấn thông tin vé sang VNPAY Ticket server thông qua hệ thống MB Server→  Billing system → Hệ thống VNPAY Ticket server

 | 
VNPAY Ticket server
 | 
Truy vấn thông tin vé và trả kết quả cho MB server qua Vnpay Billing

 | MB server | 
1/ Nhận kết quả truy vấn thông tin hóa đơn và Kiểm tra hạn mức dịch vụ và tính phí giao dịch

• Không hợp lệ: Cập nhật trạng thái giao giao dịch lỗi và trả kết quả lỗi tương ứng về Client: Theo Quy định kiểm tra hạn mức giao dịch với các giao dịch tài chính tại App server tại luồng khởi tạo giao dịch và một số lỗi như dưới đây: | | 
 | 
Trường hợp
 | 
Tác nhân
 | 
Nội dung thông báo
 | 
Xử lý

 | 1 | Mã vé hết hiệu lực thanh toán hoặc đã thanh toán | App server | Hóa đơn không tồn tại hoặc đã được thanh toán. Quý khách vui lòng kiểm tra lại! | 

• Hợp lệ: 
• Xử lý trả về phương thức xác thực, phí dịch vụ, thông tin dịch vụ cho App Client (Tham khảo tại URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)
• Ghi nhận trạng thái giao dịch ở phase khởi tạo thành công.
 | 
Client
 | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng mà App Server trả về
• Thành công: 
• Hiển thị màn hình Xác nhận giao dịch với các thông tin thanh toán và hình thức xác thực App Server trả về.

##### MH2: Màn hình xác nhận giao dịch

• Tham khảo tài liệu: URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2) | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Chọn 1 phương thức xác thực và nhấn ""Xác nhận" | App Client | Xử lý thông tin validate (nếu có) và gửi yêu cầu xác nhận giao dịch với PTXT tương ứng sang App Server
 | App Server | Xử lý và trả kết quả xác nhận giao dịch cho App Client theo PTXT tương ứng, ghi nhận giao dịch ở trạng thái "Chờ xác thực"
 | App Client | 
Nhận kết quả và hiển thị màn hình xác thực giao dịch

##### MH3: Màn hình xác thực giao dịch
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Thực hiện xác thực theo PTXT tương ứng

 | App Client | Xử lý thông tin validate (nếu có) và gửi yêu cầu xác thực giao dịch với PTXT tương ứng sang App Server
 | App Server | 
1/ Xử lý xác thực giao dịch theo PTXT (Tham khảo:  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2))

2/ Gửi yêu cầu hạch toán sang Bank Server

 | Bank Server | 
Xử lý hạch toán với Core Bank và trả kết quả:

• Không hợp lệ: Trả kết quả cho App Server | | 
 | 
Trường hợp
 | 
Thông báo
 | 
Xử lý (nếu có)

 | 1 | Số dư không đủ | Số dư tài khoản không đủ. Quý khách vui lòng kiểm tra lại | 

 | 2 | Số dư duy trì tối thiểu không đủ | Số dư tối thiểu duy trì tài khoản không đủ. Quý khách vui lòng kiểm tra lại | 

• Hợp lệ: Trả kết quả cho App Server
 | App Server | 
Nhận kết quả:

• Không hợp lệ:
• Trả kết quả cho App Client hiển thị thông báo lỗi tương ứng đã cấu hình tại bảng MB_Template
• Ghi nhận trạng thái giao dịch là Fail
• Timeout:
• Trả kết quả cho App Client hiển thị thông báo lỗi timeout.
• Ghi nhận trạng thái giao dịch là Timeout
• Hợp lệ:
• Gửi yêu cầu gạch nợ và xuất vé sang Vnpay Billing system → Ticket server → NCC
• Ghi nhận trạng thái giao dịch là Thành công (Phase 2)
 | VNPAY Billing System → Ticket server --> NCC | 
1/ Xử lý gạch nợ và xuất vé với NCC

2/ Trả kết quả gạch nợ cho App Client qua App server

 | App Server | 
1/ Nhận kết quả xác nhận giao dịch và xử lý:

• Không hợp lệ: 
• Ghi nhận trạng thái giao dịch là Fail
• Hiển thị Popup thông báo lỗi tương ứng
• Gọi API đảo tiền tới Bank server và nhận kết quả:
• Không thành công: Ghi nhận trạng thái phase đảo tiền Thất bại
• Thành công: Ghi nhận trạng thái phase đảo tiền Thành công
• TimeOut:
• Ghi nhận trạng thái giao dịch là Timeout
• Hiển thị popup thông báo lỗi tương ứng: | | 
TT
 | 
Trường hợp
 | 
Tác nhân
 | 
Nội dung thông báo

 | 1 | TimeOut | Hệ thống MB | Yêu cầu tạm thời bị gián đoạn. Quý khách vui lòng thực hiện lại sau.

•  Hợp lệ:
• Cấu hình hiển thị màn hình kết quả giao dịch
• Cập nhật trạng thái giao dịch phase trừ tiền và gạch nợ là "Thành công"
 | App Client | 
Nhận kết quả:

• Không thành công: Hiển thị Popup thông báo lỗi tương ứng
• Timeout: Hiện thị thông báo lỗi tương ứng 
•  Thành công: Hiển thị màn hình kết quả giao dịch
Lưu ý: Nhấn “Đồng ý” trên các thông báo lỗi tại màn hình xác nhận, ứng dụng hiển thị màn hình khởi tạo với các thông tin nhập trước đó và cập nhật lại số dư tài khoản theo server trả về

##### MH4: Màn hình Kết quả giao dịch
 | | 

 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn “Tạo giao dịch mới”
 | 
App Client
 | 
Hiển thị màn hình Đặt vé máy bay, MH đầu tiên của SDK

 | 2 | 
Nhấn “Home”
 | 
App Client
 | 
Hiển thị màn hình Home với thông tin số dư được cập nhật lại sau khi thanh toán thành công

 | 3 | Lấy hóa đơn | App Client | Tham khảo logic SDK Lấy vé máy bay. Sau khi lấy x

> ⚠️ *Nội dung đã cắt ngắn (15163 ký tự gốc). Xem đầy đủ trên Confluence.*


---

#### 18.2.3. Thanh toán sau (OTT) - Vé máy bay

> **Page ID:** `37657401` · **Version:** 18
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37657401

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, App Client, App Server, Bank server, Billing system, VNPAY Ticket server
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công.
• KH có tài khoản nguồn hợp lệ (cấu hình rule tại Backend) để thực hiện chức năng này.
• Số dư khả dụng của tài khoản thanh toán lớn hơn số tiền vé phải thanh toán.
• KH nhận được OTT thanh toán vé máy bay
• Kết quả mong muốn:
• KH thanh toán vé máy bay thành công.
• VNPAY Ticket xuất vé tự động thành công cho KH và thực hiện gửi SMS, Email, OTT cho KH.
• Tài khoản nguồn được trừ tiền đúng bằng số tiền sau Thuế và phí, giảm giá
• [Tên KH] TT [Tên dịch vụ] của [Nhà cung cấp] với mã thanh toán[Số mã thanh toán]
Lưu ý: Với dịch vụ addon vé máy bay cần nêu rõ thuộc loại dịch vụ nào: Đổi tên hành khách, Sửa chuyến bay, Mua hành lý/ suất ăn, Mua chỗ ngồi chức năng Đặt vé máy bay

#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

##### MH0: Thông báo tin OTT

##### MH1: Khởi tạo thanh toán

##### MH2: Xác nhận giao dịch

##### MH3: Xác thực giao dịch

##### MH4: Kết quả thanh toán

#### Mô tả màn hình:

##### MH0: Thông báo tin OTT
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
Hiển thị nội dung tin thông báo cước theo SDK trả về

 | 2 | Thanh toán | Button | Click | -- | -- | <Tham khảo logic xử lý>

##### MH1: Khởi tạo thanh toán
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
Tiêu đề: THANH TOÁN VÉ MÁY BAY

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình trước đó

 | 4 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | Yes | -- | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 5 | 
Thông tin thanh toán
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Fill thông tin từ OTT trả về gồm:

• Mã thanh toán
• Tổng tiền thanh toán
 | 6 | 
Nút Tiếp tục
 | 
Button
 | 
Click
 | -- | -- | 
• Mặc định ở trạng thái Enable<Tham khảo logic xử lý>

##### MH2: Xác nhận giao dịch

Tham khảo 

##### MH3: Xác thực giao dịch

Tham khảo URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH4: Kết quả thanh toán

Tham khảo Tham khảo 

#### 4/ Luồng xử lý

##### MH0: Truy cập chức năng: Từ tin OTT trả về điện thoại
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | TH1: Từ MH thông tin OTT
 | 
1
 | 
Tại màn hình thông tin OTT Đặt vé máy bay thành công, nhấn chọn thanh toán
 | 
App Client
 | 
1/ Kiểm tra KH thực hiện chức năng:

Trước đăng nhập: hiển thị thông báo: "Quý khách vui lòng đăng nhập Mobile Banking để thanh toán hóa đơn này."

• Nút Hủy: Nhấn nút này, tắt thông báo và hiển thị màn hình đang thao tác
• Nút Đồng ý: Nhấn nút này, ứng dụng hiển thị màn hình Đăng nhập. Sau khi đăng nhập xong thực hiện như luồng sau đăng nhập phía dươi.
Sau đăng nhập: Gọi qua App server sang Bank server lấy danh sách tài khoản thanh toán

2/ Check thông tin gói dịch vụ của KH:

• Không hợp lệ: Hiển thị thông báo tương ứng: | | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung
 | 
Xử lý (nếu có)

 | 1 | Gói dịch vụ không bao gồm dịch vụ đã lựa chọn | Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ. | 

• Hợp lệ: Gửi yêu cầu lấy thông tin tài khoản nguồn tới Bank server qua App server
 | App Server | 
Chuyển tiếp yêu cầu sang Bank server

 | Bank server | 
Truy vấn thông tin và trả kết quả danh sách TK thanh toán

 | App server | 
Nhận kết quả:

• Không thành công: Trả kết quả lỗi tương ứng | | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 

• Thành công: Kiểm tra theo rule quy định tại BE và cấu hình hiển thị các tài khoản được phép thanh toán hóa đơn tới App Client; Trả kết quả MH khởi tạo thanh toán
 | App Client | 
Nhận kết quả:

• Không thành công: Hiển thị MH popup thông báo lỗi tương ứng
• Thành công: Hiển thị MH Khởi tạo thanh toán vé máy bay với thông tin về tk nguồn và thông tin về đặt vé do SDK Ticket chuyền sang

##### MH1: Khởi tạo thanh toán

Tham khảo 

##### MH2: Xác nhận giao dịch

Tham khảo 

##### MH3: Xác thực giao dịch

Tham khảo URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH4: Kết quả thanh toán

Tham khảo Tham khảo

---

#### 18.2.4. Thanh toán các dịch vụ addon Vé máy bay

> **Page ID:** `42637812` · **Version:** 11
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/42637812

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, App Client, App Server, Bank server, Billing system, VNPAY Ticket server
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công.
• KH có tài khoản nguồn hợp lệ (cấu hình rule tại Backend) để thực hiện chức năng này.
• Số dư khả dụng của tài khoản thanh toán lớn hơn số tiền vé dịch vụ phải thanh toán.
• Kết quả mong muốn:
• KH thanh toán dịch vụ thành công.
• VNPAY Ticket xuất vé tự động thành công cho KH và thực hiện gửi SMS, Email, OTT cho KH.
• Tài khoản nguồn được trừ tiền đúng bằng số tiền sau Thuế và phí, giảm giá
•  [Tên KH] TT [Tên dịch vụ] của [Nhà cung cấp] với mã thanh toán[Số mã thanh toán]
• Lưu ý: Tên dịch vụ addon cần nêu rõ thuộc loại nào: Đổi tên hành khách, Sửa chuyến bay, Mua hành lý/ suất ăn, Mua chỗ ngồi chức năng Đặt vé máy bay
#### 2/ Luồng màn hình

##### MH1: MH khởi tạo thanh toán

##### MH1: Xác nhận thanh toán

##### MH2: Xác thực giao dịch

##### MH4.1: MH Kết quả giao dịch (Dịch vụ addon Sửa chuyến bay)

##### MH4.2: Kết quả thanh toán (các dịch vụ Addon khác)

#### Mô tả màn hình:

##### MH1: Khởi tạo thanh toán
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
Tiêu đề: THANH TOÁN

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình trước đó

 | 4 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | Yes | -- | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 5 | 
Thông tin thanh toán
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Gồm:

• Mã thanh toán
• Tổng tiền thanh toán
• Dịch vụ: Theo title lựa chọn của khách hàng ở Quản lý chuyến bay
 | 6 | 
Nút Tiếp tục
 | 
Button
 | 
Click
 | -- | -- | 
• Mặc định ở trạng thái Enable<Tham khảo logic xử lý>

##### MH2: Xác nhận giao dịch
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: XÁC NHẬN GIAO DỊCH

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó với các giá trị giữ nguyên.

 | 3 | Ghi chú | Label | ReadOnly | -- | -- | Fix tại client: Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo
 | 4 | 
Thông tin xác nhận
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị thông tin gồm:

• Tài khoản nguồn
• Dịch vụ: Fix tại Client: Theo title lựa chọn của khách hàng ở Quản lý chuyến bay
• Mã thanh toán: Hiển thị theo kết quả tra cứu 
• Số tiền
• Phí giao dịch và thuế: Hiển thị kết quả tính toán do App server trả về theo dữ liệu tại BE (hiển thị khi khác 0 và rỗng)
 | 5 | 
Hình thức xác thực:

<Tham khảo  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)>

 | 6 | 
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

##### MH4: Kết quả thanh toán
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

 | 1 | Icon Home | Icon | Click | -- | -- | Quay lại MH Home
 | 2 | Tiêu đề màn hình | Label | ReadOnly | -- | -- | Hiển thị: Kết quả giao dịch
 | 3 | Logo Bank | Label  | ReadOnly | -- | -- | Hiển thị Logo Co-opBank
 | 4 | Tên ngân hàng | Label | ReadOnly | -- | -- | Hiển thị tên Ngân hàng Co-opBank bên cạnh logo Bank
 | 5 | Icon giao dịch thành công | Label | ReadOnly | -- | -- | Hiển thị icon giao dịch thành công
 | 6 | Tiêu đề | Label | ReadOnly | -- | -- | Tiêu đề: Thanh toán thành công
 | 7 | Số tiền giao dịch | Label | ReadOnly | -- | -- | Hiển thị số tiền đã giao dịch 
 | 8 | Thời gian giao dịch | Label | ReadOnly | -- | -- | Dữ liệu do App server trả về, định dạng: dd/mm/yyyy hh:mm
 | 9 | Dịch vụ | Label | ReadOnly | -- | -- | Hiển thị dữ liệu từ MH trước
 | 10 | Mã thanh toán | Lablel | ReadOnly | -- | -- | Hiển thị Mã thanh toán do Vnticket sinh
 | 11 | Mã giao dịch | Label | ReadOnly | -- | -- | Mã do Bank server sinh khi trừ tiền thành công
 | 12 | Thông báo 1 | Label | ReadOnly | -- | -- | 
Fix tại Client: "Mã đặt chỗ sẽ được gửi về email, số điện thoại đăng ký khi đặt vé. Trong vòng 30 phút sau khi thanh toán thành công Quý khách không nhận được mã đặt chỗ vui lòng liên hệ tổng đài 1900555520 để được hỗ trợ."

Chỉ hiển thị khi dịch vụ thanh toán addon là Sửa chuyến bay

 | 13 | Thông báo 2 | Label | ReadOnly | -- | -- | 
Fix tại Client: "Nếu Quý khách có nhu cầu lấy hóa đơn GTGT, vui lòng chọn Lấy hóa đơn thanh toán tại MH này hoặc liên hệ tổng đài 1900555520 để được hỗ trợ.."

 | 14 | Lấy hóa đơn | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn Lấy hóa đơn, hiển thị màn hình SDK Lấy hóa đơn

<Logic Tham khảo URD SDK Thanh toán vé máy bay>

 | 15 | 
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

 | 16 | 
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

 | 17 | 
Nút “Tạo giao dịch mới”
 | 
Button
 | 
Click
 | -- | -- | 
Nhấn Tạo giao dịch mới, hiển thị màn hình khởi tạo giao dịch mới của thanh toán hóa đơn tương ứng (tài khoản nguồn được cập nhật số dư).

#### 4/ Luồng xử lý

##### Truy cập chức năng: Thực hiện thanh toán dịch vụ addon: Đổi tên hành khách, Sửa chuyến bay, Mua hành lý/ suất ăn, Mua chỗ ngồi chức năng Đặt vé máy bay.
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | TH1: Thanh toán ngay sau khi chọn xong dịch vụ TT vé máy bay
 | 
1
 | 
Tại màn hình Xác nhận thanh toán  của SDK, nhấn chọn Thanh toán
 | 
App Client
 | 
1/ Xử lý yêu cầu sinh mã thanh toán

2/ Check thông tin gói dịch vụ của KH:

• Không hợp lệ: Hiển thị thông báo tương ứng: | | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung
 | 
Xử lý (nếu có)

 | 1 | Gói dịch vụ không bao gồm dịch vụ đã lựa chọn | Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ. | 

• Hợp lệ: Gửi yêu cầu lấy thông tin tài khoản nguồn tới Bank server qua App server
 | App Server | 
Chuyển tiếp yêu cầu sang Bank server

 | Bank server | 
Truy vấn thông tin và trả kết quả danh sách TK thanh toán

 | App server | 
Nhận kết quả:

• Không thành công: Trả kết quả lỗi tương ứng | | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 

• Thành công: Kiểm tra theo rule quy định tại BE và cấu hình hiển thị các tài khoản được phép thanh toán hóa đơn tới App Client; Trả kết quả MH khởi tạo thanh toán
 | App Client | 
Nhận kết quả:

• Không thành công: Hiển thị MH popup thông báo lỗi tương ứng
• Thành công: Hiển thị MH Khởi tạo thanh toán vé máy bay với thông tin về tk nguồn. Thông tin về đặt vé do SDK Ticket chuyền sang

##### MH1: MH Khởi tạo thanh toán
 | TT | Thao tác | Tác nhân | Mô tả
 | 
1
 | 
Bấm chọn “Tài khoản nguồn”
 | 
Client
 | 
Kiểm tra đã lấy danh sách tài khoản thanh toán thành công chưa?

• Đã lấy thành công trước đó: Hiển thị popup chọn tài khoản nguồn gồm danh sách các tài khoản nguồn do server trả về có rule debit = yes của giao dịch TTHĐ
• Tiêu đề: Tài khoản nguồn
• Hiển thị. Hiển thị gồm:
• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
• Chưa thành công: Gửi yêu cầu lấy danh sách tài khoản thanh toán đến MB server
 | MB server | Gửi yêu cầu lấy danh sách tài khoản thanh toán đến Bank server
 | Bank server | Xử lý và phản hồi kết quả lấy danh sách tài khoản thanh toán đến MB server
 | MB server | 
1/ Nhận phản hồi kết quả lấy danh sách tài khoản thanh toán

• Không thành công: Trả kết quả thông báo lỗi: | | 
TT
 | 
Trường hợp lỗi
 | 
Thông báo
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.

• Thành công: Kiểm tra theo rule quy định tại BE và cấu hình hiển thị các tài khoản được phép thanh toán hóa đơn tới App Client
 | App Client | 
Nhận kết quả:

• Không thành công: Hiển thị MH popup thông báo lỗi tương ứng
• Thành công: Hiển thị MH danh sách tài khoản nguồn, với tài khoản mặc định theo mô tả tại mô tả MH
 | 
Chọn 1 “Tài khoản nguồn”
 | 
Client
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
Lưu ý: Chỉ được phép chọn 1 tài khoản

 | 
2

 | 
Nhấn Tiếp tục

 | 
Client
 | 
Gửi yêu cầu khởi tạo giao dịch

 | 
MB Server
 | 
Gửi yêu cầu truy vấn thông tin vé sang VNPAY Ticket server thông qua hệ thống MB Server→  Billing system → Hệ thống VNPAY Ticket server

 | 
VNPAY Ticket server
 | 
Truy vấn thông tin vé và trả kết quả cho MB server qua Vnpay Billing

 | MB server | 
1/ Nhận kết quả truy vấn thông tin hóa đơn và Kiểm tra hạn mức dịch vụ và tính phí giao dịch

• Không hợp lệ: Cập nhật trạng thái giao giao dịch lỗi và trả kết quả lỗi tương ứng về Client: Theo Quy định kiểm tra hạn mức giao dịch với các giao dịch tài chính tại App server tại luồng khởi tạo giao dịch và một số lỗi như dưới đây: | | 
 | 
Trường hợp
 | 
Tác nhân
 | 
Nội dung thông báo
 | 
Xử lý

 | 7 | Mã thanh toán hết hiệu lực | App server | Mã thanh toán hết hiệu lực. Quý khách vui lòng kiểm tra lại. | 

 | 8 | Mã thanh toán đã thanh toán | App server | Mã thanh toán đã thanh toán. Quý khách vui lòng kiểm tra lại. | 

• Hợp lệ: 
• Xử lý trả về phương thức xác thực, phí dịch vụ, thông tin dịch vụ cho App Client (Tham khảo tại URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)
• Ghi nhận trạng thái giao dịch ở phase khởi tạo thành công.
 | 
Client
 | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng mà App Server trả về
• Thành công: 
• Hiển thị màn hình Xác nhận giao dịch với các thông tin thanh toán và hình thức xác thực App Server trả về.

##### MH2: Màn hình xác nhận giao dịch

• Tham khảo tài liệu: URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2) | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Chọn 1 phương thức xác thực và nhấn ""Xác nhận" | App Client | Xử lý thông tin validate (nếu có) và gửi yêu cầu xác nhận giao dịch với PTXT tương ứng sang App Server
 | App Server | Xử lý và trả kết quả xác nhận giao dịch cho App Client theo PTXT tương ứng, ghi nhận giao dịch ở trạng thái "Chờ xác thực"
 | App Client | 
Nhận kết quả và hiển thị màn hình xác thực giao dịch

##### MH3: Màn hình xác thực giao dịch
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Thực hiện xác thực theo PTXT tương ứng

 | App Client | Xử lý thông tin validate (nếu có) và gửi yêu cầu xác thực giao dịch với PTXT tương ứng sang App Server
 | App Server | 
1/ Xử lý xác thực giao dịch theo PTXT (Tham khảo:  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2))

2/ Gửi yêu cầu hạch toán sang Bank Server

 | Bank Server | 
Xử lý hạch toán với Core Bank và trả kết quả:

• Không hợp lệ: Trả kết quả cho App Server | | 
 | 
Trường hợp
 | 
Thông báo
 | 
Xử lý (nếu có)

 | 1 | Số dư không đủ | Số dư tài khoản không đủ. Quý khách vui lòng kiểm tra lại | 

 | 2 | Số dư duy trì tối thiểu không đủ | Số dư tối thiểu duy trì tài khoản không đủ. Quý khách vui lòng kiểm tra lại | 

• Hợp lệ: Trả kết quả cho App Server
 | App Server | 
Nhận kết quả:

• Không hợp lệ:
• Trả kết quả cho App Client hiển thị thông báo lỗi tương ứng đã cấu hình tại bảng MB_Template
• Ghi nhận trạng thái giao dịch là Fail
• Timeout:
• Trả kết quả cho App Client hiển thị thông báo lỗi timeout.
• Ghi nhận trạng thái giao dịch là Timeout
• Hợp lệ:
• Gửi yêu cầu gạch nợ sang Vnpay Billing system → Ticket server → NCC
• Ghi nhận trạng thái giao dịch là Thành công (Phase 2)
 | VNPAY Billing System → Ticket server --> NCC | 
1/ Xử lý gạch nợ với NCC

2/ Trả kết quả gạch nợ cho App Client qua App server

 | App Server | 
1/ Nhận kết quả xác nhận giao dịch và xử lý:

• Không hợp lệ: 
• Ghi nhận trạng thái giao dịch là Fail
• Hiển thị Popup thông báo lỗi tương ứng
• Gọi API đảo tiền tới Bank server và nhận kết quả:
• Không thành công: Ghi nhận trạng thái phase đảo tiền Thất bại
• Thành công: Ghi nhận trạng thái phase đảo tiền Thành công
• TimeOut:
• Ghi nhận trạng thái giao dịch là Timeout
• Hiển thị popup thông báo lỗi tương ứng: | | 
TT
 | 
Trường hợp
 | 
Tác nhân
 | 
Nội dung thông báo

 | 1 | TimeOut | Hệ thống MB | Yêu cầu tạm thời bị gián đoạn. Quý khách vui lòng thực hiện lại sau.

•  Hợp lệ:
• Cấu hình hiển thị màn hình kết quả giao dịch
• Cập nhật trạng thái giao dịch phase trừ tiền và gạch nợ là "Thành công"
 | App Client | 
Nhận kết quả:

• Không thành công: Hiển thị Popup thông báo lỗi tương ứng
• Timeout: Hiện thị thông báo lỗi tương ứng 
•  Thành công: Hiển thị màn hình kết quả giao dịch
Lưu ý: Nhấn “Đồng ý” trên các thông báo lỗi tại màn hình xác nhận, ứng dụng hiển thị màn hình khởi tạo với các thông tin nhập trước đó và cập nhật lại số dư tài khoản theo server trả về

##### MH4: Màn hình Kết quả giao dịch
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn “Tạo giao dịch mới”
 | 
App Client
 | 
Hiển thị màn hình đầu tiên của SDK (menu cho phép chọn lại dịch vụ thanh toán vé máy bay KH muốn dùng)

 | 2 | 
Nhấn “Home”
 | 
App Client
 | 
Hiển thị màn hình Home với thông tin số dư được cập nhật lại sau khi thanh toán thành công

 | 3 | Lấy hóa đơn | App Client | Tham khảo logic SDK Lấy vé máy bay. Lấy xong hóa đơn về MH kết quả giao dịch
 | 4 | Chia sẻ | App Client | Tham khảo logic xử lý chung
 | 5 | Lưu ảnh | App Client | Tham khảo logic xử lý chung

---

### 18.3. URD_MB_COOPBANK_THANH TOÁN VÉ TÀU

> **Page ID:** `83866107` · **Version:** 15
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/83866107

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 

 | A | Bùi Thanh Thảo | 
 | 
Tạo mới
 | V.1
 | 
 
 | M | ThaoCY | V.2 | 
• Tích hợp SDK JSON
Map trường hiển thị theo cấu trúc Json của SDK VÉ TÀU

Cập nhật UI màn hình khởi tạo: Bỏ line gạch ngang giữa các trường thông tin
 | 

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, MB Client, MB Server, Bank server, Billing system, TichketTrain server
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công.
• Số dư khả dụng của tài khoản thanh toán lớn hơn số tiền vé phải thanh toán.
• KH có quyền truy cập chức năng này.
• Kết quả mong muốn:
• KH thanh toán vé xem phim thành công.
• TichketTrain server xuất vé tự động thành công cho KH và thực hiện gửi SMS, Email, OTT cho KH.
• Tài khoản nguồn được trừ tiền đúng bằng số tiền sau Thuế và phí, giảm giá
•  Remark: [Tên KH] TT [Tên dịch vụ] với mã thanh toán[Số mã thanh toán]
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

##### MH0: MH Thông tin thanh toán vé tàu tại SDK

##### MH1.1: MH Khởi tạo thanh toán - 1 chiều

##### MH1.2: MH Khởi tạo thanh toán - 2 chiều

##### 

##### MH2: MH Xác nhận thanh toán

#####  

##### MH3: MH Xác thực thanh toán

##### 

##### MH4: MH Kết quả thanh toán

##### MH0: MH Thông tin thanh toán vé tàu tại SDK

Tham khảo SDK vé tàu – version 2.1

##### MH1: MH Khởi tạo thanh toán
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
 | 
 | 
 | 
 | 
 | 

 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Thanh toán vé xem phim
 | 
 | 
 | 
 | 
 | 

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Về màn hình trước đó
 | 
 | 
 | 
 | 
 | 

 | 3 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | Yes | -- | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do Bank Server trả về.Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)
 | 
 | 
 | 
 | 
 | 

 | 4 | 
Quy tắc chung khi tích hợp SDK Json  QUY TẮC CHUNG TÍCH HỢP JSON CHO CÁC DỊCH VỤ SDK (CLIENT)
 | 
 | 
 | 
 | 
 | 

 | 5 | 
Thông tin thanh toán

 | 
Hiển thị theo cấu trúc JSON SDK trả về

"orderInfo": [
    {
      "title": "Thông tin thanh toán",
      "type": "GROUP"
 | 
 | 
 | 
 | 
 | 

 | 6 | 

 | 
Tổng tiền
 | 

 | 
 | 
 | 
"title": "Tổng tiền gốc", 

 "value": "860,000 VND",// Giá trị là tổng tiền đơn hàng trước khuyến mại SDK, có format dấu phẩy và đơn vị tiền tệ = VND

 "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 7 | 

 | Số tiền được giảm | 

 | 
 | 
 | 
"title": "Số tiền được giảm",
"value": "60,000 VND",// Giá trị là số tiền khuyến mại SDK, có format dấu phẩy và đơn vị tiền tệ = VND, trường hợp không có khuyến mại trả giá trị = 0
 "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 8 | 

 | 
Tổng tiền thanh toán
 | 

 | 
 | 
 | 
 "title": "Tổng tiền thanh toán",
 "value": "800,000 VND",// Giá trị là tổng tiền đơn hàng sau khuyến mại SDK, có format dấu phẩy và đơn vị tiền tệ = VND
 "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 9 | 
Thông tin chiều đi
 | 

 | 

 | 
 | 
 | 
Hiển thị theo cấu trúc JSON SDK trả về

"orderInfo": [
    {
      "title": "Thông tin chiều đi",
      "type": "GROUP"

 | 10 | 

 | 
Ga khởi hành
 | 

 | 
 | 
 | 
 "title": "Ga khởi hành"

  "value": "Ga Hà Nội",// Giá trị là tên ga khởi hành

  "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 11 | 

 | 
Ga đến
 | 

 | 
 | 
 | 
"title": "Ga đến", 

 "value": "Ga Hải Phòng",// Giá trị là tên ga đến 

 "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 12 | 

 | 
Ngày giờ khởi hành
 | 

 | 
 | 
 | 
"title": "Ngày giờ khởi hành", 

 "value": "10/02/2025 19:30",// Giá trị là thời gian khởi hành

  "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 13 | 

 | 
Mã chuyến tàu
 | 

 | 
 | 
 | 
 "title": "Mã chuyến tàu", 

 "value": "SE091",// Giá trị là mã chuyến tàu 

 "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 14 | 

 | 
Số ghế
 | 

 | 
 | 
 | 
 "title": "Số ghế", 

 "value": "Ghế 6 - Toa 3, Ghế 7 - Toa 2",// Giá trị là số ghế. Mỗi cặp ghế - toa cách nhau bởi dấu "," 

 "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 15 | 

 | 
Số lượng vé
 | 

 | 
 | 
 | 
"title": "Số lượng vé", 

 "value": "1",// Giá trị là số lượng vé 

 "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 16 | 
Thông tin chiều về
 | 

 | 

 | 
 | 
 | 
Hiển thị theo cấu trúc JSON SDK trả về

"orderInfo": [
    {
      "title": "Thông tin chiều về",
      "type": "GROUP"
 | 
 | 
 | 
 | 
 | 

 | 17 | 

 | 
Ga khởi hành
 | 

 | 
 | 
 | 
"title": "Ga khởi hành"

  "value": "Ga Hà Nội",// Giá trị là tên ga khởi hành

  "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 18 | 

 | 
Ga đến
 | 

 | 
 | 
 | 
"title": "Ga đến", 

 "value": "Ga Hải Phòng",// Giá trị là tên ga đến 

 "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 19 | 

 | 
Ngày giờ khởi hành
 | 

 | 
 | 
 | 
"title": "Ngày giờ khởi hành", 

 "value": "10/02/2025 19:30",// Giá trị là thời gian khởi hành

  "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 20 | 

 | 
Mã chuyến tàu
 | 

 | 
 | 
 | 
"title": "Mã chuyến tàu", 

 "value": "SE091",// Giá trị là mã chuyến tàu 

 "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 21 | 

 | 
Số ghế
 | 

 | 
 | 
 | 
"title": "Số ghế", 

 "value": "Ghế 6 - Toa 3, Ghế 7 - Toa 2",// Giá trị là số ghế. Mỗi cặp ghế - toa cách nhau bởi dấu "," 

 "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 22 | 

 | 
Số lượng vé
 | 

 | 
 | 
 | 
"title": "Số lượng vé", 

 "value": "1",// Giá trị là số lượng vé 

 "type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 23 | 
Thông tin khách hàng
 | 
 
 | 

 | 
 | 
 | 
Hiển thị theo cấu trúc JSON SDK trả về

 "orderInfo":

 "title": "Thông tin khách hàng",
 "type": "GROUP",
 | 
 | 
 | 
 | 
 | 

 | 24 | 

 | 
Tên khách hàng
 | 

 | 
 | 
 | 
"title": "Tên khách hàng","value": "Nguyễn Văn A",// Giá trị là tên của người liên hệ"type": "TITLE_VALUE"
 | 
 | 
 | 
 | 
 | 

 | 25 | 

 | 
Số điện thoại
 | 

 | 
 | 
 | 
"title": "Số điện thoại", "value": "01234567899",// Giá trị là số điện thoại của người liên hệ "type": "TITLE_VALUE
 | 
 | 
 | 
 | 
 | 

 | 26 | 

 | 
Email
 | 

 | 
 | 
 | 
 "title": "email", "value": "nhunghd@gmail.com",// Giá trị là email của người liên hệ "type": "TITLE_VALUE
 | 
 | 
 | 
 | 
 | 

 | 27 | 
Thông tin vé chiều đi
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Bao gồm (lấy từ SDK):

-      Ga khởi hành

-      Ga đến

-      Ngày giờ khởi hành: định danh dd/mm hh:mm

• Mã chuyến tàu
• Số ghế
• Số lượng vé | 
 | 
 | 
 | 
 | 

 | 28 | 
Thông tin vé chiều về (nếu có)
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Bao gồm (lấy từ SDK):

-      Ga khởi hành

-      Ga đến

-      Ngày giờ khởi hành: định danh dd/mm hh:mm

• Mã chuyến tàu
• Số ghế
• Số lượng vé | 
 | 
 | 
 | 
 | 

 | 29 | 
Thông tin người đặt
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Bao gồm (lấy từ SDK):

• Họ tên
• Số điện thoại
• Email | 
 | 
 | 
 | 
 | 

 | 30 | 
Nút Tiếp tục
 | 
Button
 | 
Click
 | -- | -- | 
• Mặc định ở trạng thái Enable<Tham khảo logic xử lý> | 
 | 
 | 
 | 
 | 

##### MH2: MH Xác nhận thanh toán
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Xác nhận giao dịch

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó với các giá trị giữ nguyên.

 | 3 | Ghi chú | Label | ReadOnly | -- | -- | Fix tại client: Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo
 | 4 | 
Thông tin xác nhận
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị thông tin xác nhận giao dịch bao gồm:

• Tài khoản nguồn
• Dịch vụ: Fix tại Client: Thanh toán vé tàu
• Mã thanh toán: Hiển thị theo kết quả tra cứu
• Tên khách hàng
• Số tiền thanh toán
• Phí giao dịch và thuế: Hiển thị kết quả tính toán do App server trả về theo dữ liệu tại BE
 | 5 | 
Hình thức xác thực:

<Tham khảo  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)>

 | 6 | 
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

##### MH4: Kết quả giao dịch
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

 | 1 | Tiêu đề màn hình | Label | ReadOnly | -- | -- | Hiển thị: Kết quả giao dịch
 | 2 | Logo Bank | Label  | ReadOnly | -- | -- | Hiển thị Logo Co-opBank
 | 3 | Tên ngân hàng | Label | ReadOnly | -- | -- | Hiển thị tên Ngân hàng Co-opBank bên cạnh logo Bank
 | 4 | Icon giao dịch thành công | Label | ReadOnly | -- | -- | Hiển thị icon giao dịch thành công
 | 5 | Tiêu đề | Label | ReadOnly | -- | -- | Tiêu đề: Thanh toán thành công
 | 6 | Số tiền giao dịch | Label | ReadOnly | -- | -- | Hiển thị số tiền đã giao dịch 
 | 7 | Thời gian giao dịch | Label | ReadOnly | -- | -- | Dữ liệu do App server trả về, định dạng: dd/mm/yyyy hh:mm
 | 8 | Dịch vụ | Label | ReadOnly | -- | -- | Hiển thị dịch vụ đã chọn thanh toán
 | 9 | Mã thanh toán | Lablel | ReadOnly | -- | -- | Hiển thị Mã thanh toán 

 | 10 | Mã giao dịch | Label | ReadOnly | -- | -- | Mã do Bank server sinh khi trừ tiền thành công
 | 11 | Lưu ý | Label | ReadOnly | -- | -- | 
Hiển thị thông tin do SDK trả về

"payment": {

"note": "Lưu ý: Mã xác nhận sẽ được gửi về email và số điện thoại liên hệ đăng ký khi đặt dịch vụ. Trong 30 phút sau khi thanh toán thành công Qúy khách hàng không nhận được thông tin vui lòng liên hệ tổng đài <a href='tel:*6789'>*6789</a> để được hỗ trợ.",// Câu note để hiển thị tại màn hình kết quả thanh toán

 | 12 | 
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

 | 13 | 
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

 | 14 | 
Nút “Tạo giao dịch mới”
 | 
Button
 | 
Click
 | -- | -- | 
Nhấn Tạo giao dịch mới, hiển thị màn hình tìm kiếm của SDK vé tàu.

#### 4/ Luồng xử lý

##### MH0: MH Thông tin thanh toán vé xem phim tại SDK
 | 
##### TT
 | 
##### Thao tác
 | 
##### Tác nhân
 | 
##### Mô tả

 | 
##### 1
 | 
##### Tại MH Thông tin thanh toán tại SDK Đặt vé tàu, nhấn chọn "Thanh toán"
 | 
##### MB Client
 | 
##### 1/ Check thông tin gói dịch vụ của KH:

• 
##### Không hợp lệ: Hiển thị thông báo tương ứng:
 | 
##### TT
 | 
##### Trường hợp lỗi
 | 
##### Nội dung
 | 
##### Xử lý (nếu có)

 | 
##### 1
 | 
##### Gói dịch vụ không bao gồm dịch vụ đã lựa chọn
 | 
##### Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ.
 | 
##### Hiển thị thông báo lỗi ở MH khổi tạo thanh toán

• 
##### Hợp lệ: Gửi yêu cầu lấy thông tin tài khoản nguồn tới Bank server qua App server

 | 
##### MB Server
 | 
##### Chuyển tiếp yêu cầu sang Bank server

 | 
##### Bank server
 | 
##### Truy vấn thông tin tài khoản nguồn và trả kết quả cho App Client qua App server

 | 
##### MB server
 | 
##### Nhận kết quả:

• 
##### Không thành công: Trả kết quả lỗi tương ứng
 | 
##### TT
 | 
##### Trường hợp lỗi
 | 
##### Nội dung
 | 
##### Xử lý (nếu có)

 | 
##### 1
 | 
##### Không lấy được danh sách tài khoản
 | 
##### Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại
 | 
##### Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.

 | 
##### 2
 | 
##### Không có tài khoản thanh toán hợp lệ
 | 
##### Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!
 | 

• 
##### Thành công: Trả kết quả danh sách tài khoản được phép thanh toán hóa đơn tới App Client

 | 
##### MB Client
 | 
##### Nhận kết quả:

• 
##### Không thành công: Hiển thị MH thông báo lỗi tương ứng

• 
##### Thành công: Hiển thị MH Khởi tạo thanh toán vé tàu: như mô tả màn hình.

##### MH1: MH Khởi tạo thanh toán
 | 
##### TT
 | 
##### Thao tác
 | 
##### Tác nhân
 | 
##### Mô tả

 | 
##### 1
 | 
##### Bấm chọn “Tài khoản nguồn”
 | 
##### MB Client
 | 
##### Kiểm tra đã lấy danh sách tài khoản thanh toán thành công chưa?

• 
##### Đã lấy thành công trước đó: Hiển thị popup chọn tài khoản nguồn gồm:

• 
##### Tiêu đề: Tài khoản nguồn

• 
##### Hiển thị. Hiển thị gồm:

• 
##### Số tài khoản

• 
##### Số dư khả dụng + đơn vị tiền tệ VND

• 
##### Chưa thành công: Gửi yêu cầu lấy danh sách tài khoản thanh toán đến MB server

 | 
##### MB server
 | 
##### Gửi yêu cầu lấy danh sách tài khoản thanh toán đến Bank server

 | 
##### Bank server
 | 
##### Xử lý và phản hồi kết quả lấy danh sách tài khoản thanh toán đến MB server

 | 
##### MB server
 | 
##### 1/ Nhận phản hồi kết quả lấy danh sách tài khoản thanh toán

• 
##### Không thành công: Trả kết quả thông báo lỗi:
 | 
##### TT
 | 
##### Trường hợp lỗi
 | 
##### Thông báo
 | 
##### Xử lý (nếu có)

 | 
##### 1
 | 
##### Không lấy được danh sách tài khoản
 | 
##### Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại
 | 
##### Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.

 | 
##### 2
 | 
##### Không có tài khoản thanh toán hợp lệ
 | 
##### Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!
 | 
##### Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.

• 
##### Thành công: Trả kết quả danh sách tài khoản được phép thanh toán hóa đơn tới App Client

 | 
##### MB Client
 | 
##### Nhận kết quả:

• 
##### TimeOut: Hiển thị popup thông báo lỗi " Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại" với button Đóng và Thử lại. Nhấn Thử lại, Client gửi yêu cầu lấy danh sách tài khoản thanh toán. Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.

• 
##### Không thành công: 

• 
##### Hiển thị popup thông báo lỗi "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!" với button Đóng. Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.

• 
##### Thành công: 

• 
##### Chỉ hiện thị các tài khoản được phép thực hiện chức năng Thanh toán vé tàu trên MH Khởi tạo

• 
##### Mặc định hiển thị tài khoản thanh toán mặc định tại màn hình khởi tạo gồm các thông tin: Số tài khoản, số dư + đơn vị tiền tệ VND. 

• 
##### Nếu không có tài khoản thanh toán mặc định (đã tất toán, không được phép thực hiện dịch vụ) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do Bank trả về

 | 
##### Chọn 1 “Tài khoản nguồn”
 | 
##### Client
 | 
##### Fill thông tin vào ô tài khoản nguồn bao gồm:

• 
##### Số tài khoản

• 
##### Số dư khả dụng + đơn vị tiền tệ VND

##### Lưu ý: Chỉ được phép chọn 1 tài khoản

 | 
##### 2
 | 
##### Nhấn Tiếp tục
 | 
##### Client
 | 
##### Gửi yêu cầu khởi tạo giao dịch

 | 
 | 
 | 
##### MB Server
 | 
##### 1/  Gửi yêu cầu truy vấn thông tin vé sang TichketTrain

> ⚠️ *Nội dung đã cắt ngắn (21212 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 18.4. URD_MB_COOPBANK_THANH TOÁN VÉ XE

> **Page ID:** `83871682` · **Version:** 7
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/83871682

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, MB Client, MB Server, Bank server, Billing system, Vexe server
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công.
• Số dư khả dụng của tài khoản thanh toán lớn hơn số tiền vé phải thanh toán.
• KH có quyền truy cập chức năng này.
• Kết quả mong muốn:
• KH thanh toán vé xem phim thành công.
• Vexe server xuất vé tự động thành công cho KH và thực hiện gửi SMS, OTT cho KH.
• Tài khoản nguồn được trừ tiền đúng bằng số tiền sau Thuế và phí, giảm giá
•  Remark: [Tên KH] TT [Tên dịch vụ] với mã thanh toán[Số mã thanh toán]
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

##### MH0: MH Thông tin thanh toán vé xe tại SDK

##### MH1: MH Khởi tạo thanh toán

##### MH2: MH Xác nhận thanh toán

##### MH3: MH Xác thực thanh toán

##### MH4: MH Kết quả thanh toán

##### MH0: MH Thông tin thanh toán vé xe tại SDK

Tham khảo SDK vé xe – version 3.1.

##### MH1: MH Khởi tạo thanh toán
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
Tiêu đề: Thanh toán vé xem phim

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Về màn hình trước đó

 | 3 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | Yes | -- | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do Bank Server trả về.Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 4 | 
Thông tin thanh toán
 | 

 | 

 | 
 | 
 | 
Hiển thị thông tin gồm:

• Mã thanh toán: Paycode
• Tổng tiền
• Số tiền được giảm: Chỉ hiện thị khi có giá trị khác 0
• Tổng tiền thanh toán: Chỉ hiển thị khi giá trị khác Tổng tiền
 | 5 | 
Thông tin vé
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Bao gồm (lấy từ SDK):

• Điểm đi
• Điểm đến
• Hãng xe
• Số ghế
• Số lượng ghế
 | 6 | 
Thông tin người đặt
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Bao gồm (lấy từ SDK):

• Họ tên
• Số điện thoại
• Email
 | 7 | 
Nút Tiếp tục
 | 
Button
 | 
Click
 | -- | -- | 
• Mặc định ở trạng thái Enable<Tham khảo logic xử lý>

##### MH2: MH Xác nhận thanh toán
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Xác nhận giao dịch

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó với các giá trị giữ nguyên.

 | 3 | Ghi chú | Label | ReadOnly | -- | -- | Fix tại client: Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo
 | 4 | 
Thông tin xác nhận
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị thông tin xác nhận giao dịch bao gồm:

• Tài khoản nguồn
• Dịch vụ: Fix tại Client: Thanh toán vé xe
• Mã thanh toán: Hiển thị theo kết quả tra cứu 
• Tên khách hàng
• Số tiền thanh toán
• Phí giao dịch và thuế: Hiển thị kết quả tính toán do MB server trả về theo dữ liệu tại BE
 | 5 | 
Hình thức xác thực:

<Tham khảo  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)>

 | 6 | 
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

##### MH4: Kết quả giao dịch
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

 | 1 | Tiêu đề màn hình | Label | ReadOnly | -- | -- | Hiển thị: Kết quả giao dịch
 | 2 | Logo Bank | Label  | ReadOnly | -- | -- | Hiển thị Logo Co-opBank
 | 3 | Tên ngân hàng | Label | ReadOnly | -- | -- | Hiển thị tên Ngân hàng Co-opBank bên cạnh logo Bank
 | 4 | Icon giao dịch thành công | Label | ReadOnly | -- | -- | Hiển thị icon giao dịch thành công
 | 5 | Tiêu đề | Label | ReadOnly | -- | -- | Tiêu đề: Thanh toán thành công
 | 6 | Số tiền giao dịch | Label | ReadOnly | -- | -- | Hiển thị số tiền đã giao dịch 
 | 7 | Thời gian giao dịch | Label | ReadOnly | -- | -- | Dữ liệu do App server trả về, định dạng: dd/mm/yyyy hh:mm
 | 8 | Dịch vụ | Label | ReadOnly | -- | -- | Hiển thị dịch vụ đã chọn thanh toán
 | 9 | Mã vé | Lablel | ReadOnly | -- | -- | Hiển thị Mã vé

 | 10 | Mã giao dịch | Label | ReadOnly | -- | -- | Mã do Bank server sinh khi trừ tiền thành công
 | 11 | 
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

 | 12 | 
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

 | 13 | 
Nút “Tạo giao dịch mới”
 | 
Button
 | 
Click
 | -- | -- | 
Nhấn Tạo giao dịch mới, hiển thị màn hình tìm kiếm của SDK vé tàu.

#### 4/ Luồng xử lý

##### MH0: MH Thông tin thanh toán vé xem phim tại SDK
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Tại MH Thông tin thanh toán tại SDK Đặt vé xe, nhấn chọn "Thanh toán" | MB Client | 
1/ Check thông tin gói dịch vụ của KH:

• Không hợp lệ: Hiển thị thông báo tương ứng: | TT | Trường hợp lỗi | Nội dung | Xử lý (nếu có)
 | 1 | Gói dịch vụ không bao gồm dịch vụ đã lựa chọn | Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ. | Hiển thị thông báo lỗi ở MH khổi tạo thanh toán

• Hợp lệ: Gửi yêu cầu lấy thông tin tài khoản nguồn tới Bank server qua MB server
 | MB Server | Chuyển tiếp yêu cầu sang Bank server
 | Bank server | Truy vấn thông tin tài khoản nguồn và trả kết quả cho MB Client qua MB server
 | MB server | 
Nhận kết quả:

• Không thành công: Trả kết quả lỗi tương ứng | TT | Trường hợp lỗi | Nội dung | Xử lý (nếu có)
 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 

• Thành công: Trả kết quả danh sách tài khoản được phép thanh toán hóa đơn tới App Client
 | MB Client | 
Nhận kết quả:

• Không thành công: Hiển thị MH thông báo lỗi tương ứng
• Thành công: Hiển thị MH Khởi tạo thanh toán vé tàu: như mô tả màn hình.

##### MH1: MH Khởi tạo thanh toán
 | TT | Thao tác | Tác nhân | Mô tả
 | 
1
 | 
Bấm chọn “Tài khoản nguồn”
 | 
MB Client
 | 
Kiểm tra đã lấy danh sách tài khoản thanh toán thành công chưa?

• Đã lấy thành công trước đó: Hiển thị popup chọn tài khoản nguồn gồm: 

• Tiêu đề: Tài khoản nguồn
• Hiển thị. Hiển thị gồm:
• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
• Chưa thành công: Gửi yêu cầu lấy danh sách tài khoản thanh toán đến MB server
 | MB server | Gửi yêu cầu lấy danh sách tài khoản thanh toán đến Bank server
 | Bank server | Xử lý và phản hồi kết quả lấy danh sách tài khoản thanh toán đến MB server
 | MB server | 
1/ Nhận phản hồi kết quả lấy danh sách tài khoản thanh toán

• Không thành công: Trả kết quả thông báo lỗi: | TT | Trường hợp lỗi | Thông báo | Xử lý (nếu có)
 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 
Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.

• Thành công: Trả kết quả danh sách tài khoản được phép thanh toán hóa đơn tới App Client
 | MB Client | 
Nhận kết quả:

• TimeOut: Hiển thị popup thông báo lỗi " Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại" với button Đóng và Thử lại. Nhấn Thử lại, Client gửi yêu cầu lấy danh sách tài khoản thanh toán. Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.
• Không thành công: 
• Hiển thị popup thông báo lỗi "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!" với button Đóng. Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.
• Thành công: 
• Chỉ hiện thị các tài khoản được phép thực hiện chức năng Thanh toán vé tàu trên MH Khởi tạo
• Mặc định hiển thị tài khoản thanh toán mặc định tại màn hình khởi tạo gồm các thông tin: Số tài khoản, số dư + đơn vị tiền tệ VND. 
• Nếu không có tài khoản thanh toán mặc định (đã tất toán, không được phép thực hiện dịch vụ) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do Bank trả về
 | 
Chọn 1 “Tài khoản nguồn”
 | 
Client
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
Lưu ý: Chỉ được phép chọn 1 tài khoản

 | 
2
 | 
Nhấn Tiếp tục
 | 
Client
 | 
Gửi yêu cầu khởi tạo giao dịch

 | 
 | 

 | 
MB Server
 | 
1/  Gửi yêu cầu truy vấn thông tin vé sang Vexe System thông qua hệ thống MB Server→  Billing system → Vexe System

 | 
 | 

 | 
Vexe System
 | 
Truy vấn thông tin vé và trả kết quả cho MB server qua Billing System

 | 
 | 
 | MB server | 
1/ Nhận kết quả truy vấn thông tin hóa đơn và Kiểm tra số dư, hạn mức dịch vụ và tính phí giao dịch

• Không hợp lệ: Cập nhật trạng thái giao giao dịch lỗi và trả kết quả lỗi tương ứng về Client: Theo Quy định kiểm tra số dư,hạn mức giao dịch với các giao dịch tài chính tại App server tại luồng khởi tạo giao dịch và bổ sung một số lỗi như dưới đây: | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý

 | 1 | Hóa đơn không tồn tại | Giao dịch không thành công do hóa đơn dịch vụ Đặt vé tàu không tồn tại. Quý khách vui lòng kiểm tra lại hoặc liên hệ tổng đài [Số điện thoại hỗ trợ] để được hỗ trợ. | <Cấu hình thông báo ở MB Server>
 | 2 | 
Mã thanh toán hết hiệu lực thanh toán
 | Mã vé hết hiệu lực thanh toán. Quý khách vui lòng kiểm tra lại. | 
<Cấu hình thông báo ở MB Server>

 | 3 | Timeout | <Theo nghiệp vụ hiện tại của mobile banking> | 

• Hợp lệ: 
• Xử lý trả về phương thức xác thực, phí dịch vụ, thông tin dịch vụ cho MB Client (Tham khảo tại URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)
• Ghi nhận trạng thái giao dịch ở phase khởi tạo thành công.
 | 
 | 

 | 
Client
 | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng mà MB Server trả về
• Thành công: 
• Hiển thị màn hình Xác nhận giao dịch với các thông tin thanh toán và hình thức xác thực MB Server trả về.

##### MH2: Màn hình xác nhận giao dịch

• Tham khảo tài liệu: URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2) | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Chọn 1 phương thức xác thực và nhấn ""Xác nhận" | MB Client | 
Chuyển sang màn hình xác thực giao dịch theo phương thức xác thực tương ứng đã chọn:

• Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)
• Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)
• Nếu phương thức xác thực là vân tay → Gửi yêu cầu xác thực giao dịch (Tham khảo logic xử lý tại Xác thực bằng Touch ID/Face ID)

##### MH3: Màn hình xác thực giao dịch
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Thực hiện xác thực theo PTXT tương ứng

 | MB Client | Xử lý thông tin validate (nếu có) và gửi yêu cầu xác thực giao dịch với PTXT tương ứng sang MB Server
 | MB Server | 
1/ Xử lý xác thực giao dịch theo PTXT (Tham khảo:  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2))

2/ Gửi yêu cầu hạch toán sang Bank Server

 | Bank Server | 
Xử lý hạch toán với Core Bank và trả kết quả:

• Không hợp lệ: Trả kết quả cho App Server | | 
 | 
Trường hợp
 | 
Thông báo
 | Xử lý (nếu có)
 | 1 | Số dư không đủ | Số dư tài khoản không đủ. Quý khách vui lòng kiểm tra lại | 

 | 2 | Số dư duy trì tối thiểu không đủ | Số dư tối thiểu duy trì tài khoản không đủ. Quý khách vui lòng kiểm tra lại | 

• Hợp lệ: Trả kết quả cho App Server
 | MB Server | 
Nhận kết quả:

• Không hợp lệ:
• Trả kết quả cho MB Client hiển thị thông báo lỗi tương ứng đã cấu hình tại bảng MB_Template
• Ghi nhận trạng thái giao dịch là Fail (Phase2 = NO)
• Timeout:
• Trả kết quả cho App Client hiển thị thông báo lỗi timeout.
• Ghi nhận trạng thái giao dịch là Timeout(Phase2 = TO)
• Hợp lệ:
• Gửi yêu cầu gạch nợ và xuất vé sang Billing system → Vexe System
• Ghi nhận trạng thái giao dịch là Thành công (Phase 2 = OK)
 | Billing System → Vexe System | 
1/ Xử lý gạch nợ và xuất vé với NCC

2/ Trả kết quả gạch nợ cho MB Client qua MB server

 | MB Server | 
1/ Nhận kết quả xác nhận giao dịch và xử lý:

• Không hợp lệ: 
• Ghi nhận trạng thái giao dịch là Fail (Phase3 = NO)
• Cấu hình hiển thị Popup thông báo lỗi tương ứng
• Gọi API đảo tiền tới Bank server và nhận kết quả:
• Không thành công: Ghi nhận trạng thái phase đảo tiền Thất bại (Phase 4 = NO)
• Thành công: Ghi nhận trạng thái phase đảo tiền Thành công (Phase 4 = OK)
• Timeout: Ghi nhận trạng thái phase đảo tiền khi không nhận được kết quả xử lý là Timeout (Phase 4 = TO)
• TimeOut:
• Ghi nhận trạng thái giao dịch là Timeout (Phase 3 = TO)
• Trả thông báo lỗi tương ứng: | | 
TT
 | 
Trường hợp
 | 
Tác nhân
 | 
Nội dung thông báo

 | 1 | TimeOut | Hệ thống MB | Yêu cầu tạm thời bị gián đoạn. Quý khách vui lòng thực hiện lại sau.

•  Hợp lệ:
• Trả kết quả GD thành công
• Cập nhật trạng thái giao dịch phase trừ tiền và gạch nợ là "Thành công" (Phase3 = OK)
 | MB Client | 
Nhận kết quả:

• Không thành công: Hiển thị Popup thông báo lỗi tương ứng
• Timeout: Hiện thị thông báo lỗi tương ứng 
•  Thành công: Hiển thị màn hình kết quả giao dịch (Như mô tả màn hình)

##### MH4: Màn hình Kết quả giao dịch
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | 
Nhấn “Tạo giao dịch mới”
 | 
MB Client
 | 
Hiển thị màn hình Đặt vé tàu

 | 2 | 
Nhấn “Home”
 | 
MB Client
 | 
Hiển thị màn hình Home với thông tin số dư được cập nhật lại sau khi thanh toán thành công

 | 3 | Chia sẻ | MB Client | Tham khảo logic xử lý chung
 | 4 | Lưu ảnh | MB Client | Tham khảo logic xử lý chung

Thông tin cấu hình trên BE:

• Nhóm dịch vụ: Thanh toán hóa đơn
• DỊch vụ → Bổ sung dịch vụ thanh toán vé xe: 1010
• Nhóm dịch vụ 630: 04 - Thanh toán hóa đơn
• Gói dịch vụ: Bổ sung hạn mức cho dịch vụ thanh toán vé xe

---

### 18.5. URD_MB_COOPBANK_THANH TOÁN VÉ XEM PHIM

> **Page ID:** `29890925` · **Version:** 39
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/29890925

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 

 | A | Bùi Thanh Thảo | 
 | 
Tạo mới
 | V.1
 | 

 | M | Hong LT | 
 | 
Map trường hiển thị theo cấu trúc Json của SDK Vé xem phim
 | 

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, App Client, App Server, Bank server, Billing system, VNPAY Film server
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công.
• KH có tài khoản nguồn hợp lệ (cấu hình rule tại Backend) để thực hiện chức năng này.
• Số dư khả dụng của tài khoản thanh toán lớn hơn số tiền vé phải thanh toán.
• KH thực hiện đặt vé và chọn Thanh toán tại màn hình Xác nhận đặt vé. Tham khảo 
• Kết quả mong muốn:
• KH thanh toán vé xem phim thành công.
• VNPAY Film xuất vé tự động thành công cho KH và thực hiện gửi SMS, Email, OTT cho KH.
• Tài khoản nguồn được trừ tiền đúng bằng số tiền sau Thuế và phí, giảm giá
•  [Tên KH] TT [Tên dịch vụ] tại NCC [Tên NCC] với mã thanh toán[Số mã thanh toán]
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

##### MH0: MH Thông tin thanh toán vé xem phim tại SDK

##### MH1: MH Khởi tạo thanh toán

##### MH2: MH Xác nhận thanh toán

##### MH3: MH Xác thực thanh toán

##### MH4: MH Kết quả thanh toán

##### MH0: MH Thông tin thanh toán vé xem phim tại SDK

Tham khảo tài liệu SDK Đặt vé xem film 2.0.1

Quy tắc chung hiển thị các trường theo cấu Json mới trả ra <Tham chiếu tài liệu> 

##### MH1: MH Khởi tạo thanh toán
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
Tiêu đề: Thanh toán vé xem phim

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
<Tham khảo logic xử lý>

 | 3 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | Yes | -- | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do Bank Server trả về.Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 4 | 
Đối với App cũ-  không tích hợp SDK có cấu trúc JSON (Giữ nguyên như cũ)

 | 5 | 
Thông tin giao dịch (App cũ- chưa cập nhật cấu trúc JSON)
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị lại thông tin vé ở màn hình xác nhận đặt vé: (Hiển thị thông tin truy vấn từ Film server)

• Tên khách hàng
• Số điện thoại: Được mã hóa
• Email
• Tổng tiền
• Số tiền được giảm: Chỉ hiện thị khi có giá trị khác 0
• Tổng tiền thanh toán: Chỉ hiển thị khi giá trị khác Tổng tiền
 | 6 | Lưu ý | Label | ReadOnly | -- | -- | 
Lưu ý: Sau khi thanh toán 5 phút, nếu Quý khách chưa nhận được thông tin vé, vui lòng liên hệ tới hotline *6789 để được hỗ trợ.

Đối với App mới - có tích hợp SDK có cấu trúc JSON → không hiển thị trường Lưu ý tại MH Khởi tạo mà hiển thị ghi chú tại MH kết quả, nội dung lưu ý do SDK trả về

 | 7 | 
 Đối với App mới - có tích hợp SDK có cấu trúc JSON (→ Map lại trường theo cấu trúc Json)

Quy tắc chung khi tích hợp SDK Json  

 | 8 | 

Thông tin thanh toán
 | 
Hiển thị theo cấu trúc JSON SDK trả về

"orderInfo": [
    {
      "title": "Thông tin thanh toán",
      "type": "GROUP

 | 9 | 

 | 
Tổng tiền
 | 

 | 
 | 
 | 
 "title": "Tổng tiền gốc",
 "value": "860,000 VND",// Giá trị là tổng tiền đơn hàng trước khuyến mại SDK, có format dấu phẩy và đơn vị tiền tệ = VND
"type": "TITLE_VALUE"

 | 10 |   | Số tiền được giảm | 

 | 
 | 
 | 
"title": "Số tiền được giảm",
"value": "60,000 VND",// Giá trị là số tiền khuyến mại SDK, có format dấu phẩy và đơn vị tiền tệ = VND, trường hợp không có khuyến mại trả giá trị = 0
 "type": "TITLE_VALUE"

 | 11 |   | Tổng tiền thanh toán | 

 | 
 | 
 | 
 "title": "Tổng tiền thanh toán",
 "value": "800,000 VND",// Giá trị là tổng tiền đơn hàng sau khuyến mại SDK, có format dấu phẩy và đơn vị tiền tệ = VND
 "type": "TITLE_VALUE"

 | 12 | 

 | 13 | 
Thông tin Khách hàng
 | 
Hiển thị theo cấu trúc JSON SDK trả về

 "orderInfo":

 "title": "Thông tin khách hàng",
 "type": "GROUP",

 | 14 | 

 | 
Tên khách hàng
 | 

 | 

 | 

 | 
"title": "Tên khách hàng",
"value": "Nguyễn Văn A",// Giá trị là tên của người liên hệ
"type": "TITLE_VALUE"

 | 15 | 

 | 
Số điện thoại
 | 

 | 

 | 

 | 
 "title": "Số điện thoại",
 "value": "01234567899",// Giá trị là số điện thoại của người liên hệ
 "type": "TITLE_VALUE

 | 16 | 

 | 
Email
 | 

 | 

 | 

 | 
 "title": "email",
 "value": "nhunghd@gmail.com",// Giá trị là email của người liên hệ
 "type": "TITLE_VALUE

 | 17 | 
Nút Tiếp tục
 | 
Button
 | 
Click
 | -- | -- | 
• Mặc định ở trạng thái Enable<Tham khảo logic xử lý>
 | 18 | 

 | 

 | 

 | 
 | 
 | 

##### MH2: MH Xác nhận thanh toán
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Xác nhận giao dịch

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó với các giá trị giữ nguyên.

 | 3 | Ghi chú | Label | ReadOnly | -- | -- | Fix tại client: Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo
 | 4 | 
Thông tin xác nhận
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị thông tin xác nhận giao dịch bao gồm:

• Tài khoản nguồn
• Dịch vụ: Fix tại Client: Đặt vé xem phim
• Nhà cung cấp: Tên rạp chiếu phim
• Mã thanh toán: Hiển thị theo kết quả tra cứu 
• Tên khách hàng:
• Số tiền thanh toán
• Phí giao dịch và thuế: Hiển thị kết quả tính toán do App server trả về theo dữ liệu tại BE
 | 5 | 
Hình thức xác thực:

<Tham khảo  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)>

 | 6 | 
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

##### MH4: Kết quả giao dịch
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

 | 1 | Tiêu đề màn hình | Label | ReadOnly | -- | -- | Hiển thị: Kết quả giao dịch
 | 2 | Logo Bank | Label  | ReadOnly | -- | -- | Hiển thị Logo Co-opBank
 | 3 | Tên ngân hàng | Label | ReadOnly | -- | -- | Hiển thị tên Ngân hàng Co-opBank bên cạnh logo Bank
 | 4 | Icon giao dịch thành công | Label | ReadOnly | -- | -- | Hiển thị icon giao dịch thành công
 | 5 | Tiêu đề | Label | ReadOnly | -- | -- | Tiêu đề: Thanh toán thành công
 | 6 | Số tiền giao dịch | Label | ReadOnly | -- | -- | Hiển thị số tiền đã giao dịch 
 | 7 | Thời gian giao dịch | Label | ReadOnly | -- | -- | Dữ liệu do App server trả về, định dạng: dd/mm/yyyy hh:mm
 | 8 | Dịch vụ | Label | ReadOnly | -- | -- | Hiển thị dịch vụ đã chọn thanh toán
 | 9 | Nhà cung cấp | Label | ReadOnly | -- | -- | 
Hiển thị tên rạp chiếu phim

Nếu tích hợp Json thì hiển thị thông tin do SDK trả về

"payment": {

"supplierName": "Rạp chiếu phim Quốc gia"// Tên rạp chiếu phim theo ngôn ngữ main app, Client bank lấy để hiển thị tại màn hình kết quả thanh toán

 | 10 | Mã thanh toán | Lablel | ReadOnly | -- | -- | Hiển thị Mã thanh toán do Film server sinh
 | 11 | Tên khách hàng | Label | ReadOnly | -- | -- | Hiển thị Tên khách hàng tương ứng
 | 12 | Mã giao dịch | Label | ReadOnly | -- | -- | Mã do Bank server sinh khi trừ tiền thành công
 | 13 | Lưu ý | Label | ReadOnly | -- | -- | 
Hiển thị thông tin do SDK trả về

"payment": {

"note": "Lưu ý: Mã xác nhận sẽ được gửi về email và số điện thoại liên hệ đăng ký khi đặt dịch vụ. Trong 30 phút sau khi thanh toán thành công Qúy khách hàng không nhận được thông tin vui lòng liên hệ tổng đài <a href='tel:*6789'>*6789</a> để được hỗ trợ.",// Câu note để hiển thị tại màn hình kết quả thanh toán

 | 14 | 
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

 | 15 | 
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

 | 16 | 
Nút “Tạo giao dịch mới”
 | 
Button
 | 
Click
 | -- | -- | 
Nhấn Tạo giao dịch mới, hiển thị màn hình khởi tạo giao dịch mới của thanh toán hóa đơn tương ứng (tài khoản nguồn được cập nhật số dư).

#### 4/ Luồng xử lý

##### MH0: MH Thông tin thanh toán vé xem phim tại SDK
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Tại MH Thông tin thanh toán tại SDK Đặt vé xem phim, nhấn chọn "Thanh toán" | App Client | 
1/ Xử lý yêu cầu đặt và hold vé sang Film system (Tham khảo xử lý tại URD SDK film)

2/ Check thông tin gói dịch vụ của KH:

• Không hợp lệ: Hiển thị thông báo tương ứng: | TT | Trường hợp lỗi | Nội dung | Xử lý (nếu có)
 | 1 | Gói dịch vụ không bao gồm dịch vụ đã lựa chọn | Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ. | Hiển thị thông báo lỗi ở MH khổi tạo thanh toán

• Hợp lệ: Gửi yêu cầu lấy thông tin tài khoản nguồn tới Bank server qua App server
 | App Server | Chuyển tiếp yêu cầu sang Bank server
 | Bank server | Truy vấn thông tin tài khoản nguồn và trả kết quả cho App Client qua App server
 | App server | 
Nhận kết quả:

• Không thành công: Trả kết quả lỗi tương ứng | TT | Trường hợp lỗi | Nội dung | Xử lý (nếu có)
 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 

• Thành công: Kiểm tra theo rule quy định tại BE và cấu hình hiển thị các tài khoản được phép thanh toán hóa đơn tới App Client; Trả kết quả MH khởi tạo thanh toán
 | App Client | 
Nhận kết quả:

• Không thành công: Hiển thị MH popup thông báo lỗi tương ứng
• Thành công: Hiển thị MH Khởi tạo thanh toán vé xem phim với thông tin về tk nguồn và thông tin về đặt vé do SDK film chuyền sang

##### MH1: MH Khởi tạo thanh toán
 | TT | Thao tác | Tác nhân | Mô tả
 | 
1
 | 
Bấm chọn “Tài khoản nguồn”
 | 
Client
 | 
Kiểm tra đã lấy danh sách tài khoản thanh toán thành công chưa?

• Đã lấy thành công trước đó: Hiển thị popup chọn tài khoản nguồn gồm danh sách các tài khoản nguồn do server trả về có rule debit = yes của giao dịch TTHĐ
• Tiêu đề: Tài khoản nguồn
• Hiển thị. Hiển thị gồm:
• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
• Chưa thành công: Gửi yêu cầu lấy danh sách tài khoản thanh toán đến MB server
 | MB server | Gửi yêu cầu lấy danh sách tài khoản thanh toán đến Bank server
 | Bank server | Xử lý và phản hồi kết quả lấy danh sách tài khoản thanh toán đến MB server
 | MB server | 
1/ Nhận phản hồi kết quả lấy danh sách tài khoản thanh toán

• Không thành công: Trả kết quả thông báo lỗi: | TT | Trường hợp lỗi | Thông báo | Xử lý (nếu có)
 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.

• Thành công: Kiểm tra theo rule quy định tại BE và cấu hình hiển thị các tài khoản được phép thanh toán hóa đơn tới App Client
 | App Client | 
Nhận kết quả:

• TimeOut: Hiển thị popup thông báo lỗi " Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại" với button Đóng và Thử lại. Nhấn Thử lại, Client gửi yêu cầu lấy danh sách tài khoản thanh toán. Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.
• Không thành công: 
• Hiển thị popup thông báo lỗi "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!" với button Đóng. Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.
• Thành công: 
• Chỉ hiện thị các tài khoản được phép thực hiện chức năng Thanh toán vé xem film trên MH Khởi tạo thanh toán vé xem film
• Mặc định hiển thị tài khoản thanh toán mặc định tại màn hình khởi tạo gồm các thông tin: Số tài khoản, số dư + đơn vị tiền tệ VND. 
• Nếu không có tài khoản thanh toán mặc định (đã tất toán, không được phép thực hiện dịch vụ) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do Bank trả về
 | 
Chọn 1 “Tài khoản nguồn”
 | 
Client
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
Lưu ý: Chỉ được phép chọn 1 tài khoản

 | 
2
 | 
Nhấn Tiếp tục
 | 
Client
 | 
Gửi yêu cầu khởi tạo giao dịch

 | 
 | 

 | 
MB Server
 | 
1/  Gửi yêu cầu truy vấn thông tin vé sang VNPAY Film thông qua hệ thống MB Server→  Billing system → Hệ thống VNPAY Film

 | 
 | 

 | 
VNPAY Film
 | 
Truy vấn thông tin vé và trả kết quả cho MB server qua Vnpay Billing

 | 
 | 
 | MB server | 
1/ Nhận kết quả truy vấn thông tin hóa đơn và Kiểm tra hạn mức dịch vụ và tính phí giao dịch

• Không hợp lệ: Cập nhật trạng thái giao giao dịch lỗi và trả kết quả lỗi tương ứng về Client: Theo Quy định kiểm tra hạn mức giao dịch với các giao dịch tài chính tại App server tại luồng khởi tạo giao dịch và bổ sung một số lỗi như dưới đây: | | 
 | 
Trường hợp
 | 
Tác nhân
 | 
Nội dung thông báo
 | 
Xử lý

 | 1 | Mã vé hết hiệu lực thanh toán (billing trả về mã lỗi 50, app server define về 1 mã lỗi riêng để phân biệt với mã lỗi 50 của TTHĐ) | App server | Mã vé hết hiệu lực thanh toán. Quý khách vui lòng kiểm tra lại. | 

• Hợp lệ: 
• Xử lý trả về phương thức xác thực, phí dịch vụ, thông tin dịch vụ cho App Client (Tham khảo tại URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)
• Ghi nhận trạng thái giao dịch ở phase khởi tạo thành công.
 | 
 | 

 | 
Client
 | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng mà App Server trả về
• Thành công: 
• Hiển thị màn hình Xác nhận giao dịch với các thông tin thanh toán và hình thức xác thực App Server trả về.
 | 3 | Nhấn Back | Client | Hiển thị thông báo: "Giao dịch đang thực hiện của Quý khách sẽ bị Hủy để cập nhật tình trạng ghế ngồi còn trống mới nhất. Vui lòng chọn Đồng ý để tiếp tục Thanh toán hoặc chọn Hủy để thực hiện một giao dịch khác" kèm 2 button "Hủy" và "Đồng ý". Nhấn "Hủy" giữ nguyên MH hiện tại. Nhấn "Đồng ý" về MH danh sách Film

##### MH2: Màn hình xác nhận giao dịch

• Tham khảo tài liệu: URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2) | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Chọn 1 phương thức xác thực và nhấn ""Xác nhận" | App Client | Xử lý thông tin validate (nếu có) và gửi yêu cầu xác nhận giao dịch với PTXT tương ứng sang App Server
 | App Server | Xử lý và trả kết quả xác nhận giao dịch cho App Client theo PTXT tương ứng, ghi nhận giao dịch ở trạng thái "Chờ xác thực"
 | App Client | 
Nhận kết quả và hiển thị màn hình xác thực giao dịch

##### MH3: Màn hình xác thực giao dịch
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Thực hiện xác thực theo PTXT tương ứng

 | App Client | Xử lý thông tin validate (nếu có) và gửi yêu cầu xác thực giao dịch với PTXT tương ứng sang App Server
 | App Server | 
1/ Xử lý xác thực giao

> ⚠️ *Nội dung đã cắt ngắn (17622 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 18.6. URD_MB_COOPBANK_THANH TOÁN VNSHOP

> **Page ID:** `101548843` · **Version:** 27
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/101548843

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
07/11/2022
 | A | TuanVN1 | 
 | 
Tạo tài liệu mới
 | V.1.0.0

Mục lục

### 1/ Tóm tắt Use Case
 | Use Case Name: | Thanh toán VNSHOP
 | Use Case ID: | UC-TTVNSHOP-01
 | Use Case Description: | 
Là người dùng, thanh toán đơn hàng đã đặt trên VNSHOP

 | Actor: | 
KH, MB Client, MB server, Bank server, Billing systerm, VnShop System

 | Priority: | High
 | Trigger: | 
KH thanh toán đơn hàng đã đặt trên VNSHOP bằng hình thức thanh toán hóa đơn

 | 
Pre-Condition:
 | 
• KH đăng nhập thành công ứng dụng
• KH đã thêm hàng vào giỏ và làm thủ tục thanh toán
• KH có tài khoản nguồn hợp lệ
• TK nguồn của KH có đủ số dư để thực hiện giao dịch
 | Post-Condition: | 
• KH thực hiện thanh toán hóa đơn thành công
• Tài khoản nguồn của KH bị trừ số tiền giao dịch có bao gồm cả phí
• Hệ thống MB ghi nhận giao dịch thanh toán hóa đơn vào Transaction_history
 | Basic Flow: | 
• B1: Chọn sản phẩm cần mua và nhập thông tin
• B2: Ấn "Đặt hàng" tại màn hình Xác nhận đơn hàng
• B3: Lựa chọn tài khoản nguồn 
• B4: Ấn "Tiếp tục" tại màn hình Thanh toán đơn hàng
• B5: Lựa chọn phương thức xác thực
• B6: Ấn " Thanh toán" tại màn hình Xác nhận giao dịch
• B7: Nhập SMS OTP/Soft OTP/FaceID-TouchID để xác nhận thanh toán
• B8: Ấn "Xác nhận" tại màn hình Xác thực giao dịch
• B9: Thanh toán thành công nhận thông báo kết quả
 | Alternative Flow: | 
<Không có>

 | Exception Flow: | 
• Số tiền thanh toán của giao dịch vượt quá hạn mức giao dịch KH
• Số dư khả dụng không đủ để thực hiện thanh toán
 | Bussiness Rules: | 
<Không có>

 | Non-Funtional Requiremnt: | 
<Không có>

 | Config: | 
<Không có>

 | Database Table of Backend: | 
1. Bảng [Transaction History]: Ghi nhận lịch sử giao dịch

2. Bảng []: Cấu hình các lỗi

 | Report BE | 
Cập nhật các giao dịch thanh toán đơn hàng VNSHOP trong các báo cáo sau:

1. Báo cáo chi tiết giao dịch

2. Báo cáo chi tiết giao dịch TTHĐ

3. Báo cáo tổng hợp giao dịch

### 2/ Luồng sơ đồ

#### Sơ đồ

#### Danh sách API
 | 
 | Tên API | Luồng gọi API | Input | Output | Ghi chú
 | 1 | 
Lấy danh sách tài khoản thanh toán

(queryCurrentAcc)
 | MB Client - MB Server - Bank Server | 

Xem chi tiết
"user": tài khoản đăng nhập MB Client
"accountType": Loại tài khoản

 | 

Xem chi tiết
"accountType": Loại tài khoản
"accountNo": Số tài khoản
"accountName": Tên chủ tài khoản
"availBalance": Số dư khả dụng tài khoản
"currency": Loại tiền tệ
"accountStatus": Trạng thái tài khoản
"branchCode": Mã chi nhánh mở tài khoản
"branchName": Tên chi nhánh mở tài khoản

 | 

 | 2 | 
Lấy thông tin đơn hàng VNSHOP

(mid59)
 | MB Client - MB Server - Billing System - VNSHOP | 

Xem chi tiết
"customerBillCode": Mã khách hàng
"providerBillCode": Mã dịch vụ
"serviceBillCode": Mã nhà cung cấp

 | 

Xem chi tiết
"feeInvoice": số tiền phí
"ccy": đơn vị tiền tệ
"currentDebit": số tiền thanh toán
"totalAmout": tổng số tiền
"discountAmount": số tiền giảm
"listVnShopItems": [
  "productId": mã sản phẩm
  "productName": tên sản phẩm
  "productNum": số lượng
  "productValue": giá tiền
  "totalValue": tổng tiền
         ]

 | 

 | 3 | 
Truy vấn thông tin thanh toán

(requestbilling)
 | MB Client - MB Server - Billing System - VNSHOP | 

Xem chi tiết
"ServiceCode": Mã dịch vụ
"ProviderCode": Mã nhà cung cấp
"CustomerCode": Mã khách hàng
"BankCode": Mã ngân hàng
"productCode": Mã sản phẩm
"Channel": Kênh giao dịch
"AccountNo": Số tài khoản
"LocalDateTime": Thời gian phát sinh giao dịch

 | 

Xem chi tiết
"RespCode": Trạng thái truy vấn
"ServiceCode": Mã dịch vụ
"ProviderCode": Mã nhà cung cấp
"CustomerCode": Mã khách hàng
"BankCode": Mã ngân hàng
"Channel": Kênh giao dịch
"AccountNo": Số tài khoản
"amount": Số tiền thanh toán
"FeeAmount": Số tiền có phí (nếu có)

 | Providercode: 834900    
ServiceCode: 834901    
 | 4 | 
Hạch toán giao dịch    

(billPayment)
 | MB Server - Bank Server | 

Xem chi tiết
"accountNo": Số tài khoản
"amount": Số tiền thanh toán
"transFee": Tiền phí
"transVAT": Tiền VAT
"productCode": Mã sản phẩm
"provider": Mã Nhà cung cấp dịch vụ

 | 

Xem chi tiết
"accountNo": Số tài khoản
"amount": Số tiền thanh toán
"transFee": Tiền phí
"transVAT": Tiền VAT

 | 

 | 5 | 
Gạch nợ hóa đơn    

(paymentbilling)
 | 
MB Server - Billing System
 | 

Xem chi tiết
"amount": Số tiền thanh toán
"ServiceCode": Mã dịch vụ
"ProviderCode": Mã nhà cung cấp
"CustomerCode": Mã khách hàng
"BankCode": Mã ngân hàng
"Channel": Kênh giao dịch
"accountNo": Số tài khoản
"LocalDateTime": Thời gian phát sinh giao dịch

 | 

Xem chi tiết
"RespCode": Trạng thái truy vấn
"ServiceCode": Mã dịch vụ
"ProviderCode": Mã nhà cung cấp
"CustomerCode": Mã khách hàng
"BankCode": Mã ngân hàng
"Channel": Kênh giao dịch
"AccountNo": Số tài khoản
"amount": Số tiền thanh toán
"VnPayDateTime": Thời gian thực hiện giao dịch

 | 

 | 6 | 
Đảo tiền giao dịch    

(reversePayment)
 | MB Server - Bank Server | 

Xem chi tiết
"orgRefNo": Số bút toán gốc

 | 

Xem chi tiết
"transRefNo": Số giao dịch

 | 

### 3/ Luồng màn hình

#### Danh sách màn hình

MH1: Home

MH2: Xác nhận đơn hàng

MH3: Thanh toán đơn hàng

MH4: Xác nhận giao dịch

MH5: Xác thực giao dịch

MH6: Kết quả giao dịch

#### Mô tả màn hình

##### MH1: Home

<Tham khảo >
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | Nhóm chức năng mua sắm
 | 1 | Mua sắm VNSHOP | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình trang chủ của SDK VNSHOP

MH2: Xác nhận đơn hàng

<Theo định nghĩa tại màn hình đặt hàng VnShop>

##### MH3: Thanh toán đơn hàng
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đều | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Tiêu đề: Thanh toán đơn hàng
 | 2 | Icon Back | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn Back, hiển thị màn hình trước đó
 | 3 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | 
Yes
 | 
--
 | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do Bank Server trả về.

Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.

Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 4 | 
Thông tin thanh toán
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị thông tin gồm:

• Dịch vụ: thanh toán đơn hàng vnshop
• Mã đơn hàng: customerBillCode
• Giá trị đơn hàng: totalAmout (tổng của thành tiền của các loại sp)
• Phí giao hàng: feeInvoice
• Số tiền giảm, hiển thị khi số tiền khác 0: discountAmount
• Tổng tiền thanh toán: currentDebit
 | 5 | 
Danh sách sản phẩm
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn chọn sẽ ẩn/hiện danh sách sản phẩm, mặc định là ẩn

Danh sách về các sản phẩm gồm các thông tin:

• Tên sản phẩm: productName
• Số lượng: productNum
• Đơn giá: productValue
• Thành tiền: totalValue
 | 6 | 
Tiếp tục
 | 
Button
 | 
Click
 | 
--
 | 
--
 | Mặc định Enable<Tham khảo logic xử lý>

##### MH4: Xác nhận giao dịch
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đều | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Tiêu đề: Xác nhận giao dịch
 | 2 | Icon Back | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn Back, hiển thị màn hình trước đó
 | 3 | Ghi chú | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Fix tại Client: Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo
 | 4 | 
Thông tin xác nhận
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị thông tin xác nhận giao dịch bao gồm:

• Tài khoản nguồn
• Dịch vụ: Fix tại Client: Thanh toán đơn hàng VNSHOP
• Mã đơn hàng: Hiển thị theo kết quả tra cứu
• Số tiền thanh toán: hiển thị bằng số và chữ
• Phí giao dịch và thuế: Hiển thị kết quả tính toán do App server trả về theo dữ liệu tại BE, hiển thị khi phí khác 0
 | 5 | 
Phương thức xác thực
 | 
Combobox
 | 
List
 | 
Yes
 | 
--
 | <Tham khảo  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)>
 | 6 | 
Thanh toán
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định Enable
<Tham khảo logic xử lý>

##### MH5: Xác thực giao dịch

<Tham khảo URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)>

##### MH6: Kết quả giao dịch
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề màn hình | Label | ReadOnly | -- | -- | Hiển thị: Kết quả giao dịch
 | 2 | Logo bank | Label | ReadOnly | -- | -- | Hiển thị Logo Co-opBank
 | 3 | Tên ngân hàng | Label | ReadOnly | -- | -- | Hiển thị tên Ngân hàng Co-opBank bên cạnh logo Bank
 | 4 | Icon giao dịch thành công | Icon | ReadOnly | -- | -- | Hiển thị icon giao dịch thành công
 | 5 | Tiêu đề | Label | ReadOnly | -- | -- | Tiêu đề: Thanh toán thành công
 | 6 | Số tiền giao dịch | Label | ReadOnly | -- | -- | Hiển thị số tiền đã giao dịch
 | 7 | Thời gian giao dịch | Label | 
ReadOnly
 | -- | -- | 
Dữ liệu do App server trả về, định dạng: dd/mm/yyyy hh:mm

 | 8 | Dịch vụ | Label | ReadOnly | 
--
 | -- | Hiển thị dịch vụ đã chọn thanh toán
 | 9 | Mã đơn hàng | Label | ReadOnly | 
--
 | -- | Hiển thị Mã đơn hàng
 | 10 | Mã giao dịch | Label | ReadOnly | 
--
 | -- | Mã do Bank server sinh khi trừ tiền thành công
 | 11 | Icon chia sẻ | Icon | 
Click
 | 
--
 | 
--
 | 
Nhấn Chia sẻ, Hiển thị popup lựa chọn kênh chia sẻ của thiết bị đã cài đặt

<Logic Tham khảo tính năng Chia sẻ của ứng dụng>

 | 12 | Icon lưu ảnh | Icon | Click | -- | -- | Nhấn Image, Lưu ảnh về thư viện hình ảnh của thiết bị
 | 13 | Tạo giao dịch mới | Button | Click | -- | -- | Nhấn Tạo giao dịch mới, hiển thị màn hình mua hàng của VNSHOP

### 4/ Luồng xử lý

##### Truy cập chức năng

a. MH1: Home

<Tham khảo >

b. MH2: Xác nhận đơn hàng
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Tại màn hình Đặt hàng tại SDK VNSHOP, nhấn "Đặt hàng"

 | MB Client | 
Kiểm tra thông tin gói dịch vụ của KH

• Không thành công: Hiển thị thông báo lỗi | | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung
 | 
Xử lý (nếu có)

 | 1 | Gói dịch vụ không bao gồm dịch vụ đã lựa chọn | Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ. | Hiển thị thông báo lỗi ở MH Thanh toán đơn hàng

• Thành công: Gọi đồng thời api lấy ds tài khoản nguồn và api lấy thông tin lấy thông tin đơn hàng. 
 | 
MB Server
 | 
Chuyển tiếp yêu cầu lấy danh sách tài khoản nguồn sang Bank Server

Chuyển tiếp yêu cầu truy vấn thông tin đơn hàng sang VnShop System thông qua hệ thống MB Server→  Billing system → VnShop System

 | 
Bank Server
 | 
Nhận yêu cầu lấy danh sách tài khoản nguồn, xử lý và phản hồi kết quả đến MB server

 | 
Billing System
 | 
Chuyển tiếp yêu cầu lấy thông tin đơn hàng từ MB server đến VNSHOP systerm

Nhận kết quả phản hồi từ VNSHOP systerm và trả kết quả cho MB server

 | 
MB Server
 | 
Nhận kết quả từ Bank Server và Billing, xử lý theo quy tắc như sau:

- Không thành công: trả thông báo lỗi cho MB Client
 | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung
 | 
Xử lý (nếu có)

 | 1 | Lấy thông tin tài khoản nguồn lỗi Timeout, lấy thông tin đơn hàng thành công | Thông báo Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Tắt thông báo vẫn hiển thị MH Thanh toán đơn hàng và danh sách sản phẩm, Tài khoản nguồn để trống, khi nhấn chọn Tài khoản nguồn thì gửi lại yêu cầu lấy thông tin tài khoản
 | 2 | Không có tài khoản thanh toán hợp lệ, lấy thông tin đơn hàng thành công | Thông báo Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | Tắt thông báo sẽ về MH home của app bank
 | 3 | Lấy thông tin tài khoản nguồn lỗi Timeout, lấy thông tin đơn hàng lỗi (timeout, hóa đơn không tồn tại, hóa đơn hết hiệu lực) | Thông báo lỗi tương ứng khi truy vấn thông tin đơn hàng lỗi | Tắt thông báo sẽ về MH home của VNSHOP
 | 4 | Không có tài khoản thanh toán hợp lệ, lấy thông tin đơn hàng lỗi (timeout, hóa đơn không tồn tại, hóa đơn hết hiệu lực) | Thông báo Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | Tắt thông báo sẽ về MH home của app bank
 | 5 | Lấy thông tin tài khoản nguồn thành công, lấy thông tin đơn hàng lỗi (timeout, hóa đơn không tồn tại, hóa đơn hết hiệu lực) | Thông báo lỗi tương ứng khi truy vấn thông tin đơn hàng lỗi | Tắt thông báo sẽ về MH home của VNSHOP

- Thành công: gửi ds TK nguồn và thông tin sản phẩm tới MB client

 | 
 | 

 | 
MB Client
 | 
- Không thành công: hiển thị thông báo lỗi và điều hướng màn hình

- Thành công: hiển thị MH Thanh toán đơn hàng

##### MH3: Thanh toán đơn hàng
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Bấm chọn “Tài khoản nguồn”

 | MB Client | 
Kiểm tra đã lấy danh sách tài khoản thanh toán thành công chưa?

• Đã lấy thành công trước đó: Hiển thị popup chọn tài khoản nguồn gồm:

• Tiêu đề: Tài khoản nguồn
• Hiển thị. Hiển thị gồm:
• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
• Chưa thành công: Gửi yêu cầu lấy danh sách tài khoản thanh toán đến MB server
 | MB server | Gửi yêu cầu lấy danh sách tài khoản thanh toán đến Bank server
 | Bank server | Xử lý và phản hồi kết quả lấy danh sách tài khoản thanh toán đến MB server
 | MB server | 
Nhận phản hồi kết quả lấy danh sách tài khoản thanh toán

• Không thành công: Trả kết quả thông báo lỗi: | | 
TT
 | 
Trường hợp lỗi
 | 
Thông báo
 | 
Xử lý (nếu có)

 | 1 | Lỗi Timeout | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 
Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.

• Thành công: Trả kết quả danh sách tài khoản được phép thanh toán hóa đơn tới MB Client
 | MB Client | 
Nhận kết quả:

• TimeOut: Hiển thị popup thông báo lỗi " Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại" với button Đóng và Thử lại. Nhấn Thử lại, Client gửi yêu cầu lấy danh sách tài khoản thanh toán. Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.
• Không thành công: 
• Hiển thị popup thông báo lỗi "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!" với button Đóng. Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.
• Thành công: 
• Hiển thị danh sách các tài khoản thanh toán
• Mặc định hiển thị tài khoản thanh toán tại màn hình khởi tạo gồm các thông tin: Số tài khoản, số dư + đơn vị tiền tệ VND. 
• Nếu không có tài khoản thanh toán mặc định (đã tất toán, không được phép thực hiện dịch vụ) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do Bank trả về
 | 
Chọn 1 “Tài khoản nguồn”
 | 
MB Client
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
Lưu ý: Chỉ được phép chọn 1 tài khoản

 | 
2
 | 
Nhấn Tiếp tục

 | 
MB Client
 | 
Gửi yêu cầu kiểm tra thông tin hạn mức giao dịch

 | 
MB Server
 | 
Nhận yêu cầu và kiểm tra thông tin hạn mức giao dị

> ⚠️ *Nội dung đã cắt ngắn (19314 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 18.7. bankProductcode

> **Page ID:** `129433608` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/129433608

Khai báo trên MB server cho các dịch vụ thanh toán hóa đơn và sdk

 | STT | Tên dịch vụ | Code
 | 1 | Hóa đơn tiền điện | TOPUP60
 | 2 | Hóa đơn tiền nước | TOPUP61
 | 3 | Cước di động trả sau | TOPUP62
 | 4 | Cước điện thoại cố định | TOPUP63
 | 5 | Cước internet ADSL | TOPUP64
 | 6 | Cước truyền hình cáp | TOPUP65
 | 7 | Thanh toán vé máy bay | TOPUP66
 | 8 | Thanh toán học phí | TOPUP67
 | 9 | Nạp tiền TK VETC | TOPUP68
 | 10 | Nạp tiền điện thoại | TOPUP69
 | 11 | Thanh toán vé xem phim | TOPUP70
 | 12 | Thanh toán vé tàu | TOPUP71
 | 13 | Thanh toán vé xe | TOPUP72
 | 14 | Mua sắm VNSHOP | TOPUP73
 | 15 | Thanh toán phòng khách sạn | TOPUP74
 | 16 | Thanh toán gọi Taxi | TOPUP75
 | 17 | Thanh toán gọi Taxi sân bay | TOPUP76

---

### 18.8. URD_MB_COOPBANK_ĐẶT PHÒNG KHÁCH SẠN

> **Page ID:** `151454054` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/151454054

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*4 trang con:*

#### 18.8.1. UC-HOTEL-01: Usecase Summary

> **Page ID:** `151454790` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/151454790

| Use Case Name | Đặt phòng khách sạn
 | Use Case ID | uc-hotel-01
 | Use Case Description | 
Là người dùng, tôi muốn đặt phòng khách sạn thành công

 | Actor | 
KH, App Client, App server, Bank server, Billing systerm, Hotel System

 | Priority | 
trueYellowmedium

 | Trigger | 
KH đặt phòng khách sạn và thực hiện thanh toán

 | 
Pre-Condition
 | 
• KH truy cập chức năng "Đặt phòng khách sạn"
• KH có gói dịch vụ được sử dụng chức năng này
• KH có tài khoản nguồn hợp lệ
• TK nguồn của KH có đủ số dư để thực hiện giao dịch
 | Post-Condition | 
• KH thực hiện thanh toán thành công
• Tài khoản nguồn của KH bị trừ số tiền tương ứng với số tiền giao dịch trừ phí (nếu có)
• Hệ thống MB ghi nhận giao dịch thanh toán của KH
• Hệ thống MB ghi nhận log giao dịch thanh toán của KH
 | Basic Flow | 
• KH truy cập chức năng "Đặt phòng khách sạn"
• KH chọn/nhập thông tin để đặt phòng
• KH thực hiện khởi tạo giao dịch
• KH thực hiện xác thực giao dịch
• KH nhận được kết quả giao dịch thành công
 | Alternative Flow | 
<Không có>

 | Exception Flow | 
• KH hủy giao dịch
• Số tiền thanh toán của giao dịch vượt quá hạn mức giao dịch KH
• Số dư khả dụng không đủ để thực hiện thanh toán
 | Bussiness Rules | 

 | Non-Funtional Requirement |

---

#### 18.8.2. UC-HOTEL-01: Flow Chart

> **Page ID:** `151454792` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/151454792

Mục lục
none

### 1/ Activity Diagram

trueđặt phòng ksfalseautotoptrue14418

Danh sách bước thực hiện và luồng gọi giữa các hệ thống:
 | Bước người dùng thực hiện | TT | Mục đích hệ thống giao tiếp | Luồng gọi | Ghi chú
 | 
Nhấn Thanh toán tại SDK
 | 
1
 | 
Lấy danh sách tài khoản thanh toán 
 | App Client → App Server → Bank Server | 

 | 
Màn hình khởi tạo

 | 
1
 | 
Lấy thông tin đặt phòng
 | App Client → App Server → Billing system → Hotel system | 

 | 
2
 | 
Kiểm tra hạn mức GD
 | App Client → App Server | 

 | 
3
 | 
Kiểm tra PTXT
 | App Client → App Server  | 

 | 
4
 | 
Khởi tạo giao dịch
 | App Client → App Server | 

 | 
5
 | 
Tính phí
 | App Server → Bank Server | 

 | 
Xác nhận giao dịch

 | 
1
 | 
Xác nhận giao dịch
 | App Client → App Server → Bank Server | 

 | 
2
 | 
Hạch toán giao dịch
 | App Server → Bank Server | 

 | 
3
 | 
Gạch nợ
 | App Client → App Server → Billing system → Hotel system | 

 | 
4
 | 
Đảo tiền
 | App Server → Bank Server |

---

#### 18.8.3. UC-HOTEL-01: Flow & Action Screen

> **Page ID:** `152174648` · **Version:** 6
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/152174648

Mục lục
none

### 1/ Luồng di chuyển màn hình

trueluồng MH đặt phòng ksfalseautotoptrue12811

### 2/ Luồng màn hình

##### <MH0: MH trang chủ>

##### <MH1: MH Đặt phòng của SDK>

##### <MH2: MH khởi tạo>

##### <MH3: MH Xác nhận GD>

##### <MH4: MH Xác thực GD>

##### <MH5: MH kết quả>

### 3/ Mô tả màn hình

##### <MH0: MH Home>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Đặt vé máy bay | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình trang chủ của SDK Đăt vé máy bay
 | 2 | Đặt vé xem phim | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình trang chủ của SDK Đăt vé xem phim
 | 3 | Đặt vé tàu | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình trang chủ của SDK Đăt vé tàu
 | 4 | Đặt xe liên tỉnh | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình trang chủ của SDK Đăt xe liên tỉnh
 | 5 | Mua sắm VNSHOP | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình trang chủ của Mua sắm VNSHOP
 | 6 | Đăt phòng khách sạn | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình trang chủ của SDK Đăt phòng khách sạn

##### <MH1: MH Đặt phòng của SDK>

Theo định nghĩa tại màn hình xác nhận đặt phòng của SDK Đặt phòng khách sạn

##### <MH2: MH khởi tạo>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đều | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Tiêu đề: Thanh toán đặt phòng
 | 2 | Icon Back | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn Back, hiển thị màn hình trước đó
 | 3 | Icon Home | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn Home, hiển thị màn hình Trang chủ
 | 4 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | 
Yes
 | 
--
 | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do Bank Server trả về.

Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.

Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 5 | 
Thông tin thanh toán
 | 

 | 

 | 

 | 

 | 
Các thông tin được lấy từ SDK, hiển thị thông tin gồm:

- Mã thanh toán

- Số tiền thanh toán

- Số tiền giảm: Chỉ hiện thị khi có giá trị khác 0

- Tổng tiền thanh toán: Chỉ hiển thị khi giá trị khác Số tiền thanh toán

 | 6 | 
Thông tin đặt phòng
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Các thông tin được lấy từ SDK, hiển thị thông tin gồm:

- Tên khách sạn

- Ngày nhận phòng

- Ngày trả phòng

- Số đêm

 | 7 | 
Thông tin khách hàng
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Các thông tin được lấy từ SDK, hiển thị thông tin gồm:

- Tên khách hàng

- Số điện thoại

- Email

 | 8 | 
Tiếp tục
 | 
Button
 | 
Click
 | 
--
 | 
--
 | Mặc định Enable<Tham khảo logic xử lý>

##### <MH3: MH Xác nhận GD>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đều | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Tiêu đề: Xác nhận giao dịch
 | 2 | Icon Back | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn Back, hiển thị màn hình trước đó
 | 3 | Ghi chú | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Fix tại Client: Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo
 | 4 | 
Thông tin xác nhận
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị thông tin xác nhận giao dịch bao gồm:

• Tài khoản nguồn
• Dịch vụ: Fix tại Client: Đặt phòng khách sạn
• Mã thanh toán: Hiển thị theo kết quả tra cứu
• Số tiền thanh toán: hiển thị bằng số và chữ
• Phí giao dịch và thuế: Hiển thị kết quả tính toán do App server trả về theo dữ liệu tại BE, hiển thị khi phí khác 0
 | 5 | 
Phương thức xác thực
 | 
Combobox
 | 
List
 | 
Yes
 | 
--
 | <Tham khảo  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)>
 | 6 | 
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
Mặc định Enable
<Tham khảo logic xử lý>

##### <MH4: MH Xác thực GD>

Tham khảo URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### <MH5: MH Kết quả>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề màn hình | Label | ReadOnly | -- | -- | Hiển thị: Kết quả giao dịch
 | 2 | Icon home | Icon | Click | -- | -- | Về màn hình trang chủ
 | 3 | Logo bank | Label | ReadOnly | -- | -- | Hiển thị Logo Co-opBank
 | 4 | Tên ngân hàng | Label | ReadOnly | -- | -- | Hiển thị tên Ngân hàng Co-opBank bên cạnh logo Bank
 | 5 | Icon giao dịch thành công | Icon | ReadOnly | -- | -- | Hiển thị icon giao dịch thành công
 | 6 | Tiêu đề | Label | ReadOnly | -- | -- | Tiêu đề: Thanh toán thành công
 | 7 | Số tiền giao dịch | Label | ReadOnly | -- | -- | Hiển thị số tiền đã giao dịch
 | 8 | Thời gian giao dịch | Label | 
ReadOnly
 | -- | -- | 
Dữ liệu do App server trả về, định dạng: dd/mm/yyyy hh:mm

 | 9 | Dịch vụ | Label | ReadOnly | 
--
 | -- | Hiển thị dịch vụ đã chọn thanh toán
 | 10 | Mã thanh toán | Label | ReadOnly | 
--
 | -- | Hiển thị Mã thanh toán
 | 11 | Mã giao dịch | Label | ReadOnly | 
--
 | -- | Mã do Bank server sinh khi trừ tiền thành công
 | 12 | Icon chia sẻ | Icon | 
Click
 | 
--
 | 
--
 | 
Nhấn Chia sẻ, Hiển thị popup lựa chọn kênh chia sẻ của thiết bị đã cài đặt

<Logic Tham khảo tính năng Chia sẻ của ứng dụng>

 | 13 | Icon lưu ảnh | Icon | Click | -- | -- | Nhấn Image, Lưu ảnh về thư viện hình ảnh của thiết bị
 | 14 | Tạo giao dịch mới | Button | Click | -- | -- | Nhấn Tạo giao dịch mới, hiển thị màn hình Đặt phòng khách sạn

---

#### 18.8.4. UC-HOTEL-01: User Action Flow

> **Page ID:** `152176141` · **Version:** 6
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/152176141

Mục lục
none

### 1/ Truy cập chức năng
 | TT | Tác nhân | Mô tả
 | 
#### Event 1: Tại màn hình Mua sắm, KH nhấn "Đặt phòng khách sạn"

 | 1 | Ứng dụng MB | 
Hiển thị màn hình trang chủ của SDK Đặt phòng khách sạn

### 2/ MH Đặt phòng tại SDK
 | TT | Tác nhân | Mô tả
 | 
#### Event 1: Tại màn hình Đặt phòng tại SDK, KH nhấn "Thanh toán"

 | 1 | Ứng dụng MB | 
Kiểm tra thông tin gói dịch vụ của KH

• Không hợp lệ: Hiển thị thông báo lỗi

 | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Gói dịch vụ không bao gồm dịch vụ đã lựa chọn | Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ. | 

• Hợp lệ: Gửi yêu cầu kiểm lấy danh sách tài khoản thanh toán
 | 
 | Bank | 
Xử lý truy vấn thông tin tài khoản nguồn

• Không thành công: Trả lỗi cho Ứng dụng MB

 | 
 | Trường hợp | Mã lỗi | Xử lý (nếu có)
 | 1 | Lỗi timeout không truy vấn được tài khoản thanh toán | 
 | 

 | 2 | Không có tài khoản thanh toán hợp lệ | 
 | 

• Thành công: Trả kết quả thành công cho Ứng dụng MB
 | 
 | Ứng dụng MB | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi cấu hình | Xử lý (nếu có)
 | 1 | Lỗi timeout không truy vấn được tài khoản thanh toán | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | 
 | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 
 | 

• Thành công: Hiển thị màn hình khởi tạo

### 3/ Khởi tạo giao dịch
 | TT | Tác nhân | Mô tả
 | 
#### Event 1: Tại màn hình khởi tạo giao dịch, KH nhấn chọn "Tài khoản nguồn"

 | 1 | Ứng dụng MB | 
Kiểm tra đã lấy danh sách tài khoản thanh toán thành công chưa?

• Đã lấy thành công: Hiển thị popup chọn tài khoản nguồn gồm
• Tiêu đề: Tài khoản nguồn
• Hiển thị. Hiển thị gồm:
• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
• Chưa thành công: Gửi yêu cầu lấy danh sách tài khoản thanh toán
 | 2 | Bank | 
Xử lý truy vấn thông tin tài khoản nguồn

• Không thành công: Trả lỗi cho Ứng dụng MB

 | 
 | Trường hợp | Mã lỗi | Xử lý (nếu có)
 | 1 | Lỗi timeout không truy vấn được tài khoản thanh toán | 
 | 

 | 2 | Không có tài khoản thanh toán hợp lệ | 
 | 

• Thành công: Trả kết quả thành công cho Ứng dụng MB
 | 3 | Ứng dụng MB | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi cấu hình | Xử lý (nếu có)
 | 1 | Lỗi timeout không truy vấn được tài khoản thanh toán | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | 
 | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 
 | 

• Thành công:
- Hiển thị danh sách các tài khoản thanh toán

- Mặc định hiển thị tài khoản thanh toán tại màn hình khởi tạo gồm các thông tin: Số tài khoản, số dư + đơn vị tiền tệ VND. 

- Nếu không có tài khoản thanh toán mặc định (đã tất toán, không được phép thực hiện dịch vụ) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do Bank trả về

 | 
#### Event 2: Tại màn hình khởi tạo giao dịch, KH chọn 1 Tài khoản nguồn

 | 
4
 | 
Ứng dụng MB
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
Lưu ý: Chỉ được phép chọn 1 tài khoản

 | 
#### Event 3: Tại màn hình khởi tạo giao dịch, KH nhấn "Tiếp tục"

 | 
5
 | 
Ứng dụng MB
 | 
Kiểm tra validate

• Không hợp lệ: Hiển thị thông báo lỗi

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi cấu hình | Xử lý (nếu có)
 | 1 | Số dư không đủ | Số dư tài khoản không đủ. Quý khách vui lòng kiểm tra lại | 
 | 

• Hợp lệ: Gửi yêu cầu lấy thông tin đặt phòng khách sạn đến Hotel System thông qua ứng dụng MB →  Billing system → Hotel System
 | 
6
 | 
Billing system → Hotel System
 | 
Chuyển tiếp yêu cầu lấy thông tin đơn hàng từ ứng dụng MB đến Hotel System

Nhận kết quả phản hồi từ Hotel System và trả kết quả cho ứng dụng MB

 | 
7
 | 
Ứng dụng MB
 | 
Nhận kết quả truy vấn thông tin hóa đơn; Kiểm tra số dư, hạn mức dịch vụ và tính phí giao dịch

• Không hợp lệ: Cập nhật trạng thái giao dịch lỗi và hiển thị thông báo lỗi

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi cấu hình | Xử lý (nếu có)
 | 1 | Hóa đơn không tồn tại | Giao dịch không thành công do hóa đơn dịch vụ Đặt phòng khách sạn không tồn tại. Quý khách vui lòng kiểm tra lại hoặc liên hệ tổng đài [Số điện thoại hỗ trợ] để được hỗ trợ. | 
 | 

 | 2 | 
Mã thanh toán hết hiệu lực thanh toán
 | Mã đặt phòng hết hiệu lực thanh toán. Quý khách vui lòng kiểm tra lại. | 
 | 

• Hợp lệ: 
• Xử lý trả về phương thức xác thực, phí dịch vụ, thông tin dịch vụ (Tham khảo tại URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)
• Ghi nhận trạng thái giao dịch ở phase khởi tạo thành công.
• Hiển thị màn hình Xác nhận giao dịch với các thông tin thanh toán và hình thức xác thực

### 4/ Xác nhận và xác thực giao dịch
 | TT | Tác nhân | Mô tả
 | Event 1: KH kiểm tra thông tin giao dịch, chọn 1 PTXT và nhấn "Xác nhận"
 | 1 | Ứng dụng MB | 
• Xử lý thông tin validate (nếu có)
• Xử lý xác thực giao dịch theo PTXT (Tham khảo:  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2))
• Gửi yêu cầu hạch toán sang Bank Server
 | 2 | Bank | 
Xử lý hạch toán:

• Không thành công: Trả kết quả lỗi cho Ứng dụng

 | 
 | Trường hợp | Mã lỗi | Xử lý (nếu có)
 | 1 | Timeout | 
 | 

 | 2 | Số dư không đủ | 
 | 

 | 3 | Số dư duy trì tối thiểu không đủ | 
 | 

• Thành công: Trả kết quả thành công cho Ứng dụng MB
 | 3 | Ứng dụng MB | 
1/ Không nhận được kết quả:

• Cập nhật trạng thái giao dịch "Timeout" (Phase2 = TO)
• Hiển thị thông báo lỗi "Timeout"

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi cấu hình | Xử lý (nếu có)
 | 1 | Timeout | Hệ thống đang tạm thời gián đoạn. Quý khách vui lòng thử lại | 
 | 

2/ Nhận được kết quả:

• Không thành công:
• Cập nhật trạng thái giao dịch "Thất bại" (Phase2 = NO)
• Hiển thị thông báo lỗi tương ứng

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi cấu hình | Xử lý (nếu có)
 | 1 | Số dư không đủ | Số dư tài khoản không đủ. Quý khách vui lòng kiểm tra lại | 
 | 

 | 2 | Số dư duy trì tối thiểu không đủ | Số dư tối thiểu duy trì tài khoản không đủ. Quý khách vui lòng kiểm tra lại | 
 | 

• Thành công:
• Cập nhật trạng thái giao dịch "Thành công" (Phase 2 = OK)
• Gửi yêu cầu gạch nợ và đặt phòng sang Billing system → Hotel System
 | 4 | 
Billing system → Hotel System
 | 
Xử lý gạch nợ và xuất mã nhận phòng với NCC

Trả kết quả gạch nợ cho ứng dụng MB

 | 5 | Ứng dụng MB | 
1/ Không nhận được kết quả:

• Cập nhật trạng thái giao dịch "Timeout" (Phase3 = TO)
• Hiển thị thông báo lỗi "Timeout"

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi cấu hình | Xử lý (nếu có)
 | 1 | Timeout | Hệ thống đang tạm thời gián đoạn. Quý khách vui lòng thử lại | 
 | 

2/ Nhận được kết quả:

• Thành công:
• Cập nhật trạng thái giao dịch "Thành công" (Phase3 = OK)
• Trả kết quả giao dịch thành công
• Không thành công:
• Cập nhật trạng thái giao dịch "Thất bại" (Phase3 = NO)
• Hiển thị thông báo lỗi tương ứng
• Gửi yêu cầu đảo tiền GD sang Bank
 | 6 | Bank | 
Xử lý đảo tiền và trả kết quả cho ứng dụng MB

 | 7 | Ứng dụng MB | 
1/ Không nhận được kết quả:

• Cập nhật trạng thái đảo tiền "Timeout" (Phase4 = TO)
2/ Nhận được kết quả:

• Không thành công:
• Cập nhật trạng thái đảo tiền "Thất bại" (Phase4 = NO)
• Thành công:
• Cập nhật trạng thái đảo tiền "Thành công" (Phase4 = OK)
• Hiển thị MH kết quả GD

---

### 18.9. URD_MB_THANH TOÁN TAXI

> **Page ID:** `201491322` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/201491322

Phiên bản tài liệu

---

*3 trang con:*

#### 18.9.1. Thanh toán gọi Taxi

> **Page ID:** `204702616` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/204702616

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*3 trang con:*

##### 18.9.1.1. [Taxi] Usecase Summary

> **Page ID:** `205456810` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/205456810

| Use Case Name | Thanh toán taxi
 | Use Case ID | uc-taxi-01
 | Use Case Description | 
Là người dùng tôi muốn đặt Taxi trên ứng dụng CoopBank và thanh toán Taxi từ tài khoản nguồn

 | Actor | 
KH, App Client, App server, Bank server, Billing systerm, Taxi System

 | Priority | 
trueYellowmedium

 | Trigger | 

 | 
Pre-Condition
 | 
• KH truy cập chức năng "Đặt taxi" và bấm Thanh toán
• KH có gói dịch vụ được sử dụng chức năng này
• KH có tài khoản nguồn hợp lệ
• TK nguồn của KH có đủ số dư để thực hiện giao dịch
 | Post-Condition | 
• KH thực hiện thanh toán thành công
• Tài khoản nguồn của KH bị trừ số tiền tương ứng với số tiền giao dịch trừ phí (nếu có)
• Hệ thống MB ghi nhận giao dịch thanh toán của KH
• Hệ thống MB ghi nhận log giao dịch thanh toán của KH
 | Basic Flow | 
• KH truy cập chức năng "Đặt taxi"
• KH nhập thông tin điểm đến/ điểm đi
• KH bấm Đặt xe
• KH bấm Thanh toán
• KH thực hiện khởi tạo giao dịch
• KH thực hiện xác thực giao dịch
• KH nhận được kết quả giao dịch thành công
 | Alternative Flow | 
<Không có>

 | Exception Flow | 
• Số tiền thanh toán của giao dịch vượt quá hạn mức giao dịch KH
• Số dư khả dụng không đủ để thực hiện thanh toán
 | Bussiness Rules | 

 | Non-Funtional Requirement |

---

##### 18.9.1.2. [Taxi] Flow& Action screen

> **Page ID:** `201491525` · **Version:** 12
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/201491525

Mục lục
none

### 1/ Luồng di chuyển màn hình

<Vẽ luồng di chuyển màn hình trực tiếp bằng Draw.io trên Confluence hoặc vẽ và đính kèm link Axure>

### 2/ Danh sách màn hình

Các cách truy cập chức năng Thanh toán taxi

##### <Cách 1: Chọn thanh toán ngay > Tiếp tục từ màn hình SDK>

<Cách 1: Chọn thanh toán ngay> Tiếp tục từ màn hình SDK>

##### <Cách 2: Chọn thanh toán từ OTT trong ứng dụng>

##### <MH1 Khởi tạo>

##### <MH 2 Xác nhận>

##### <MH 3 Xác thực>

##### <MH4 Kết quả giao dịch>

### 3/ Mô tả màn hình

##### <MH: Truy cập chức năng>

Cách 1: Truy cập từ chức năng Thanh toán ngay > Tiếp tục trong SDK (Xem mô tả mockup)

Cách 2: Truy cập từ chức năng thông báo OTT
 | | 
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

 | 1 | Màn hình OTT | 

 | 

 | 

 | 

 | 
Hiển thị tại tab Thông báo khác

 | 2 | Thông báo | 
Noti
 | 
Click
 | 
--
 | 
--
 | 
Nội dung ott lấy từ taxi system trả

 | 3 | Button "Thanh toán" | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Click Thanh toán mở đến màn hình Khởi tạo thanh toán taxi <Tham khảo logic xử lý>

Chỉ hiển thị với tin ott taxi type = 35

##### MH2: Khởi tạo giao dịch thanh toán taxi
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Thanh toán gọi taxi
 | 2 | Icon back  | 
Icon
 | 
Click
 | 
--
 | 
--
 | Click → Về MH thanh toán của SDK (Mã thanh toán của SDK giữ nguyên, ko bị reset lại do SDK taxi đã tạo mã thanh toán dựa trên tripID rồi)
 | 3 | 
Tài khoản nguồn
 | 
Combobox
 | 
Select
 | 
Yes
 | 
--
 | 
• Mặc định hiển thị tài khoản thanh toán mặc định
• Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.
• Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.
• Click vào mở ra màn hình popup “Danh sách tài khoản nguồn”, chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)
 | 
Thông tin thanh toán

 | 4 | Mã thanh toán | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Dữ liệu lấy từ SDK taxi đẩy về cho Client App.( Trường tripNo)

(Note: SDK Taxi không có thời hạn thanh toán do KH đã sử dụng dịch vụ rồi mới thanh toán)

 | 5 | Số tiền thanh toán | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
• Dữ liệu lấy từ SDK taxi đẩy về cho Client App (Trường totalPrice)
• Chỉ hiển thị khi 1 trong các trường Số tiền được giảm/ Phụ phí/ Thưởng tài xế có giá trị
 | 6 | Số tiền giảm | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
• Dữ liệu lấy từ SDK taxi đẩy về cho Client App (Trường discountAmount)
• Chỉ hiển thị khi có giá trị
 | 7 | Phụ phí | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
• Dữ liệu lấy từ SDK taxi đẩy về cho Client App (Trường surcharge)
• Chỉ hiển thị khi có giá trị
 | 8 | Thưởng tài xế | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
• Dữ liệu lấy từ SDK taxi đẩy về cho Client App (Trường tipAmount)
• Chỉ hiển thị khi có giá trị
 | 9 | Tổng tiền thanh toán | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
• Dữ liệu lấy từ SDK taxi đẩy về cho Client App (Trường paymentAmount)
 | 
Thông tin đặt xe

 | 10 | Điểm đi | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Dữ liệu lấy từ SDK taxi đẩy về cho Client App. (Trường originAddress)

 | 11 | Điểm đến | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Dữ liệu lấy từ SDK taxi đẩy về cho Client App. (Trường destinations.address)
 | 12 | Hãng xe | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Dữ liệu lấy từ SDK taxi đẩy về cho Client App. (Trường brandName)
 | 13 | Biển số xe | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Dữ liệu lấy từ SDK taxi đẩy về cho Client App. (Trường vehicleLicensePlate)
 | 13 | Button Tiếp tục | 
Button
 | 
Click
 | 
--
 | 
--
 | Click → Tham khảo logic xử lý

##### MH3: Xác nhận giao dịch thanh toán taxi
 | | 
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

 | 1 | Tiêu đề | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Xác nhận thông tin
 | 2 | Icon back  | 
Icon
 | 
Click
 | 
--
 | 
--
 | Click → Về MH Khởi tạo
 | 3 | Ghi chú | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo

 | 4 | 
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
Tài khoản nguồn đã chọn

 | 5 | Dịch vụ | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Gọi taxi

 | 6 | Mã thanh toán  | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Mã thanh toán do SDK trả từ bước trước

Bôi đỏ

 | 7 | Số tiền thanh toán | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ. Số tiền viết bằng chữ tương ứng (bôi đỏ)

(Số tiền phải thanh toán do SDK trả từ bước trước)

 | 8 | Phí giao dịch và thuế | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ (Nếu có)

 | 9 | Phương thức xác thực | 
Combobox
 | 
Select
 | 
x
 | 
--
 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 10 | Button Tiếp tục | Button | Click | -- | -- | 
Click → Tham khảo logic xử lý 

##### MH4: Kết quả giao dịch
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
2
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
Kết quả giao dịch

 | 
3
 | 
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
Hiển thị Logo Co-opBank

 | 
4
 | 
Icon thành công
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị icon giao dịch thành công

 | 
5
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
Thanh toán thành công

 | 
6
 | 
Số tiền
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Số tiền- VND

 | 
7
 | 
Thời gian giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị theo định dạng dd/mm/yyyy hh:mm

 | 
8
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
Gọi taxi

 | 
9
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
Hiển thị thông tin mã thanh toán của sdk

 | 
10
 | 
Mã giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị thông tin mã giao dịch

 | 
11
 | 
Nội dung
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị nội dung giao dịch

 | 
12
 | 
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
Nhấn Tạo giao dịch mới, hiển thị màn hình đầu tiên khi bắt đầu vào luồng SDK gọi taxi

 | 
13
 | 
Nhấn Icon lưu ảnh
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý chung

 | 
14
 | 
Nhấn Nút chia sẻ
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý chung

---

##### 18.9.1.3. [Taxi] User Action Flow

> **Page ID:** `202180492` · **Version:** 6
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/202180492

Mục lục
none

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 21/04/2023 | A | HongLT | 
 | 
Tạo mới
 | V.1

4/ Luồng xử lý

MH0: Truy cập chức năng
 | 4 | KH vào trong SDK gọi taxi → Đặt xe và bấm Thanh toán | HT MB | 
Gửi yêu cầu lấy thông tin tài khoản nguồn tới Bank server

 | Bank server | Truy vấn thông tin tài khoản nguồn và trả kết quả cho MB Client qua MB server
 | HT MB | 
Nhận kết quả:

• Không thành công: Trả kết quả lỗi tương ứng | | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 

• Thành công: Trả kết quả danh sách tài khoản được phép thanh toán hóa đơn tới App Client

MH1: Khởi tạo thanh toán
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
Chọn 1 “Tài khoản nguồn”
 | 
HT MB
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

• 
Số tài khoản

• 
Số dư khả dụng + đơn vị tiền tệ VND

Lưu ý: Chỉ được phép chọn 1 tài khoản

 | 
2
 | 
Nhấn Tiếp tục
 | 
HT MB
 | 
1/ Thực hiện khởi tạo giao dịch với số tiền là số tiền thanh toán từ SDK

2/ Kiểm tra Hạn mức/ PTXT và trả PTXT cho MB App theo logic mô tả tại 

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng
• Hợp lệ: Hiển thị màn hình Xác nhận giao dịch

MH2: Màn hình xác nhận giao dịch

• 
Tham khảo tài liệu: URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)
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
Chọn 1 phương thức xác thực và nhấn ""Xác nhận"
 | 
HT MB
 | 
Chuyển sang màn hình xác thực giao dịch theo phương thức xác thực tương ứng đã chọn:

• 
Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)

• 
Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)

• 
Nếu phương thức xác thực là vân tay → Gửi yêu cầu xác thực giao dịch (Tham khảo logic xử lý tại Xác thực bằng Touch ID/Face ID)

MH3: Màn hình xác thực giao dịch
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
Thực hiện xác thực theo PTXT tương ứng
 | 
HT MB
 | 
1/ Xử lý thông tin validate (nếu có) và gửi yêu cầu xác thực giao dịch với PTXT tương ứng sang MB Server

2/ Xử lý xác thực giao dịch theo PTXT (Tham khảo:  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2))

3/ Gửi yêu cầu hạch toán sang Bank Server

 | 
Bank Server
 | 
Xử lý hạch toán với Core Bank và trả kết quả:

• 
Không hợp lệ: Trả kết quả cho App Server
 | | 
 | 
Trường hợp
 | 
Thông báo
 | 
Xử lý (nếu có)

 | 
1
 | 
Số dư không đủ
 | 
Số dư tài khoản không đủ. Quý khách vui lòng kiểm tra lại
 | 

 | 
2
 | 
Số dư duy trì tối thiểu không đủ
 | 
Số dư tối thiểu duy trì tài khoản không đủ. Quý khách vui lòng kiểm tra lại
 | 

• 
Hợp lệ: Trả kết quả cho App Server

 | 
HT MB
 | 
Nhận kết quả:

• 
Không hợp lệ:

• 
Hiển thị thông báo lỗi tương ứng đã cấu hình tại bảng MB_Template

• 
Timeout:

• 
Hiển thị thông báo lỗi timeout

• 
Hợp lệ:

• 
Gửi yêu cầu gạch nợ sang HT Taxi

 | 
HT Taxi
 | 
1/ Xử lý gạch nợ với NCC

2/ Trả kết quả gạch nợ cho HT MB

 | 
HT MB
 | 
1/ Nhận kết quả xác nhận giao dịch và xử lý:

• 
Không hợp lệ: 

• 
Hiển thị Popup thông báo lỗi tương ứng

• 
Gọi API đảo tiền tới Bank server theo quy trình hiện tại

• 
TimeOut:

• 
Trả thông báo lỗi tương ứng:
 | | 
TT
 | 
Trường hợp
 | 
Tác nhân
 | 
Nội dung thông báo

 | 
1
 | 
TimeOut
 | 
Hệ thống MB
 | 
Yêu cầu tạm thời bị gián đoạn. Quý khách vui lòng thực hiện lại sau.

• 
 Hợp lệ:

• 
Hiển thị kết quả GD thành công

MH4: Màn hình Kết quả giao dịch
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn “Tạo giao dịch mới”
 | 
MB Client
 | 
Hiển thị màn hình đầu tiên trong SDK gọi Taxi

 | 2 | 
Nhấn “Home”
 | 
MB Client
 | 
Hiển thị màn hình Home với thông tin số dư được cập nhật lại sau khi thanh toán thành công

 | 3 | 
Chia sẻ
 | 
MB Client
 | 
Tham khảo logic xử lý chung

 | 4 | 
Lưu ảnh
 | 
MB Client
 | 
Tham khảo logic xử lý chung

---

#### 18.9.2. Thanh toán đặt taxi sân bay

> **Page ID:** `204702619` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/204702619

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*4 trang con:*

##### 18.9.2.1. [Taxi sân bay] Usecase Summary

> **Page ID:** `201491337` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/201491337

| Use Case Name | Thanh toán taxi sân bay
 | Use Case ID | uc-taxisb-01
 | Use Case Description | 
Là người dùng tôi muốn đặt Taxi sân bay trên ứng dụng CoopBank và thanh toán từ tài khoản nguồn

 | Actor | 
KH, App Client, App server, Bank server, Billing systerm, Taxi System

 | Priority | 
trueYellowmedium

 | Trigger | 

 | 
Pre-Condition
 | 
• KH truy cập chức năng "Đặt taxi" chọn tab "Taxi sân bay" và bấm Thanh toán
• KH có gói dịch vụ được sử dụng chức năng này
• KH có tài khoản nguồn hợp lệ
• TK nguồn của KH có đủ số dư để thực hiện giao dịch
 | Post-Condition | 
• KH thực hiện thanh toán thành công
• Tài khoản nguồn của KH bị trừ số tiền tương ứng với số tiền giao dịch trừ phí (nếu có)
• Hệ thống MB ghi nhận giao dịch thanh toán của KH
• Hệ thống MB ghi nhận log giao dịch thanh toán của KH
 | Basic Flow | 
• KH truy cập chức năng "Đặt taxi sân bay" 
• KH nhập thông tin điểm đến/ điểm đi trong đó có 1 điểm là sân bay
• KH bấm Đặt xe
• KH bấm Thanh toán
• KH thực hiện khởi tạo giao dịch
• KH thực hiện xác thực giao dịch
• KH nhận được kết quả giao dịch thành công
 | Alternative Flow | 
<Không có>

 | Exception Flow | 
• Số tiền thanh toán của giao dịch vượt quá hạn mức giao dịch KH
• Số dư khả dụng không đủ để thực hiện thanh toán
 | Bussiness Rules | 

 | Non-Funtional Requirement |

---

##### 18.9.2.2. [Taxi sân bay ] Flow& Action screen

> **Page ID:** `205456826` · **Version:** 11
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/205456826

Mục lục
none

### 1/ Luồng di chuyển màn hình

<Vẽ luồng di chuyển màn hình trực tiếp bằng Draw.io trên Confluence hoặc vẽ và đính kèm link Axure>

### 2/ Danh sách màn hình

Các cách truy cập chức năng Thanh toán taxi sân bay

##### <Chọn Gọi Taxi > Đặt xe sân bay từ màn hình SDK>

##### <Tiếp tục từ màn hình SDK>

##### <Thanh toán ngay từ màn hình SDK>

##### <MH1 Khởi tạo>

##### <MH 2 Xác nhận>

##### <MH2.1 Xác thực giao dịch>

##### <MH3 Kết quả giao dịch>

### 3/ Mô tả màn hình

##### <MH: Truy cập chức năng>

Truy cập từ chức năng Gọi taxi sân bay> Tiếp tục trong SDK > Thanh toán ngay trong SDK (Xem mô tả mockup)

MH1: Khởi tạo giao dịch thanh toán taxi sân bay
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Thanh toán gọi taxi sân bay
 | 2 | Icon back  | 
Icon
 | 
Click
 | 
--
 | 
--
 | Click → Về MH thanh toán của SDK
 | 3 | 
Tài khoản nguồn
 | 
Combobox
 | 
Select
 | 
Yes
 | 
--
 | 
• Mặc định hiển thị tài khoản thanh toán mặc định
• Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.
• Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.
• Click vào mở ra màn hình popup “Danh sách tài khoản nguồn”, chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)
 | 
Thông tin thanh toán

 | 4 | Mã thanh toán | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Dữ liệu lấy từ SDK taxi  sân bay đẩy về cho Client App.( Trường payCode)

(Thời hạn 15 phút)

 | 5 | Số tiền thanh toán | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
• Dữ liệu lấy từ SDK taxi đẩy về cho Client App (Trường amount)
 | 
Thông tin người đặt

 | 6 | Họ và tên | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
• Dữ liệu lấy từ SDK taxi đẩy về cho Client App. (Trường beneficiaryName)
 | 7 | Số điện thoại | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
• Dữ liệu lấy từ SDK taxi đẩy về cho Client App. (Trường beneficiaryPhone)
 | 
Thông tin đặt xe

 | 8 | Điểm đi | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
• Dữ liệu lấy từ SDK taxi đẩy về cho Client App. (Trường startLocationName)
 | 9 | Điểm đến | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
• Dữ liệu lấy từ SDK taxi đẩy về cho Client App. (Trường endLocationName)
 | 10 | Hãng xe | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
• Dữ liệu lấy từ SDK taxi đẩy về cho Client App. (Trường vehicleName)
 | 11 | Button Tiếp tục | 
Button
 | 
Click
 | 
--
 | 
--
 | Click → Tham khảo logic xử lý

##### MH2: Xác nhận giao dịch thanh toán taxi
 | | 
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

 | 1 | Tiêu đề | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Xác nhận thông tin
 | 2 | Icon back  | 
Icon
 | 
Click
 | 
--
 | 
--
 | Click → Về MH Khởi tạo
 | 3 | Ghi chú | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo

 | 4 | 
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
Tài khoản nguồn đã chọn

 | 5 | Dịch vụ | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Gọi taxi sân bay

 | 6 | Mã thanh toán  | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Mã thanh toán do SDK trả từ bước trước (bôi đỏ)

 | 7 | Số tiền thanh toán | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ. Số tiền viết bằng chữ tương ứng (bôi đỏ)

(Số tiền phải thanh toán do MB Server trả về)

 | 8 | Phí giao dịch và thuế | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ (Nếu có)

 | 9 | Phương thức xác thực | 
Combobox
 | 
Select
 | 
x
 | 
--
 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 10 | Button Tiếp tục | Button | Click | -- | -- | 
Click → Tham khảo logic xử lý 

##### MH2.1 Xác thực giao dịch
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
Xác thực giao dịch

 | 
2
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
Quý khách vui lòng nhập mã Pin của Soft OTP để xác thực giao dịch

 | 
3
 | 
Mã OTP
 | 
Text
 | 
Select
 | 
x
 | 
--
 | 
Nhập PIN Soft OTP đã đăng ký

 | 
4
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
Soft OTP sẽ bị khóa nếu Quý khách nhập sai Pin quá 5 lần liên tiếp

 | 
5
 | 
Nhấn Nút Xác nhận
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý chung

##### 3: Kết quả giao dịch
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
2
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
Kết quả giao dịch

 | 
3
 | 
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
Hiển thị Logo Co-opBank

 | 
4
 | 
Icon thành công
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị icon giao dịch thành công

 | 
5
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
Thanh toán thành công

 | 
6
 | 
Số tiền
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Số tiền- VND

 | 
7
 | 
Thời gian giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị theo định dạng dd/mm/yyyy hh:mm

 | 
8
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
Gọi taxi sân bay

 | 
9
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
Hiển thị thông tin mã thanh toán của sdk

 | 
10
 | 
Mã giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị thông tin mã giao dịch

 | 
11
 | 
Nội dung
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị nội dung giao dịch 

 | 
12
 | 
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
Nhấn Tạo giao dịch mới, hiển thị màn hình đầu tiên khi bắt đầu vào luồng SDK gọi taxi

 | 
13
 | 
Nhấn Icon lưu ảnh
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý chung

 | 
14
 | 
Nhấn Nút chia sẻ
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý chung

---

##### 18.9.2.3. [Taxi sân bay ] User Action Flow

> **Page ID:** `205456843` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/205456843

Mục lục
none

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 26/04/2023 | A | Hangnt12 | 
 | 
Tạo mới
 | V.1

4/ Luồng xử lý

MH0: Truy cập chức năng
 | 4 | KH vào trong SDK gọi taxi sân bay → Đặt xe và bấm Thanh toán ngay | HT MB | 
Gửi yêu cầu lấy thông tin tài khoản nguồn tới Bank server

 | Bank server | Truy vấn thông tin tài khoản nguồn và trả kết quả cho MB Client qua MB server
 | HT MB | 
Nhận kết quả:

• Không thành công: Trả kết quả lỗi tương ứng | | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 

• Thành công: Trả kết quả danh sách tài khoản được phép thanh toán hóa đơn tới App Client

MH1: Khởi tạo thanh toán
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
Chọn 1 “Tài khoản nguồn”
 | 
HT MB
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

• 
Số tài khoản

• 
Số dư khả dụng + đơn vị tiền tệ VND

Lưu ý: Chỉ được phép chọn 1 tài khoản

 | 
2
 | 
Nhấn Tiếp tục
 | 
HT MB
 | 
1/ Thực hiện khởi tạo giao dịch với số tiền là số tiền thanh toán từ SDK

2/ Kiểm tra Hạn mức/ PTXT và trả PTXT cho MB App theo logic mô tả tại 

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng
• Hợp lệ: Hiển thị màn hình Xác nhận giao dịch

MH2: Màn hình xác nhận giao dịch

• 
Tham khảo tài liệu: URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)
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
Chọn 1 phương thức xác thực và nhấn ""Xác nhận"
 | 
HT MB
 | 
Chuyển sang màn hình xác thực giao dịch theo phương thức xác thực tương ứng đã chọn:

• 
Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)

• 
Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)

• 
Nếu phương thức xác thực là vân tay → Gửi yêu cầu xác thực giao dịch (Tham khảo logic xử lý tại Xác thực bằng Touch ID/Face ID)

MH3: Màn hình xác thực giao dịch
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
Thực hiện xác thực theo PTXT tương ứng
 | 
HT MB
 | 
1/ Xử lý thông tin validate (nếu có) và gửi yêu cầu xác thực giao dịch với PTXT tương ứng sang MB Server

2/ Xử lý xác thực giao dịch theo PTXT (Tham khảo:  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2))

3/ Gửi yêu cầu hạch toán sang Bank Server

 | 
Bank Server
 | 
Xử lý hạch toán với Core Bank và trả kết quả:

• 
Không hợp lệ: Trả kết quả cho App Server
 | | 
 | 
Trường hợp
 | 
Thông báo
 | 
Xử lý (nếu có)

 | 
1
 | 
Số dư không đủ
 | 
Số dư tài khoản không đủ. Quý khách vui lòng kiểm tra lại
 | 

 | 
2
 | 
Số dư duy trì tối thiểu không đủ
 | 
Số dư tối thiểu duy trì tài khoản không đủ. Quý khách vui lòng kiểm tra lại
 | 

• 
Hợp lệ: Trả kết quả cho App Server

 | 
HT MB
 | 
Nhận kết quả:

• 
Không hợp lệ:

• 
Hiển thị thông báo lỗi tương ứng đã cấu hình tại bảng MB_Template

• 
Timeout:

• 
Hiển thị thông báo lỗi timeout

• 
Hợp lệ:

• 
Gửi yêu cầu gạch nợ sang HT Taxi

 | 
HT Taxi
 | 
1/ Xử lý gạch nợ với NCC

2/ Trả kết quả gạch nợ cho HT MB

 | 
HT MB
 | 
1/ Nhận kết quả xác nhận giao dịch và xử lý:

• 
Không hợp lệ: 

• 
Hiển thị Popup thông báo lỗi tương ứng

• 
Gọi API đảo tiền tới Bank server theo quy trình hiện tại

• 
TimeOut:

• 
Trả thông báo lỗi tương ứng:
 | | 
TT
 | 
Trường hợp
 | 
Tác nhân
 | 
Nội dung thông báo

 | 
1
 | 
TimeOut
 | 
Hệ thống MB
 | 
Yêu cầu tạm thời bị gián đoạn. Quý khách vui lòng thực hiện lại sau.

• 
 Hợp lệ:

• 
Hiển thị kết quả GD thành công

MH4: Màn hình Kết quả giao dịch
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn “Tạo giao dịch mới”
 | 
MB Client
 | 
Hiển thị màn hình đầu tiên trong SDK gọi Taxi

 | 2 | 
Nhấn “Home”
 | 
MB Client
 | 
Hiển thị màn hình Home với thông tin số dư được cập nhật lại sau khi thanh toán thành công

 | 3 | 
Chia sẻ
 | 
MB Client
 | 
Tham khảo logic xử lý chung

 | 4 | 
Lưu ảnh
 | 
MB Client
 | 
Tham khảo logic xử lý chung

---

##### 18.9.2.4. SOW_ Tài liệu xác định phạm vi

> **Page ID:** `204014824` · **Version:** 28
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/204014824

## 1/ Mục đích & ý nghĩa chức năng
false
• 
• Cho phép người dùng đặt trước xe cho hành trình đặc thù đi từ/đến sân bay tại một thời điểm cố định, với giá cả cạnh tranh và chất lượng được đảm bảo.
• Cho phép người dùng tìm xe phù hợp theo vị trí và thông tin đã nhập
• Người dùng có thông tin của từng xe được đề suất trong danh sách xe
• Người dùng có thể lọc hiển thị xe theo đánh giá của khách hàng và theo giá tiền
• Gửi hóa đơn thanh toán đến khách hàng theo yêu cầu
• Xem lại lịch sử đặt xe, và thông tin chi tiết chuyến
• Hỗ trợ hủy chuyến khi không còn nhu cầu hoặc cần thay đổi thông tin.

## 2/ Nguyên tắc chung

## 2/ Phạm vi

### 2.1/ FrontEnd

Vẽ và chèn sơ đồ phân rã chức năng dựa theo các trường: Epic, Story, Categorize.
 | Nhóm chức năng | Chức năng | Kênh | Mô tả | Độ khó | Phạm vi tác nhân | Thông tin API
 | 
• Đặt xe | Đặt taxi sân bay | App Client, SDK | 
Truy cập vào chức năng "Gọi Taxi" chọn tab "Taxi sân bay

• Client sẽ gửi yêu cầu đặt xe taxi sân bay cùng với thông tin (Tên chủ tài khoản, Số điện thoại, Email) sang SDK
• Nhập thông tin đặt xe trên SDK, hoàn thành xác nhận thanh toán SDk gửi về Client thông tin (Thông đặt xe, thông tin người đặt, thông tin chuyến, mã đặt chỗ, thông tin thanh toán, số tiền) | 

 | App Client, SDK, Billing server, Taxi server | 

 | 
• Khởi tạo thanh toán | Thanh toán taxi sân bay | MB Server, bank | 
• SDK gửi thông tin gửi thanh toán đến MB server (số tiền, mã thanh toán, thông tin xe)
• Mb server lấy thông tin tài khoản nguồn và khởi tạo thanh toán | 

 | MB Server, Bank, Billing server, Taxi server | 

 | 
• Xác nhận thanh toán | Thanh toán taxi sân bay | MB Server, app client | 
Hiển thị màn hình thông tin đặt xe:

• Gọi điện ( icon) số điện thoại do server trả về, gọi điện tới tổng đài chăm sóc khách hàng của NCC
• Thông tin hành trình
• Điểm đến, điểm đi, ngày giờ xuất phát, số hành khách, tên xe (Readonly)
• Thông tin người đặt xe
• Họ và tên (Lấy từ Họ tên từ app có thể chỉnh sửa)
• Số điện thoại ( Lấy từ app có thể lấy từ danh bạ hoặc nhập)
• Email (Lấy từ app có thể chỉnh sửa. theo định dạng text@text.text)
• Thông tin chuyến bay
• Loại vé Nội địa hoặc Quốc tế (click)
• Số hiệu chuyến bay (text)
• Yêu cầu khác
• Ghi chú ( text)
• Dịch vụ bổ xung

• Đón bằng điểm tên
• Đón thêm điểm
• Yêu cầu tài xế nói tiếng anh
• Bảo hiểm chuyến đi
• Lấy hóa đơn
• Tên công ty (text)
• Địa chỉ công ty (text)
• Mã số thuế (text)
• Email nhận hóa đơn (text)
• Thông tin thanh toán
• Giá cước ( giá tiền ở mục 2)
• Giá dịch vụ bổ sung khác
• Tổng thanh toán (= Giá tạm tính = <Giá cước> + <Chương trình tăng/giảm giá> + <Giá dịch vụ bổ sung>)
• Tiếp tục ( Lưu thông tin thanh toán chuyển đến bước xác nhận) | 

 | App Client, MB Server, Billing server | 
• Số điện thoại chăm sóc khách hàng của NCC
 | 
• Nhấn "Tiếp tục" / Xác nhận thanh toán | Đặt taxi sân bay | App Client | 
Hiển thị màn hình xác nhận thanh toán:

• Back (trở về màn hình Thông tin xe)
• Gọi điện ( icon) số điện thoại do server trả về, gọi điện tới tổng đài chăm sóc khách hàng của NCC
• Thông tin hành trình
• Thông tin hành trình
• Điểm đến, điểm đi, ngày giờ xuất phát, số hành khách, tên xe (Readonly)
• Thông tin người đặt xe
• Họ và tên (Readonly)
• Số điện thoại ( Readonly)
• Email (Readonly/ Ẩn nếu bước trước không được nhập)
• Thông tin chuyến bay
• Loại vé Nội địa hoặc Quốc tế (Readonly)
• Số hiệu chuyến bay (Readonly/ Ẩn nếu bước trước không được nhập)
• Yêu cầu khác
• Ghi chú (Readonly/ Ẩn nếu bước trước không được nhập)
•  Dịch vụ bổ xung (Readonly/ Ẩn nếu bước trước không được nhập)
• Lấy hóa đơn (Readonly/ Ẩn nếu bước trước không được nhập)
• Tôi đã đọc và xác nhận với Điều khoản và điều kiện dịch vụ (checkbox) 
• Nhúng link điều khoản điều kiện sử dụng dịch vụ
• Giảm giá
• Mã khuyến mãi áp dụng ( text hoặc lựa từ danh sách mã khuyến mãi bên dưới)
• Danh sách mã khuyến mãi hợp lệ
• Tên mã khuyến mãi
• Số tiền giảm
• Điều kiện áp dụng
• Hạn sử dụng
• Áp dụng/ Hủy bỏ (tự động điền mã giảm giá vào/ bỏ mã giảm giá đang được áp dụng)
• Thông tin thanh toán
• Tổng thanh toán (Readonly)
• Giảm giá (Hiển thị khi áp dụng ở mục trên)
• Chi tiết giá ( Click: Mở Popup chi tiết giá)
• Thanh toán ngay 
• 
• Khởi tạo giao dịch
• Lưu thông tin hóa đơn ở server
• Gọi sang server chuyển luồng thanh toán | 

 | App Client, MB Server, Billing server | 
• Thông tin mã khuyến mãi theo user
 | 
• Xác thực thanh toán | Thanh toán | App  Client
MB server 

MB app

Billing server
 | 
 App Client chuyển màn hình Khởi tạo thanh toán của bank tương ứng với các thông tin sau:

• Tổng tiền thanh toán
• Mã thanh toán.
• Họ tên người đặt
• SĐT người đặt
•  Điểm đi
• Điểm đến
• Thời gian đi
• Tên xe
MB app nhận yêu cầu thanh toán, xử lý tiếp các quy trình truy vấn giao dịch theo luồng thanh toán Billing
 | 

 | App  Client
MB server

Billing server

MB app
 | 
• Mid 40
• Mid 11
• Mid 41
• Mid 200
• Lấy danh sách tài khoản thanh toán
• Lấy thông tin hóa đơn
• Truy vấn thông tin thanh toán

 | 
• Thực hiện xác nhận thanh toán theo luồng bill | Thanh toán | 
MB server

Billing server
 | 
• Billing server nhận yêu cầu thanh toán, xác nhận thanh toán theo luồng Bill
• Trả kết quả đến MB server

 | 

 | 
MB app

MB server

Core banking

Billing server
 | 
• Truy vấn thông tin thanh toán
• Hạch toán giao dịch
 | 
• Trả kết quả thanh toán | Thanh toán | 
AirportCab Server

Nhà cung cấp
 | 
Ghi nhận kết quả thanh toán

• Thanh toán thành công (Gửi yêu cầu khởi tạo đơn hàng sang nhà cung cấp
• Timeout (Ghi nhận kết quả thanh toán)
• Thanh toán thất bại (Đảo tự động)
Nhà cung cấp: Ghi nhận và khởi tạo đơn trả kết quả về server

AirportCab Server nhận kết quả từ nhà cung cấp:

• Thành công
• Thay đổi trạng thái của đơn đặt xe
• Trả kết quả cho Billing
• Timeout
• Không nhận được kết quả từ nhà cung cấp
• Trả kết quả cho billing
• Gửi mail báo lỗi
• Thất bại
• Cập nhật trạng thái thất bại
• Cập nhật trạng thái cho billing đảo tiền cho khách
• Gửi mail báo lỗi | 

 | 
AirportCab Server

MB app

Nhà cung cấp
 | 
• Gạch nợ hóa đơn
• Đảo tiền giao dịch
 | 
• Hiển thị màn thanh toán thành công | Thanh toán | 
MB app
 | 
Hiển thị kết quả thanh toán thành công
 | 

 | 

 | 

 | Xem danh sách chuyến | Quản lý chuyến | 
App Client
 | 
Danh sách lịch sử đặt taxi sân bay, thông tin 1 bản ghi gồm:

• Mã thanh toán
• Ngày tạo giao dịch
• Trạng thái đặt xe
• Điểm đón, điểm đi
• Tổng thanh toán
• Mã hiệu chuyến bay (Nếu có)
• Đặt chiều về (Nếu đặt chuyến đi)
• Thanh toán ngay (khi ở trạng thái chờ thanh toán)
• Trải nghiệm ngay (Hiển thị khi danh sách lịch sử trống) | 

 | 
App Client
 | 
• Thông tin chuyến xe
• Thông tin tài xế nhận chuyến
 | Xem chi tiết chuyến | Quản lý chuyến | 
App Client
 | 
Xem thông tin chi tiết đặt xe sân bay:

• Giống màn hình xác nhận thanh toán
• Mã giao dịch (Readonly)
• Trạng thái đặt xe 
• Khởi tạo
• Đang tìm xe
• Chờ xử lý
• Tài xế đã nhận chuyến
• Hoàn thành
• Đã hủy
• Hủy bởi khách hàng
• Hủy bởi CSKH
• Hủy bởi NCC
• Hủy chuyến:
• Hiển thị khi đã thanh toán 
• Trạng thái đặt xe
• Đang tìm xe
• Chờ xử lý
• Tài xế đã nhận chuyến
• Click hiển thị popup "Hủy chuyến"
• Phí hủy chuyến (Readonly)
• Lí do hủy chuyến chọn 1 trong số lý do sau:
• Thay đổi hành trình
• Sai thông tin
• Di chuyển bằng phương tiện khác
• Lý do khác (text)
• Hủy chuyến: Chỉ thực hiện khi đã chọn lý do hủy chuyến
• Thông tin tài xế (chỉ hiển thị khi tài chế đã nhận chuyến, đã hoàn thành)
• Ảnh tài xế
• Tên tài xế
• Gọi điện
• SĐT do server trả về
• Gọi điện cho tài xế
• SMS
• Chuyển sang màn hình SMS fill sẵn SĐT tài xế
• Đánh giá chuyến đi
• Chưa đánh giá hiển thị "Đánh giá ngay" 
• Chỉ đánh giá khi chuyến đi đã hoàn thành
• Chỉ đánh giá trong 72h khi hoàn thành chuyến
• Click hiển thị popup "đánh giá chuyến đi"
• Đã đánh giá hiển thị "Xem lại đánh giá"
• Click chuyển popup "Đánh giá chuyến đi
• Popup đánh giá chuyến đi:
• Tiêu đề
• Số sao
• Mô tả ngắn
• Nội dung chia sẻ
• Tag
• Gửi
• Thông tin hành trình | 

 | 
App Client
 | 

 | Hủy chuyến/ xem lý do hủy chuyến | Quản lý chuyến | 
App Client
 | 
• Chọn "hủy chuyến" ở màn thông tin chi tiết đặt xe
• Hủy chuyến pử trạng thái:
• Đã thanh toán 
• Trạng thái đặt xe
• Đang tìm xe
• Chờ xử lý
• Tài xế đã nhận chuyến
• Click hiển thị popup "Hủy chuyến"
• Phí hủy chuyến (Readonly)
• Lí do hủy chuyến chọn 1 trong số lý do sau:
• Thay đổi hành trình
• Sai thông tin
• Di chuyển bằng phương tiện khác
• Lý do khác (text)
• Hủy chuyến: Chỉ thực hiện khi đã chọn lý do hủy chuyến | 

 | 
App Client
 | 

 | 
• Chọn mục khuyến mại/ Bấm vào ô mã giảm giá | Mã giảm giá | 
App Client
 | 

 | 

 | 

 | 
• Thông tin mã khuyễn mãi

### 2.2/ BO (Back Office)

### 2.3/ API kênh cung cấp (nếu có)
 | TT | API Name | API Description | Channel use | Input | Output
 | 1 | 
Lấy danh sách tài khoản thanh toán

(queryCurrentAcc)
 | MB Client - MB Server - Bank Server | 
 | 
 | 

 | 2 | 
Lấy thông tin đơn hàng từ NCC
 | MB Client - MB Server - Billing System - NCC | 
 | 
 | 

 | 3 | 
Truy vấn thông tin thanh toán

(requestbilling)
 | MB Client - MB Server - Billing System - VNSHOP | 
 | 
 | 

 | 4 | 
Hạch toán giao dịch    

(billPayment)
 | MB Server - Bank Server | 
 | 
 | 

 | 5 | 
Gạch nợ hóa đơn    

(paymentbilling)
 | 
MB Server - Billing System
 | 
 | 
 | 

 | 6 | 
Đảo tiền giao dịch    

(reversePayment)
 | MB Server - Bank Server | 
 | 
 | 

## 3/ Sơ đồ Diagram (Sequence/Activity/Stage)

 

## 4/ Q&A

### 4.1/ Frontend

### 4.2/ BO (Back Office)

### 4.3/ API kênh cung cấp (nếu có)

## 5/ Khác

---

#### 18.9.3. Luồng thanh toán tự động Taxi

> **Page ID:** `288589786` · **Version:** 10
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/288589786

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | 
HongLT
 | 
 | 
Tạo mới tài liệu
 | 

Mục lục
none

### 1/ Tóm tắt Use Case

 | Use Case Name | Thanh toán tự động Taxi - Bank
 | Use Case ID | --
 | Use Case Description | 
Kết thúc chuyến đi hệ thống tự động trừ tiền từ tài khoản nguồn là tài khoản thanh toán mà KH đã thực hiện liên kết thành công trước đó

 | Actor | 
KH, SDK Client, MB App, MB Server, SDK Server, CoreBank

 | Priority | High
 | Trigger | 
KH đặt xe lựa chọn PTTT tự động

 | 
Pre-Condition
 | 
KH truy cập dịch vụ Gọi Taxi và thực hiện đặt xe

 | Post-Condition | 
KH chọn PTTT tự động, liên kết tài khoản và hệ thống tự động trừ tiền khi kết thúc chuyến xe thành công

 | Basic Flow | 
1/ KH truy cập dịch vụ

2/ Thực hiện chọn điểm đến, xác nhận điểm đón và PTTT tự động

3/ Thực hiện liên kết tài khoản thanh toán tự động

4/ Đặt xe và di chuyển tới điểm đến, hệ thống tự động hạch toán trừ tiền chuyến đi khi kết thúc

 | Alternative Flow | 
--

 | Exception Flow | 
--

 | Business Rules | 
--

 | Non-Functional Requirement | 
--

### 2/ Luồng sơ đồ

#### 2.1/ Sơ đồ

trueLuồng thanh toán tự động VBAfalseautotoptrue153112

#### 2.2/ Danh sách API
 | Bước thực hiện | Tên API | Luồng gọi API | Địa chỉ API | Input | Output | Ghi chú
 | 
SDK Client gọi MB App (Client → Client)

 | Chọn Quản lý liên kết | 
Điều hướng tới màn hình danh sách tài khoản của MB App
 | SDK Client - MB App | 
 | 

 | 

 | 

 | Chọn Đặt xe | 
Gọi check số dư tới MB App
 | SDK Client - MB App | 
 | 

 | 

 | 

 | 
MB App gọi MB Server và MB Server gọi Core Bank

 | Gọi check số dư tới Core Bank | 
Nếu Core Bank trả số dư đủ + MB server kiểm tra hạn mức đủ thì MB Server sinh token 
 | MB App- MB Server - Bank | 
 | 

 | 

 | Token này dùng để xác thực cho từng giao dịch
 | 
SDK Client gọi SDK Server

 | 
Nhận kết quả từ MB App liên kết tài khoản thành công
 | 
Yêu cầu lưu trạng thái đã liên kết tài khoản thanh toán tự động
 | SDK Client - SDK Server | 
 | 

 | 

 | 

 | 
Chọn Đặt xe
 | 
Yêu cầu đặt xe (truyền token)
 | SDK Client - SDK Server | 
 | 

 | 

 | 

 | 
SDK Server gọi MB Server

 | 
Kết thúc chuyến đi
 | 
Thanh toán sử dụng Token được cấp 1 lần cho mỗi GD
 | SDK Server - MB Server | 
 | 

Xem chi tiết
{
"token":"676667676767676878",
"amount":"1000000",
} 

 | 

Xem chi tiết
{
"token":"676667676767676878",
"amount":"1000000",
} 

 | Nhập ghi chú (nếu có)

### 3/ Luồng màn hình

#### 3.1/ Danh sách màn hình

##### MH1: KH truy cập App Bank - Đặt Taxi

##### MH2: Home SDK Taxi - Chọn điểm đến 

##### MH3: Tìm kiếm điểm đến

##### MH4: Xác nhận điểm đón

##### MH5: Hiển thị giá dịch vụ

##### Bước 5.1: PTTT - Thanh toán chủ động

##### MH6: KH chọn Phương thức thanh toán - đã liên kết

##### MH6.1: KH chọn Phương thức thanh toán - chưa liên kết

##### 

##### MH6.2: KH chọn 

##### MH7: [Bank] Danh sách tài khoản

##### MH7.1: [Bank] Popup cho TK chưa liên kết  thanh toán tự động 

##### MH7.2: [Bank] KH nhập OTP xác thực liên kết

##### MH8: Đặt xe PTTT tự động

##### MH9: Lỗi không đủ số dư

##### 

##### MH10: Tìm tài xế

##### MH11: Tài xế nhận chuyến

##### 

##### MH12: Tài xế đang đến

##### MH13: Tài xế đã đến

##### MH14: Đang trong hành trình

##### MH15: Kết thúc chuyến - thanh toán tự động thành công

##### MH16: Kết thúc chuyến - thanh toán tự động thất bại -> Luồng thu bù

#### 3.2/ Mô tả màn hình

##### MH1: <Tên màn hình>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Nhập tên hạng mục mô tả, ví dụ: Tiêu đề, Tài khoản nguồn | 
Nhập kiểu hiển thị, ví dụ: Label
 | 
Nhập kiểu thao tác, ví dụ: Read Only
 | 
Nếu bắt buộc nhập Yes, để trống nếu không bắt buộc
 | 
Nhập min - max
 | Nhập các mô tả, diễn giải cho hạng mục 1 cách đầy đủ

### 4/ Luồng xử lý

##### Truy cập chức năng
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | Trường hợp 1: Đi từ đâu
 | 
1
 | 
Nhập thao tác của KH
 | App Client | 

 | App Server | 

##### MH1: <Tên màn hình>
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhập thao tác của KH | 
App Client
 | 
Kiểm tra validate:

• Không hợp lệ: Hiển thị thông báo lỗiDanh sách lỗi

 | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Nhập trường hợp lỗi (ghi rõ ràng) | Nhập nội dung thông báo lỗi. Chú ý với thông báo lỗi ở client phải rõ ràng, đầy đủ, dễ hiểu. | 

• Hợp lệ: Mô tả tiến trình xử lý tiếp theo là gì
 | 
2
 | 
Nhập thao tác của KH
 | 
App Client
 | 
Kiểm tra validate:

• 
Không hợp lệ: Hiển thị thông báo lỗi
Danh sách lỗi

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi | Xử lý (nếu có)
 | 1 | Nhập trường hợp lỗi (ghi rõ ràng) | Nhập nội dung thông báo lỗi. Chú ý với thông báo lỗi ở client phải rõ ràng, đầy đủ, dễ hiểu. | Ví dụ: BLANK_AMOUNT | 

• Hợp lệ: Mô tả tiến trình xử lý tiếp theo
 | 
App Server
 | 
Nhập các tiến trình xử lý của App Server theo tuần tự, rõ ràng, dễ hiểu. Ví dụ:

1/ Kiểm tra logic 1:

• Không hợp lệ: Trả thông báo lỗi cho ứng dụngDanh sách lỗi

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi | Xử lý  (nếu có)
 | 1 | Nhập trường hợp lỗi (ghi rõ ràng) | Nhập nội dung thông báo lỗi. Chú ý với các thông báo lỗi có sử dụng tham số động. | Ví dụ: LIMIT_28 | 

• Hợp lệ: Xử lý điều kiện kiểm tra logic 2 hoặc gửi yêu cầu sang Bank
 | Bank | 
Nhập các tiến trình xử lý của Bank (nếu nắm bắt được). Đồng thời nêu các trường hợp lỗi (do Bank xử lý và trả ra). Ví dụ:

1/ Kiểm tra OTP

• Không hợp lệ: Trả lỗi cho App ServerDanh sách lỗi

 | 
 | Mã lỗi | Mô tả ý nghĩa lỗi | Ghi chú
 | 1 | Nhập mã lỗi từ Bank. Ví dụ: 28 | Lỗi không đủ số dư | 

• Hợp lệ: Xử lý tiến trình 2
2/ Xử lý hạch toán và trả kết quả

• Không hợp lệ: Trả lỗi cho App ServerDanh sách lỗi

 | 
 | Mã lỗi | Mô tả ý nghĩa lỗi | Ghi chú
 | 1 | Nhập mã lỗi từ Bank. Ví dụ: 28 | Lỗi không đủ số dư | 

• Timeout: Trả lỗi timeout cho App Server
• Hợp lệ: Trả kết quả thành công cho App Server
 | 
App Server
 | 
Nhận kết quả:

• Không thành công:
• Tiến trình 1: Cập nhật trạng thái giao dịch "Không thành công" vào bảng [Transaction History]
• Tiến trình 2: Trả thông báo lỗi cho App Client theo mã lỗi cấu hình tại BEDanh sách lỗi

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi | Xử lý  (nếu có)
 | 1 | Nhập trường hợp lỗi (ghi rõ ràng) | Nhập nội dung thông báo lỗi. Chú ý với các thông báo lỗi có sử dụng tham số động. | Ví dụ: BANK_28 | 

• Timeout:
• Tiến trình 1: Cập nhật trạng thái giao dịch "Nghi vấn" vào bảng [Transaction History]
• Tiến trình 2: Trả thông báo lỗi timeout cho App Client
• Thành công: 
• Tiến trình 1: Cập nhật trạng thái giao dịch "Thành công" vào bảng [Transaction History]
• Tiến trình 2: Trả kết quả thành công cho App Client
 | 
App Client
 | 
Nhận kết quả:

• Không thành công: Hiển thị các thông báo lỗi tương ứng theo các trường hợp ngoại lệ xảy ra.
• Timeout: Hiển thị thông báo lỗi timeout
• Thành công: Hiển thị màn hình tiếp theo.

### 5/ Bảng dữ liệu

#### 5.1/ Bảng dữ liệu sử dụng

Bao gồm tất cả các bảng dữ liệu có sử dụng trong nghiệp vụ phân tích

 | TT | Table Name | Description | Create | Reference | Update | Delete
 | 1 | Nhập tên Table có sử dụng trong nghiệp vụ (có thể lấy từ Dev team) | Nhập mô tả mục đích của Table | Gõ "x" nếu nghiệp vụ có thao tác "Create" đến Table | Gõ "x" nếu nghiệp vụ có thao tác "Reference" đến Table | Gõ "x" nếu nghiệp vụ có thao tác "Update" đến Table | Gõ "x" nếu nghiệp vụ có thao tác "Delete" đến Table

5.2/ Thông tin cập nhật vào bảng dữ liệu

Áp dụng cho các bảng dữ liệu có sử dụng thao tác "Create", "Update"

 | TT | Table Name | Field | Value | Note
 | 1 | Nhập tên Table có sử dụng trong nghiệp vụ (có thể lấy từ Dev team) | Nhập trường dữ liệu (thuộc tính) có cập nhật giá trị dữ liệu | Nhập giá trị dữ liệu cập nhật | Nhập ghi chú thêm (nếu có)

---

### 18.10. URD_MB_MUA XỔ SỐ VIETLOT

> **Page ID:** `515867000` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/515867000

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

#### 18.10.1. [Vietlott] Flow& Action screen

> **Page ID:** `517407381` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/517407381

Mục lục
none

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | HongLT | 
 | 
Tạo mới
 | V.1
 | 
 
 | M | HongLT | 
 | 
Bổ sung trường phí giao dịch + thuế tại MH KQ để clear cho KH (do NCC Vietlott có thu phí)
 | 

 | 
 
 | M | HongLT | 
 | 
Bỏ hiển thị riêng trường phí giao dịch + thuế tại MH KQ → để cộng gộp chung vào Tổng số tiền giao dịch tại MH KQGD (do Vietlott và các nhà mạng tham gia nghiệm thu không không đồng ý tách riêng trường phí vì dễ gây hiểu nhầm cho KH) 

(Màn hình xác nhận thì vẫn tách)
 | 

### 1/ Luồng di chuyển màn hình

<Vẽ luồng di chuyển màn hình trực tiếp bằng Draw.io trên Confluence hoặc vẽ và đính kèm link Axure>

### 2/ Danh sách màn hình

Các cách truy cập chức năng Thanh toán taxi

##### MH 1: Trang chủ

##### MH 2: Trong SDK Vietlott

##### MH 3: Khởi tạo

##### MH 4 Xác nhận giao dịch

##### MH 5 Xác thực

##### <MH 6 Kết quả>

### 3/ Mô tả màn hình

##### <MH1 + MH 2 : Truy cập chức năng>
 | | 
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

 | 1 | Icon chức năng "Vietlott SMS" tại Home | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mở đến SDK Vietlott.

• KH đăng ký tài khoản Vietlott
• KH lựa chọn mua xổ số và bấm Xác nhận thanh toán
 | 2 | Bấm Xác nhận thanh toán trong SDK Vietlott | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Chuyển đến MH Khởi tạo của App

##### MH3: Khởi tạo giao dịch
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Thanh toán mua xổ số Vietlott
 | 2 | Icon back  | 
Icon
 | 
Click
 | 
--
 | 
--
 | Click Back→ Về MH chọn mua của Vietlott (Không Back được về MH thanh toán để tiếp tục thanh toán đơn hàng do nội tại của hệ thống Vietlott mỗi hóa đơn chỉ được thanh toán 1 lần)
 | 3 | 
Tài khoản nguồn
 | 
Combobox
 | 
Select
 | 
Yes
 | 
--
 | 
• Mặc định hiển thị tài khoản thanh toán mặc định
• Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.
• Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.
• Click vào mở ra màn hình popup “Danh sách tài khoản nguồn”, chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)
 | 
Thông tin thanh toán

 | 4 | Dịch vụ | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Mua xổ số Vietlott SMS
 | 
 | Mã thanh toán | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Dữ liệu lấy từ SDK Vietlott đẩy về cho Client App.( Trường Trans_id)

 | 5 | Số tiền thanh toán | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Dữ liệu lấy từ SDK Vietlott đẩy về cho Client App (Trường money)

 | 13 | Button Tiếp tục | 
Button
 | 
Click
 | 
--
 | 
--
 | Mở đến MH Xác nhận giao dịch→ Tham khảo logic xử lý

##### MH3: Xác nhận giao dịch thanh toán Vietlott
 | | 
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
Thông tin hiển thị tại MH xác nhận do MB server trả về

 | 1 | Tiêu đề | 
Label
 | 
Read Only
 | 
--
 | 
--
 | Xác nhận thông tin
 | 2 | Icon back  | 
Icon
 | 
Click
 | 
--
 | 
--
 | Click → Về MH Khởi tạo
 | 3 | Ghi chú | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo

 | 4 | 
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
Tài khoản nguồn đã chọn

 | 5 | Dịch vụ | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Mua xổ số Vietlott SMS

 | 6 | Mã thanh toán  | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Mã thanh toán

 | 7 | Số tiền thanh toán | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tiền (truy vấn từ NCC) và đơn vị tiền tệ. Số tiền viết bằng chữ tương ứng (bôi đỏ) (Trường: amount)

 | 8 | Phí giao dịch và thuế | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
• Trường phí giao dịch và thuế chỉ hiển thị nếu số tiền > 0
• MB Server trả về theo công thức = (Phí giao dịch theo nhà cung cấp, do hệ thống Billing trả về) + Phí theo dịch vụ của gói dịch vụ khai báo tại BackOffice
 | 9 | Phương thức xác thực | 
Combobox
 | 
Select
 | 
x
 | 
--
 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 10 | Button Tiếp tục | Button | Click | -- | -- | 
Hiển thị MH Xác thực giao dịch → Tham khảo logic xử lý 

##### MH4: Xác thực giao dịch

<Hiển thị MH Xác thực giao dịch + Facepay(nếu có) theo Logic chung>

Tham chiếu tài liệu: và tài liệu 

##### MH5: Kết quả giao dịch
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
2
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
Kết quả giao dịch

 | 
3
 | 
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
Hiển thị Logo Co-opBank

 | 
4
 | 
Icon thành công
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị icon giao dịch thành công

 | 
5
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
Thanh toán thành công

 | 
6
 | 
Số tiền
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị tổng số tiền thanh toán gốc + phí giao dịch và thuế

 | 
7
 | 
Thời gian giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị theo định dạng dd/mm/yyyy hh:mm

 | 
8
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
Mua xổ số Vietlott SMS

 | 
9
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
Hiển thị thông tin mã thanh toán của sdk

 | 
10
 | 
Mã giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị thông tin mã giao dịch (Mã hạch toán do Corebank trả về)

 | 
12
 | 
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
Nhấn Tạo giao dịch mới, hiển thị màn hình đầu tiên khi bắt đầu vào luồng SDK gọi Vietlott

 | 
13
 | 
Nhấn Icon lưu ảnh
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý chung

 | 
14
 | 
Nhấn Nút chia sẻ
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý chung

---

#### 18.10.2. [Vietlott] User Action Flow

> **Page ID:** `515867034` · **Version:** 7
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/515867034

Mục lục
none

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | HongLT | 
 | 
Tạo mới
 | V.1

### 1/ Mô tả UseCase
 | Use Case Name | 
Mua Vietlott

 | Actor | 
KH, Client, MB Server, VNPAY Billing, NCC Vietlott

 | Trigger | 
• Tại Trang chủ nhấn icon Mua xổ số Vietlott
 | 
Pre-Condition
 | 
• KH đã cập nhật app lên phiên bản hỗ trợ chức năng
• KH đăng nhập app thành công
• KH có TKTT hợp lệ và đủ số dư để thực hiện giao dịch
• Gói dịch vụ của KH thuộc gói dịch vụ được sử dụng chức năng Mua Vietlott
 | Post-Condition | 
• KH thanh toán đơn đặt mua xổ số Vietlott thành công
• Hệ thống MB ghi nhận giao dịch mua Vietlott của KH
 | Basic Flow | 
• KH Chọn chức năng Mua xổ số Vietlott
• KH Chọn nhà mạng (Đối với KH chưa đăng ký tài khoản)
• Nhập SĐT (Đối với KH chưa đăng ký tài khoản)
• Chụp ảnh giấy tờ (Đối với KH chưa đăng ký tài khoản)
• Chọn mua Xổ số
• Bấm Xác nhận thanh toán
 | Remark dịch vụ | 

### 2/ Luồng truy cập chức năng
 | 
 | 
Tác nhân
 | 
Mô tả
 | 

 | 1 | Khai báo icon chức năng Vietlott | MB | 
Khai báo chức năng Thanh toán mua xổ số Vietlott

 | 2 | KH login vào ứng dụng | MB | 
Kiểm tra list dịch vụ thuộc gói dịch vụ

• Nếu có: Cho phép KH vào trong MH đầu tiên của MB
• Nếu không: Hiển thị thông báo "Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ."
 | 3 | KH Đăng ký tài khoản Vietlott | MB | 
• KH Chọn chức năng Mua xổ số Vietlott
• KH Chọn nhà mạng (Đối với KH chưa đăng ký tài khoản)
• Nhập SĐT (Đối với KH chưa đăng ký tài khoản)
• Chụp ảnh giấy tờ (Đối với KH chưa đăng ký tài khoản)
• Chọn mua Xổ số
• Bấm Xác nhận thanh toán
 | 4 | Bấm Xác nhận thanh toán trong MH của Vietlott | MB | 
Gửi yêu cầu lấy thông tin tài khoản nguồn tới Bank

 | Bank server | Truy vấn thông tin tài khoản nguồn và trả kết quả cho MB MB qua MB server
 | MB | 
Nhận kết quả:

• Không thành công: Trả kết quả lỗi tương ứng | | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 

• Thành công: Trả kết quả danh sách tài khoản được phép thanh toán hóa đơn tới App MB
 | MB | 
Nhận kết quả:

• Không thành công: Hiển thị MH thông báo lỗi tương ứng
• Thành công: Hiển thị MH Khởi tạo thanh toán như mô tả màn hình.

### 4/ Luồng chức năng chính

MH1: Khởi tạo thanh toán
 | TT | Thao tác | Tác nhân | Mô tả
 | 
1
 | 
Bấm chọn “Tài khoản nguồn”
 | 
MB
 | 
Kiểm tra đã lấy danh sách tài khoản thanh toán thành công chưa?

• Đã lấy thành công trước đó: Hiển thị popup chọn tài khoản nguồn gồm:

• Tiêu đề: Tài khoản nguồn
• Hiển thị. Hiển thị gồm:
• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
• Chưa thành công: Gửi yêu cầu lấy danh sách tài khoản thanh toán đến Bank
 | Bank server | Xử lý và phản hồi kết quả lấy danh sách tài khoản thanh toán cho MB
 | MB | 
1/ Nhận phản hồi kết quả lấy danh sách tài khoản thanh toán

• Không thành công: Trả kết quả thông báo lỗi: | | 
TT
 | 
Trường hợp lỗi
 | 
Thông báo
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 
Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.

• Thành công: Trả kết quả danh sách tài khoản được phép thanh toán tới MB
 | MB | 
Nhận kết quả:

• TimeOut: Hiển thị popup thông báo lỗi " Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại" với button Đóng và Thử lại. Nhấn Thử lại, MB gửi yêu cầu lấy danh sách tài khoản thanh toán. Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.
• Không thành công: 
• Hiển thị popup thông báo lỗi "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!" với button Đóng. Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.
• Thành công: 
• Mặc định hiển thị tài khoản thanh toán mặc định tại màn hình khởi tạo gồm các thông tin: Số tài khoản, số dư + đơn vị tiền tệ VND. 
• Nếu không có tài khoản thanh toán mặc định (đã tất toán, không được phép thực hiện dịch vụ) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do Bank trả về
 | 
Chọn 1 “Tài khoản nguồn”
 | 
MB
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ VND
Lưu ý: Chỉ được phép chọn 1 tài khoản

 | 
2
 | 
Nhấn Tiếp tục
 | 
MB
 | 
Khởi tạo giao dịch với thông tin đơn hàng 

 | 
 | 

 | 
MB
 | 
1/ Truy vấn đơn hàng

• Không thành công/ Timeout trả thông báo lỗi của hệ thống Billing tương ứng cho MB theo 
• Thành công → Chuyển bước 2
2/ Khởi tạo giao dịch ( Service code = 0425) và kiểm tra hạn mức

Tham chiếu tài liệu: URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)và tài liệu II. Xác thực Facepay (nếu có)

• Lưu ý: Phí dịch vụ MB server trả cho MB = Phí do hệ thống Billing trả + Phí của dịch vụ theo cấu hình gói dịch vụ
 | 
 | 

 | 
MB
 | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng mà MB Server trả về
• Thành công: 
• Hiển thị màn hình Xác nhận giao dịch với các thông tin thanh toán và hình thức xác thực MB Server trả về.

##### MH2: Màn hình xác nhận giao dịch
Tham chiếu tài liệu: URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)và tài liệu II. Xác thực Facepay (nếu có) | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Chọn 1 phương thức xác thực và nhấn ""Xác nhận" | MB | 
Chuyển sang màn hình xác thực giao dịch theo phương thức xác thực tương ứng đã chọn:

• Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)
• Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)
• Nếu phương thức xác thực là vân tay → Gửi yêu cầu xác thực giao dịch (Tham khảo logic xử lý tại Xác thực bằng Touch ID/Face ID)

##### MH3: Màn hình xác thực giao dịch
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | Thực hiện xác thực theo PTXT tương ứng

 | MB  | 
1/ Xử lý thông tin validate (nếu có)

2/ Xử lý xác thực giao dịch theo PTXT (Tham khảo:  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2))

3/ Gửi yêu cầu hạch toán sang Bank Server

 | Bank Server | 
Xử lý hạch toán với Core Bank và trả kết quả:

• Không hợp lệ: Trả kết quả cho App Server | | 
 | 
Trường hợp
 | 
Thông báo
 | 
Xử lý (nếu có)

 | 1 | Số dư không đủ | Số dư tài khoản không đủ. Quý khách vui lòng kiểm tra lại | 

 | 2 | Số dư duy trì tối thiểu không đủ | Số dư tối thiểu duy trì tài khoản không đủ. Quý khách vui lòng kiểm tra lại | 

• Hợp lệ: Trả kết quả cho App Server
 | MB | 
Nhận kết quả:

• Không hợp lệ:
• Trả kết quả cho MB MB hiển thị thông báo lỗi tương ứng đã cấu hình tại bảng MB_Template
• Timeout:
• Trả kết quả cho App MB hiển thị thông báo lỗi timeout.
• Hợp lệ:
• Gửi yêu cầu gạch nợ sang Billing
 | MB | 
1/ Nhận kết quả gạch nợ và xử lý:

• Không hợp lệ: 
• Cấu hình hiển thị Popup thông báo lỗi tương ứng
• Gọi API đảo tiền tới Bank server và nhận kết quả:
• Không thành công: Ghi nhận trạng thái phase đảo tiền Thất bại
• Thành công: Ghi nhận trạng thái phase đảo tiền Thành công 
• Timeout: Ghi nhận trạng thái phase đảo tiền khi không nhận được kết quả xử lý là Timeout
• TimeOut:
• Ghi nhận trạng thái giao dịch là Timeout
• Trả thông báo lỗi tương ứng: | | 
TT
 | 
Trường hợp
 | 
Tác nhân
 | 
Nội dung thông báo

 | 1 | TimeOut | Hệ thống MB | Yêu cầu tạm thời bị gián đoạn. Quý khách vui lòng thực hiện lại sau.

•  Hợp lệ:
• Trả kết quả GD thành công
• Cập nhật trạng thái giao dịch phase trừ tiền và gạch nợ là "Thành công"
 | MB | 
Nhận kết quả:

• Không thành công: Hiển thị Popup thông báo lỗi tương ứng
• Timeout: Hiện thị thông báo lỗi tương ứng 
•  Thành công: Hiển thị màn hình kết quả giao dịch (Như mô tả màn hình)

##### MH4: Màn hình Kết quả giao dịch
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
Nhấn “Tạo giao dịch mới”
 | 
MB
 | 
Hiển thị màn hình đầu tiên trong MB

 | 2 | 
Nhấn “Home”
 | 
MB
 | 
Hiển thị màn hình Home với thông tin số dư được cập nhật lại sau khi thanh toán thành công

 | 3 | Chia sẻ | MB | Tham khảo logic xử lý chung
 | 4 | Lưu ảnh | MB | Tham khảo logic xử lý chung

Thông tin cấu hình trên BE: Tham khảo tại

---

### 18.11. API Billing

> **Page ID:** `517409128` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/517409128

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

#### 18.11.1. API Request Billing (Theo cấu trúc Json mới)

> **Page ID:** `517409051` · **Version:** 6
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/517409051

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | HongLT | 
 | 
Tạo mới
 | V.1
 | 
 
 | M | ThaoCY | 
 | 
Mở rộng tài liệu cho các dịch vụ TTHĐ, SDK
 | V.2

## Input
 | 
Tên trường
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả

 | 
##### Header

 | 
trans_id
 | 
 String
 | 
M
 | 
Là trường định danh request trên toàn hệ thống.

Tương ứng giá trị trans_id trong body request

Nên sử dụng UUID hoặc GUID để đảm bảo tính duy nhất của request.

 | 
##### Body Request

 | 
Tên trường
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả

 | 
data
 | 
 Object
 | 
M
 | 
Thông tin giao dịch.
 | 
Tham số
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả
 | 
Ghi chú

 | 
account_no
 | 
 String
 | 
O
 | 
Số tài khoản thanh toán của khách hàng
 | 

 | 
bin_code
 | 
 String
 | 
M
 | 
Truyền 970446
 | 

 | 
channel
 | 
 String
 | 
M
 | 
Truyền 6015
 | 
Các kênh hiện có:

6012 TELLER
6013 SMS
6014 INTERNET
6011 ATM
6015 MB
6019 AUTOBILL

 | 
recipient_code
 | 
 String
 | 
M
 | 
Số điện thoại của KH 
 | 
(tùy theo từng dịch vụ mã này có thể là mã khách hàng, số điện thoại, số danh bộ hoặc mã vé,...)

 | 
local_datetime
 | 
 String
 | 
M
 | 
Thời gian phát sinh giao dịch tại nơi yêu cầu, theo định dạng: yyyyMMddHHmmss.
 | 

 | 
partner_code
 | 
 String
 | 
M
 | 
Truyền bankcode do billing quy định
 | 
Tương ứng với trường bankCode trong API cũ

 | 
provider_code
 | 
 String
 | 
M
 | 
Truyền tương ứng theo từng nhà mạng

• VIETTEL  → Truyền: 00000037
• VINAPHONE → Truyền: 00000060
• MOBIFONE → Truyền: 00000061 | 

 | 
recipient_code 
 | 
 String
 | 
M
 | 
Mã truy vấn (tùy theo từng dịch vụ mã này có thể là mã khách hàng, số điện thoại, số danh sách bộ hoặc mã vé,...)
 | 

 | 
service_code
 | 
 String
 | 
M
 | 
Truyền mã dịch vụ quy định tại: https://docs.google.com/spreadsheets/d/1ZHE1VhrY725aRTEoOcaQ12fqvm1uR53okwwg_PTeTwc/edit?gid=2750558#gid=2750558
 | 

 | 
sender_code
 | 
 String
 | 
O
 | 
Mã yêu cầu (số điện thoại thanh toán)
 | 
Không bắt buộc

 | 
sub_partner
 | 
 String
 | 
O
 | 
Mã điểm thu thuộc đối tác
 | 
Không bắt buộc

 | 
trace
 | 
 String
 | 
M
 | 
Số thứ tự giao dịch tại đối tác đi qua hệ thống trong một khoảng thời gian. Giá trị từ 1-999999 (thêm 0 đằng trước cho đủ 6 ký tự)
 | 

 | 
trans_id
 | 
String
 | 
M
 | 
Mã giao dịch tại đối tác
 | 
Là mã giao dịch đã mô tả tại Header

(Nên sử dụng UUID hoặc GUID để đảm bảo tính duy nhất của request.)

 | 
sign
 | 
 String
 | 
M
 | 
Chữ ký điện tử được ký theo dữ liệu json object tham số data theo thứ tự từ trên xuống dưới

 | 
additional_info
 | 
 Object
 | 
O
 | 
Thông tin dữ liệu bổ sung cho dịch vụ cần bổ sung
 | 
Tham số
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Giá trị

 | 
amount
 | 
Decimal
 | 
M
 | 
Số tiền thanh toán 

 | 
recipient_type
 | 
 String
 | 
O
 | 
Loại truy vấn (số điện thoại/ mã thanh toán/ mã sinh viên/ biển số xe...)

 | 
request_id
 | 
String
 | 
M
 | 
Mã đơn hàng thanh toán 

 | 
request_code
 | 
String
 | 
O
 | 
Mã định danh dịch vụ, truyền vào tương ứng theo nhà mạng của KH:

• VIETTEL
• VINAPHONE
• MOBIFONE
 | 
request_type
 | 
String
 | 
O
 | 
Không bắt buộc

 | 
account_type
 | 
String
 | 
O
 | 
Không bắt buộc

### Output
 | 
Tên trường
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả
 | 
Ghi chú

 | 
data
 | 
 Object
 | 
M
 | 
Thông tin giao dịch.
 | 
Tham số
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả
 | 
Ghi chú

 | 
account_no
 | 
String
 | 
O
 | 
Số tài khoản của khách hàng
 | 

 | 
bin_code
 | 
String
 | 
M
 | 

 | 

 | 
channel
 | 
String
 | 
M
 | 
Kênh giao dịch
 | 

 | 
recipient_code
 | 
 String
 | 
M
 | 
Mã truy vấn (tùy theo từng dịch vụ mã này có thể là mã khách hàng, số điện thoại, số danh bộ hoặc mã vé,...)
 | 

 | 
local_datetime
 | 
 String
 | 
M
 | 
Thời gian phát sinh giao dịch tại nơi yêu cầu, theo định dạng: yyyyMMddHHmmss.
 | 

 | 
provider_code
 | 
 String
 | 
M
 | 
Mã nhà cung cấp (Vnpay cung cấp)
 | 

 | 
service_code
 | 
 String
 | 
M
 | 
Mã dịch vụ (Vnpay cung cấp)
 | 

 | 
trace
 | 
 String
 | 
M
 | 
Số thứ tự giao dịch tại đối tác đi qua hệ thống trong một khoảng thời gian. Giá trị từ 1-999999 (thêm 0 đằng trước cho đủ 6 ký tự)
 | 

 | 
trans_id
 | 
String
 | 
M
 | 
Mã giao dịch tại đối tác
 | 

 | 
vnpay_datetime
 | 
String
 | 
M
 | 
Thời gian thực hiện giao dịch yyyyMMddHHmmss
 | 

 | 

 | 
sign
 | 
 String
 | 
M
 | 
Chữ ký điện tử được ký theo dữ liệu json object tham số data theo thứ tự từ trên xuống dưới
 | 

 | 
resp_code
 | 
String
 | 
M
 | 
Mã lỗi của hệ thống Billing

 | 

 | 
resp_desc
 | 
String
 | 
O
 | 
Mô tả chi tiết lỗi
 | 

 | 
payment_type
 | 
Number
 | 
M
 | 
Kiểu thanh toán:

0 - Toàn phần (mặc định)

1 - Từng phần theo hóa đơn 

2 - Số tiền được phép thanh toán
 | 

 | 
amount
 | 
 Decimal
 | 
M
 | 
Số tiền thanh toán với nhà cung cấp
 | 

 | 
fee_amount
 | 
 Decimal
 | 
M
 | 
Số tiền phí thu khách hàng do hệ thống Billing quy định
 | 

 | 
total_amount
 | 
 Decimal
 | 
M
 | 
Tổng số tiền đã bao gồm phí thu khách hàng 
 | 

 | 
customer_info
 | 
 Object
 | 
O
 | 
Thông tin chi tiết của khách hàng
 | 
Tham số
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả
 | 
Ghi chú

 | 
customer_code
 | 
String
 | 
O
 | 
Mã nhà cung cấp trả về (tùy theo từng dịch vụ mã này có thể là mã thanh toán,...)
 | 
Billing sẽ trả cho MB server nếu NCC có trả cho Billing

 | 
customer_name
 | 
 String
 | 
O
 | 
Họ tên
 | 
Billing sẽ trả cho MB server nếu NCC có trả cho Billing

 | 
phone
 | 
String
 | 
O
 | 
Số điện thoại
 | 
Billing sẽ trả cho MB server nếu NCC có trả cho Billing

 | 
email
 | 
String
 | 
O
 | 
Email
 | 
Billing sẽ trả cho MB server nếu NCC có trả cho Billing

 | 
address
 | 
String
 | 
O
 | 
Địa chỉ
 | 
Billing sẽ trả cho MB server nếu NCC có trả cho Billing

 | 

 | 
bill_info
 | 
Array Object
 | 
O
 | 
Thông tin chi tiết hóa đơn của khách hàng
 | 
Tham số
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả
 | 
Ghi chú

 | 
bill_code 
 | 
String 
 | 
O 
 | 
Mã (Số hóa đơn/gói cước, kích hoạt,...) 
 | 
Billing sẽ trả cho MB server nếu NCC có trả cho Billing

 | 
bill_type
 | 
String
 | 
O
 | 
Loại (Loại hóa đơn điện/loại dịch vụ trả trước/trả sau/loại tài khoản,...)
 | 
Billing sẽ trả cho MB server nếu NCC có trả cho Billing

 | 
bill_name
 | 
String 
 | 
O 
 | 
Tên (Tên kỳ cước/gói cước,..) 
 | 
Billing sẽ trả cho MB server nếu NCC có trả cho Billing

 | 
bill_status
 | 
String 
 | 
O
 | 
Trạng thái (Trạng thái tài khoản,...)
 | 
Billing sẽ trả cho MB server nếu NCC có trả cho Billing

 | 
amount
 | 
Decimal
 | 
O 
 | 
Số tiền (Số tiền cước/gói cước,...)
 | 
Billing sẽ trả cho MB server nếu NCC có trả cho Billing

 | 
bill_desc
 | 
String
 | 
O
 | 
Mô tả
 | 
 

 | 
Sample:

[ { "bill_code": "E10", "bill_type": "",

 "bill_name": "E10", → Kỳ hóa đơn

 "amount": 10000, → Số tiền thanh toán

 "bill_desc": "Goi E10 co 2GB su dung trong 1 ngay" },

 { "bill_code": "E11", "bill_type": "",

 "bill_name": "E11", → Kỳ hóa đơn

 "amount": 15000, → Số tiền thanh toán

 "bill_desc": "Goi E11 co 5GB su dung trong 1 ngay" } ] }

 | 
detail_data
 | 
Array Object
 | 
M
 | 
Thông tin chi tiết dữ liệu chi tiết
 | 
Tham số
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả

 | 
field_key
 | 
String
 | 
O
 | 
Mã tham số động theo từng dịch vụ

 | 
filed_name
 | 
String
 | 
O
 | 
Tên tham số động theo từng dịch vụ

 | 
field_type
 | 
String
 | 
O
 | 
Loại dữ liệu sẽ trả ra ở field_value

 | 
field_value
 | 
String
 | 
O
 | 
Giá trị tham số động theo từng dịch vụ

 | 
field_desc
 | 
String
 | 
O
 | 
Diễn giải tham số động theo từng dịch vụ

Tham khảo tại https://docs.google.com/spreadsheets/d/1ZHE1VhrY725aRTEoOcaQ12fqvm1uR53okwwg_PTeTwc/edit#gid=2750558
 | 
Các thông tin detail_data này áp dụng cho các dịch vụ đặc thù như SDK:

• Mua vé xe
• Mua vé xem phim
• Đặt phòng khách sạn
• Thanh toán học phí 
• Thanh toán cước truyền hình 
• Thanh toán phí bảo hiểm 
• VNSHOP
• Thanh toán vay tín dụng 
• Taxi
• Golf
• Mua sổ xố
• Thanh toán vé máy bay
• Giao hàng 
• Thanh toán phí chung cư 
• Tổng hợp (VNPT media)

---

#### 18.11.2. API Payment Billing (Cấu trúc Json)

> **Page ID:** `517409153` · **Version:** 6
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/517409153

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | HongLT | 
 | 
Tạo mới
 | V.1
 | 
 
 | M | ThaoCY | 
 | 
Mở rộng phạm vi tài liệu cho các dịch vụ TTHĐ, SDK
 | V.2

## Input
 | 
Tên trường
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả

 | 
##### Header

 | 
trans_id
 | 
 String
 | 
M
 | 
Là trường định danh request trên toàn hệ thống.

Tương ứng giá trị trans_id trong body request

Nên sử dụng UUID hoặc GUID để đảm bảo tính duy nhất của request.

 | 
##### Body Request

 | 
Tên trường
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả

 | 
data
 | 
 Object
 | 
M
 | 
Thông tin giao dịch.
 | 
Tham số
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả
 | 
Ghi chú

 | 
account_no
 | 
 String
 | 
M
 | 
Số tài khoản thanh toán của khách hàng
 | 
Tuy kiểu dữ liệu của Billing là Option, nhưng do file đối soát giữa 2 bên có thông tin về TKTT nên cần MB Server truyền cho Billing cả TKTT thực hiện giao dịch của KH

 | 
amount
 | 
 Decimal
 | 
M
 | 
Số tiền hóa đơn cần thanh toán với nhà cung cấp
 | 
Là số tiền chưa bao gồm phí billing, mà Billing đã trả ở hàm Request tại trường "amount"

 | 
bin_code
 | 
 String
 | 
M
 | 
Truyền 970446
 | 
Dùng chung với KHCN

 | 
channel
 | 
 String
 | 
M
 | 
Truyền 6015
 | 
Các kênh hiện có:

6012 TELLER
6013 SMS
6014 INTERNET
6011 ATM
6015 MB
6019 AUTOBILL

 | 
recipient_code
 | 
 String
 | 
M
 | 
Mã thanh toán
 | 
(tùy theo từng dịch vụ mã này có thể là mã khách hàng, số điện thoại, số danh bộ hoặc mã vé,...)

 | 
debit_amount
 | 
 Decimal
 | 
M
 | 
Số tiền thanh toán bao đã bao gồm phí billing cần thu của KH
 | 
Là số tiền mà HT Billing trả tại trường total_amount (trường total_amount chính bằng = amount + fee_amount)

 | 
local_datetime
 | 
 String
 | 
M
 | 
Thời gian phát sinh giao dịch tại nơi yêu cầu, theo định dạng: yyyyMMddHHmmss.
 | 

 | 
partner_code
 | 
 String
 | 
M
 | 
Truyền 970502
 | 
Dùng chung với KHCN

 | 
provider_code
 | 
 String
 | 
M
 | 
Mã nhà cung cấp (Vnpay cung cấp)
 | 
Đã mô tả ở hàm truy vấn

 | 
service_code
 | 
 String
 | 
M
 | 
Mã dịch vụ (Vnpay cung cấp)
 | 
Đã mô tả ở hàm truy vấn

 | 
sender_code
 | 
 String
 | 
O
 | 
Mã yêu cầu (số điện thoại thanh toán)
 | 
Không bắt buộc

 | 
sub_partner
 | 
 String
 | 
O
 | 
Mã điểm thu thuộc đối tác
 | 
Không bắt buộc

 | 
trace
 | 
 String
 | 
M
 | 
Số thứ tự giao dịch tại đối tác đi qua hệ thống trong một khoảng thời gian. Giá trị từ 1-999999 (thêm 0 đằng trước cho đủ 6 ký tự)
 | 

 | 
trans_id
 | 
String
 | 
M
 | 
Mã giao dịch tại đối tác
 | 
Là mã giao dịch đã mô tả tại Header

(Nên sử dụng UUID hoặc GUID để đảm bảo tính duy nhất của request.)

 | 
sign
 | 
 String
 | 
M
 | 
Chữ ký điện tử được ký theo dữ liệu json object tham số data theo thứ tự từ trên xuống dưới

 | 
bill_info
 | 
Array Object
 | 
O
 | 
Thông tin chi tiết hóa đơn của khách hàng

Tham chiếu bảng mô tả “bill_info request” bên dưới
 | 
Tham số
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả
 | 
Ghi chú

 | 
bill_code 
 | 
String 
 | 
O 
 | 
Mã (Số hóa đơn/gói cước, kích hoạt,...) 
 | 
Chỉ truyền vào billing có trả thông tin này tại hàm Request truy vấn

 | 
bill_name
 | 
String 
 | 
O 
 | 
Tên (Tên kỳ cước/gói cước,..) 

 | 
amount
 | 
Decimal
 | 
O 
 | 
Số tiền (Số tiền cước/gói cước,...)

 | 
additional_info
 | 
 Object
 | 
O
 | 
Thông tin dữ liệu bổ sung cho dịch vụ cần bổ sung
 | 
Tham số
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả
 | 
Ghi chú

 | 
promotion_code
 | 
String
 | 
O
 | 
Mã khuyến mại
 | 
Billing tạo ra trường này để ghi nhận mã giảm giá của Bank cho dịch vụ Billing (nếu có)

Nhưng do CoopBank không có giảm giá cho các dịch vụ Billing nên không phải truyền trường này

 | 
promotion_amount
 | 
Decimal
 | 
M
 | 
Số tiền khuyến mại (không có khuyến mại mặc định là 0)

 | 
fee_amout_partner
 | 
Decimal
 | 
O
 | 
Số tiền thu phí tại đối tác
 | 

Không bắt buộc

 | 
real_amout
 | 
Decimal
 | 
O
 | 
Số tiền đối tác thực trừ KH

 | 
recipient_type
 | 
 String
 | 
O
 | 
Loại truy vấn (Số điện thoại/ Mã thanh toán/ Mã sinh viên/ Biển số xe.....)

 | 
request_id
 | 
String
 | 
O
 | 
Mã giao dịch cần thanh toán tại hoá đơn (Yêu cầu đối với một số nhà cung cấp để thực hiện truy vấn dữ liệu chi tiết hóa đơn,...)

 | 
request_code
 | 
String
 | 
O
 | 
Thông tin mã bổ sung để thực hiện truy vấn (đối với một số nhà cung cấp có yêu cầu ngoài mã thanh toán cần có số điện thoại/ email/…, để lấy thông tin chi tiết hóa đơn)

 | 
request_type
 | 
String
 | 
O
 | 
Loại mã yêu cầu gửi bổ sung (loại mã của request_code như số điện thoại/ email/…) 

 | 
account_type
 | 
String
 | 
O
 | 
Loại hình tài khoản thanh toán của khách hàng:

• 01: Tài khoản/ thẻ nội địa
• 02: Tài khoản ví
• 03: Tài khoản tín dụng nội địa
• 04: Tài khoản tín dụng quốc tế

### Output
 | 
Tên trường
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả
 | 
Ghi chú

 | 
data
 | 
 Object
 | 
M
 | 
Thông tin giao dịch.
 | 
Tham số
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả

 | 
account_no
 | 
String
 | 
O
 | 
Số tài khoản thanh toán của khách hàng

 | 
amount
 | 
 Decimal
 | 
M
 | 
Số tiền hóa đơn cần thanh toán

 | 
bin_code
 | 
String
 | 
M
 | 
 

 | 
channel
 | 
String
 | 
M
 | 
Kênh giao dịch

 | 
recipient_code
 | 
 String
 | 
M
 | 
Mã truy vấn (tùy theo từng dịch vụ mã này có thể là mã khách hàng, số điện thoại, số danh bộ hoặc mã vé,...)

 | 
debit_amount
 | 
 Decimal
 | 
O
 | 
Số tiền thực trừ của khách hàng bao gồm phí

 | 
local_datetime
 | 
 String
 | 
M
 | 
Thời gian phát sinh giao dịch tại nơi yêu cầu, theo định dạng: yyyyMMddHHmmss.

 | 
provider_code
 | 
 String
 | 
M
 | 
Mã nhà cung cấp (Vnpay cung cấp)

 | 
service_code
 | 
 String
 | 
M
 | 
Mã dịch vụ (Vnpay cung cấp)

 | 
sub_partner
 | 
String
 | 
O
 | 
Mã điểm thu thuộc đối tác

 | 
trace
 | 
 String
 | 
M
 | 
Số thứ tự giao dịch tại đối tác đi qua hệ thống trong một khoảng thời gian. Không được trùng lặp thông tin trong 1 ngày giá trị từ 1-999999 (thêm 0 đằng trước cho đủ 6 ký tự)

Chú ý: Giá trị của trường này sẽ sử dụng để đối chiếu giữa đối tác, Vnpay và Nhà cung cấp

 | 
trans_id
 | 
String
 | 
M
 | 
Mã giao dịch tại đối tác

 | 
vnpay_datetime
 | 
String
 | 
M
 | 
Thời gian thực hiện giao dịch yyyyMMddHHmmss

 | 

 | 
sign
 | 
 String
 | 
M
 | 
Chữ ký điện tử được ký theo dữ liệu json object tham số data theo thứ tự từ trên xuống dưới
 | 

 | 
resp_code
 | 
String
 | 
M
 | 
Mã lỗi của hệ thống Billing

 | 

 | 
resp_desc
 | 
String
 | 
O
 | 
Mô tả chi tiết lỗi
 | 

 | 
bill_info
 | 
Array Object
 | 
O
 | 
Thông tin chi tiết hóa đơn của khách hàng
 | 
Tham số
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả

 | 
bill_code 
 | 
String 
 | 
O 
 | 
Mã (Số hóa đơn/gói cước, kích hoạt,...) 

 | 
bill_type
 | 
String
 | 
O
 | 
Loại (Loại hóa đơn điện/loại dịch vụ trả trước/trả sau,...)

 | 
bill_name
 | 
String 
 | 
O 
 | 
Tên (Tên kỳ cước/gói cước,..) 

 | 
amount
 | 
Decimal
 | 
O 
 | 
Số tiền (Số tiền cước/gói cước,...)

 | 
bill_desc
 | 
String
 | 
O
 | 
Mô tả

 | 

 | 
detail_data
 | 
Array Object
 | 
M
 | | 
Tham số
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Mô tả

 | 
field_key
 | 
String
 | 
M
 | 
Mã tham số động theo từng dịch
vụ

 | 
field_name 
 | 
String
 | 
O
 | 
Tên mô tả tham số động theo
từng dịch vụ

 | 
field_type
 | 
String
 | 
O
 | 
Loại dữ liệu sẽ trả ra ở
field_value

 | 
field_value 
 | 
String
 | 
O
 | 
Giá trị tham số động theo từng
dịch vụ

 | 
field_desc 
 | 
String
 | 
O
 | 
Diễn giải tham số động theo
từng dịch vụ

 | 

 | 
payment_type
 | 
Number
 | 
M
 | 
Kiểu thanh toán

0 - Toàn phần (mặc định)

1 - Từng phần theo hóa đơn 

2 - Số tiền được phép thanh toán
 |

---


