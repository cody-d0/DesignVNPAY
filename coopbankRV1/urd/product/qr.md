# 📋 QR Pay & QR Napas

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `product/`
> **Trích xuất:** 2026-03-28

---

## 17. URD_MB_COOPBANK_QRPAY

> **Page ID:** `37654602` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37654602

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*10 trang con:*

### 17.1. Màn hình chức năng quét QR

> **Page ID:** `37654733` · **Version:** 7
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37654733

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client MB
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công
• Thiết bị sử dụng có hỗ trợ camera
• Kết quả mong muốn:
• KH thực hiện quét được QR (QR chuyển tiền, QR type1, QR type 2, QR type 3, QR type 4)
• Xem Danh sách đơn vị hỗ trợ
• Xem và lưu được ảnh MyQR
#### 2/ Luồng màn hình

##### MH1: Màn hình Quét QR

##### MH2: Màn hình Đơn vị hỗ trợ

##### MH3: Màn hình hướng dẫn

#### Mô tả:

Tại màn hình home, chọn chức năng QRPay -> Chuyển sang màn hình Quét QR

##### MH1: Màn hình quét QR
 | TT | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Quét mã QR

 | 
2
 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 
3
 | 
Text ghi chú
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Fix tại client:

Di chuyển camera đến vùng chứa mã QR, tiến trình quét mã diễn ra tự động

 | 4 | Logo nhận diện thương hiệu | image | Readonly | -- | -- | Logo ngân hàng Co-opBank, logo của VNPAY và logo Napas247
 | 5 | 
Vùng Camera
 | 
--
 | 
--
 | -- | -- | 
Vùng camera quét ảnh QR

 | 6 | 
Icon Flash
 | 
Icon
 | 
Click
 | -- | -- | 
Khi chưa bật flash thì icon ở chế độ ON 

Khi bật flash thì icon ở chế độ OFF

 | 7 | Thư viện ảnh | Icon | Click | 
 | 
 | Nhấn icon -> Tham chiếu logic xử lý
 | 
Nút chức năng

 | 8 | QR thanh toán | Icon | Click | 
 | 
 | Nhấn icon -> Tham chiếu logic xử lý
 | 9 | Đơn vị hỗ trợ | Icon | Click | 
 | 
 | Nhấn icon -> Tham chiếu logic xử lý
 | 10 | Lịch sử giao dịch | Icon | Click | 
 | 
 | Nhấn icon -> Tham chiếu logic xử lý
 | 11 | Hướng dẫn | Icon | Click | 
 | 
 | Nhấn icon -> Tham chiếu logic xử lý
 | 12 | Tạo mã QR chuyển khoản | Button | Click | 
 | 
 | Nhấn nút -> Tham chiều logic xử lý

##### MH2: Màn hình đơn vị hỗ trợ
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
 | -- | -- | 
Tiêu đề: Đơn vị hỗ trợ

 | 
2
 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | Icon home | Icon | Click | -- | -- | Nhấn icon, xử lý quay về màn hình home
 | 4 | Ô textsearch | Textbox | Input | 
 | 
 | 
Cho phép tìm kiếm gần đúng theo các trường thông tin: Loại hình kinh doanh, Tên cửa hàng, Địa chỉ.

Hiển thị dấu "x" cho phép xóa toàn bộ các ký tự đã nhập khi focus vào ô.

 | 
5
 | 
Danh sách các điểm chấp nhận thah toán QR
 | 
List
 | 
Click
 | -- | -- | 
Gồm 2 tab: Điểm thanh toán Offline và Điểm thanh toán Online

• Điểm thanh toán Offline: Danh sách các điểm chấp nhận thanh toán QR offline
• Điểm thanh toán Offline: Danh sách các điểm chấp nhận thanh toán QR online
Mặc định focus tab Điểm thanh toán Offline

##### MH3: Màn hình hướng dẫn
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
Hiển thị text "Hướng dẫn"

 | 
2
 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó.

 | 3 | Nội dung hướng dẫn | Label | View | -- | - | 
Hiển thị nội hướng dẫn QR là link HTML được tích hợp tại client.

#### 3/ Luồng xử lý

##### Tại màn hình home, chọn chức năng "Dịch vụ QR", client kiểm tra quyền thao tác dịch vụ của khách hàng:

• Nếu dịch vụ sử dụng không thuộc gói dịch vụ của khách hàng, thông báo lỗi: "Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ."
• Nếu ứng dụng chưa có quyền truy cập camera, hiển thị thông báo "Quý khách vui lòng cho phép ứng dụng truy cập Camera để thực hiện chức năng quét mã QR." và 2 nút "Đồng ý", "Không phải bậy giờ" (2 button tùy theo yêu cầu thiết bị)
MH1: Màn hình quét QR
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Nhấn bật/tắt icon flash | Client MB | Xử lý bật/tắt đèn flash trên thiết bị
 | 2 | Thực hiện quét 1 QR hoặc chọn 1 ảnh từ Thư viện ảnh | Client MB | 
Kiểm tra quyền truy cập camera của thiết bị: Nếu chưa quyền có hiển thị thông báo theo thiết bị hiện tại

 | 
SDK
 | 
Đọc và giải mã trường thông tin trên mã QR theo thuật toán

• Nếu hợp lệ, trả kết quả các trường dữ liệu trong QR cho App CLient
• Nếu không hợp lệ, trả kết quả lỗi cho App Client hiển thị thông báo lỗi tương ứng với các trường hợp sau: Ảnh không phải mã QR hoặc QR không đúng định dạng hỗ trợ trên SDK (chuẩn EMV Co/chuẩn VNPAY-QR).
 | Client MB | 
Nhận kết quả:

• Thành công:(QR chuyển khoản, QR thanh toán) -> Gửi yêu cầu lấy danh sách tài khoản nguồn sang server 
• 
Không thành công: Hiển thị thông báo lỗi:
 | STT | Case | Thông báo | 

 | 1 | Ảnh không phải mã QR hoặc QR không đúng định dạng hỗ trợ trên SDK (chuẩn EMV Co/chuẩn VNPAY-QR) | Mã QR không hợp lệ. Quý khách vui lòng kiểm tra lại. | 

 | MB server | Nhận và gửi yêu cầu lấy danh sách tài khoản thanh toán qua bank server
 | Bank server | Xử lý và phản hồi lại MB server
 | MB server | Nhận và gửi phản hồi lại Client
 | Client MB | 
Nhận phản hồi:

• Trường hợp không có tài khoản thanh toán (đã tất toán hết tài khoản thanh toán), hiển thị thống báo dạng popup "Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại!"
• Có tài khoản thanh toán → Hiển thị màn hình Thông tin thanh toán tương ứng
 | 3 | Nhấn icon QR thanh toán | 
Client MB
 | 
Thực hiện gen mã qr theo tài khoản nguồn mặc định hiện tại đang hiển thị tại màn hình home và hiển thị màn hình QR thanh toán

 | 4 | Nhấn icon Đơn vị hỗ trợ | Client MB | Hiển thị màn hình Đơn vị hỗ trợ
 | 5 | Nhấn icon Thư viện ảnh | Client MB | 
Kiểm tra quyền truy cập Thư viện ảnh trên thiết bị:

• Nếu chưa có quyền: Hiển thị thông báo "Quý khách vui lòng cho phép ứng dụng truy cập thư viện ảnh để thực hiện chức năng quét mã QR.". Khách hàng nhấn:
• Đồng ý: Truy cập thư viện ảnh, cho phép khách hàng chọn ảnh đã lưu trên thiết bị.
• Hủy: Đóng câu thông báo và giữ nguyên màn hình hiện tại.
• Nếu đã có quyền: Truy cập thư viện ảnh, cho phép khách hàng chọn ảnh đã lưu trên thiết bị.
 | 6 | Nhấn icon Hướng dẫn | Client MB | Hiển thị màn hình Hướng dẫn
 | 7 | Nhấn icon Lịch sử giao dịch | Client MB | Hiển thị màn hình chức năng Lịch sử thanh toán QR
 | 8 | Nhấn "Tạo mã QR chuyển khoản" | Client MB | 
Chuyển sang màn hình Tạo mã QR napas

<Tham khảo chi tiết tại >

---

### 17.2. Gen QR thanh toán

> **Page ID:** `40653917` · **Version:** 11
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/40653917

##### Ghi chú: Tài liệu URD gen QR thanh toán được phân tích dựa trên tài liệu BANK SOW_QRCustomerPresented_v1.0.0_final

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client MB, MB Server, Bank Server.
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công;
• KH có tài khoản thanh toán hợp lệ để gen QR.
• Kết quả mong muốn:
• KH tạo mã QR thanh toán thành công
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

##### MH1: Màn hình quét QR

##### MH2: Màn hình gen QR thanh toán

##### MH3: Màn hình cập nhật QR thanh toán theo mã giảm giá

