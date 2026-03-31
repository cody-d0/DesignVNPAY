# 📋 Tra soát & Event

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `ops/`
> **Trích xuất:** 2026-03-28

---

## 33. API BANK

> **Page ID:** `353566775` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/353566775

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*1 trang con:*

### 33.1. SMS_BankingSecnumber - Đăng ký chia sẻ thông tin biến động số dư

> **Page ID:** `353566781` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/353566781

#### Input
 | 
Data element/ Field Name
 | Description | 

 | systemID | 
Ứng dụng gửi tin = VNPAY
 | R
 | requestID | ID tin điện | R
 | 
accountNo
 | Số tài khoản | R - Cho phép truyền list
 | 
primary_number
 | 
Số điện thoại
 | R
 | 
record_stat
 | 
Trạng thái
 | R, O: Mở - C: Đóng

Output
 | 
Data element/ Field Name
 | Description | 

 | requestId | ID tin điện | R
 | 
resDesc
 | 
Mã tả lỗi nếu có
 | C - Chỉ bắt buộc khi tin điện xử lý thành công (resCode="000")
 | 
resCode
 | 
Mã trả về
 | C - Chỉ bắt buộc khi tin điện xử lý thành công (resCode="000")

---


## 37. Tra soát khiếu nại

> **Page ID:** `845119854` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/845119854

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*4 trang con:*

### 37.1. SOW - Tra soát khiếu nại

> **Page ID:** `845119866` · **Version:** 24
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/845119866

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThaoCY | 
 | 
Tạo mới tài liệu
 | 
V1.0.0

### 1/ Ý nghĩa chức năng

• Chức năng tra soát trực tuyến cho phép khách hàng chủ động gửi các yêu cầu tra soát giao dịch phát sinh qua Mobile banking hoặc các trường hợp khác (nhập thông tin thủ công), đồng thời theo dõi tình trạng xử lý ngay trên ứng dụng 
• Về phía ngân hàng, Backoffice có công cụ tiếp nhận, cậ nhật kết quả và phản hồi cho khách hàng
• Mục tiêu:
• Nâng cao trải nghiệm khách hàng, giảm thời gian và thủ tục ra quầy 
• Chuẩn hóa quy trình quản lý khiếu nại/tra soát 
• Giảm rủ ro thất thoát thông tin tra soát thủ công, tăng tính minh bạch
### 2/ Tóm tắt usecase
 | Use Case Name | Tra soát khiếu nại
 | Use Case ID | --
 | Use Case Description | 
Khách hàng sử dụng Mobile Banking để gửi yêu cầu tra soát giao dịch (qua MB hoặc nhập tay). Hệ thống tiếp nhận, xác thực, lưu yêu cầu và hiển thị trong danh sách để BackOffice xử lý.

• Tra soát qua Mobile Banking: Dành cho các giao dịch phát sinh trực tiếp trên kênh Mobile Banking. Khách hàng chọn giao dịch từ danh sách để gửi yêu cầu tra soát.
• Tra soát khác: Dành cho cả những giao dịch không phát sinh trên mobile banking. Khách hàng nhập thủ công thông tin giao dịch để gửi yêu cầu tra soát.
 | Actor | 
KH, MB App, MB server,Backoffice

 | Priority | High
 | 
Trigger
 | 
Khách hàng chọn chức năng “Tra soát trực tuyến” và bấm gửi yêu cầu.

 | 
Pre-Condition
 | 
• Khách hàng đã đăng nhập Mobile Banking thành công.
• Chưa vượt quá số lần tra soát cho phép
 | 
Post-Condition
 | 
• Yêu cầu được ghi nhận vào hệ thống với mã tra soát riêng.
• Khách hàng nhận thông báo xác nhận đã tiếp nhận yêu cầu.
• Yêu cầu hiển thị trong danh sách để BackOffice xử lý.
 | 
Bussiness Rule
 | 
• Lý do tra soát được quản lý tại hệ thống BackOffice. Mỗi lý do tra soát được cấu hình:
• Loại giao dịch được tra soát 
• Số lần tra soát tối đa
• Thời gian tra soát tối đa (ngày)
• Phí tra soát
• Không cho phép tạo tra soát mới cùng lý do khi giao dịch có yêu cầu tra soát đang ở trạng thái "Đã tiếp nhận"
• Không cho phép khách hàng hủy yêu cầu tra soát ở bất kỳ trạng thái nào
• Được phép cứu danh sách giao dịch tra soát trong thời gian tối đa 12 tháng (gần nhất)
• MB server sinh mã định danh duy nhất cho mỗi yêu cầu tra soát
 | 
Tài liệu liên quan
 | 
BRD: 250

### 3/ Luồng màn hình

<tham chiếu >

### 4/ Phạm vi chức năng

#### 4.1/ Phạm vi FrontEnd
 | 
 | Chức năng | Loại | Tác nhân | Mô tả cơ bản | Assign
 | 1 | 
Tạo yêu cầu tra soát
 | 
RedThêm mới
 | 
MB Client

MB Server
 | 
Cho phép KH tạo yêu cầu tra soát tên mobile app

Yêu cầu được ghi nhận và lưu trên hệ thống Backoffice để GDV xử lý
 | 
ThaoCY

 | 2 | 
Danh sách yêu cầu tra soát
 | 
RedThêm mới
 | 
MB Client

MB Server
 | 
Danh sách yêu cầu tra soát của khách hàng, bao gồm các thông tin như: Ngày giao dịch, mã giao dịch, Số tiền, ngày tra soát, trạng thái tra soát,....
 | 
ThaoCY

 | 3 | 
Báo cáo giao dịch → Bank báo tạm để sau
 | 
GreenCập nhật
 | MB Client | 
Cập nhật logic trường Loại giao dịch:

Hiện tại: Fix Client → client tự map Loại giao dịch với serviceCode truyền xuống MB server lấy lịch sử giao dịch 

Cập nhật: Gọi MB server lấy danh sách Loại giao dịch → MB server map seviceCode để trả về lịch sử giao dịch 

→ Client check tham số version:

• Version cũ: Theo logic cũ
• Version mới: Theo logic mới
Mục đích: Đồng nhất Loại giao dịch tại màn Báo cáo giao dịch và màn Tra soát khiếu nại
 | 

 | 4 | 
Điều hướng từ tin OTT về màn hình chi tiết yêu cầu tra soát
 | 
RedThêm mới
 | 
MB Client
 | 
Lưu ý: Cần có mã giao dịch tra soát để điều hướng đến đúng màn hình
 | 
ThanhLV

#### 4.2/ Phạm vi BackEnd
 | 
 | Chức năng | Loại | Tác nhân | Mô tả cơ bản | Assign
 | 1 | 
Quản lý tra soát khiếu nại
 | 
RedThêm mới
 | BO | 
Cho phép GDV tìm kiếm và xử lý (cập nhật trạng thái, nội dung tra soát), thông tin hiển thị tùy vào loại tra soát là Tra soát giao dịch qua Mobile Banking/ Tra soát khác

Khi GDV cập nhật trạng thái xử lý trên BO → Push tin OTT về user của KH
 | 
ThanhLV

 | 2 | 
Quản lý lý do tra soát khiếu nại
 | 
RedThêm mới
 | BO | 
Cho phép quản lý Lý do tra soát (thêm mới/ sửa/ xóa). Từng lý do sẽ được cấu hình:

• Loại giao dịch được tra soát 
• Số lần tra soát tối đa
• Thời gian tra soát tối đa (ngày)
• Thuế VAT, Phí tra soát | 
ThanhLV

 | 3 | 
Lịch sử hành động
 | 
GreenCập nhật
 | BO | 
Bổ sung lưu log GDV xử lý Tra soát
 | 
ThanhLV

 | 4 | 
Loại dịch vụ
 | 
GreenCập nhật
 | BO | 
Hiện trạng: Hiện đang ẩn module Loại dịch vụ trên BO, không cho phép người dùng cấu hình (đã có URD)

Cập nhật:

• Hiển thị lại module Loại dịch vụ
• Bổ sung thêm trường STT trả về
• Bổ sung thêm Cờ trả về cho MB Client (checkbox - mặc định tick chọn)
• Bổ sung chức năng Thêm mới Loại dịch vụ
Link tài liệu: 
 | 
ThaoCY

---

### 37.2. Flow&Action screen - Tra soát khiếu nại

> **Page ID:** `849478298` · **Version:** 69
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/849478298

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
Màn hình danh sách giao dịch qua mobile banking: Hiển thị thêm giao dịch gạch nợ timeout
 | 
v.1.0.1

 | 
 
 | M | ThaoCY | v.1.0.1 | 
1/ Chỉnh sửa luồng màn hình: Tại các màn hình cho phép xem chi tiết giao dịch qua mobile banking

Khi người dùng click hyperlink "Chi tiết giao dịch" → Điều hướng sang màn chi tiết giao dịch của chức năng Báo cáo giao dịch. Ấn back → Quay lại màn hình trước đó, giữ nguyên thông tin đã nhập

2/ Thông tin chi tiết giao dịch qua mobile banking: 3 trường thông tin hiển thị trong Block Thông tin giao dịch: Mặc định hiển thị 3 trường:

