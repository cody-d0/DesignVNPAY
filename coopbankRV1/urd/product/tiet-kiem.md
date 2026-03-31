# 📋 Tiết kiệm

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `product/`
> **Trích xuất:** 2026-03-28

---

## 30. URD_MB_COOPBANK_Tiết kiệm

> **Page ID:** `70713436` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/70713436

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*5 trang con:*

### 30.1. MB_Danh sách tiền gửi

> **Page ID:** `70713683` · **Version:** 146
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/70713683

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | TrangNH | 
 | 
Tạo mới tài liệu
 | V.1.0.0
 | 
 
 | M | TuấnVN1 | V.1.0.0 | 
MH Thông tin tài khoản bổ sung chức năng Rút gốc một phần. Hiển thị thêm thông tin: Phương thức đáo hạn, Tài khoản nhận gốc lãi
 | V.1.1.0
 | 
 
 | M | NhungNTH8 | V1.1.0 | 
Bổ sung Màn hình danh sách thêm chức năng tiết kiệm tích lũy

Bổ sung trường thông tin tại màn hình xem chi tiết
 | V1.2.0
 | 
 
 | M | HongLT |   | 
MH xem chi tiết TKTK tích lũy linh động → Đổi tên trường Lãi suất thành Lãi suất của kỳ hạn gốc (Do bank thay đổi công thức tính lãi của gửi gốc thêm)
 | 

Mục lục

### 1/ Tóm tắt Use Case
 | Use Case Name: | Danh sách tiền gửi 
 | Use Case ID: | UC_Saving_01
 | Use Case Description: | 
Là người dùng, tôi muốn xem danh sách tài khoản tiền gửi trực tuyến và tài khoản tiền gửi tại quầy tổng số dư của tài khoản đã thực hiện giao dịch mở tiền gửi tiết kiệm thành công 

 | Actor: | 
KH, App Client, MB Server, GW Bank, Core Bank

 | Priority: | Medium 
 | Trigger: | 
KH thực hiện lệnh Danh sách tiền gửi 

 | 
Pre-Condition:
 | 
1/ KH đăng nhập thành công vào hệ thống Mobile banking

2/ KH thuộc gói dịch vụ được phép sử dụng chức năng này.

3/ KH có tài khoản nguồn hợp lệ để thực hiện chức năng này

4/ KH đã mở ít nhất 1 tài khoản tiền gửi trực tuyến tại NH Co-opBank

 | Post-Condition: | 
1/ KH được Danh sách, Chi tiết tài khoản tiền gửi trực tuyến , Lịch sử giao dịch và Chi tiết lịch sử giao dịch

 | Basic Flow: | 
1/ KH đăng nhập ứng dụng

2/ KH chọn chức năng "Tiết kiệm" và thực hiện chọn chức năng  "Danh sách tiền gửi"

3/ KH chọn tài khoản xem chi tiết 

4/ Hệ thống MB/Bank truy vấn thông tin chi tiết Tài khoản tiền gửi và trả về thông tin tài khoản thành công 

 | Alternative Flow: | 
Nhập các bước tuần tự của luồng hợp lệ nhưng rẽ nhánh theo từng dòng có đầu mục thứ tự. Ví dụ: 1. KH đăng nhập ứng dụng; 2. KH chọn chức năng "Chuyển tiền nội bộ"; 3. KH chọn danh bạ thụ hưởng, số tiền, nội dung chuyển tiền; Tiếp theo mục 4 của Basic Flow.

 | Exception Flow: | 
Nhập các trường hợp ngoại lệ chính khiến usecase không thể tiếp tục. Ví dụ: 1. KH thực hiện khởi tạo giao dịch không thành công; 2. KH thực hiện xác thực giao dịch không thành công; 3. KH chọn hủy lệnh giao dịch.

 | Bussiness Rules: | 
Nhập danh sách các rule quy định (nếu có) liên quan tới chính sách, nghiệp vụ quan trọng. Ví dụ: BR-1: KH thực hiện xác thực giao dịch sai thông tin OTP 3 lần liên tiếp sẽ bị khóa chức năng gửi OTP trong vòng 30 phút.

 | Non-Funtional Requiremnt: | 
Nhập các yêu cầu về phi tài chính liên quan tới usecase. Ví dụ: NFR-1: Thời gian hiệu lực xác thực giao dịch là 120 giây.

 | Config: | 
Không có

 | Database Table of Backend: | 
Các bảng trên Backend có lưu trữ dữ liệu tra cứu liên quan tới chức năng :

1. Bảng [Lịch sử truy cập hệ thống]: Ghi nhận lịch sử truy cập vào ứng dụng

2. Bảng[Lịch sử giao dịch]: Ghi nhận lịch sử giao dịch của KH

### 2/ Luồng sơ đồ

#### Sơ đồ

trueUntitled Diagramfalseautotoptrue91110

#### Danh sách API
 | 
 | Tên API | Luồng gọi API | Input | Output | Ghi chú
 | 1 | 
Lấy danh sách tiền gửi (queryTDAccSum)
 | MB Server - GW Bank, Core Bank | 

Xem chi tiết
"accountType " :"Y","S"
"isOnline": "0"

 | 

Xem chi tiết
"totalBal": Tổng số dư 
"listAccountn ": Danh sách tài khoản
 "accountNo"
     "marturityDate ": Ngày đến hạn
 "accountClass": Kỳ hạn
 "availBalance": Số dư khả dụng
 "currency"
 "passbookNo"
 

 | 

 | 2 | Lấy chi tiết tiền gửi (queryTDAcc) | MB Server - GW Bank, Core Bank | 

Xem chi tiết
"accountType": "Y", "S"
"frozenStatus"

 | 

Xem chi tiết
"accountName"
"accountType": Tài khoản tiền gửi
"branchName": Chi nhánh/ PDG mở
"productDesc"
"termDesc"
"openDate ": Ngày hiệu lực
"marturityDate": Ngày đáo hạn
"balance": Số dư gốc
"amountBlock": Số tiền phong tỏa
"accountName ": Tên chủ tài khoản
"interestRate ": Lãi suất
"accrued_cr": Lãi cộng dồn
"passbook_no": Số sổ

 | 

 | 3 | Lịch sử giao dịch (queryTDAccTxnHist) | MB Server - GW Bank, Core Bank | 

Xem chi tiết
"systemID"
"requestId"

"accountNo"

"fromDate "

"toDate"

"pos"  

"limitRecord" 

 | 

Xem chi tiết
"systemID": Ứng dụng gửi tin điện

"requestId": ID tin điện

"accountNo" : Số tài khoản

"fromDate ": Từ ngày

"toDate": Đến ngày

"pos "= limitRecord (Giá trị từ bản ghi sẽ bằng giá trị Đến bản ghi của lần lấy lịch sử gần nhất trước đó)

"limitRecord" = pos + 10

 | 

### 3/ Luồng màn hình

#### Danh sách màn hình

MH0: Chưa có danh sách tiền gửi

MH1: Danh sách tiền gửi 

M1.1: Danh sách tiền gửi ( TH: Tổng số dư tab TK Thường )

MH1.2: Danh sách tiền gửi ( TH KH chỉ có tiền gửi thường )

MH1.3: Sắp xếp

MH2: Thông tin tài khoản ( TH Tiền gửi thường )

MH2.1: Thông tin tài khoản ( TH Tích lũy linh động ) → Đổi tên trường Lãi suất = Lãi suất của kỳ hạn gốc

MH:2.2: Thông tin tài khoản ( TH Tích lũy tự động )

MH2.3: Thông tin tài khoản ( Chức năng khác )

MH3.1: Lịch sử giao dịch (Tài khoản tiền gửi mở tại quầy)

 MH3.2: Lịch sử giao dịch (Tài khoản tiền gửi mở online)

MH3.3: Lịch sử giao dịch (Chọn khoảng thời gian)

MH4: <Chi tiết giao dịch>

MH5 : <Giấy xác nhận 

#### Mô tả màn hình

##### MH0: <Chưa có Danh sách tiền gửi > 
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

 | 1 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 2 | Tiêu đề  | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Danh sách tiền gửi 
 | 3 | Câu thông báo | Label | Click | -- | -- | 
Chưa có danh sách tài khoản tiền gửi hiển thị:

" Quý khách chưa có tài khoản Tiền gửi. Vui lòng bấm vào Mở mới để mở tiền gửi trực tuyến."

Bấm vào" Mở mới ": Điều hướng sang màn hình chức năng Mở tiền gửi trực tuyến <luồng xử lý chi tiết>

 | 4 | Mở mới | Icon | Click | -- | -- | 
Trường hợp1: Nếu KH chưa được đăng ký gói dịch vụ hiển thị Popup thông báo " Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ."

Trường hợp 2: Nếu KH đã đăng ký gói dịch vụ Điều hướng sang màn hình chức năng Mở tiền gửi trực tuyến <luồng xử lý chi tiết>

##### MH1: <Danh sách tiền gửi >
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

 | 1 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 2 | Tiêu đề  | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Danh sách tiền gửi 
 | 3 | Câu thông báo | Label | Click | -- | -- | 
Chưa có danh sách tài khoản tiền gửi hiển thị:

" Quý khách chưa có tài khoản Tiền gửi. Vui lòng bấm vào Mở mới để mở tiền gửi trực tuyến."

 | 4 | Tổng số dư gốc | Label | ReadOnly | -- | -- | totalBal
 | 5 | Icon "Sắp xếp" | Label | ReadOnly | -- | -- | 
Hiển thị có từ 3 tài khoản trở lên: Cho phép sắp xếp tài khoản Tiền gửi theo các tiêu chí

- Ngày đến hạn gần nhất (marturityDate )

- Ngày gửi mới nhất (createDt )

- Số tiền tăng dần (availBalance)

- Số tiền giảm dần

- Kỳ hạn tăng dần (tenorInDay)

- Kỳ hạn giảm dần

 | 6 | Tổng số dư gốc ( Số lượng tài khoản ) | Label | ReadOnly | -- | -- | 
Hiển thị tổng số dư của tất cả các tài khoản tương ứng với Tab được lựa chọn, đơn vị VND
Tổng số dư gốc ( tab tất cả ): totalBalTDAcc
Tổng số dư tiền gửi thường: totalAmountTdAccount

Tống số dư tiền gửi tích lũy: totalAmountAcmlAccount

 | 7 | 
Tất cả (số lượng tài khoản)
 | Tab | Click | -- | -- | 
Mặc định hiển thị ở Tab Tất cả
Hiển thị danh sách tất cả các tài khoản tiền gửi thường và tiền tích lũy

(Trường hợp: KH chỉ có Tiền gửi Thường hoặc Tiền gửi tích lũy → Chỉ hiển thị 1 tab , ẩn tab tất cả )

 | 7.1 | Tiền gửi thường( số lượng tài khoản ) | Tab | Click | -- | -- | 
• Hiển thị danh sách tất cả các tài khoản tiền gửi thường 
(Hiển thị tab TK thường khi: productType <>4 )

 | 7.2 | Tiền gửi tích lũy ( số lượng tài khoản ) | Tab | Click | -- | -- | 
• Hiển thị danh sách tất cả các tài khoản tiền gửi tích lũy
(Hiển thị tab TK tích lũy khi: productType = 4)

 | 8 | Danh sách các tài khoản ( listAccount )  | List | Click | -- | -- | 
• Hiển thị theo từng tab được lựa chọn
• Sắp xếp theo thứ tự ngày gửi ban đầu mới nhất lên trước
• Click vào tài khoản → điều hướng sang màn hình xem chi tiết 
 | 8.1 | Tài khoản tiền gửi thường | Label | Read Only | -- | -- | 
Các thông tin hiển thị bao gồm:

• Số Tài khoản tiền gửi : accountNo
• Ngày đáo hạn: Hiển thị ngày đến hạn của lần tái tục mới nhất của tài khoản (marturityDate )
• Kỳ hạn : Hiển thị kỳ hạn tương ứng với loại sản phẩm (accountClass)
• Số sổ: Chỉ hiển thị với tài khoản Tiền gửi mở  tại quầy(nếu có) ( passbookNo)
• Số dư gốc hiện tại: Table A.1 for ListAccount data elements
 | 8.2 | Tài khoản tiền gửi tích lũy | Label | ReadOnly | -- | -- | 
Các thông tin hiển thị bao gồm:

• Tài khoản tiền gửi: accountNo
• Ngày tích lũy tiếp theo: rdNextSche ( chỉ hiển thị với TK tích lũy định kỳ)
• Ngày đáo hạn: marturityDate
• Trạng thái tích lũy:rdScheStatus:Tạm dừng/ Hoạt động tích lũy (chỉ hiển thị với TK tích lũy định kỳ đang có trạng thái tạm dừng, Trường hợp đang hoạt động thì không  hiển thị )
• Kỳ hạn: accountClass
• Số dư gốc hiện tại: Table A.1 for ListAccount data elements
 | 11 | Mở mới | Icon | Click | -- | -- | 
Điều hướng sang màn hình chức năng Mở tiền gửi trực tuyến <luồng xử lý chi tiết>

( Trường hợp: KH chưa có tài khoản hiển thị icon + tooltip " Nhấn vào đây để mở mới tiền gửi trực tuyến" )

##### MH2: <Thông tin tài khoản >
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
balance  openBalance

 | 12 | Số dư gốc hiện tại | Label | ReadOnly | -- | -- | availBalance balance
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
rdPaymentAccount

(Hiển thị nếu hình thức tích lũy là tích lũy định kỳ tự động)

 | 18.5 | Trạng thái tích lũy | Label | ReadOnly | -- | -- | 
rdScheStatus 

P: Tạm dừng: Hiển thị khi KH tắt tích lũy định kỳ tự động

Y: Hoạt động: Hiển thi khi KH bật tích lũy định kỳ tự động

(Hiển thị nếu hình thức tích lũy là tích lũy định kỳ tự động)

 | 19 | Phương thức đáo hạn | Label | ReadOnly | -- | -- | 
Hiển thị phương thức đáo hạn (setType)

• setType = 0, fix tại client "Chuyển gốc và lãi sang kỳ hạn mới"
• setType = 1, fix tại client "Gốc sang kỳ hạn mới, nhận lãi về TKTT"
• setType = 2, fix tại client "Tự động tất toán, nhận gốc và lãi về TKTT"
 | 20 | Tài khoản nhận gốc lãi | Label | ReadOnly | -- | -- | 
Hiển thị tài khoản nhận gốc lãi (reciprocalAccount)

nếu phương thức đáo hạn setType = 0 (Chuyển gốc và lãi sang kỳ hạn mới) thì ẩn Tài khoản nhận gốc lãi

 | 21 | Phương thức tất toán/rút gốc
 | Label
 | ReadOnly
 | -- | -- | 
Hiển thị phương thức tất toán/ rút gốc tương ứng KH đã chọn tại màn hình mở tiết kiệm

 | 21 | Tất toán tiền gửi trực tuyến | Label | ReadOnly | -- | -- | 
Chỉ hiển thị với tài khoản Tiền gửi trực tuyến 

Kiểm tra nếu Bank đang chạy batch thì HT chặn ngay sau khi click

Nếu bank không chạy batch thì điều hướng sang màn hình chức năng Tất toán tiền gửi trực tuyến