(Thông báo tự động tắt/ẩn sau 3 giây

##### MH4: Màn hình cập nhật lại bỏ mã giảm

(Thông báo tự động tắt/ẩn sau 3 giây)

#### Mô tả màn hình:

##### MH1: Màn hình quét QR

• Xem mô tả màn hình tại màn hình chức năng Quét QR
##### MH2/3/4: Màn hình QR thanh toán
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | 
Label
 | 
Read Only
 | 

 | 
--
 | QR thanh toán
 | 2 | Icon Back | 
Icon
 | 
Click
 | 

 | -- | Nhấn Back, quay về màn hình thao tác trước đó 
 | Thông tin giao dịch
 | 1 | 
Ghi chú 1
 | Label | Read Only | -- | -- | 
Fix tại client:

"MÃ QR DÙNG CHO THANH TOÁN

Vui lòng đưa mã VNPAY - QR cho điểm bán để thực hiện quét và thanh toán cho đơn hàng của Quý khách."

 | 2 | Mã giảm giá (Nếu có) | Textbox | Input | -- | 20 | 
Mặc định trống, nhập ký tự không dấu, không bao gồm các ký tự đặc biệt

 | 3 | Icon Tạo mã QR | Icon | Click | -- | -- | <Tham khảo logic xử lý>
 | 4 | Ghi chú 2 | Label | Read Only | -- | -- | 
Fix tại client:

"Nhập mã giảm giá để áp dụng cho đơn hàng"

 | 5 | Ảnh QR | Picture | View | -- | -- | 
Ảnh QR do client hiển thị

 | 6 | 
Thông tin mô tả QR
 | Label | Read Only | -- | -- | 
Hiển thị bao gồm các thông tin do client fix:

• Tên chủ tài khoản: Lấy từ thông tin tài khoản
• Thời gian hết hạn theo định dạng hh:mm dd/mm/yyyy 
 | Nút thao tác
 | 1 | Lưu ảnh | 

 | 

 | 

 | -- | <Tham khảo logic xử lý>
 | 2 | Chia sẻ | 
 | 
 | 
 | 
 | <Tham khảo logic xử lý>

##### MH4: Màn hình popup chọn lại tài khoản nguồn gen QR thanh toán
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | 
Label
 | 
Read Only
 | 

 | 
--
 | Danh sách tài khoản thanh toán
 | 2 | Icon Đóng | 
Icon
 | 
Click
 | 

 | -- | Nhấn nút, đóng màn hình popup
 | Thông tin hiển thị
 | 1 | tài khoản nguồn | 
List
 | 
Click
 | 

 | -- | 
Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Đánh dấu tích nhận biết tài khoản đang được chọn

#### 4/ Luồng xử lý

##### Truy cập chức năng:
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 |  Đi từ màn hình Quét QR
 | 
1
 | 
Tại màn hình quét QR, nhấn icon "QR thanh toán"
 | 
Client MB
 | 
Client thực hiện gen QR theo tài khoản thanh toán mặc định đã lấy lúc đăng nhập và hiển thị màn hình QR thanh toán

• Lưu ý:
• Client thực hiện gen chuỗi QR theo định dạng QR được quy định
• Thời gian hiệu lực của QR là 15p, tính từ lúc Client thực hiện gen
• Trường hợp KH thoát khỏi màn hình QR thanh toán sau đó chọn Gen lại QR, cho phép Client gen lại mã QR mới và thời gian hiệu lực được reset lại

##### MH2/3/5: Màn hình QR thanh toán
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhập mã giảm giá và nhấn icon "Tạo mã QR" | 
Client MB
 | 
Client thực hiện gen QR theo mã giảm giá KH đã nhập, hiển thị như mô tả màn hình 4

Lưu ý:

• Client thực hiện gen chuỗi QR theo định dạng QR được quy định
• Thời gian hiệu lực của QR là 15p, tính từ lúc Client thực hiện gen
• Trường hợp KH thoát khỏi màn hình QR thanh toán sau đó chọn Gen lại QR, cho phép Client gen lại mã QR mới (tài khoản nguồn là tài khoản thanh toán mặc định, mã giảm giá trống và thời gian hiệu lực được reset lại)
• TH bỏ trống mã giảm giá: Cho phép Client gen 1 mã QR mới
 | 2 | Nhấn "Lưu ảnh" | Client MB | Tham khảo tại Logic xử lý chung
 | 3 | Nhấn "Chia sẻ" | Client MB | Tham khảo tại Logic xử lý chung

---

### 17.3. Nhận thông tin OTT và thực hiện thanh toán

> **Page ID:** `40654656` · **Version:** 31
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/40654656

##### Ghi chú: Tài liệu URD QR thanh toán được phân tích dựa trên tài liệu BANK SOW_QRCustomerPresented_v1.0.0_final

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client,M B Server , Merchant App, Hệ thống MMS VNPAY, Hệ thống OTT
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công;
• KH đã gen QR thành công 
• App merchant đáp ứng các yêu cầu thỏa mãn để có thể đọc mã qr mà KH đã gen
• Kết quả mong muốn:
• KH thực hiện thanh toán giao dịch thành công
• Remark: [Tên KH] TT QRPay tại [Tên điểm bán] với mã [Số hóa đơn] trên Co-opBank Mobile banking 
#### 2/ Luồng sơ đồ

#### 3/ Luồng màn hình

#### Mã giảm giá hợp lệ

##### MH1: Hiển thị thông báo trên màn hình khi khóa thiết bị

##### MH2: Hiển thị tại màn hình quản lý thông báo

##### MH3: Hiển thị tại màn hình đang trong phiên làm việc - nhấn xem tin notify

#### Mã giảm giá không hợp lệ

##### MH1: Hiển thị thông báo trên màn hình khi khóa thiết bị

##### MH2: Hiển thị tại màn hình quản lý thông báo

##### MH3: Hiển thị tại màn hình đang trong phiên làm việc - nhấn xem tin notify

#### Luồng giao dịch

##### MH4: Xác nhận giao dịch

##### MH6: Màn hình kết quả

#### Mô tả màn hình:

##### MH1: Hiển thị thông báo trên màn hình khi khóa thiết bị
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Thông tin bank
 | 
--
 | 
ReadOnly
 | 
 | -- | 
Logo bank + tên ứng dụng

 | 2 | Nội dung tin | Label | ReadOnly | 
 | -- | 
Hiển thị nội dung tin:

"Thông báo Co-opbank: Quý khách có yêu cầu thanh toán từ điểm bán [Tên điểm bán]

• Số hóa đơn: [Số hóa đơn]
• Số tiền: [Số tiền thanh toán] -> (chỉ hiển thị khi nhập mã giảm giá)
• Số tiền giảm giá ([Mã giảm giá]): [Số tiền được giảm] -> (chỉ hiển thị khi nhập mã giảm giá)
• Số tiền thanh toán: [Số tiền thanh toán đã trừ số tiền được giảm VND]
• Ghi chú: [Nội dung ghi chú từ App Merchant nhập]
• Thời gian giao dịch: [hh:mm dd/mm/yyyy]
• Thời gian hết hạn: [hh:mm dd/mm/yyyy]
• [Nội dung mã giảm giá không hợp lệ]: (thông báo lỗi cụ thể mã giảm giá do hệ thống MMS trả về nếu có )
Cho phép nhấn chọn để mở app, truy cập chức năng Thông báo và hiển thị màn hình chi tiết tin <c.Hiển thị tại màn hình quản lý thông báo>

Tin hiển thị dạng banner trên thiết bị

##### MH2: Hiển thị tại màn hình quản lý thông báo <Hiển thị mặc định tại mục tin khác/Tất cả>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Nội dung tin
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Hiển thị nội dung tin:

"Quý khách có yêu cầu thanh toán từ điểm bán [Tên điểm bán]

• Số hóa đơn: [Số hóa đơn]
• Số tiền: [Số tiền thanh toán] -> (chỉ hiển thị khi nhập mã giảm giá)
• Số tiền giảm giá ([Mã giảm giá]): [Số tiền được giảm] -> (chỉ hiển thị khi nhập mã giảm giá)
• Số tiền thanh toán: [Số tiền thanh toán đã trừ số tiền được giảm VND]
• Ghi chú: [Nội dung ghi chú từ App Merchant nhập]
• Thời gian giao dịch: [hh:mm dd/mm/yyyy]
• Thời gian hết hạn: [hh:mm dd/mm/yyyy]
• [Nội dung mã giảm giá không hợp lệ]:  (thông báo lỗi cụ thể mã giảm giá do hệ thống MMS trả về )
 | 2 | Thanh toán | Button | Click | -- | -- | Mặc định enable <Tham khảo logic xử lý>

##### MH3: Hiển thị tại màn hình đang trong phiên làm việc - Khi KH click vào tin notify
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Thông báo

 | 2 | Nội dung tin | Label | ReadOnly | -- | -- | 
Hiển thị nội dung tin:

"Quý khách có yêu cầu thanh toán từ điểm bán [Tên điểm bán]

• Số hóa đơn: [Số hóa đơn]
• Số tiền: [Số tiền thanh toán] -> (chỉ hiển thị khi nhập mã giảm giá)
• Số tiền giảm giá ([Mã giảm giá]): [Số tiền được giảm] -> (chỉ hiển thị khi nhập mã giảm giá)
• Số tiền thanh toán: [Số tiền thanh toán đã trừ số tiền được giảm VND]
• Ghi chú: [Nội dung ghi chú từ App Merchant nhập]
• Thời gian giao dịch: [hh:mm dd/mm/yyyy]
• Thời gian hết hạn: [hh:mm dd/mm/yyyy]
• [Nội dung mã giảm giá không hợp lệ]: (thông báo lỗi cụ thể mã giảm giá do hệ thống MMS trả về nếu có )
 | 3 | Để sau | Button | Click | -- | -- | 
Mặc định enable <Tham khảo logic xử lý>

 Nhấn Để sau, tắt popup và hiển thị màn hình đang thao tác

 | 4 | Thanh toán | Button | Click | -- | -- | Mặc định enable <Tham khảo logic xử lý>

##### MH4: Màn hình Xác nhận giao dịch
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Thông báo

 | 2 | Icon back | Icon | Click | -- | -- | Nhấn nút, xử lý quay về màn hình thao tác trước đó
 | Thông tin giao dịch
 | 1 | 
Tài khoản nguồn
 | 
Label
 | 
ReadOnly
 | -- | -- | Là tài khoản nguồn mặc định, lấy từ MB Server
 | 2 | 
Tên điểm bán
 | 
Label
 | 
ReadOnly
 | -- | -- | Thông tin từ màn OTT
 | 3 | 
Số hóa đơn
 | 
Label
 | 
ReadOnly
 | -- | -- | Thông tin từ màn OTT, bôi đỏ
 | 4 | 
Số tiền 
 | 
Label
 | 
ReadOnly
 | -- | -- | Thông tin từ màn OTT, hiển thị nếu có nhập Mã giảm giá
 | 5 | 
Số tiền giảm giá <Nếu có mã giảm giá hợp lệ>
 | 
Label
 | 
ReadOnly
 | -- | -- | Thông tin từ màn OTT, hiển thị nếu có nhập Mã giảm giá
 | 6 | 
Số tiền thanh toán
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Thông tin từ màn OTT

 | 7 | Phí giao dịch và thuế | 
Label
 | 
ReadOnly
 | -- | -- | Giá trị do server trả về (chỉ hiển thị nếu khác 0 hoặc rỗng)
 | 8 | Ghi chú | 
Label
 | 
ReadOnly
 | -- | -- | Thông tin từ màn OTT
 | 9 | Chọn phương thức xác thực | Combobox | Select | 
 | 
 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | Nút chức năng
 | 1 | Xác nhận | Button | Click | 
 | 
 | Nhấn nút, tham khảo logic xử lý

##### MH5: Xác thực giao dịch

Xem tại màn hình xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH6: Kết quả giao dịch
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
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

• Logo Co-opbank
•  Icon thành công (nút tích trong nền tròn xanh để riêng một dòng)
• Thanh toán thành công
•  Số tiền bằng số + đơn vị tiền tệ
• Thời gian giao dịch
• Tài khoản nguồn
• Tên điểm bán
• Số hóa đơn
• Mã giao dịch
 | 4 | 
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
Nhấn icon nút chia sẻ → Tham khảo logic xử lý

 | 5 | Lưu ảnh | Icon | Click | -- | -- | Nhấn icon chụp ảnh màn hình → Tham khảo logic xử lý
 | 
6
 | 
Tạo mới giao dịch
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon tạo giao dịch mới → Tham khảo logic xử lý

#### 4/ Luồng xử lý

##### Nhận tin OTT:
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | Quét mã QR từ Merchant App
 | 1 | Seller dùng Merchant app để quét mã QR của KH | Hệ thống Merchant app | 
Đọc thông tin QR, kiểm tra thời gian hiệu lực của mã QR và hiển thị màn hình thanh toán

Thực hiện đọc thông tin QR, kiểm tra thời gian hiệu lực của QR:

• Hợp lệ: Hiển thị màn hình thanh toán
• Không hợp lệ: Hiển thị thông báo lỗi tương ứng với merchant app (thông báo lỗi do SDK QR trả về)
 | 2 | Seller nhập Số tiền giao dịch và nhấn Tiếp tục

 | Hệ thống Merchant app | 
Gọi API check sang hệ thống MMS VNPAY để kiểm tra thông tin MID/TID/ CTKM 

• Thành công: Hiển thị thông báo gửi yêu cầu thành công
• Không hợp lệ: Hiển thị thông báo lỗi tương ứng với merchant app
 | Hệ thống MMS VNPAY | 
Nhận yêu cầu và thực hiện kiểm tra thông tin:

• Thành công: Gửi nội dung OTT bao gồm thông tin giao dịch + CTKM (nếu có) sang hệ thống OTT
• Không thành công: Trả về kết quả cho Merchant app (tham khảo bảng mã lỗi thanh toán chung)
 | Hệ thống OTT | Nhận nội dung và gửi tin OTT tới App client 
 | 
App client
 | 
Nhận thông tin push từ Hệ thống OTT và thực hiện kiểm tra trạng thái sử dụng app và hiển thị màn hình thông báo tương ứng

• KH đang không sử dụng app: Thực hiện cơ chế gửi tin offline: Hiển thị thông báo trên màn hình khi khóa thiết bị
• KH đang đăng nhập và sử dụng app: Hiển thị tại màn hình đang trong phiên làm việc
Lưu ý:

Các tin Notify khi được gửi đều được lưu tại chức năng Thông báo của App. KH có thể truy cập vào chức năng Thông báo để xem tin đã gửi tại màn hình quản lý thông báo

##### MH1: KH thực hiện thanh toán khi nhận tin khi khách hàng không đăng nhập ứng dụng
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
Nhận và nhấn vào tin Notify yêu cầu thanh toán tại màn hình thiết bị khi chưa mở khóa thiết bị
 | 
client MB
 | 
Mở app và điều hướng vào màn hình tin OTT theo logic nghiệp vụ xử lý chức năng tin OTT hiện tại

 | 2 | Nhấn "Thanh toán" trên màn hình tin OTT | client MB | 
Hiển thị thông báo : "Quý khách vui lòng đăng nhập để thực hiện thanh toán.", giá trị lựa chọn:

• Nút Hủy: Nhấn Hủy, tắt thông báo hiển thị màn hình đang thao tác
• Nút Đồng ý: Nhấn Đồng ý, hiển thị màn hình Đăng nhập. Điều hướng vào màn hình tin OTT, focus vào tin notify vừa thao tác
→  Chuyển tiếp luồng Thanh toán từ chức năng Thông báo

##### MH3: KH thực hiện thanh toán khi nhận tin khi khách hàng đăng nhập ứng dụng
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
Nhấn "Thanh toán" tại popup notify
 | 
Client MB
 | 
Kiểm tra Số hóa đơn - Merchant đã được thanh toán hay chưa

• Đã thanh toán: Hiển thị thông báo lỗi | | 
TT
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Số hóa đơn - Merchant đã được thanh toán | Đơn hàng đã được thanh toán. Quý khách vui lòng kiểm tra lại. | 

• Chưa thanh toán: Gửi yêu cầu khởi tạo sang MB Server theo thông tin tại tin OTT
• Lưu ý: 
• Lấy STK nguồn mặc định để truyền vào hàm khởi tạo. Trong đó cập nhật thêm các thông tin:
• 
"typeSource"// Loại nguồn thanh toán, giá trị mặc định "Trống". Bao gồm các quy định giá trị sau:

• 
01: Tài khoản nội địa

• 
02: Visa

• 
04: Unionpay

• 
05: Master

• 
06: JCB

• 
07: Thẻ nội địa

• 
08: Tài khoản ví

• 
"bankCard"// Loại thẻ thanh toán, giá trị mặc định "Trống". Trường này là bắt buộc nếu "typeSource" thuộc 1 trong các giá trị 02, 04, 05, 06 và bao gồm các giá trị sau:

• 
01: Thẻ tín dụng nội địa

• 
02: Thẻ tín dụng quốc tế

• 
03: Thẻ ghi nợ quốc tế

 | MB Server | 
1/ Thực hiện kiểm tra thời gian giao dịch theo quy tắc:

• Thời gian hiện tại của thiết bị =< thời gian hết hạn thanh toán (15 phút tính từ lúc merchent quét QR, do hệ thống OTT trả về)→ Giao dịch còn thời hạn thanh toán, chuyển bước 2
• Thời gian hiện tại của thiết bị > thời gian hết hạn thanh toán (15 phút tính từ lúc merchent quét QR, do hệ thống OTT trả về)→ Giao dịch đã hết thời hạn thanh toán, trả về thông báo "Giao dịch đã hết hạn thanh toán, quý khách vui lòng thực hiện giao dịch khác"
2/ Thực hiện khởi tạo giao dịch theo tài khoản nguồn là tài khoản thanh toán mặc định mà KH đã cài đặt và Chuyển tiếp luồng Thanh toán giao dịch <tham khảo luồng logic tại Luồng thanh toán giao dịch>

##### MH2: KH thực hiện thanh toán từ chức năng Thông báo
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
Nhấn "Thanh toán" tại tin OTT
 | 
App client
 | 
1/ Kiểm tra trạng thái đăng nhập:

• Ngoài phiên đăng nhập: Hiển thị thông báo yêu cầu đăng nhập "Quý khách vui lòng đăng nhập ứng dụng để thực hiện giao dịch.". Đóng câu thông báo, hiển thị màn hình login của app Mobile banking Co-opbank. Login thành công, hiển thị màn hình thông tin OTT, focus vào tin KH vừa nhấn Thanh toán. <Luồng thanh toán khi nhận tin Offline>
• Trong phiên đăng nhập: Chuyển bước tiếp theo
2/ Kiểm tra Số hóa đơn - Merchant đã được thanh toán hay chưa (kiểm tra theo thông tin Ngày hết hạn server có trả về)

• Đã thanh toán: Hiển thị thông báo lỗi | | 
TT
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 1 | Số hóa đơn - Merchant đã được thanh toán | Đơn hàng đã được thanh toán. Quý khách vui lòng kiểm tra lại. | 

• Chưa thanh toán: Gửi yêu cầu sang bank lấy thông tin số dư khả dụng, sau khi nhận được phản hồi bank trả về thực hiện gửi yêu cầu khởi tạo sang MB Server theo thông tin tại tin OTT
• 
• Lưu ý: 
• Lấy STK nguồn mặc định để truyền vào hàm khởi tạo. Trong đó cập nhật thêm các thông tin:
• 
"typeSource"// Loại nguồn thanh toán, giá trị mặc định "Trống". Bao gồm các quy định giá trị sau:

• 
01: Tài khoản nội địa

• 
02: Visa

• 
04: Unionpay

• 
05: Master

• 
06: JCB

• 
07: Thẻ nội địa

• 
08: Tài khoản ví

• 
"bankCard"// Loại thẻ thanh toán, giá trị mặc định "Trống". Trường này là bắt buộc nếu "typeSource" thuộc 1 trong các giá trị 02, 04, 05, 06 và bao gồm các giá trị sau:

• 
01: Thẻ tín dụng nội địa

• 
02: Thẻ tín dụng quốc tế

• 
03: Thẻ ghi nợ quốc tế

 | MB Server | 
1/ Thực hiện kiểm tra thời gian giao dịch theo quy tắc:

• Thời gian hiện tại của thiết bị =< thời gian hết hạn thanh toán (15 phút tính từ lúc merchent quét QR, do hệ thống OTT trả về)→ Giao dịch còn thời hạn thanh toán, chuyển bước 2
• Thời gian hiện tại của thiết bị > thời gian hết hạn thanh toán (15 phút tính từ lúc merchent quét QR, do hệ thống OTT trả về)→ Giao dịch đã hết thời hạn thanh toán, trả về thông báo "Giao dịch đã hết hạn thanh toán, quý khách vui lòng thực hiện giao dịch khác"
2/ Thực hiện khởi tạo giao dịch theo tài khoản nguồn là tài khoản thanh toán mặc định mà KH đã cài đặt và Chuyển tiếp luồng Thanh toán giao dịch <tham khảo luồng logic tại Luồng thanh toán giao dịch>

##### Luồng thanh toán giao dịch:
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | Khởi tạo giao dịch
 | 1

 | MB Server thực hiện khởi tạo giao dịch (tiếp các luồng ở trên)

 | Client MB | Gửi yêu cầu lấy lại danh sách số dư tài khoản và hiển thị màn hình khởi tạo mặc định ban đầu của chức năng
 | MB Server | 
Nhận kết quả 

• Hợp lệ, kiểm tra hạn mức gói dịch theo loại giao dịch tương ứng. → Tham khảo logic xử lý tại Logic kiểm tra PTXT. Gửi phản hồi lại client
• Không hợp lệ, gửi kết quả lại cho client
 | Client MB | 
Nhận kết quả:

• Hợp lệ: Hiển thị màn hình xác nhận giao dịch
• Không hợp lệ: Hiển thị thông báo lỗi như Server trả về, đóng thông báo giữ nguyên màn hình thao tác trước đó

##### MH4: Xác nhận giao dịch
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhấn "Tiếp tục"

 | Client MB | 
Chuyển sang màn hình xác thực giao dịch theo phương thức xác thực tương ứng đã chọn:

• Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)
• Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)
• Nếu phương thức xác thực là vân tay → Gửi yêu cầu xác thực giao dịch (Tham khảo logic xử lý tại Xác thực bằng Touch ID/Face ID)
Lưu ý: Nếu gặp các lỗi ở bước này, hiển thị thông báo lỗi tương ứng tới KH và xử lý điều hướng như sau:
 | STT | Case | Thông báo | Xử lý
 | 1 | Giao dịch hết hiệu lực | Hiển thị thông báo như quy định của luồng GD tài chính trên hệ thống hiện tại | 
Đóng câu thông báo, điều hướng về màn hình trước đó đã thực hiện thanh toán

 | SMS
 | 2 | SMS OTP hết hiệu lực | Hiển thị thông báo như quy định của PTXT SMS OTP trên hệ thống hiện tại
 | 3 | Nhập SMS OTP sai quá số lần | Hiển thị thông báo nh

> ⚠️ *Nội dung đã cắt ngắn (18272 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 17.4. Lịch sử thanh toán QR

> **Page ID:** `40641973` · **Version:** 17
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/40641973

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client, MB Server
• Điều kiện trước: 
• KH đăng nhập ứng dụng thành công.
• KH đã thực hiện ít nhất 1 giao dịch thanh toán QR thành công
• Kết quả mong muốn:
• KH xem được danh sách và chi tiết các giao dịch thanh toán QR thành công.
#### 2/ Luồng màn hình

##### MH1: Màn hình lịch sử thanh toán QR -  Chưa phát sinh giao dịch

##### MH2: Màn hình lịch sử thanh toán QR

##### MH3: Chi tiết QR offline

##### MH4: Chi tiết QR billing

##### MH5: Chi tiết QR sản phẩm

##### MH6: CHi tiết QR cổng

##### MH7: CHi tiết QR thanh toán

#### Mô tả màn hình:

##### MH1/2: Màn hình lịch sử thanh toán QR
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Lịch sử thanh toán QR

 | 
2
 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | Icon Home | 
Icon
 | 
Click
 | -- | -- | Nhấn Home, Hiển thị màn hình trang chủ
 | 4 | Textsearch | Textsearch | Input | 
 | 
 | 
Cho phép tìm kiếm full text dữ liệu nhập vào theo thông tin hiển thị của từng row (thời gian, tên điểm bán, số tiền)

Có dấu x cho phép xóa toàn bộ ký tự đã nhập

 | 
5
 | 
Danh sách giao dịch thanh toán QR
 | 
List
 | 
Click
 | -- | -- | 
Hiển thị danh sách giao dịch thanh toán QR gần nhất, hiển thị các thông tin:

• Tên điểm bán: Nếu tên điểm bán dài quá thì hiển thị ba chấm.
• Thời gian giao dịch: định dạng dd/mm/yyyy hh:mm
• Số tiền giao dịch
Lưu ý:

• Nếu không có giao dịch, hiển thị màn hình danh sách trống theo design.
• Nếu có giao dịch thứ tự hiển thị giảm dần theo Thời gian giao dịch
• KH vuốt lên sẽ hiển thị tiếp GD tiếp theo (Tối đa 30 giao dịch gần nhất)

##### MH3/4/5/6/7: Màn hình chi tiết giao dịch thanh toán QR
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Chi tiết giao dịch

 | 
2
 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 3 | Icon Home | 
Icon
 | 
Click
 | -- | -- | Nhấn Home, Hiển thị màn hình trang chủ
 | 4 | Thông tin chi tiết giao dịch | Label | ReadOnly | 
 | 
 | 
Hiển thị bao gồm các thông tin sau:

1/ Đối với QR cho điểm Offline (type 1)

• Tài khoản nguồn
• Thanh toán tại
• Mã điểm bán
• Tên điểm bán
• Số hóa đơn
• Số tiền
• Số tiền giảm (nếu có)
• Số tiền thanh toán (nếu có số tiền giảm)
• Phí giao dịch và thuế
• Ghi chú
• Ngày giao dịch (định dạng dd/mm/yyyy hh:mm)
2/ Đối với QR billing (type 2)

• Tài khoản nguồn
• Nhà cung cấp
• Dịch vụ
• Mã khách hàng
• Tên khách hàng
• Số tiền
• Số tiền giảm (nếu có)
• Số tiền thanh toán (nếu có số tiền giảm)
• Phí giao dịch và thuế
• Ngày giao dịch (định dạng dd/mm/yyyy hh:mm)
3/ Đối với QR sản phẩm (type 3)

• Thông tin giao dịch:
• Tài khoản nguồn
• Thanh toán tại
• Tên điểm bán
• Mã điểm bán
• Số hóa đơn
• Số tiền
• Số tiền giảm (nếu có)
• Số tiền thanh toán (nếu có số tiền giảm)
• Phí giao dịch và thuế
• Ngày giao dịch (định dạng dd/mm/yyyy hh:mm)
• Thông tin người nhận:
• Họ và tên người nhận
• Địa chỉ
• Số tiền thoại
• Danh sách sản phẩm:
• Mã sản phẩm
• số lượng
• Đơn giá
• Ghi chú
4/  Đối với QR cổng (type 4)

• Tài khoản nguồn
• Thanh toán tại
• Tên điểm bán
• Số hóa đơn
• Số tiền
• Số tiền giảm (nếu có)
• Số tiền thanh toán (nếu có số tiền giảm)
• Phí giao dịch và thuế
• Mô tả
• Ngày giao dịch (định dạng dd/mm/yyyy hh:mm)
• Thời hạn thanh toán (định dạng dd/mm/yyyy hh:mm)
5/ Đối với QR thanh toán

• Tài khoản nguồn
• Tên điểm bán
• Số hóa đơn
• Số tiền
• Số tiền giảm (nếu có)
• Số tiền thanh toán (nếu có số tiền giảm)
• Phí giao dịch và thuế (nếu có)
• Ghi chú
• Ngày giao dịch (định dạng dd/mm/yyyy hh:mm)

#### 4/ Luồng xử lý

##### Truy cập chức năng:
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Tại màn hình quét QR, nhấn chọn chức năng "Lịch sử quét" | 
Client MB
 | 
Hiển thị màn hình danh sách lịch sử giao dịch QR (lưu tại client)

##### MH1/2: Danh sách lịch sử thanh toán QR
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Nhấn chọn 1 giao dịch | Client MB | 
Hiển thị thông tin chi tiết giao dịch theo loại QR tương ứng đã mô tả ở trên.

---

### 17.5. Thanh toán QR type 1 offus - Điểm bán (Tĩnh và động)

> **Page ID:** `37654981` · **Version:** 16
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37654981

##### Ghi chú: Tài liệu URD thanh toán QR được phân tích dựa trên tài liệu URD_SDK thanh toán QR 1.0.1

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client MB, SDK, MB Server, Bank Server, MMS VNPAY.
• Điều kiện trước: 
• KH đã tải ứng dụng Mobile Banking của Ngân hàng thành công.
• Ứng dụng đã tích hợp bản SDK QR do VNPAY phát triển.
• Tài khoản KH đủ điều kiện thanh toán dịch vụ QR.
• Kết quả mong muốn:
• KH thực hiện thanh toán QR Type 01 (Điểm bán) thành công trên ứng dụng Mobile Banking của Ngân hàng.
• Hệ thống MMS VNPAY ghi nhận giao dịch giao dịch tại các phase thành công.
• Remark: [Tên KH] TT QRPay tại [Tên điểm bán] với mã [Số hóa đơn] trên Co-opBank Mobile banking 
#### 2/ Luồng màn hình

##### a) QR tĩnh

##### MH1: Màn hình quét QR

##### MH2: Màn hình thông tin thanh toán

##### MH3: Màn hình xác nhận thông tin

##### MH4: Màn hình Kết quả giao dịch

##### b) QR động

##### MH1: Màn hình quét QR

##### MH2: Màn hình thông tin thanh toán

##### MH3: Màn hình xác nhận thông tin

##### MH5: Màn hình Kết quả giao dịch

#### Mô tả:

##### MH1: Màn hình quét QR

• Xem tại mô tả 
##### MH2: Màn hình thông tin thanh toán

Việc hiển thị màn hình được xử lý tại App Client, bao gồm các thông tin dựa trên kết quả SDK trả về và do nghiệp vụ App Client đang quy định hiên tại.
 | TT | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tittle | Label | Read only | 
 | 
 | 
Thanh toán QRPAY

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn icon → Xử lý quay về màn hình thao tác trước đó
 | 3 | Tài khoản nguồn | Combobox | Select | Yes | -- | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do bank server trả vềHiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 4 | Thông tin thanh toán | Label | Read only | Yes | 
 | 

 | 5 | Thanh toán tại | Label | Read only | Yes | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 6 | Tên điểm bán | Label | Read only | Yes | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 7 | Mã điểm bán | Label | Read only | Yes | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 8 | 
Số hóa đơn

(QR động)
 | Label | Read only | Yes | 
 | 
Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)