• Mã giao dịch transRefNo
• Nội dung giao dịch (transRemark)
• (-) Số tiền giao dịch = Số tiền giao dịch gốc (amount) | 
v.1.0.2

 | 
 
 | M | ThaoCY | v.1.0.2 | 
Khởi tạo tra soát khác: Trường Số TK/Số thẻ cho phép nhập cả số và chữ
 | 
v.1.0.3

Mục lục

### 1/ Luồng màn hình 

### 2/ Danh sách màn hình

#### 2.1/ Tạo yêu cầu tra soát giao dịch qua Mobile Banking

##### MH0: Home

(bổ sung thêm chức năng Tra soát khiếu nại tại nhóm Tiện ích)

##### MH1: Chọn hình thức tra soát

##### MH2: Tìm kiếm giao dịch qua Mobile Banking

##### MH3: Danh sách giao dịch qua Mobile Banking

##### MH4: Tạo yêu cầu tra soát giao dịch qua Mobile banking

MH5: Popup Thông tin giao dịch qua Mobile banking Chi tiết giao dịch

##### MH6.1: Xác thực giao dịch (SMS OTP)

##### MH6.2: Xác thực giao dịch (Soft OTP)

##### MH7: Kết quả giao dịch

#### 2.2. Tạo yêu cầu tra soát khác

##### MH8: Tạo yêu cầu tra soát khác

##### MH9: Xác nhận yêu cầu

##### MH10: Popup Thông tin giao dịch khác

#### 2.3/ Tra cứu yêu cầu tra soát

##### MH11: Tìm kiếm yêu cầu tra soát

##### MH12: Danh sách yêu cầu tra soát

##### MH13.1: Chi tiết yêu cầu tra soát (TH: Chưa xử lý)

##### MH13.2: Chi tiết yêu cầu tra soát (TH: Đã xử lý)

### 3/ Mô tả màn hình

##### MH1: Chọn hình thức tra soát
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | - | - | Tra soát khiếu nại
 | 2 | Icon Back | Icon | Click | - | - | Click để quay lại màn hình trước đó
 | 3 | Home | Icon | Click | - | - | Click để quay về màn hình Trang chủ
 | 4 | Tab "Tạo yêu cầu" | Tab | Click | - | - | 
Mặc định chọn 

 | 5 | Tab "Tra cứu yêu cầu" | Tab | Click | - | - | Click để tra cứu  danh sách yêu cầu tra soát
 | 6 | Ghi chú | Label | ReadOnly | - | - | Chọn hình thức tra soát
 | 7 | Hình thức tra soát | Radio button | Select | Có | - | 
Gồm 2 giá trị:

• Tra soát giao dịch qua Mobile banking
• Tra soát khác
Mặc định không chọn

##### MH2: Tìm kiếm giao dịch qua Mobile Banking
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | - | - | Tra soát khiếu nại
 | 2 | Icon Back | Icon | Click | - | - | Click để quay lại màn hình trước đó
 | 3 | Home | Icon | Click | - | - | Click để quay về màn hình Trang chủ
 | 4 | Loại giao dịch | Combobox | Select | - | - | 
Giá trị hiển thị là danh sách dịch vụ được cấu hình trên BE  + giá trị "Tất cả" 

Mặc định: Tất cả

Cho phép chọn 1 giá trị 

 | 5 | Tài khoản tra soát | Combobx | Select | Yes | - | 
Giá trị hiển thị là danh sách tài khoản thanh toán của KH do server trả về

Mặc định hiển thị TKTT mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.

Cho phép chọn 1 giá trị 

Click:

• Nếu không có tài khoản thanh toán → Thông báo: "Quý khách không có tài khoản thanh toán. Vui lòng kiểm tra lại"
• Nếu có tài khoản thanh toán → Click vào mở ra màn hình popup chọn tài khoản:
• Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.
• nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định
 | 6 | Từ ngày | 
Calender
 | 
Date
 | 
--
 | 
--
 | 
Định dạng: dd/mm/yyyy

Mặc định Ngày T-7

Cho phép chọn, nhập lại giá trị (Hiển thị lịch tiếng Việt khi nhấn icon lịch)

Không cho phép chọn những ngày tương lai

Từ ngày nhỏ hơn hoặc bằng đến ngày và từ ngày ≤ ngày hiện tại.

Khoảng thời gian tìm kiếm giữa Từ ngày ... Đến ngày không quá 3 tháng tính theo lịch

Thời gian tối đa cho phép tìm kiếm trong vòng 100 ngày

 | 7 | Đến ngày | 
Calender
 | 
Date
 | 
--
 | 
--
 | 
Định dạng: dd/mm/yyyy

Mặc định Ngày T (Today)

Cho phép chọn, nhập lại giá trị (Hiển thị lịch tiếng Việt khi nhấn icon lịch)

Không cho phép chọn những ngày tương lai

Đến ngày lớn hơn hoặc bằng từ ngày và đến ngày ≤ ngày hiện tại.

Khoảng thời gian tìm kiếm giữa Từ ngày ... Đến ngày không quá 3 tháng tính theo lịch

Thời gian tối đa cho phép tìm kiếm trong vòng 100 ngày

 | 8 | Tìm kiếm | Button | Click | - | - | 
Luôn enable

<tham chiếu logic xử lý>

##### MH3: Danh sách giao dịch qua Mobile Banking
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | - | - | Tra soát khiếu nại
 | 2 | Icon Back | Icon | Click | - | - | Click để quay lại màn hình trước đó
 | 3 | Home | Icon | Click | - | - | Click để quay về màn hình Trang chủ
 | 4 | 
Ô textsearch
 | 
Textbox
 | 
Text
 | 
--
 | 
200
 | 
• 
Mặc định trống

• 
Cho phép tìm kiếm gần đúng theo: Mã giao dịch, Nội dung giao dịch, Số tiền

• Nếu kết quả tìm kiếm không có dữ liệu: hiển thị thông báo "Không tìm thấy kết quả."
• Nếu kết quả tìm kiếm có dữ liệu hiển thị theo tab dữ liệu tương ứng.
• Chỉ hiển thị khi có trên n bản ghi (xem tại quy tắc chung)
 | 5 | Danh sách giao dịch | ListView | ReadOnly | - | - | 
Hiển thị 10 giao dịch gần nhất thỏa mãn điều kiện tìm kiếm, cho phép loadmore đến khi hết giao dịch

Lấy các giao dịch TIỀN RA thuộc các trạng thái:

• Giao dịch thành công (transStatus=2)  → Hiển thị trạng thái ở màn hình danh sách "Thành công"
• Giao dịch nghi vấn/time-out tại bước hạch toán ( trạng thái GD là GD nghi vấn) (transStatus=3, resCode=98) → Hiển thị trạng thái ở màn hình danh sách "Nghi vấn"
• Hoàn tiền thành công (trạng thái GD: Gạch nợ thất bại và Trạng thái hòa tiền là Hoàn tiền thành công) (transStatus=4, refundSatus=6) → Hiển thị trạng thái ở màn hình danh sách "Thất bại"
• Hoàn tiền thất bại (Trạng thái GD là Gạch nợ thất bại và Trạng thái hoàn tiền là Hoàn tiền thất bại) (transStatus=4, refundSatus=5) →  Hiển thị trạng thái ở màn hình danh sách "Thất bại"
• Hoàn tiền timeout (Trạng thái GD là Gạch nợ thất bại và Trạng thái hoàn tiền là Giao dịch nghi vấn) (transStatus=3, resCode=98) → Hiển thị trạng thái ở màn hình danh sách "Nghi vấn"ư
• Gạch nợ timeout (transStatus=3, resCode=98) → Hiển thị trạng thái ở màn hình danh sách "Nghi vấn"
• Hạch toán thất bại → Hiển thị trạng thái ở màn hình danh sách "Thất bại"
(Không hiển thị các giao dịch chuyển tiền thất bại và gạch nợ time-out, server xử lý lọc bỏ luôn các GD ở trạng thái này)

Gồm các nội dung:

• Mã giao dịch transRefNo
• Ngày giao dịch: định dạng dd/mm/yyyy hh:mm (transTime)
• Nội dung giao dịch (transRemark)
• (-) Số tiền giao dịch = Số tiền giao dịch gốc (amount)
• Trạng thái giao dịch: Thành công, Nghi vấn, Thất bại
 | 6 | 
Icon 
 | Icon | Click | - | - | 
Click để tạo yêu cầu tra soát

Luôn enable

##### MH4: Tạo yêu cầu tra soát giao dịch qua Mobile banking
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | - | - | Tra soát khiếu nại
 | 2 | Icon Back | Icon | Click | - | - | Tạo yêu cầu tra soát
 | 3 | Home | Icon | Click | - | - | Click để quay về màn hình Trang chủ
 | 4 | Block Thông tin giao dịch
 | 5 | Tiêu đề | Label | ReadOnly | - | - | 
Thông tin giao dịch

 | 6 | Thông tin chi tiết giao dịch | Label | ReadOnly | - | - | 
Hiển thị theo thông tin giao dịch gốc

Hiển thị 3 trường thông tin đầu tiên trong chi tiết giao dịch do MB server trả về

Hiển thị mặc định 3 trường thông tin:

• Mã giao dịch transRefNo
• Nội dung giao dịch (transRemark)
• (-) Số tiền giao dịch = Số tiền giao dịch gốc (amount)
 | 7 | 
 Chi tiết giao dịch
 | Textlink | Click | - | - | 