Điều kiện Server lọc hiển thị nút chức năng < Tham khảo logic xử lý >
Trường hợp | Cấu hình tại BE (chỉ check với những chức năng có phát sinh GD tài chính | Đặc tính sản phẩm | Trường hợp | Trạng thái GD | Hình Thức tích lũy | Hiện thị chức năng
 | 

Có cấu hình các chức năng

• Tất toán tiền gửi
• Rút gốc 1 phần
• Gửi gốc thêm
(cấu hình thiếu chức năng nào thì chức năng đó không hiển thị trên app
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

=> Kết quả Server trả về client hiển thị ( usedFor=CTA)

 | 22 | Thay đổi thông tin tích lũy định kỳ | icon | Click | -- | -- | 
Click → chuyển sang màn hình Thay đổi thông tin tích lũy định kỳ

Chỉ hiển thị với Tài khoản mở trực tuyến có Hình thức tích lũy tự động

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

=> Kết quả Server trả về client hiển thị ( usedFor=CAI)

 | 22.1 | Gửi gố

> ⚠️ *Nội dung đã cắt ngắn (30454 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 30.2. MB_Mở tiền gửi trực tuyến - TK thường

> **Page ID:** `70713438` · **Version:** 196
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/70713438

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | TrangNH | 
 | 
Tạo mới tài liệu
 | 
V.1.0.0

 | 
 
 | M | TuanVN1 | V.1.0.0 | 
Bổ sung thêm điều kiện khi lấy danh sách sản phẩm tiết kiệm được phép mở tài khoản tiền gửi

Bổ sung thêm kiểm tra thời gian chạy batch của bank khi nhấn icon chức năng Tất toán, Rút gốc
 | 
V.1.1.0

 | 
17/03/2023
 | M | TuanVN1 | V.1.1.0 | 
Bổ sung thêm điều kiện lấy ds loại sản phẩm tiết kiệm
 | 

 | 
 
 | M | HongLT | 
 | 
• Mở rộng maxlength trường "Người giới thiệu" lên 11 ký tự | 

 | 
 
 | M | HongLT | 
 | Tài khoản nhận gốc lãi điều chỉnh Từ hiển thị các TKTT thuộc cùng CN/PGD mở tài khoản nguồn thành cho phép hiện all TKTT của KH | 

 | 
 
 | M | HongLT | 
 |  Bổ sung phương thức tất toán/ rút gốc tại MH Khởi tạo và Xác nhận | 

Mục lục

### 1/ Tóm tắt Use Case
 | Use Case Name: | Mở tiền gửi trực tuyến 
 | Use Case ID: | UC_Open Account Saving_02
 | Use Case Description: | 
Là người dùng tôi muốn thực hiện giao dịch mở tài khoản tiền gửi tiết kiệm thành công 

 | Actor: | 
KH, App Client, MB Server, GW Bank, Core Bank. 

 | Priority: | Medium 
 | Trigger: | 
KH thực hiện lệnh mở tiền gửi trực tuyến 

 | 
Pre-Condition:
 | 
1/ KH đăng nhập thành công vào hệ thống Mobile banking

2/ KH thuộc gói dịch vụ được phép sử dụng chức năng này.

3/ KH có tài khoản nguồn hợp lệ để thực hiện chức năng này

4/ KH có Tài khoản thanh toán đủ số dư cho phép mở tài khoản tiết kiệm

 | Post-Condition: | 
1/ KH thực hiện mở tài khoản tiết kiệm thành công

2/ Tài khoản thanh toán bị trừ số tiền tương ứng với số tiền mở sổ

 | Basic Flow: | 
1/ KH đăng nhập ứng dụng

2/ KH chọn chức năng "Tiết kiệm" và thực hiện chọn chức năng  "Mở tiền gửi trực tuyến"

3/ KH nhập/chọn thông tin

4/ KH thực hiện khởi tạo giao dịch

5/ KH thực hiện xác nhận giao dịch

6/ KH thực hiện xác thực giao dịch 

7/ Hệ thống MB/Bank xác thực giao dịch, hạch toán và trả kết quả mở tài khoản tiết kiệm thành công

 | Alternative Flow: | 
1/ KH đăng nhập ứng dụng

2/ KH chọn chức năng "Tiết kiệm" và thực hiện chọn chức năng  "Danh sách tiền gửi"

3/ KH chọn tài khoản xem chi tiết 

4/ KH chọn chức năng "Mở tiền gửi trực tuyến"

5/ KH nhập/chọn thông tin

6/ KH thực hiện khởi tạo giao dịch

7/ KH thực hiện xác nhận giao dịch 

8/ KH thực hiện xác thực giao dịch 

9/ Hệ thống MB/Bank xác thực giao dịch, hạch toán và trả kết quả mở tài khoản tiết kiệm thành công

 | Exception Flow: | 
1/ Lấy danh sách tài khoản nguồn không thành công

2/ KH thực hiện hủy yêu cầu khởi tạo giao dịch

3/ KH thực hiện khởi tạo giao dịch không thành công

4/ KH thực hiện hủy xác thực giao dịch 

5/ KH thực hiện xác thực giao dịch không thành công

6/ Mở tiền gửi trực tuyến không thành công

 | Bussiness Rules: | 

 | Non-Funtional Requiremnt: | 
Nhập các yêu cầu về phi tài chính liên quan tới usecase. Ví dụ: NFR-1: Thời gian hiệu lực xác thực giao dịch là 120 giây.

 | Config: | 
 Không có

 | Database Table of Backend: | 
Các bảng trên Backend có lưu trữ dữ liệu tra cứu liên quan tới chức năng này. 

1. Bảng [Quản lý loại sản phẩm]: Quản lý loại sản phẩm cho phép thực hiện mở tiền gửi trực tuyến trên ứng dụng MB

2. Bảng [Quản lý kỳ hạn]: Quản lý kỳ hạn với loại sản phẩm tương ứng  cho phép thực hiện mở tiền gửi trực tuyến trên ứng dụng MB

3. Bảng [Quản lý phương thức đáo hạn]: Quản lý phương thức đáo hạn với loại sản phẩm tương ứng cho phép thực hiện mở tiền gửi trực tuyến trên ứng dụng MB 

4. Bảng Báo cáo [ Báo cáo tổng hợp khách hàng sử dụng dịch vụ Mobile Banking]: Ghi nhận Báo cáo tổng hợp khách hàng sử dụng dịch vụ Mobile Banking

5. Bảng Báo cáo [ Chi tiết giao dịch]: Ghi nhận chi tiết giao dịch mở tiền gửi trực tuyến

6. Bảng [Lịch sử giao dịch]: Ghi nhận lịch sử giao dịch mở tiền gửi trực tuyến

7. Bảng Báo cáo [Báo cáo mã giới thiệu]

### 2/ Luồng sơ đồ

#### Sơ đồ

trueUntitled Diagramfalseautotoptrue158227

#### Danh sách API
 | 
 | Tên API | Luồng gọi API | Input | Output | Ghi chú
 | Truy cập chức năng và trước khi khởi tạo
 | 1 | 
Lấy danh sách tài khoản thanh toán
 | App Client- MB Server - GW Bank, Core Bank | 

 | 

 | 

 | 2 | Lấy danh sách loại sản phẩm, phương thức đáo hạn | App Client -MB Server | 

 | 

 | 

 | Khởi tạo giao dịch
 | 1 | Lấy danh sách kỳ hạn và lãi suất tương ứng theo sản phẩm (queryICRate) | App Client - MB Server - GW Bank, Core Bank | 

Xem chi tiết
"systemID":
"accountNo": 
"productCode" 

 | 

Xem chi tiết
"termDesc"
"rateList": Danh sách lãi suất
"effectiveDate"
"marturityDate"

 | 

 | 2 | Kiểm tra mã giới thiệu | App Client - MB Server | 
 | 
 | 

 | 3 | Gửi yêu cầu khởi tạo giao dịch | App Client - MB Server | 
 | 
 | 

 | 4 | 
Kiểm tra chạy batch tại Bank (queryEODstat)
 | MB Server - GW Bank, Core Bank | 

Xem chi tiết
"systemID":
"requestId"
"accountNo": 
"referenceID"
"eodStat" 

 | 

 | 

 | Xác nhận giao dịch
 | 1 | Gửi yêu cầu xác thực giao dịch | App Client - MB Server | 
 | 
 | 

 | Xác thực giao dịch
 | 1 | Mở tiền gửi trực tuyến (openTDAcc) | MB Server - GW Bank, Core Bank | 

Xem chi tiết
"systemID":
"cifNo"
"productCode"
"accountClass"
"requestId"
"debitAccount"
"amount"
"setType"
"TellerStatus": phương thức tất toán/ rút gốc KH đã chọn

 | 

Xem chi tiết
"accountNo": Số tài khoản tiền gửi
"branchName ": Chi nhánh /PGD mở
"transRefNo ": Mã giao dịch

 | 

### 3/ Luồng màn hình

#### Danh sách màn hình

MH0: Tiền gửi trực tuyến 

MH1: < Khởi tạo>

MH1.1 : <Khởi tạo>

MH1.1.1 : <Khởi tạo>TH: Không hiển thị Tài khoản nhận gốc và lãi

MH1.1.2 : <Khởi tạo> TH: Hiển thị Tài khoản nhận gốc và lãi

MH1.2 : <Điều khoản & điều kiện >

MH1.3 : <Chọn loại sản phẩm>

MH1.4 : <Chọn kỳ hạn>

MH1.5 : <Chọn phương thức đáo hạn>

MH1.6 : <Gơi ý nhập số tiền>

Chọn Phương thức tất toán/ Rút gốc

 

Chọn Phương thức tất toán/ Rút gốc

 

 MH2 : <Xác nhận giao dịch > - Bổ sung Phương thức tất toán/ Rút gốc

MH3 : Xác thực giao dịch<SMS OTP>

 MH4 : <Kết quả giao dịch>

MH5 : <Giấy xác nhận >

MH6: <Danh bạ> 

MH7: <Giấy xác nhận> Lưu file PDF

Mô tả màn hình

##### MH0: <Tiền gửi trực tuyến >
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề  | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Tiền gửi trực tuyến
 | 2 | 
Icon Back
 | Icon | Click  | -- | -- | Nhấn Back, hiển thị màn hình đang thao tác trước đó
 | 3 | Mở tiền gửi trực tuyến  | Icon + Text | Click | -- | -- | 
Trường hợp 1: Nếu KH chưa được đăng ký gói dịch vụ hiển thị Popup thông báo " Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ."

Trường hợp 2: Nếu KH đã đăng ký gói dịch vụ, kiểm tra thời gian chạy batch tại bank, Hiển thị màn hình "Mở tiền gửi trực tuyến "

 | 4 | Tất toán tiền gửi trực tuyến  | Icon + Text | Click | -- | -- | 
Trường hợp 1: Nếu KH chưa được đăng ký gói dịch vụ hiển thị Popup thông báo " Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ."

Trường hợp 2: Nếu KH đã đăng ký gói dịch vụ, kiểm tra thời gian chạy batch tại bank, Hiển thị màn hình "Tất toán tiền gửi trực tuyến"

 | 5 | Rút gốc một phần | Icon + Text | Click | -- | -- | 
Trường hợp 1: Nếu KH chưa được đăng ký gói dịch vụ hiển thị Popup thông báo " Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ."

Trường hợp 2: Nếu KH đã đăng ký gói dịch vụ, kiểm tra thời gian chạy batch tại bank, Hiển thị màn hình "Rút gốc một phần"

 | 6 | Danh sách tiền gửi trực tuyến | Icon + Text | Click | -- | -- | Hiển thị màn hình "Danh sách tiền gửi trực tuyến"

##### MH1+MH1.1+MH1.1.1+MH1.1.2: <Khởi tạo >
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề  | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Mở tiền gửi trực tuyến
 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | Yes | -- | 
Hợp lệ: 

• Mặc định hiển thị tài khoản thanh toán mặc định
• Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do bank Server trả về.
• Hiển thị Tài khoản nguồn + Số dư khả dụng tương ứng và đơn vị tiền tệ.
• Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản nguồn)
 | Thông tin mở tiền gửi
 | 1 | Loại sản phẩm | Combobox  | List | Yes | -- | 
• Mặc định trống
• 
Hiển thị danh sách theo cấu hình tại BE, chức năng quản lý sản phẩm tiết kiệm với trạng thái bản ghi là Hoạt động và có Chức năng mở tiền gửi trực tuyến

• Click vào mở ra màn hình popup chọn loại sản phẩm Chi tiết hiển thị: MH4
• Cho phép chọn 1 loại sản phẩm trong danh sách
 | 2 | Kỳ hạn | Combobox | 
List
 | Yes | -- | 
• Hiển thị danh sách kỳ hạn và lãi suất tương ứng với loại sản phẩm  
 | 3 | Lãi suất | Label | ReadOnly | -- | -- | 
Tự động hiển thị theo danh sách kỳ hạn 

Hiển thị đơn vị  mặc định “%/năm”

Đơn vị: %/năm

 | 4 | Ngày hiệu lực | Label | ReadOnly | -- | -- | 
• Hiển thị ngày hiệu lực của tài khoản sau khi chọn 1 kỳ hạn
• Định dạng: dd/mm/yyyy
• Do Bank trả về và được tính: 
• Ngày hành chính: Ngày hiệu lực = ngày hiện tại
• Ngày nghỉ, ngày lễ: Ngày hiệu lực = ngày tiếp theo sau ngày nghỉ, ngày lễ
• Ngày nghỉ: thứ 7, chủ nhật
• Ngày lễ: theo quy định của Nhà nước
 | 5 | Ngày đáo hạn  | Label | ReadOnly | -- | -- | 
• Hiển thị ngày đến hạn của lần tái tục mới nhất của tài khoản sau khi chọn 1 kỳ hạn
• Định dạng: dd/mm/yyyy
• Do Bank trả về và được tính là Ngày cuối cùng theo kỳ hạn đã chọn
 | 6 | Số tiền gửi | 
Textbox
 | 
Number
 | Yes | 15 | 
• Chỉ hiển thị sau khi chọn Kỳ hạn
• Chặn nhập: 0 và dấu cách
• Hiển thị đơn vị tiền tệ của Số tiền mặc định “VND”
• Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
• Focus textbox sẽ không ẩn trường số tiền gửi tối thiểu và hiển thị bàn phím số cho KH nhập
• Gợi ý số tiền chuyển theo quy tắc: <Tham khảo quy tắc gợi ý chung trong BẢNG MÃ LỖI CHUNG>
• Số tiền nhập < Số tiền tối thiểu thì hiển thị popup "Số tiền gửi tối thiểu là x VND. Quý khách vui lòng kiểm tra lại!"
 | 7 | Số tiền tối thiểu  | 
Label 
 | 
ReadOnly
 | -- | -- | 
Hiển thị  "Số tiền gửi tối thiểu là <x> đồng" với x là giá trị số tiền gửi tối thiểu theo cấu hình tại BE bảng quản lý sản phẩm tương ứng với loại sản phẩm chọn

 | 8 | Lãi dự tính | Text | ReadOnly | -- | -- | 
•  Chỉ hiển thị lãi dự tính sau khi nhập số tiền
• Client tự tính Lãi dự tính sau khi có lãi suất trả  về.
• Hiển thị đơn vị tiền tệ của Số tiền lãi dự tính mặc định “VND”
• Tính theo công thức = (Ngày đáo hạn – Ngày hiệu lực) * Lãi suất * Số tiền gửi / 365
• Quy tắc làm tròn:
 Lãi dự tính: Không làm tròn mà cắt đi phần thập phân.

• 
Ví dụ: 20,156.69 thì lãi dự tính hiển thị là 20,156

• Là số lãi dự tính cả kỳ đối với cả sản phẩm lĩnh lãi cuối kỳ và định kỳ
 | 9 | Phương thức đáo hạn | 
Combobox
 | 
List
 | Yes | -- | 
• Mặc định trống
• Hiển thị danh sách theo cấu hình tại BE bảng quản lý kỳ hạn với trạng thái bản ghi là Hoạt động
• 
Cho phép chọn 1 giá trị tương ứng với loại sản phẩm được config trên client 

• Click để mở ra màn hình popup chọn Phương thức đáo hạn 
• 
Giá trị bao gồm:
 | STT | Loại sản phẩm  | Phương thức đáo hạn
 | 1 | Tiền gửi lĩnh lãi cuối kỳ | 
+ Tự động tất toán, nhận gốc và lãi về TKTT
+ Gốc sang kỳ hạn mới, nhận lãi về TKTT
+ Chuyển gốc và lãi sang kỳ hạn mới 

 | 2 | Tiền gửi lĩnh lãi định kỳ tháng | 
+ Tự động tất toán, nhận gốc và lãi về TKTT
+ Gốc sang kỳ hạn mới, nhận lãi về TKTT

Popup hiển thị - MH 1.6 Chọn phương thức đáo hạn

 | 
 | Phương thức tất toán/ rút gốc | 
Combobox
 | 
List
 | Yes | -- | 
• Bao gồm 2 giá trị:
- Tất toán, rút gốc Online (Mặc định)

- Tất toán, rút gốc tại Quầy

Cho phép chọn 1 giá trị

 | 10 | Tài khoản nhận gốc lãi  | 
Label
 | 
ReadOnly
 | -- | -- | 
• Mặc định là Tài khoản nguồn. 
• Khi bấm vào thì hiện ra danh sách các TKTT của khách hàng
• Chỉ hiện các TKTT thuộc cùng chi nhánh/PGD mở TK nguồn → Bỏ
• Trường hợp: KH chọn lại tài khoản nguồn khác thì tài khoản nhận gốc lãi được chuyển về mặc định tài khoản nguồn vừa thay đổi
• Chọn xong phương thức đáo hạn thì mới hiện thị trường này. Trường hợp Chuyển gốc và lãi sang kỳ hạn mới thì không hiển thị trường này
 | 11 | Mã giới thiệu  | Textbox | Number | -- | 11 | 
• Mặc định trống, cho nhập ký tự số (là số điện thoại đăng ký MB của người giới thiệu và thuộc loại khách hàng Nhân viên có giá trị "S") (nếu có)
• Hiển thị bàn phím số
• 
Nhập mã giới thiệu chính xác: Hiển thị thêm trường Họ và tên người giới thiệu

• Nhập mã giới thiệu không chính xác, hệ thống thông báo: “Mã giới thiệu không hợp lệ. Vui lòng nhập lại thông tin hợp lệ hoặc bỏ trống”
• Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
 | 12 | Icon Danh bạ  | Icon  | Click  | -- | -- | Nhấn chọn icon Danh bạ →  focus màn hình danh bạ số điện thoại từ thiết bị  MH6
 | 13 | Điều khoản & Điều kiện | Checkbox | Click | Yes | -- | 
• Hiển thị nội dung "Tôi đã đọc, hiểu rõ, đồng ý và cam kết tuân thủ các Điều khoản, điều kiện sử dụng dịch vụ tiền gửi tiết kiệm trực tuyến trên ứng dụng Mobile Banking của Co-opbank. "
• Click vào Text như mô tả MH1.2 : <Điều khoản & điều kiện >
• 
Mặc định tích chọn, cho phép bỏ chọn/tích chọn.

• Trường Hợp KH chưa tick chọn:  Hiển thị popup thông báo :"Quý khách chưa đồng ý với Điều khoản, điều kiện sử dụng dịch vụ tiền gửi trực tuyến của Co-opbank Mobile Banking."
 | 14 | Tiếp tục | Button | 
Click
 | -- | -- | <Tham khảo logic xử lý>

##### MH1.2: <Điều khoản & điều kiện >
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
Tiêu đề: Điều khoản & điều kiện 

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
Nhấn Home, hiển thị màn hình Trang chủ

 | 4 | 
Nội dung
 | 
html
 | 
ReadOnly
 | -- | -- | 
Hiển thị nội dung Thỏa thuận mở và sử dụng tiền gửi có kỳ hạn trên kênh NHĐT

##### MH1.3 + MH 1.4 + MH 1.5 : Popup
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | MH1.3 <Chọn loại sản phẩm>
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Loại sản phẩm

 | 2 | Icon “X” | Icon | Click | -- | -- | 
Nhấn để đóng popup

• Click chọn 1 loại sản phẩm, đóng popup fill sản phẩm đã chọn vào trường dữ liệu "Loại sản phẩm”
• Không chọn sản phẩm nào, đóng popup, trường  “Loại sản phẩm” trống
 | 3 | Sản phẩm | List | Select | -- | -- | 
• Hệ thống BE trả về
• Hiển thị tên loại sản phẩm :
-Tiền gửi lĩnh lãi cuối kỳ

-Tiền gửi lĩnh lãi định kỳ hàng tháng

 | MH1.4: <Chọn kỳ hạn>
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Kỳ hạn 

 | 2 | Icon “X” | Icon | Click | -- | -- | 
Nhấn để đóng 

> ⚠️ *Nội dung đã cắt ngắn (36812 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 30.3. MB_Rút gốc 1 phần

> **Page ID:** `129925139` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/129925139

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*4 trang con:*

#### 30.3.1. UC-RUTGOC-01: Usecase Summary

> **Page ID:** `130482193` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/130482193

### 1/ Tóm tắt Usecase

 | Use Case Name | Rút gốc một phần
 | Use Case ID | UC-RUTGOC-01
 | Use Case Description | 
Là người dùng, tôi muốn rút gốc một phần từ tài khoản tiết kiệm trực tuyến thành công

 | Stage | 
• Gói tháng 12/2022: Thêm mới
 | Actor | 
KH, MB Client, MB Server, Bank

 | Priority | 
trueYellowmedium

 | Trigger | 
KH muốn rút gốc một phần về TK thanh toán

 | 
Pre-Condition
 | 
• KH truy cập chức năng "Rút gốc một phần"
• KH có gói dịch vụ được sử dụng chức năng này
• KH có tài khoản tiết kiệm hợp lệ
• Tài khoản thụ hưởng hợp lệ
• Số tiền giao dịch hợp lệ
• Số dư gốc còn lại trong tài khoản tiết kiệm hợp lệ
 | Post-Condition | 
• KH thực hiện rút gốc 1 phần về TK thành công
• Tài khoản tiết kiệm của KH bị trừ số tiền tương ứng với số tiền giao dịch (trừ phí nếu có)
• Tài khoản thụ hưởng được cộng số tiền tương ứng với số tiền giao dịch (trừ phí nếu có)
• Hệ thống MB ghi nhận giao dịch rút gốc về TK của KH
• Hệ thống MB ghi nhận log giao dịch rút gốc về TK của KH
 | Basic Flow | 
• KH truy cập chức năng "Rút gốc một phần"
• KH lựa chọn tài khoản tiết kiệm
• KH chọn/nhập thông tin: số tiền, TK nhận gốc và lãi
• KH thực hiện khởi tạo giao dịch
• KH thực hiện xác thực giao dịch
• KH nhận được kết quả giao dịch thành công
 | Alternative Flow | 

 | Exception Flow | 
• KH hủy giao dịch
• Không có TK tiết kiệm hợp lệ
• Thông tin giao dịch không hợp lệ: số tiền không hợp lệ, TK nhận tiền không hợp lệ, số dư gốc còn lại trong TK không hợp lệ
• Bank đang chạy batch
 | Bussiness Rules | 
Loại sản phẩm được phép rút gốc một phần

Số tiền rút gốc tối thiểu

Số dư gốc tối thiểu còn lại 

 | Non-Funtional Requiremnt |

---

#### 30.3.2. UC-RUTGOC-01: Flow Chart

> **Page ID:** `129925314` · **Version:** 14
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/129925314

Tùy từng dự án/chức năng, Nghiệp vụ áp dụng các sơ đồ UML phù hợp:

• Activity Diagram
• Sequence Diagram
• Stage Diagram

Mục lục
none

### 1/ Activity Diagram

trueRút gốc 1 phầnfalseautotoptrue118233

Danh sách bước thực hiện và luồng gọi giữa các hệ thống:
 | Bước người dùng thực hiện | TT | Mục đích hệ thống giao tiếp | Luồng gọi | Ghi chú
 | 
Truy cập chức năng trước khi khởi tạo
 | 
1
 | 
Kiểm tra thông tin gói dịch vụ
 | Client → Server | 

 | 
2
 | 
Lấy danh sách TK tiền gửi trực tuyến hợp lệ và TK thanh toán 
 | Client → Server → Bank | 

 | 
Màn hình danh sách TK tiết kiệm, nhấn chọn 1 TK tiết kiệm để rút gốc

 | 
1
 | 
Kiểm tra thời gian chạy batch
 | Client → Server → Bank | 

 | 
2
 | 
Lấy thông tin chi tiết TK tiết kiệm
 | Client → Server → Bank | 

 | 
3
 | 
Kiểm tra TK bị phong tỏa không
 | Client | 

 | 
Màn hình khởi tạo, nhập thông tin và nhấn tiếp tục

 | 1 | 
Lấy danh sách TK thanh toán 
 | Client → Server → Bank | gọi lại để lấy ds nếu ở truy cập chức năng chưa lấy được ds TK thanh toán
 | 
2
 | 
Kiểm tra thông tin rút gốc đã nhập/lựa chọn
 | Client | 

 | 
3
 | 
Kiểm tra số tiền rút tối thiểu, số dư gốc còn lại tối thiểu và PTXT
 | Client → Server | 

 | 
4
 | 
Kiểm tra thời gian chạy batch
 | Server → Bank | 

 | 
5
 | 
Khởi tạo giao dịch
 | Client → Server | 

 | 
Xác nhận giao dịch, lựa chọn PTXT và nhấn xác nhận

 | 
1
 | 
Xác nhận giao dịch
 | Client → Server → Bank | 

 | 
2
 | 
Hạch toán giao dịch
 | Server → Bank |

---

#### 30.3.3. UC-RUTGOC-01: Flow & Action Screen

> **Page ID:** `130482208` · **Version:** 23
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/130482208

Mục lục
none

### 1/ Luồng di chuyển màn hình

truerút gốc - luồng MHfalseautotoptrue147116

### 2/ Danh sách màn hình

##### MH0: Chức năng Tiền gửi tiết kiệm

##### MH1.1: Rút gốc một phần

##### MH1.2: Rút gốc một phần- điều kiện sắp xếp

##### MH1.3: Chức năng danh sách tiền gửi nhấn chọn 1 TK tiết kiệm → hiển thị chi tiết thông tin tài khoản

##### MH1.4: Chức năng Tài khoản, lựa chọn Tài khoản tiết kiệm, nhấn chọn 1 TK tiết kiệm -> hiển thị chi tiết thông tin tài khoản

##### MH2: Khởi tạo 

##### MH3: Xác nhận GD

##### MH4: Xác thực GD

##### MH5: Kết quả GD

### 3/ Định nghĩa màn hình

##### MH0: Chức năng Tiền gửi tiết kiệm

Tham khảo 
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Mở tiền gửi trực tuyến | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình Mở tiền gửi trực tuyến
 | 2 | Tất toán tiền gửi trực tuyến | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình Tất toán tiền gửi trực tuyến
 | 3 | Danh sách tiền gửi | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình Danh sách tiền gửi
 | 4 | Rút gốc một phần | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình Rút gốc một phần

##### MH1.1: Rút gốc một phần
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
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
Nhấn Back, hiển thị màn hình đang thao tác trước đó

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
Rút gốc một phần

 | 
3
 | 
Icon "Sắp xếp"
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị khi có từ 3 tài khoản trở lên

 | 
4
 | 
Câu thông báo
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Chọn tài khoản tiền gửi trực tuyến để Rút gốc một phần

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
Tiêu đề: Tài khoản tiền gửi trực tuyến + số lượng tài khoản

Chỉ hiển thị những tài khoản thuộc loại sản phẩm được phép rút gốc một phần (cấu hình tài khoản được phép rút gốc trong BE)

 | 
6
 | 
Tiêu đề
 | 

 | 

 | 

 | 

 | 
Tiêu đề: Tổng số dư gốc + tổng số tiền dư gốc và đơn vị tiền tệ VND

 | 
7
 | 
Icon + Số tài khoản
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị số tài khoản tiền gửi

 | 
8
 | 
Ngày hiệu lực
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Ngày hiệu lực do bank trả về (openDate)

Ngày hiệu lực được tính :

• Ngày hành chính: Ngày hiệu lực = ngày hiện tại
• Ngày nghỉ, ngày lễ: Ngày hiệu lực = ngày tiếp theo sau ngày nghỉ, ngày lễ
• Ngày nghỉ: Thứ 7, chủ nhật
• Ngày lễ: theo quy định của ngân hàng Nhà nước
 | 
9
 | 
Ngày đáo hạn
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Ngày đáo hạn do bank trả về (marturityDate)

Ngày đáo hạn được tính là Ngày cuối cùng theo kỳ hạn đã chọn

 | 10 | 
Số dư gốc hiện tại
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị số tiền của tài khoản tiền gửi trực tuyến

Số tiền + VND (availBalance)

##### MH1.2: Rút gốc một phần - Điều kiện sắp xếp
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | 
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
Tiêu đề: Sắp xếp

 | 
2
 | 
Icon "X"
 | 
Text
 | 
Click
 | 
--
 | 
--
 | 
Nhấn để đóng popup

• Click chọn 1 tiêu chí sắp xếp, đóng popup thực hiện sắp xếp tiêu chí đã chọn
• Không click chọn tiêu chí sắp xếp nào, đóng popup, Mặc định sắp xếp Ngày đến hạn gần nhất
 | 
3
 | 
Tiêu chí sắp xếp
 | 
List
 | 
Select
 | 
--
 | 
--
 | 
Cho phép sắp xếp tài theo các tiêu chí

- Ngày đến hạn gần nhất (marturityDate )

- Ngày gửi mới nhất (createDt )

- Số tiền tăng dần (availBalance)

- Số tiền giảm dần

- Kỳ hạn tăng dần (tenorInDay)

- Kỳ hạn giảm dần

##### MH1.3 & 1.4: Thông tin tài khoản
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
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
Hiển thị tên chủ tài khoản (accountName)

 | 5 | Số tài khoản Tiền gửi | Label | ReadOnly | -- | -- | 
accountNo

 | 6 | Chi nhánh/PGD mở | Label | ReadOnly | -- | -- | branchName
 | 7 | Loại sản phẩm | Label | 
ReadOnly
 | -- | -- | 
productName

 | 
8
 | Kỳ hạn | Label | ReadOnly | -- | -- | Hiển thị kỳ hạn tương ứng với loại sản phẩm (termdesc)
 | 9 | Ngày hiệu lực | Label | ReadOnly | -- | -- | 
Ngày hiệu lực do bank trả về (effectiveDate)

Ngày hiệu lực được tính :

• Ngày hành chính: Ngày hiệu lực = ngày hiện tại
• Ngày nghỉ, ngày lễ: Ngày hiệu lực = ngày tiếp theo sau ngày nghỉ, ngày lễ
• Ngày nghỉ: Thứ 7, chủ nhật
• Ngày lễ: theo quy định của ngân hàng Nhà nước
 | 10 | Ngày đáo hạn  | Label | ReadOnly | -- | -- | 
Ngày đáo hạn do bank trả về (marturityDate)

Ngày đáo hạn được tính là Ngày cuối cùng theo kỳ hạn đã chọn

 | 11 | Số tiền gốc | Label | ReadOnly | -- | -- | 
Hiển thị số tiền gốc còn lại của tài khoản tiền gửi trực tuyến (availBalance)

Số tiền + VND 

 | 12 | Số tiền phong tỏa | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị số tiền đang bị phong tỏa (amountBlock)

 | 13 | Lãi suất | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị lãi suất của tiền gửi tiết kiệm do bank trả về (interestRate)

 | 14 | Lãi cộng dồn | Label | ReadOnly | -- | -- | accrued_cr
 | 15 | Số tiền lãi đã lĩnh | Label | ReadOnly | -- | -- | 
Hiển thị theo giá trị Bank trả về. (lai_da_linh)

Nếu số tiền bằng 0 thì ẩn trường này

 | 16 | Phương thức đáo hạn | Label | ReadOnly | -- | -- | Hiển thị phương thức đáo hạn (setType)
 | 17 | Tài khoản nhận gốc lãi | Label | ReadOnly | -- | -- | 
Hiển thị tài khoản nhận gốc lãi (reciprocalAccount)

Cho phép chọn 1 giá trị trong danh sách Tài khoản thanh toán của KH

với phương thức đáo hạn là lãi nhập gốc thì không hiển thị tài khoản nhận gốc lãi

 | 18 | Tất toán tiền gửi trực tuyến | Icon | Click | -- | -- | 
Chỉ hiển thị với tài khoản Tiền gửi trực tuyến, không hiển thị đối với tài khoản gửi tiền tiết kiệm tại quầy (check qua trường passbook_no: số sổ tiết kiệm tại quầy)

Điều hướng sang màn hình chức năng Tất toán tiền gửi trực tuyến

Kiểm tra nếu Bank đang chạy batch thì HT chặn ngay sau khi click vào button Tất toán

 | 19 | Lịch sử giao dịch  | Icon | Click | -- | -- | 
Điều hướng sang màn hình chức năng Lịch sử giao dịch

 | 
20
 | Giấy xác nhận  | Icon | Click | -- | -- | 
• Khi bấm vào xem giấy xác nhận hiển thị nút Tải về, KH có thể chọn tải file PDF về máy hoặc chia sẻ qua các phương tiện
• Chỉ hiển thị đối với tài khoản mở online
 | 21 | 
Rút gốc một phần
 | 

 | 

 | 

 | 

 | 
Chỉ hiển thị những tài khoản thuộc loại sản phẩm được phép rút gốc một phần

Điều hướng sang MH chức năng Rút gốc một phần

Kiểm tra nếu Bank đang chạy batch thì HT chặn ngay sau khi click vào button Rút gốc một phần

##### MH2: Khởi tạo
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | 
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
Rút gốc một phần

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
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | 
Icon Home
 | 
Icon
 | 
Click
 | 

 | 

 | 
Nhấn Home hiển thị màn hình Trang chủ

 | 4 | 
Tài khoản tiền gửi trực tuyến
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Logo ngân hàng + Tài khoản tiền gửi trực tuyến

Hiển thị tài khoản tiền gửi trực tuyến (accountNo)

Không cho phép chọn tài khoản tiền gửi trực tuyến khác

 | 5 | 
Số dư gốc hiện tại
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị số tiền của tài khoản tiền gửi trực tuyến (availBalance)

Số tiền + VND 

 | 6 | Tiêu đề | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Thông tin tài khoản
 | 7 | 
Icon thu gọn/ mở rộng
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn mở rộng thì hiện đầy đủ thông tin tài khoản

 | 8 | 
Loại sản phẩm
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
productName

 | 9 | 
Kỳ hạn
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị kỳ hạn tương ứng với loại sản phẩm (termdesc)

 | 10 | 
Ngày hiệu lực
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Ngày hiệu lực do bank trả về (effectiveDate)

Ngày hiệu lực được tính :

• Ngày hành chính: Ngày hiệu lực = ngày hiện tại
• Ngày nghỉ, ngày lễ: Ngày hiệu lực = ngày tiếp theo sau ngày nghỉ, ngày lễ
• Ngày nghỉ: Thứ 7, chủ nhật
• Ngày lễ: theo quy định của ngân hàng Nhà nước
 | 11 | 
Ngày đáo hạn
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Ngày đáo hạn do bank trả về (marturityDate)

Ngày đáo hạn được tính là Ngày cuối cùng theo kỳ hạn đã chọn

 | 12 | 
Lãi suất
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị lãi suất của tiền gửi tiết kiệm do bank trả về (interestRate)

 | 13 | Tiêu đề | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Thông tin giao dịch
 | 14 | 
Số tiền rút gốc
 | 
Textbox
 | 
Number (15 kí tự cả dấu phẩy)
 | 
--
 | 
--
 | 
- Cho phép nhập số tiền rút gốc, có dấu phân cách hàng nghìn

- Có quy luật gợi ý số tiền

 | 15 | 
Ghi chú
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị ghi chú bên dưới trường Số tiền rút gốc

- Số tiền rút tối thiểu là x VND

- Số tiền tối thiểu sau rút gốc là y VND

x, y được cấu hình ở chức năng Quản lý sản phẩm tiết kiệm trên BE

 | 16 | 
Tài khoản nhận gốc lãi
 | 
Combobox
 | 
List
 | 
--
 | 
--
 | 
Cho phép chọn 1 giá trị trong danh sách

Cho phép chọn lại tài khoản khác trong danh sách Tài khoản thanh toán của KH

Giá trị mặc định: Tài khoản mặc định của KH tại thời điểm tất toán

Click vào mở ra màn hình popup chọn tài khoản (Định dạng: số tài khoản )

 | 17 | 
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
Mặc định Enable

##### MH3: Xác nhận giao dịch
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | 
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
Xác nhận giao dịch

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
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | 
Câu thông báo
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo

 | 4 | 
Tài khoản tiền gửi trực tuyến
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị tài khoản tiền gửi trực tuyến (accountNo)

 | 5 | 
Loại sản phẩm
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
productName

 | 6 | 
Kỳ hạn
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị kỳ hạn tương ứng với loại sản phẩm (termdesc)

 | 7 | 
Ngày hiệu lực
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Ngày hiệu lực do bank trả về (effectiveDate)

Ngày hiệu lực được tính :

• Ngày hành chính: Ngày hiệu lực = ngày hiện tại
• Ngày nghỉ, ngày lễ: Ngày hiệu lực = ngày tiếp theo sau ngày nghỉ, ngày lễ
• Ngày nghỉ: Thứ 7, chủ nhật
• Ngày lễ: theo quy định của ngân hàng Nhà nước
 | 8 | 
Ngày đáo hạn
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Ngày đáo hạn do bank trả về (marturityDate)

Ngày đáo hạn được tính là Ngày cuối cùng theo kỳ hạn đã chọn

 | 9 | 
Lãi suất
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị lãi suất của tiền gửi tiết kiệm do bank trả về (interestRate)

 | 10 | 
Số tiền gốc
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị số tiền gốc còn lại của tài khoản tiền gửi trực tuyến do bank trả về (availBalance)

Số tiền + VND 

 | 11 | 
Số tiền rút gốc
 | 
Label
 | 
ReadOnly
 | 

 | 

 | 
Hiển thị số tiền rút gốc đã nhập (transAmount)

 | 12 | 
Số tiền rút gốc bằng chữ
 | 
Label
 | 
ReadOnly
 | 

 | 

 | 
Hiển thị số tiền rút gốc bằng chữ bên dưới trường Số tiền rút gốc, bôi đỏ thông tin

 | 13 | 
Số tiền gốc còn lại
 | 
Label
 | 
ReadOnly
 | 

 | 

 | 
Số tiền gốc còn lại = Số tiền gốc - Số tiền rút gốc

 | 14 | 
Lãi suất rút trước hạn
 | 
Label
 | 
ReadOnly
 | 

 | 

 | 
Là lãi suất không kỳ hạn (KKH) tại thời điểm rút gốc được bank trả về thông tin, bôi đỏ thông tin (ratekkh)

 | 15 | 
Số tiền lãi thu hồi
 | 
Label
 | 
ReadOnly
 | 

 | 

 | 
Hiển thị số tiền lãi thu hồi được bank trả về thông tin (lai_thu_hoi)

Nếu bằng 0 hoặc Null thì ẩn trường này

 | 16 | 
Số tiền lãi thực hưởng
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Là số tiền tính trên số tiền rút gốc với lãi suất KKH do bank trả về (lai_giao_dich)

 | 17 | 
Tổng số tiền
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Tổng số tiền (Amount) = Số tiền rút gốc + số tiền lãi thực hưởng - số tiền lãi thu hồi (nếu có); do bank trả về

 | 18 | 
Tài khoản nhận gốc lãi
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị tài khoản nhận gốc lãi đã lựa chọn (reciprocalAccount)

 | 19 | 
Phương thức xác thực
 | 
Combobox
 | 
Select
 | 
Yes
 | 
--
 | 
Hiển thị đủ 3 phương thức xác thực (TouchID/FaceID, SMS OTP, SoftOTP) nếu KH có cài đặt, KH để có thể lựa chọn bất kỳ không theo logic hạn mức của các màn hình khác

 | 20 | 
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

##### MH4: Xác thực

Tham khảo tại màn hình xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH5: Kết quả
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
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
Rút gốc một phần thành công

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
Số tiền hiển thị là trường Tổng số tiền

Số tiền bằng số + đơn vị tiền tệ

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
Tài khoản tiền gửi trực tuyến
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị số tài khoản tiền gửi trực tuyến

 | 
9
 | 
Tài khoản nhận gốc lãi
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị số tài khoản nhận gốc lãi

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
Điều hướng về màn hình khởi tạo giao dịch ban đầu

 | 
12
 | 
Nhấn Nút chia sẻ
 | 
Icon
 | 
Click
 | 
--
 | 
 --
 | 
Tham khảo tại Logic xử lý chung

 | 
13
 | 
Nhấn Icon lưu ảnh
 | 
Icon
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
Danh sách tiền gửi
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Điều hướng về màn hình chức năng Danh sách tiền gửi

---

#### 30.3.4. UC-RUTGOC-01: User Action Flow

> **Page ID:** `130482491` · **Version:** 36
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/130482491

Mục lục
none

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Thời gian cập nhật
 | 18/01/2023 | A | TuấnVN1 | 
 | 
Tạo mới
 | V.1 | 

 | 
 
 | M | HongLT | V.1 | 
Cập nhật Rule lọc cho phép tài khoản tiết kiệm được tất toán:

• App cũ: theo trường PassbookNo
• App mới: theo trường PassbookNo+ TellerStatus (do bank mới bổ sung trường này sau khi có chức năng mới tiết kiệm tích lũy) | 
 | 

### 1/ Truy cập chức năng
 | 
 | Tác nhân | Mô tả
 | 1
 | 2 | Ứng dụng MB | 
Kiểm tra thông tin gói dịch vụ của KH

• Không hợp lệ: Hiển thị thông báo lỗi

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi | Xử lý (nếu có)
 | 1 | Gói dịch vụ không bao gồm dịch vụ đã lựa chọn | Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ. | 
 | 

• Hợp lệ: Gửi yêu cầu lấy danh sách tài khoản tiền gửi trực tuyến cho phép rút gốc 1 phần và ds TK thanh toán
 | 3 | Bank server | 
Nhận yêu cầu, truy vấn thông tin và trả kết quả cho ứng dụng MB

• Không thành công: Trả lỗi cho Ứng dụng MB

 | 
 | Trường hợp | Mã lỗi | Xử lý (nếu có)
 | 1 | Lỗi timeout không truy vấn được tài khoản tiền gửi | 
 | 

 | 2 | Lỗi timeout không truy vấn được tài khoản thanh toán | 
 | 

 | 3 | Tài khoản tiền gửi không tồn tại | 
 | 

 | 4 | Tài khoản thụ hưởng không tồn tại | 
 | 

• Thành công: Trả kết quả thành công cho Ứng dụng MB
 | 4 | Ứng dụng MB | 
1/ Nhận kết quả từ Bank

• Không thành công: Hiển thị thông báo lỗi 

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi | Xử lý (nếu có)
 | 1 | Không lấy được ds TK tiết kiệm | Không lấy được danh sách tài khoản tiền gửi trực tuyến. Quý khách vui lòng thử lại | 
 | Tắt thông báo sẽ về MH home của app bank
 | 2 | Không có TK tiết kiệm hợp lệ | Quý khách không có tài khoản tiền gửi trực tuyến hợp lệ để thực hiện chức năng này | 
 | Tắt thông báo sẽ về MH home của app bank
 | 3 | Không lấy được TK thanh toán |   | 
 | Không hiển thị lỗi này, khi rút gốc lựa chọn TK nhận gốc  lãi thì sẽ check và gọi lại để lấy danh sách TK thanh toán
 | 4 | Không có TK thanh toán hợp lệ |   | 
 | Không hiển thị lỗi này, khi rút gốc lựa chọn TK nhận gốc  lãi thì sẽ check và gọi lại để lấy danh sách TK thanh toán

• Thành công: Có danh sách TK trả về → Chuyển bước 2
2/ Kiểm tra version app

• App cũ (Không có truyền trường SubType) → Giữ nguyên rule cũ trước 10/07/2024 là Client lọc
                 - Tài khoản tiết kiệm được phép Rút gốc/Tất toán Online phải được mở Online (Mở tại quầy không được phép tất toán/rút gốc Online) →  trường passbookNo bank trả = null (mở online), passbookNo # null ( mở tại quầy)

                - Tài khoản tiết kiệm có thuộc loại sản phẩm đang hoạt động + được phép  tích chọn chức năng Rút gốc/Tất toán (khai báo trên BE, chức năng QL sản phẩm tiết kiệm)

• App mới (Có truyền trường SubType) → MB Server lọc và trả về cho Client Danh sách TKTK được sử dụng cho chức năng nào
                - Tài khoản tiết kiệm được phép Rút gốc/tất toán Online phải được mở Online và có phương thức Rút gốc/tất toán = Online ((passbook_no = Null + tellerStatus=1)

                - Tài khoản tiết kiệm có thuộc loại sản phẩm đang hoạt động + được phép tích chọn chức năng Rút gốc/ Tất toán (khai báo trên BE, chức năng QL sản phẩm tiết kiệm)

3/ Trả kết quả danh sách tài khoản tiết kiệm được phép Rút gốc cho Client (nếu dstk hợp lệ sẽ có usedfor = SPW)

### 2/ Rút gốc một phần
 | 
 | Tác nhân | Mô tả
 | 
#### Event 1: Tại MH Rút gốc một phần, KH nhấn chọn 1 tài khoản tiết kiệm

 | 1 | Ứng dụng MB | 
Gửi yêu cầu kiểm tra chạy batch

 | 2 | Bank server | 
Nhận yêu cầu kiểm tra chạy batch, truy vấn thông tin và trả kết quả cho Ứng dụng MB

• Không thành công: Trả lỗi cho Ứng dụng MB

 | 
 | Trường hợp | Mã lỗi | Xử lý (nếu có)
 | 1 | Bank đang chạy batch | 
 | 

• Thành công: Trả kết quả thành công cho Ứng dụng MB
 | 3 | Ứng dụng MB | 
Nhận kết quả từ bank server

• Không thành công: hiển thị thông báo lỗi 

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi | Xử lý (nếu có)
 | 1 | Bank đang chạy batch | Xin lỗi quý khách, hệ thống đang xử lý dữ liệu cuối ngày. Quý khách vui lòng không thực hiện giao dịch | 
 | Tắt thông báo sẽ giữ nguyên MH Rút gốc một phần

• Thành công:  Gửi yêu cầu lấy thông tin chi tiết tài khoản tiết kiệm sang bank
 | 4 | Bank server | 
Nhận yêu cầu lấy thông tin chi tiết tài khoản tiết kiệm, truy vấn thông tin và trả kết quả cho Ứng dụng MB

• Không thành công: Trả lỗi cho Ứng dụng MB

 | 
 | Trường hợp | Mã lỗi | Xử lý (nếu có)
 | 1 | Không lấy được thông tin tài khoản tiết kiệm | 
 | 

• Thành công: Trả kết quả thành công cho Ứng dụng MB
 | 5 | Ứng dụng MB | 
Nhận kết quả từ bank server

• Không thành công: hiển thị thông báo lỗi 

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi | Xử lý (nếu có)
 | 1 | Không lấy được thông tin tài khoản tiết kiệm | Không lấy được thông tin tài khoản tiền gửi trực tuyến. Quý khách vui lòng thử lại | 
 | Tắt thông báo sẽ giữ nguyên MH Rút gốc một phần

• Thành công:  trả thông tin chi tiết tài khoản tiết kiệm và hiển thị MH Khởi tạo với các thông tin theo mô tả màn hình

### 3/ Khởi tạo giao dịch
 | TT | Tác nhân | Mô tả
 | 
#### Event 1: KH nhập số tiền rút gốc, lựa chọn tài khoản nhận gốc lãi

 | 1 | Ứng dụng MB | 
Kiểm tra khi truy cập vào chức năng đã lấy danh sách tài khoản thành công chưa?

• Đã lấy thành công trước đó: Hiển thị popup chọn tài khoản nhận gốc lãi gồm:

• Tiêu đề: Tài khoản nhận gốc lãi
• Hiển thị Số tài khoản
• Chưa thành công: Gửi yêu cầu lấy danh sách tài khoản thanh toán đến Bank
 | 2 | Bank server | 
Xử lý và phản hồi kết quả lấy danh sách tài khoản thanh toán đến Ứng dụng MB

• Không thành công: Trả lỗi cho Ứng dụng MB

 | 
 | Trường hợp | Mã lỗi | Xử lý (nếu có)
 | 1 | Lỗi Timeout | 
 | 

 | 2 | Không có tài khoản thanh toán hợp lệ | 
 | 

• Thành công: Trả kết quả thành công cho Ứng dụng MB
 | 3 | Ứng dụng MB | 
Nhận kết quả từ bank server

• Không thành công: hiển thị thông báo lỗi 

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi | Xử lý (nếu có)
 | 1 | Lỗi Timeout | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | 
 | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.
 | 2 | Không có tài khoản thanh toán hợp lệ | Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại! | 

 | Nhấn Đóng, tắt popup và hiển thị MH đang thao tác.

• Thành công: Hiển thị popup danh sách các tài khoản thanh toán
 | 
#### Event 2: Tại popup danh sách các TK thanh toán, KH Chọn 1 “Tài khoản nhận gốc lãi”

 | 1 | Ứng dụng MB | 
Fill thông tin số tài khoản vào ô tài khoản nhận gốc lãi

Lưu ý: Chỉ được phép chọn 1 tài khoản

 | 
#### Event 3: Nhấn "Tiếp tục"

 | 1 | Ứng dụng MB | 
1/ Kiểm tra các thông tin

• Không hợp lệ: Hiển thị thông báo lỗi

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi | Xử lý (nếu có)
 | 1 | Bỏ trống số tiền | Quý khách vui lòng nhập số tiền | 
 | 

 | 2 | Bỏ trống tài khoản nhận gốc lãi | Quý khách vui lòng lựa chọn tài khoản nhận gốc và lãi | 
 | 

 | 3 | Số tiền rút gốc < Số tiền rút tối thiểu | Số tiền rút gốc tối thiểu là: {n} VND. Quý khách vui lòng kiểm tra lại! | 
 | Nhấn nút "Kiểm tra lại" giữ nguyên MH hiện tại, focus vào ô Số tiền rút gốc
 | 4 | [Số dư gốc hiện tại] – [Số tiền rút gốc 1 phần] < [Số dư gốc tối thiểu còn lại]; TK rút gốc không được phép tất toán | Số dư còn lại sau giao dịch rút gốc không được nhỏ hơn số dư gốc tối thiểu là {m} VND. Quý khách vui lòng kiểm tra lại! | 
 | 
Nhấn nút "Kiểm tra lại" giữ nguyên MH hiện tại, focus vào ô Số tiền rút gốc

 | 5 | [Số dư gốc hiện tại] – [Số tiền rút gốc 1 phần] < [Số dư gốc tối thiểu còn lại]; TK rút gốc được phép tất toán | Số dư còn lại sau giao dịch rút gốc không được nhỏ hơn số dư gốc tối thiểu là {m} VND. Quý khách vui lòng sử dụng chức năng tất toán tiền gửi trực tuyến. | 
 | 
Nhấn nút "Tất toán" sẽ điều hướng về MH Khởi tạo của chức năng Tất toán tiền gửi trực tuyến với Số tài khoản thực hiện tất toán chính là Số tài khoản đang thực hiện rút gốc

Kiểm tra nếu Bank đang chạy batch thì HT chặn ngay sau khi click vào button

Nhấn nút "Kiểm tra lại" giữ nguyên MH hiện tại, focus vào ô Số tiền rút gốc

Điều kiện để TK tiết kiệm được phép rút gốc bao gồm:

- Tài khoản tiết kiệm được phép Rút gốc một phần Online phải được mở Online và có phương thức tất toán/rút gốc Onlune (passbook_no = Null + tellerStatus=1)

- Tài khoản tiết kiệm thuộc danh sách loại sản phẩm được cho phép tất toán (khai báo trong QL sản phẩm tiết kiệm trên BE, used_for = CTA)

Lưu ý: 

- Số tiền rút tối thiểu, Số dư gốc còn lại tối thiểu được khai báo trong chức năng Quản lý sản phẩm tiết kiệm (sản phẩm tiết kiệm có Trạng thái: hoạt động, Chức năng: rút gốc 1 phần)

- Nếu ngày rút gốc < ngày hiệu lực thì vẫn thực hiện đc rút tiền và được hưởng lãi suất không kỳ hạn

- Nếu ngày rút gốc >= ngày hiệu lực thì vẫn thực hiện đc rút tiền và được hưởng lãi suất không kỳ hạn

- Nếu ngày rút gốc > ngày đáo hạn thì vẫn theo các nguyên tắc chung của rút gốc

• Hợp lệ: Kiểm tra hạn mức giao dịch, phí, PTXT
2/ Kiểm tra các điều kiện về hạn mức giao dịch, phí, PTXT
 | STT | Loại hạn mức/phí | Yêu cầu
 | 1 | Hạn mức tối thiểu/ Giao dịch | không kiểm tra
 | 2 | Hạn mức tối đa/ Giao dịch | không kiểm tra
 | 3 | Hạn mức về số lần giao dịch/ ngày | không cộng dồn số lần giao dịch, không kiểm tra
 | 4 | Hạn mức theo nhóm chuyển tiền/ ngày (Cài đặt trên App) | không kiểm tra
 | 5 | Hạn mức theo nhóm dịch vụ 630/ngày/ PTXT | không kiểm tra
 | 6 | 
Phí giao dịch
 | có kiểm tra
 | 7 | Phương thức xác thực | kiểm tra PTXT theo user

Kiểm tra PTXT theo user

• Nếu user có cài đặt Soft OTP ( đã xác thực đủ n GD tài chính) + có cài đặt FaceID/TouchID → Lấy ra các PTXT : TouchID/ FaceID, SMS OTP, SOFT OTP
• Nếu user có cài đặt Soft OTP (đã xác thực đủ n GD tài chính) + không cài đặt FaceID/TouchID → Lấy ra các PTXT: SMS OTP, SOFT OTP
• Nếu user không cài đặt Soft OTP (hoặc có cài Soft OTP nhưng chưa xác thực đủ n GD tài chính) + có cài đặt FaceID/TouchID → Lấy ra các PTXT TouchID/FaceID, SMS OTP
• Nếu user không cài đặt Soft OTP (hoặc có cài Soft OTP nhưng chưa xác thực đủ n GD tài chính)+ không cài đặt FaceID/TouchID → Lấy ra PTXT SMS OTP
3/ Gửi yêu cầu kiểm tra thời điểm chạy batch của bank server

 | 2 | Bank server | 
Xử lý và phản hồi kết quả lấy danh sách tài khoản thanh toán đến Ứng dụng MB

• Không thành công: Trả lỗi cho Ứng dụng MB

 | 
 | Trường hợp | Mã lỗi | Xử lý (nếu có)
 | 1 | Lỗi Timeout | 
 | 

 | 2 | Tại thời điểm bank chạy batch, không cho phép rút gốc | 
 | 

• Thành công: Trả kết quả thành công cho Ứng dụng MB
 | 3 | Ứng dụng MB | 
Nhận kết quả từ bank server

• Không thành công: hiển thị thông báo lỗi 

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi cấu hình | Xử lý (nếu có)
 | 1 | Timeout | Hệ thống đang tạm thời gián đoạn. Quý khách vui lòng thử lại | 999 | 

 | 2 | Tại thời điểm bank chạy batch, không cho phép rút gốc | Xin lỗi quý khách, hệ thống đang xử lý dữ liệu cuối ngày. Quý khách vui lòng không thực hiện giao dịch | 
 | 

 | 3 | Tài khoản bị phong tỏa | "Tài khoản của Quý khách đang bị phong tỏa. Quý khách vui lòng đến Chi nhánh/Quầy giao dịch ngân hàng gần nhất để được hỗ trợ." | 
 | Tắt thông báo sẽ giữ nguyên MH Rút gốc một phần

• Thành công: thực hiện khởi tạo giao dịch, hiển thị màn hình Xác nhận giao dịch

### 4/ Xác nhận giao dịch
 | TT | Tác nhân | Mô tả
 | 
#### Event 1: KH chọn 1 PTXT và nhấn "Xác nhận"

 | 1 | Ứng dụng MB | 
Chuyển sang màn hình xác thực giao dịch theo phương thức xác thực tương ứng đã chọn:

• Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)
• Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)
• Nếu phương thức xác thực là vân tay → Gửi yêu cầu xác thực giao dịch (Tham khảo logic xử lý tại Xác thực bằng Touch ID/Face ID)

### 5/ Xác thực giao dịch
 | TT | Tác nhân | Mô tả
 | 
#### Event 1: KH kiểm tra thông tin giao dịch và thực hiện xác thực bằng PTXT tương ứng (TouchID/FaceID, SMS OTP, SoftOTP)

 | 1 | Ứng dụng MB | 
Kiểm tra:

• Không hợp lệ: Hiển thị thông báo lỗi

 | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Bỏ trống OTP | Quý khách vui lòng nhập mã OTP | 

 | 2 | Mã OTP nhỏ hơn 6 ký tự | Mã OTP phải bao gồm 6 ký tự | 

• Hợp lệ: Gửi yêu cầu xác nhận giao dịch rút gốc sang Bank
 | 3 | Bank | 
Xử lý hạch toán:

• Không thành công: Trả kết quả lỗi cho Ứng dụng

 | 
 | Trường hợp | Mã lỗi | Xử lý (nếu có)
 | 1 | Timeout | 
 | 

 | 2 | Tài khoản bị phong tỏa | 
 | 

 | 3 | Hạch toán thất bại | 
 | 

• Thành công: Trả kết quả thành công cho Ứng dụng MB
 | 4 | Ứng dụng MB | 
1/ Không nhận được kết quả:

• Cập nhật trạng thái giao dịch "Timeout"
• Hiển thị thông báo lỗi "Timeout"

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi cấu hình | Xử lý (nếu có)
 | 1 | Timeout tại bước xác thực giao dịch | Hệ thống đang tạm thời gián đoạn. Quý khách vui lòng thử lại | 999 | 

2/ Nhận được kết quả:

• Timeout:
• Cập nhật trạng thái giao dịch "Timeout"
• Hiển thị thông báo lỗi "Timeout"

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi cấu hình | Xử lý (nếu có)
 | 1 | Bank phản hồi kết quả timeout tại bước xác thực | Hệ thống đang tạm thời gián đoạn. Quý khách vui lòng thử lại | 999 | 

• Không thành công:
• Cập nhật trạng thái giao dịch "Thất bại"
• Hiển thị thông báo lỗi tương ứng

 | 
 | Trường hợp | Nội dung thông báo | Mã lỗi cấu hình | Xử lý (nếu có)
 | 1 | Hạch toán thất bại | Hiển thị thông báo lỗi theo mã lỗi theo từng hệ thống trả về | 
 | 

 | 2 | Tài khoản bị phong tỏa | Tài khoản của Quý khách đang bị phong tỏa. Quý khách vui lòng đến Chi nhánh/Quầy giao dịch ngân hàng gần nhất để được hỗ trợ.  | 
 | 

• Thành công:
• Cập nhật trạng thái giao dịch "Thành công"
• Hiển thị màn hình kết quả thành công

### 6/ Kết quả giao dịch
 | TT | Tác nhân | Mô tả
 | 
#### Event 1: Tại màn hình Kết quả GD, KH nhấn chọn "Lưu ảnh"

 | 1 | Ứng dụng MB | 
Tham khảo tại Logic xử lý chung

 | 
#### Event 2: Tại màn hình Kết quả GD, KH nhấn chọn "Chia sẻ"

 | 1 | Ứng dụng MB | 
Tham khảo tại Logic xử lý chung

 | 
#### Event 3: Tại màn hình Kết quả GD, KH nhấn chọn "Tạo giao dịch mới"

 | 1 | Ứng dụng MB | 
Điều hướng về MH Rút gốc một phần, xóa các dữ liệu của GD trước đó và thực hiện như mục 1/ Truy cập chức năng

 | 
#### Event 4: Tại màn hình Kết quả GD, KH nhấn chọn "Danh sách tiền gửi"

 | 1 | Ứng dụng MB | 
Điều hướng về MH Danh sách tiền gửi và thực hiện như bước 1 của chức năng Danh sách tiền gửi

Tham khảo

---

### 30.4. MB_Tất toán tiền gửi trực tuyến

> **Page ID:** `70719727` · **Version:** 15
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/70719727

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
14/03/2022
 | A | TrangNH | 
 | 
Tạo mới tài liệu 
 | V.1.0.0
 | 
23/12/2022
 | M | TuanVN1 | V.1.0.0 | 
1. MH Tiền gửi tiết kiệm bổ sung chức năng Rút gốc một phần

2. Bổ sung thêm số tiền bằng chữ ở MH khởi tạo và xác nhận

3. Bổ sung thêm kiểm tra chạy batch khi ấn chọn 1 tài khoản để tất toán
 | V1.1.0
 | 
17/03/2023
 | M | TuanVN1 | V1.1.0 | 
Bổ sung thêm điều kiện hiển thị ds tài khoản tiết kiệm được tất toán
 | V1.1.1
 | 
 
 | M | 
 | V.1.1.1 | 
Do bank mới bổ sung chức năng mới cho phép thay đổi phương thức tất toán/ rút gốc tại Quầy/Online nên Rule lọc cho phép tài khoản tiết kiệm được tất toán bị thay đổi như sau:

• Bổ sung truyền tên chức năng (Usedfor) cần lấy DSTKTK
• App cũ Client vẫn lọc DSTKTK theo trường PassbookNo + Usedfor.  App mới server lọc theo trường PassbookNo+Usedfor+ TellerStatus  | V1.1.2

Mục lục

### 1/ Tóm tắt Use Case
 | Use Case Name: | Tất toán tiền gửi trực tuyến
 | Use Case ID: | UC_Close Account Saving_03
 | Use Case Description: | 
 Là người dùng tôi muốn thực hiện giao dịch tất toán tiền gửi trực tuyến thành công

 | Actor: | 
KH, App Client, MB Server, GW Bank, Core Bank

 | Priority: | Medium 
 | Trigger: | 
KH thực hiện lệnh Tất toán tiền gửi trực tuyến

 | 
Pre-Condition:
 | 
1/ KH đăng nhập thành công vào hệ thống Mobile banking

2/ KH có Tài khoản nguồn hợp lệ để thực hiện chức năng này 

3/ KH đang có ít nhất một tài khoản tiết kiệm thuộc loại tiền gửi tiết kiệm trực tuyến chưa tất toán và trạng thái tài khoản là hoạt động, số tiền không bị phong tỏa

 | Post-Condition: | 
1/ KH thực hiện  tất toán tiền gửi trực tuyến thành công

2/ Tài khoản thanh toán được cộng số tiền tương ứng với số tiền tất toán

 | Basic Flow: | 
1/ KH đăng nhập ứng dụng

2/ KH chọn chức năng "Tiết kiệm" và thực hiện chọn chức năng  "Tất toán tiền gửi trực tuyến"

3/ KH nhập/chọn thông tin

+ Chọn Tiền gửi trực tuyến 

+ Chọn tài khoản nhận gốc lãi

4/ KH thực hiện khởi tạo giao dịch

5/ KH thực hiện xác nhận giao dịch

6/ KH thực hiện xác thực giao dịch 

7/ Hệ thống MB/Bank xác thực giao dịch, hạch toán và trả kết quả tất toán tài khoản tiết kiệm thành công

 | Alternative Flow: | 
1/ KH đăng nhập ứng dụng

2/ KH chọn chức năng "Tiết kiệm" và thực hiện chọn chức năng  "Danh sách tiền gửi "

3/ KH chọn tài khoản xem chi tiết 

4/ KH chọn chức năng "Tất toán tiền gửi trực tuyến"

5/ KH nhập/chọn thông tin

+ Chọn Tiền gửi trực tuyến 

+ Chọn tài khoản nhận gốc lãi

6/ KH thực hiện khởi tạo giao dịch

7/ KH thực hiện xác nhận giao dịch 

8/ KH thực hiện xác thực giao dịch 

9/ Hệ thống MB/Bank xác thực giao dịch, hạch toán và trả kết quả tất toán tài khoản tiết kiệm thành công

 | Exception Flow: | 
1/ Lấy danh sách tài khoản tiền gửi trực tuyến không thành công

2/ KH thực hiện hủy yêu cầu khởi tạo giao dịch

3/ KH thực hiện khởi tạo giao dịch không thành công

4/ KH thực hiện hủy xác thực giao dịch 

5/ KH thực hiện xác thực giao dịch không thành công

6/ Tất toán tiền gửi trực tuyến không thành công

 | Bussiness Rules: | 

 | Non-Funtional Requiremnt: | 

 | Config: | 
Không có

 | Database Table of Backend: | 
Các bảng trên Backend có lưu trữ dữ liệu tra cứu liên quan tới chức năng này.

1. Bảng Báo cáo [ Chi tiết giao dịch]: Ghi nhận chi tiết giao dịch tất toán tiền gửi trực tuyến

2. Bảng [Lịch sử giao dịch]: Ghi nhận lịch sử giao dịch tất toán tiền gửi trực tuyến

### 2/ Luồng sơ đồ

#### Sơ đồ

trueUntitled Diagramfalseautotoptrue213313

#### Danh sách API
 | 
 | Tên API | Luồng gọi API | Input | Output | Ghi chú
 | Truy cập chức năng và trước khi khởi tạo
 | 1 | Lấy danh sách tiền gửi cho phép tất toán trực tuyến (queryTDAccSum) | App Client - MB Server - GW Bank, Core Bank | 

 | 

 | 

 | Khởi tạo giao dịch
 | 1 | Thông tin chi tiết 1 tài khoản tiết kiệm (queryTDAcc) | App Clien- MB Server - GW Bank, Core Bank | 
 | 
 | 

 | 2 | Lấy danh sách tài khoản thanh toán | App Client -MB Server - GW Bank, Core Bank | 
 | 
 | 

 | 3 | Gửi yêu cầu khởi tạo giao dịch | App Client -MB Server | 
 | 
 | 

 | 4 | Kiểm tra chạy batch tại Bank (queryEODstat) | MB Server - GW Bank, Core Bank | 

Xem chi tiết
"systemID":
"requestId"

 | 

Xem chi tiết
"eodStat": Trang thái chạy batch

 | 

 | Xác nhận giao dịch
 | 1 | 
Gửi yêu cầu xác thực giao dịch
 | App Client -MB Server | 
 | 
 | 

 | Xác thực giao dịch
 | 1 | Tất toán tiền gửi trực tuyến ( closeTDAcc) | 
MB Server - GW Bank, Core Bank
 | 

Xem chi tiết
"systemID"
"accountNo"
"productCode"
"reciprocalAccoununt"

 | 

Xem chi tiết
"transRefNo": Mã giao dịch
"accountNo": Tài khoản tiền gửi trực tuyến
"amount ": Tổng số tiền

 | 

### 3/ Luồng màn hình

#### Danh sách màn hình

MH0: Tiền gửi trực tuyến 

 MH1.1: Danh sách Tất toán tiền gửi trực tuyến 

MH1.2: Danh sách Tất toán tiền gửi trực tuyến - Sắp xếp

MH2.1: <Khởi tạo> TH2: Danh sách tiền gửi → Tất toán tiền gửi trực tuyến

MH2.2: <Khởi tạo> Sau khi chọn TKTGTT, hiển thị thông tin 

MH3.1: <Xác nhận giao dịch>TH: Không hiển thị trường Số tiền lãi đã lĩnh và Số tiền lãi thu hồi

MH3.2: <Xác nhận giao dịch >TH: Hiển thị trường Số tiền lãi đã lĩnh và Số tiền lãi thu hồi

MH4: <Xác thực giao dịch>SMS OTP

MH5: <Kết quả giao dịch >

#### Mô tả màn hình

##### MH0: Tiền gửi tiết kiệm
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

 | 1 | Mở tiền gửi trực tuyến | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình Mở tiền gửi trực tuyến
 | 2 | Tất toán tiền gửi trực tuyến | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình Tất toán tiền gửi trực tuyến
 | 3 | Danh sách tiền gửi | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình Danh sách tiền gửi
 | 4 | Rút gốc một phần | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn chọn sẽ vào màn hình Rút gốc một phần

##### MH1: Danh sách Tất toán tiền gửi trực tuyến 
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

 | 1 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 2 | Tiêu đề  | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Tất toán tiền gửi trực tuyến 
 | 4 | Tổng số dư gốc | Label | ReadOnly | -- | -- | totalBal
 | 5 | Icon "Sắp xếp" | Label | ReadOnly | -- | -- | 
Hiển thị có từ 3 tài khoản trở lên: Cho phép sắp xếp tài khoản Tiền gửi theo các tiêu chí

- Ngày đến hạn gần nhất 

- Ngày gửi mới nhất 

- Số tiền tăng dần

- Số tiền giảm dần

- Kỳ hạn tăng dần

- Kỳ hạn giảm dần

 | 6 | Ngày hiệu lực | Label | ReadOnly | -- | -- | 
effectiveDate

Ngày hiệu lực được tính :

• Ngày hành chính: Ngày hiệu lực = ngày hiện tại
• Ngày nghỉ, ngày lễ: Ngày hiệu lực = ngày tiếp theo sau ngày nghỉ, ngày lễ
• Ngày nghỉ: Thứ 7, chủ nhật
• Ngày lễ: theo quy định của ngân hàng Nhà nước
 | 7 | Ngày đáo hạn | Label | ReadOnly | -- | -- | 
maturityDate

Ngày đáo hạn được tính là Ngày cuối cùng theo kỳ hạn đã chọn 

 | 8 | Số dư gốc hiện tại | Label | ReadOnly | -- | -- | balance
 | MH1.1: Sắp xếp
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Sắp xếp

 | 2 | 
Icon "X"
 | 
Text
 | 
Click
 | -- | -- | 
• 
Nhấn để đóng popup

• Click chọn 1 tiêu chí sắp xếp, đóng popup thực hiện sắp xếp tiêu chí đã chọn
• Không click chọn tiêu chí sắp xếp nào, đóng popup, Mặc định sắp xếp Ngày đến hạn gần nhất 

 | 3 | Tiêu chí sắp xếp | List | Select | -- | -- | 
Hiện icon khi có từ 3 tài khoản trở lên: Cho phép sắp xếp tài khoản Tất toán theo các tiêu chí

- Ngày đến hạn gần nhất

- Ngày gửi mới nhất 

- Số tiền tăng dần

- Số tiền giảm dần

- Kỳ hạn tăng dần

- Kỳ hạn giảm dần

MH2.1: <Khởi tạo>TH2: Danh sách tiền gửi → Tất toán tiền gửi trực tuyến
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề  | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Tất toán tiền gửi trực tuyến
 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | Tài khoản tiền gửi trực tuyến | Label | ReadOnly | -- | -- | 
Hiển thị tài khoản tiền gửi trực tuyến

Không cho phép chọn tài khoản tiền gửi trực tuyến khác

 | 4 | Số dư gốc hiện tại | Label | ReadOnly | -- | -- | Hiển thị số tiền của tài khoản tiền gửi trực tuyến
 | THÔNG TIN TÀI KHOẢN
 | 5 | Iconthu gọn/ mở rộng | Icon | Click | -- | -- | Nhấn mở rộng thì hiện đầy đủ thông tin tài khoản
 | 4 | Tiêu đề  | Label | ReadOnly | -- | -- | Thông tin tài khoản
 | 5 | Số tài khoản  | Label | ReadOnly | -- | -- | accountNo 
 | 5 | Loại sản phẩm | Label | ReadOnly | -- | -- | productName
 | 6 | Kỳ hạn | Label | ReadOnly | -- | -- | termDesc 
 | 7 | Ngày hiệu lực | Label | ReadOnly | -- | -- | 
effectiveDate

Ngày hiệu lực được tính :

• Ngày hành chính: Ngày hiệu lực = ngày hiện tại
• Ngày nghỉ, ngày lễ: Ngày hiệu lực = ngày tiếp theo sau ngày nghỉ, ngày lễ
• Ngày nghỉ: Thứ 7, chủ nhật
• Ngày lễ: theo quy định của ngân hàng Nhà nước
 | 8 | Ngày đáo hạn | Label | ReadOnly | -- | -- | 
maturityDate

Ngày đáo hạn được tính là Ngày cuối cùng theo kỳ hạn đã chọn 

 | 9 | Lãi suất | Label | ReadOnly | -- | -- | interestRate
 | 10 | Số tiền gốc | Label | ReadOnly | -- | -- | 
balance

Hiển thị số tiền + đơn vị tiền tệ

Hiển thị số tiền bằng chữ (tô màu đỏ)

 | 11 | Lãi cộng dồn  | Label | ReadOnly | -- | -- | accrued_cr
 | 11 | Số tiền lãi đã lĩnh | Label | ReadOnly | -- | -- | 
Hiển thị theo giá trị Bank trả về. (interestReceived)

Số tiền lãi đã trả vào tài khoản của KH

Nếu số tiền bằng 0. Yêu cầu hiển thị ẩn trường này

Đối với sản phẩm lĩnh lãi cuối kỳ thì cũng ẩn trường này

 | 12 | Số tiền lãi thu hồi | Label | ReadOnly | -- | -- | 
Hiển thị theo giá trị Bank trả về. (lai_thu_hoi)

Số lãi đã trả vào tài khoản thanh toán của KH (sử dụng trong trường hợp Sản phẩm lĩnh lãi định kỳ, KH đã được chi trả 1 hoặc 1 vài kỳ sau đó tất toán trước hạn).

Nếu tất toán đúng hạn số tiền lãi thu hồi bằng 0. Yêu cầu hiển thị ẩn trường này

Đối với sản phẩm lĩnh lãi cuối kỳ thì cũng ẩn trường này

 | 13 | Số tiền lãi thực hưởng | Label | ReadOnly | -- | -- | 
Hiển thị theo giá trị Bank trả về. (lai_thuc_huong)

- Nếu tất toán trước hạn: là số tiền lãi khách hàng thực hưởng  với lãi suất không kỳ hạn từ ngày hiệu lực đến ngày tất toán
- Nếu tất toán đúng hạn: là số lãi của kỳ lĩnh lãi cuối 
 | 14 | Tổng số tiền | Label | ReadOnly | -- | -- | 
Hiển thị theo giá trị Bank trả về.(txnamount)

Công thức tính Tổng số tiền phụ thuộc vào Loại sản phẩm:

• Sản phẩm lĩnh lãi cuối kỳ: Tổng số tiền = Số tiền gốc + Số tiền lãi thực hưởng
• Sản phẩm lĩnh lãi định kỳ:Tổng số tiền = Số tiền gốc + Số tiền lãi thực hưởng – Số tiền lãi thu hồi
 | 15 | Tiêu đề | Label | ReadOnly | -- | -- | Thông tin giao dịch 
 | 16 | Tài khoản nhận gốc lãi | Combobox | List | -- | -- | 
Cho phép chọn 1 giá trị trong danh sách

Cho phép chọn lại tài khoản khác trong danh sách Tài khoản thanh toán của KH

Giá trị mặc định: Tài khoản mặc định của KH tại thời điểm tất toán 

Click vào mở ra màn hình popup chọn tài khoản (Định dạng: số tài khoản )

 | 17 | Tiếp tục  | Button | Click | -- | -- | <Tham khảo logic xử lý>

MH2.2: <Khởi tạo>Sau khi chọn TKTGTT, hiển thị thông tin 
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề  | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Tất toán tiền gửi trực tuyến
 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình danh sách tài khoản tiền gửi trực tuyến (MH1)

 | 3 | Tài khoản tiền gửi trực tuyến | Combobox | List | Yes | -- | 
• Mặc định: Tài khoản chọn từ danh sách tài khoản tiền gửi trực tuyến
• Chỉ hiển thị danh sách tài khoản tiền gửi trực tuyến
• Cho phép chọn tài khoản tiền gửi trực tuyến khác ( Nhấn icon Back để chọn lại)
 | THÔNG TIN TÀI KHOẢN
 | 5 | Iconthu gọn/ mở rộng | Icon | Click | -- | -- | Nhấn mở rộng thì hiện đầy đủ thông tin tài khoản
 | 4 | Tiêu đề  | Label | ReadOnly | -- | -- | Thông tin tài khoản
 | 5 | Số tài khoản  | Label | ReadOnly | -- | -- | accountNo 
 | 5 | Loại sản phẩm | Label | ReadOnly | -- | -- | productName
 | 6 | Kỳ hạn | Label | ReadOnly | -- | -- | termDesc
 | 7 | Ngày hiệu lực | Label | ReadOnly | -- | -- | 
effectiveDate

Ngày hiệu lực được tính :

• Ngày hành chính: Ngày hiệu lực = ngày hiện tại
• Ngày nghỉ, ngày lễ: Ngày hiệu lực = ngày tiếp theo sau ngày nghỉ, ngày lễ
• Ngày nghỉ: Thứ 7, chủ nhật
• Ngày lễ: theo quy định của ngân hàng Nhà nước
 | 8 | Ngày đáo hạn | Label | ReadOnly | -- | -- | 
maturityDate

Ngày đáo hạn được tính là Ngày cuối cùng theo kỳ hạn đã chọn 

 | 9 | Lãi suất | Label | ReadOnly | -- | -- | interestRate
 | 10 | Số tiền gốc | Label | ReadOnly | -- | -- | 
balance

Hiển thị số tiền + đơn vị tiền tệ

Hiển thị số tiền bằng chữ (tô màu đỏ)

 | 11 | Lãi cộng dồn  | Label | ReadOnly | -- | -- | accrued_cr
 | 11 | Số tiền lãi đã lĩnh | Label | ReadOnly | -- | -- | 
Hiển thị theo giá trị Bank trả về. interestReceived

Số tiền lãi đã trả vào tài khoản của KH

Nếu số tiền bằng 0. Yêu cầu hiển thị ẩn trường này

Đối với sản phẩm lĩnh lãi cuối kỳ thì cũng ẩn trường này

 | 12 | Số tiền lãi thu hồi | Label | ReadOnly | -- | -- | 
Hiển thị theo giá trị Bank trả về.

Số lãi đã trả vào tài khoản thanh toán của KH (sử dụng trong trường hợp Sản phẩm lĩnh lãi định kỳ, KH đã được chi trả 1 hoặc 1 vài kỳ sau đó tất toán trước hạn).

Nếu tất toán đúng hạn số tiền lãi thu hồi bằng 0. Yêu cầu hiển thị ẩn trường này

Đối với sản phẩm lĩnh lãi cuối kỳ thì cũng ẩn trường này

 | 13 | Số tiền lãi thực hưởng | Label | ReadOnly | -- | -- | 
Hiển thị theo giá trị Bank trả về.

- Nếu tất toán trước hạn: là số tiền lãi khách hàng thực hưởng  với lãi suất không kỳ hạn từ ngày hiệu lực đến ngày tất toán
- Nếu tất toán đúng hạn: là số lãi của kỳ lĩnh lãi cuối 
 | 14 | Tổng số tiền | Label | ReadOnly | -- | -- | 
Hiển thị theo giá trị Bank trả về. (txnamount)

Công thức tính Tổng số tiền phụ thuộc vào Loại sản phẩm:

• Sản phẩm lĩnh lãi cuối kỳ: Tổng số tiền = Số tiền gốc + Số tiền lãi thực hưởng
• Sản phẩm lĩnh lãi định kỳ:Tổng số tiền = Số tiền gốc + Số tiền lãi thực hưởng – Số tiền lãi thu hồi
 | 15 | Tiêu đề | Label | ReadOnly | -- | -- | THÔNG TIN GIAO DỊCH
 | 16 | Tài khoản nhận gốc lãi | Combobox | List | -- | -- | 
Cho phép chọn 1 giá trị trong danh sách

Cho phép chọn lại tài khoản khác trong danh sách Tài khoản thanh toán của KH

Giá trị mặc định: Tài khoản mặc định của KH tại thời điểm tất toán 

Click vào mở ra màn hình popup chọn tài khoản (Định dạng: số tài khoản )

 | 17 | Tiếp tục  | Button | Click | -- | -- | <Tham khảo logic xử lý>

##### MH3: <Xác nhận giao dịch>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề  | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Tất toán tiền gửi trực tuyến
 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | Tài khoản tiền gửi trực tuyến | Label | ReadOnly | -- | -- | 
accountNo

 | 6 | Loại sản phẩm | Label | ReadOnly | -- | -- | productName
 | 7 | Kỳ hạn | Label | ReadOnly | --

> ⚠️ *Nội dung đã cắt ngắn (27996 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 30.5. URD_Tiết kiệm tích lũy

> **Page ID:** `554567961` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/554567961

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*5 trang con:*

#### 30.5.1. SOW chức năng Tiết kiệm tích lũy

> **Page ID:** `552241186` · **Version:** 20
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/552241186

###  1/ Mục đích & ý nghĩa chức năng

 BRD chức năng Bank cung cấp

### 2/ Ma trận chức năng

#### App mới:
 | 
Cấu hình tại BE (chỉ check với những chức năng có phát sinh GD tài chính
 | Đặc tính sản phẩm
(productType) | Kênh mở (passbook_no) | Trạng thái giao dịch tại quầy (tellerStatus) | Hình thức tích lũy 
(rdType) | Chức năng được thực hiện trên app
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
Mở tại quầy

(passbook_no ≠ Null)

 | 
GD tại quầy 
(tellerStatus=0)

Trường hợp mở tại quầy KH bắt buộc phải giao dịch tại quầy, không có trường hợp tellerStatus = 1)
 | Linh động (rdType = 0) | 

 | Tự động (rdType = 1) | 
1. Thay đổi thông tin tích lũy định kỳ

• Thay đổi trạng thái
 | 
Mở tại app

(passbook_no = Null)

 | 
GD tại quầy 
(tellerStatus=0)
 | Linh động (rdType = 0) | 
1. Thay đổi phương thức tất toán/ rút gốc

2. Gửi gốc thêm

 | Tự động (rdType = 1) | 
1. Thay đổi phương thức tất toán/ rút gốc

2. Thay đổi thông tin tích lũy định kỳ

• Thay đổi trạng thái
• Thay đổi số tiền
• Thay đổi tài khoản trích tiền
 | 
GD tại app
(tellerStatus=1)
 | Linh động (rdType = 0) | 
1. Tất toán tiền gửi

2. Thay đổi phương thức tất toán/ rút gốc

3. Gửi gốc thêm

 | Tự động (rdType = 1) | 
1. Tất toán tiền gửi

2. Thay đổi phương thức tất toán/rút gốc

3. Thay đổi thông tin tích lũy định kỳ

• Thay đổi trạng thái
• Thay đổi số tiền
• Thay đổi tài khoản trích tiền
 | 
Thường

(productType ≠4)
 | 
Mở tại quầy

(passbook_no ≠ Null)
 | 
GD tại quầy 
(tellerStatus=0)
 | -- | 

 | 
Mở tại app

(passbook_no = Null)
 | 
GD tại quầy 
(tellerStatus=0)
 | -- | 
1. Thay đổi phương thức tất toán/ rút gốc

 | 
GD tại app
(tellerStatus=1)
 | -- | 
1. Thay đổi phương thức tất toán/ rút gốc

2. Tất toán tiền gửi

3. Rút gốc 1 phần

### 3/ Phạm vi

#### 3.1/ Phạm vi FrontEnd
 | 
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | Assign | Deadline | Phạm vi tác nhân thực hiện | Link tài liệu
 | 1 | Tiết kiệm tích lũy | 
Mở tài khoản tích lũy
 | 
RedThêm mới
 | MB | 
Dùng chung với Mở tài khoản tiết kiệm thông thường đã có trước đó. Phân biệt bằng loại sản phẩm được khai báo ở BE.

• Tại MH Home: KH chọn chức năng Mở tiết kiệm
• Chọn loại sản phẩm: Tiết kiệm tích lũy
• KH có version app chưa cập nhật cho chức năng Tiết kiệm tích lũy cần update app
• KH chọn Hình thức tích lũy, Chu kỳ tích lũy, Số tiền tích lũy ...
• KH xác thực GD, MB gửi yêu cầu mở TK TKTL sang HT Bank | 

 | 
HongLT
 | 
2/10/2024
 | 
 | 

 | 2 | 
 | 
Thay đổi thông tin tiết kiệm tích lũy
 | 
RedThêm mới
 | MB | 
Cho phép thay đổi:

• Số tiền tích lũy
• Trạng thái trích tích lũy (Tạm dừng/ Hoạt động)
• Tài khoản trích tiền tự động | 

 | 
ThaoCY
 | 
02/10/2024
 | 
 | 

 | 3 | 
 | 
Gửi gốc thêm tiền gửi tích lũy
 | 
RedThêm mới
 | MB | 
Cho phép gửi thêm tiền vào tài khoản tiết kiệm  tích lũy đã được mở trước đó
 | 

 | 
ThaoCY
 | 
02/10/2024
 | 
 | 

 | 4 | 
 | 
Thay đổi phương thức tất toán/ rút gốc
 | 
RedThêm mới
 | MB | 
Chỉ cho phép thay đổi phương thức tất toán/ rút gốc từ Kênh Quầy về kênh Online và ngược lại đối với các tài khoản tiết kiệm thường, tiết kiệm tích lũy mở Online (Tài khoản tiết kiệm mở tại Quầy không cho phép thay đổi phương thức Tất toán/ Rút gốc)
 | 

 | 
ThaoCY
 | 
04/10/2024
 | 
 | 

 | 5 | 
 | 
Tất toán tài khoản tích lũy
 | 
BlueCập nhật
 | MB | 
• Dùng chung với chức năng Tất toán và Rút gốc thông thường. Không phải sửa API. Các trường thông tin hiển thị cho Tiết kiệm tích lũy do Bank trả giống với Tiết kiệm thông thường
• Tuy nhiên chức năng Tất toán + Rút gốc cũ cần cập nhật đầu MB server cần rule lọc tài khoản được phép Tất toán và rút gốc theo kênh được phép giao dịch (Teller Status) như sau:
1- Client truyền vào chức năng cần lấy Danh sách tài khoản tiết kiệm (MID 7) được sử dụng cho chức năng nào:
 | field | description | value
 | cifNo | số cif của kh | 

 | accountType | loại tài khoản | 
T: TK tiết kiệm

 | Subtype | 
• Truyền Subtype tương ứng với chức năng cần lấy | 
SPW: Rút gốc

CTA: Tất toán

SPA: Gửi thêm gốc

2- MB server lọc và trả kết quả DSTK tiết kiệm thỏa mãn theo chức năng:

• App mới: Có truyền Subtype để server thì client không phải lọc nữa nên không cần trả Usefor
• App cũ: Vẫn trả Usefor cho Client tự lọc | 

 | 
--
 | 
--
 | 
 | 

 | 6 | 
 | 
Rút gốc tài khoản tích lũy

(Theo quy định của Bank, sản phẩm tiết kiệm tích lũy không được rút gốc → Cấu hình rule tại BE)

 | 
BlueCập nhật9
 | MB | 

 | 
--
 | 
--
 | 
 | 

 | 7 | Tài khoản | 
• Danh sách tài khoản
• Danh sách tài khoản tiết kiệm | 
BlueCập nhật
 | MB | 
Trong API Getlist → Bank bổ sung type để phân biệt tiết kiệm thường và tiết kiệm tích lũy ( =4 là TK tích lũy, #4 là TK thường)

→ Lưu ý: KH đang dùng App cũ, không xem được tài khoản tích lũy đã mở. Còn KH mở tài khoản tích lũy Online xem được thông tài khoản tích lũy tại MH DS do đã yêu cầu KH update app khi mở tài khoản tích lũy rồi
 | 

 | 
NhungNTH8
 | 
02/10/2024
 | 

 | 

 | 8 | 
 | Xem chi tiết tài khoản tiết kiệm | 
BlueCập nhật
 | 
 | 
MH chi tiết của tài khoản tiết kiệm tích lũy bổ sung:

•  Bổ sung các trường chi tiết tiết kiệm tích lũy
• Thêm các icon chức năng: Thay đổi thông tin tích lũy, Thay đổi phương thức tất toán/ rút gốc ... theo ma trận đã mô tả ở trên | 

 | 
NhungNTH8
 | 
04/10/2024 
 | 

 | 

 | 9 | Báo cáo giao dịch trên App | Xem chi tiết báo cáo giao dịch của TK tích lũy | 
BlueCập nhật
 | 
 | 

 | 

 | 
HongLT
 | 
04/10/2024
 | 

 | 

#### 3.2/ Phạm vi Backend
 | 
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Assign | Deadline | Độ khó | Link tài liệu
 | 1 | Cấu hình | 
Khai báo cấu hình liên quan đến sản phẩm tiết kiệm tích lũy
 | 
BlueCập nhật
 | BE | 
Khai báo cấu hình: 

• Sản phẩm tiết kiệm tích lũy
• Số tiền tối thiểu mỗi lần tích lũy tự động
• Số tiền tối thiểu mỗi lần gửi gốc thêm | 
HongLT
 | 
03/10/2024
 | 

 | 

 | 2 | 
 | 
Chu kỳ tích lũy
 | 
RedThêm mới
 | 
 | 
→ Bank gửi lại API mô tả logic truyền chu kỳ tích lũy
 | 
HongLT
 | 

 | 

 | 

 | 3 | Báo cáo | 
Báo cáo quản lý giao dịch tích lũy
 | 
RedThêm mới
 | BE |  Quản lý các giao dịch liên quan đến :Mở tiền gửi tích lũy trực tuyến/ Gửi gốc thêm | HongLT | 07/10/2024 | 

 | 

 | 4 | 
 | 
Báo cáo quản lý thay đổi thông tin tích lũy định kỳ tự động
 | 
RedThêm mới
 | 
 | 
Quản lý thông tin liên quan đến thay đổi tài khoản tiết kiệm tích lũy của KH như thay đổi:

• Số tiền tích lũy
• Trạng thái trích tích lũy
• Tài khoản trích tiền tự động | 
ThaoCY
 | 
05/10/2024
 | 

 | 

2.4/ Đánh giá ảnh hưởng

App/ Server
 | Hệ thống | Chức năng | Ảnh hưởng
 | App | Mở tiết kiệm | Test thông luồng lại chức năng Mở tiết kiệm với sản phẩm thông thường → do mở tiết kiệm tích lũy dùng chung API gọi sang Bank theo loại sản phẩm mới, và truyền thêm 1 số trường mới trong API
 | Tất toán/ Rút gốc | 
Thay đổi rule lọc tài khoản tiết kiệm được phép Tất toán/ Rút gốc. Nên cần test lại theo rule mới . Chi tiết tại mô tả của chức năng

 | Danh sách Tài khoản/ Chi tiết tài khoản tiết kiệm | 

 | BO | Báo cáo chi tiết Mở tiền gửi | 
Không hiển thị gd mở tiền gửi tích lũy ở báo cái Mở tiền gửi thường

 | Báo cáo chi tiết Tất toán tiền gửi | 
Hiển thị cả giao dịch Tất toán tiền gửi tích lũy, Tất toán tiền gửi thường

 | Báo cáo chi tiết Rút gốc một phần | 
Không hiển thị giao dịch của Rút gốc của tài khoản tiết kiệm tích lũy

#### 2.4/ Phạm vi API Bank cung cấp cung cấp (nếu có)
 | 
 | Tên API | Định nghĩa API | Kênh sử dụng | Input | Output | Ghi chú
 | 1 | Mở tài khoản tiết kiệm tích lũy | 
 | 
 | 

 | 

 | Bank dự kiến bổ sung thêm trường trong API để dùng chung với API mở tài khoản tiết kiệm thường
 | 2 | Danh sách tài khoản tiết kiệm tích lũy | 
 | 
 | 

 | 

 | Bank dự kiến bổ sung thêm trường trong API để dùng chung với API danh sách tài khoản tiết kiệm thường
 | 3 | Xem chi tiết tài khoản tiết kiệm tích lũy | 
 | 
 | 

 | 

 | Bank dự kiến bổ sung thêm trường trong API để dùng chung với API xem chi tiết tài khoản tiết kiệm thường
 | 4 | Tất toán/ Rút gốc Tiết kiệm tích lũy | 
 | 
 | 

 | 

 | 

 | 5 | Thay đổi phương thức tất toán/ rút gốc : Quầy→ Online, Online → Quầy | Bank cấp mới | 
 | 

 | 

 | 

 | 6 | Thay đổi thông tin tích lũy tự động | Bank cấp mới | 
 | 

 | 

 | 

 | 7 | 
Gửi gốc thêm cho loại gửi linh động
 | Bank cấp mới | 
 | 

 | 

 |

---

#### 30.5.2. Gửi gốc thêm

> **Page ID:** `559582166` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/559582166

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

##### 30.5.2.1. Flow& Action screen - Gửi gốc thêm

> **Page ID:** `559582167` · **Version:** 31
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/559582167

Mục lục
none
greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThaoCY | 
 | 
Tạo mới
 | V.1
 | 
 
 | M | ThaoCY | V.1 | 
Bổ sung Lưu ý trong màn hình Khởi tạo Gửi gốc thêm

Cập nhật logic lấy lãi con khi gửi gốc thêm
 | V.1

### 1/ Luồng di chuyển màn hình

true1falseautotoptrue12623

### 2/ Danh sách màn hình

##### MH1: Tiền gửi tiết kiệm

#####  MH1.1: Popup thông báo trường hợp KH không có tài khoản tiền gửi trực tuyến tích lũy linh động

##### MH1.2: Thông tin chi tiết tài khoản tích lũy linh động

##### MH2: Danh sách tài khoản Gửi gốc thêm

##### MH2.1: Sắp xếp

#####  

##### MH3: Khởi tạo Gửi gốc thêm

##### MH4: Xác nhận giao dịch

##### MH5: Xác thực giao dịch

##### MH6: Kết quả giao dịch

### 3/ Mô tả màn hình

##### MH1: Tiền gửi tiết kiệm
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Tiền gửi tiết kiệm
 | 2 | Back | Icon | Click | -- | -- | Nhấn Back, hiển thị màn hình đang thao tác trước đó
 | 3 | Mở tiền gửi trực tuyến  | Icon + Text | Click | -- | -- | Tham chiếu mô tả <MH0, >
 | 4 | Tất toán tiền gửi trực tuyến  | Icon + Text | Click | -- | --
 | 5 | Rút gốc một phần | Icon + Text | Click | -- | --
 | 6 | Danh sách tiền gửi trực tuyến | Icon + Text | Click | -- | --
 | 7 | Gửi gốc thêm tiền gửi tích lũy | Icon + Text | Click | -- | -- | 
Trường hợp 1: Nếu KH không có tài khoản tiền gửi trực tuyến tích lũy linh động nào → hiện popup Thông báo: "Quý khách không có tài khoản tiền gửi trực tuyến hợp lệ để thực hiện chức năng này". Button Đóng

Trường hợp 2: Nếu KH có tài khoản tiền gửi trực tuyến tích lũy linh động → Kiểm tra thời gian chạy batch tại bank → Hiển thị MH2

##### MH1.2: Thông tin chi tiết tài khoản tích lũy linh động

<Tham chiếu >

##### MH2: Danh sách tài khoản gửi gốc thêm
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Gửi gốc thêm tiền gửi tích lũy
 | 2 | Back | Icon | Click | -- | -- | Nhấn Back, hiển thị màn hình đang thao tác trước đó
 | 3 | 
Icon sắp xếp
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Chỉ hiện khi có từ 3 tài khoản trở lên theo từng tab (mô tả bên dưới): Cho phép sắp xếp các tài khoản theo các tiêu chí

- Ngày đến hạn gần nhất (marturityDate )

- Ngày gửi mới nhất (createDt )

- Số tiền tăng dần (availBalance)

- Số tiền giảm dần

- Kỳ hạn tăng dần (tenorInDay)

- Kỳ hạn giảm dần

 | 4 | Ghi chú | Label | ReadOnly | -- | -- | Chọn tài khoản tiền gửi trực tuyến để gửi gốc thêm
 | 5 | Tài khoản tiền gửi trực tuyến tích lũy (số lượng tài khoản) | Label | ReadOnly | -- | -- | 

 | 6 | Tổng số dư gốc | Label | ReadOnly | -- | -- | Hiển thị tổng số dư của tất cả các tài khoản tích lũy linh động trực tuyến, đơn vị là VND
 | 7 | Danh sách tài khoản | 
 | 
 | 
 | 
 | 
Hiển thị các tài khoản tích lũy linh động trực tuyến

Sắp xếp theo thứ tự ngày gửi ban đầu mới nhất lên trước 

Bao gồm:

• Icon tiền gửi online
• Số tài khoản (accountNo)
• Ngày hiệu lực (effectiveDate )
• Ngày đến hạn (maturityDate )
• Số dư gốc hiện tại (balance)
Click vào tài khoản nào thì chuyển sang MH3

##### MH2.1: Sắp xếp
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Sắp xếp

 | 2 | 
Icon "X"
 | 
Text
 | 
Click
 | -- | -- | 
Nhấn để đóng popup

• Click chọn 1 tiêu chí sắp xếp, đóng popup thực hiện sắp xếp tiêu chí đã chọn
• Không click chọn tiêu chí sắp xếp nào, đóng popup, Mặc định sắp xếp Ngày đến hạn gần nhất 
 | 3 | Tiêu chí sắp xếp | List | Select | -- | -- | 
Hiện icon khi có từ 3 tài khoản trở lên: Cho phép sắp xếp tài khoản theo các tiêu chí

- Ngày đến hạn gần nhất (marturityDate )

- Ngày gửi mới nhất (createDt )

- Số tiền tăng dần (availBalance)

- Số tiền giảm dần

- Kỳ hạn tăng dần (tenorInDay)

- Kỳ hạn giảm dần

##### MH3: Khởi tạo Gửi gốc thêm
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Gửi gốc thêm tiền gửi tích lũy
 | 2 | Back | Icon | Click | -- | --  | Click icon Back, quay lại màn hình thao tác trước đó
 | 3 | Tài khoản tiền gửi trực tuyến | 
Label
 | 
Readonly
 | 

 | 

 | 
Icon logo ngân hàng Co-opBank

Hiển thị bao gồm:

• 
Hiển thị tài khoản tiền gửi trực tuyến (accountNo)

• 
Hiển thị số tiền của tài khoản tiền gửi trực tuyến (availBalance)

• 
Định dạng: Số tiền + VND 

• 
Không cho phép chọn tài khoản tiền gửi trực tuyến khác

 | 4 | Tiêu đề | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Thông tin tài khoản
 | 5 | Loại sản phẩm | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị thông tin loại sản phẩm (productName)

 | 6 | Hình thức tích lũy | Label | ReadOnly | -- | -- | 
Hiển thị hình thức tích lũy (rdType)

(0: Linh động, 1: Định kỳ tự động)

 | 7 | Kỳ hạn | Label | ReadOnly | -- | -- | Hiển thị theo thông tin tài khoản (termDesc)
 | 8 | Ngày đáo hạn | Label | ReadOnly | -- | -- | Hiển thị theo thông tin tài khoản (maturityDate)
 | 9 | Thông tin giao dịch | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Thông tin giao dịch
 | 10 | Số tiền gửi thêm | Textbox | Input | x | 15 | 
Chỉ được phép nhập số, không cho nhập số 0 ở đầu, ngăn cách nhau bằng dấu ","

Có số tiền gợi ý theo quy tắc chung 

Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

 | 11 | Số tiền gửi tối thiểu | Label | ReadOnly | -- | -- | 
Hiển thị giá trị khai báo trên BE (minAddPrincipalAmount)

Ẩn nếu giá trị khai báo trên BE = 0

 | 12 | Tài khoản trích tiền | Combobox | Select | x | -- | 
Mặc định hiển thị tài khoản thanh toán mặc định

Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do bank trả về.

Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Hiển thị bao gồm:

• Số tài khoản
• Số dư
 | 13 | Lãi suất | Label | ReadOnly | -- | -- | 
Hiển thị theo thông tin do bank trả về (Rate)

 | 14 | Lưu ý | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Nội dung:

" Lưu ý: Số tiền nộp thêm trong kỳ được áp dụng lãi suất từng lần tính từ ngày gửi gốc đến ngày đến hạn"

 | 15 | Tiếp tục | Button | Click | -- | -- | <tham khảo logic xử lý>

##### MH4: Xác nhận giao dịch
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | --  | Xác nhận giao dịch
 | 2 | Thông báo | Label | ReadOnly | -- | -- | 
Fix tại client

• Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo
 | 3 | Back | icon | click | -- | -- | Click quay về màn hình thao tác trước đó 
 | 4 | Tài khoản tiền gửi trực tuyến | Label | ReadOnly | -- | --  | Hiển thị tài khoản tương ứng
 | 5 | Loại sản phẩm | Label | ReadOnly | -- | --  | 
Hiển thị thông tin loại sản phẩm

 | 6 | Kỳ hạn | Label | ReadOnly | -- | --  | 
Hiển  thị thông tin kỳ hạn

 | 7 | Lãi suất | Label | ReadOnly | -- | --  | Hiển thị thông tin lãi suất
 | 8 | Số tiền gửi thêm | Label | ReadOnly | -- | --  | Hiển thị số tiền gửi thêm
 | 9 | Ngày đáo hạn | Label | ReadOnly | -- | --  | Hiển thị thông tin ngày đáo hạn
 | 10 | Hình thức tích lũy | Label | ReadOnly | -- | --  | Hiển thị hình thức tích lũy
 | 11 | Tài khoản trích tiền | Label | ReadOnly | -- | --  | Hiển thị tài khoản trích tiền
 | 12 | Phương thức xác thực | Combobox | Select | x | -- | 
Bao gồm các giá trị:

• Soft OTP (mặc định chọn)
• FaceID/TouchID (nếu có cài đặt)
• SMS OTP
Cho phép chọn 1 PTXT

Mặc định chọn vào PTXT có thứ tự ưu tiên 1 được trả ra

<Tham khảo Logic kiểm tra chung Hạn mức, PTXT, Phí dịch vụ>

 | 13 | Tiếp tục | Button | Click | -- | -- | <tham khảo logic xử lý>

##### MH5: Xác thực giao dịch

<Hiển thị theo PTXT được chọn>

##### MH6: Kết quả giao dịch
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | icon Home | Icon | Click | -- | -- | Click Quay về màn hình trang chủ
 | 2 | Tiêu đề | Label | ReadOnly | -- | --  | Kết quả giao dịch
 | 3 | Logo | Image | ReadOnly | -- | -- | Logo Co-op Bank
 | 4 | Icon thành công | Icon | ReadOnly | -- | -- | 

 | 5 | Thông báo | Label | ReadOnly | -- | -- | 
Fix tại client:

• Gửi gốc thêm thành công
Hiển thị số tiền gửi gốc bên dưới câu thông báo

 | 6 | Thời gian giao dịch | Label | ReadOnly | -- | -- | Hiển thị thời gian giao dịch
 | 7 | Tài khoản tiền gửi | Label | ReadOnly | -- | -- | desAccountNo
 | 8 | Tài khoản trích tiền | Label | ReadOnly | -- | -- | accountNo
 | 9 | Mã giao dịch | Label | ReadOnly | -- | -- | Hiển thị mã giao dịch (transRefNo)
 | 10 | 
Nút chia sẻ
 | 
Icon
 | 
Click
 | -- | -- | Tham khảo tại Logic xử lý chung
 | 11 | 
 Icon lưu ảnh
 | 
Icon
 | 
Click
 | -- | -- | Tham khảo tại Logic xử lý chung
 | 12 | 
Tạo giao dịch mới
 | 
Button
 | 
Click
 | -- | -- | <Tham khảo logic xử lý>
 | 13 | 
Danh sách tiền gửi
 | 
Button
 | 
Click
 | -- | -- | <Tham khảo logic xử lý>

---

##### 30.5.2.2. User Action Flow - Gửi gốc thêm

> **Page ID:** `565641232` · **Version:** 17
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/565641232

Mục lục
none
greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
  
 | A | ThaoCY | 
 | 
Tạo mới
 | V.1
 | 
 
 | M | ThaoCY | V.1 | 
Bổ sung bước hệ thống MB gọi API truy vấn lãi suất gửi gốc thêm khi chọn tài khoản trích tiền 
 | V.2

### 1/ Mô tả UseCase
 | Use Case Name: | Gửi gốc thêm
 | Use Case ID: | UC_Saving_06
 | Use Case Description: | 
Là người dùng, tôi muốn gửi gốc thêm tiền gửi tích lũy

 | Actor: | 
KH, MB, Bank

 | Priority: | Medium 
 | Trigger: | 
KH thực hiện lệnh Gửi gốc thêm tiền gửi tích lũy

 | 
 | 
1/ KH đăng nhập thành công vào hệ thống Mobile banking

2/ KH thuộc gói dịch vụ được phép sử dụng chức năng này.

3/ KH có tài khoản nguồn hợp lệ để thực hiện chức năng này

4/ KH đã mở ít nhất 1 tài khoản tiền gửi trực tuyến tại NH Co-opBank

 | Post-Condition: | 
1/ KH gửi gốc thêm tiền gửi tích lũy thành công

 | Basic Flow: | 
1/ KH đăng nhập ứng dụng

2/ KH chọn chức năng "Tiền gửi tiết kiệm" và thực hiện chọn chức năng  "Gửi gốc thêm tiền gửi tích lũy"

3/ Hệ thống kiểm tra thời gian chạy Batch tại Bank, hiển thị màn hình danh sách tài khoản

4/ KH chọn 1 tài khoản 

5/ Hệ thống hiển thị màn hình Khởi tạo gửi gốc thêm tiền gửi tích lũy 

6/ KH nhập thông tin giao dịch, chọn 'Tiếp tục"

7/ Hệ thống hiển thị màn hình "Xác nhận giao dịch"

8/ KH chọn PTXT

9/ Hệ thống hiển thị màn hình Xác thực giao dịch 

10/ KH xác thực giao dịch

11/ Hệ thống thông báo xác thực thành công

 | Alternative Flow: | 
Tại màn hình thông tin chi tiết tài khoản trực tuyến tích lũy linh động, chọn icon "Gửi gốc thêm"

 | Exception Flow: | 

 | Bussiness Rules: | 
1/ Chỉ có thể thực hiện Gửi gốc thêm với tài khoản trực tuyến tích lũy, hình thức tích lũy là Tích lũy linh động (không gửi gốc thêm online với sản phẩm tích lũy tại quầy)

2/ Không cho phép gửi gốc thêm trong thời gian chạy batch tại Bank

 | Non-Funtional Requiremnt: | 

### 2/ Luồng sơ đồ

trueUntitled Diagramfalseautotoptrue82110

### 3/ Luồng xử lý

MH1: Tiền gửi tiết kiệm
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn "Gửi gốc thêm tiền gửi tích lũy" tại màn hình Tiền gửi tiết kiệm/ Màn hình Thông tin chi tiết tài khoản tiết kiệm | MB  | Gửi yêu cầu kiểm tra thời gian chạy batch đến Bank qua API: /queryEODStat
 | Bank | Kiểm tra thời điểm chạy batch và phản hồi 
 | MB | 
Nhận kết quả và xử lý

• Không hợp lệ: Tại thời điểm core chạy batch, không cho phép gửi thêm gốc → Trả về thông báo lỗi "Yêu cầu không thực hiện được trong lúc này. Quý khách vui lòng thực hiện lại sau."
• Hợp lệ: Gửi yêu cầu lấy danh sách tài khoản tiết kiệm đến Bank qua API: /queryTDAccSum
 | Bank | 
Nhận yêu cầu và truy vấn lấy danh sách tài khoản tiết kiệm

Trả kết quả về MB

 | MB | 
Nhận kết quả

• Không thành công: Hiển thị thông báo lỗi tương ứng
• Thành công: Lọc và hiển thị danh sách tài khoản có productType=4, passbook_no = Null, rdNextSche=Null
• Nếu không tồn tại tài khoản nào thỏa mãn → Hiển thị thông báo lỗi: "Quý khách không có tài khoản tiền gửi trực tuyến hợp lệ để thực hiện chức năng này"
• Nếu có tồn tại ít nhất 1 tài khoản thỏa mãn → Hiển thị MH2

##### MH2: Danh sách tài khoản Gửi gốc thêm
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Người dùng chọn 1 tài khoản bất kỳ | MB | Gửi yêu cầu lấy thông tin chi tiết tài khoản tiết kiệm đến Bank qua API: queryTDAcc
 | 2 | Bank | Truy vấn thông tin chi tiết của tài khoản và trả kết quả về MB
 | 3 | MB | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng
• Thành công: Hiển thị MH3

##### MH3: Khởi tạo gửi gốc thêm
 | 
 | Tác nhân  | Mô tả
 | Bấm chọn tài khoản trích tiền | MB | Gửi yêu cầu lấy danh sách tài khoản thanh toán đến Bank qua API: /queryCurrentAccSum
 | Bank | 
Nhận yêu cầu và truy vấn lấy danh sách tài khoản thanh toán 

Trả kết quả về MB

 | MB | 
Nhận kết quả:

• Không thành công | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại. | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn "Thử lại" gọi lấy lại danh sách tài khoản

• Thành công: Hiển thị popup chọn Tài khoản gồm danh sách các tài khoản do bank trả về, hiển thị bao gồm
• Số tài khoản
• Số dư
 | Chọn 1 tài khoản trích tiền | MB | 
Đóng popup

Fill thông tin vào ô tài khoản trích tiền, bao gồm:

• Số tài khoản
Lưu ý: Chỉ được phép chọn 1 tài khoản

Gửi yêu cầu truy vấn lãi suất đến Bank qua API queryRdRateByAccount

 | Bank | 
Truy vấn lãi suất và trả về MB

 | MB | 
Nhận kết quả

• Không thành công | | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | Không lấy được lãi suất | Không lấy được lãi suất. Quý khách vui lòng thử lại | Hiển thị Button Thử lại trên thông báo. Sau khi nhấn "Thử lại" gọi lấy lại lãi suất

• Thành công: Hiển thị lãi suất
 | Nhấn "Tiếp tục" | MB | 
1/ Kiểm tra thông tin validate tại màn hình khởi tạo

• Không thành công: | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Bỏ trống số tiền gửi thêm | Quý khách vui lòng nhập số tiền gửi thêm | 

• Hợp lệ: chuyển sang 2 (serviceCode=0914)
2/ Kiểm tra số tiền tối thiểu theo loại sản phẩm được cấu hình tại bảng Quản lý sản phẩm tiết kiệm

• Không hợp lệ: Trả về lỗi như logic validate của PTXT | | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Số tiền gửi thêm < Số tiền gửi gốc tối thiểu | Số tiền gửi gốc tối thiểu là x VND. Quý khách vui lòng kiểm tra lại! | 

• Hợp lệ: Chuyển sang 3
3/ Kiểm tra logic Hạn mức/phí/PTXTX/Số dư khả dụng như sau:
 | 
 | Loại hạn mức/phí giao dịch | Yêu cầu
 | 1 | Phương thức xác thực | 
• Nếu dịch vụ không cấu hình kiểm tra hạn mức theo QĐ 2345 thì kiểm tra theo QĐ 630, tham khảo tại tài liệu URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)
• Nếu dịch vụ được cấu hình kiểm tra hạn mức/ptxt theo QĐ 2345, tham khảo tại tài liệu Logic kiểm tra hạn mức và xác thực giao dịch theo QĐ 2345
 | 2 | Hạn mức theo nhóm dịch vụ 630/ngày | Không kiểm tra/ Không cộng dồn vào hạn mức ngày
 | 3 | Phí giao dịch | Không kiểm tra
 | 4 | Hạn mức theo nhóm chuyển tiền/ngày (Cài đặt trên App) | Không kiểm tra/ Không cộng dồn vào hạn mức ngày
 | 5 | Hạn mức về số lần giao dịch/ngày | Không kiểm tra/ Không cộng dồn vào hạn mức ngày
 | 6 | Hạn mức tối đa/Giao dịch | Không kiểm tra
 | 7 | Hạn mức tối thiểu/ Giao dịch | Không kiểm tra (Kiểm tra theo số tiền tối thiểu tại bảng Quản lý sản phẩm)
 | 8 | Số dư khả dụng | Có kiểm tra

• Không hợp lệ: Trả về lỗi như logic validate của PTXT
• Hợp lệ: Khởi tạo giao dịch, ghi nhận giao dịch ở phase khởi tạo, hiển thị MH4

##### MH4: Xác nhận giao dịch
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Nhấn back | MB | Hiển thị màn hình khởi tạo giao dịch với các thông tin trước đó
 | 2 | Chọn 1 PTXT và nhấn Tiếp tục | MB | 
1/Gửi yêu cầu xác thực theo các phương thức xác thực

• Nếu PTXT là Soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)
• Nếu PTXT là SMS OTP → Gửi yêu cầu xác thực là SMS OTP  (Nội dung SMS OTP (Co-opBank) là " QK KHONG GUI OTP cho bat ky ai. Ma OTP xac thuc GD so tien {tổng số tiền} VND la {mã OTP}, co hieu luc trong {n} phut." sẽ được gửi số điện thoại KH đăng kí dịch vụ )→ Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)
• Nếu PTXT là FaceID/TouchID → Gửi yêu cầu xác thực giao dịch (Tham khảo logic xử lý tại Xác thực bằng Touch ID/Face ID)
2/ Xử lý và trả kết quả xác nhận giao dịch theo PTXT tương ứng. Ghi nhận giao dịch ở trạng thái "Chờ xác thực"

3/ Hiển thị màn hình xác thực giao dịch

##### MH5: Xác thực giao dịch

<Tham khảo URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)>
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Thực hiện xác thực theo PTXT tương ứng | MB | 
1/ Xử lý thông tin validate (nếu có)