Chỉ hiển thị khi QR được quét là QR động

 | 9 | 
Số tiền

(QR tĩnh)
 | Textbox | Input | Yes | 13 | 
Nhập vào ô số tiền:

• Chỉ cho nhập ký tự số, tối đa 13 ký tự (bao gồm cả dấu phẩy). Không nhập số bắt đầu bằng số 0
• Hiển thị ngăn cách hàng nghìn bằng dấu “,”
• Hiển thị đơn vị tiền tệ mặc định “VND”
• Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo logic xử lý

 | 10 | 
Số tiền

(QR động)
 | Label | Read only | Yes | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 11 | Ghi chú | Textbox | Input | 
 | 
 | 
Cho phép nhập số, chữ không dấu và các ký tự đặc biệt

Hiển thị số ký tự nhập/số ký tự tối đa 250 kí tự

Nhập ghi chú → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

Mặc định là giá trị quét được từ QR

 | 12 | Mã giảm giá (nếu có) | Textbox | Input | 
 | 20 | Mặc định trống, nhập ký tự không dấu, không bao gồm các ký tự đặc biệt
 | 13 | Nút chức năng
 | 14 | Tiếp tục | Button | Click | Yes | 
 | Nhấn nút -> Tham khảo logic xử lý

##### MH3: Màn hình xác nhân thông tin
 | TT | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tittle | Label | Read only | 
 | 
 | 
Xác nhận thông tin

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn icon → Xử lý quay về màn hình thao tác trước đó
 | 
 | Ghi chút | Label | Read only | 
 | 
 | Fix tại client: "Quý khách vui lòng kiểm tra thông tin thanh toán đã khởi tạo"
 | 3 | Tài khoản nguồn | Label | Read only | Yes | 
 | Hiển thị số tài khoản nguồn được chọn từ màn hình trước
 | 4 | Thanh toán tại | Label | Read only | 
 | 
 | 
Hiển thị dữ liệu từ màn hình trước

Hiển thị màu đỏ

 | 5 | Tên điểm bán | Label | Read only | 
 | 
 | Hiển thị dữ liệu từ màn hình trước
 | 6 | 
Số hóa đơn
 | Label | Read only | 
 | 
 | 
Nếu là QR động: Hiển thị dữ liệu từ màn hình trước

Nếu là QR tĩnh: là mã tự tăng trên thông do MB server tự sinh khi khởi tạo GD thành công

Hiển màu đỏ.

 | 7 | Số tiền | Label | Read only | 
 | 
 | 
Hiển thị dữ liệu từ màn hình trước

 | 8 | Số tiền giảm | Label | Read only | 
 | 
 | Chỉ hiển thị khi màn hình trước có nhập mã giá giảm giá
 | 9 | Số tiền thanh toán | Label | Read only | 
 | 
 | 
Giá trịv do MB Server tính = Số tiền thanh toán – Số tiền được giảm giá

Chỉ hiển thị khi có số tiền được giảm giá

Hiển thị số tiền bằng chữ

 | 
 | Phí giao dịch và thuế | Label | Read only | 
 | 
 | Hiển thị dữ liệu do server trả về (chỉ hiển thị nếu khác 0 và rỗng)
 | 10 | Ghi chú | Label | Read only | 
 | 
 | Chỉ hiển thị khi màn hình trước có nhập giá trị ghi chú
 | 11 | Chọn phương thức xác thực | Combobox | Select | Yes | 
 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 12 | Nút chức năng
 | 13 | Xác nhận | Button | Click | 
 | 
 | Nhấn nút -> Tham khảo logic xử lý

##### MH4:Xác thực giao dịch

Xem tại màn hình xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH5: Màn hình  kết quả giao dịch
 | TT | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Logo
 | 
Image
 | 
Read Only
 | 
--
 | 
--
 | 

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

• Logo Co-opbank
•  Icon thành công (nút tích trong nền tròn xanh để riêng một dòng)
• Thanh toán thành công
•  Số tiền bằng số + đơn vị tiền tệ
• Thời gian giao dịch
• Tài khoản nguồn
• Tên đại lý
• Tên điểm bán
• Số hóa đơn
• Mã giao dịch
 | 4 | 
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
Nhấn icon nút chia sẻ → Tham khảo logic xử lý

 | 5 | Lưu ảnh | Icon | Click | -- | -- | Nhấn icon chụp ảnh màn hình → Tham khảo logic xử lý
 | 
6
 | 
Tạo mới giao dịch
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon tạo giao dịch mới → Tham khảo logic xử lý

#### 3/ Luồng xử lý

##### MH1: Màn hình Quét QR
 | TT | Thao tác | Tác nhân | Mô tả
 | 1 | Thực hiện quét mã QR hoặc chọn ảnh QR từ thư viện ảnh | Client MB | 
Kiểm tra quyền thao tác dịch vụ của khách hàng:

• Nếu dịch vụ sử dụng thuộc gói dịch vụ của khách hàng: Gửi yêu cầu lấy danh sách tài khoản nguồn <Tham chiếu logic lấy danh sách tài khoản nguồn tại màn hình chuyển tiền> và chuyển sang bước SDK giải mã QR
• Nếu dịch vụ sử dụng không thuộc gói dịch vụ của khách hàng, thông báo lỗi: "Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ."
 | 
SDK
 | 
Đọc và giải mã trường thông tin trên mã QR theo thuật toán

• Nếu hợp lệ, trả kết quả các trường dữ liệu trong QR cho App CLient
• Nếu không hợp lệ, trả kết quả lỗi cho App Client hiển thị thông báo lỗi tương ứng với các trường hợp sau: Ảnh không phải mã QR hoặc QR không đúng định dạng hỗ trợ trên SDK (chuẩn EMV Co/chuẩn VNPAY-QR).
 | Client MB | 
Nhận kết quả:

• Thành công: Hiển thị màn hình thông tin thanh toán (MH 2)
• Không thành công: Hiển thị thông báo lỗi:  | STT | Case | Thông báo | 

 | 1 | Ảnh không phải mã QR hoặc QR không đúng định dạng hỗ trợ trên SDK (chuẩn EMV Co/chuẩn VNPAY-QR) | Mã QR không hợp lệ. Quý khách vui lòng kiểm tra lại. | 

##### MH2: Màn hình thông tin thanh toán
 | TT | Thao tác | Tác nhân | Mô tả
 | 1 | Nhấn chọn tài khoản nguồn khác | 
Client MB
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

•  Số tài khoản
•  Số dư khả dụng + đơn vị tiền tệ VND
 | 2

 | Nhấn "Tiếp tục"

 | Client MB | 
Kiểm tra validate:

• Hợp lệ, gửi yêu cầu khởi tạo giao dịch sang MB Server
• Không hợp lệ: Hiển thị thông báo lỗi theo các trường hợp validate tại Client của Ngân hàng (nếu có) | TT | Case | Tác nhân | Nội dung thông báo | Ghi chú
 | 1 | Bỏ trống số tiền (QR tĩnh) | Client | Số tiền không được bỏ trống. Quý khách vui lòng kiểm tra lại. | 

 | MB Server | 
Gửi yêu cầu kiểm tra thông tin QR sang hệ thống MMS VNPAY

 | MMS VNPAY | Kiểm tra thông tin QR, thông tin mã giảm giá (nếu có) và trả kết quả về cho  Server
 | MB Server | 
Nhận kết quả 

• Hợp lệ, kiểm tra hạn mức gói dịch theo loại giao dịch tương ứng và tính phí giao dịch. → Tham khảo logic xử lý tại Logic kiểm tra PTXT. Gửi phản hồi lại client
• Không hợp lệ, gửi kết quả lại cho client
 | Client MB | 
Nhận kết quả:

1/ Kết quả kiểm tra thông tin QR

• Hợp lệ, chuyển bước 2
• Không hợp lệ, hiển thị thông báo lỗi tương ứng <tham khảo >
2/ Kết quả kiểm tra thông tin mã giảm giá (nếu có mã giảm giá)

• Hợp lệ, chuyển bước 3
• Không hợp lệ, hiển thị thông báo lỗi tương ứng <tham khảo >
3/ Kiểm tra hạn mức gói dịch theo dịch vụ tương ứng:

• Hợp lệ, hiển thị màn hình xác nhận giao dịch
• Không hợp lệ, thông báo lỗi tương ứng:<Tham khảo >

##### MH3: Màn hình xác nhận thông tin
 | TT | Thao tác | Tác nhân | Mô tả
 | 1 | Nhấn "Xác nhận"

 | Client MB | 
Chuyển sang màn hình xác thực giao dịch theo phương thức xác thực tương ứng đã chọn:

• Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)
• Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)
• Nếu phương thức xác thực là vân tay → Gửi yêu cầu xác thực giao dịch (Tham khảo logic xử lý tại Xác thực bằng Touch ID/Face ID)

##### MH4:Xác thực giao dịch
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
Xử lý:

1/ Kiểm tra hiệu lực của giao dịch:

• Không hợp lệ: Trả mã lỗi tương ứng theo PTXT cho client
• Hợp lệ: Chuyển bước tiếp2/ Gọi bank server hạch toán
 | Bank server | Thực hiện hạch toán và trả kết quả về cho MB server
 | MB server | 
Nhận kết quả: Cập nhật trạng thái giao dịch thành công và gửi kết quả cho MMS VNPAY

 | MMS VNPAY | 
Nhận kết quả:

• Thành công:
• Ghi nhận giao dịch phase 2 thành công
• Kiểm tra/gửi yêu cầu xử lý đơn hàng sang Merchant
• Không thành công:Ghi nhận giao dịch phase 2 không thành công
 | Merchant | Xử lý đơn hàng và trả kết quả về MMS VNPAY
 | MMS VNPAY | 
Nhận kết quả:

• Thành công:
• Ghi nhận giao dịch phase 3 thành công
• Trả kết quả về cho App Server
• Không thành công:
• Ghi nhận giao dịch phase 3 không thành công
• Trả kết quả về cho MB  Server yêu cầu đảo giao dịch
• Timeout: 
• Ghi nhận giao dịch tại phase 3 là Timeout
• Trả kết quả về cho MB Server
 | MB Server | 
Nhận kết quả:

• Phase 3 thành công: Trả kết quả cho App Client hiển thị màn hình kết quả giao dịch
• Phase 3 không thành công: Gửi yêu cầu đảo giao dịch sang Bank Server và nhận kết quả:
• Trả kết quả cho MMS VNPAY ghi nhận giao dịch phase 4 (thành công/không thành công)
• Trả kết quả cho Client MB hiển thị thông báo lỗi xử lý gạch nợ không thành công.
 | Client MB | 
Nhận kết quả:

Thành công: Chuyển sang màn hình kết quả giao dịch

Không thành công: Hiển thị thông báo lỗi tương ứng 
 | | 
Case
 | 
Tác nhân
 | 
Thông báo
 | 
Ghi chú

 | Bank server hạch toán Time out | Client | Xem tại BẢNG MÃ LỖI CHUNG | Đóng câu thông báo và xử lý quay lại màn hình home
 | Thanh toán thất bại (bank server hạch toán thất bại hoặc đã đảo/hoàn tiền cho KH thành công) | Client | Hiển thị thông báo do hệ thống trả về với lỗi tương ứng  | Đóng câu thông báo: Quay lại màn hình khởi tạo, xử lý reset các giá trị khởi tạo trước đó.
 | Time out tại đầu MB server | Client | Xem tại BẢNG MÃ LỖI CHUNG | Đóng câu thông báo: Quay lại màn hình thao tác trước đó, giữ nguyên giá trị khởi tạo trước đó

##### MH5: Màn hình kết quả giao dịch
 | TT | Thao tác | Tác nhân | Mô tả
 | 1 | 
Nhấn Icon home
 | 
Client MB
 | 
Hiển thị màn hình home

 | 2 | 
Nhấn Icon lưu ảnh
 | 
Client MB
 | 
Tham khảo tại Logic xử lý chung

 | 3 | 
Nhấn Nút chia sẻ
 | 
Client MB
 | 
Tham khảo tại Logic xử lý chung

 | 4 | 
Nhấn nút Tạo giao dịch mới
 | 
Client MB
 | 
Gọi lại api chi tiết tài khoản thanh toán vừa thực hiện giao dịch để cập nhật lại số dư tài khoản

Trở lại màn hình quét QR

---

### 17.6. Thanh toán QR type 2 - Hóa đơn

> **Page ID:** `37655484` · **Version:** 13
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37655484

##### Ghi chú: Tài liệu URD thanh toán QR được phân tích dựa trên tài liệu URD_SDK thanh toán QR 1.0.1

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client MB, SDK, MB Server, Hệ thống Billing, Bank Server, MMS VNPAY.
• Điều kiện trước: 
• KH đã tải ứng dụng Mobile Banking của Ngân hàng thành công.
• Ứng dụng đã tích hợp bản SDK QR do VNPAY phát triển.
• Tài khoản KH đủ điều kiện thanh toán dịch vụ QR.
• Kết quả mong muốn:
• KH thực hiện thanh toán QR Type 02– (Hóa đơn) thành công trên ứng dụng Mobile Banking của Ngân hàng.
• Hệ thống MMS VNPAY ghi nhận giao dịch giao dịch tại các phase thành công.
• Remark: [Tên KH] TT QRPay [Tên dịch vụ] của [Nhà cung cấp] với mã KH [Mã khách hàng] trên Co-opBank Mobile banking. (Lưu ý: Tên KH không hiển thị với trường hợp không có giá trị trả về)
#### 2/ Luồng màn hình

##### a) Có kỳ cước

##### MH1: Màn hình quét QR

##### MH2: Màn hình thông tin thanh toán

##### MH3: Màn hình xác nhận giao dịch

##### MH5: Màn hình kết quả giao dịch

##### b) Không kỳ cước

##### MH1: Màn hình quét QR

##### MH2: Màn hình thông tin thanh toán

##### MH3: Xác nhận thanh toán

##### MH5: Kết quả giao dịch

#### Mô tả:

##### MH1: Màn hình quét QR

• Xem tại mô tả màn hình quét QR
##### MH2: Màn hình thông tin thanh toán

Việc hiển thị màn hình được xử lý tại App Client, bao gồm các thông tin dựa trên kết quả SDK trả về và do nghiệp vụ App Client đang quy định hiên tại.
 | TT | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tittle | Label | Read only | 
 | 
 | 
Thông tin thanh toán

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn icon → Xử lý quay về màn hình thao tác trước đó
 | 3 | Tài khoản nguồn | Combobox | Select | Yes | -- | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do bank server trả vềHiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 4 | Thông tin giao dịch | Label | Read only | Yes | 
 | 

 | 5 | Dịch vụ | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 6 | Nhà cung cấp | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 7 | Mã khách hàng | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 8 | Kỳ cước | Label | Read only | 
 | 
 | 
Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)

Chỉ hiển thị nếu QR có kỳ cước

 | 9 | Mã giảm giá | Textbox | Input | 
 | 
 | Mặc định trống, nhập ký tự không dấu, không bao gồm các ký tự đặc biệt
 | 10 | Nút chức năng
 | 11 | Tiếp tục | Button | Click | 
 | 
 | Nhấn nút -> Tham khảo logic xử lý

##### MH3: Màn hình xác nhận thông tin
 | TT | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tittle | Label | Read only | 
 | 
 | 
Xác nhận giao dịch

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn icon → Xử lý quay về màn hình thao tác trước đó
 | 3 | Ghi chú | Icon | Click | -- | -- | Fix tại client: "Quý khách vui lòng kiểm tra thông tin thanh toán đã khởi tạo"
 | 4 | Tài khoản nguồn | Label | Read only | Yes | 
 | Hiển thị số tài khoản nguồn được chọn từ màn hình trước
 | 5 | Dịch vụ | Label | Read only | 
 | 
 | Hiển thị dữ liệu từ màn hình trước
 | 6 | Nhà cung cấp | Label | Read only | 
 | 
 | Hiển thị dữ liệu từ màn hình trước
 | 7 | Mã khách hàng | Label | Read only | 
 | 
 | Hiển thị dữ liệu từ màn hình trước (bôi đỏ giá trị)
 | 8 | 
Tên khách hàng
 | Label | Read only | 
 | 
 | 
Hiển thị dữ liệu do hệ thống billing trả về qua server

 | 9 | Kỳ cước | Label | Read only | 
 | 
 | 
Hiển thị dữ liệu từ màn hình trước

Chỉ hiển thị nếu có giá trị

 | 10 | Số tiền | Label | Read only | 
 | 
 | 