Click để mở popup Thông tin giao dịch

Hiển thị đầy đủ thông tin giao dịch theo bảng trên

Chọn "Đóng" tại popup → đóng popup, giữ nguyên màn hình hiện tại

Click để điều hướng vào màn hình Chi tiết giao dịch của chức năng báo cáo giao dịch < >

Khi người dùng nhấn back tại màn chi tiết giao dịch: Quay trở lại màn hình Tạo yêu cầu tra soát, giữ nguyên các thông tin khách hàng đã nhập

 | 8 | 
Thông tin tra soát

 | 9 | 
Lý do tra soát
 | Combobox | Select | Yes | - | 
Chọn lý do tra soát

Giá trị gồm danh sách lý do tra soát được cấu hình tại BO, type ≠ Lý do khác

Mặc định để trống 

Chỉ được chọn 1 giá trị

 | 10 | 
Phí tra soát 
 | Lable | ReadOnly | - | - | 
Chỉ hiển thị sau khi chọn Lý do tra soát

Hiển thị phí tra soát được cấu hình tại BE tương ứng với lý do tra soát

(feeVat)

 | 11 | 
Nội dung tra soát
 | Textbox | Input | Yes | 500 | 
Cho phép nhập mọi ký tự

Focus ô Nội dung tra soát → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập 

Mặc định để trống

 | 12 | 
Tài khoản thu phí tra soát
 | Combobox | Select | Yes | - | 
Giá trị hiển thị là danh sách tài khoản thanh toán của KH (cache tại client)

Mặc định hiển thị TKTT mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.

Cho phép chọn 1 giá trị

Click vào mở ra màn hình popup chọn tài khoản:

• Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.
• nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định
 | 13 | 
Tiếp tục
 | Button | Click | - | - | 
Luôn enable

<Tham chiếu logic xử lý>

##### MH6.1: Xác thực giao dịch (SMS OTP)

Hiển thị màn hình xác thực bằng SMS OTP với trường hợp:

• KH chưa cài đặt kích hoạt Soft OTP
• KH đã cài đặt kích hoạt Soft OTP nhưng chưa thực hiện đủ (n ) giao dịch bằng SMS OTP
<Tham chiếu tài liệu Xác thực GD bằng SMS OTP>

##### MH6.2: Xác thực giao dịch (Soft OTP)

Hiển thị màn hình xác thực bằng Soft OTP với trường hợp:

• KH đã đăng ký Soft OTP và đã thực hiện đủ (n ) giao dịch bằng SMS OTP
<Tham chiếu tài liệu Xác thực bằng Soft OTP>

##### MH7: Kết quả giao dịch
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Logo | Image | ReadOnly | - | - | Logo Co-opBank
 | 2 | icon Home | Icon | Click | - | - | Click để quay về màn hình trang chủ
 | 3 | Icon thành công | Icon | ReadOnly | - | - | 

 | 4 | Thông báo | Lable | ReadOnly | - | - | Quý khách đã lập yêu cầu tra soát thành công!
 | 5 | Thông tin tra soát | Lable | ReadOnly | - | - | 
Hiển thị thông tin gồm:

• Mã tra soát
• Lý do tra soát
• Thời gian tra soát
 | 6 | Ghi chú | Lable | ReadOnly | - | - | Co-opBank sẽ xử lý yêu và cập nhật kết quả xử lý tới Quý khách trong thời gian tra soát quy định
 | 7 | 
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

 | 8 | Lưu ảnh | icon | click | 
 | 
 | Nhấn icon → Tham khảo logic xử lý
 | 9 | 
Tạo yêu cầu mới
 | 
Button
 | 
Click
 | 
-
 | 
-
 | 
Click → Quay về màn hình Chọn hình thức tra soát

#### 2.2. Tạo yêu cầu tra soát khác

##### MH8: Tạo yêu cầu tra soát khác
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | - | - | Tạo yêu cầu tra soát
 | 2 | Icon Back | Icon | Click | - | - | Click để quay lại màn hình trước đó
 | 3 | Home | Icon | Click | - | - | Click để quay về màn hình Trang chủ
 | 4 | Ngày giao dịch | Combobox | Select | Yes | - | 
Định dạng: dd/mm/yyyy

Mặc định Ngày T (Today)

Cho phép chọn, nhập lại giá trị (Hiển thị lịch tiếng Việt khi nhấn icon lịch)

Không cho phép chọn những ngày tương lai

Không cho phép chọn những ngày <(T-100) (Thời gian tối đa cho phép tìm kiếm trong vòng 100 ngày)

 | 5 | Loại giao dịch | Textbox | Input | Yes | 500 | 
Mặc định để trống

Cho phép nhập mọi ký tự

Focus → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập 

 | 6 | Số TK/Số thẻ giao dịch | Textbox | Input | Yes | 30 | 
Nhập số tài khoản/ số thẻ thực hiện giao dịch

Cho phép nhập số và chữ

Focus → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập 

Mặc định để trống

 | 7 | Số tiền giao dịch | Textbox | Input | Yes | 13 | 
Nhập vào ô số tiền::

• Chỉ cho nhập ký tự số, tối đa 13 ký tự (bao gồm cả dấu phẩy). Không nhập số bắt đầu bằng số 0
• Hiển thị ngăn cách hàng nghìn bằng dấu “,”
• Hiển thị đơn vị tiền tệ mặc định “VND”
• Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo logic xử lý

 | 8 | Số TK/Số thẻ nhận | Textbox | Input | - | 40 | 
Cho phép nhập số và chữ

Focus → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập 

Mặc định để trống

 | 9 | Mã giao dịch | Textbox | Input | - | 30 | 
Chỉ cho phép nhập chữ và số, không cho phép nhập các ký tự đặc biệt

Focus → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập 

Mặc định để trống

 | 10 | 
Lý do tra soát
 | Textbox | Input | Yes | 500 | 
Cho phép nhập mọi ký tự

Focus ô Lý do tra soát→ Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập 

Mặc định để trống

 | 11 | 
Nội dung tra soát
 | Textbox | Input | Yes | 500 | 
Cho phép nhập mọi ký tự

Focus ô Nội dung tra soát → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập 

Mặc định để trống

 | 12 | Tài khoản thu phí tra soát | Combobox | Select | Yes | - | 
Giá trị hiển thị là danh sách tài khoản thanh toán của KH do server trả về

Mặc định hiển thị TKTT mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.

Cho phép chọn 1 giá trị

Click vào mở ra màn hình popup chọn tài khoản:

• Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.
• nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định
 | 13 | Tra soát | Button | Click | - | - | 
Luôn enable

<tham chiếu logic xử lý>

##### MH9: Xác nhận yêu cầu
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | - | - | Xác nhận yêu cầu
 | 2 | Icon Back | Icon | Click | - | - | Click để quay lại màn hình trước đó
 | 3 | Home | Icon | Click | - | - | Click để quay về màn hình Trang chủ
 | 4 | Block Thông tin giao dịch
 | 5 | Ngày giao dịch | Label | ReadOnly | - | - | Hiển thị thông tin người dùng nhập
 | 6 | Loại giao dịch | Label | ReadOnly | - | - | Hiển thị thông tin người dùng nhập
 | 7 | Số TK/Số thẻ giao dịch | Label | ReadOnly | - | - | Hiển thị thông tin người dùng nhập
 | 8 | 
 Chi tiết giao dịch
 | Textlink | Click | - | - | 
Click để mở popup Thông tin giao dịch, bao gồm các thông tin:

• Ngày giao dịch (transTimeOther)
• Loại giao dịch (transTypeOther)
• Số TK/Số thẻ giao dịch (fromAcc)
• Số tiền giao dịch (amount)
• Số TK/Số thẻ nh