2/ Xử lý xác thực giao dịch theo PTXT Tham khảo URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2))

3/ Gửi yêu cầu hạch toán sang Bank qua API: createTDPayin

 | 2 | Bank | 
Xử lý hạch toán và trả kết quả về MB

Lưu ý: Bank trả thêm thông tin về số dư của của tài khoản tiết kiệm trong respone của API createTDPayin

 | 3 | MB | 
Nhận kết quả từ Bank và trả về clinet

• Không thành công: Cập nhật trạng thái giao dịch phase trừ tiền là False và hiển thị thông báo lỗi 
• Thành công: Cập nhật trạng trạng thái giao dịch phase trừ tiền là Success và hiển thị MH6

##### MH6: Kết quả
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Nhấn chọn "Tạo giao dịch mới" | MB | 
Gọi API Lấy danh sách tài khoản tiết kiệm, lọc theo điều kiện sản phẩm trực tuyến tích lũy linh động

→ Điều hướng về màn hình Danh sách tài khoản Gửi gốc thêm

 | 2 | Danh sách tiền gửi | MB | 
Gọi API Lấy danh sách tiền gửi → Điều hướng về màn hình Danh sách tiền gửi

 | 3 | Chọn "Chia sẻ" | MB | Tham khảo tại Logic xử lý chung
 | 4 | Chọn "Lưu ảnh" | MB | Tham khảo tại Logic xử lý chung