Hiển thị dữ liệu do hệ thống billing trả về qua server

 | 11 | Phí giao dịch và thuế | Label | Read only | 
 | 
 | Hiển thị dữ liệu do server trả về (chỉ hiển thị nếu khác 0 và rỗng)
 | 13 | Số tiền giảm | Label | Read only | 
 | 
 | 
Hiển thị đúng số tiền giảm giá do hệ thống MMS VNPAY trả về (sau khi check mã giảm giá hợp lệ)

Chỉ hiển thị nếu có giá trị trả về

 | 14 | Số tiền thanh toán | Label | Read only | 
 | 
 | 
Giá trị do server tính = Số tiền – Số tiền giảm (nếu có)

Hiển thị số tiền bằng chữ

 | 15 | Chọn phương thức xác thực | Combobox | Select | Yes | 
 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 16 | Nút chức năng
 | 17 | Xác nhận | Button | Click | 
 | 
 | Nhấn nút -> Tham khảo logic xử lý

##### MH4:Xác thực giao dịch

Xem tại màn hình xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH5: Màn hình  kết quả giao dịch
 | TT | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Logo
 | 
Image
 | 
Read Only
 | 
--
 | 
--
 | 

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
Nhấn nút, hiển thị màn hình home

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

• Logo Co-opbank
•  Icon thành công (nút tích trong nền tròn xanh để riêng một dòng)
• Thanh toán thành công
•  Số tiền bằng số + đơn vị tiền tệ
• Thời gian giao dịch
• Tài khoản nguồn
• Nhà cung cấp
• Dịch vụ
• Mã khách hàng
• Tên khách hàng
• Mã giao dịch
 | 4 | 
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
Nhấn icon nút chia sẻ → Tham khảo logic xử lý

 | 5 | Lưu ảnh | Icon | Click | -- | -- | Nhấn icon chụp ảnh màn hình → Tham khảo logic xử lý
 | 
6
 | 
Tạo mới giao dịch
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon tạo giao dịch mới → Tham khảo logic xử lý

#### 3/ Luồng xử lý

##### MH1: Màn hình quét QR
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả xử lý

 | 1 | Thực hiện quét mã QR hoặc chọn ảnh QR từ thư viện ảnh | Client MB | 
Kiểm tra quyền thao tác dịch vụ của khách hàng:

• Nếu dịch vụ sử dụng thuộc gói dịch vụ của khách hàng: Gửi yêu cầu lấy danh sách tài khoản nguồn <Tham chiếu logic lấy danh sách tài khoản nguồn tại màn hình chuyển tiền> và chuyển sang bước SDK giải mã QR
• Nếu dịch vụ sử dụng không thuộc gói dịch vụ của khách hàng, thông báo lỗi: "Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ."
 | 
SDK
 | 
Đọc và giải mã trường thông tin trên mã QR theo thuật toán

• Nếu hợp lệ, trả kết quả các trường dữ liệu trong QR cho App CLient
• Nếu không hợp lệ, trả kết quả lỗi cho App Client hiển thị thông báo lỗi tương ứng với các trường hợp sau: Ảnh không phải mã QR hoặc QR không đúng định dạng hỗ trợ trên SDK (chuẩn EMV Co/chuẩn VNPAY-QR).
 | Client MB | 
Nhận kết quả:

• Thành công: Hiển thị màn hình thông tin thanh toán (MH 2)
• Không thành công: Hiển thị thông báo lỗi: 
• 

 | STT | Case | Thông báo | 

 | 1 | Ảnh không phải mã QR hoặc QR không đúng định dạng hỗ trợ trên SDK (chuẩn EMV Co/chuẩn VNPAY-QR) | Mã QR không hợp lệ. Quý khách vui lòng kiểm tra lại. | 

##### MH2: Màn hình thông tin thanh toán
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1 | Nhấn chọn tài khoản nguồn khác | 
Client MB
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

•  Số tài khoản
•  Số dư khả dụng + đơn vị tiền tệ VND
 | 2

 | Nhập thông tin thanh toán và nhấn "Tiếp tục"

 | 
Client MB
 | 
Gửi yêu cầu truy vấn hóa đơn sang MMS VNPAY thông qua MB Server

 | 
MB Server
 | 
Chuyển tiếp yêu cầu truy vấn hóa đơn sang MMS VNPAY

 | 
MMS VNPAY
 | 
Thực hiện lấy thông tin Service Code và Provider Code tương ứng theo MID/TID:

• Nếu MID/TID hợp lệ: Gửi yêu cầu truy vấn hóa đơn sang Hệ thống Billing (theo loại hóa đơn)
• Nếu MID/TID không hợp lệ (bị khóa): Trả kết quả cho Client MB thông qua MB Server: "Truy vấn thông tin hóa đơn không thành công do Nhà cung cấp không hỗ trợ."
 | 
Hệ thống Billing
 | 
Xử lý và trả kết quả cước cho MMS VNPAY

 | 
MMS VNPAY
 | 
1/ Nhận kết quả:

• Thành công: Ghi nhận giao dịch phase 1 (truy vấn) thành công, chuyển bước tiếp theo
• Không thành công: Ghi nhận giao dịch phase 1 (truy vấn) lỗi, đồng thời trả kết quả về cho Client MB thông qua MB Server.
2/ Kiểm tra mã giảm giá (nếu có):

• Hợp lệ, trả kết quả cho Client MB thông qua MB Server hiển thị màn hình xác nhận giao dịch (có số tiền giảm giá)
• Không hợp lệ, trả kết quả cho Client MB thông qua MB Server hiển thị thông báo lỗi <tham khảo >
 | Server MB | 
Nhận kết quả 

• Hợp lệ, kiểm tra hạn mức gói dịch theo loại giao dịch tương ứng và tính phí giao dịch. → Tham khảo logic xử lý tại Logic kiểm tra PTXT. Gửi phản hồi lại client
• Không hợp lệ, gửi kết quả lại cho client
 | 
 Client MB
 | 
Nhận kết quả:

1/ Kết quả kiểm tra thông tin QR

• Hợp lệ, chuyển bước 2
• Không hợp lệ, hiển thị thông báo lỗi tương ứng <tham khảo bảng mã lỗi>
2/ Kết quả kiểm tra thông tin mã giảm giá (nếu có mã giảm giá)

• Hợp lệ, chuyển bước 3
• Không hợp lệ, hiển thị thông báo lỗi tương ứng <tham khảo bảng mã lỗi>
3/ Kiểm tra hạn mức gói dịch theo dịch vụ tương ứng:

• Hợp lệ, hiển thị màn hình xác nhận giao dịch
• Không hợp lệ, thông báo lỗi tương ứng: <Tham khảo >

##### MH3: Màn hình xác nhận thông tin
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1 | Nhấn "Xác nhận"

 | Client MB | 
Chuyển sang màn hình xác thực giao dịch theo phương thức xác thực tương ứng đã chọn:

• Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)
• Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)
• Nếu phương thức xác thực là vân tay → Gửi yêu cầu xác thực giao dịch (Tham khảo logic xử lý tại Xác thực bằng Touch ID/Face ID)

##### MH4: Màn hình xác thực thanh toán
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1

 | Nhập thông tin xác thực và nhấn "Tiếp tục"

 | 
Client MB
 | 
Validate thông tin  (xem tại logic màn hình xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)) và gửi yêu cầu xác thực sang server

 | 
MB Server
 | 
Xử lý:

1/ Kiểm tra hiệu lực của giao dịch:

• Không hợp lệ: Trả mã lỗi tương ứng theo PTXT cho client
• Hợp lệ: Chuyển bước tiếp
2/ Gọi bank server hạch toán

 | 
Bank Server
 | 
Xử lý hạch toán và trả kết quả về cho MB Server:

•  Ghi nợ (trừ tiền) tài khoản KH tại Ngân hàng
•  Ghi có (cộng tiền) tài khoản thu hộ VNPAY tại Ngân hàng
 | 
MB Server
 | 
Nhận kết quả:

Hợp lệ, gửi thông tin giao dịch sang MMS VNPAY (truyền số tiền nợ cước và số tiền sau giảm giá)

Không hợp lệ, phản hồi mã lỗi về cho client

 | 
MMS VNPAY
 | 
Nhận kết quả:

• Thành công:
•  Ghi nhận giao dịch phase 2 thành công
• Kiểm tra/gửi yêu cầu xử lý gạch nợ hóa đơn sang hệ thống Billing (truyền số tiền nợ cước)
• Không thành công:Ghi nhận giao dịch phase 2 không thành công
 | 
Hệ thống Billing
 | 
Xử lý gạch nợ hóa đơn và trả kết quả về MMS VNPAY

 | 
MMS VNPAY
 | 
Nhận kết quả:

• Thành công:
• Ghi nhận giao dịch phase 3 thành công
• Trả kết quả về cho App Server
• Không thành công:
• Ghi nhận giao dịch phase 3 không thành công
• Trả kết quả về cho MB  Server yêu cầu đảo giao dịch
• Timeout:
• Ghi nhận giao dịch tại phase 3 là Timeout
• Trả kết quả về cho MB Server
 | 
MB Server
 | 
Nhận kết quả:

• Phase 3 thành công: Trả kết quả cho App Client hiển thị màn hình kết quả giao dịch
• Phase 3 không thành công: Gửi yêu cầu đảo giao dịch sang Bank Server và nhận kết quả:
• Trả kết quả cho MMS VNPAY ghi nhận giao dịch phase 4 (thành công/không thành công)
• Trả kết quả cho Client MB hiển thị thông báo lỗi xử lý gạch nợ không thành công.
 | Client MB | 
Nhận kết quả:

Thành công: Chuyển sang màn hình kết quả giao dịch

Không thành công: Hiển thị thông báo lỗi tương ứng
 | TT | Case | Nội dung thông báo | Ghi chú
 | 1 | Bank server hạch toán Time out | Xem tại BẢNG MÃ LỖI CHUNG | Đóng câu thông báo và xử lý quay lại màn hình home
 | 2 | Thanh toán thất bại (bank server hạch toán thất bại hoặc đã đảo/hoàn tiền cho KH thành công) | Hiển thị thông báo do hệ thống trả về với lỗi tương ứng (có thể cấu hình lại trên QUản lý mã lỗi ở BE) | Đóng câu thông báo: Quay lại màn hình khởi tạo, xử lý reset các giá trị khởi tạo trước đó.
 | 3 | Time out tại đầu MB server | Xem tại BẢNG MÃ LỖI CHUNG | Đóng câu thông báo: Quay lại màn hình thao tác trước đó, giữ nguyên giá trị khởi tạo trước đó

##### MH5: Màn hình kết quả
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1 | 
Nhấn Icon home
 | 
Client MB
 | 
Hiển thị màn hình home

 | 2 | 
Nhấn Icon lưu ảnh
 | 
Client MB
 | 
Tham khảo tại Logic xử lý chung

 | 3 | 
Nhấn Nút chia sẻ
 | 
Client MB
 | 
Tham khảo tại Logic xử lý chung

 | 4 | 
Nhấn nút Tạo giao dịch mới
 | 
Client MB
 | 
Gọi lại api chi tiết tài khoản thanh toán vừa thực hiện giao dịch để cập nhật lại số dư tài khoản

Trở lại màn hình quét QR

---

### 17.7. Thanh toán QR type 3 - Sản phẩm

> **Page ID:** `37656629` · **Version:** 20
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37656629

##### Ghi chú: Tài liệu URD thanh toán QR được phân tích dựa trên tài liệu URD_SDK thanh toán QR 1.0.1

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client MB, SDK, MB Server, Bank Server, MMS VNPAY.
• Điều kiện trước: 
• KH đã tải ứng dụng Mobile Banking của Ngân hàng thành công.
• Ứng dụng đã tích hợp bản SDK QR do VNPAY phát triển.
• Tài khoản KH đủ điều kiện thanh toán dịch vụ QR.
• Kết quả mong muốn:
• KH thực hiện thanh toán QR Type 03 (Sản phẩm) thành công trên ứng dụng Mobile Banking của Ngân hàng.
• Hệ thống MMS VNPAY ghi nhận giao dịch giao dịch tại các phase thành công.
• Remark: [Tên KH] TT QRPay tại [Tên điểm bán] với mã [Số hóa đơn] trên Co-opBank Mobile banking 
#### 2/ Luồng màn hình

##### MH1: Màn hình quét QR

##### MH2: Màn hình thông tin đơn hàng - 1 sản phẩm

##### MH3: Màn hình thông tin đơn hàng - nhiều hơn 1 sản phẩm

##### MH4: Màn hình chọn hình thức giao hàng

##### MH5: Màn hình địa chỉ giao hàng

##### MH6: Thêm mới địa chỉ giao hàng

##### MH7: Màn hình chỉnh sửa địa chỉ giao hàng

##### MH8: Màn hình xác nhận thông tin thanh toán

##### MH10: Màn hình kết quả giao dịch

#### Mô tả:

##### MH1: Màn hình quét QR

• Xem tại mô tả màn hình quét QR
##### MH2/3: Màn hình thông tin đơn hàng

Việc hiển thị màn hình được xử lý tại App Client, bao gồm các thông tin dựa trên kết quả SDK trả về và do nghiệp vụ App Client đang quy định hiên tại.
 | TT | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tittle | Label | Read only | 
 | 
 | 
Thanh toán QRPAY

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn icon → Xử lý quay về màn hình thao tác trước đó
 | 4 | Tài khoản nguồn | Combobox | Select | Yes | -- | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do bank server trả vềHiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 5 | Thông tin thanh toán | Label | Read only | -- | -- | 

 | 6 | 
Thanh toán tại
 | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 7 | Tên điểm bán | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 8 | Mã điểm bán | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 9 | icon thu gọn/mở rộng danh sách sản phẩm | Icon | Click | 
 | 
 | Nhấn icon -> xử lý thu gọn/mở rộng vùng hiển thị danh sách sản phẩm đã quét QR
 | 10 | Danh sách sản phẩm | Label | Read only | 
 | 
 | 

 | 11 | 
Tên sản phẩm
 | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 12 | 
Mã sản phẩm
 | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 13 | 
Đơn giá
 | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 14 | 
Số lượng
 | Number Input | Input/click | 
 | 99 | 
Mặc định giá trị 1 khi quét

Cho phép nhập hoặc tăng/giảm giá trị, tối đa 2 chữ số. Không cho phép nhập số bắt đầu bằng số 0 hoặc giảm số lượng về 0.

 | 15 | 
Ghi chú
 | Textbox | Input | 
 | 250 | 
Mặc định trống

Hiển thị số ký tự đã nhập/số ký tự tối đa (mặc định: 0/250)

khi nhập ghi, hiển thị dấu x cho phép xóa toàn bộ các ký tự đã nhập

Cho phép nhập các ký tự số, chữ không dấu, dấu cách và các ký tự đặc biệt

(Hiển thị ghi chú riêng cho từng sản phẩm)

 | 16 | 
Số tiền thanh toán
 | Label | Read only | 
 | 
 | 
Hiển thị số tiền tổng cần thanh toán

Giá trị do server tính theo công thức: Số tiền thanh toán = Tổng các (Số lượng  * Đơn giá)

Hiển thị số tiền bằng chữ

 | 17 | 
Nút “Xóa” tại 1 sản phẩm 
 | Icon | Click | 
 | 
 | Chỉ hiển thị khi KH thực hiện quét nhiều hơn 1 sản phẩm trong danh sách sản phẩm thanh toán
 | 18 | 
Nút “Mở rộng/Thu gọn” tại 1 sản phẩm
 | Icon | Click | 
 | 
 | 
Chỉ hiển thị khi KH thực hiện quét nhiều hơn 1 sản phẩm trong danh sách sản phẩm thanh toán

Nhấn icon -> xử lý thu gọn/mở rộng vùng hiển thị thông tin sản phẩm đó

 | 19 | Mã giảm giá (nếu có) | Textbox | Input | 
 | 
 | Mặc định trống, nhập ký tự không dấu, không bao gồm các ký tự đặc biệt
 | Nút chức năng
 | 20 | Quét thêm QR | Button | Click | 
 | 
 | Nhấn nút -> Tham khảo logic xử lý
 | 21 | Tiếp tục | Button | Click | 
 | 
 | Nhấn nút -> Tham khảo logic xử lý

##### MH4: Màn hình chọn hình thức nhận hàng
 | TT | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tittle | Label | Read only | 
 | 
 | 
Hình thức nhận hàng

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn icon → Xử lý quay về màn hình thao tác trước đó
 | 4 | Ghi chú | Label | Read only | 
 | 
 | Fix tại client: "Quý khách vui lòng chọn hình thức nhận hàng."
 | 5 | Hình thức giao hàng | Radio button | Click | 
 | 
 | 
Hiển thị 2 giá trị:

• Nhận hàng tại điểm bán
• Nhận hàng tại địa chỉ khác
Mặc định chọn: Nhân hàng tại điểm bán

Cho phép chọn lại hình thức nhận hàng, bắt buộc chọn 1 trong 2 giá trị

 | 6 | Tiếp tục | Button | Click | 
 | 
 | Nhấn nút -> Tham khảo logic xử lý

##### MH5: Màn hình Địa chỉ giao hàng
 | TT | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tittle | Label | Read only | 
 | 
 | 
Địa chỉ nhận hàng

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn icon → Xử lý quay về màn hình thao tác trước đó
 | 4 | 
Text ghi chú
 | 
Label
 | 
ReadOnly
 | 
 | 
 | Fix tại client: "Các sản phẩm sẽ được giao đến địa chỉ dưới đây, vui lòng chọn địa chỉ hoặc thêm mới:"
 | 5 | Danh sách địa chỉ giao hàng (Cho phép lưu tối đa 10 địa chỉ giao hàng. Thức tự sắp xếp: Địa chỉ lưu gần nhất hiển thị đầu danh sách).
 | 
 | 
Địa chỉ 1
 | 
Label
 | 
ReadOnly
 | 
 | 
 | 
Là địa chỉ mới nhất được lưu và mặc định tích chọn. Thông tin địa chỉ bao gồm: Họ và tên, Địa chỉ, Quận huyện, Tỉnh thành, Số điện thoại.

Nút thao tác: Xóa, Sửa <Tham khảo logic xử lý>

 | 
Địa chỉ 2
 | 
Label
 | 
ReadOnly
 | 
 | 
 | 
Là địa chỉ thứ 2 được lưu gần nhất và mặc định không tích chọn. Thông tin địa chỉ bao gồm: Họ và tên, Địa chỉ, Quận huyện, Tỉnh thành, Số điện thoại.

Nút thao tác: Xóa, Sửa <Tham khảo logic xử lý>

 | 
Địa chỉ [n]
 | 
Label
 | 
ReadOnly
 | 
 | 
 | 
Là địa chỉ thứ [n] được lưu gần nhất và mặc định không tích chọn. Thông tin địa chỉ bao gồm: Họ và tên, Địa chỉ, Quận huyện, Tỉnh thành, Số điện thoại.