> ⚠️ *Nội dung đã cắt ngắn (21099 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 37.3. User Action Flow_Tra soát khiếu nại

> **Page ID:** `860098384` · **Version:** 32
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/860098384

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
 | Use Case Name | Tra soát khiếu nại
 | Use Case ID | --
 | Use Case Description | 
Khách hàng sử dụng Mobile Banking để gửi yêu cầu tra soát giao dịch (qua MB hoặc nhập tay). Hệ thống tiếp nhận, xác thực, lưu yêu cầu và hiển thị trong danh sách để BackOffice xử lý.

 | Actor | 
KH, Hệ thống MB, Backoffice

 | Priority | High
 | 
Trigger
 | 
Khách hàng chọn chức năng “Tra soát trực tuyến” và bấm gửi yêu cầu.

 | 
Pre-Condition
 | 
• Khách hàng đã đăng nhập Mobile Banking thành công.
• Chưa vượt quá số lần tra soát cho phép
 | 
Post-Condition
 | 
• Yêu cầu được ghi nhận vào hệ thống với mã tra soát riêng.
• Khách hàng nhận thông báo xác nhận đã tiếp nhận yêu cầu.
• Yêu cầu hiển thị trong danh sách để BackOffice xử lý.
 | 
Basic Flow
 | 
Tra soát giao dịch qua Mobile banking

1/ KH đăng nhập → Chọn Tra soát khiếu nại → Chọn loại Tra soát giao dịch qua Mobile Banking

2/ KH chọn TK cần tra soát, chọn loại giao dịch, nhập thời gian tra soát → Nhấn "Tìm kiếm"

3/ Hệ thống hiển thị danh sách giao dịch

4/ KH chọn icon Tra soát tại 1 giao dịch cụ thể

5/ Hệ thống hiển thị màn hình Tạo yêu cầu tra soát chi tiết

6/ KH chọn lý do và nhập nội dung mô tả, sau đó chọn Tiếp tục

7/ KH xác nhận theo PTXT theo cài đặt

8/ Hệ thống tạo yêu cầu tra soát với trạng thái "Đã tiếp nhận" 

Tra soát khác

1/ 1/ KH đăng nhập → Chọn Tra soát khiếu nại → Tra soát khác

2/ KH nhập thông tin tra soát → chọn Tiếp tục

3/ Hệ thống hiển thị màn hình xác nhận →  KH chọn "Tiếp tục"

4/ KH xác nhận theo PTXT theo cài đặt

5/ Hệ thống tạo yêu cầu tra soát với trạng thái "Đã tiếp nhận" 

Tra cứu danh sách giao dịch tra soát

1/ KH đăng nhập → Chọn Tra soát khiếu nại → chọn Tra cứu yêu cầu

2/ KH nhập điều kiện tìm kiếm 

3/ Hệ thống hiển thị danh sách yêu cầu tra soát 

4/ KH chọn 1 yêu cầu tra soát cụ thể

5/ Hệ thống hiển thị màn hình Chi tiết yêu cầu Tra soát

 | 
Exception Flow
 | 
1/ Thời gian tra soát vượt quá thời gian quy định với lý do tra soát tương ứng → Hệ thống hiển thị thông báo lỗi

2/ Loại giao dịch không hợp lệ với lý do tra soát tương ứng → Hệ thống hiển thị thông báo lỗi 

3/ Lý do tra soát được chọn đã hết lượt (n lần, cấu hình tại BO) → Hệ thống hiển thị thông báo lỗi

 | 
Bussiness Rule
 | 
1/ Lý do tra soát được quản lý tại hệ thống BackOffice. Mỗi lý do tra soát được cấu hình:

• 
• Loại giao dịch được tra soát 
• Số lần tra soát tối đa
• Thời gian tra soát tối đa (ngày)
2/ Không cho phép tạo tra soát mới cùng lý do khi giao dịch có yêu cầu tra soát đang ở trạng thái "Đã tiếp nhận"

3/ Không cho phép khách hàng hủy yêu cầu tra soát ở bất kỳ trạng thái nào

4/ Được phép cứu danh sách giao dịch tra soát trong thời gian tối đa 12 tháng (gần nhất)

5/ Khoảng thời gian tìm kiếm giao dịch để tra soát không được vượt quá 3 tháng

6/ Phí tra soát không tính vào hạn mức giao dịch

### 2/ Luồng sơ đồ

#### 2.1/ Tra soát giao dịch qua Mobile Banking

trueUntitled Diagram-1759309571115falseautotoptrue101235246

#### 2.2/ Tra soát khác

trueUntitled Diagram-1760433365069falseautotoptrue97122546

#### 2.3/ Tra cứu yêu cầu tra soát

trueUntitled Diagram-1761016165180falseautotoptrue4516414

### 3/ Logic xử lý
Lưu ý
Bổ sung serviceCode: 1210_Tra soát khiếu nại thuộc Loại dịch vụ Tra soát

Bổ sung Loại dịch vụ: 12_Tra soát

#### 3.1/ Tạo yêu cầu tra soát giao dịch qua Mobile Banking

##### MH1: Chọn hình thức tra soát
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Click icon Back | Hệ thống MB | Quay về màn hình thao tác trước đó
 | 2 | Click icon Home | Hệ thống MB | Điều hướng về màn hình Trang chủ
 | 3 | Chọn "Tra soát giao dịch qua Mobile Banking" | Hệ thống MB | Gửi yêu cầu lấy danh sách tài khoản thanh toán sang Bank
 | Bank | Truy vấn danh sách tài khoản thanh toán và trả MB server
 | Hệ thống MB | 
Nhận kết quả: 

• Không thành công: Hiển thị thông báo lỗi tương ứng
• Thành công:
• Không có tài khoản thanh toán hợp lệ (server trả list rỗng):  Hiển thị thông báo lỗi "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại",  button "Đóng".
• Nhấn "Đóng:  Đóng câu thông báo, quay lại màn hình trước đó
• Có tài khoản thanh toán hợp lệ: Hiển thị MH Tìm kiếm giao dịch qua Mobile banking
 | 4 | Chọn "Tra soát khác" | Hệ thống MB | Gửi yêu cầu lấy danh sách tài khoản thanh toán sang Bank
 | Bank | Truy vấn danh sách tài khoản thanh toán và trả MB server
 | Hệ thống MB | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng
• Thành công:
• Không có tài khoản thanh toán hợp lệ (server trả list rỗng):  Hiển thị thông báo lỗi "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại",  button "Đóng".
• Nhấn "Đóng:  Đóng câu thông báo, quay lại màn hình trước đó
• Có tài khoản thanh toán hợp lệ: Hiển thị MH:  Tạo yêu cầu tra soát khác

##### MH2: Tìm kiếm giao dịch qua Mobile Banking
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Click icon Back | Hệ thống MB | Quay về màn hình thao tác trước đó
 | 2 | Click icon Home | Hệ thống MB | Điều hướng về màn hình Trang chủ
 | 3 | Click Loại giao dịch | Hệ thống MB | 
Hiển thị popup chọn Loại giao dịch

• Thứ tự loại giao dịch được cấu hình tại BE <tham chiếu tài liệu Loại dịch vụ>
•  Chỉ trả về các Loại dịch vụ được đánh dấu cờ Trả về cho Client
 | 4 | Chọn 1 loại giao dịch cụ thể | Hệ thống MB | 
Tắt popup Danh sách loại giao dịch

Hiển thị loại giao dịch được chọn

 | 5 | Chọn Tài khoản tra soát | Hệ thống MB | 
Nếu có tài khoản thanh toán: Hiển thị màn hình popup danh sách tài khoản nguồn, bao gồm các thông tin:

• Số tài khoản
• Số dư khả dụng + đơn vị tiền tệ
Nếu không có tài khoản thanh toán, hiển thị thông báo dạng popup "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!"

 | 6 | Bấm chọn Từ ngày | Hệ thống MB | 
Hiển thị lịch cho phép chọn và cho phép chọn 1 giá trị ngày trong lịch 

Định dạng hiển thị sau khi chọn: dd/mm/yyyy

 | 7 | Bấm chọn Đến ngày | Hệ thống MB | 
Hiển thị lịch cho phép chọn và cho phép chọn 1 giá trị ngày trong lịch 

Định dạng hiển thị sau khi chọn: dd/mm/yyyy

 | 8 | Nhập giá trị ô Từ ngày, Đến ngày, nhấn "Tìm kiếm" | Hệ thống MB | 
1/ Thực hiện kiểm tra giá trị khách hàng đã chọn/nhập

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng  | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Bỏ trống Tài khoản tra cứu  | Quý khách vui lòng chọn Tài khoản tra cứu | 

 | 2 | Bỏ trống Loại giao dịch | Quý khách vui lòng chọn Loại giao dịch | 

 | 3 | Khoảng thời gian tìm kiếm lớn hơn 3 tháng (tính theo thời gian trên lịch) | Khoảng thời gian tối đa cho phép tìm kiếm là 3 tháng. Quý khách vui lòng chọn lại thời gian tra cứu | 

• Hợp lệ: Chuyển sang 2
2/ Dựa vào loại dịch vụ → Mapping với serviceCode theo cấu hình tại BE

3/ Truy vấn và tìm kiếm giao dịch theo điều kiện KH chọn dựa theo serviceCode:

Lấy các giao dịch TIỀN RA thuộc các trạng thái:

• Giao dịch thành công
• Giao dịch nghi vấn/time-out tại bước hạch toán ( trạng thái GD là GD nghi vấn) 
• Hoàn tiền thành công (trạng thái GD: Gạch nợ thất bại và Trạng thái hòa tiền là Hoàn tiền thành công) 
• Hoàn tiền thất bại (Trạng thái GD là Gạch nợ thất bại và Trạng thái hoàn tiền là Hoàn tiền thất bại) 
• Hoàn tiền timeout (Trạng thái GD là Gạch nợ thất bại và Trạng thái hoàn tiền là Giao dịch nghi vấn)
(Không trả về các giao dịch chuyển tiền thất bại và gạch nợ time-out)

4/ Hiển thị:

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng 
• Hợp lệ:
• Không có giao dịch: Hiển thị thông báo lỗi : "Không có giao dịch phát sinh trong khoảng thời gian tra cứu. quý khách vui lòng thử lại với các điều kiện tìm kiếm phù hợp"
• Đóng thông báo, giữ nguyên màn hình tìm kiếm
• Có kết quả: Hiển thị MH Danh sách giao dịch qua Mobile Banking

##### MH3: Danh sách giao dịch qua Mobile Banking
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Click icon Back | Hệ thống MB | Quay về màn hình thao tác trước đó
 | 2 | Click icon Home | Hệ thống MB | Điều hướng về màn hình Trang chủ
 | 3 | Nhập dữ liệu vào ô Tìm kiếm | Hệ thống MB | Tìm kiếm gần đúng theo các nội dung: Mã giao dịch, Nội dung giao dịch, Số tiền 
 | 4 | Vuốt lên để xem giao dịch tiếp theo | Hệ thống MB | Gửi yêu cầu lấy 10 giao dịch tiếp theo sang MB server và nhận kết quả hiển thị tiếp các giao dịch phía dưới cho đến khi lấy hết
 | 5 | 
Nhấn tab thẻ giao dịch

 | Hệ thống MB | 
1/ Truy vấn danh sách lý do tra soát khiếu nại

• Lý do
• Type (dùng để phân biệt Lý do khác)
• Phí tra soát cho từng lý do (Phí tra soát = Phí + Phí *VAT, làm tròn theo quy tắc chung) 
Không hợp lệ: Hiển thị thông báo lỗi tương ứng
 | 
 | Trường hợp | Nội dung thông báo | Xử lý
 | 1 | Không tìm thấy lý do tra soát tương ứng với loại giao dịch tương ứng | Hệ thống chưa thể xử lý yêu cầu. Quý khách vui lòng liên hệ tổng đài để được hỗ trợ. | Tắt thông báo, giữ nguyên màn hình hiện tại

Hợp lệ: Hiển thị MH Tạo yêu cầu tra soát giao dịch qua Mobile Banking

##### MH4: Tạo yêu cầu tra soát giao dịch qua Mobile banking
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Click icon Back | Hệ thống MB | Quay về màn hình thao tác trước đó
 | 2 | Click icon Home | Hệ thống MB | Điều hướng về màn hình Trang chủ
 | 3 | Click "Chi tiết giao dịch" | Hệ thống MB | 
Hiển thị màn hình chi tiết giao dịch (điều hướng đến chức năng Báo cáo giao dịch)

Nhấn Back tại màn Chi tiết giao dịch → Quay về màn hình Tạo yêu cầu tra soát, giữ nguyên các thông tin khách hàng nhập

 | 4 | Chọn "Lý do tra soát" | Hệ thống MB | 
Hiển thị popup Danh sách lý do tra soát với các lý do:

• được cấu hình cho Loại giao dịch được chọn
• có type ≠Lý do khác 
 | 5 | Chọn 1 lý do tra soát cụ thể | Hệ thống MB | 
Đóng popup

Hiển thị lý do tra soát được chọn 

Hiển thị Phí tra soát tương ứng

 | 6 | Chọn Tài khoản thu phí tra soát | Hệ thống MB | 
Hiển thị danh sách tài khoản thanh toán do Bank trả về

 | 7 | Nhấn "Tiếp tục" | Hệ thống MB | 
Thực hiện validate

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng | 
 | Trường hợp | Thông báo lỗi | Xử lý (nếu có)
 | 1 | Bỏ trống "Lý do tra soát" | Quý khách vui lòng chọn Lý do tra soát | 

 | 2 | Bỏ trống "Nội dung tra soát" | Quý khách vui lòng nhập Nội dung tra soát | 

 | 3 | Bỏ trống "Tài khoản thu phí tra soát" | Quý khách vui lòng chọn Tài khoản thu phí tra soát | 

 | 4 | Số dư khả dụng tài khoản thu phí < Số phí tra soát | Số dư tài khoản thu phí không đủ để thực hiện tra soát | 

• Hợp lệ: Chuyển sang 2
2/ Thực hiện kiểm tra điều kiện giao dịch được phép tra soát 

• Không hợp lệ: Trả về thông báo lỗi | 
 | Trường hợp | Thông báo lỗi | Xử lý (nếu có)
 | 1 | 
Lý do tra soát đã bị quá thời hạn tra soát quy định tại BE

Ví dụ: Lý do chuyển nhầm được cấu hình thời gian tra soát tối đa là 30 ngày → Những giao dịch thực hiện trước 30 ngày kể từ ngày hiện tại sẽ không thể tra soát với lý do này.
 | Quý khách không thể thực hiện tra soát do vượt quá thời hạn tra soát | 

 | 2 | 
Giao dịch đã bị quá số lần tra soát tối đa với lý do tương ứng quy định tại BE

Ví dụ: Lý do Chuyển nhầm được cấu hình số lần tra soát tối đa là 2. 
Giao dịch X đã tra soát với lý do này 2 lần → Thực hiện tạo tra soát lần 3 → Báo lỗi
 | Quý khách không thể thực hiện tra soát do vượt quá số lần tra soát | 

• Hợp lệ: Chuyển bước 2
3/ Kiểm tra PTXT

• 3.1/ Kiểm tra trạng thái Soft OTP của user
• Nếu KH đã kích hoạt Soft OTP → Chuyển sang 2.2
• Nếu KH chưa kích hoạt Soft OTP → Server xác định PTXT là SMS OTP
• 3.2/ Kiểm tra số lần giao dịch xác thực bằng SMS OTP thành công trước đó
• Nếu số lần xác thực SMS OTP < (n ) → Server xác định PTXT là SMS OTP
• Nếu số lần xác thực SMS OTP >= (n ) → Server xác định PTXT ưu tiên nhất so Server trả về là Soft OTP → Chuyển bước xác thực bằng Soft OTP
• Nếu trạng thái Soft OTP = Lock/AutoLock → Server xác định PTXT là SMS OTP
(Tham khảo Logic xác định PTXT của GD phi tài chính tại Logic kiểm tra chung Hạn mức, PTXT, Phí dịch vụ)

{n} là số lần xác thực SMS OTP trước khi xác thực bằng Soft OTP

4/ Hiển thị màn hình xác thực với PTXT tương ứng

##### MH6.1: Xác thực giao dịch (SMS OTP) + MH6.2: Xác thực giao dịch (Soft OTP)
 | 
 | 
 | 
 | 

 | 1 | Nhập OTP và chọn "Xác nhận" | Hệ thống MB | 
1/ Thực hiện xác thực giao dịch

• Nếu PTXT là SMS OTP: tham chiếu tài liệu Xác thực GD bằng SMS OTP
(Nếu xác thực bằng SMS OTP, nội dung SMS = Xac thuc tra soat khieu nai co ma OTP là 123456, co hieu luc trong 1 phut)

• Nếu PTXT là Soft OTP: tham chiếu tài liệu Xác thực bằng Soft OTP
Validate thông tin:

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng 
• Hợp lệ: Chuyển sang 2
2/ Kiểm tra OTP:

• Không hợp lệ: Trả kết quả lỗi
• Nếu PTXT là SMS OTP: tham chiếu tài liệu Xác thực GD bằng SMS OTP
• Nếu PTXT là Soft OTP: tham chiếu tài liệu Xác thực bằng Soft OTP
• Hợp lệ: Chuyển bước 2
3/ Kiểm tra trường Phí tra soát:

• Nếu Phí tra soát = 0:
• Thực hiện cập nhật bản ghi khiếu nại vào bảng quản lý Tra soát khiếu nại
• Nếu phí tra soát > 0:
• Gọi API createOnlFee sang Bank hạch toán phí tra soát
 | 2 | 
 | Bank | 
Thực hiện trừ phí tra soát và trả kết quả về cho Hệ thống MB

 | 3 | 
 | Hệ thống MB | 
Nhận, kiểm tra kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng
• TO:
• Lưu bản ghi vào bảng Quản lý tra soát khiếu nại, với trạng thái tra soát là Timeout (các thông tin cần lưu tương tự như case thành công)
• Hiển thị thông báo lỗi: "Hệ thống đang tạm thời gián đoạn. Quý khách vui lòng tra cứu tài khoản trước khi thực hiện yêu cầu mới hoặc hoặc liên hệ tổng đài Co-opBank 1900545554 để được hỗ trợ"
• Thành công: 
• Thực hiện cập nhật bản ghi khiếu nại vào bảng quản lý Tra soát khiếu nại (nếu cho có)
• Hiển thị màn hình Kết quả giao dịch

##### MH7: Kết quả giao dịch
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | 
Nhấn Icon home
 | 
Hệ thống MB
 | 
Hiển thị màn hình home

 | 2 | 
Nhấn Icon lưu ảnh
 | 
Hệ thống MB
 | 
Tham khảo tại Logic xử lý chung

 | 3 | 
Nhấn Nút chia sẻ
 | 
Hệ thống MB
 | 
Tham khảo tại Logic xử lý chung

 | 4 | 
Nhấn nút "Tạo yêu cầu mới"
 | 
Hệ thống MB
 | 
Điều hướng về về MH Chọn hình thức tra soát

#### 2.2. Tạo yêu cầu tra soát khác

##### MH8: Tạo yêu cầu tra soát khác
 | 
 | Thao tác | Tác nhân  | Mô tả
 | 1 | Chọn "Tra soát" | Hệ thống MB | 
1/ Thực hiện Validate

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng | 
 | Trường hợp | Nội dung thông báo | Xử lý (Nếu có)
 | 1 | Bỏ trống Loại giao dịch | Quý khách vui lòng nhập Loại giao dịch | 

 | 2 | Bỏ trống Số TK/ Số thẻ giao dịch | Quý khách vui lòng nhập Số TK/ Số thẻ giao dịch | 

 | 3 | Bỏ trống Số tiền giao dịch | Quý khách vui lòng nhập Số tiền giao dịch | 

 | 4 | Bỏ trống Lý do tra soát | Quý khách vui lòng nhập Lý do tra soát | 

 | 5 | Bỏ trống Nội dung tra soát | Quý khách vui lòng nhập Nội dung tra soát | 

 | 6 | 
Chưa có cấu hình Lý do tương ứng với Lý do tra soát khác
 | Hệ thống chưa thể xử lý yêu cầu. Quý khách vui lòng liên hệ tổng đài để được hỗ trợ | 

• Hợp l

> ⚠️ *Nội dung đã cắt ngắn (18271 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 37.4. Điều hướng từ tin OTT về màn hình chi tiết yêu cầu tra soát

> **Page ID:** `864197014` · **Version:** 13
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/864197014

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThanhLV | 
 | 
Tạo mới tài liệu
 | V1.0.0
Mục lục
none

### 1/ Tóm tắt Use Case
 | Use Case Name | Điều hướng từ tin OTT về màn hình chi tiết yêu cầu tra soát
 | Use Case ID | 

 | Use Case Description | 
Là người dùng, tôi muốn hiển thị màn hình chi tiết kết quả yêu cầu tra soát khi nhấn vào tin OTT

 | Actor | 
App Client, MB Server, KH

 | Priority | High
 | Trigger | 
GDV thực hiện xử lý yêu cầu tra soát trên hệ thống BO

 | 
Pre-Condition
 | 
• KH đăng nhập hệ thống thành công
• KH tạo yêu cầu tra soát trên App thành công
• GDV thực hiện xử lý yêu cầu tra soát trên hệ thống BO
 | Post-Condition | 
Sau khi nhận được OTT thông báo xử lý yêu cầu tra soát giao dịch thành công, KH nhấn vào tin OTT, App điều hướng đến màn hình chi tiết giao dịch xử lý yêu cầu tra soát

 | Basic Flow | 
• KH đăng nhập hệ thống
• KH truy cập chức năng thông báo trên App
•  KH nhấn vào tin OTT thông báo xử lý yêu cầu tra soát giao dịch thành công
• Hiển thị màn hình chi tin thông tin xử lý yêu cầu tra soát
 | Bussiness Rules | 
OTT thông báo cần chứa Mã tra soát (Request ID) để App có thể xác định và gọi đúng API chi tiết.

### 2/ Luồng sơ đồ

#### 2.1/ Sơ đồ

trueUntitled Diagram-1761901660871falseautotoptrue10324314

### 3/ Luồng màn hình

#### 3.1/ Danh sách màn hình

##### MH1: Thông báo kết quả xử lý yêu cầu tra soát

#### 3.2/ Mô tả màn hình

##### MH1: Thông báo kết quả xử lý yêu cầu tra soát
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Nội dung thông báo yêu cầu tra soát đã được xử lý qua OTT
 | 
Label
 | 
ReadOnly
 | 
--

 | -- | 
Hiển thị nội dung tin thông báo cước kèm button "Xem chi tiết":

• Type OTT: 30
• Nội dung thông báo:
• Yêu cầu tra soát {Mã tra soát} của Quý khách ngày {Ngày tra soát} đã được cập nhật kết quả. Vui lòng đăng nhập ứng dụng Co-opBank Mobile Banking để tra cứu kết quả xử lý yêu cầu tra soát. Trân trọng!
• Trong đó: {Mã tra soát} là mã hệ thống tự sinh ứng với yêu cầu tra soát của KH, {Ngày tra soát} là thời gian KH thực hiện yêu cầu tra soát với định dạng dd/mm/yyyy hh/mm/ss
 | 2 | Xem chi tiết | Button | Click | -- | -- | <Tham khảo logic xử lý>

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
KH bấm vào Thông báo trên App để xem tin OTT/ Bấm vào thông báo OTT của thiết bị
 | App Client | 
Hiển thị nội dung tin OTT thông báo yêu cầu tra soát đã được xử lý

Tin sẽ được hiển thị tại Tab Toàn bộ và Tin khác

##### MH1: Thông báo kết quả xử lý yêu cầu tra soát
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhấn vào "Xem chi tiết" trong tin OTT trên App | 
MB Client
 | 
Dựa vào Mã tra soát trong nội dung để gửi yêu cầu lấy thông tin chi tiết yêu cầu tra soát đã được xử lý xuống MB Server

 | 

 |   | MB Server | 
Dựa vào Mã tra soát để để lấy chi tiết thông tin giao dịch tra soát

• Không hợp lệ: trả thông báo mã lỗi
Danh sách lỗi
 | 
 | Trường hợp | Nội dung thông báo | 

 | 1 | TimeOut | Đang có lỗi trong quá trình xử lý. Vui lòng thử lại sau | 

• Hợp lệ: Gửi thông tin chi tiết yêu cầu tra soát đã được xử lý cho MB Client
 | 

 |   | MB Client | 
Nhận kết quả từ MB server:

• Không thành công: Hiển thị Popup lỗi tương ứng
• Thành công: Điều hướng tới màn hình chi tiết thông tin yêu cầu tra soát đã được xử lý
Tham chiếu tại tài liệu  MH 13.2

---


## 38. Nghiệp vụ Event

> **Page ID:** `918914650` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/918914650

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*3 trang con:*

### 38.1. [Bank] Luồng xử lý điều hướng và đo lường của deeplink

> **Page ID:** `919865348` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/919865348

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
  
 | A | 
ThaoCY
 | 
 | 
Tạo mới tài liệu
 | V1 | 

Mục lục
none

### 1/ Mục đích và ý nghĩa

• Mô tả tổng quan về Deeplink (phân loại, cấu trúc, thành phần)
• Luồng xử lý chính sách với các loại Deeplink 
### 2/ Tổng quan về Deeplink

Deeplink là đường dẫn sâu giúp điều hướng người dùng từ nguồn ngoài vào thẳng ứng dụng điện thoại hoặc chợ ứng dụng tùy theo hiện trạng cài đặt ứng dụng trên thiết bị. VnEvent cung cấp nền tảng cho phép tạo lập Deeplink hỗ trợ điều hướng và phương thức đo lường hiệu quả của Deeplink đó (tương tác, sự kiện chuyển đôi,... ) tương tự một số giải pháp trên thị trường. Hiện deeplink đang áp dụng nhằm đáp ứng 2 luồng sau:
 | Loại deeplink | Deeplink App to App | Deeplink Marketing
 | Mục đích | 
Cung cấp link hỗ trợ mở ứng dụng ngân hàng từ ứng dụng khác, kèm thêm đáp ứng nghiệp vụ như điều hướng vào chức năng, xác thực chữ ký, khởi tạo thông tin giao dịch,...

Ví dụ: Deeplink đặt tại app VNeID

→ Mục đích chủ yếu nhằm hỗ trợ điều hướng và chuyển tiếp dữ liệu giao dịch
 | 
Cung cấp link điều hướng người dùng từ kênh truyền thông vào thẳng chức năng trên ứng dụng ngân hàng nhằm tối ưu trải nghiệm và đo lường hiệu quả chuyển đổi

→ Mục đích chủ yếu nhằm hỗ trợ điều hướng và đo lường hiệu quả chuyển đổi

 | Usecase | Ứng dụng/website đối tác như VNeID, Cổng thanh toán,... tạo đơn hàng và cần link dẫn dang ứng dụng ngân hàng để thực hiện thanh toán cho giao dịch đó | Link gán trên nội dung truyền thông, quảng cáo, chăm sóc trên mạng xã hội, email, SMS, mã QR sự kiện, landing page,...

### 3/ Luồng xử lý chính đối với các loại Deeplink

#### 3.1/ Luồng xử lý của Deeplink app to app

 

#### 3.2/ Luồng xử lý của Deeplink marketing

---

### 38.2. Danh sách FunctionID của các chức năng chính trên ứng dụng

> **Page ID:** `905383446` · **Version:** 6
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/905383446

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
  
 | A | 
ThaoCY
 | 
 | 
Tạo mới tài liệu
 | V1 | 

Mục lục
none

### 1/ Mục tiêu tài liệu 

Tài liệu này dùng để:

• Chuẩn hóa FunctionID cho các chức năng chính của Mobile App
• Làm cơ sở cho việc điều hướng Deeplink
• Đảm bảo việc điều hướng ổn định, không phụ thuộc UI 
• Thống nhất sử dụng giữa các bên
### 2/ Phạm vi áp dụng

• Áp dụng cho Mobile Banking App
• Chỉ bao gồm các chức năng nghiệp vụ chính 
• Không bao gồm:
• Screen UI trung gian 
• Popup/Dialog thuần UI 
• Màn hình kỹ thuật (loading, error system) 
### 3/ Quy ước FunctionID

Cấu trúc:<MODULE>_<NUMBER>

Trong đó

• Module: Nhóm chức năng (AUTH, HOME, ACC, TRF, PAY, CARD, SAVE, SET, SUP,...)
• Number: Số thứ tự (01,02,...)
### 4/ Bảng tổng hợp FunctionID
 | 
 | FunctionID | Tên chức năng | Tên màn hình | Tài liệu tham khảo
 | 1 | Nhóm đăng ký mở tài khoản trực tuyến |  
 | 2 | OB_01 | Đăng ký dịch vụ | Đăng ký dịch vụ | 
 | 3 | Nhóm Thu thập sinh trắc học |  
 | 4 | BIO_01 | Thu thập sinh trắc học  | Thu thập sinh trắc học | 
 | 5 | BIO_02 | Thu thập sinh trắc học - VNeID | Xác nhận thông tin | 
 | 6 | BIO_03 | Thu thập sinh trắc học - VNeID | Từ chối chia sẻ | 
 | 7 | Nhóm Authentication |  
 | 8 | AUTH_01 | Đăng nhập ứng dụng | Đăng nhập | 
 | 9 | Nhóm Home |  
 | 10 | HOME_01 | Trang chủ | Trang chủ | 
 | 11 | Nhóm Account |  
 | 12 | ACC_01 | Danh sách tài khoản | Danh sách tài khoản | 
 | 13 | Nhóm Transfer |  
 | 14 | TRF_01 | Màn hình chuyển tiền | Chuyển tiền | 
 | 15 | TRF_02 | Chuyển tiền nội bộ cùng chủ | Khởi tạo | 
 | 16 | TRF_03 | Chuyển tiền nội bộ khác chủ | Khởi tạo | 
 | 17 | TRF_04 | Chuyển tiền nhanh 24/7 qua thẻ | Khởi tạo | 
 | 18 | TRF_05 | Chuyển tiền nhanh 24/7 qua tài khoản | Khởi tạo | 
 | 19 | TRF_06 | Chuyển tiền qua GTTT | Khởi tạo | 
 | 20 | Nhóm Payment |  
 | 21 | Pay_01 | Quét QR | Quét mã QR | 
 | 22 | Pay_02 | Thanh toán hóa đơn | Thanh toán hóa đơn | 
 | 23 | Pay_03 | Hóa đơn tiền điện | Khởi tạo
 | 24 | Pay_04 | Hóa đơn tiền nước | Khởi tạo
 | 25 | Pay_05 | Cước di động trả sau | Khởi tạo
 | 26 | Pay_06 | Cước điện thoại cố định | Khởi tạo
 | 27 | Pay_07 | Cước internet | Khởi tạo
 | 28 | Pay_08 | Cước truyền hình cap | Khởi tạo
 | 29 | Pay_09 | Thanh toán vé máy bay | Khởi tạo
 | 30 | Pay_10 | Thanh toán học phí | Khởi tạo
 | 31 | Pay_11 | Nạp tiền tài khoản VETC | Khởi tạo
 | 32 | Pay_12 | Thanh toán hóa đơn tự động | Danh sách hóa đơn đăng ký tự động | 
 | 33 | Pay_13 | Nạp tiền điện thoại | Khởi tạo | 
 | 34 | Nhóm Thông báo
 | 35 | NOTI_01 | Thông báo | Thông báo | 
 | 36 | Nhóm Setting
 | 37 | SET_01 | Cài đặt Soft OTP | Cài đặt Soft OTP | 
 | 38 | SET_02 | Đặt và quản lý Alias | Đặt và quản lý Alias | 
 | 39 | SET_03 | Quản lý thông báo | Quản lý thông báo | 
 | 40 | SET_04 | Chia sẻ thông báo BĐSD | Đăng ký | 
 | 41 | SET_05 | Cài đặt Voice OTT | Cài đặt Voice OTT | 
 | 42 | Nhóm Card |  
 | 43 | CARD_01 | Danh sách thẻ | Dịch vụ thẻ | 
 | 44 | CARD_02 | Kích hoạt thẻ | Nhập 8 số cuối của thẻ | 
 | 45 | CARD_03 | Cài đặt PIN thẻ | Cài đặt mã PIN | 
 | 46 | CARD_04 | Lịch sử giao dịch thẻ  | Lịch sử giao dịch | 
 | 47 | CARD_05 | Thanh toán dư nợ | Thanh toán thẻ tín dụng | 
 | 48 | CARD_06 | Sao kê thẻ | Sao kê thẻ (chọn kỳ sao kê) | 
 | 49 | Nhóm Saving |  
 | 50 | SAVE_01 | Danh sách tiền gửi | Danh sách tiền gửi | 

 | 51 | SAVE_02 | Mở tiền gửi trực tuyến | Khởi tạo | 
 | 52 | SAVE_03 | Tất toán tiền gửi trực tuyến | Danh sách Tất toán tiền gửi trực tuyến | 
 | 53 | SAVE_04 | Tất toán tiền gửi trực tuyến | Khởi tạo
 | 54 | SAVE_05 | Gửi gốc thêm tiền gửi tích lũy | Danh sách tài khoản Gửi gốc thêm | 
 | 55 | SAVE_06 | Gửi gốc thêm tiền gửi tích lũy | Chi tiết tài khoản tích lũy linh động
 | 56 | SAVE_07 | Gửi gốc thêm tiền gửi tích lũy | Khởi tạo
 | 57 | SAVE_08 | Rút gốc một phần | Danh sách tài khoản Rút gốc 1 phần | 
 | 58 | SAVE_09 | Rút gốc một phần | Khởi tạo
 | 59 | SAVE_10 | Thay đổi phương thức tất toán/rút gốc | Chọn phương thức tất toán/rút gốc | 
 | 60 | SAVE_11 | Thay đổi thông tin tích lũy định kỳ | Thay đổi thông tin tích lũy định kỳ | 
 | 61 | Nhóm SDK |  
 | 62 | SDK_01 | Đặt vé máy bay | Đặt vé máy bay | 

 | 63 | SDK_02 | Đặt vé tàu | Đặt vé tàu | 

 | 64 | SDK_03 | Đặt vé xem phim | Đặt vé xem phim | 

 | 65 | SDK_04 | Đặt vé xe | Đặt vé xe | 

 | 66 | SDK_05 | Mua sắm VNSHOP | Mua sắm VNSHOP | 

 | 67 | SDK_06 | Đặt phòng khách sạn | Đặt phòng khách sạn | 

 | 68 | SDK_07 | Đặt taxi | Đặt taxi | 

 | 69 | SDK_08 | Mua xổ số Vietlot | Chọn mua viettlot | 

 | 70 | Nhóm Vay
 | 71 | LOAN_01 | Tạo lệnh trả nợ vay chính chủ | Khởi tạo | 
 | 72 | LOAN_02 | Tạo lệnh trả nợ vay theo địa bàn | Khởi tạo | 
 | 73 | Nhóm Tra soát khiếu nại
 | 74 | TSOL_01 | Tra soát khiếu nại | Chọn hình thức tra soát |

---

### 38.3. Thu thập event làm báo cáo và kịch bản

> **Page ID:** `919863532` · **Version:** 13
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/919863532

| 
 | Chức năng | Màn hình | Event name -> Đặt tên theo chuẩn underscore với format "Tên chức năng_Tên màn hình_Tên thao tác", text thao tác chung như View / Click / Success / Error / Scroll / Swipe / ... | Bên thực hiện gửi | Parameter -> Theo dạng json và chuẩn camelCase, không gửi param cấp cha con hoặc định dạng không hợp lệ (chỉ hỗ trợ Dictionary, Array, String, Number, and Bool) hoặc độ dài value quá 64 ký tự | Mô tả (logic của BA khi nào gửi lên event của Client app, param gồm các key/value nào và ở định dạng nào) | Mục đích khai thác | Cụ thể mục tiêu (File nhu cầu đo lường của Bank + kịch bản AI Omni + báo cáo Deeplink mặc định bắt event Success/View)
 | 1 | Mở ứng dụng | Mở ứng dụng lần đầu | first_open | SDK analytics | 
 | Mở ứng dụng lần đầu | Báo cáo, Bám đuôi | Kịch bản bám đuôi
 | 2 | Mở ứng dụng | Mở ứng dụng lượt mới | session_start | SDK analytics | 
 | Mở ứng dụng lượt mới | Báo cáo | 

 | 3 | 
Đăng nhập
 | 
Màn đăng nhập
 | Login_Success | Client app chủ | 
 | Đăng nhập thành công | Báo cáo, Bám đuôi, Deeplink | Kịch bản bám đuôi
 | Login_EKYC_View | Client app chủ | 
 | Client đăng nhập bằng vân tay/faceid | Báo cáo | 

 | Login_EKYC_Success | Client app chủ | 
 | Clinet đăng nhập bằng vân tay/faceid thành công | Báo cáo | 

 | Login_failed | Client app chủ | 
 | Đăng nhập không thành công | Báo cáo | 

 | Màn quên mật khẩu | Login_PasswordReset | Client app chủ | 
 | Quên mật khẩu | Báo cáo | 

 | Xem thông báo | Login_Notification | Client app chủ | 
 | Click vào chức năng thông báo tai màn đăng nhập | Báo cáo | 

 | Click hỗ trợ | Login_Support | Client app chủ | 
 | Click vào chức năng hỗ trợ tai màn đăng nhập | Báo cáo | 

 | Xem ATM/CN | Login_ATM | Client app chủ | 
 | Click vào chức năng xem ATM/CN tai màn đăng nhập | Báo cáo | 

 | 4 | 
Trang chủ
 | Màn Home | Home_View | Client app chủ | 
 | Truy cập vào màn Home | Báo cáo, Bám đuôi, Deeplink | Phân tích thói quen sử dụng, vùng được quan tâm + Kịch bản bám đuôi
 | Nhìn thấy banner | Home_ViewBanner | Client app chủ | 
 | Nhìn thấy banner tại màn Home | Báo cáo | Phân tích thói quen sử dụng, vùng được quan tâm
 | Click vào banner | Home_ClickBanner | Client app chủ | 
 | Click vào banner tại màn Home | Báo cáo | Phân tích thói quen sử dụng, vùng được quan tâm
 | Click vào chức năng | Home_ClickFunction | Client app chủ | {
"functionId": "xxxxxx"
} | Click vào chức năng tại màn Home | Báo cáo | Phân tích thói quen sử dụng, vùng được quan tâm
 | 5 | 
Đăng ký tài khoản trực tuyến
 | Màn đầu tiên | Register_View | Client app chủ | 
 | Truy cập màn đầu tiên của luồng đăng ký | Báo cáo, Bám đuôi, Deeplink | Theo dõi KH mới + Kịch bản bám đuôi
 | Màn nhập SĐT đăng ký dịch vụ | Register_Phone_View | Client app chủ | 
 | KH nhập SĐT đăng ký dịch vụ | Báo cáo | 

 | Màn hình đồng ý lưu dữ liệu STH | Register_EKYC_View | Client app chủ | 
 | KH click Đồng ý & Tiếp tục | Báo cáo | 

 | Lấy thông tin định danh KH thành công | Register_EKYC_IdentityInfo_View | Client app chủ | 
 | Hiển thị thông tin định danh của KH | Báo cáo | 

 | Bước đổi mật khẩu | Register_Password_Success | Client app chủ | 
 | Đổi mật khẩu thành công trong luồng đăng ký | Báo cáo, Bám đuôi, Deeplink | Theo dõi KH mới + Kịch bản bám đuôi
 | 6 | 
Thiết lập
 | Màn thiết lập | Setting_View | Client app chủ | 
 | Truy cập vào màn thiết lập | Báo cáo | Theoi dõi hành vi bật tắt tính năng + VoiceOTT, SoftOTP
 | Màn thiết lập SoftOTP | Setting_SoftOTP | Client app chủ | {
"status": "on | off"
} | Thao tác cài đặt SoftOTP thành công | Báo cáo | Theoi dõi hành vi bật tắt tính năng + VoiceOTT, SoftOTP
 | Màn thiết lập VoiceOTT | Setting_VoiceOTT | Client app chủ | {
"status": "on | off"
} | Thao tác cài đặt VoiceOTP thành công | Báo cáo | Theoi dõi hành vi bật tắt tính năng + VoiceOTT, SoftOTP
 | 7 | 
Chuyển tiền
 | 
Màn đầu tiên
 | Transfer_Home_View | Client app chủ | {
"transferType": "xxxxxx"
} | Truy cập màn đầu tiên của luồng chuyển tiền | Báo cáo, Deeplink | Đo tỉ lệ, nhu cầu sử dụng
 | Màn khởi tạo | Transfer_Error | Client app chủ | {
"transferType": "xxxxxx"
} | Truy cập màn khởi tạo của luồng chuyển tiền | Báo cáo, Deeplink | Đo tỉ lệ, nhu cầu sử dụng
 | Màn xác nhận | Transfer_Confirm_View | Client app chủ | {
"transferType": "xxxxxx"
} | Truy cập màn xác nhận của luồng chuyển tiền | Báo cáo, Deeplink | Đo tỉ lệ, nhu cầu sử dụng
 | Màn kết quả | Transfer_Result_View | Client app chủ | {
"transferType": "xxxxxx"
} | Truy cập màn kết quả thành công của luồng chuyển tiền | Báo cáo, Bám đuôi, Deeplink | Đo tỉ lệ, nhu cầu sử dụng + Kịch bản bám đuôi
 | Lưu danh bạ | Transfer_SaveContact | Client app chủ | 
 | Lưu danh bạ ở luồng chuyển tiền | Báo cáo | Đo tỉ lệ, nhu cầu sử dụng
 | Lưu lịch chuyển tiền | Transfer_SetCalendar | Client app chủ | 
 | Lưu lịch chuyển tiền ở luồng chuyển tiền | Báo cáo | Đo tỉ lệ, nhu cầu sử dụng
 | Chỉnh hạn mức | Transfer_ChangeLimit | Client app chủ | 
 | Chỉnh hạn mức ở luồng chuyển tiền | Báo cáo | Đo tỉ lệ, nhu cầu sử dụng
 | Lỗi phát sinh | Transfer_Error | Client app chủ | {
"errorCode": "xxxxxx",
"errorDesc": "xxxxx"
} | Báo lỗi khi thao tác (lỗi validate client hoặc lỗi server trả về) ở luồng chuyển tiền | Báo cáo | Theo dõi lỗi
 | 8 | 
Quét QR
 | 
Màn quét QR
 | QRPay_ScanQR_View | Client app chủ |   | KH truy cập màn hình quét QR |   | 

 | 9 | 
Thanh toán hóa đơn
 | Màn đầu tiên | Billing_Home_View | Client app chủ | {
"txnType": "xxxxxx"
} | Truy cập màn đầu tiên của luồng thanh toán hóa đơn | Báo cáo, Deeplink | Đo tỉ lệ, nhu cầu sử dụng
 | Màn khởi tạo | Billing_Init_View | Client app chủ | {
"txnType": "xxxxxx"
} | Truy cập màn khởi tạo của luồng thanh toán hóa đơn | Báo cáo, Deeplink | Đo tỉ lệ, nhu cầu sử dụng
 | Màn xác nhận | Billing_Confirm_View | Client app chủ | {
"txnType": "xxxxxx"
} | Truy cập màn xác nhận của luồng thanh toán hóa đơn | Báo cáo, Deeplink | Đo tỉ lệ, nhu cầu sử dụng
 | Màn kết quả | Billing_Result_View | Client app chủ | {
"txnType": "xxxxxx"
} | Truy cập màn kết quả thành công của luồng thanh toán hóa đơn | Báo cáo, Bám đuôi, Deeplink | Đo tỉ lệ, nhu cầu sử dụng + Kịch bản bám đuôi
 | Bật thanh toán tự động | Billing_SetAuto | Client app chủ | {
"txnType": "xxxxxx"
} | Lưu danh bạ ở luồng thanh toán hóa đơn | Báo cáo | Đo tỉ lệ, nhu cầu sử dụng
 | Lưu danh bạ | Billing_SaveContact | Client app chủ | {
"txnType": "xxxxxx"
} | Lưu lịch thanh toán hóa đơn ở luồng thanh toán hóa đơn | Báo cáo | Đo tỉ lệ, nhu cầu sử dụng
 | Nhập voucher | Billing_TypeVoucher | Client app chủ | {
"txnType": "xxxxxx"
} | Chỉnh hạn mức ở luồng thanh toán hóa đơn | Báo cáo | Đo tỉ lệ, nhu cầu sử dụng
 | Lỗi phát sinh | Biing_Error | Client app chủ | {
"errorCode": "xxxxxx",
"errorDesc": "xxxxx",
"txnType": "xxxxxx"
} | Báo lỗi khi thao tác (lỗi validate client hoặc lỗi server trả về) ở luồng hóa đơn | Báo cáo | Theo dõi lỗi
 | 10 | 
Nạp tiền điện thoại
 | Khởi tạo giao dịch nạp tiền điện thoại | TopUp_Initialization_View | Client app chủ | 
 | KH truy cập màn khởi tạo GD nạp tiền điện thoại | 
 | 

 | 11 | 
Hệ sinh thái
 | 
Dịch vụ Phim
 | Event name thu thập của riêng SDK tiện ích | SDK tiện ích | 
 | Chọn phim | Bám đuôi | Kịch bản bám đuôi
 | Event name thu thập của riêng SDK tiện ích | SDK tiện ích | 
 | Đặt vé thành công để chuẩn bị thanh toán | Bám đuôi | Kịch bản bám đuôi
 | 
Dịch vụ Vé xe
 | Event name thu thập của riêng SDK tiện ích | SDK tiện ích | 
 | Chọn xe, ghế | Bám đuôi | Kịch bản bám đuôi
 | Event name thu thập của riêng SDK tiện ích | SDK tiện ích | 
 | Đặt vé thành công để chuẩn bị thanh toán | Bám đuôi | Kịch bản bám đuôi
 | 12 | 
Tiết kiệm
 | Màn đầu tiên | Saving_View | Client app chủ | 
 | Truy cập màn đầu tiên của luồng gửi tiết kiệm | Bám đuôi, Deeplink | Kịch bản bám đuôi
 | Chọn sản phẩm | Saving_SelectProduct | Client app chủ | 
 | Chọn sản phẩm ở luồng gửi tiết kiệm | Bám đuôi | Kịch bản bám đuôi
 | Chọn kỳ hạn | Saving_SelectTerm | Client app chủ | 
 | Chọn kỳ hạn ở luồng gửi tiết kiệm | Bám đuôi | Kịch bản bám đuôi
 | Nhập số tiền | Saving_TypeAmount | Client app chủ | 
 | Nhập số tiền ở luồng gửi tiết kiệm | Bám đuôi | Kịch bản bám đuôi
 | Màn kết quả | Saving_Result_View | Client app chủ | 
 | Truy cập màn kết quả thành công của luồng gửi tiết kiệm | Bám đuôi, Deeplink | Kịch bản bám đuôi

---