---

#### 30.5.3. Mở tài khoản tiền gửi tích lũy

> **Page ID:** `564824877` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/564824877

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

##### 30.5.3.1. Flow& Action screen- TK tích lũy

> **Page ID:** `564035797` · **Version:** 11
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/564035797

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | Hong LT | 
 | 
Chức năng Mở tài khoản tiết kiệm tích lũy được xây dựng dựa trên chức năng gốc là Mở tài khoản tiết kiệm thường 
 | 

Mục lục

### 1/ Tóm tắt Use Case
 | Use Case Name: | Mở tiền gửi tích lũy trực tuyến (Kênh Online)
 | Use Case ID: | UC_Open Account Saving_02
 | Use Case Description: | 
• Hiện tại Bank có 2 kênh mở tiết kiệm tích lũy là Kênh Quầy và Kênh Online
• Phạm vi Online: Cho phép KH mở tiết kiệm tích lũy trên kênh Mobile Banking
 | Actor: | 
KH, App Client, MB Server, GW Bank, Core Bank. 

 | Priority: | Medium 
 | Trigger: | 
KH thực hiện lệnh mở tiền gửi tích lũy trực tuyến 

 | 
Pre-Condition:
 | 
1/ KH đăng nhập thành công vào hệ thống Mobile banking