Nút thao tác: Xóa, Sửa <Tham khảo logic xử lý>

 | 6 | Thêm địa chỉ mới | Button | Click | 
 | 
 | Nhấn nút, hiển thị màn hình thêm mới địa chỉ giao hàng
 | 7 | Tiếp tục | Button | Click | 
 | 
 | 
Nhấn nút -> Tham khảo logic xử lý

chỉ hiển thị nếu tích chọn "Nhận hàng tại điểm bán"

##### MH6: Màn hình thêm mới địa chỉ giao hàng
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tittle | Label | Read only | 
 | 
 | 
Địa chỉ nhận hàng

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn icon → Xử lý quay về màn hình thao tác trước đó
 | 4 | 
Text ghi chú
 | 
Label
 | 
ReadOnly
 | 
 | 
 | Fix tại client: "Các sản phẩm sẽ được giao đến địa chỉ dưới đây, vui lòng nhập thông tin:"
 | 5 | 
Họ và tên
 | 
Textbox
 | 
Text
 | Yes | 60 | 
Mặc định trống

Cho phép nhập tiếng việt có dấu (không chứa ký tự đặc biệt)

 | 6 | 
Tỉnh/thành phố
 | 
Combobox
 | 
List
 | Yes | 
 | 
Mặc định trống

 Cho phép chọn 1 giá trị tỉnh thành được config tại Client MB

Có textsearch cho phép tìm gần đúng theo giá trị đã nhaanpj tìm kiếm

Khi focus nhập ô textsearch, hiển thị dấu x cho phép xóa toàn bộ ký tự đã nhập

 | 7 | 
Quận huyện
 | 
Combobox
 | 
List
 | Yes | 
 | 
Mặc định trống

Cho phép chọn 1 giá trị quận huyện theo tỉnh thành đã chọn và được config tại Client MB

Có textsearch cho phép tìm gần đúng theo giá trị đã nhaanpj tìm kiếm

Khi focus nhập ô textsearch, hiển thị dấu x cho phép xóa toàn bộ ký tự đã nhập

Nếu nhấn chọn Quận huyện khi chưa chọn Tỉnh thành, hiển thị thông báo "Qúy khách vui lòng chọn tỉnh/ thành phố trước"

 | 8 | 
Địa chỉ chi tiết
 | 
TextArea
 | 
Text
 | Yes | 100 | 
Mặc định trống

Cho phép nhập ký tự bất kỳ

 | 9 | 
Số điện thoại
 | 
Textbox
 | 
Number
 | Yes | 10 | 
Mặc định trống

 Chỉ cho nhập ký tự số (bàn phím số)

 | 10 | 
Email
 | 
Textbox
 | 
Text
 | 
 | 100 | 
 Mặc định trống

Chỉ cho nhập tiếng Việt không dấu, không có khoảng trắng, số và 1 số ký tự đặc biết: @._-

 Kiểm tra định dạng email hợp lệ: text@text.text hoặc text@text.text.text

 | 11 | Tiếp tục | Button | Click | 
 | 
 | Nhấn nút -> Tham khảo logic xử lý

##### MH7:Màn hình chỉnh sửa địa chỉ giao hàng

• Xem mô tả tại màn hình Thêm mới địa chỉ giao hàng (MH6)
• Fill các giá trị tương ứng và cho phép KH chỉnh sửa lại thông tin
##### MH8: Màn hình xác nhận thông tin đơn hàng
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tittle | Label | Read only | 
 | 
 | 
Xác nhận giao dịch

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn icon → Xử lý quay về màn hình danh sách địa chỉ nhận hàng
 | 3 | Ghi chú | Icon | Read Only | -- | -- | Fix tại client: "Quý khách vui lòng kiểm tra thông tin thanh toán đã khởi tạo"
 | 4 | Tài khoản nguồn | Label | Read only | 
 | 
 | Hiển thị số tài khoản nguồn được chọn từ màn hình trước
 | 5 | Thanh toán tại | Label | Read only | 
 | 
 | Hiển thị dữ liệu từ màn hình trước (bôi đỏ giá trị)
 | 6 | Tên điểm bán | Label | Read only | 
 | 
 | Hiển thị dữ liệu từ màn hình trước
 | 8 | Số hóa đơn | Label | Read only | 
 | 
 | 
Hiển thị số hóa đơn do server trả về (bôi đỏ giá trị), là mã tự tăng trên thông do MB server tự sinh khi khởi tạo GD thành công

 | 9 | Số tiền | Label | Read only | 
 | 
 | Hiển thị dữ liệu từ màn hình trước
 | 11 | Số tiền giảm | Label | Read only | 
 | 
 | Chỉ hiển thị khi màn hình trước có nhập mã giá giảm giá
 | 12 | Số tiền thanh toán | Label | Read only | 
 | 
 | 
Giá trị do MB Server tính = Số tiền thanh toán – Số tiền được giảm giá

Chỉ hiển thị khi có số tiền được giảm giá

 | 
 | Phí giao dịch và thuế | Label | Read only | 
 | 
 | Hiển thị dữ liệu do server trả về (chỉ hiển thị nếu khác 0 và rỗng)
 | 13 | Địa chỉ giao hàng | Label | Read only | 
 | 
 | Hiển thị dữ liệu theo địa chỉ giao hàng đã chọn từ màn hình trước
 | 15 | Chọn phương thức xác thực | Combobox | Select | Yes | 
 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 16 | Xác nhận | Button | Click | 
 | 
 | Nhấn nút -> Tham khảo logic xử lý

##### MH9: Màn hình xác thực giao dịch

Xem tại màn hình xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH10: Màn hình kết quả giao dịch
 | TT | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Logo
 | 
Image
 | 
Read Only
 | 
--
 | 
--
 | 

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

• Logo Co-opbank
•  Icon thành công (nút tích trong nền tròn xanh để riêng một dòng)
• Thanh toán thành công
•  Số tiền bằng số + đơn vị tiền tệ
• Thời gian giao dịch
• Tài khoản nguồn
• Tên đại lý
• Tên điểm bán
• Số hóa đơn
• Mã giao dịch
 | 4 | 
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
Nhấn icon nút chia sẻ → Tham khảo logic xử lý

 | 5 | Lưu ảnh | Icon | Click | -- | -- | Nhấn icon chụp ảnh màn hình → Tham khảo logic xử lý
 | 
6
 | 
Tạo mới giao dịch
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon tạo giao dịch mới → Tham khảo logic xử lý

#### 3/ Luồng xử lý

##### MH1: Màn hình quét QR
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1

 | 
Thực hiện quét mã QR hoặc chọn ảnh QR từ thư viện ảnh

 | Client MB | 
Kiểm tra quyền thao tác dịch vụ của khách hàng:

• Nếu dịch vụ sử dụng thuộc gói dịch vụ của khách hàng: Gửi yêu cầu lấy danh sách tài khoản nguồn <Tham chiếu logic lấy danh sách tài khoản nguồn tại màn hình chuyển tiền> và chuyển sang bước SDK giải mã QR
• Nếu dịch vụ sử dụng không thuộc gói dịch vụ của khách hàng, thông báo lỗi: "Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ."
 | 
SDK
 | 
Đọc và giải mã trường thông tin trên mã QR theo thuật toán:

• Nếu hợp lệ, trả kết quả cho client MB hiển thị màn hình Thanh toán đơn hàng (1 sản phẩm)
• Nếu không hợp lệ, trả kết quả cho Client MB hiển thị thông báo lỗi tương ứng với các trường hợp sau: Ảnh không phải mã QR hoặc QR không đúng định dạng hỗ trợ trên SDK (chuẩn EMV Co/chuẩn VNPAY-QR)
 | 
Client MB
 | 
Nhận kết quả:

• Thành công: Hiển thị màn hình thanh toán thanh toán (màn hình 2)
• Không thành công: Hiển thị thông báo lỗi: 
• 

 | STT | Case | Thông báo | 

 | 1 | Ảnh không phải mã QR hoặc QR không đúng định dạng hỗ trợ trên SDK (chuẩn EMV Co/chuẩn VNPAY-QR) | Mã QR không hợp lệ. Quý khách vui lòng kiểm tra lại. | 

##### MH2/3: Màn hình thông tin đơn hàng
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1 | Nhấn chọn tài khoản nguồn khác | 
Client MB
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

•  Số tài khoản
•  Số dư khả dụng + đơn vị tiền tệ VND
 | 2 | 
Nhấn “Quét thêm QR”
 | 
Client MB
 | 
Hiển thị màn hình Quét QR thêm (xử lý ẩn thanh menu vùng footer tránh KH nhấn nhầm khi đang thực hiện chức năng)

 | 
Thực hiện Quét thêm 1 QR hoặc chọn từ thư viện ảnh
 | 
SDK
 | 
Kiểm tra thông tin QR:

• Nếu hợp lệ, trả kết quả cho client MB hiển thị màn hình Thanh toán đơn hàng (nhiều sản phẩm)
• Nếu không hợp lệ, trả kết quả cho Client MB hiển thị thông báo lỗi
 | 
Client MB
 | 
Nhận kết quả:

• Thành công: Hiển thị màn hình Thanh toán đơn hàng (nhiều sản phẩm)
• Không thành công: Hiển thị thông báo lỗi (tham khảo )
 | 3 | 
Nhấn “Xóa” tại 1 sản phẩm đã quét (ít nhất 2 sản phẩm)
 | 
Client MB
 | 
Hiển thị thông báo: Quý khách chắc chắn muốn xóa sản phẩm này khỏi danh sách?

• Nút Xóa: Nhấn nút này, ứng dụng thực hiện xóa sản phẩm khỏi danh sách.
• Nút Hủy: Nhấn nút này, tắt thông báo và giữ nguyên màn hình hiện tại.
 | 4 | Nhấn thu gọn/mở rộng danh sách sản phẩm | Client MB | Hiển thị danh sách sản phẩm ở chế độ thu gọn/mở rộng tương ứng.
 | 5 | Nhấn thu gọn/mở rộng thông tin 1 sản phẩm | Client MB | Hiển thị sản phẩm ở chế độ thu gọn/mở rộng tương ứng.
 | 6 | 
Nhấn Tăng/giảm số lượng hoặc nhập thay đổi số lượng sản phẩm
 | 
Cllient MB
 | 
Trường hợp tăng/giảm số lượng sản phẩm bằng cách click vào icon (-) và (+):

• Nếu bằng 1 thì không cho thao tác với icon (-).
• Cho phép tăng giảm số lượng, tối đa không quá 2 chữ số.
Trường hợp nhập thay đổi số lượng sản phẩm:

• Chỉ cho nhập số (bàn phím số), không nhập ký tự đặc biệt
• Không nhập số bắt đầu bằng số 0
• Số lượng nhập tối đa không quá 2 chữ số
Khi thực thay đổi số lượng sản phẩm, trường “Tổng tiền thanh toán” tự động tính lại tại ứng dụng theo công thức: Tổn

> ⚠️ *Nội dung đã cắt ngắn (24275 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 17.8. Thanh toán QR type 4 - Cổng thanh toán

> **Page ID:** `37657472` · **Version:** 11
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37657472

##### Ghi chú: Tài liệu URD thanh toán QR được phân tích dựa trên tài liệu URD_SDK thanh toán QR 1.0.1

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Client MB, SDK, MB  Server, Bank Server, MMS VNPAY.
• Điều kiện trước: 
• KH đã tải ứng dụng Mobile Banking của Ngân hàng thành công.
• Ứng dụng đã tích hợp bản SDK QR do VNPAY phát triển.
• Tài khoản KH đủ điều kiện thanh toán dịch vụ QR.
• Kết quả mong muốn:
• KH thực hiện thanh toán QR Type 04 – Cổng thanh toán VNPAY-QR thành công trên ứng dụng Mobile Banking của Ngân hàng.
• Hệ thống MMS VNPAY ghi nhận giao dịch giao dịch tại các phase thành công.
• Remark: [Tên KH] TT QRPay tại [Tên điểm bán] với mã [Số hóa đơn] trên Co-opBank Mobile banking 
#### 2/ Luồng màn hình

##### MH1: Màn hình quét QR

##### MH2: Màn hình thông tin thanh toán

##### MH3: Màn hình xác nhận giao dịch

##### MH5: Màn hình kết quả giao dịch

#### Mô tả:

##### MH1: Màn hình quét QR

• Xem tại mô tả màn hình quét QR
##### MH2: Màn hình thông tin thanh toán

Việc hiển thị màn hình được xử lý tại App Client, bao gồm các thông tin dựa trên kết quả SDK trả về và do nghiệp vụ App Client đang quy định hiên tại.
 | TT | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tittle | Label | Read only | 
 | 
 | 
Thanh toán QRPAY

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn icon → Xử lý quay về màn hình thao tác trước đó
 | 4 | Tài khoản nguồn | Combobox | Select | Yes | -- | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do bank server trả vềHiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 5 | Thông tin thanh toán | Label | Read only | -- | -- | 

 | 6 | 
Thanh toán tại
 | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 7 | Tên điểm bán | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 8 | Số tiền | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 9 | Thời hạn thanh toán | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 10 | Mô tả | Label | Read only | 
 | 
 | Hiển thị theo giá trị SDK trả về (thông tin đã quét và giải mã được từ QR)
 | 11 | Mã giảm giá (nếu có) | Textbox | Input | 
 | 
 | Mặc định trống, nhập ký tự không dấu, không bao gồm các ký tự đặc biệt
 | 12 | Tiếp tục | Button | Click | 
 | 
 | Nhấn nút -> Tham khảo logic xử lý

##### MH3: Màn hình xác nhận thông tin thanh toán
 | TT | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tittle | Label | Read only | 
 | 
 | 
Xác nhận giao dịch

 | 2 | Icon Back | Icon | Click | -- | -- | Nhấn icon → Xử lý quay về màn hình thao tác trước đó
 | 3 | Ghi chú | Label | Read only | 
 | 
 | Fix tại client: "Quý khách vui lòng kiểm tra thông tin thanh toán đã khởi tạo"
 | 4 | Tài khoản nguồn | Label | Read only | Yes | 
 | Hiển thị số tài khoản nguồn được chọn từ màn hình trước
 | 5 | Thanh toán tại | Label | Read only | 
 | 
 | 
Hiển thị dữ liệu từ màn hình trước

Hiển thị màu đỏ

 | 6 | Tên điểm bán | Label | Read only | 
 | 
 | Hiển thị dữ liệu từ màn hình trước
 | 7 | Số hóa đơn | Label | Read only | 
 | 
 | 
Hiển thị số hóa đơn do server trả về

Hiển thị màu đỏ

 | 8 | Số tiền | Label | Read only | 
 | 
 | Hiển thị dữ liệu từ màn hình trước
 | 10 | Số tiền giảm | Label | Read only | 
 | 
 | Chỉ hiển thị khi màn hình trước có nhập mã giá giảm giá
 | 11 | Số tiền thanh toán | Label | Read only | 
 | 
 | 
Giá trị do MB Server tính = Số tiền thanh toán – Số tiền được giảm giá

Chỉ hiển thị khi có số tiền được giảm giá

Hiển thị số tiền bằng chữ

 | 
 | Phí giao dịch và thuế | Label | Read only | 
 | 
 | Hiển thị dữ liệu do server trả về (chỉ hiển thị nếu khác 0 và rỗng)
 | 12 | Mô tả | Label | Read only | 
 | 
 | Hiển thị dữ liệu từ màn hình trước
 | 13 | Chọn phương thức xác thực | Combobox | Select | Yes | 
 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 14 | Xác nhận | Button | Click | 
 | 
 | Nhấn nút -> Tham khảo logic xử lý

##### MH4: Màn hình xác thực giao dịch

• Xem tại màn hình xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)
##### MH5: Màn hình kết quả giao dịch
 | TT | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Logo
 | 
Image
 | 
Read Only
 | 
--
 | 
--
 | 

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

• Logo Co-opbank
•  Icon thành công (nút tích trong nền tròn xanh để riêng một dòng)
• Thanh toán thành công
•  Số tiền bằng số + đơn vị tiền tệ
• Thời gian giao dịch
• Tài khoản nguồn
• Tên đại lý
• Tên điểm bán
• Số hóa đơn
• Mã giao dịch
 | 4 | 
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
Nhấn icon nút chia sẻ → Tham khảo logic xử lý

 | 5 | Lưu ảnh | Icon | Click | -- | -- | Nhấn icon chụp ảnh màn hình → Tham khảo logic xử lý
 | 
6
 | 
Tạo mới giao dịch
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Nhấn icon tạo giao dịch mới → Tham khảo logic xử lý

#### 3/ Luồng xử lý

##### MH1: Màn hình quét QR
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1

 | Thực hiện quét mã QR hoặc chọn ảnh QR từ thư viện ảnh

 | Client MB | 
Kiểm tra quyền thao tác dịch vụ của khách hàng:

• Nếu dịch vụ sử dụng thuộc gói dịch vụ của khách hàng: Gửi yêu cầu lấy danh sách tài khoản nguồn <Tham chiếu logic lấy danh sách tài khoản nguồn tại màn hình chuyển tiền> và chuyển sang bước SDK giải mã QR
• Nếu dịch vụ sử dụng không thuộc gói dịch vụ của khách hàng, thông báo lỗi: "Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ."
 | 
SDK
 | 
Đọc và giải mã trường thông tin trên mã QR theo thuật toán

• Nếu hợp lệ, hiển thị màn hình Thông tin QR
• Nếu không hợp lệ, hiển thị thông báo lỗi tương ứng với các trường hợp sau: Ảnh không phải mã QR hoặc QR không đúng định dạng hỗ trợ trên SDK (chuẩn EMV Co/chuẩn VNPAY-QR)
 | 
Client MB
 | 
Nhận kết quả:

• Thành công: Hiển thị màn hình thông tin thanh toán (màn hình 2)
• Không thành công: Hiển thị thông báo lỗi:  | STT | Case | Thông báo | 

 | 1 | Ảnh không phải mã QR hoặc QR không đúng định dạng hỗ trợ trên SDK (chuẩn EMV Co/chuẩn VNPAY-QR) | Mã QR không hợp lệ. Quý khách vui lòng kiểm tra lại. | 

##### MH2: Màn hình thông tin thanh toán
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1 | Nhấn chọn tài khoản nguồn khác | 
Client MB
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

•  Số tài khoản
•  Số dư khả dụng + đơn vị tiền tệ VND
 | 2

 | Nhấn "Tiếp tục"

 | 
Client MB
 | 
Gửi yêu cầu khởi tạo giao dịch sang MB Server

 | 
MB Server
 | 
Nhận và gửi yêu cầu kiểm tra thông tin QR sang hệ thống MMS VNPAY

 | 
MMS VNPAY
 | 
1/ Nhận kết quả:

• Thành công: Ghi nhận giao dịch phase 1 (truy vấn) thành công, chuyển bước tiếp theo
• Không thành công: Ghi nhận giao dịch phase 1 (truy vấn) lỗi, đồng thời trả kết quả về cho Client MB thông qua MB Server.
2/ Kiểm tra mã giảm giá (nếu có):

• Hợp lệ, trả kết quả cho Client MB thông qua MB Server hiển thị màn hình xác nhận giao dịch (có số tiền giảm giá)
• Không hợp lệ, trả kết quả cho Client MB thông qua MB Server hiển thị thông báo lỗi <tham khảo bảng mã lỗi thanh toán QR>
 | MB Server | 
Nhận kết quả 

• Hợp lệ, kiểm tra hạn mức gói dịch theo loại giao dịch tương ứng và tính phí giao dịch. → Tham khảo logic xử lý tại Logic kiểm tra PTXT. Gửi phản hồi lại client
• Không hợp lệ, gửi kết quả lại cho client
 | 
App Client
 | 
Nhận kết quả:

1/ Kết quả kiểm tra thông tin QR

• Hợp lệ, hiển thị màn hình xác nhận giao dịch
• Không hợp lệ, hiển thị thông báo lỗi theo 
2/ Kết quả kiểm tra thông tin mã giảm giá

• Hợp lệ, hiển thị màn hình xác nhận giao dịch (có số tiền giảm giá)
• Không hợp lệ, hiển thị thông báo lỗi theo
 3/ Kiểm tra hạn mức gói dịch theo dịch vụ tương ứng:

• Hợp lệ, hiển thị màn hình xác nhận thanh toán (MH8)
• Không hợp lệ, thông báo lỗi tương ứng: <Tham khảo >

##### MH3: Màn hình xác nhận thông tin
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1 | Nhấn "Xác nhận" | Client MB | 
Chuyển sang màn hình xác thực giao dịch theo phương thức xác thực tương ứng đã chọn:

• Nếu phương thức xác thực là soft OTP → Gửi yêu cầu xác thực giao dịch theo Soft OTP (Tham khảo logic xử lý tại Xác thực bằng soft OTP)
• Nếu phương thức xác thực là sms OTP → Gửi yêu cầu xác thực giao dịch theo SMS OTP (Tham khảo logic xử lý tại Xác thực bằng SMS OTP)
• Nếu phương thức xác thực là vân tay → Gửi yêu cầu xác thực giao dịch (Tham khảo logic xử lý tại Xác thực bằng Touch ID/Face ID)

##### MH4: Màn hình xác thực giao dịch
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1

 | Nhấn "Tiếp tục"

 | 
Client MB
 | 
Validate thông tin  (xem tại logic màn hình xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)) và gửi yêu cầu xác thực sang server

 | 
MB Server
 | 
Xử lý:

1/ Kiểm tra hiệu lực của giao dịch:

• Không hợp lệ: Trả mã lỗi tương ứng theo PTXT cho client
• Hợp lệ: Chuyển bước tiếp
2/ Gọi bank server hạch toán

 | 
Bank Server
 | 
Xử lý hạch toán và trả kết quả về cho MB Server:

• Ghi nợ (trừ tiền) tài khoản KH tại Ngân hàng
• Ghi có (cộng tiền) tài khoản VNPAY tại Ngân hàng
 | 
MB Server
 | 
Nhận kết quả:

Hợp lệ, gửi thông tin giao dịch sang MMS VNPAY

Không hợp lệ, phản hồi mã lỗi tương ứng cho Client và MMS VNPAY để ghi nhập kết quả phase 2

 | 
MMS VNPAY
 | 
Nhận kết quả:

• Thành công:
• Ghi nhận giao dịch phase 2 thành công
• Kiểm tra/gửi yêu cầu xử lý đơn hàng sang Cổng thanh toán VNPAY-QR
• Không thành công: Ghi nhận giao dịch phase 2 không thành công
 | 
Cổng thanh toán VNPAY-QR
 | 
Xử lý đơn hàng và trả kết quả về MMS VNPAY

 | 
MMS VNPAY
 | 
Nhận kết quả:

• Thành công:
• Ghi nhận giao dịch phase 3 thành công
• Trả kết quả về cho MB Server
• Không thành công:
• Ghi nhận giao dịch phase 3 không thành công
•  Trả kết quả về cho MB Server yêu cầu đảo giao dịch
 | 
MB  Server
 | 
Nhận kết quả:

• Phase 3 thành công: Trả kết quả cho Client MB hiển thị màn hình kết quả giao dịch
• Phase 3 không thành công: Gửi yêu cầu đảo giao dịch sang Bank Server và nhận kết quả:
• Trả kết quả cho MMS VNPAY ghi nhận giao dịch phase 4 (thành công/không thành công)
• Trả kết quả cho Client MB hiển thị thông báo lỗi xử lý đơn hàng không thành công.
 | Client MB | 
Nhận kết quả:

• Thành công: Chuyển sang màn hình kết quả giao dịch
• Không thành công: Hiển thị thông báo lỗi tương ứng: | TT | Case | Tác nhân | Nội dung thông báo | Ghi chú
 | 1 | Bank server hạch toán Time out | Xem tại BẢNG MÃ LỖI CHUNG | Đóng câu thông báo và xử lý quay lại màn hình home | Đóng câu thông báo và xử lý quay lại màn hình home
 | 2 | Thanh toán thất bại (bank server hạch toán thất bại hoặc đã đảo/hoàn tiền cho KH thành công) | Hiển thị thông báo do hệ thống trả về với lỗi tương ứng (có thể cấu hình lại trên QUản lý mã lỗi ở BE) | Đóng câu thông báo: Quay lại màn hình khởi tạo, xử lý reset các giá trị khởi tạo trước đó. | Đóng câu thông báo: Quay lại màn hình khởi tạo, xử lý reset các giá trị khởi tạo trước đó.
 | 3 | Time out tại đầu MB server | Xem tại BẢNG MÃ LỖI CHUNG | Đóng câu thông báo: Quay lại màn hình thao tác trước đó, giữ nguyên giá trị khởi tạo trước đó | Đóng câu thông báo: Quay lại màn hình thao tác trước đó, giữ nguyên giá trị khởi tạo trước đó

##### MH5: Màn hình kết quả giao dịch
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1 | 
Nhấn Icon home
 | 
Client MB
 | 
Hiển thị màn hình home

 | 2 | 
Nhấn Icon lưu ảnh
 | 
Client MB
 | 
Tham khảo tại Logic xử lý chung

 | 3 | 
Nhấn Nút chia sẻ
 | 
Client MB
 | 
Tham khảo tại Logic xử lý chung

 | 4 | 
Nhấn nút Tạo giao dịch mới
 | 
Client MB
 | 
Gọi lại danh sách tài khoản thanh toán vừa thực hiện giao dịch để cập nhật lại số dư tài khoản

Trở lại màn hình quét QR

---

### 17.9. Quét QR theo hình thức call App

> **Page ID:** `37658076` · **Version:** 10
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37658076

#### 1/ Tác nhân, điều kiện trước, kết quả mong muốn

• Tác nhân tham gia: KH, Website Merchant, Client MB, SDK, MB Server, Bank Server, MMS VNPAY.
• Điều kiện trước: 
• KH đã tải và cài đặt ứng dụng thành công.
• KH truy cập thiết bị di động có cài ứng dụng MB và mua hàng tại Website TMĐT thanh toán qua hình thức quét mã QR
• Kết quả mong muốn:
• KH thực hiện thanh toán thành công đơn hàng tại website TMĐT theo hình thức QR Call App bằng ứng dụng MB
• Hệ thống MMS VNPAY ghi nhận thành công giao dịch thanh toán QR.
• Website merchant được cập nhật trạng thái xử lý đơn hàng thành công.
#### 2/ Luồng màn hình

##### MH1: Màn hình chọn thanh toán QR tại các website

##### MH2: Màn hình thông tin thanh toán

##### MH3: Màn hình xác nhận thông tin thanh toán

##### MH5: Màn hình kết quả giao dịch

#### Mô tả:

##### MH1: Màn hình chọn thanh toán QR tại các website
 | 
 | Hạng mục | Kiểu hiểu thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Các thông tin hiển thị tùy theo từng trang website thương mại điện tử của merchant 

 | Mã QR | Image | Read only | 
 | 
 | Ảnh QR công thanh toán
 | 2 | Danh sách ứng dụng hỗ trợ VNPAY QR | Button | Click | Yes | 
 | 
Nhấn chọn 1 ứng dụng -> Tham khảo logic xử lý

##### MH2: Màn hình thông tin thanh toán

• Xem mô tả tại 
##### MH3: Màn hình xác nhận thông tin thanh toán

• Xem tại mô tả tại 
##### MH4: Màn hình xác thực giao dịch

• Xem mô tả tại 
##### MH5: Màn hình kết quả giao dịch

• Xem mô tả tại
• Thay nút "Tạo giao dịch mới" thành "Về website"
#### 3/ Luồng xử lý

##### Thao tác chọn Thanh toán QR tại các Website Thương mại điện tử:
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1 | Chọn phương thức thanh toán quét QR qua ứng dụng hỗ trợ | 
Website Merchant
 | 
Website Merchant gửi thông tin giao dịch sang hệ thống Cổng thanh toán VNPAY

 | Cổng thanh toán VNPAY | 
Hệ thống Cổng thanh toán VNPAY khởi tạo giao dịch, sinh mã QR theo quy định và hiển thị màn hình thông tin tương ứng dựa trên thiết bị truy cập của người dùng (MH1)

##### MH1: Màn hình chọn thanh toán QR tại các website
 | TT | Thao tác | Tác nhân | Mô tả xử lý
 | 1 | Nhấn chọn thanh toán qua ứng dụng Co-opBank Mobile Banking | 
Cổng thanh toán VNPAY
 | 
Hệ thống Cổng thanh toán gửi yêu cầu giao tiếp mở ứng dụng Co-opbank Mobile Banking trên thiết bị di động (bao gồm truyền dữ liệu đơn hàng QR đã thực hiện)

 | Thiêt bị  | 
Kiểm tra ứng dụng Co-opbank Mobile Banking có cài đặt trên thiết bị di động:

• Trường hợp chưa cài đặt trên thiết bị: "Không thể mở trang này vì địa chỉ không hợp lệ." -> Đóng thông báo, giữ nguyên màn hình xử lý trước đó.
• Trường hợp đã cài đặt ứng dụng:
• Không sử dụng trình duyệt mặc định của hệ điều hành, hiển thị thông báo: "Quý khách vui lòng sử dụng trình duyệt mặc định của thiết bị." -> Đóng thông báo, giữ nguyên màn hình xử lý trước đó.
• Có sử dụng trình duyệt mặc định của hệ điều hành, mở ứng dụng Co-opBank Mobile Banking và chuyển bước tiếp theo
 | Client MB | 
 Hiển thị màn hình đăng nhập ứng dụng, KH thực hiện đăng nhập -> Tham chiếu :

• Đăng nhập thành công, tự động xử lý giải mã QR và hiển thị màn hình thông tin thanh toán (MH2)
• Đăng nhập không thành công, giữ nguyên màn hình đăng nhập ứng dụng hiện tại.

##### MH2: Màn hình thông tin thanh toán

• Xem mô tả logic xử lý tại 
##### MH3: Màn hình xác nhận thông tin thanh toán

• Xem tại mô tả logic xử lý tại 
##### MH4: Màn hình xác thực giao dịch

• Xem mô tả logic xử lý tại 
##### MH5: Màn hình kết quả giao dịch
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả xử lý

 | 1 | 
Nhấn Icon home
 | 
Client MB
 | 
Hiển thị màn hình home

 | 2 | 
Nhấn Icon lưu ảnh
 | 
Client MB
 | 
Tham khảo tại Logic xử lý chung

 | 3 | 
Nhấn Nút chia sẻ
 | 
Client MB
 | 
Tham khảo tại Logic xử lý chung

 | 4 | 
Nhấn nút "Về website (20s)"
 | 
Client MB
 | 
Có đếm ngược thời gian, sau 20s KH không thao tác, tự động xử lý quay lại website

Gọi lại api chi tiết tài khoản thanh toán vừa thực hiện giao dịch để cập nhật lại số dư tài khoản

Xử lý quay lại màn hình kết quả thanh toán tương ứng theo từng website

---

### 17.10. Bảng mã lỗi QRPAY

> **Page ID:** `37655350` · **Version:** 13
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/37655350

| 
TT
 | 
Điều kiện
 | 
Tác nhân 
 | 
Nội dung thông báo lỗi
 | 
Mô tả thêm

 | 
Kiểm tra thông tin QR

 | 1 | 
Ip address is denied
(Địa chỉ IP không được truy cập) | 
MMS 

(02)
 | Địa chỉ truy cập của Quý khách không hợp lệ. Vui lòng kiểm tra lại. | 

 | 2 | 
This Qrcode is paid
(Mã Qrcode này đã được thanh toán ứng với paytype 01) | 
MMS 

(01)
 | Đơn hàng đã được thanh toán. Quý khách vui lòng kiểm tra lại. | 

 | 3 | 
Bank code is not exist in QrcodeGateway
(Mã ngân hàng không tồn tại trong hệ thống) | 
MMS 

(03)
 | Giao dịch không thành công do đơn vị hỗ trợ thanh toán không tồn tại. Quý khách vui lòng kiểm tra lại. | 

 | 4 | 
QRcode is not in format

(Dữ liêu Qrcode không theo định dạng)

Data of Qrcode is changed

(Dữ liệu trong Qrcode đã bị thay đổi)
 | 
MMS 

(04/30)
 | Thông tin mã QR không hợp lệ. Quý khách vui lòng kiểm tra lại. | 

 | 5 | 
List QRcode is required
(Danh sách Qrcode truyền vào bị null hoặc trống) | 
MMS 

(05)
 | Danh sách QR thanh toán không hợp lệ. Quý khách vui lòng kiểm tra lại. | 

 | 6 | 
Merchant is not exist

(Merchant không tồn tại trong hệ thống Qrcode)

Terminal is not exist

(Terminal không tồn tại trong hệ thống)

Master merchant is not exist

(Đơn vị phát triển Qrcode không tồn tại)
 | 
MMS 

(07/21/25/)
 | Giao dịch không thành công do đơn vị kinh doanh không tồn tại. Quý khách vui lòng kiểm tra lại. | 

 | 7 | 
Merchant is not active

(Merchant chưa được kích hoạt)

Terminal is not active

(Terminal chưa được kích hoạt)

Master merchant is not active

(Đơn vị phát triển Qrcode khôn hoạt động)

Giao dịch không hợp lệ hoặc bị chặn với MC này
 | 
MMS 

(11/24/26/14)
 | Giao dịch không thành công do đơn vị kinh doanh chưa hỗ trợ. Quý khách vui lòng kiểm tra lại. | 

 | 8 | 
These Qrcode dont have the same merchant

(Các Qrcode không cùng Merchant)

These Qrcode dont have the same terminal

(Các Qrcode không cùng terminal)
 | 
MMS 

(31/32)
 | Danh sách QR thanh toán không cùng đơn vị kinh doanh. Quý khách vui lòng kiểm tra lại. | 

 | 9 | Mã khách hàng không hợp lệ | 
MMS 

(50)
 | Thông báo như của TTHĐ hiện tại trên app | 

 | 10 | 
Username is invalid.
(Tài khoản không hợp lệ) | 
MMS 

(70)
 | Tài khoản thanh toán không hợp lệ. Quý khách vui lòng kiểm tra lại. | 

 | 11 | Bank not support | 
MMS 

(76)
 | Khởi tạo giao dịch không thành công do đơn vị thanh toán không hỗ trợ. | 

 | 12 | Nhà cung cấp bảo trì | 
MMS 

(96)
 | Kết nối đơn vị thanh toán bị gián đoạn. Quý khách vui lòng thử lại | 

 | 13 | 
Internal error

False checksum

(Check sum vào hàm Gateway bị sai)
 | 
MMS 

(99/12)
 | Hệ thống tạm thời gián đoạn. Quý khách vui lòng thử lại. | 

 | 14 | QRcode is not active  | MMS (29) | Mã QR đã hết hạn hoặc không ở trạng thái hoạt động. Quý khách vui lòng kiểm tra lại. | 

 | 
QR Type 03 – Sản phẩm

 | 
1
 | 
QR đã hết hạn thanh toán
 | 
App Client
 | 
Mã QR đã hết hạn thanh toán. Quý khách vui lòng kiểm tra lại.
 | 

 | 
2
 | 
Mã QR đúng định dạng nhưng khác thông tin Đại lý với thông tin mã QR đã được quét trước đó
 | 
App Client
 | 
Quý khách vui lòng chọn đúng sản phẩm cùng nhà cung cấp.
 | 

 | 
3
 | 
Mã QR đúng định dạng, cùng Đại lý nhưng khác Điểm bán với thông tin mã QR đã được quét trước đó
 | 
App Client
 | 
Quý khách vui lòng chọn đúng sản phẩm cùng 1 điểm bán hàng.
 | 

 | 
4
 | 
Mã QR được quét đang tồn tại trong danh sách QR đã quét
 | 
App Client
 | 
Sản phẩm này đã có trong danh sách. Quý khách vui lòng kiểm tra lại.
 | 

 | 
5
 | 
Mã QR không cùng định dạng QR sản phẩm đã quét trước đó
 | 
App Client
 | 
Định dạng QR sản phẩm này không giống với định dạng QR sản phẩm đã quét trước đó. Quý khách vui lòng kiểm tra lại.
 | 

 | 
6
 | 
Quét mã QR vượt quá số lượng cho phép (tối đa 10 mã)
 | 
App Client
 | 
Số lượng mã QR đã vượt  quá số lần quy định. Quý khách vui lòng thực hiện thanh toán.
 | 

 | 
QR Type 04 – Cổng thanh toán VNPAY-QR

 | 
1
 | 
Mã QR đã hết hạn thanh toán
 | 
App Client
 | 
Mã QR đã hết hạn thanh toán. Quý khách vui lòng kiểm tra lại.
 | 

 | 
Kiểm tra mã giảm giá (Áp dụng cho tất cả các type QR)

Lưu ý: Cập nhật các case check mã giảm giá theo điều kiện chương trình thực tế

 | 
 | Không có chương trình khuyến mại | MMS (60,48) | Không tồn tại chương trình khuyến mại, giao dịch không được giảm giá. Quý khách có muốn tiếp tục giao dịch? | 
Đối với các thông báo lỗi này, ứng dụng hiển thị 2 nút thao tác trên popup:

• Nút Không: Nhấn nút này, tắt popup thông báo và hiển thị màn hình đang thao tác.
• Nút Tiếp tục: Nhấn nút này, ứng dụng khởi tạo giao dịch và hiển thị màn hình xác nhận giao dịch tương ứng.

 | 
1
 | 