2/ KH thuộc gói dịch vụ được phép sử dụng chức năng này.

3/ KH có tài khoản nguồn hợp lệ để thực hiện chức năng này

4/ KH có Tài khoản thanh toán đủ số dư cho phép mở tài khoản tiết kiệm

 | Post-Condition: | 
1/ KH thực hiện mở tài khoản tiết kiệm thành công

2/ Tài khoản thanh toán bị trừ số tiền tương ứng với số tiền mở sổ

 | Basic Flow: | 
1/ KH đăng nhập ứng dụng

2/ KH chọn chức năng "Tiết kiệm" và thực hiện chọn chức năng  "Mở tiền gửi trực tuyến" (Theo luồng hiện tại )

3/ KH chọn sản phẩm "Tiết kiệm tích lũy ..."

4/ KH nhập/chọn thông tin

5/ KH thực hiện khởi tạo giao dịch

6/ KH thực hiện xác nhận giao dịch

7/ KH thực hiện xác thực giao dịch 

8/ Hệ thống MB/Bank xác thực giao dịch, hạch toán và trả kết quả mở tài khoản tiết kiệm thành công

 | Alternative Flow: | 
1/ KH đăng nhập ứng dụng

2/ KH chọn chức năng "Tiết kiệm" và thực hiện chọn chức năng  "Danh sách tiền gửi"