Mã giảm giá không đúng 
 | 
MMS (61)
 | 
Mã giảm giá không đúng. Quý khách có muốn tiếp tục giao dịch?

 | 
2
 | 
Mã giảm giá hết số lần áp dụng/KH (số lần cấu hình tại MMS VNPAY)
 | 
MMS (66)
 | 
Giao dịch không được giảm giá do đã hết số lần áp dụng/KH. Quý khách có muốn tiếp tục giao dịch?

 | 
3
 | 
Mã giảm giá hết hiệu lực sử dụng
 | 
MMS (69)
 | 
Mã giảm giá đã hết hiệu lực. Quý khách có muốn tiếp tục giao dịch?

 | 
4
 | 
Hết số lượng mã giảm giá trong chương trình
 | 
MMS (64)
 | 
Số lượng mã giảm giá đã hết. Quý khách có muốn tiếp tục giao dịch?

 | 
5
 | 
Giao dịch không được giảm giá (hóa đơn/đơn hàng có nợ cước hoặc số tiền < A VNĐ)
 | 
MMS (65)
 | 
Giao dịch không được giảm giá do giá trị nhỏ hơn giá trị tối thiểu quy định. Quý khách có muốn tiếp tục giao dịch?

 | 
6
 | 
Đại lý, điểm bán không được cấu hình giảm giá
 | 
MMS (63)
 | 
Giao dịch không được giảm giá do đơn vị kinh doanh chưa tham gia chương trình. Quý khách có muốn tiếp tục giao dịch?

 | 
7
 | 
Ngân hàng không còn hiệu lực áp dụng giảm giá
 | 
MMS (62)
 | 
Giao dịch không được giảm giá do ngân hàng thanh toán không hỗ trợ. Quý khách có muốn tiếp tục giao dịch?

 | 
8
 | 
Mã giảm giá chưa được áp dụng
 | 
MMS (67)
 | 
Mã giảm giá chưa được áp dụng. Quý khách có muốn tiếp tục giao dịch?

 | 
9
 | 
Mã giảm giá đang bị khóa
 | 
MMS (68)
 | 
Mã giảm giá đang bị khóa. Quý khách có muốn tiếp tục giao dịch?

 | Thanh toán QR customer (QR thanh toán)
 | TT | Case | Tác nhân | Thông báo lỗi | Mô tả thêm
 | 1 | Mã giảm giá không đúng  | Mã GG sai | 
MMS (61) | 
Mã giảm giá không đúng. Quý khách có muốn tiếp tục giao dịch? | 

Trả về cùng nội dung tin OTT thanh toán

 | Mã GG hết hiệu lực thời gian
 | Mã GG bị khóa
 | 2 | Kiểm tra số lần sử dụng được mã giảm giá > n lần cấu hình tại MMS MMS | (Qúa số lần áp dụng KH/ CTKM) | MMS (66) | Số lần sử dụng mã khuyến mãi tại đại lý này đã hết. Qúy khách có muốn tiếp tục giao dịch?
 | (Qúa số lần áp dụng KH/chu kì ngày, tuần, tháng)
 | 3 | Mã giảm giá còn hiệu lực về thời gian nhưng hết số lượng cho phép  | (Hết số lượng mã GG) | MMS (64) | Số lượng mã giảm giá đã hết. Quý khách có muốn tiếp tục giao dịch?
 | 4 | Giao dịch không được giảm giá do số tiền < A VNĐ  | (hóa đơn/đơn hàng có nợ cước hoặc số tiền < A VNĐ) | MMS (65) | Số tiền giao dịch chưa đạt mức tối thiểu để áp dụng mã khuyến mãi. Qúy khách có muốn tiếp tục giao dịch?
 | 5 | Merchant không có trong danh sách được cấu hình theo chương trình giảm giá  | 
 | MMS (63) | Đơn hàng không được giảm giá do đơn vị kinh doanh chưa tham gia chương trình. Quý khách có muốn tiếp tục giao dịch?
 | 6 | Ngân hàng không có trong danh sách áp dụng KM  | 
 | MMS (62) | Đơn hàng không được giảm giá do ngân hàng thanh toán không hỗ trợ. Quý khách có muốn tiếp tục giao dịch?
 | 7 | Kiểm tra nhập mã giảm giá chưa được áp dụng  | (Mã GG Chờ hoạt động) | MMS (67) | Mã giảm giá chưa được áp dụng tại thời điểm này. Quý khách có muốn tiếp tục giao dịch?
 | 8 | Không có chương trình khuyến mại | 
 | MMS (60, 48) | Không tồn tại chương trình khuyến mại, giao dịch không được giảm giá. Quý khách có muốn tiếp tục giao dịch?

---


## 29. URD_MB_COOPBANK_QRNapas

> **Page ID:** `64251414` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/64251414

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

### 29.1. MB_Quét QR Napas

> **Page ID:** `64251634` · **Version:** 9
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/64251634

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
23/02/2022
 | A | TrangVT | Nhập phiên bản tài liệu cũ, ví dụ: V.1 | 
Nhập mô tả các thay đổi trong tài liệu sau các lần cập nhật
 | V1.0
 | 08/03/2022  | M | TrangVT | V1.0 | Tách serviceCode của Chuyển tiền nhanh 247 qua tK bằng mã QR và Chuyển tiền nhanh 247 qua số thẻ bằng mã QR | V1.2
 | 05/07/2023 | M | HongLT | V1.2 | Bổ sung hiển thị tài khoản nguồn khi quét mã QR của STK có Alias | V2.0
 | 
16/08/2023 
 | M | HongLT | V2.0 | 
Cập nhật: Sau khi quét QR Napas (Bao gồm CK QR nội bộ cùng chủ/ khác chủ qua STK, QR liên ngân hàng qua STK và qua số thẻ) không cho phép chỉnh sửa các thông tin:

• Ngân hàng thụ hưởng
• Số tài khoản thụ hưởng
• Không cho chọn danh bạ
• Số tiền (Nếu có thông tin từ QR)
• Nội dung giao dịch (Nếu có thông tin từ QR) | 

Mục lục

### 1/ Tóm tắt Use Case
 | Use Case Name: | Chuyển tiền bằng mã QR
 | Use Case ID: | UC_QRNAPAS_02
 | Use Case Description: | 
Là người dùng, tối muốn thực hiện được các giao dịch chuyển tiền nội bộ - chuyển tiền nhanh 247 qua QR Napas

 | Actor: | 
KH, App Client, App Server, Bank, Napas.

 | Priority: | Medium
 | Trigger: | 
KH thực hiện chuyển tiền bằng mã QR

 | 
Pre-Condition:
 | 
1/ KH đăng nhập thành công ứng dụng

2/ KH có tài khoản nguồn hợp lệ để thực hiện giao dịch

3/ Tài khoản nguồn của KH có đủ số dư để thực hiện giao dịch

 | Post-Condition: | 
1/ KH thực hiện lệnh chuyển tiền bằng mã QR thành công

2/ Tài khoản nguồn của KH bị trừ số tiền giao dịch (bao gồm cả phí nếu có)

3/ Tài khoản/số thẻ thụ hưởng nhận được số tiền chuyển tương ứng (trừ phí nếu có)

4/ Hệ thống MB ghi nhận giao dịch chuyển tiền bằng mã QR vào Activity log

5/ Hệ thống MB ghi nhận giao dịch chuyển tiền bằng mã QR vào Transaction history

 | Basic Flow: | 
1/ KH đăng nhập ứng dụng

2/ KH chọn chức năng chuyển tiền bằng mã QR

3/ KH quét mã QR có định dạng chuẩn của Napas

4/ KH chọn tài khoản nguồn thực hiện giao dịch

5/ KH xác nhận giao dịch

6/ KH xác thực giao dịch

7/ Bank thực hiện hạch toán giao dịch

7/ Hệ thống MB ghi nhận giao dịch chuyển tiền bằng mã QR vào Activity log

8/ Hệ thống MB ghi nhận giao dịch chuyển tiền bằng mã QR vào Transaction history

9/ KH nhận được kết quả thực hiện giao dịch

 | Alternative Flow: | 
Nhập các bước tuần tự của luồng hợp lệ nhưng rẽ nhánh theo từng dòng có đầu mục thứ tự. Ví dụ: 1. KH đăng nhập ứng dụng; 2. KH chọn chức năng "Chuyển tiền nội bộ"; 3. KH chọn danh bạ thụ hưởng, số tiền, nội dung chuyển tiền; Tiếp theo mục 4 của Basic Flow.

 | Exception Flow: | 
Nhập các trường hợp ngoại lệ chính khiến usecase không thể tiếp tục. Ví dụ: 1. KH thực hiện khởi tạo giao dịch không thành công; 2. KH thực hiện xác thực giao dịch không thành công; 3. KH chọn hủy lệnh giao dịch.

 | Bussiness Rules: | 
Nhập danh sách các rule quy định (nếu có) liên quan tới chính sách, nghiệp vụ quan trọng. Ví dụ: BR-1: KH thực hiện xác thực giao dịch sai thông tin OTP 3 lần liên tiếp sẽ bị khóa chức năng gửi OTP trong vòng 30 phút.

 | Non-Funtional Requiremnt: | 
Nhập các yêu cầu về phi tài chính liên quan tới usecase. Ví dụ: NFR-1: Thời gian hiệu lực xác thực giao dịch là 120 giây.

 | Config: | 
Nhập danh sách các bảng, config sử dụng cho chức năng này theo quy định. Ví dụ:

1. Bảng Service Type: Chuyển tiền

2. Bảng Service MB: Chuyển tiền nội bộ cùng chủ, Chuyển tiền nội bộ khác chủ

3. Bảng Config:

Tên config 1 = {A}

Tên config 2 = {A,B}

Tên config 3 = {"listConfig": [{"key1": "value1","key2":"value1"},{"key1": "value2","key2":"value2"}]}

 | Database Table of Backend: | 
Nhập các bảng trên Backend có lưu trữ dữ liệu tra cứu liên quan tới chức năng này. Ví dụ:

1. Bảng [Transaction History]: Ghi nhận lịch sử giao dịch

2. Bảng [SMS History]: Ghi nhận lịch sử gửi SMS OTP

3. Bảng [Soft History Transaction]: Ghi nhận lịch sử xác nhận giao dịch Soft

4. Báo cáo [Summary Transaction]: Ghi nhận báo cáo giao dịch chuyển tiền nội bộ

5. Báo cáo [Transfer Detail]: Ghi nhận chi tiết giao dịch chuyển tiền nội bộ

### 2/ Luồng sơ đồ

#### Sơ đồ

<Insert flowchart> 

#### Danh sách API
 | 
 | Tên API | Luồng gọi API | Input | Output | Ghi chú
 | Truy cập chức năng
 | 1 | 
Lấy danh sách tài khoản nguồn
 | Client-server-bank | 

Xem chi tiết

 | 

Xem chi tiết
Tên chủ tài khoản : accountName
Số tài khoản : accountNo
Chi nhánh mở : branchName
Số dư thực tế : balance
Số dư khả dụng : availBalance
Số dư phong tỏa : amountBlock
Lãi cộng dồn : accrued_cr
Lãi suất TKTT: interestRate
Hạn mức thấu chi : todLimit
Lãi thấu chi : acy_accrued_dr_ic
Lãi suất thấu chi : ovdRate
Ngày mở tài khoản  : open_Date

 | 

### 3/ Luồng màn hình

#### Danh sách màn hình

##### MH1: Màn hình quét QR

Luồng màn hình chuyển tiền nội bộ trong Co-opbank

##### MH2.1: Khởi tạo chuyển tiền nội bộ cùng chủ - quét QR tĩnh

##### MH2.1: Khởi tạo chuyển tiền nội bộ cùng chủ  - quét QR động

##### MH3.1: Khởi tạo chuyển tiền nội bộ khác chủ - quét QR tĩnh

##### MH3.2: Khởi tạo chuyển tiền nội bộ khác chủ - quét QR động

Luồng màn hình chuyển tiền nhanh 24/7

##### MH4.1: Khởi tạo chuyển tiền nhanh 24/7 qua TK - quét QR tĩnh

##### MH4.2: Khởi tạo chuyển tiền nhanh 24/7 qua TK - quét QR động

##### MH5.1: Khởi tạo chuyển tiền nhanh 24/7 qua thẻ - quét QR tĩnh

##### MH5.2: Khởi tạo chuyển tiền nhanh 24/7 qua thẻ - quét QR động

#### Mô tả màn hình

MH1: Quét mã QR

• Xem mô tả chi tiết tại 
##### MH2.1/2.2: Luồng màn hình chuyển tiền nội bộ cùng chủ

###### a) Màn hình khởi tạo
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
Chuyển tiền nội bộ cùng chủ

 | 
4
 | 
Thông tin người chuyển
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
6
 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | 
X
 | 
--
 | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do bank server trả về
Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.
Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 
7
 | 
Thông tin người hưởng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
8
 | 
Tài khoản thụ hưởng
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị số tài khoản thụ hưởng đọc từ QR

(Trường hợp quét QR của STK có Alias - Vẫn hiển thị số tài khoản thụ hưởng đọc được từ QR)

 | 
10
 | 
Thông tin chuyển tiền

 | 
11
 | 
Số tiền
 | 
Label/Textbox phụ thuộc vào loại QR động/ tĩnh
 | 
Number
 | 
X
 | 
13
 | 
• Đối với QR động: Hiển thị số tiền đọc được từ QR và không cho phép sửa lại số tiền
• Đối với QR tĩnh: Cho phép nhập số tiền:
- Hiển thị ngăn cách hàng nghìn bằng dấu “,”

- Độ dài 13 ký tự bao gồm cả dấu “,  “

- Hiển thị đơn vị tiền tệ mặc định “VND”

- Không nhập số bắt đầu bằng số 0

- Focus ô Số tiền → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

- Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo quy tắc gợi ý chung trong BẢNG MÃ LỖI CHUNG 6: Quy tắc hiển thị thông tin]]>

 | 12 | 
Đối tượng chịu phí
 | 
Combobox
 | 
Select
 | 
X
 | 
--
 | 
Cho phép chọn “Người chuyển trả” hoặc “Người nhận trả”

Mặc định hiển thị “Người chuyển trả”

 | 
13
 | 
Nội dung giao dịch
 | 
Label/Textbox phụ thuộc vào loại QR động/ tĩnh
 | 
Text
 | 
X
 | 
210
 | 
• Đối với QR động: Hiển thị nội dung đọc được từ QR và không cho phép sửa
• Đối với QR tĩnh: Mặc định hiển thị: tên người chuyển (viết hoa không dấu) + “chuyen tien”. Tên người chuyển lấy theo tên tài khoản nguồn do bank server trả về. Cho phép nhập lại nội dung giao dịch:
- Cho phép nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():

- Hiển thị số ký tự nhập/số ký tự tối đa 210 kí tự

- Focus ô Nội dung giao dịch → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

 | 
14
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
Mặc định Enable

###### b) Màn hình xác nhận giao dịch/màn hình xác thực giao dịch/màn hình kết quả giao dịch -> Tham khảo mô tả chi tiết luồng màn hình chức năng 

##### MH3.1/3.3: Luồng màn hình chuyển tiền nội bộ khác chủ

###### a) Màn hình khởi tạo
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
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Chuyển tiền nội bộ khác chủ

 | 
4
 | 
Thông tin người chuyển
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
5
 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | 
x
 | 
--
 | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách do bank server trả vềHiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 
6
 | 
Thông tin người hưởng

 | 
7
 | 
Tài khoản thụ hưởng
 | 
Label
 | 
Read Only
 | 
x
 | 
--
 | 
Hiển thị số tài khoản đọc được từ QR

(Trường hợp quét QR của STK có Alias - Vẫn fill số tài khoản thụ hưởng đọc được từ QR)

 | 
8
 | 
Tên người thụ hưởng
 | 
Label
 | 
Read only
 | 

 | 

 | 
Hiển thị thông tin tên người thụ hưởng đọc được từ QR

 | 
9
 | 
Lưu danh bạ thụ hưởng
 | 
Switch button
 | 
click
 | 
-
 | 
-
 | 
Mặc định: OFF

Cho phép thực hiện switch ON/OFF

 | 10 | Tên gợi nhớ | Textbox | Text | 
 | 20 | 
Chỉ hiển thị khi nút Lưu người thụ hưởng switch ON

• Cho nhập ký tự tiếng Việt có dấu
 | 
11
 | 
Số tiền
 | 
Label/Textbox phụ thuộc vào loại QR động/ tĩnh
 | 
Number
 | 
X
 | 
13
 | 
• Đối với QR động: Hiển thị số tiền đọc được từ QR và không cho phép sửa lại số tiền
• Đối với QR tĩnh: Cho phép nhập số tiền:
- Hiển thị ngăn cách hàng nghìn bằng dấu “,”

- Độ dài 13 ký tự bao gồm cả dấu “,  “

- Hiển thị đơn vị tiền tệ mặc định “VND”

- Không nhập số bắt đầu bằng số 0

- Focus ô Số tiền → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

- Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo quy tắc gợi ý chung trong BẢNG MÃ LỖI CHUNG 6: Quy tắc hiển thị thông tin]]>

 | 
12
 | 
Đối tượng chịu phí
 | 
Combobox
 | 
Select
 | 
--
 | 
--
 | 
Cho phép chọn “Người chuyển trả” hoặc “Người nhận trả”

Mặc định hiển thị “Người chuyển trả”

 | 
13
 | 
Nội dung giao dịch
 | 
Label/Textbox phụ thuộc vào loại QR động/ tĩnh
 | 
Text
 | 
Yes
 | 
210
 | 
• Đối với QR động: Hiển thị nội dung đọc được từ QR và không cho phép sửa
• Đối với QR tĩnh: Mặc định hiển thị: tên người chuyển (viết hoa không dấu) + “chuyen tien”. Tên người chuyển lấy theo tên tài khoản nguồn do bank server trả về. Cho phép nhập lại nội dung giao dịch:
- Cho phép nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():

- Hiển thị số ký tự nhập/số ký tự tối đa 210 kí tự

- Focus ô Nội dung giao dịch → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

 | 
14
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
Mặc định Enable

###### b) Màn hình xác nhận giao dịch/màn hình xác thực giao dịch/màn hình kết quả giao dịch -> Tham khảo mô tả chi tiết luồng màn hình chức năng Chuyển tiền nội bộ khác chủ

##### MH4.1/4.2: Luồng màn hình chuyển tiền nhanh 247 qua tài khoản bằng mã QR

###### a) Màn hình khởi tạo
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
Tiêu đề màn hình
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Chuyển tiền qua tài khoản

 | 
4
 | 
Thông tin người chuyển
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 

 | 
6
 | 
Tài khoản nguồn
 | 
Combobox
 | 
List
 | 
x
 | 
--
 | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán đầu tiên trong danh sách bank server trả về