3/ KH chọn tài khoản xem chi tiết 

4/ KH chọn chức năng "Mở tiền gửi trực tuyến" → Tiếp tục luồng như đã mô tả ở Basic Flow

 | Exception Flow: | 
1/ Lấy danh sách tài khoản nguồn không thành công

2/ KH thực hiện hủy yêu cầu khởi tạo giao dịch

3/ KH thực hiện khởi tạo giao dịch không thành công

4/ KH thực hiện hủy xác thực giao dịch 

5/ KH thực hiện xác thực giao dịch không thành công

6/ Mở tiền gửi trực tuyến không thành công

 | Bussiness Rules: | 

 | Non-Funtional Requiremnt: | 
Nhập các yêu cầu về phi tài chính liên quan tới usecase. Ví dụ: NFR-1: Thời gian hiệu lực xác thực giao dịch là 120 giây.

 | Config: | 
 Không có

 | Database Table of Backend: | 
Tham khảo 

### 1/Chi tiết thao tác chọn mở tài khoản tiết kiệm

### 

### 2/ Luồng màn hình

#### Danh sách màn hình

##### MH: Truy cập chức năng - Thông báo yêu cầu Update App khi KH chọn Loại sản phẩm (Mục đích để App cũ có thể update lên version Mở tiết kiệm có sản phẩm Tích lũy)

##### MH: < Khởi tạo 1> Sau khi chọn loại sản phẩm, kỳ hạn

#####  Popup chọn phương thức tất toán/ rút gốc (mặc định = Online)

##### Popup chọn Hình thức tích lũy

##### MH: < Khởi tạo 2> Sau khi chọn hình thức tích lũy

#####  Popup chọn Chu kỳ tích lũy với hình thức tích lũy = Tích lũy định kỳ tự động

##### Popup chọn Tài khoản trích tiền với hình thức tích lũy = Tích lũy định kỳ tự động

##### MH Khởi tạo sau khi đã chọn đầy đủ thông tin

 

##### MH Khởi tạo sau khi đã chọn đầy đủ thông tin

MH Xác nhận

MH Xác thực

MH Kết quả

### Mô tả màn hình

##### MH: <Truy cập chức năng- Tiền gửi trực tuyến > 

Tham khảo mô tả tại 

##### MH <Khởi tạo >
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề  | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Mở tiền gửi trực tuyến
 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | Yes | -- | 
Tham khảo mô tả tại 

 | Thông tin mở tiền gửi
 | 1 | Loại sản phẩm | Combobox  | List | Yes | -- | 
Tham khảo mô tả tại 

Sau khi gọi lấy danh sách loại sản phẩm, MB sẽ check version app theo tham số OPEN_SAVING_FORCE_VERSION để yêu cầu KH cập nhật app mới nhất
 | Lưu ý: 
• Để mở tài khoản tiền gửi trực tuyến tích lũy, khách hàng vẫn sử dụng màn hình Mở tiền gửi trực tuyến hiện tại (bổ sung thêm sản phẩm Tiền gửi trực tuyến tích lũy)
• BE sẽ cấu hình thêm loại sản phẩm = Tiền gửi trực tuyến tích lũy và đánh dấu cờ = Là sản phẩm tiết kiệm tích lũy để phân biệt sản phẩm tiết kiệm thường và sản phẩm tiết kiệm tích lũy
( Sản phẩm này cũng sẽ được quy định tại CoreBank để khi chọn Loại sản phẩm = Tiền gửi trực tuyến tích lũy , khi gọi sang Bank truy vấn sẽ trả ra Kỳ hạn, Lãi suất, Ngày hiệu lực, Ngày đáo hạn tương ứng)

 | 2 | Kỳ hạn | Combobox | 
List
 | Yes | -- | 
Do Bank trả. Hiển thị danh sách kỳ hạn và lãi suất tương ứng với loại sản phẩm

Tham khảo mô tả tại 

 | 3 | Lãi suất | Label | ReadOnly | -- | -- | 
Do Bank trả. Hiển thị danh sách kỳ hạn và lãi suất tương ứng với loại sản phẩm 

Tham khảo mô tả tại 

 | 4 | Ngày hiệu lực | Label | ReadOnly | -- | -- | 
Do Bank trả. Hiển thị danh sách kỳ hạn và lãi suất tương ứng với loại sản phẩm 

Tham khảo mô tả tại 

 | 5 | Ngày đáo hạn  | Label | ReadOnly | -- | -- | 
Do Bank trả. Hiển thị danh sách kỳ hạn và lãi suất tương ứng với loại sản phẩm 

Tham khảo mô tả tại 

 | 6 | Số tiền gửi | 
Textbox
 | 
Number
 | Yes | 15 | 
Tham khảo mô tả tại 

 | 7 | Hình thức tích lũy | Combobox | 
List
 | Yes | -- | 
Mặc định trống. 

Chỉ hiển thị sau khi đã chọn Kỳ hạn và Loại sản phẩm được gắn cờ Tiết kiệm tích lũy

Cho phép chọn 1 trong 2 giá trị:

• Tích lũy định kỳ tự động: Nếu KH chọn hình thức này → Hiển thị các trường Chu kỳ tích lũy, Số tiền tích lũy định kỳ, Tài khoản trích tiền
• Tích lũy linh động: Nếu KH chọn hình thức này → Không hiển thị các trường  trên
 | 8 | Chu kỳ tích lũy | Combobox | 
List
 | Yes | -- | 
Mặc định trống

Chỉ hiển thị nếu chọn hình thức tích lũy tự động

Giá trị chu kỳ tích lũy được cấu hình tại , dữ liệu trả về dạng xD, xM, xQ, xY. Hiển thị như sau:

• xD → Hiển thị = x ngày/lần (nếu dữ liệu trả về có Mô tả thì lấy theo mô tả, ví dụ trả chu kỳ = 1D, nhưng mô tả = "Hằng ngày" thì hiển thị là Hằng ngày
• xM → Hiển thị = x tháng/lần (nếu dữ liệu trả về có Mô tả thì lấy theo mô tả, ví dụ trả chu kỳ = 1M, nhưng mô tả = "Hằng tháng" thì hiển thị là Hằng tháng
• xQ → Hiển thị= x quý/ lần (nếu dữ liệu trả về có Mô tả thì lấy theo mô tả, ví dụ trả chu kỳ = 1Q, nhưng mô tả = "Hằng quý" thì hiển thị là Hằng quý
• xY → Hiển thị= x năm/ lần (nếu dữ liệu trả về có Mô tả thì lấy theo mô tả, ví dụ trả chu kỳ = 1Y, nhưng mô tả = "Hằng năm" thì hiển thị là Hằng năm)
 | 9 | Số tiền tích lũy đinh kỳ | Combobox | 
List
 | Yes | -- | 
• Mặc định trống
• Chỉ hiển thị nếu chọn hình thức tích lũy tự động
• Chặn nhập: 0 và dấu cách
• Hiển thị đơn vị tiền tệ của Số tiền mặc định “VND”
• Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
• Focus textbox sẽ không ẩn trường số tiền gửi tối thiểu và hiển thị bàn phím số cho KH nhập
• Gợi ý số tiền chuyển theo quy tắc: <Tham khảo quy tắc gợi ý chung trong BẢNG MÃ LỖI CHUNG>
• Hiển thị label ngay dưới trường "Số tiền tích lũy định kỳ" như sau: 
 Số tiền gửi định kỳ tối thiểu là <x> đồng ( với x là giá trị số tiền gửi tối thiểu theo cấu hình tại BE bảng quản lý sản phẩm < > tương ứng với loại sản phẩm chọn 

(Nếu x khai báo = 0 thì ẩn label số tiền tối thiểu)

 | 10 | Lãi dự tính | Text | ReadOnly | -- | -- | 
Tham khảo mô tả tại 

 | 11 | Tài khoản trích tiền | 
Label
 | 
ReadOnly
 | -- | -- | 
• Chỉ hiển thị nếu chọn hình thức tích lũy tự động
• Mặc định là Tài khoản nguồn. 
• Khi bấm vào thì hiện ra danh sách các TKTT của khách hàng, dữ liệu do Bank trả
Tham khảo mô tả tại 

 | 12 | Phương thức đáo hạn | 
Combobox
 | 
List
 | Yes | -- | 
Mặc định trống

Hiển thị danh sách theo cấu hình tại BE bảng quản lý phương thức đáo hạn với trạng thái bản ghi là Hoạt động <>

Thông tin khai báo trên BE như sau:
 | Sản phẩm | Mã phương thức đáo hạn | Phương thức đáo hạn
 | Tiền gửi tích lũy | 0 | Chuyển gốc và lãi sang kỳ hạn mới
 | 1 | Gốc sang kỳ hạn mới, nhận lãi về TKTT
 | 2 | Tự động tất toán, nhận gốc và lãi về TKTT

 | 13 | Phương thức tất toán/ rút gốc | 
Combobox
 | 
List
 | Yes | -- | 
• Bao gồm 2 giá trị:
- Tất toán, rút gốc Online (Mặc định)

- Tất toán, rút gốc tại Quầy

Cho phép chọn 1 giá trị

 | 14 | Tài khoản nhận gốc lãi  | 
Label
 | 
ReadOnly
 | -- | -- | 
• Mặc định là Tài khoản nguồn. 
• Khi bấm vào thì hiện ra danh sách các TKTT của khách hàng, dữ liệu do Bank trả
Tham khảo mô tả tại 

 | 14 | Mã giới thiệu  | Textbox | Number | -- | 11 | 
Tham khảo mô tả tại 

 | 15 | Lưu ý | 
Label
 | 
ReadOnly
 | -- | -- | 
Text Lưu ý fix tại Client

Hiển thị sau khi chọn Hình thức tích lũy = Linh động

Lãi suất áp dụng đối với số tiền gốc gửi khi mở tài khoản: Là lãi suất của kỳ hạn gốc (Kỳ hạn do khách hàng lựa chọn khi mở tài khoản tiền gửi tích lũy)
Lãi suất áp dụng đối với số tiền gửi gốc định kỳ/linh hoạt trong kỳ: Là lãi suất của từng lần nộp thêm tiền trong kỳ (lãi suất từng lần tính từ ngày gửi gốc đến ngày đến hạn)

Cho phép Mở rộng/ Thu gọn câu lưu ý

 | 16 | Icon Danh bạ (Để chọn mã giới thiệu) | Icon  | Click  | -- | -- | Tham khảo mô tả tại 
 | 17 | Điều khoản & Điều kiện | Checkbox | Click | Yes | -- | 
Tham khảo mô tả tại 

 | 168 | Tiếp tục | Button | 
Click
 | -- | -- | <Tham khảo logic xử lý>

##### MH : <Xác nhận giao dịch >
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Icon Back | 
Icon
 | 
Click
 | 
--
 | 
--
 | Nhấn Back, hiển thị màn hình đang thao tác trước đó
 | 2 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Xác nhận giao dịch

 | 3 | Câu thông báo | Label | ReadOnly | -- | -- | Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo
 | 4 | 
Tài khoản nguồn
 | 
Label
 | 
ReadOnly
 | -- | -- | 
debitAccount

 | 5 | Loại sản phẩm | Label | ReadOnly | -- | -- | 
accountClassDesc

 | 6 | Kỳ hạn | Label | 
ReadOnly
 | -- | -- | 
term

 | 7 | Lãi suất | Label | ReadOnly | -- | -- | rate
 | 8 | Số tiền gửi | 
Label
 | 
ReadOnly
 | -- | --- | 
amount

 | 9 | Ngày hiệu lực | Label | ReadOnly | -- | -- | 
effectiveDate ( dd/mm/yyyy )

 | 10 | Ngày đáo hạn  | Label | ReadOnly | -- | -- | 
maturityDate (dd/mm/yyyy )

 | 11 | Lãi dự tính | Label | ReadOnly | -- | -- | 
Số tiền lãi dự tính- VND

 | 12 | Hình thức tích lũy | Label | ReadOnly | -- | -- | 
Hiển thị hình thước tích lũy tương ứng KH đã chọn ( Chỉ hiển thị khi loại sản phẩm là tiết kiệm tích lũy)

 | 13 | Số tiền tích lũy định kỳ | Label | ReadOnly | -- | -- | 
Chỉ hiển thị hình thức tích lũy = Tích lũy định kỳ tự động

 | 14 | Chu kỳ tích lũy | Label | ReadOnly | -- | -- | 
Chỉ hiển thị hình thức tích lũy = Tích lũy định kỳ tự động

 | 15 | Tài khoản trích tiền | Label | ReadOnly | -- | -- | 
Chỉ hiển thị hình thức tích lũy = Tích lũy định kỳ tự động (rdPaymentAcount)

 | 16 | Phương thức tất toán/ rút gốc | Label | ReadOnly | -- | -- | 
Hiển thị phương thức tất toán/ rút gốc tương ứng KH đã chọn

 | 17 | Phương thức đáo hạn | 
Label
 | 
ReadOnly
 | -- | -- | 
setType

 | 18 | Tài khoản nhận gốc lãi | Label | ReadOnly | -- | -- | 
reciprocalAccount

 | 19 | Phương thức xác thực | Combobox | Select | Yes | -- | 
Nếu dịch vụ không cấu hình kiểm tra hạn mức theo QĐ 2345 thì kiểm tra theo QD 630, thì tham khải tại tài liệu <Tham khảo  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)> 

Nếu dịch vụ được cấu hình kiểm tra hạn mức/ptxt theo QĐ 2345 thì tham khảo tại tài liệu 

 | 20 | Tiếp tục | Button | 
Click
 | -- | -- | 
Mặc định Enable

<Tham khảo logic xử lý>

##### MH : <Xác thực giao dịch>

Tham khảo URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2) và 

##### MH : <Kết quả giao dịch>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Icon Home | 
Icon
 | 
Click
 | 
--
 | 
--
 | Quay trở lại màn hình trang chủ
 | 2 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Kết quả giao dịch

 | 3 | Logo Bank  | Label | ReadOnly | -- | -- | Hiển thị Logo Co-opBank
 | 4 | 
Icon thành công
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị icon giao dịch thành công

 | 5 | Tiêu đề | Label | ReadOnly | -- | -- | 
Mở tiền gửi trực tuyến thành công

 | 6 | Số tiền gửi | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị Số tiền- VND

 | 7 | Thời gian giao dịch | Label | ReadOnly | -- | -- | 
Hiển thị theo định dạng dd/mm/yyyy hh:mm

 | 8 | Tài khoản tiền gửi | Label | ReadOnly | -- | -- | 
Hiển thị số tài khoản tiền gửi bank trả

 | 9 | Chu kỳ tích lũy | Label | ReadOnly | -- | -- | 
Chỉ hiển thị nếu hình thức tích lũy  là tích lũy định kỳ tự động

 | 10 | Số tiền tích lũy định kỳ | Label | ReadOnly | -- | -- | 
Chỉ hiển thị nếu hình thức tích lũy  là tích lũy định kỳ tự động

 | 11 | Chi nhánh/PGD mở | Label | ReadOnly | -- | -- | 
Chi nhánh/PGD  mà KH chọn tài khoản nguồn khi Mở tiền gửi trực tuyến

 | 12 | Mã giao dịch | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị thông tin mã giao dịch do Bank trả

 | 13 | Giấy xác nhận  | 
Button
 | 
Click
 | -- | -- | 
Tham khảo mô tả tại 

 | 14 | Tạo giao dịch mới | Button | Click | -- | -- | 
Trở lại màn hình khởi tạo giao dịch ban đầu

 | 15 | 
Nhấn Icon lưu ảnh
 | 
Button
 | 
Click
 | -- | -- | Tham khảo tại Logic xử lý chung
 | 16 | 
Nhấn Nút chia sẻ
 | 
Button
 | 
Click
 | -- | -- | Tham khảo tại Logic xử lý chung

##### MH : <Giấy xác nhận> Tham khảo mô tả tại

---

##### 30.5.3.2. User Action Flow_TK tích lũy

> **Page ID:** `564824723` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/564824723

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | Hong LT | 
 | 
Chức năng Mở tài khoản tiết kiệm tích lũy được xây dựng dựa trên chức năng gốc là Mở tài khoản tiết kiệm thường 
 | 

Mục lục

### 1/ Luồng Mở tiết kiệm trực tuyến

Tham khảo tại: 

### 3/ Luồng xử lý

##### MH Truy cập chức năng

##### Có 2 cách để vào chức năng Mở tiền gửi trực tuyến < Giữ nguyên như hiện tại- Tham khảo tại >

##### MH Khởi tạo
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 2

 | Bấm chọn “Loại sản phẩm” | MB | 
1/ Kiểm tra version app

Version yêu cầu forceupdate theo chức năng Mở tiết kiệm được cấu hình tại tham số OPEN_SAVING_FORCE_VERSION

• Nếu version app của KH < version cấu hình tại tham số OPEN_SAVING_FORCE_VERSION (ver hiện tại =1.2.3)→ Trả thông báo force update app "Quý khách vui lòng nâng cấp ứng dụng trước khi tiếp tục sử dụng dịch vụ" và Client có 1 nút Đồng ý điều hướng tải app
• Nếu version app của KH = version cấu hình tại tham số OPEN_SAVING_FORCE_VERSION → Chuyển bước 2: Lấy danh sách loại sản phẩm
2/ Lấy danh sách Loại sản phẩm có đánh dấu sản phẩm tiết kiệm tích lũy được cấu hình tại BE và Phương thức đáo hạn

 | Bấm chọn "Kỳ hạn"

 | MB | 
• Nếu bấm chọn Kỳ hạn mà chưa chọn Loại sản phẩm: Hiển thị popup thông báo " Quý khách vui lòng chọn Loại sản phẩm"
• Nếu đã chọn Loại sản phẩm : Gửi yêu cầu lấy danh sách Kỳ hạn tới HT Bank theo mã sản phẩm KH đã chọn
 | 
HT Bank
 | 
Trả kết quả lấy danh sách kỳ hạn theo sản phẩm bao gồm:

• Kỳ hạn
• Lãi suất theo kỳ hạn
• Ngày hiệu lực
• Ngày đáo hạn
 | 3 | MB | 
Hiển thị Danh sách kỳ hạn, lãi suất, ngày hiệu lực, ngày đáo hạn theo loại sản phẩm tương ứng. 

• Lưu ý: Chọn lại một trong các trường Tài khoản nguồn / Loại sản phẩm sẽ lấy lại giá trị danh sách kỳ hạn, Lãi suất tương ứng với thay đổi.
 | 5 | Nhập số tiền gửi (số tiền ban đầu) | MB | 
Theo quy tắc đã mô tả tại tài liệu mô tả màn hình

Tự động tính lãi dự tính theo công thức = (Ngày đáo hạn – Ngày hiệu lực) * Lãi suất * Số tiền gửi / 365

 |   | Chọn Hình thức tích lũy | MB | 
• Nếu chọn Hình thức tích lũy định kỳ tự động → Hiển thị trường Chu kỳ tích lũy, Số tiền tích lũy định kỳ, Tài khoản trích tiền
• Nếu chọn Hình thức tích lũy linh động → Không hiển thị trường nêu trêu
 |   | Chọn chu kỳ tích lũy | MB | 
Lấy danh sách chu kỳ tích lũy cho Client (Danh sách cấu hình tại BE , chỉ lấy các chu kỳ có trạng thái = Hoạt động)

Hiển thị Danh sách chu kỳ tích lũy theo thứ tự tăng dần

 |   | Nhập số tiền tích lũy định kỳ (với hình thức tích lũy định kỳ tự động) | MB | 
Theo quy tắc đã mô tả tại tài liệu mô tả màn hình

 |   | Chọn Tài khoản trích tiền | MB | 
Theo quy tắc đã mô tả tại tài liệu mô tả màn hình

 |   | Bấm chọn “Phương thức đáo hạn” | MB | Hiển thị list Phương thức đáo hạn tương ứng  Lọc  theo Loại sản phẩm đã chọn
 |   | Chọn tài khoản nhận gốc lãi |  MB | Theo quy tắc đã mô tả tại tài liệu mô tả màn hình
 |   | Chọn 1 “Phương thức đáo hạn” | MB | 
Hiển thị phương thức đáo hạn đã chọn

Kiểm tra Phương thức đáo hạn:

• Chuyển cả  gốc và lãi sang kỳ hạn: Không hiển thị trường Tài khoản nhận gốc lãi
• Phương thức đáo hạn còn lại: Hiển thị trường Tài khoản nhận gốc lãi. Mặc định là tài khoản nguồn
 |   | Chọn phương thức tất toán/ rút gốc | MB | 
Theo quy tắc đã mô tả tại tài liệu mô tả màn hình

 | 9

 | Nhấn "Tiếp tục"

 | MB | 
1/ Kiểm tra thông tin validate tại màn hình khởi tạo:

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng: | TT | Trường hợp lỗi | Nội dung  | Xử lý (nếu có)
 | 1 | Bỏ trống trường bắt buộc | {Trường bắt buộc không được bỏ trống}. Quý khách vui lòng kiểm tra lại! | 

 | 2 | Bỏ trống điều kiện điều khoản | 
Quý khách chưa đồng ý với thỏa thuận mở và sử dụng tiền gửi trực tuyến qua Co-opbank mobile banking
 | 

• Hợp lệ: Khởi tạo giao dịch (theo service mới: Mở tài khoản tiền gửi tích lũy riêng với Mở tài khoản tiết kiệm thường)
2/ Kiểm tra số tiền tối thiểu theo loại sản phẩm được cấu hình tại bảng Quản lý sản phẩm tiết kiệm

• Không hợp lệ:  | TT | Trường hợp lỗi | Nội dung  | Xử lý (nếu có) | Note
 | 1 | 
Số tiền gửi ban đầu < Số tiền tối thiểu
 | 
Số tiền gửi tối thiểu là x VND. Quý khách vui lòng kiểm tra lại!
 | 
 | 

 | 2 | Số tiền gửi định kỳ < Số tiền gửi định kỳ tối thiểu | 
Số tiền gửi  định kỳ tối thiểu là y VND. Quý khách vui lòng kiểm tra lại!
 | 
 | Chỉ xảy ra với Hình thức tích lũy = Tích lũy định kỳ tự động

• Hợp lệ → Chuyển bước  Kiểm tra logic Hạn mức/ phí/PTXT/ Số dư khả dụng
3/ Kiểm tra logic Hạn mức/ phí/PTXT/ Số dư khả dụng như sau
 | | 
STT
 | 
Loại hạn mức/ phí giao dịch
 | 
Yêu cầu

 | 1 | Phương thức xác thực | 
• Nếu dịch vụ không cấu hình kiểm tra hạn mức theo QĐ 2345 thì kiểm tra theo QD 630, thì tham khải tại tài liệu <Tham khảo  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)> 
• Nếu dịch vụ được cấu hình kiểm tra hạn mức/ptxt theo QĐ 2345 thì tham khảo tại tài liệu Logic kiểm tra hạn mức và xác thực giao dịch theo QĐ 2345
• Đối với Hình thức tích lũy = Tích lũy định kỳ tự động, có 2 trường Số tiền là: Số tiền gửi ban đầu và Số tiền gửi định kỳ thì chỉ kiểm tra hạn mức/ PTXT theo trường Số tiền gửi ban đầu
 | 2 | Hạn mức theo nhóm dịch vụ 630/ngày | Không kiểm tra/ Không cộng dồn vào hạn mức ngày
 | 3 | 
Phí giao dịch 
 | Không kiểm tra
 | 4 | Hạn mức theo nhóm chuyển tiền/ ngày (Cài đặt trên App) | Không kiểm tra/ Không cộng dồn vào hạn mức ngày
 | 5 | Hạn mức về số lần giao dịch/ ngày | Không kiểm tra/ Không cộng dồn vào hạn mức ngày
 | 6 | Hạn mức tối đa/ Giao dịch | Không kiểm tra
 | 7 | Hạn mức tối thiểu/ Giao dịch | Không kiểm tra (Kiểm tra theo số tiền tối thiểu tại bảng Quản lý sản phẩm)
 | 8 | Số dư khả dụng | Có kiểm tra. 
Đối với Hình thức tích lũy = Tích lũy định kỳ tự động, có 2 trường Số tiền là: Số tiền gửi ban đầu và Số tiền gửi định kỳ thì chỉ kiểm tra số dư khả dụng theo trường Số tiền gửi ban đầu

• Hợp lệ: Gửi yêu cầu kiểm tra thời điểm core chạy batch
 | 
GW Bank 

Core Bank
 |  Kiểm tra thời điểm chạy batch và trả về kết quả
 | MB | 
Nhận kết quả:

• Không thành công:  Tại thời điểm core chạy batch, không cho phép mở sổ. Hiển thị thông báo lỗi tương ứng "Xin lỗi quý khách, hệ thống đang xử lý dữ liệu cuối ngày. Quý khách vui lòng không thực hiện giao dịch" . Đóng thông báo, giữ nguyên màn hình hiện tại.
• Thành công:  Hiển thị màn hình xác nhận giao dịch

##### MH Xác nhận giao dịch
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhấn "Xác nhận"

 | MB | 
Chuyển sang màn hình xác thực giao dịch theo phương thức xác thực tương ứng đã chọn:

• Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)
• Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)
• Nếu phương thức xác thực là vân tay → Gửi yêu cầu xác thực giao dịch (Tham khảo logic xử lý tại Xác thực bằng Touch ID/Face ID)