Hiển thị số tài khoản + Số dư khả dụng tương ứng và đơn vị tiền tệ.
Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)

 | 
7
 | 
Thông tin người hưởng

 | 
8
 | 
Tài khoản thụ hưởng
 | 
Label
 | 
Read Only
 | 
x
 | 
30
 | 
Hiển thị số tài khoản thụ hưởng đọc được từ QR

 | 9 | 
Tên người thụ hưởng
 | 
Label
 | 
Read only
 | 

 | 

 | 
Hiển thị thông tin tên người thụ hưởng đọc được từ QR

 | 10 | Ngân hàng thụ hưởng | Label | Read only | x | 
 | 
Lấy đầu BankCode của NH hưởng đã return hoặc mã QR và mapping với đầu BankCode ở danh sách NH hưởng ở Co-opbank -> Hiển thị thông tin ngân hàng hưởng mapping được

Không cho phép sửa

 | 
12
 | 
Lưu danh bạ thụ hưởng
 | 
Switch Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định: OFF

Cho phép thực hiện switch ON/OFF

 | 
 | Tên gợi nhớ | Textbox | Input | 
 | 20 | 
Chỉ hiển thị khi nút Lưu danh bạ ở trạng thái ON

• Cho nhập ký tự tiếng Việt có dấu
 | 
13
 | 
Số tiền
 | 
Label/Textbox phụ thuộc vào loại QR động/ tĩnh
 | 
Number
 | 
X
 | 
13
 | 
• Đối với QR động: Hiển thị số tiền đọc được từ QR và không cho phép sửa lại số tiền
• Đối với QR tĩnh: Cho phép nhập số tiền:
- Hiển thị ngăn cách hàng nghìn bằng dấu “,”

- Độ dài 13 ký tự bao gồm cả dấu “,  “

- Hiển thị đơn vị tiền tệ mặc định “VND”

- Không nhập số bắt đầu bằng số 0

- Focus ô Số tiền → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

- Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo quy tắc gợi ý chung trong BẢNG MÃ LỖI CHUNG 6: Quy tắc hiển thị thông tin]]>

 | 
14
 | 
Đối tượng chịu phí
 | 
Listbox
 | 
Select
 | 
--
 | 
--
 | 
 Cho phép chọn “Người chuyển trả” hoặc “Người nhận trả”

Mặc định hiển thị “Người chuyển trả”

 | 
15
 | 
Nội dung giao dịch
 | 
Label/Textbox phụ thuộc vào loại QR động/ tĩnh
 | 
Text
 | 
Yes
 | 
210
 | 
• Đối với QR động: Hiển thị nội dung đọc được từ QR và không cho phép sửa
• Đối với QR tĩnh: Mặc định hiển thị: tên người chuyển (viết hoa không dấu) + “chuyen tien”. Tên người chuyển lấy theo tên tài khoản nguồn do bank server trả về. Cho phép nhập lại nội dung giao dịch:
- Cho phép nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():

- Hiển thị số ký tự nhập/số ký tự tối đa 210 kí tự

- Focus ô Nội dung giao dịch → Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

 | 
16
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
Mặc định Enable

###### b) Màn hình xác nhận giao dịch/màn hình xác thực giao dịch/màn hình kết quả giao dịch -> Tham khảo mô tả chi tiết luồng màn hình chức năng 

##### MH5.1/5.2: Luồng màn hình chuyển tiền nhanh 247 qua thẻ bằng mã QR

###### a) Màn hình khởi tạo
 | | 
TT

> ⚠️ *Nội dung đã cắt ngắn (25475 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 29.2. MB_Tạo mã QR napas

> **Page ID:** `64251439` · **Version:** 12
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/64251439

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
23/02/2022
 | A | TrangVT | Nhập phiên bản tài liệu cũ, ví dụ: V.1 | 
Nhập mô tả các thay đổi trong tài liệu sau các lần cập nhật
 | V1.0
 | 14/03/2022 | M | TrangVT | 
 | Cập nhật theo comment design của bank | V1.1
 | 28/06/2023 | M | Hồng LT | 
 | Bổ sung yêu cầu tạo QR  đối với số tài khoản có Alias trạng thái Active | V2.0
 | 
 
 | M | ThuDM2 | V2.0 | Bổ sung thông tin MH Mã QR của tôi với Đối tượng là thành viên của QTDND | V2.0.1

Mục lục

### 1/ Tóm tắt Use Case
 | Use Case Name: | Tạo mã QR Napas
 | Use Case ID: | UC_QRNAPAS_01
 | Use Case Description: | 
Là người dùng, tối muốn tạo thành công mã QR napas theo số tài khoản thanh toán của tôi thành công

 | Actor: | 
KH, App Client, App Server, Bank, Napas.

 | Priority: | Medium
 | Trigger: | 
KH thực hiện tạo mã QR napas theo số tài khoản thành công

 | 
Pre-Condition:
 | 
1/ KH đăng nhập thành công ứng dụng

2/ KH có tài khoản nguồn hợp lệ để thực hiện tạo mã QR theo tài khoản đó

 | Post-Condition: | 
1/ KH tạo mã QR tới TKTT theo chuẩn QR Napas thành công.

 | Basic Flow: | 
1/ KH đăng nhập ứng dụng

2/ KH chọn chức năng Chuyển tiền

3/ KH chọn chức năng Chuyển tiền bằng mã QR

4/ KH nhấn chọn Tạo mã QR

5/ KH chọn tài khoản thanh toán và nhập thông tin tạo mã QR

6/ Ứng dụng thực hiện gen mã QR theo chuẩn QR Napas thành công

### 2/ Luồng sơ đồ

#### Danh sách API
 | 
 | Tên API | Luồng gọi API | Input | Output | Ghi chú
 | Truy cập chức năng, trước khi vào màn hình tạo mã QR
 | 1 | 
Lấy danh sách tài khoản nguồn
 | Client-Server-Bank | 

Xem chi tiết

 | 

Xem chi tiết
Tên chủ tài khoản : accountName
Số tài khoản : accountNo
Alias: Nếu có
Chi nhánh mở : branchName
Số dư thực tế : balance
Số dư khả dụng : availBalance
Số dư phong tỏa : amountBlock
Lãi cộng dồn : accrued_cr
Lãi suất TKTT: interestRate
Hạn mức thấu chi : todLimit
Lãi thấu chi : acy_accrued_dr_ic
Lãi suất thấu chi : ovdRate
Ngày mở tài khoản  : open_Date

 | 

### 3/ Luồng màn hình

#### Danh sách màn hình

##### MH1: Màn hình chuyển tiền

Chèn ảnh với chế độ "Original", kích thước 375 px

Chèn ảnh với chế độ "Original", kích thước 375 px

SDK QR Napas:

##### MH2: Màn hình quét QR

##### 

##### MH3: Màn hình tạo mã QR cho số TKTT (Bổ sung Alias- nếu có)

##### MH3: Màn hình tạo mã QR cho số TKTT - nhập thông tin 

##### (Bổ sung Alias- nếu có)

##### MH 3: Chọn danh sách tài khoản nguồn có Alias

##### MH4: Màn mình mã QR của tôi theo số TKTT (QR tĩnh) 

##### (Bổ sung Alias- nếu có)

##### MH5: Màn mình mã QR của tôi theo số TKTT (QR động)

##### (Bổ sung Alias- nếu có)

##### MH5: Mã QR của tôi - đối tượng là thành viên QTDND

#### Mô tả màn hình

##### MH1:  Truy cập chức năng - Màn hình chuyển tiền
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 
##### Ngân hàng Co-opbank

 | 1 | Màn hình chuyển tiền | -- | -- | -- | -- | 
Bổ sung thêm 1 tính năng:

• Chuyển tiền bằng mã QR

##### MH2: Màn hình quét QR
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

 | 1 | Icon Back | -- | -- | -- | -- | 
Nhấn back, xử lý quay về màn hình hiển thị trước đó

 | 2 | Icon Flash | -- | -- | -- | -- | 
Cho phép bật/tắt flash của thiết bị

Mặc định ở chế độ tắt flash.

 | 3 | Icon Chọn từ thư viện ảnh | -- | -- | -- | -- | Cho phép chọn 1 ảnh từ thư viện ảnh của thiết bị
 | 4 | Vùng camera quét QR | -- | -- | -- | -- | Hiển thị vùng camera quét QR
 | 5 | Ghi chú 1 | Label | Read Only | -- | -- | 
Fix tại client:

• Đưa mã QR vào trung tâm của camera, tiến trình quét mã sẽ diễn ra tự động.
 | 6 | Vùng logo | Picture | Read Only | -- | -- | 
Hiển thị 2 logo:

• Logo Bank
• Logo Napas
 | 7 | Vùng chức năng | Button | Click | -- | -- | 
Hiển thị nút chức năng:

• Tạo mã QR

##### MH3: Màn hình tạo mã QR
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

 | 1 | Tiêu đề | Label | Read Only | -- | -- | Tạo mã QR
 | 2 | Icon Back | -- | -- | -- | -- | 
Nhấn Back, hiển thị màn hình Quét QR trước đó

 | 3 | Ghi chú 1 | Label | Read Only | 
 | 
 | 
Fix tại client: "Quý khách vui lòng chọn tài khoản thanh toán để tạo mã QR"

 | 4 | Tài khoản nguồn | Combobox | List | Yes | -- | 
Mặc định hiển thị tài khoản thanh toán mặc định. Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về

Mỗi tài khoản hiển thị thông tin: (Hiển thị như mockup)

• Số tài khoản
• Tài khoản Alias (Nếu có)  
• Số dư khả dụng + đơn vị tiền tệ
Click vào mở ra màn hình popup chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết

Cho phép chọn 1 tài khoản thanh toán

 | 5 | Ghi chú 2 | Label | Read Only | 
 | 
 | 
Fix tại client: "Thông tin bổ sung tạo mã QR (nếu có):"

 | 6 | Số tiền  | Textbox | Number | -- | 13 | 
Mặc định trống

Nhập vào ô số tiền::

• Chỉ cho nhập ký tự số, tối đa 13 ký tự (bao gồm cả dấu phẩy). Không nhập số bắt đầu bằng số 0
• Hiển thị ngăn cách hàng nghìn bằng dấu “,”
• Hiển thị đơn vị tiền tệ mặc định “VND”
• Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
Hiển thị số tiền bằng chữ tương ứng khi nhập.

 | 7 | Nội dung  | Textbox | Text | -- | 25 | 
Mặc định trống

Cho phép nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/()

Cho phép xóa nhanh bằng icon "x"

 | 7 | Tạo mã QR | Button | Click | 
 | 
 | Nhấn nút, tham khảo logic xử lý

##### MH4: Màn hình mã QR của tôi;  MH5: Mã QR của tôi - đối tượng là thành viên QTDND
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu dữ liệu | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | Read Only | -- | -- | Mã QR của tôi
 | 2 | Icon back | Button | Click | -- | -- | 
Nhấn nút, hiển thị màn hình trước đó

 | 3 | Icon home | Icon | Click | 
 | 
 | Nhấn nút, hiển thị màn hình home
 | 4 | Ghi chú 1 | Label | Read Only | -- | -- | 
Fix tại client:

Gửi mã QR cho người khác để chuyển khoản nội bộ - liên ngân hàng Napas 24/7

 | 5 | Logo thương hiệu QR | Picture | Read Only | -- | -- | Hiển thị logo thương hiệu QR: VietQR
 | 6 | Ảnh QR | Picture | Read Only | -- | -- | Ảnh QR do client sinh
 | 7 | Logo Bank | Picture | Read Only | -- | -- | 
Hiển thị logo CoopBank

 | 8 | Logo Napas | Picture | Read Only | -- | -- | 
Hiển thị logo Napas

 | 9 | Logo QTDND | Picture | -- | -- | -- |  Chỉ hiển thị với đối tượng là thành viên QTDND
 | 10 | Tên QTDND | Label | Read Only | -- | -- | Chỉ hiển thị với đối tượng là thành viên QTDND
 | 
 | Thông tin
 | 1 | Tên khách hàng | Label | Read Only | -- | -- | Hiển thị tên khách hàng tại Bank
 | 2 | Số tài khoản | Label | Read Only | -- | -- | 
Hiển thị số tài khoản đã chọn gen mã QR

 | 3 | Số tài khoản Alias | Label | Read Only | -- | -- | 
Hiển thị số tài khoản Alias của số tài khoản đã chọn

 | 4 | Số tiền | 
 | 
 | 
 | 
 | Hiển thị số tiền + đơn vị tiền tệ (nếu tạo QR động)
 | 5 | Nội dung giao dịch | Label | Read Only | 
 | 
 | Hiển thị nội dung giao dịch đã nhập màn hình trước đó (nếu tạo QR động)
 | 6 | Ngân hàng/chi nhánh | Label | Read Only | -- | -- | 
Hiển thị tên ngân hàng và chi nhánh, cấu trúc:

• Ngân hàng <Tên ngân hàng viết tắt> - <Tên chi nhánh của tài khoản chọn gen mã QR lấy dữ liệu tại Bank>
 | 
 | Nút thao tác
 | 1 | Lưu ảnh | Icon | Click | -- | -- | 
Cho phép lưu ảnh QR qua các ứng dụng chia sẻ trên thiết bị của Khách hàng

Lưu ý: Ảnh lưu về thiết bị không bao gồm câu Ghi chú

 | 2 | Chia sẻ  | Icon | Click | -- | -- | 
Cho phép chia sẻ ảnh QR vào thư viện ảnh thiết bị của Khách hàng

Lưu ý: Ảnh lưu về thiết bị không bao gồm câu Ghi chú

### 4/ Luồng xử lý

##### Truy cập chức năng
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
Tại màn hình chuyển tiền, KH chọn chức năng "Chuyển khoản bằng mã QR"
 | 
App Client 
 | 
1/ Gửi yêu cầu  danh sách tài khoản thanh toán (lọc theo rule tài khoản được phép tạo QR như hiện tại)

2/  Xử lý khởi tạo yêu cầu truy cập SDK QR Napas. Thông tin cơ bản App Client truyền sang SDK:

• Bank Code
• Bank Name
• Họ tên khách hàng
• Mã màu ứng dụng
• Ngôn ngữ
• Loại chuyển khoản hỗ trợ:
• Nội bộ tới TK, Nhanh 24/7 tới TK, Nhanh 24/7 tới Thẻ
• Danh sách tài khoản thanh toán hợp lệ theo rule của Ngân hàng triển khai:
• Số tài khoản
• Số dư khả dụng
• Chi nhánh mở tài khoản
 | SDK QR Napas | Hiển thị màn hình Quét mã QR

SDK QR Napas:

##### MH1: Quét mã QR
 | | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhấn vào chức năng "Quét mã QR" | SDK QR Napas | Hiển thị màn hình quét mã QR
 | 2 | Nhấn vào chức năng "Tạo mã QR" | SDK QR Napas | 
Hiển thị màn hình tạo mã QR như mô tả

Lưu ý:

• Trong trường hợp không lấy được danh sách tài khoản thanh toán hoặc tài khoản thanh toán không hợp lệ, hiển thị label thông báo: Không lấy được danh sách tài khoản hoặc Quý khách không có tài khoản thanh toán hợp lệ để thực hiện chức năng này.
 | 3 | Nhấn icon hướng dẫn | Client | Hiển thị màn hình "Hướng dẫn" đã tích hợp dạng link trên app

##### MH2: Tạo mã QR
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Bấm chọn Tạo mã QR | Client | Gửi yêu cầu lấy danh sách tài khoản thanh toán
 | 
 | MB server | 
Gửi yêu cầu lấy danh sách tài khoản thanh toán sang HT Bank

 | 
 | HT Bank | 
Trả kết quả bao gồm:

• Danh sách tài khoản thanh toán hợp lệ và Alias (có trạng thái active) của tài khoản thanh toán đó (nếu có) 
 | 
 | MB server | 
Trả kết quả cho Client

 | 
 | Client/ SDK QR Napas | Hiển thị màn hình Tạo mã QR với danh sách tài khoản nguồn do Bank đã trả
 | Bấm chọn "Tài khoản nguồn" | SDK QR Napas | Hiển thị popup danh sách tài khoản + Alias của số tài khoản đó nếu có theo dữ liệu App Client đã truyền sang
 | Chọn 1 tài khoản | SDK QR Napas | Fill số tài khoản đã chọn + số dư khả dụng trên màn hình như mô tả
 | 3 | Nhấn "Tạo mã QR" | SDK QR Napas | Thực hiện gen mã QR theo quy định (QR tĩnh, QR động)

### 5/ Định dạng QR Chuyển khoản Napas

• 
#### Đến tài khoản (Tĩnh)
 | Tên trường | Tag | Độ dài | Mô tả | Giá trị
 | Payload Format Indicator
Phiên bản dữ liệu | 00 | 2 | 

 | 01
 | Point of initiation method
Phương thức khởi tạo | 01 | 2 | 

 | 11
 | Consumer Account Information
Thông tin định danh người thụ hưởng | 38 | 57 | 00 | Mã đơn vị phát triển (Napas) | A000000727
 | 01 | Mã đầu BIN của Ngân hàng thụ hưởng và Số tài khoản thụ hưởng | 000697040301130011012345678
 | 02 | Mã dịch vụ chuyển tiền nhanh 24/7 bằng QR đến tài khoản. | QRIBFTTA
 | Transaction Currency
Mã tiền tệ | 53 | 03 | 

 | 704
 | Country Code
Mã quốc gia | 58 | 02 | 

 | VN
 | 
CRC
 | 63 | 04 | 
 | 3E09

• 
#### Đến tài khoản (Động)
 | Tên trường | Tag | Độ dài | Mô tả | Giá trị
 | Payload Format Indicator
Phiên bản dữ liệu | 00 | 2 | 

 | 01
 | Point of initiation method
Phương thức khởi tạo | 01 | 2 | 

 | 12
 | Consumer Account Information
Thông tin định danh người thụ hưởng | 38 | 57 | 00 | Mã đơn vị phát triển (Napas) | A000000727
 | 01 | Mã đầu BIN của Ngân hàng thụ hưởng và Số tài khoản thụ hưởng | 000697040301130011012345678
 | 02 | Mã dịch vụ chuyển tiền nhanh 24/7 bằng QR đến tài khoản. | QRIBFTTA
 | Transaction Currency
Mã tiền tệ | 53 | 03 | 

 | 704
 | 
Transaction Amount

Số tiền giao dịch
 | 54 | 06 | 
 | <Theo số tiền KH nhập>
 | Country Code
Mã quốc gia | 58 | 02 | 

 | VN
 | 
Additional Data Field Template

Thông tin bổ sung
 | 62 | 
 | 08 | Nội dung chuyển khoản | <Theo nội dung chuyển khoản KH nhập>
 | 
CRC
 | 63 | 04 | 
 | 3E09

---