##### MH Xác thực giao dịch
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhập thông tin xác thực và nhấn "Tiếp tục"

 | MB | 
1/ Xử lý xác thực giao dịch theo PTXT (Tham khảo:  URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2))

2/ Gửi yêu cầu Mở tiền gửi tiết kiệm trực tuyến sang HT Bank (API: openTDAcc)

Input: 
 | 
 | Trường | Mô tả | Ghi chú
 | 1 | 
CifNo
 | Mã KH | 

 | 2 | 
productCode 
 | Mã sản phẩm | Như hiện tại
 | 3 | 
accountClass
 | 
 | Như hiện tại
 | 4 | 
debitAccount
 | Tài khoản ghi
nợ | Như hiện tại
 | 5 | 
amount
 | Số tiền gửi tích lũy ban đầu | 

 | 6 | 
reciprocalAccount
 | Tài khoản nhận gốc lãi | Như hiện tại
 | 7 | 
rdType
 | Hình thức gửi
góp | 
Chỉ truyền nếu Sản phẩm tiết kiệm được đánh dấu = Tích lũy

• 0:  Hình thức tích lũy linh động
• 1: Hình thức tích lũy định kỳ tự động
 | 8 | 
rdAmount
 | Số tiền gửi định kỳ | Chỉ truyền nếu Sản phẩm tiết kiệm được đánh dấu = Tích lũy
 | 9 | 
rdPaymentAcount
 | Tài khoản trích tiền tự động | Chỉ truyền nếu Sản phẩm tiết kiệm được đánh dấu = Tích lũy
 | 10 | 
rdFrequency
 | 
Chu kỳ  tích lũy
 | 
Chỉ truyền nếu Sản phẩm tiết kiệm được đánh dấu = Tích lũy

• Hàng ngày→ Truyền 1D
• 2 ngày/ lần → Truyền 2D
• Hàng tuần → Truyền 7D
• Hàng tháng → Truyền 1M
• 2 tháng/ lần → Truyền 2M
• Hàng quý → Truyền 1Q
• Hàng năm → Truyền 1Y
 | 11 | 
setType
 | Phương thức
đáo hạn | Như hiện tại
 | 12 | 
...
 | 
 | 

 | HT Bank | 
1/ Ghi nhận mở tài khoản tiết kiệm tích lũy trên hệ thống của Bank

2/ Phản hồi lại kết quả cho MB Server

 | MB | 
Nhận, kiểm tra kết quả:

• Không thành công: Cập nhật trạng thái giao dịch thất bại và phản hồi mã lỗi về cho Client
• Time-out: Cập nhật trạng thái time-out và phàn hồi về cho Client
• Thành công: Trả kết quả thành công

##### MH: Kết quả giao dịch
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
Nhấn chọn Tạo giao dịch mới
 | MB | 
Gọi lại danh sách tài khoản vừa thực hiện giao dịch để cập nhật lại số dư tài khoản

Trở lại màn hình khởi tạo Mở tiền gửi trực tuyến

 | 2 | Nhấn chọn Giấy xác nhận  | MB/HT Bank | Như hiện tại <Tham khảo tại >
 | 3 | Chọn lưu file PDF | MB | 
Như hiện tại <Tham khảo tại >

 | 4 | 
Nhấn Icon lưu ảnh
 | 
MB
 | 
Tham khảo tại Logic xử lý chung

 | 5 | 
Nhấn Nút chia sẻ
 | 
MB
 | 
Tham khảo tại Logic xử lý chung

---

#### 30.5.4. Thay đổi phương thức tất toán/rút gốc

> **Page ID:** `559054874` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/559054874

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

##### 30.5.4.1. Flow& Action screen - Thay đổi phương thức tất toán/rút gốc

> **Page ID:** `559054875` · **Version:** 26
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/559054875

Mục lục
none
greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThaoCY | 
 | 
Tạo mới
 | V.1

### 1/ Luồng di chuyển màn hình

trueUntitled Diagramfalseautotoptrue20615

### 2/ Danh sách màn hình

##### MH1: Thông tin chi tiết tài khoản

##### MH2: Thay đổi phương thức tất toán/rút gốc

##### MH3: Popup xác nhận

#### 2.1. Luồng màn hình xác thực Facepay kết hợp SMS OTP

##### MH4: Xác thực facepay thành công

##### MH5: Xác thực facepay lỗi (lỗi oval)

 

##### MH6:  Xác thực SMS OTP

##### MH8: Kết quả

##### 

#### 2.2 Luồng màn hình xác thực Facepay kết hợp Soft OTP

 MH7.1: Nhập mã PIN Soft OTP

#####  MH7.2: Xác thực Soft OTP

##### 

##### MH8: Kết quả

##### 

#### 2.3. Luồng màn hình yêu cầu xác thực Facepay nhưng KH chưa có dữ liệu STH C06/ Đã có dữ liệu nhưng GTTT hết hạn

### 3/ Mô tả màn hình

##### MH1: Thông tin chi tiết tài khoản

<Tham chiếu >

##### MH2: Thay đổi phương thức tất toán/rút gốc
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Thay đổi phương thức tất toán/rút gốc
 | 2 | Icon Back | Icon | Click  | -- | -- | Quay về màn hình Thông tin chi tiết tài khoản
 | 3 | Icon Home | Icon | Click  | -- | -- | Quay về màn hình Trang chủ
 | 4 | Tất toán/rút gốc online | Radio button | Click | -- | -- | 
Mặc định hiển thị tương ứng với phương thức tất toán/ rút gốc của tài khoản. 

Cho phép thay đổi

tellerStatus =1

 | 5 | Tất toán/rút gốc tại quầy | Radio button | Click | -- | -- | 
Mặc định hiển thị tương ứng với phương thức tất toán/ rút gốc của tài khoản. 

Cho phép thay đổi

tellerStatus =0

##### MH3: Popup Xác nhận 
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | --  | Thông báo
 | 2 | Nội dung | Label | ReadOnly | -- | -- | 
Quý khách có chắc chắn thay đổi phương thức Tất toán/Rút gốc của tài khoản không?

 | 3 | Hủy | Button | Click | -- | -- | Tắt thông báo, giữ nguyên màn hình cũ
 | 4 | Đồng ý | Button | Click | -- | -- | <tham chiếu logic xử lý>

##### MH4: Xác thực facepay thành công
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Xác thực khuôn mặt
 | 2 | Hướng dẫn  | 
Label
 | 
Auto action
 | 
--
 | 
--
 | 
Hướng dẫn xác thực: 

• Label
 | 3 | Vùng chụp ảnh và % hoàn thành | 
Capture
 | 
View
 | 
--
 | 
--
 | 
Tự động thực hiện quét ảnh khuôn mặt theo hướng dẫn thực hiện

Hiển thị vòng tròn xanh tương ứng với % hoàn tất

Trong quá trình chụp ảnh, nếu khuôn mặt thoát khỏi vùng định vị khuôn mặt (vòng tròn) thì reset quá trình khuôn mặt và lấy ngẫu nhiên các hướng dẫn khác để thực hiện xác thực khuôn mặt

Yêu cầu chụp 1 ảnh xa

 | 4 | Hướng dẫn hành động cần thực hiện | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
• 
Hiển thị theo nhận diện khuôn mặt, thông báo động theo lỗi SDK nhận diện 

• Đưa khuôn mặt vào giữa khung hình
• Giữ thiết bị ổn định 
• ...
• Hoàn thành 
 | 5 | Hoàn thành | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hoàn thành. Tự động chuyển sang MH5

 | 6 | Nội dung hướng dẫn | 
Label
 | 
ReadOnly
 | 
--
 | 
-- 
 | 
Nội dung được fix tại Client: "Điều chỉnh khuôn mặt nằm trong khung hình"

##### MH5: Xác thực facepay lỗi 
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề
 | 
Label
 | 
Click
 | 
--
 | 
--
 | 
Kết quả xác thực

 | 2 | 
Back
 | 
icon
 | 
Click
 | 
--
 | 
--
 | 
Trở về màn hình Thông tin chi tiết tài khoản

 | 3 | 
Nội dung
 | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Fix Client

Ảnh chân dung không hợp lệ. Vui lòng thực hiện lại 

 | 4 | 
Ảnh chụp thẳng khuôn mặt
 | 
Picture/ icon
 | 
Readonly
 | 
--
 | 
--
 | 
Icon lỗi và hình ảnh chụp chân dung do SDK trả

Cho phép click xem ảnh đã chụp 

 | 5 | 
Ghi chú
 | 
Label
 | 
Click
 | 
--
 | 

 | 
Xác thực không thành công.

Trả mã lỗi tương ứng từ FacePay server trả về.

 | 6 | 
Chụp lại
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Trở về màn hình chụp khuôn mặt

##### MH6: Xác thực SMS OTP

Hiển thị màn hình xác thực bằng SMS OTP với trường hợp:

• KH chưa cài đặt kích hoạt Soft OTP
• KH đã cài đặt kích hoạt Soft OTP nhưng chưa thực hiện đủ (n ) giao dịch bằng SMS OTP | | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Xác thực giao dịch
 | 2 | Ghi chú xác thực 1 | Label | ReadOny | -- | -- | 
Hiển thị nội dung fix tại Client:

• Nội dung: Quý khách vui lòng nhập mã OTP đã được gửi về số điện thoại 098*****23
 | 3 | Ô nhập OTP | Textbox | Number | Yes | 6 | 
Hiển thị 6 ô nhập ký tự OTP

Bàn phím số

Mặc định trống

 | 4 | Ghi chú xác thực 2 | Lable | ReadOnly | -- | -- | 
Hiển thị nội dung fix tại Client

"Lưu ý: Quý khách còn {n} giao dịch xác thực bằng SMS OTP để chuyển sang phương thức Soft OTP"

Trong đó:

• (n ) là giá trị do server trả về: Là số lần giao dịch có xác thực SMS OTP còn lại cần thực hiện trước kh chuyển sang phương thức Soft OTP được đếm tại MB server tính từ lúc kích hoạt Soft OTP thành công
 | 5 | Nút "Xác nhận" | Button | Click | -- | -- | 
Mặc định enable

##### MH7.1: Xác thực bằng Soft OTP

Hiển thị màn hình xác thực bằng Soft OTP với trường hợp:

• KH đã đăng ký Soft OTP và đã thực hiện đủ (n ) giao dịch bằng SMS OTP | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Xác thực giao dịch
 | 2 | Ghi chú 1 | Label | ReadOnly | -- | -- | 
Hiển thị nội dung fix tại Client

• "Vui lòng nhập mã PIN của Soft OTP để xác thực giao dịch"
 | 3 | Nhập mã PIN | Textbox | Number | Yes | 6 | 
Mặc định trống

Bàn phím số

Cho phép nhập mã PIN Soft OTP tối đa 6 ký tự

Mã hóa ký tự nhập vào bằng ký tự *

 | 4 | Ghi chú 2 | Label | ReadOnly | -- | -- | 
Lưu ý: Soft OTP sẽ bị khóa nếu Qúy khách nhập sai PIN {n} lần liên tiếp

 | 5 | Xác nhận | Button | Click | -- | -- | 
Chuyển sang màn hình Xác thực

##### MH7.2: Xác thực bằng Soft OTP
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Xác thực giao dịch
 | 2 | Ghi chú xác nhận giao dịch Soft OTP | Label | Read Only | -- | -- | 
Mã xác thực OTP bằng phương thức xác thực Soft OTP của Quý khách đang hiển thị dưới đây. Vui lòng bấm "Xác thực" để hoàn tất giao dịch

 | 3 | Mã Soft OTP | Label | Read Only | -- | -- | 
Hiển thị mã Soft OTP 6 ký tự số do Client sinh theo thuật toán quy định và tự động thay đổi mã Soft OTP khác sau mỗi block 30 giây.

Hiển thị  thanh đếm ngược thời gian. Hết {n} giây thanh đếm ngược lại được làm đầy và giảm dần theo thời gian

Lưu ý:

• n là tham số block 30 giây đếm ngược tại Client do Soft OTP Server trả về.
 | 4 | Nút "Xác nhận" | Button | Click | -- | -- | 
Mặc định Enable

MH8: Kết quả 
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | --  | Thông báo
 | 2 | Nội dung | Label | ReadOnly | -- | -- | 
Quý khách đã thay đổi phương thức Tất toán/ Rút gốc thành công

 | 3 | Đóng | Button | Click | -- | -- | Quay lại màn hình Danh sách tài khoản/ danh sách tiền gửi tiết kiệm

---

##### 30.5.4.2. User Action Flow - Thay đổi phương thức tất toán/rút gốc

> **Page ID:** `565641266` · **Version:** 15
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/565641266

Mục lục
none
greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThaoCY | 
 | 
Tạo mới
 | V.1

### 1/ Mô tả UseCase
 | Use Case Name: | Thay đổi phương thức tất toán/rút gốc
 | Use Case ID: | UC_Saving_06
 | Use Case Description: | 
Là người dùng, tôi muốn thay đổi phương thức tất toán/rút gốc

 | Actor: | 
KH, MB, Bank, eKYC

 | Priority: | Medium 
 | Trigger: | 
KH thực hiện lệnh Thay đổi phương thức tất toán/rút gốc

 | 
Pre-Condition:
 | 
1/ KH đăng nhập thành công vào hệ thống Mobile banking

2/ KH thuộc gói dịch vụ được phép sử dụng chức năng này.

3/ KH có tài khoản nguồn hợp lệ để thực hiện chức năng này

4/ KH đã mở ít nhất 1 tài khoản tiền gửi trực tuyến tại NH Co-opBank

 | Post-Condition: | 
1/ KH thay đổi phương thức tất toán/rút gốc

 | 
 | 
1/ KH đăng nhập ứng dụng

2/ KH chọn chức năng "Tiết kiệm" và thực hiện chọn chức năng  "Danh sách tiền gửi"

3/ KH chọn tài khoản xem chi tiết 

4/ Hệ thống MB/Bank truy vấn thông tin chi tiết Tài khoản tiền gửi và trả về thông tin tài khoản

5/ KH chọn "Chức năng khác" → chọn "Thay đổi phương thức tất toán/rút gốc"

6/ Hệ thống hiển thị màn hình Thay đổi phương thức tất toán/rút gốc

7/ KH thực hiện thay đổi phương thức

8/ Hệ thống hiển thị màn hình xác nhận

9/ KH chọn "Đồng ý" 

TH1: KH thay đổi phương thức tất toán/rút gốc tại quầy thành phương thức tất toán/rút gốc online

10.1/ Hệ thống hiển thị màn hình xác thực với PTXT là Soft OTP/SMS OTP kết hợp Facepay

11.1/ KH thực hiện xác thực

12.1/ Hiển thị màn hình kết quả, hệ thống cập nhật thông tin

TH2: KH thay đổi phương thức tất toán/rút online thành phương thức tất toán/rút tại quầy

10.2/ Hiển thị màn hình kết quả, hệ thống cập nhật thông tin

 | Alternative Flow: | 

 | Exception Flow: | 

 | Bussiness Rules: | 
1/ Nếu tài khoản đã chọn phương thức Tất toán/rút gốc tại quầy, hệ thống sẽ không cho phép thực hiện giao dịch tất toán/rút gốc trực tuyến

2/ Tại thời điểm core bank chạy batch, không được phép thay đổi phương thức tất toán/rút gốc

3/ Chỉ được thay đổi phương thức tất toán/rút gốc với các tài khoản tiền gửi online, không áp dụng với các tài khoản mở tại quầy 

 | Non-Funtional Requiremnt: | 

### 2/ Luồng sơ đồ

true1falseautotoptrue11014

### 3/ Luồng xử lý

MH1: Thông tin chi tiết tài khoản
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Người dùng chọn "Thay đổi phương thức tất toán/rút gốc" | MB | 
Gửi yêu cầu kiểm tra thời gian chạy batch đến bank qua API: /queryEODStat

 | 2 | Bank | 
Kiểm tra thời gian chạy batch và phản hồi MB server

 | 3 | MB | 
Nhận kết quả và xử lý

• Không hợp lệ: Tại thời điểm core chạy batch, không cho phép thay đổi phương thức tất toán/rút gốc → Trả thông báo lỗi "Yêu cầu không thực hiện được lúc này. Quý khách vui lòng thực hiện lại sau"
• Hợp lệ: Hiển thị MH2

##### MH2: Thay đổi phương thức tất toán/rút gốc
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn phương thức tất toán/rút gốc | MB  | 
Hiển thị MH3

##### MH3: Popup xác nhận
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn "Hủy" | MB  | Đóng popup, cập nhật lại phương thức tất toán/rút gốc ban đầu
 | 2 | Chọn "Đồng ý" | MB  | 
Kiểm tra giá trị trường tellerStatus trong request:

• Nếu tellerStatus=0 → Gửi yêu cầu thay đổi phương thức tất toán sang Bank qua API: changeTxnTeller
• Nếu tellerStatus=1
• 1/ Kiểm tra tham số REQUIRE_FACEPAY_ FEE (ON/OFF)
• Nếu REQUIRE_FACEPAY_ FEE=OFF → Trả client cờ Require_facepay = 0
• Nếu REQUIRE_FACEPAY_ FEE=ON → Trả client cờ Require_facepay = 1
• 2/ Kiểm tra PTXT
• 
• 
• Trường hợp KH có cài đặt Soft OTP
• Nếu KH đã xác thực đủ (n ) GD tài chính bằng SMS OTP → Trả PTXT Soft OTP
• Nếu KH chưa xác thực đủ (n ) GD tài chính bằng SMS OTP → Trả PTXT SMS OTP
• Nếu Soft OTP của KH đang bị Lock/Auto Lock → Trả PTXT SMS OTP
• Trường hợp KH không cài đặt Soft OTP → Trả PTXT SMS OTP
 | 3 | 
TH1: tellerStatus=0

 | 4 | 
 | Bank | 
Xử lý và trả kết quả về MB

 | 5 | 
 | MB | 
Hiển thị kết quả:

• Không thành công: Hiển thị thông báo lỗi tương ứng
• Thành công: Hiển thị MH8
 | 6 | 
TH2: tellerStatus=1

 | 7 | 
 | 
MB
 | 
• Nếu Require_facepay = 0 → Thực hiện xác thực theo PTXT MB server trả
• Nếu Require_facepay =1 → Thực hiện như mô tả sau:
A. Nhận PTXT

1/ Bật gọi ngầm SDK Thu thập STH

2/ Gửi yêu cầu kiểm tra trạng thái STH đến SDK thu thập STH  (Tham khảo tài liệu Thu thập STH: Detail logic flow_Luồng Thu thập STH qua eKYC CCCD CHIP check C06)

3/ Nhận kết quả check trạng thái STH

• Đã thu thập STH + GTTT chưa hết hạn → Mở đến SDK Facepay →  Xem mô tả API check FacePay tại Detail Logic Flow_Xác thực giao dịch bằng FacePay → Sau khi thực hiện xong → Chuyển bước B. Kiểm tra kết quả thực hiện STH/FacePay
• Chưa thu thập STH → Điều hướng đến SDK Thu thập như đã mô tả → Sau khi thực hiện xong→ Chuyển bước B.Kiểm tra kết quả thực hiện STH/FacePay
• Đã thu thập STH + Giấy tờ hết hạn → Hiển thị thông báo "Giấy tờ của Quý khách đã hết hạn. Quý khách vui lòng thu thập lại thông tin sinh trắc học để tiếp tục thực hiện giao dịch"
Cả 2 trường hợp Chưa thu thập và Đã thu thập + giấy tờ hết hạn sẽ có 2 lựa chọn: Bỏ qua và Đồng ý

• Hủy: Tắt thông báo, quay lại màn hình "Thay đổi phương thức tất toán/rút gốc"
• Đồng ý: Điều hướng đến SDK Thu thập như đã mô tả → Sau khi thực hiện xong, hiển thị MH2, tiếp tục thực hiện Thay đổi phương thức tất toán/rút gốc
B. Kiểm tra kết quả thực hiện STH/Facepay

• Kết quả Facepay: (Luồng API Facepay tham khảo mô tả API tại : Detail Logic Flow_Xác thực giao dịch bằng FacePay)
• Không thành công: Hiển thị thông báo lỗi và không cho đi tiếp
• Thành công: Hiển thị màn hình theo PTXT tương ứng MB server trả → KH thực hiện xác thực → Thành công (xử lý tương tự TH1, MB server gọi API changeTxnTeller sang Bank) → Update cờ First_Facepay = 1  (Để giao dịch đầu tiên không yêu cầu quét FacePay nữa)

##### MH6: Xác thực SMS OTP

<tham khảo >

##### MH7.1: Nhập mã PIN SOFT OTP

<tham khảo >

##### MH7.2: Xác thực Soft OTP

<tham khảo >

##### MH8: Kết quả
 | Thao tác | Tác nhân | Mô tả
 | Chọn "Đóng" | MB | Hiển thị MH Danh sách tài khoản / Danh sách tiết kiệm (tùy thuộc luồng truy cập chức năng của KH)

---

#### 30.5.5. Thay đổi thông tin tích lũy định kỳ

> **Page ID:** `557058076` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/557058076

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

##### 30.5.5.1. Flow& Action screen - Thay đổi thông tin tích lũy định kỳ

> **Page ID:** `557058084` · **Version:** 32
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/557058084

Mục lục
none
greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThaoCY | 
 | 
Tạo mới
 | V.1

### 1/ Luồng di chuyển màn hình

trueUntitled Diagramfalseautotoptrue19315

### 2/ Danh sách màn hình

##### MH1: Thông tin chi tiết tài khoản

##### MH2: Thay đổi thông tin tích lũy định kỳ (trường hợp passbook_no=Null, ON trích tự động tích lũy) 

##### MH2.1: Popup chọn tài khoản trích tiền

##### MH2.2: Thay đổi thông tin tích lũy định kỳ (trường hợp passbook_no=Null,  OFF trích tự động tích lũy) 

##### MH2.3: Thay đổi thông tin tích lũy định kỳ (trường hợp passbook_no ≠Null , ON trích tự động tích lũy)

 MH2.3: Thay đổi thông tin tích lũy định kỳ (trường hợp passboook_no ≠ Null, OFF trích tự động tích lũy)

#####  MH3: Popup xác nhận

##### MH4: Xác thực bằng SMS OTP

##### MH5: Nhập mã PIN Soft OTP 

##### MH6: Xác thực giao dịch bằng Soft OTP 

##### MH7: Kết quả

### 3/ Mô tả màn hình

##### MH1: Thông tin chi tiết tài khoản
<Tham chiếu >

##### MH2: Thay đổi thông tin tích lũy định kỳ
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Thay đổi thông tin tích lũy định kỳ
 | 2 | Icon Back | Icon | Click  | -- | -- | Quay về màn hình Thông tin chi tiết tài khoản
 | 3 | Tài khoản tiền gửi | Label | ReadOnly | -- | -- | 
Logo ngân hàng + Tài khoản tiền gửi trực tuyến

Hiển thị tài khoản tiền gửi trực tuyến (accountNo)

Không cho phép chọn tài khoản tiền gửi trực tuyến khác

 | 4 | Số dư gốc hiện tại | Label | ReadOnly | -- | -- | 
Hiển thị số tiền của tài khoản tiền gửi trực tuyến (availBalance)

Định dạng: availBalance + currency

 | 5 | Tiêu đề | Label | ReadOnly | -- | -- | Thông tin tài khoản
 | 6 | Hình thức tích kỹ | Label | ReadOnly | -- | -- | Tích lũy định kỳ tự động
 | 7 | Chu kỳ tích lũy | Label | ReadOnly | -- | -- | Hiển thị theo thông tin tài khoản
 | 8 | Thay đổi thông tin tích lũy | Label | ReadOnly | -- | -- | Thay đổi thông tin tích lũy
 | 9 | Trích tự động tích lũy | Toggle | Click | -- | -- | 
Cho phép ON/OFF trạng thái Trích tích lũy tự động

Hiển thị theo trạng thái tích lũy của tài khoản 

rdScheStatus, mặc định là 1 nếu server trả ""

 | 10 | Số tiền tích lũy định kỳ | Text | Input | -- | 15 | 
Chỉ được nhập số, không cho nhập số 0 ở đầu, có dấu "," phân cách hàng nghìn

Chỉ hiển thị với tài khoản mở  tại app (passbook_no=Null) và trạng thái Trích tự động tích lũy là ON (rdScheStatus = Y)

Mặc định trống

• Nếu đang ON: Mặc định để trống, hintext: "Số tiền tích lũy định kỳ hiện tại là x" (x là số tiền tích lũy định kỳ hiện tại của TK tương ứng)
• Nếu đang OFF chuyển sang ON thì hiển thị trống
Có gợi ý số tiền chuyển, quy tắc gợi ý số tiền xem tại quy tắc xử lý chung.

Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

 | 11 | Số tiền tích lũy định kỳ tối thiểu | Label | ReadOnly | -- | -- | 
Chỉ hiển thị với tài khoản:

• Mở tại app (passbook_no=Null) 
• Trạng thái Trích tự động tích lũy là ON (rdScheStatus = Y)
• và giá trị khai báo trong BE ≠ 0
Hiển thị giá trị khai báo trên BE

 | 12 | Ghi chú | Label | ReadOnly | -- | -- | 
Nội dung: Số tiền tích lũy định kỳ hiện tại là x" (x là số tiền tích lũy định kỳ hiện tại của TK tương ứng). Bỏ trống nếu không thay đổi số tiền tích lũy định kỳ

 | 13 | Tài khoản trích tiền | Combobox | Select | -- | -- | 
Chỉ hiển thị với tài khoản giao dịch tại app (passbook_no=Null) và trạng thái Trích tự động tích lũy là ON (rdScheStatus = Y)

Mặc định là Tài khoản trích tích lũy hiện tại, cho phép chọn lại

Click vào mở ra màn hình popup chọn tài khoản

• Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết
•  Tài khoản trích tích lũy hiện tại được mặc định tích chọn, có thể thay đổi
• Hiển thị bao gồm:
• Số tài khoản
• Số dư
 | 14 | Tiếp tục | Button | Click | -- | -- | <Tham chiếu logic xử lý>

##### MH3: Popup Xác nhận 
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | --  | Thông báo
 | 2 | Nội dung | Label | ReadOnly | -- | -- | 
Quý khách có chắc chắn muốn thay đổi thông tin tích lũy định kỳ không?

 | 3 | Hủy | Button | Click | -- | -- | Tắt thông báo, giữ nguyên màn hình cũ
 | 4 | Đồng ý | Button | Click | -- | -- | <tham chiếu logic xử lý>

##### MH4: Xác thực bằng SMS OTP

Hiển thị màn hình xác thực bằng SMS OTP với trường hợp:

• KH chưa cài đặt kích hoạt Soft OTP
• KH đã cài đặt kích hoạt Soft OTP nhưng chưa thực hiện đủ (n ) giao dịch bằng SMS OTP | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Xác thực giao dịch
 | 2 | Ghi chú xác thực 1 | Label | ReadOny | -- | -- | 
Hiển thị nội dung fix tại Client:

• Nội dung: Quý khách vui lòng nhập mã OTP đã được gửi về số điện thoại 098*****23
 | 3 | Ô nhập OTP | Textbox | Number | Yes | 6 | 
Hiển thị 6 ô nhập ký tự OTP

Bàn phím số

Mặc định trống

 | 4 | Ghi chú xác thực 2 | Lable | ReadOnly | -- | -- | 
Hiển thị nội dung fix tại Client

"Lưu ý: Quý khách còn {n} giao dịch xác thực bằng SMS OTP để chuyển sang phương thức Soft OTP"

Trong đó:

• (n ) là giá trị do server trả về: Là số lần giao dịch có xác thực SMS OTP còn lại cần thực hiện trước kh chuyển sang phương thức Soft OTP được đếm tại MB server tính từ lúc kích hoạt Soft OTP thành công
 | 5 | Nút "Xác nhận" | Button | Click | -- | -- | 
Mặc định enable

##### MH5: Nhập mã PIN Soft OTP 

Hiển thị màn hình xác thực bằng Soft OTP với trường hợp:

• KH đã đăng ký Soft OTP và đã thực hiện đủ (n ) giao dịch bằng SMS OTP | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Xác thực giao dịch
 | 2 | Ghi chú 1 | Label | ReadOnly | -- | -- | 
Hiển thị nội dung fix tại Client

• "Vui lòng nhập mã PIN của Soft OTP để xác thực giao dịch"
 | 3 | Nhập mã PIN | Textbox | Number | Yes | 6 | 
Mặc định trống

Bàn phím số

Cho phép nhập mã PIN Soft OTP tối đa 6 ký tự

Mã hóa ký tự nhập vào bằng ký tự *

 | 4 | Ghi chú 2 | Label | ReadOnly | -- | -- | 
Lưu ý: Soft OTP sẽ bị khóa nếu Qúy khách nhập sai PIN {n} lần liên tiếp

 | 5 | Xác nhận | Button | Click | -- | -- | 
Chuyển sang màn hình Xác thực

##### MH6: Xác thực bằng Soft OTP
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | -- | Xác thực giao dịch
 | 2 | Ghi chú xác nhận giao dịch Soft OTP | Label | Read Only | -- | -- | 
Mã xác thực OTP bằng phương thức xác thực Soft OTP của Quý khách đang hiển thị dưới đây. Vui lòng bấm "Xác thực" để hoàn tất giao dịch

 | 3 | Mã Soft OTP | Label | Read Only | -- | -- | 
Hiển thị mã Soft OTP 6 ký tự số do Client sinh theo thuật toán quy định và tự động thay đổi mã Soft OTP khác sau mỗi block 30 giây.

Hiển thị  thanh đếm ngược thời gian. Hết {n} giây thanh đếm ngược lại được làm đầy và giảm dần theo thời gian

Lưu ý:

• n là tham số block 30 giây đếm ngược tại Client do Soft OTP Server trả về.
 | 4 | Nút "Xác nhận" | Button | Click | -- | -- | 
Mặc định Enable

##### MH7: Kết quả 
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | -- | --  | Thông báo
 | 2 | Nội dung | Label | ReadOnly | -- | -- | 
Quý khách đã thay đổi thông tin tích lũy định kỳ thành công

 | 3 | Đóng | Button | Click | -- | -- | Quay lại màn hình Danh sách tài khoản/ Danh sách tiền gửi

---

##### 30.5.5.2. User Action Flow - Thay đổi thông tin tích lũy định kỳ

> **Page ID:** `565641831` · **Version:** 15
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/565641831

Mục lục
none
greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThaoCY | 
 | 
Tạo mới
 | V.1

### 1/ Mô tả UseCase
 | Use Case Name: | Thay đổi thông tin tích lũy định kỳ]
 | Use Case ID: | UC_Saving_05
 | Use Case Description: | 
Là người dùng, tôi muốn xem danh sách tài khoản tiền gửi trực tuyến và tài khoản tiền gửi tại quầy, đồng thời thay đổi thông tin tiết kiệm tích lũy

 | Actor: | 
KH, MB, Bank

 | Priority: | Medium 
 | Trigger: | 
KH thực hiện lệnh Thay đổi thông tin tích lũy định kỳ

 | 
Pre-Condition:
 | 
1/ KH đăng nhập thành công vào hệ thống Mobile banking

2/ KH thuộc gói dịch vụ được phép sử dụng chức năng này.

3/ KH có tài khoản nguồn hợp lệ để thực hiện chức năng này

4/ KH đã mở ít nhất 1 tài khoản tiền gửi trực tuyến tại NH Co-opBank

 | Post-Condition: | 
1/ KH thay đổi thông tin tích lũy định kỳ thành công

 | Basic Flow: | 
1/ KH đăng nhập ứng dụng

2/ KH chọn chức năng "Tiết kiệm" và thực hiện chọn chức năng  "Danh sách tiền gửi"

3/ KH chọn tài khoản xem chi tiết 

4/ Hệ thống MB/Bank truy vấn thông tin chi tiết Tài khoản tiền gửi và trả về thông tin tài khoản

5/ KH chọn "Thay đổi thông tin tích lũy định kỳ"

6/ Hệ thống hiển thị màn hình Thay đổi thông tin tích lũy định kỳ 

7/ KH thực hiện thay đổi thông tin, sau đó chọn "Tiếp tục"

8/ Hệ thống hiển thị màn hình xác nhận

9/ KH chọn "Đồng ý" 

10/ Hệ thống hiển thị popup Xác thực

11/ KH thực hiện xác thực

12/ Hệ thống cập nhật thông tin

 | Alternative Flow: | 

 | Exception Flow: | 

 | Bussiness Rules: | 
1/ Chỉ có thể thực hiện thay đổi thông tin với Tài khoản có Hình thức tích lũy là tích lũy định kỳ tự động (rdType=1)

• Sản phẩm tích lũy trực tuyến linh động: cho phép thay đổi trạng thái (on/off), số tiền trích mỗi kỳ, Tk trích
• Sản phẩm tích lũy linh động tại quầy: cho phép thay đổi trạng thái trích (on/ off)
2/ Hệ thống không cho phép thay đổi thông tin tích lũy trong thời gian chạy batch tại Bank

3/ Chỉ được thay đổi thông tin trong trường hợp trạng thái Trích tự động tích lũy là ON

 | Non-Funtional Requiremnt: | 

### 2/ Luồng sơ đồ

trueUntitled Diagramfalseautotoptrue8213

### 3/ Luồng xử lý

MH1: Thông tin chi tiết tài khoản
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Người dùng chọn "Thay đổi thông tin tích lũy định kỳ" tại màn hình Thông tin chi tiết | MB | Nhận và gửi yêu cầu kiểm tra thời gian chạy batch tại Bank qua API queryEODStat
 | Bank | Kiểm tra thời điểm chạy batch
 | MB | 
Nhận kết quả và xử lý

• Không hợp lệ: Tại thời điểm core chạy batch, không có phép thay đổi thông tin tích lũy định kỳ → Trả về thông báo lỗi: "Yêu cầu không thực hiện được trong lúc này. Quý khách vui lòng thực hiện lại sau"
• Hợp lệ: Hiển thị MH2

##### MH2: Thay đổi thông tin tích lũy định kỳ
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Bấm "ON" trích tích lũy tự động | MB | 
Nếu passbook_no = Null → Hiển thị các trường:

• Số tiền tích lũy định kỳ
• Số tiền tích lũy định kỳ tối thiểu
• Tài khoản trích tiền
Nếu passbook_no ≠ Null → Chỉ được thay đổi trạng thái tích lũy, không hiển thị các thông tin khác

 | 2 | Bấm "OFF" trích tích lũy tự động | MB | 
Ẩn các trường:

• Số tiền tích lũy định kỳ
• Số tiền tích lũy định kỳ tối thiểu
• Tài khoản trích tiền
 | 3 | Bấm "Chọn tài khoản trích tiền" | MB | Gửi yêu cầu lấy danh sách tài khoản thanh toán đến Bank qua API: /queryCurrentAccSum
 | 4 | Bank | 
Nhận yêu cầu và truy vấn lấy danh sách tài khoản thanh toán 

Trả kết quả về MB

 | 5 | MB | 
Nhận kết quả

• Không thành công: | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại. | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn "Thử lại" gọi lấy lại danh sách tài khoản

• Thành công: Hiển thị popup chọn Tài khoản gồm danh sách các tài khoản do bank trả về, hiển thị bao gồm
• Số tài khoản
 | 6 | Chọn 1 tài khoản trích tiền | MB | 
Đóng popup

Fill thông tin vào ô tài khoản trích tiền, bao gồm:

• Số tài khoản
Lưu ý: Chỉ được phép chọn 1 tài khoản

 | 7 | Chọn "Tiếp tục" | MB | 
Thực hiện Validate

• Không hợp lệ: Hiển thị thông báo lỗi | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Số tiền tích lũy định kỳ = Số tiền tích lũy định kỳ hiện tại | Quý khách vui lòng bỏ trống nếu không thay đổi số tiền tích lũy định kỳ. | 

 | 2 | 
Không thay đổi thông tin nào

Thực hiện so sánh thông tin về Trạng thái trích gửi góp (rdScheStatus), Số tiền tích lũy định kỳ (rdAmount), Tài khoản trích tiền (rdPaymentAcount) từ respone MB server trả về trong mid11 với thông tin KH nhập/chọn → Nếu tất cả các thông tin trên trùng nhau thì hiển thị thông báo
 | Quý khách vui lòng  thay đổi ít nhất một thông tin. | Button "Đóng". Click "Đóng", tắt popup, giữ nguyên màn hình hiện tại

• Hợp lệ: Hiển thị MH3

##### MH3: Popup xác nhận
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn "Hủy"  | MB | Đóng popup, giữ nguyên màn hình hiện tại
 | 2 | Chọn "Đồng ý"  | MB | 
1/ Kiểm tra số tiền tích lũy định kỳ

• Không hợp lệ: Trả về thông báo lỗi | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Sồ tiền tích lũy định kỳ < Số tiền tích lũy định kỳ tối thiểu | Số tiền tích lũy định kỳ tối thiểu là x VND. Quý khách vui lòng kiểm tra lại! | 

• Hợp lệ: Nhận và gửi yêu cầu kiểm tra thời gian chạy batch tại Bank qua API queryEODStat
 | 3 | 
 | Bank | Kiểm tra thời điểm chạy batch
 | 4 | 
 | MB | 
Nhận kết quả và xử lý

• Không hợp lệ: Tại thời điểm core chạy batch, không có phép thay đổi thông tin tích lũy định kỳ → Trả về thông báo lỗi: "Yêu cầu không thực hiện được trong lúc này. Quý khách vui lòng thực hiện lại sau"
• Hợp lệ:
• 1/ Kiểm tra trạng thái Soft OTP của user
• Nếu KH đã kích hoạt Soft OTP → Chuyển bước 2
• Nếu KH chưa kích hoạt Soft OTP → Server xác định PTXT là SMS OTP → <tham chiếu TH1>
• 2/ Kiểm tra số lần giao dịch xác thực bằng SMS OTP thành công trước đó
• Nếu số lần xác thực SMS OTP < (n ) → Server xác định PTXT là SMS OTP → <tham chiếu TH1>
• Nếu số lần xác thực SMS OTP >= (n ) → Server xác định PTXT ưu tiên nhất so Server trả về là Soft OTP → Chuyển bước xác thực bằng Soft OTP → <tham chiếu TH2>
• Nếu trạng thái Soft OTP = Lock/AutoLock → Server xác định PTXT là SMS OTP → <tham chiếu TH1>
(Tham khảo Logic xác định PTXT của GD phi tài chính tại Logic kiểm tra chung Hạn mức, PTXT, Phí dịch vụ)

{n} là số lần xác thực SMS OTP trước khi xác thực bằng Soft OTP

 | 5 | TH1: Xác thực bằng SMS OTP
 | 6 | 
 | MB | Thực hiện sinh OTP và gửi yêu cầu cho Bank gửi SMS OTP cho KH 
 | 7 | 
 | Bank | Trả kết quả phản hồi gửi SMS OTP cho MB
 | 8 | 
 | MB | 
Nhận phản hồi:

• Không thành công: Hiển thị thông báo lỗi theo quy tắc chung
• Thành công: Hiển thị MH4
 | 9 | 
TH2: Xác thực bằng Soft OTP

 | 10 | 
 | MB | 
Gửi yêu cầu khởi tạo giao dịch Soft OTP đến Soft OTP server

 | 11 | 
 | Soft OTP Server | 
1/ Kiểm tra yêu cầu khởi tạo giao dịch Soft OTP

• Không hợp lệ: | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | 
Thiết bị Root/Jailbreak không được phép xác thực SoftOTP (nếu có)
 | Thiết bị của Quý khách bị Root/Jailbreak không được phép xác thực bằng phương thức Soft OTP. Quý khách vui lòng kiểm tra lại thiết bị hoặc liên hệ tổng đài CSKH: <xxxxxx> để được hỗ trợ. | 

 | 2 | 
Soft OTP đang bị khóa (Auto Lock)
 | Tài khoản của Quý khách bị khóa xác thực Soft OTP do nhập sai PIN quá số lần cho phép. Quý khách vui lòng thực hiện lại sau <dd/mm/yyyy hh:mm:ss> | dd/mm/yyyy hh:mm:ss là tham số thời gian tự động mở khóa Soft OTP tại hệ thống Soft OTP.
 | 3 | Soft OTP đang bị khóa (Lock) | Tài khoản của Quý khách đang bị khóa xác thực Soft OTP. Quý khách vui lòng kiểm tra lại hoặc liên hệ tổng đài CoopBank <xxxxxx> để được hỗ trợ. | 

• Hợp lệ: Trả kết quả thành công cho MB
 | 12 | 
 | MB | 
Nhận và hiển thị kết quả

• Không thành công: Hiển thị thông báo lỗi tương ứng
• Thành công: Hiển thị MH5

##### MH4: Xác thực bằng SMS OTP
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Nhấn "Xác nhận" | MB | 
1/ Thực hiện validate

• Không hợp lệ: | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Bỏ trống OTP | Mã OTP không được để trống | 

 | 2 | OTP nhỏ hơn 6 ký tự | Mã OTP phải bao gồm 6 ký tự | 

 | 3 | OTP sai | Mã OTP không chính xác. Quý khách vui lòng kiểm tra lại.  | Tắt thông báo giữ nguyên màn hình đang thao tác
 | 4 | OTP hết hiệu lực | Mã OTP đã hết hiệu lực. quý khách vui lòng thực hiện lại. | Tắt thông báo hiển thị màn hình thao tác trước đó

• Hợp lệ: Gửi yêu cầu thay đổi thông tin tích lũy định kỳ sang Bank qua API: changeRdAccountInfor (chỉ truyền những thông tin thay đổi, những không tin không thay đổi truyền Null)
 | Bank | 
Xử lý và trả kết quả cho MB

 | MB  | 
Nhận kết quả

• Không thành công: Hiển thị thông báo lỗi tương ứng 
• Thành công: Hiển thị MH7

MH5: Nhập PIN Soft OTP
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Nhấn "Xác nhận" | MB | 
Kiểm tra mã PIN

• Không hợp lệ: | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Mã PIN sai | Mã PIN không chính xác | 

 | 2 | Sai mã PIN 5 lần liên tiếp | Quý khách đã nhập sai mã PIN quá số lần quy định. quý khách vui lòng thực hiện giao dịch lại sau | Số lần sai PIN được cộng dồn của những lần sai PIN của cả những phiên đăng nhập trước đó. Ứng dụng thực hiện khóa Soft OTP ở ứng dụng. Đồng thời gửi yêu cầu khóa Soft OTP lên Soft OTP server thông qua MB server và hiển thị màn hình Thay đổi thông tin tích lũy định kỳ

• Hợp lệ: Sinh mã Soft OTP theo thuật toán quy định và hiển thị màn hình Xác thực giao dịch

#####  MH6: Xác thực bằng Soft OTP
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Nhấn "Xác nhận"  | MB | 
1/ Kiểm tra hiệu lực giao dịch

• Hết hiệu lực | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Giao dịch hết hiệu lực | Giao dịch đã hết hiệu lực. Quý khách vui lòng thực hiện lại giao dịch mới. | 

• Còn hiệu lực
2/ Gửi yêu cầu xác nhận giao dịch sang Soft OTP Server

 | Soft OTP server | 
1/ Kiểm tra yêu cầu xác nhận giao dịch

• Không hợp lệ: | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Thời gian không đồng bộ giữa Client và Soft OTP (lệch quá 120 giây) | Xác thực giao dịch không thành công do thời gian trên thiết bị chưa đồng bộ với thời gian trên hệ thống Soft OTP. quý khách vui lòng vào Cài đặt Ngày và giờ của thiết bị để điều chỉnh thời gian theo chế độ tự động. | 
Ứng dụng hiển thị thông báo lỗi và 2 nút thao tác "Cài đẳ thời gian", "Đóng"

• Nhấn "Cài đặt thời gian": Hiển thị màn hình cài đặt thời gian của thiết bị. Sau khi cài đặt thời gian, quay lại MH xác thực để KH tiếp tục xác thực giao dịch
• Nhấn "Đóng": Tắt thông báo và hiển thị màn hình khởi tạo giao dịch
 | 2 | Soft OTP đang bị khóa (AutoLock)  | Tài khoản của quý khách đang bị khóa xác thực Soft OTP do nhập sau PIN quá số lần cho phép. quý khách vui lòng thực hiện lại sau <dd/mm/yyyy hh:mm:ss> | 
dd/mm/yyyy hh:mm:ss là tham số thời gian tự động mở khóa Soft OTP tại hệ thống Soft OTP.

Tắt thông báo về màn hình Thay đổi thông tin tích lũy định kỳ

 | 3 | Soft OTP đang bị khóa (Lock) | Tài khoản của Quý khách đang bị khóa xác thực Soft OTP. Quý khách vui lòng kiểm tra lại hoặc liên hệ tổng đài Co-op Bank xxxxx để được hỗ trợ. | 
Tắt thông báo về màn hình Thay đổi thông tin tích lũy định kỳ

• Hợp lệ: Chuyển bước 2
2/ Sinh mã Soft OTP theo thuật toán quy định và kiểm tra mã Soft OTP do client gửi lên

• Không hợp lệ | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Mã Soft OTP không đúng (sai thông tin sinh mã giữa client và Soft OTP Server) | Xác thực giao dịch không thành công do sai dữ liệu Soft OTP. Quý khách vui lòng liên hệ chi nhánh/phòng giao dịch gần nhất để được hỗ trợ hoặc liên hệ: xxxxxx | 

• Hợp lệ: Trả kết quả thành công cho MB
 | MB | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo tương ứng
• Thành công: Gửi yêu cầu xác nhận giao dịch sang Bank qua API: changeRdAccountInfor (chỉ truyền những thông tin thay đổi, những thông tin không thay đổi truyền Null)
 | Bank | 
Xử lý và trả kết quả cho MB

 | MB | 
Nhận kết quả

• Không thành công: Hiển thị thông báo lỗi tương ứng 
• Thành công: Hiển thị MH7

##### MH7: Kết quả
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn "Đóng" | MB  | Quay về màn hình danh sách tài khoản/ Danh sách tiết kiệm (tùy vào luồng truy cập chức năng)

---


