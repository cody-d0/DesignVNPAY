# 📋 Auth & Security

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `security/`
> **Trích xuất:** 2026-03-28

---

## 1. URD_ Accessibility

> **Page ID:** `257982899` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/257982899

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

### 1.1. Nghiệp vụ xử lý liên quan tới quyền Accessibility

> **Page ID:** `251823478` · **Version:** 14
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/251823478

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | HongLT | 
 | Giai đoạn 1: Xử lý chặn Accessibility tại Client theo PA3 | V.1

Mục lục
none

### 1/ Tóm tắt Use Case

 | Use Case Name | Chặn và thông báo khi KH sử dụng ứng dụng ngân hàng mà trên thiết của KH có ứng dụng bật ON quyền Accessibility
 | Use Case ID | 

 | Use Case Description | Là KH sử dụng ứng dụng Banking (ứng dụng đích), trên thiết bị của khách hàng có cài đặt ứng dụng nguồn (có cài đặt bật ON quyền Accessbility), khi truy cập các chức năng trên ứng dụng đích có giao tiếp giữa App Client gọi lên Server sẽ nhận được thông báo lỗi trong các trường hợp quy định 
 | Actor | 
App Client, Server

 | Priority | 
trueRedHighest

 | Trigger | 
• KH mở ứng dụng
 | 
Pre-Condition
 | 
• KH đã cài đặt ứng dụng nguồn (ứng dụng tấn công và KH đã cài đặt bật ON quyền Accessbility cho ứng dụng này) trên hệ điều hành Android với 3 trường hợp có thể xảy ra:
• Có sử dụng  Target Package Name của ứng dụng đích hoặc để trống
• Cặp Vender + Owner Package Name không thuộc cấu hình Whitelist
• KH đã cài ứng dụng đích có bản cập nhật xử lý nghiệp vụ này
• Server cấu hình bảng tham số Whitelist gồm: Vendor, Package

 | Post-Condition | 
KH nhận được thông báo lỗi không cho phép đi tiếp trong các trường hợp:

• 
• 
•  KH đã cài đặt bật ON quyền Accessbility và có cài đặt thông tin Target Package Name của BIDV SmartBanking
•  KH đã cài đặt bật ON quyền Accessbility và không cài đặt thông tin Target Package Name và cặp Vendor, Owner Package name không nằm trong danh sách Whitelist
 | Basic Flow | 

 | Alternative Flow | 

 | Exception Flow | 

 | Bussiness Rules | 

 | Non-Funtional Requiremnt | 

### 2/ Thuật ngữ

 | 
 | Thuật ngữ | Diễn giải | Ví dụ
 | 1 | ACCESSIBILITY  |  Mục cài đặt hỗ trợ các tính năng trợ năng được tích hợp trong hệ điều hành Android/IOS. Các tính năng này được thiết kế để giúp người khuyết tật, bao gồm cả những người khiếm thị, khiếm thính hoặc thể chất, sử dụng thiết bị Android của họ dễ dàng hơn  | TalkBack ở ANDROID, VoiceControl  ở IPHONE
 | 2 | VENDOR | Hãng thiết bị  | 
samsung, oppo, xiaomi...

 | 3 | OWNER_PACKAGE_NAME | Ứng dụng cài đặt trên thiết bị, có yêu cầu cấp quyền Hỗ trợ Accessibility | 
com.samsung.android.accessibility.talkback

com.microsoft.appmanager...

 | 4 | TARGET_PACKAGE_NAME | Ứng dụng cài đặt trên thiết bị, được một ứng dụng khác yêu cầu cấp các quyền  | 

 | 5 | VIEW_ACTION | Các quyền điều khiển của ứng được được ON quyền Hỗ trợ Accessibility, trên các ứng dụng đích  | TYPE_VIEW_CLICKED, TYPE_VIEW_FOCUSED, TYPE_VIEW_ACCESSIBILITY_FOCUSED

### 3/ Bảng dữ liệu cấu hình thêm

#### 3.1/ CONFIG

 | 
 | Config_Code | Value | Description
 | 1 | TIME_CACHE_ACCESSIBILITY | 0.5h, 1h, 2h ... | 
Thời gian cấu hình cho phép Client lưu Cache danh sách Whitelist

#### 3.2/ WHITELIST_VENDOR_ACCESSBILITY

Cặp key: VENDOR + OWNER_PACKAGE_NAME
 | 
 | Field | Description | Note
 | 1 | VENDOR | Hãng cung cấp thiết bị di động (samsung, oppo,...)  | 

 | 2 | OWNER_PACKAGE_NAME | Package Name do chính Vendor cung cấp | 

 | 3 | VIEW_ACTION | Các quyền liên quan tới Package Name được cung cấp | 

Danh sách whitelist vendor package: https://docs.google.com/spreadsheets/d/1WHGue1F-aAGuQQ8kR9efqG0ZcsdyWvGRLGZv-sbPLh8/edit#gid=0

### 4/ Luồng xử lý

trueAccessfalseautotoptrue14024

#### 4.1. Giai đoạn 1
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả xử lý

 | 
1
 | 
• TH1: KH bắt đầu mở ứng dụng
• TH2: KH đang ở MH login nhưng chưa đăng nhập và quay ra ON Accessibility và Quay lại MH login
• TH3: KH đã đăng nhập vào App và quay ra ON Accessibility và quay lại bất kỳ màn hình nào trong App | 
MB App
 | 
1/ Kiểm tra trên thiết bị KH sử dụng có ứng dụng nào bật ON quyền Accessibility không?

• 
Nếu không: Xử lý theo nghiệp vụ hiện tại

• 
Nếu có: Chuyển bước 2

2/  Lấy thông tin  Vendor, Owner Package name, View Action, Target Package Name của các ứng dụng đã cài bật quyền Accessibility và kiểm tra

 | TT | Trường hợp | Thông báo | Xử lý
 | 1 | 
Nếu Target Package Name = Package Name của App chủ 

 | 
Ứng dụng <Danh sách các Tên ứng dụng của Owner Package name đang bật ON Accessibility tới ứng dụng Co-opbank> đang cài đặt trên thiết bị của Quý khách có thể không an toàn vì đang được cấp quyền điều khiển Trợ năng/ Accessibility. Vui lòng gỡ bỏ Tất cả các ứng dụng này để tránh nguy cơ rủi ro và tiếp tục sử dụng ứng dụng Co-opBank Mobile Banking
 | Đóng thông báo, thoát ứng dụng
 | 3 | 
Nếu Target Package Name khác Package Name của App chủ
 | 

 | 
• Nếu có sự kiện thay đổi về quyền ON/OFF Accessibility -->
Thực hiện gửi ngay yêu cầu lấy danh sách Whitelist Vendor accessibility sang MB Server

• Nếu chưa có cache lưu danh sách Whitelist → Thực hiện gửi Gửi yêu cầu lấy danh sách Whitelist Vendor accessibility sang MB Server
• Nếu đã có danh sách Whitelist lưu cache tại Client trước đó → Kiểm tra thời gian lưu Cache:
- Nếu thời gian thực hiện request >= Thời gian lưu cache server trả→ Gửi yêu cầu lấy danh sách Whitelist vendor accessibility sang MB Server

- Nếu thời gian thực hiện request >= Thời gian lưu cache server trả → Kiểm tra thông tin cặp Vendor, Owner Package name theo danh sách Whitelist đã cache trước đó (Xem mô tả chi tiết bên dưới)

 | 

 | 
 | 
MB Server
 | 
Trả kết quả gồm

• Whitelist vendor accessibility
• Thời gian lưu cache = (Thời gian trả kết quả cho client + Thời gian cấu hình tại TIME_CACHE_ACCESSIBILITY)
 | 

 | 
 | 
MB App
 | 
1/ Nhận kết quả do MB server trả:

• Danh sách Whitelist trống hoặc kết quả Timeout → Hiển thị thông báo "Ứng dụng (Danh sách tên ứng dụng cấp quyền Acessbility không nằm trong Whitelist) đang cài đặt trên thiết bị của Quý khách có thể không an toàn vì đang được cấp quyền điều khiển Trợ năng/ Accessibility. Vui lòng gỡ bỏ hoặc tắt quyền Trợ năng/ Accessibility của Tất cả các ứng dụng này để tránh nguy cơ rủi ro và tiếp tục sử dụng ứng dụng Co-opBank Mobile Banking. Xem hướng dẫn tắt quyền Trợ năng/ Accessibility tại đây".
Bấm vào Xem hướng dẫn tắt quyền Trợ năng/ Accessibility tại đây → mở ra link html hướng dẫn sử dụng tắt quyền trợ năng

• 
• Nút "Đồng ý": Điều hướng KH đến mục "Setting>Accessibility>Installed services" của thiết bị , đồng thời Thoát ứng dụng
• 
• Nút "Bỏ qua":  Thoát ứng dụng
• Có kết quả danh sách Whitelist + thời gian lưu cache whitelist tại client → Chuyển bước 2
2/ Kiểm tra thông tin cặp Vendor, Owner Package name có nằm trong danh sách  WHITELIST_VENDOR_Accessibility (khi check không phân biệt hoa thường):

• 
Tất cả các Cặp: Vendor và Owner Package Name thuộc danh sách Whitelist cấu hình → Xử lý nghiệp vụ như hiện tại

• 
Có ít nhất 1 cặp: Vendor và Owner Package Name không thuộc bảng cấu hình → Hiển thị cảnh báo ""Ứng dụng (Danh sách tên ứng dụng cấp quyền Acessbility không nằm trong Whitelist) đang cài đặt trên thiết bị của Quý khách có thể không an toàn vì đang được cấp quyền điều khiển Trợ năng/ Accessibility. Vui lòng gỡ bỏ hoặc tắt quyền Trợ năng/ Accessibility của Tất cả các ứng dụng này để tránh nguy cơ rủi ro và tiếp tục sử dụng ứng dụng Co-opBank Mobile Banking. Xem hướng dẫn tắt quyền Trợ năng/ Accessibility tại đây

Bấm vào Xem hướng dẫn tắt quyền Trợ năng/ Accessibility tại đây → mở ra link html hướng dẫn sử dụng tắt quyền trợ năng

• 
• Nút "Đồng ý": Điều hướng KH đến mục "Setting>Accessibility>Installed services" của thiết bị , đồng thời Thoát ứng dụng
• 
• Nút "Bỏ qua":  Thoát ứng dụng

---

### 1.2. Nghiệp vụ xử lý liên quan tới quyền Accessibility (nâng cấp)

> **Page ID:** `272466284` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/272466284

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | M | HongLT | V1.0.0 | 
Bổ sung so với ver trước đó của tài liệu :

• SDK Accesbility:
• Logic gửi yêu cầu lấy nguồn cài ứng dụng bật quyền ON Accessbility trên thiết bị
• Các output gửi ra cho App Client
• Lib Accesbility:
• Bổ sung 2 tham số: CHECK_SOURCE_SAFE, SOURCE_SAFE
• Logic check: CHECK_SOURCE_SAFE, SOURCE_SAFE
• Server dự án:
• Thống nhất trả về trạng thái Status Accessbility: 
• 1: Không an toàn
• 2: An toàn
• 3: Nghi ngờ
• Server kiểm tra eTag_Accessbility không đổi và trả kết quả tham số "isChange" = "False"
• Bổ sung nghiệp vụ bàn phím ảo | V1.1.0

Mục lục
none

### 1/ Tóm tắt Use Case

 | Use Case Name | Chặn ứng dụng độc tấn công bằng accessibility
 | Use Case ID | UC-AC
 | Use Case Description | 
KH sử dụng ứng dụng MobileBanking (ứng dụng đích), trên thiết bị của khách hàng có cài đặt ứng dụng nguồn (có cài đặt bật ON quyền Accessbility), khi truy cập các chức năng trên ứng dụng đích có giao tiếp giữa App Client gọi lên Server sẽ nhận được thông báo lỗi trong các trường hợp quy định 

 | Actor | 
KH, App client, App server

 | Priority | HIGHEST
 | Trigger | 
KH mở ứng dụng hoặc đang trong phiên đăng nhập nhưng ON quyền Accessbility

 | 
Pre-Condition
 | 
• KH đã cài đặt ứng dụng nguồn (ứng dụng tấn công và KH đã cài đặt bật ON quyền Accessbility cho ứng dụng này) trên hệ điều hành Android với 2 trường hợp có thể xảy ra:
• Có sử dụng  Target Package Name của ứng dụng đích hoặc để trống
• Cặp Vender + Owner Package Name không thuộc cấu hình Whitelist
• KH đã cài ứng dụng đích có bản cập nhật xử lý nghiệp vụ này
• BE cấu hình tham số và danh sách Whitelist vendor, whitelist big corp, blacklist
 | Post-Condition | 
KH nhận được thông báo lỗi không cho phép đi tiếp trong các trường hợp:

• KH đã cài đặt bật ON quyền Accessbility và có cài đặt thông tin Target Package Name của Co-opBank Mobile Banking
• KH đã cài đặt bật ON quyền Accessbility và không cài đặt thông tin Target Package Name và cặp Vendor, Owner Package name không nằm trong danh sách Whitelist
 | Basic Flow | 
• KH mở ứng dụng đích
• App Client truyền thông tin giao tiếp sang Server và SDK accessibility
• Server kiểm tra và trả kết quả cho App Client
• KH nhận được kết quả tương ứng theo từng trường hợp

### 2/ Mô tả tình huống

Rủi ro khi Attacker lợi dụng tính năng Accessiblity của HĐH Android

• Một số ứng dụng đã khai thác lỗ hổng và XD các kịch bản để thu thập thông tin người dùng và thực hiện các cuộc tấn công
• Tình huống cụ thể của Attacker: Kẻ gian gọi điện cho KH ==> attacker đọc cho KH đường link trên trình duyệt ==> trỏ đến trang web tương tự các appstore để download ứng dụng Attacker (vd ứng dụng thuế) ==> Attacker hướng dẫn KH cấp quyền Accessibility cho ứng dụng ==> tất cả thao tác của KH (gõ username/pass) bị collect và chuyển về máy chủ của attacker.
• Ứng dụng Attacker có thể:
• set Target package name = Co-opBank Mobile Banking ==> collect tất cả thông tin của ứng dụng khi KH thao tác
• set Target package name = NULL ==> collect thông tin của tất cả các ứng dụng trên device của KH.
• Attacker có thể viết 1 layer phía trước ứng dụng target ( 1 MH đen) ==> bật MH đen khi tấn công, người dùng ko nhìn thấy và thực hiện collect dc toàn bộ thông tin của KH.
### 3/ Thuật ngữ
 | 
 | Thuật ngữ | Diễn giải | Ví dụ
 | 1 | ACCESSIBILITY  |  Mục cài đặt hỗ trợ các tính năng trợ năng được tích hợp trong hệ điều hành Android/IOS. Các tính năng này được thiết kế để giúp người khuyết tật, bao gồm cả những người khiếm thị, khiếm thính hoặc thể chất, sử dụng thiết bị Android của họ dễ dàng hơn  | TalkBack ở ANDROID, VoiceControl  ở IPHONE
 | 2 | VENDOR | Hãng thiết bị  | samsung, oppo, xiaomi...
 | 3 | OWNER_PACKAGE_NAME | Ứng dụng cài đặt trên thiết bị, có yêu cầu cấp quyền Hỗ trợ Accessibility | 
com.samsung.android.accessibility.talkback

com.microsoft.appmanager...

 | 4 | TARGET_PACKAGE_NAME | Ứng dụng cài đặt trên thiết bị, được một ứng dụng khác yêu cầu cấp các quyền  | 

 | 5 | VIEW_ACTION | Các quyền điều khiển của ứng được được ON quyền Hỗ trợ Accessibility, trên các ứng dụng đích  | TYPE_VIEW_CLICKED, TYPE_VIEW_FOCUSED, TYPE_VIEW_ACCESSIBILITY_FOCUSED

### 4/ Luồng sơ đồ

#### 4.1/ Sơ đồ

trueUntitled Diagramfalseautotoptrue22721

#### 4.2/ Danh sách API
 | Bước thực hiện | Tên API | Luồng gọi API | Địa chỉ API | Input | Output | Ghi chú
 | 
Truy cập ứng dụng
 | 
Lấy danh sách whitelist
 | App Client - App Server | 
 | 

 | 

 | 

### 5/ Luồng xử lý

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
• TH1: KH bắt đầu mở ứng dụng
• TH2: KH đang ở MH login nhưng chưa đăng nhập và quay ra ON Accessibility và Quay lại MH login
• TH3: KH đã đăng nhập vào App và quay ra ON Accessibility và quay lại bất kỳ màn hình nào trong App | App Client | 
Gửi yêu cầu sang SDK Accessbility

 | 

 | 

 | SDK Accessbility | 
1/ Kiểm tra trên thiết bị KH có ứng dụng nào bật ON quyền Accessbility hay không?

• Nếu không: Trả kết quả cho App Client tiếp tục nghiệp vụ hiện tại
• Nếu có: Chuyển bước 2
2/ Gửi yêu cầu lấy thông tin nguồn cài ứng dụng của tất cả OwnerPackageName đã bật ON quyền Accessbility (API do Google cấp) và nhận kết quả:

• Không có kết quả: Chuyển bước 3
• Có kết quả: Chuyển bước 3
3/ Kiểm tra điều kiện gửi yêu cầu check Accessbility lên Server

• Đủ điều kiện → Trả kết quả cho App Client gửi yêu cầu check Accessbility
(Các trường hợp đủ điều kiện là:

• 
• 1. Chưa có eTag_Accessbility hoặc;
• 2. Đã có eTag_Accessbility và đã tới (x) phút (x là thời gian cho phép SDK lưu và sử dụng thông tin về Accesbility mà server đã trả trước đó) 
• 3. Có thay đổi ứng dụng bật quyền Accessbility trong thiết bị (on/off, xóa) => Truyền eTag_Accessbility = 0
• Chưa đủ điều kiện gửi check Accessbility và:
• 
• Trạng thái Status Accessbility đang lưu cache là không an toàn: Trả phản hồi cho App Client để cảnh báo
• Trạng thái Status Accessbility đang lưu cache là an toàn: Trả phản hồi cho App Client để tiếp tục nghiệp vụ hiện tại
• Trạng thái Status Accessbility đang lưu cache là chưa xác định: Trả phản hồi cho App Client để xử lý yêu cầu định danh KH
 | 

 | 

 | App Client | 
Nhận kết quả từ SDK Accessbility:

• Chưa đủ điều kiện gọi check Accessbility lên Server: Xử lý tương ứng với Status Accessbility do SDK Accessbility trả ra
• Đủ điều kiện gọi check Accessbility lên Server: Gửi yêu cầu cầu check Accessbility
{
   "user":"0977662075",
   "accessibility":{
      "ownerAccessibilityList":[
         {
            "targetPackageNameList":[
               
            ],
            "ownerAppName":"Accessibility menu",
            "a":"C9:00:9D:01:EB:F9:F5:D0:30:2B:C7:1B:2F:E9:AA:9A:47:A4:32:BB:A1:73:08:A3:11:1B:75:D7:B2:14:90:25",
            "osVersion":"10",
            "viewActionList":[
               
            ],
            "ownerPackageName":"com.android.settings"
         },
         {
            "targetPackageNameList":[
               "com.VCB",
               "com.vietinbank.ipay",
               "com.vnpay.bidv",
               "com.vnpay.Agribank3g"
            ],
            "ownerAppName":"Attacker",
            "ownerInstalledSource":"com.google.android.packageinstaller",
            "a":"29:C3:0E:70:69:68:2E:A7:FF:5B:22:78:A6:F5:30:AA:C7:7E:2F:D9:68:28:7D:2A:EA:C3:58:67:B4:23:8F:2E",
            "osVersion":"10",
            "viewActionList":[
               13,
               15,
               21,
               25
            ],
            "ownerPackageName":"com.vnpay.anti.attack2"
         }
      ],
      "vendorName":"Redmi"
   },
   "eTagAccessibility":"0", 

(Nếu chưa có eTag_Accessbility → truyền Null

 Nếu đã có eTag_Accessbility và không có sự thay đổi về quyền → eTag_Accessbility = eTag_Accessbility đã lưu trước đó

Nếu đã có eTag_Accessbility có sự thay đổi về quyền → eTag_Accessbility = 0)

   "mid":"3013",
   "ver":"5.5.5",
   "lang":"vi",
   "DT":"ANDROID",
   "E":"###0686e69a6977d48f###ffffffff-dd57-f817-ffff-ffffef05ac4a",
   "PM":"M2006C3MG",
   "OV":"29",
   "PS":"IS_SAFE",
   "ATS":"23:07:15:06:13:39"
}

 | 

 | 

 | App Server | 
Tiếp nhận và kiểm tra eTag_Accessbility:

• Nếu eTag_Accessbility = eTag_Accessbility hiện tại trên đang lưu trên Server: Trả kết quả cho App Client:
• isChange = False
• Nếu eTag_Accessbility khác eTag Accessbility hiện tại đang lưu trên Server: Gửi yêu cầu check Accessbility sang Lib Server
 | 

 | 

 | Lib Accessbility Server | 
Nếu tham số CHECK_SOURCE_SAFE = ON thì thực hiện

1/ Kiểm tra các ứng dụng bật quyền Accessbility theo điều kiện check nguồn cài:

• Nếu tất cả các nguồn cài ứng dụng bật quyền Accessbility là hợp lệ: Trả kết quả an toàn cho Server
• Nếu có ít nhất 1 nguồn cài ứng dụng bật quyền Accessbility là không hợp lệ: Trả kết quả không an toàn cho Server
Nếu tham số CHECK_SOURCE_SAFE = OFF thì thực hiện

2/ Kiểm tra các ứng dụng bật quyền Accessbility theo điều kiện check không phải nguồn cài:

• TH1: Có ít nhất 1 ứng dụng bật quyền Accessbility là không an toàn: Trả kết quả cho Server để cảnh báo trên ứng dụng KH đang sử dụng
• TH2: Tất cả các ứng dụng bật quyền Accessbility là an toàn: Trả kết quả cho Server xử lý nghiệp vụ như hiện tại
• TH3: Có ít nhất 1 ứng dụng bật quyền Accessbility nhưng chưa xác định là an toàn hoặc không an toàn: Trả kết quả cho Server để yêu cầu người dùng xác thực TouchID trên thiết bị
 | 

 | 

 | App Server | 
Nhận kết quả từ Lib Accessbility:

• Nếu Status Accessbility = NOT_SAFE 
• Lưu thông tin user và các dữ liệu liên quan tới xử lý quyền Accessbility vào DB
• Trả kết quả cho App Client
• Status Accessbility = 1
• eTag Accessbility
• Thời gian (x) phút (x là thời gian cho phép SDK lưu và sử dụng thông tin về Accesbility mà server đã trả)
• Danh sách ứng dụng không an toàn
• Trả câu thông báo
• Nếu Status = SAFE
• Trả kết quả cho App Client
• Status Accessbility = 2
• eTag Accessbility
• Thời gian (x) phút (x là thời gian cho phép SDK lưu và sử dụng thông tin về Accesbility mà server đã trả)
• Danh sách ứng dụng không an toàn: Null
• Nếu Status = SUSPECTED 
• Lưu thông tin user và các dữ liệu liên quan tới xử lý quyền Accessbility vào DB
• Trả kết quả cho App Client
• Status Accessbility = 3
• eTag Accessbility
• Thời gian (x) phút (x là thời gian cho phép SDK lưu và sử dụng thông tin về Accesbility mà server đã trả)
• Danh sách ứng dụng không an toàn
• Trả câu thông báo
 | 

 | 

 | App Client | 
1/ Nhận kết quả từ Server:

• Lỗi chung của hệ thống hoặc timeout: Hiển thị thông báo như hiện tại. Tắt thông báo và thoát app.
• Có kết quả:
• eTag_Accessbility không đổi (isChange = False):
• Hiển thị câu thông báo đã lưu cache trước đó tương ứng với các trường hợp của Status Accessbility = 1 hoặc 3.
• eTag_Accessbility thay đổi: Gửi yêu cầu sang SDK Accessbility xử lý. Thông tin truyền sang:
• Status Accessbility
• eTag Accessbility
• Thời gian (x) phút
• Danh sách ứng dụng không an toàn server trả về
 | 

 | 

 | SDK Accessbility | 
Xử lý:

1/ Lưu cache:

• Danh sách ứng dụng bật quyền ON Accessbility trên thiết bị
• Status Accessbilty
• eTag Accessbility
• Thời gian (x) phút cần gọi check Accessbility
• Danh sách ứng dụng không an toàn do Server trả về sau khi check Accessbility
2/ Trả về cho App Client:

• 
• Status Accessbility
• Owner App Name
 | 

 | 

 | App Client | 
1/ Nhận kết quả từ SDK Accessbility

• Trạng thái Status Accessbility = 1 (không an toàn): Hiển thị cảnh báo theo nội dung sauDanh sách lỗi

 | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Trạng thái Status Accessbility = 1 | Ứng dụng <Danh sách tên ứng dụng cấp quyền Acessbility không nằm trong Whitelist> đang cài đặt trên thiết bị của Quý khách có thể không an toàn vì đang được cấp quyền điều khiển Trợ năng/ Accessibility. Vui lòng gỡ bỏ hoặc tắt quyền Trợ năng/ Accessibility của Tất cả các ứng dụng này để tránh nguy cơ rủi ro và tiếp tục sử dụng ứng dụng Co-opBank Mobile Banking. Xem hướng dẫn tắt quyền Trợ năng/ Accessibility tại đây <Link html> | 
• Bỏ qua: Tắt thông báo và thoát ứng dụng
• Cài đặt trợ năng: Điều hướng KH đến mục cài đặt trợ năng trên thiết bị, đồng thời thoát ứng dụng

• Trạng thái Status Accessbility= 2 (an toàn): Xử lý nghiệp vụ như hiện tại
• Trạng thái Status Accessbility = 3 (chưa xác định): Yêu cầu KH xác thực định danh => Chuyển bước 2
2/ Kiểm tra thiết bị có cài đặt vân tay chưa?

• Nếu thiết bị của KH không hỗ trợ vân tay: App Client ứng xử như trường hợp Accessbility = 1
• Nếu KH đã cài vân tay trên thiết bị: Hiển thị popup xác thực vân tay với nội dung sauDanh sách lỗi

 | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | KH đã cài vân tay trên thiết bị | Thiết bị của Quý khách có thể không an toàn. Vui lòng thực hiện cài đặt và xác thực Vân tay trên thiết bị hoặc gỡ bỏ, tắt quyền Trợ năng/ Accessbility của Tất cả các ứng dụng sau để tránh nguy cơ rủi ro và tiếp tục sử dụng ứng dụng Co-opBank Mobile Banking. Danh sách ứng dụng đang bật quyền Trợ năng/ Accessbility <Danh sách tên ứng dụng cấp quyền Acessbility không nằm trong Whitelist, Blacklist>. Xem hướng dẫn tắt quyền Trợ năng/ Accessibility tại đây <Link html> | 
• Đồng ý: Thực hiện quét vân tay => Sau khi nhận kết quả xác thực vân tay thành công của thiết bị thì chuyển luồng nghiệp vụ hiện tại, cho phép KH sử dụng ứng dụng theo nghiệp vụ hiện tại.
• Cài đặt trợ năng: Điều hướng KH đến mục cài đặt trợ năng trên thiết bị.

• Nếu KH chưa cài vân tay trên thiết bị: Hiển thị popup cài đặt vân tay với nội dung sauDanh sách lỗi

 | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | KH chưa cài vân tay trên thiết bị | Thiết bị của Quý khách có thể không an toàn. Vui lòng thực hiện cài đặt và xác thực Vân tay trên thiết bị hoặc gỡ bỏ, tắt quyền Trợ năng/ Accessbility của Tất cả các ứng dụng sau để tránh nguy cơ rủi ro và tiếp tục sử dụng ứng dụng Co-opBank Mobile Banking. Danh sách ứng dụng đang bật quyền Trợ năng/ Accessbility <Danh sách tên ứng dụng cấp quyền Acessbility không nằm trong Whitelist, Blacklist>. Xem hướng dẫn tắt quyền Trợ năng/ Accessibility tại đây <Link html> | 
• Cài đặt vân tay: Điều hướng KH đến mục cài đặt vân tay trên thiết bị
• Cài đặt trợ năng: Điều hướng KH đến mục cài đặt trợ năng trên thiết bị.

### 6/ Nghiệp vụ bàn phím ảo trên Android

• Bàn phím ảo được xây dựng thành 1 lib để tích hợp trên các ứng dụng Client. Giao tiếp: App Client → Lib Keyboard
• Bàn phím ảo được sử dụng trên ứng dụng Client với mục đích dữ liệu KH nhập trên bàn phím sẽ không bị lấy cắp bởi kẻ lợi dụng.
• Có 3 loại chế độ bàn phím ảo: 
• Bàn phím chỉ số
• Bàn phím chỉ có chữ
• Bàn phím số + ký tự đặc biệt
• Bàn phím ảo đảm bảo có đầy đủ ký tự như bàn phím thông thường của thiết bị, không có con mắt (eye), có suggest số tiền, có logo của ứng dụng, có microphone
• Loại bàn phím ảo được hiển thị trong các trường hợp sau (thay thế đúng loại bàn phím ở thiết bị trước đó):
• Khi KH focus vào các field liên quan tới user: User khi đăng nhập, User khi xác thực
• Khi KH focus vào c

> ⚠️ *Nội dung đã cắt ngắn (18527 ký tự gốc). Xem đầy đủ trên Confluence.*


---


## 8. THU THẬP STH

> **Page ID:** `588546127` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/588546127

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*3 trang con:*

### 8.1. Thu thập STH kênh Quầy

> **Page ID:** `588546132` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/588546132

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*1 trang con:*

#### 8.1.1. (Bank) SOW Thu thập STH tại Quầy

> **Page ID:** `589299846` · **Version:** 8
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/589299846

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Thời gian cập nhật
 | 
 
 | A | HongLT | 
 | 
Tạo mới
 | V0.0.1 | 

### 1/ Tóm tắt Usecase
 | Use Case Name | Thu thập STH tại Quầy (Tích hợp vào web BO của hệ thống Mobile Banking)
 | Use Case ID | --
 | Use Case Description | 
• Cho phép thu thập dữ liệu STH cho KH tại Quầy để thực hiện giao dịch đáp ứng các yêu cầu của Thông tư 17, và QĐ 2345 của NHNN
• Các loại giấy tờ được phép thu thập gồm:
- CCCD21 gắn chip

- CCCD24 gắn chip

- Hộ chiếu

 | Actor | 
KH, BackOffice, eKYC SDK, eKYC Server, Image Server, Bank C06, Core AI, Agent C06

 | Priority | Medium
 | Trigger | 
KH chưa thu thập STH hoặc đã thu thập STH nhưng GTTT bị hết hạn hoặc KH có nhu cầu thu thập lại STH

 | 
Pre-Condition
 | 
GDV có quyền truy cập vào chức năng Thu thập STH tại BE, và có thiết bị hỗ trợ thu thập STH tại Quầy

 | Post-Condition | 
KH được thu thập STH thành công

• Với CCCD Chip: Thu thập STH thành công + C06 thành công
• Với Hộ chiếu: Thu thập STH thành công + Không có C06
 | Bussiness Rules | 
1/ Chỉ thu thập STH tại quầy với KH đã đăng ký dịch vụ MB của Co-op Bank và:

• Nếu KH là người có quốc tịch VN: Chỉ thu thập với căn cước gắn chip (CCCD21 & CCCD24) → Có xác thực C06
• Nếu KH là người có quốc tịch nước ngoài: Chỉ thu thập với hộ chiếu → Không xác thực C06
2/ Nếu KH đã thu thập STH, KH có thể được thu thập lại với cùng loại GTTT hoặc khác loại GTTT

3/ Với giấy tờ là Hộ chiếu, sau khi eKYC server trả kết quả đọc giấy tờ cho BO, cho phép GDV cập nhật lại toàn bộ thông tin trên BO 

4/ Khi so khớp dữ liệu nhận được từ eKYC server và MB, thực hiện so khớp: Số GTTT+ Họ tên (không dấu) + Ngày sinh + giới tính → Trùng khớp toàn bộ thông tin mới chuyển sang bước Liveness

5/ Không có luồng off Gtel với CCCD gắn chip

6/ Bắt buộc chụp ảnh 2 mặt GTTT

### Link Mockup tham khảo:

https://vqfnsc.axshare.com

### 2/ Luồng quy trình

trueThu thập tại quầyfalseautotoptrue16123

### 3/ Phạm vi chức năng
 | 
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản
 | 1 | Thu thập STH tại Quầy | 
Thu thập bằng CCCD Chip
 | 
RedThêm mới
 | BO | 

• KH ra Quầy để thu thập STH
• GDV truy cập chức năng thu thập STH, tìm kiếm thông tin KH = GTTT
• Hệ thống hiển thị thông tin STH của KH: Nếu có cho phép thu thập lại, Nếu chưa cho phép Thu thập
• Chọn loại giấy tờ. Đối với loại giấy tờ = Hộ chiếu, chỉ cho phép KH nước ngoài được phép thu thập
• Thực hiện chụp ảnh giấy tờ/ liveness KH
• Hệ thống hiển thị kết quả đọc giấy tờ và xác thực C06 (Với thu thập loại giấy tờ = Hộ chiếu, trạng thái xác thực C06 = Chưa xác thực)
 | 2 | 
Thu thập bằng Hộ chiếu (Chỉ áp dụng cho KH nước ngoài)
 | 
RedThêm mới
 | BO
 | 3 | Quản lý dữ liệu thu thập | 
Báo cáo thu thập STH
 | 
BlueCẬP NHẬT
 | BO | 
Bổ sung cột Loại giấy tờ, Quốc tịch, Kênh thu thập

 | 4 | 
Quản lý eKYC
 | 
BlueCẬP NHẬT
 | BO | 
Bổ sung cột Loại giấy tờ, Quốc tịch, Kênh thu thập

 | 5 | Logic check Facepay | 
FacePay khi giao dịch

 | 
BlueCẬP NHẬT
 | eKYC server | 
Bổ sung logic check khuôn mặt khi giao dịch Facepay đối với loại giấy tờ = Hộ chiếu

### 2/ Đánh giá ảnh hưởng
 | 
 | Chức năng | Nội dung | Tác nhân | Đánh giá
 | 1 | Cài đặt thu thập STH | 
Test ảnh hưởng đối với KH đã thu thập tại Quầy,

Riêng với thu thập = Hộ chiếu, hiển thị như sau

• Họ tên: Họ tên từ Hộ chiếu
• Số giấy tờ: Số hộ chiếu
• Trạng thái BCA = Chưa xác thực (Đã chốt với Bank) | App Client | Không ảnh hưởng, nhưng vẫn nên test lại
 | 2 | FacePay | 
Test ảnh hưởng đối với KH thu thập tại quầy = CCCD Chip và Hộ chiếu:

• Kiểm tra trạng thái STH trước khi FacePay | App Client | 
Không ảnh hưởng do với Hộ chiếu chưa xác thực C06, eKYC server vẫn lưu CHECKBIOMETRIC= 0, nhưng vẫn nên test lại

 | 3 | Kiểm tra FacePay với các KH đã thu thập tại Quầy | eKYC server | 
 eKYC server sửa lại logic so sánh khuôn mặt với loại giấy tờ = Hộ chiếu

 | 4 | Thu thập tại Login | 
Test ảnh hưởng đối với KH thu thập tại quầy = CCCD Chip và Hộ chiếu:

• Kiểm tra trạng thái STH trước khi FacePay | App Client | 
Không ảnh hưởng, nhưng vẫn nên test lại đại diện 1 Login type

 | 5 | Kiểm tra FacePay với các KH đã thu thập tại Quầy | eKYC server

---

### 8.2. Thu thập STH kênh App- NFC

> **Page ID:** `442305073` · **Version:** 6
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/442305073

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*7 trang con:*

#### 8.2.1. eKYC Onboarding (Update C06)

> **Page ID:** `439779493` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/439779493

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 

 | A | 
 
 | 
 | 
Tạo mới
 | V1.0.0
Mục lục
none

### 1/Tác nhân, điều kiện, kết quả mong muốn

#### 1.1/ Tác nhân: KH, App Client, App Server, Hệ thống eKYC, Hệ thống Bank, C06

#### 1.2/ Điều kiện trước: 

#### 1.3/ Kết quả mong muốn:

### 2/ Basic Flow

---

#### 8.2.2. Flow action Screen_Luồng Thu thập STH qua eKYC CCCD CHIP check C06

> **Page ID:** `525435024` · **Version:** 7
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/525435024

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThuDM2 | 
 | 
Tạo mới
 | V.1.0
 | 
 
 | M | ThuDM2 | V.1.0 | 
Cập nhật:

• Màn hình: kết quả Liveness bỏ hiển thị text "Đang xác thực BCA tại MH loading C06"
• Màn hình: ở MH Kết quả thu thập STH, Click nút Back quay về MH1.2 | V.1.1
 | 
 
 | M | ThuDM2 | V.1.2 | 
Cập nhật thao tác:

• Lỗi giấy tờ: Back của thiết bị + Back của App + Submit (Chụp lại): đều về màn chụp CCCD mặt trước
• Lỗi Liveness: Back của thiết bị + Back của App + Submit (Chụp lại): đều về màn chụp mặt 1  | V.1.3
 | 
 
 | M | ThuDM2 | V.1.3 | 
Cập nhật MH và logic xử lý NFC
 | V.1.4
 | 
 
 | M | HongLT | 
 | 
• Do giải pháp Off mã lỗi OCR để đọc CCCD24 không đọc được trường Nơi cấp, nên eKYC server sẽ cập nhật fix Nơi cấp theo Ngày cấp và trả cho Client
• Sửa text ghi chú màn hình hướng dẫn quét QR | 

 | 
 
 | 
 | 
 | 
 | 
Đổi tên trường Đã xác thực BCA = Trạng thái

Bổ sung hiển thị trường Loại giấy tờ
 | 

Mục lục
none

### 1/ Luồng màn hình

#### 1.1/ Danh sách màn hình

##### Nhóm Màn hình truy cập - 1

##### MH1.1: Truy cập tính năng

##### MH1.2 Màn hình thu thập STH - Đổi tên trường Đã xác thực BCA = Trạng thái

##### MH1.3: Màn hình thông báo thêm mới STH

##### MH1.4: Màn hình đồng ý lưu dữ liệu STH

##### Nhóm màn hình chụp giấy tờ - 2

##### MH2.1: Màn hình chọn giấy tờ

##### MH2.2: Màn hình thực hiện chụp mặt trước CCCD (tự động)

##### MH2.3: Màn hình thực hiện chụp mặt trước CCCD (thủ công)

##### MH2.4: Màn hình hiển thị ảnh chụp mặt trước

MH2.5: Hướng dẫn quét QR (Nếu không đọc đc QR từ mặt trước)

MH2.6: Kết quả đọc QR

##### Nhóm MH NFC - 3

##### MH3.01: Màn hình hướng dẫn NFC

##### MH3.02: Popup video hướng dẫn NFC

##### MH3.03: Màn hình thực hiện NFC 1 (Chờ thiết bị phản hồi khởi tạo phiên NFC)

##### MH3.1: Màn hình hướng dẫn NFC

##### MH3.2: Màn hình thực hiện NFC 2+3

  

##### MH3.2.1: Màn hình khởi tạo phiên NFC không thành công (Chưa tạo được section NFC mới)

##### MH3.2.2: Màn hình quá trình đọc KH di chuyển giấy tờ ra ngoài vùng đọc

##### MH3.3: Màn hình NFC không thành công

##### MH3.4: Màn hình NFC thành công

##### Nhóm màn hình nhập NFC (Chỉ hiển thị nếu không đọc được QR)

##### MH4.3: Màn hình nhập thông tin NFC khi QR lỗi (tuổi KH từ 58->59 tuổi)

##### MH4.4: Màn hình nhập thông tin NFC khi QR lỗi (KH < 25 tuổi, hoặc từ 26->39 tuổi)

##### MH4.5: Màn hình nhập thông tin NFC khi QR lỗi (KH>=60 tuổi)

##### MH4.6: KQ giấy tờ CCCD Chip

 

##### Nhóm màn hình chụp khuôn mặt (Liveness) - 5

##### MH5.1: Màn hình Liveness 1

##### MH5.2: Màn hình Liveness 2

##### MH5.3: Màn hình Liveness thành công

##### MH5.4. Loading khi đang check C06

##### MH5.5 Màn hình kết quả thu thập STH - xác thực C06 thành công

##### MH5.6. Màn hình kết quả thu thập STH - xác thực C06 không thành công

##### MH5.7. Các MH kết quả Liveness bị lỗi

#### 1.2/ Mô tả màn hình

##### MH1.1: Truy cập tính năng

Tham chiếu 

##### MH1.2 Màn hình thu thập STH

Chỉ hiển thị với KH đã thực hiện luồng eKYC Onboarding mới (có xác thực C06)
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Back | Icon | Click | 
--
 | 
--
 | Click back về MH Cài đặt
 | 2 | 
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
Thu thập sinh trắc học

 | 2 | Nội dung | 
Lable 
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị các thông tin:

• Họ và tên: 
• Số giấy tờ tùy thân: 
• Xác thực Bộ Công An → Đổi tên trường thành "Trạng thái" →Hiển thị 1 trong 3 giá trị theo loại giấy tờ <xem logic xử lý>
• CCCD Chip: Đã xác thực BCA
• Hộ chiếu: Đã xác thực
• CCCD Chip chưa xác nhận C06 thành công: Chưa xác thực  BCA
 | 3 | Loại giấy tờ | 
Lable 
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị loại giấy tờ theo dữ liệu eKYC server trả gì trong hàm Check trạng thái STH

• "type" : "CCCD21","CCC24": Hiển thị loại giấy tờ  = CCCD gắn chip
• "type" : "P": Hiển thị loại giấy tờ = Hộ chiếu
• "type": "VNEID": Hiển thị loại giấy tờ = CCCD gắn chip (trường Type=VNEID do eKYC server trả về dựa vào collectSuorce = "VNEID", DB không lưu type với luồng VNEID)
 | 3 | Thu thập lại | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định Enable

Chuyển sang MH2,1

(Ko đi qua MH1.4 nữa vì đã thực hiện luồng Onboard mới thì chắc chắn đã đồng ý chia sẻ thông tin)

##### MH1.3: Màn hình thông báo thêm mới STH

Hiển thị với tất cả các KH chưa thực hiện luồng eKYC Onboarding mới (có xác thực C06) (Kể cả đã từng thực hiện thu thập STH trước đó với CCCD gắn chip/CCCD thường/ CMTND/ Hộ chiếu, liveness)
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Thông báo

 | 2 | Nội dung | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị:

Quý khách vui lòng thực hiện quy trình thu thập sinh trắc học.

* Thông tin sinh trắc học được sử dụng trong xác thực giao dịch để nâng cao tính an toàn, bảo mật thông tin

 | 3 | Checkbox | 
Checkbox
 | 
Click
 | 
--
 | 
--
 | 
Mặc định có check

Hiển thị kèm nội dung: Tôi đã đọc, hiểu và đồng ý với các Điều kiện, điều khoản giao dịch chung về tài khoản, thẻ, dịch vụ ngân hàng điện tử

 | 4 | Hủy | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Quay về MH1.1

 | 5 | Đồng ý | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Mặc định Enable theo checkbox, nếu ND bỏ check thì Disable

Hiển thị MH1.4

##### MH1.4: Màn hình đồng ý lưu dữ liệu STH

Chỉ hiển thị ở lần thực hiện thu thập đầu tiên (Nếu đã thực hiện luồng eKYC Onboarding mới thành công thì sẽ ko hiện MH này)
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
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
Thông báo

 | 
2
 | 
Nội dung thông báo
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Fix trên client:

"Quý khách đang sử dụng dịch vụ định danh điện tử (eKYC) do VNPAY cung cấp. Trong quá trình sử dụng dịch vụ, chúng tôi (VNPAY) sẽ lưu trữ phục vụ các nghiệp vụ định danh xác thực. Các thông tin chia sẻ gồm:
- Số giấy tờ
- Họ và tên
- Ngày sinh
- Giới tính
- Quê quán
- Địa chỉ thường trú
- Ngày cấp
- Nơi cấp
- Ảnh chân dung và ảnh giấy tờ tùy thân
Quý khách vui lòng đọc kỹ quyền, nghĩa vụ của chủ thể dữ liệu và các nội dung khác liên quan tại "Chính sách bảo vệ dữ liệu cá nhân" được Co-opBank ban hành và có hiệu lực từ ngày 01/07/2023

 | 
3
 | 
Nút "Đóng"
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Đóng thông báo và thoát ứng dụng

 | 
4
 | 
Nút "Đồng ý & Tiếp tục"
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Hiển thị MH2.1

##### MH2.1: Màn hình chọn giấy tờ
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
 | Tên màn hình | 
 | 
 | 
 | 
 | Xác thực giấy tờ
 | 1 | Câu ghi chú | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Quý khách vui lòng sử dung CCCD gắn chip

 | 2 | Loại giấy tờ | Radio button | Click | Yes | 6 | 
• Mặc định Căn cước công dân
 | 3 | Text hướng dẫn | Label | ReadOnly | -- | -- | 
• Vui lòng sử dụng giấy tờ gốc (bản chính), còn hạn sử dụng
• Chụp ảnh trong môi trường sáng đảm bảo rõ nét, không bị mờ lóa, không bị mất góc
• Khách hàng không sử dụng Giấy tờ tùy thân giả mạo, không chính chủ. Khách hàng hoàn toàn chịu trách nhiệm trước pháp luật về thông tin Giấy tờ tùy thân cung cấp cho ngân hàng
Kèm 3 hình ảnh chụp GTTT không hợp lệ: ảnh chụp quá mờ, ảnh chụp mất góc, ảnh chụp lóa sáng

 | 4 | Back | Icon | Click | 
--
 | 
--
 | Click back về MH Cài đặt
 | 5 | Tiếp tục | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Click Tiếp tục mở ra MH chụp ảnh mặt trước GTTT

##### MH2.2: Màn hình thực hiện chụp mặt trước CCCD (tự động); MH2.3: Màn hình thực hiện chụp mặt trước CCCD (thủ công); MH2.4: Màn hình hiển thị ảnh chụp mặt trước

(Đối với Mặt sau tương tự, chỉ thay tiêu đề vùng chụp từ "Mặt trước" thành "mặt sau")
 | 

 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Nút “Quay lại”
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước đó

 | 
2
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
Fix Client 

Xác thực giấy tờ tùy thân

 | 
3
 | 
Mô tả
 | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Fix tại Client

MH2.2: Vui lòng điều chỉnh thiết bị để thấy rõ giấy tờ tùy thân. Hệ thống sẽ tự động chụp khi giấy tờ nằm trong khung hình.

MH2.3: Vui lòng điều chỉnh thiết bị để thấy rõ giấy tờ tùy thân. Khi giấy tờ nằm trong khung hình, nhấn nút "Chụp ảnh".

MH2.4: Vui lòng kiểm tra lại hình ảnh đã chụp và nhấn nút "Xác nhận".

 | 
4
 | 
Tiêu đề vùng chụp
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Mặt trước

 | 
5
 | 
Vùng chụp ảnh
 | 
capture
 | 
View
 | 
--
 | 
--
 | 
Vùng chụp ảnh CCCD

 | 
6
 | 
Nội dung hướng dẫn
 | 
Label
 | 
Text
 | 
--
 | 
--
 | 
Hiển thị trên khung chụp ảnh giấy tờ; Nội dung thông báo tương ứng với các trường hợp lỗi mà client nhận diện được

-       Không phát hiện mặt trước

-       Không phát hiện được mặt sau giấy tờ

-       Giấy tờ đặt quá gần

-       Giấy tờ đặt quá xa

-       …

 | 
8
 | 
Chụp tự động
 | 
Switch button
 | 
Click
 | 
--
 | 
--
 | 
<Tham khảo luồng xử lý chi tiết>

Chỉ hiển thị đối với Ios

Mặc định là “Chụp tự động”

 | 
9
 | 
Nút “Chụp”
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
<Tham khảo luồng xử lý chi tiết>

-       Mặc định hiển thị với Android

-       Đối với IOS:

o   Ẩn nếu “Chụp tự động”

o   Hiển thị nếu “Tắt chụp tự động”

 | 
5
 | 
Nút “Chụp lại”
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình chụp ảnh trước đó

 | 
6
 | 
Nút "Xác nhận"
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
<Tham khảo luồng xử lý chi tiết>

##### MH2.5: Màn hình hướng dẫn và thực hiện Scan QR
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Nút back
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước đó

 | 
2
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
Scan mã QR

 | 
3
 | 
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
Di chuyển camera để thấy rõ nét mã QR tại mặt trước của giấy tờ tùy thân. Hệ thống sẽ tự động quét mã QR

 | 
3
 | 
Vùng scan mã QR
 | 
Capture
 | 
View
 | 
--
 | 
--
 | 
Tự động scan mã QR

<Tham khảo luồng xử lý> 

 | 
4
 | 
Hướng dẫn quét QR
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị thông tin hướng dẫn bằng hình ảnh và hướng dẫn bằng chữ

• Đưa camera vào vùng mã QR ở góc phải mặt trước CCCD
• Hướng camera vào vùng mã QR trên thẻ căn cước
 | 5 | Nút "Bỏ qua" | Button | Click | -- | -- | 
Mặc định disable, hiển thị khi hết time cấu hình trên BE

Nhấn bỏ qua, chuyển sang màn hình "Chụp mặt sau"

 | 6 | Scan QR thành công | -- | -- | -- | -- | Chuyển sang MH NFC

##### MH 2.6: Màn hình Scan QR thất bại
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Icon
 | 
Icon
 | 
Read Only
 | 
--
 | 
--
 | 
--

 | 
2
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
Định dạng mã QR không hợp lệ, quý khách vui lòng thực hiện quét mã QR trên mặt trước của giấy tờ tùy thân

 | 
3
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
Tham khảo logic xử lý

##### MH3.01 + 3.03: Hướng dẫn NFC + Thực hiện NFC 1
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
Đọc thẻ Căn cước bằng công nghệ không chạm (NFC)

 | 
2
 | 
Hướng dẫn thực hiện
 | 
Picture
 | 
Read Only
 | 
--
 | 
--
 | 
Fix client

 | 
3
 | 
Hướng dẫn 
 | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Fix client:

- Đưa mặt lưng của điện thoại (vị trí như trong hình hướng dẫn) vào con chip ở mặt sau của giấy tờ tùy thân
- Giữ nguyên điện thoại và căn cước khi có thông báo rung và chạy quá trình đọc thông tin
- Quý khách vui lòng xem kỹ hướng dẫn trước khi thực hiện

 | 
 4
 | Xem video hướng dẫn | Link | Click | -- | --- | 
textVIE: Xem video hướng dẫn

Link url: fix cứng tại client

VNPAY cung cấp link video hướng dẫn tương ứng từng bank 

Xử lý khi click → Chuyển sang popup video hướng dẫn NFC

 | 5 | Đã hiểu | Button | Click | -- | -- | 
Onclick chuyển sang Màn hình thực hiện NFC 1 (Chờ thiết bị phản hồi khởi tạo phiên NFC)

Tham khảo logic xử lý

 | 6 | Đang xử lý  | Button | Click | -- | -- | 
Mặc định disable

Tham khảo logic xử lý 

##### MH3.1: Màn hình hướng dẫn NFC
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
Đọc thẻ Căn cước bằng công nghệ không chạm (NFC)

 | 
2
 | 
Hướng dẫn thực hiện
 | 
Picture
 | 
Read Only
 | 
--
 | 
--
 | 
Text hướng dẫn chạm thẻ

• Ảnh động hướng dẫn
• Quý khách vui lòng đọc kỹ hướng dẫn
• Đưa 2 vị trí khoanh vùng đỏ lại gần nhau (xem hình hướng dẫn: đưa phần đầu điện thoại lại gần vị trí chính giữa thẻ căn cước có biểu tượng chip xanh).
• Giữ nguyên thẻ & điện thoại khi màn hình thông báo đang đọc thông tin.
 | 
3
 | 
Hướng dẫn 
 | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Xin nhấn "Tôi đã hiểu và bắt đầu đọc thông tin" và đưa căn cước gần mặt sau điện thoại

 | 3 | Đọc thông tin ngay | Button | Click | -- | -- | Chuyển sang MH 3.2

##### MH3.2.1: Màn hình khởi tạo phiên NFC không thành công (Chưa tạo được section NFC mới)
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
Fix Client 

Đọc dữ liệu từ thẻ Chíp

 | 
2
 | 
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
Đưa điện thoại của quý khách tới gần vùng gắn Chíp trên CCCD

 | 
3
 | 
Icon
 | 
Icon
 | 
Read Only
 | 
--
 | 
--
 | 
--

 | 
4
 | 
Tiến trình
 | 
Timeline
 | 
Read Only
 | 
--
 | 
--
 | 
Ẩn nếu thiết bị chưa khởi tạo được phiên đọc NFC

Hiển thị nếu thiết bị có kết nối và khởi tạo được phiên đọc NFC

 | 
5
 | 
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
• Ẩn khi chưa nhận quét thẻ Chíp
• Hiển thị " Đang đọc, vui lòng không di chuyển thiết bị" trong quá trình quét thẻ Chip (MH.6.2)
• Hiển thị "Kết nối tới CCCD gián đoạn, quý khách vui lòng thực hiện lại" khi lỗi kết nối tới Chip trong quá trình đọc hoặc Timeout (MH.6.4)
• Hiển thị popup "Thiết bị không phản hồi. Quý khách vui lòng thực hiện sau giây lát." khi khởi tạo phiên NFC không thành công (MH.6.5)

##### MH3.2.2 : Màn hình quá trình đọc KH di chuyển giấy tờ ra ngoài vùng đọc
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

 | 1 | 
Icon lỗi
 | 
Icon
 | 
Read Only
 | 
--
 | 
--
 | 
Icon lỗi tương ứng

 | 2 | 
Thông báo
 | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Kết nối tới CCCD bị gián đoạn, Quý khách vui lòng thực hiện lại!

 | 3 | 
Video
 | 
Video
 | 
Click
 | 
--
 | 
--
 | 
Cho phép click để xem video

Video Server trả 

 | 4 | 
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
Tham khảo logic xử lý

##### MH3.3: Màn hình NFC không thành công,  MH3.4: Màn hình NFC thành công
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
Icon
 | 
Icon
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị icon tương ứng với 2 trường hợp

 | 
2
 | 
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
Hiển thị nội dung tương ứng với 2 trường hợp:

• 

> ⚠️ *Nội dung đã cắt ngắn (21564 ký tự gốc). Xem đầy đủ trên Confluence.*


---

#### 8.2.3. User action flow_Luồng Thu thập STH qua eKYC CCCD CHIP check C06 (BANK-VNPAY)

> **Page ID:** `445317361` · **Version:** 18
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/445317361

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThuDM2 | 
 | 
Tạo mới
 | V.1.0
 | 
 
 | M | ThuDM2 | V.1.0 | 
Cập nhật:

• Logic: Bỏ check số giấy tờ thực hiện thu thập và số giấy tờ lưu tại MB server → Thay vào đó check Họ tên + ngày sinh + giới tính
• MH: ở MH Kết quả thu thập STH, Click nút Back quay về MH1.2 | V.1.1
 | 
 
 | M | ThuDM2 | V.1.1 | 
Cập nhật thao tác:

• Lỗi giấy tờ: Back của thiết bị + Back của App + Submit (Chụp lại): đều về màn chụp CCCD mặt trước
• Lỗi Liveness: Back của thiết bị + Back của App + Submit (Chụp lại): đều về màn chụp mặt 1 
Bổ sung các trường hợp Kiểm tra quét NFC thất bại:

• Khi đọc NFC mà bị TO do lỗi SDK/ do KH bỏ tay ra không tap tiếp
• Thông tin lúc đọc NFC ra không trùng khớp với thông tin key trước đó (3 thông tin ID, ngày sinh, ngày hết hạn)
• Đọc NFC và check ra chip đó không hợp lệ
Điều chỉnh: 

• So khớp thông tin eKYC với thông tin ở MB: Họ tên check ko dấu, ko phân biệt hoa thường | V.1.2
 | 
 
 | M | ThuDM2 | V.1.3 | 
Cập nhật TH lỗi NFC và thông báo
 | V.1.4
 | 
 
 | M | ThuDM2 | V.1.4 | 
Cập nhật: Tại bước so khớp thông tin eKYC với thông tin ở MB: Check Họ tên ko dấu, ko phân biệt hoa thường (Bỏ dấu Tiếng việt và ký tự đặc biệt)
 | V.1.5
Mục lục
none

### 1/ Tóm tắt Use Case
 | Use Case Name | Thu thập và xác thực C06 dữ liệu STH
 | Use Case ID | --
 | Use Case Description | 
Là người dùng tôi muốn cập nhật/ thêm mới dữ liệu sinh trắc học phụ vụ các giao dịch ngân hàng yêu cầu FacePay

 | Actor | 
KH, Hệ thống MB, Hệ thống eKYC

 | Priority | Medium
 | Trigger | 
KH cập nhật và cài đặt dữ liệu sinh trắc học cho các giao dịch yêu cầu FacePay

 | 
Pre-Condition
 | 
• KH cài đặt và truy cập thành công tính năng tích hợp SDK
• KH có CCCD gắn chip, còn giá trị sử dụng
• Thiết bị sử dụng được cấp quyền truy cập camera

 | Post-Condition | 
Khách hàng cập nhật hoặc đăng ký dữ liệu sinh trắc học thành công và thông tin được xác thực C06

 | Basic Flow | 
• KH truy cập chức năng Cập nhật và xác thực STH
• Hệ thống hiển thị màn hình tương ứng trạng thái Đã xác thực/ Chưa xác thực
• KH thực hiện theo hướng dẫn của từng trạng thái 
• Hệ thống ghi nhận kết quả xác thực của khách hàng
• Bank lưu log lịch sử
 | Alternative Flow | 

 | Exception Flow | 
KH không đồng ý xác thực thông tin với C06

KH thoát khỏi trình xác thực

Dữ liệu CCCD và khuôn mặt không hợp lệ 

 | Bussiness Rules | 
Br-1: KH thực hiện xác thực fail quá n lần sẽ bị khóa trong khoảng thời gian được cấu hình ở SDK Server 

 | Non-Funtional Requiremnt | 
NFR1: Thời gian thực hiện chức năng xác thực không quá x giây

### 2/ Luồng nghiệp vụ

#### 2.1/ Flow thu thập Sinh trắc học C06 chủ động

trueKH thu thập STHfalseautotoptrue11717

#### 2.2/ Danh sách API
 | Bước thực hiện | Tên API | Luồng gọi API | Địa chỉ API | Input | Output | Ghi chú
 | 
Check thông tin chữ ký trên CHIP
 | 
verify
 | eKYC Server → GTEL | {{ApiBaseUrl}}/eid_verify/sdk/verify | 
 | 
 | Nhập ghi chú (nếu có)

### 3/ Luồng xử lý

* Tham số Bank có thể cấu hình: Check NFC (SKIP_NFC: 0, 1, 2, 3), Check C06 (CHECK_GTEL: ON, OFF) 

(1: ON, 0=OFF)

• Với luồng thu thập này yêu cầu bắt buộc cấu hình để đảm bảo có thể thu thập và check C06 thành công: CHECK_GTEL=ON, SKIP_NFC=2 (thiết bị không hỗ trợ NFC thì ko cho thực hiện luồng → thông báo cho ND)
• Nếu bank cấu hình CHECK_GTEL=ON mà cấu hình SKIP_NFC # 2 (=0,1,3) → vẫn thực hiện luồng gọi sang C06, nhưng ko đủ thông tin để check hợp lệ thì sẽ hiển thị thông báo "Chưa xác thực C06"
• Nếu bank cấu hình CHECK_GTEL=OFF thì chỉ thực hiện thu thập thông tin, không gọi sang C06
#### 3.1/ Truy cập chức năng
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả chi tiết

 | 
1
 | 
Từ MH Cài đặt, chọn tính năng "Thu thập sinh trắc học"
 | Hệ thống MB | 
1/ Check trạng thái thiết bị

• Nếu thiết bị không hỗ trợ NFC hoặc có NFC nhưng không hỗ trợ tap thẻ (NFC không active được) :
• Bank cấu hình SKIP_NFC=1,2,3 thì ko cho thực hiện luồng → thông báo lỗi cho ND: Thiết bị của quý khách không hỗ trợ NFC. Vui lòng sử dụng thiết bị khác hoặc liên hệ 1900xxxx để được hỗ trợ.
• Bank cấu hình SKIP_NFC =0 thì theo luồng: Mặt trc - QR - Mặt sau - Liveness
• Nếu thiết bị có hỗ trợ NFC: chuyển bước 2 check thiết bị đã bật NFC chưa, chỉ check với hệ điều hành android, với ios (>=13.0) bỏ qua bước này chuyển sang màn hình 1.3
2/ Kiểm tra thiết bị đã bật NFC chưa

• Không hợp lệ:  | | 
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (Nếu có)

 | 1 | Thiết bị android chưa bật NFC | 
Quý khách vui lòng bật NFC trong Cài đặt của thiết bị để thực hiện đọc thông tin giấy tờ tùy thân.
 | 
Hiển thị 2 buttons:

Cài đặt: Sẽ chuyển sang màn hình cài đặt Hệ điều hành thiết bị

Hủy: Tắt popup đồng thời giữ nguyên màn hình hiện tại

• Hợp lệ: Gửi yêu cầu check trạng thái STH đến Hệ thống eKYC theo: CIF
 | 

 | 

 | Hệ thống eKYC | 
Nhận và xử lý

Không hợp lệ: Trả mã lỗi tương ứng

Hợp lệ: 

• Đối với KH đã thực hiện luồng eKYC Onboarding mới có tích hợp check C06 → Hiển thị MH 1.2 
• Đã có dữ liệu STH check thành công C06 (CHECK_BIOMETRIC=0) 
• Đã có dữ liệu CCCD gắn chip, liveness nhưng chưa xác thực C06 (CHECK_BIOMETRIC=2)
• Đối với KH chưa thực hiện luồng eKYC Onboarding mới có tích hợp check C06 → Hiển thị MH 1.3
• Chưa có dữ liệu STH (CHECK_BIOMETRIC=1)
• Đã có dữ liệu CCCD gắn chip, liveness, chưa xác thực C06 (CHECK_BIOMETRIC=2)
 | TT | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
MH1.3 nhấn "Đồng ý"

 
 | 
Hệ thống MB
 | 
Kiểm tra trạng thái chia sẻ dữ liệu của KH

• Nếu trạng thái = null => Hiển thị MH1.4
• Nếu trạng thái = Đồng ý chia sẻ (Đã đồng ý ở luồng Onboarding) => Hiển thị MH 2.1
 | TT | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
MH1.4 nhấn "Đồng ý và tiếp tục"

 
 | 
Hệ thống MB
 | 
Cập nhật trạng thái chia sẻ dữ liệu của KH

Hiển thị MH2.1

#### 3.2/ Luồng chức năng chính

##### Chụp ảnh mặt trước CCCD gắn chip
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | 
Nhấn "Chụp"
 | 
Hệ thống eKYC
 | 
Thực hiện chụp mặt trước CCCD theo hướng dẫn

Chụp xong hiển thị MH2.4 ảnh chụp mặt trước

 | 
 | 
Nhấn “Xác nhận”
 | 
Hệ thống eKYC
 | 
Kiểm tra kết quả đọc mã QR trên mặt trước CCCD

• Không hợp lệ: Không đọc được thông tin hoặc thông tin không hợp lệ →  Chuyển sang màn hình quét mã QR
• Hợp lệ: 
       - Thông tin đọc QR gồm: Số GTTT, họ tên, ngày sinh, giới tính, nơi thường trú, ngày cấp, số CMND

       - Dựa vào kết quả QR, client thực hiện tính thời gian hết hạn GTTT:

          Tính theo quy định: Dựa vào ngày sinh khách hàng, khi đủ: 25 tuổi, đủ 40 tuổi và đủ 60 tuổi.

          VD: KH sinh ngày 26/01/1988 → Ngày hết hạn là 26/01/2028

                 Trên 60 tuổi, ngày hết hạn = Không thời hạn

       - Lưu thông tin KH, Chuyển sang MH3.1: Màn hình hướng dẫn NFC (Nếu tham số SKIP_NFC=2 - lý tưởng)

##### Quét mã QR (Nếu chụp ảnh lỗi)
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Quét mã QR trên mặt trước CCCD | Hệ thống eKYC | 
Hệ thống tự động quét mã QR cho đến khi nhận được thông tin hợp lệ theo đúng định dạng quy định

Không thành công: Hiển thị thông báo như mô tả MH

• 
• Sau thời gian cấu hình trên BE (Tham số ScanQR_Time). Hiển thị nút Bỏ qua. Nhấn "Bỏ qua" (Hoặc đóng Popup thông báo):
• Nếu có NFC: Hiển thị màn hình Nhập thông tin NFC
• Nếu không có NFC: Hiển thị màn hình chụp mặt Sau giấy tờ
• Thành công: Hiển thị thông báo "Scan QR thành công". Đồng thời: 
• Lưu thông tin khách hàng Số GTTT,  ngày hết hạn, ngày sinh
• Check tham số SKIP_NFC (Bật tắt luồng NFC)
• Nếu tham số SKIP_NFC = 0 - Tắt - Chuyển sang chụp mặt sau CCCD
• Nếu tham số SKIP_NFC = 1 - Cho phép bỏ qua sau khi tap n lần không được
• Nếu tham số SKIP_NFC = 2 - bắt buộc thực hiện luồng NFC, Client truyền 3 thông tin khách hàng gồm: Số GTTT,  ngày hết hạn, ngày sinh chuyển sang màn chạm thẻ chip 
• Nếu tham số SKIP_NFC = 3 - cho phép bỏ qua NFC nếu quét được QR, nếu k quét được QR thì bắt buộc quét quét NFC

##### Nhập thông tin NFC (Nếu QR lỗi)
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhập thông tin "Số thẻ CCCD" & "ngày sinh" | Hệ thống eKYC | 
Nhập thông tin 

 | 2 | Nhấn tiếp tục | 
 | 
Kiểm tra validate các trường nhập vào:

• Không hợp lệ: | | 
 | 
Trường hợp
 | 
Thông báo
 | 
Xử lý (Nếu có)

 | 1 | Không nhập thông tin số GTTT | Quý khách vui lòng nhập số căn cước công dân. | 

 | 2 | Nhập số GTTT ko đúng định dạng (12 số) | Số Căn cước công dân không đúng định dạng. Quý khách vui lòng kiểm tra lại. | 

 | 3 | Không nhập thông tin trường ngày sinh(IOS) | Quý khách vui lòng nhập ngày sinh. | 

 | 4 | Nhập sai định dạHệ thống eKYCng trường ngày sinh(IOS)
 | Trường ngày sinh nhập theo định dạng dd/mm/yyyy. Quý khách vui lòng kiểm tra lại. | 

• Hợp lệ: Client thực hiện tính ngày hết hạn CCCD dựa theo quy tắc phần mô tả chi tiết, Dựa vào 3 thông tin: Số GTTT, ngày sinh, ngày hết hạn hợp lệ là key để truyền sang đọc thông tin thẻ chip 

##### Thực hiện NFC

* Trong khi thực hiện NFC, nếu ND chọn nút Back của thiêt bị thì đưa về MH Chụp ảnh GTTT mặt trước
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Ở MH3.01, Nhấn "Đã hiểu" | 
Hệ thống eKYC
 | 
Bước 1: Thực hiện kiểm tra trạng thái sẵn sàng đọc NFC của thiết bị:

Đối với IOS:

• 
Thực hiện kiểm tra trạng thái sẵn sàng đọc NFC của thiết bị:

Đối với IOS:

• Hiển thị màn hình có nút "Đang xử lý" 

• Nút "Đang xử lý" disable cho đến khi khởi tạo thành công phiên đọc NFC; trong quá trình chờ khởi tạo; nếu quá 60s thiết bị không phản hồi hoặc phản hồi không mở phiên mới →  hiển thị Màn hình khởi tạo phiên NFC không thành công (Chưa tạo được section NFC mới)
• Trường hợp "ready" khởi tạo phiên đọc NFC trên thiết bị→ Hiển thị màn hình thực hiện NFC 2, thực hiện bước 2:
Đối với Android:

• Thực hiện ngay bước 2
Bước 2:

Hệ thống tự động quét thẻ chip cho đến khi nhận được thông tin hợp lệ

• Không hợp lệ:  | | 
 | 
Trường hợp
 | 
Thông báo
 | 
Xử lý (Nếu có)

 | 1 | Lỗi kết nối trong quá trình tap thẻ
(VD: tap chip nửa chừng bỏ ra) | "Kết nối tạm thời gián đoạn. Quý khách vui lòng đợi trong giây lát"- button Thử lại | Quay về MH chọn giấy tờ tùy thân
 | 2 | Lỗi đọc thông tin không thành công
(VD: mở lên nhưng không tap chip, đang tap thì bỏ tay ra không tab tiếp, khi đọc NFC bị TO do lỗi SDK, Tap thẻ atm/visa) | "Đọc thông tin không thành công. Quý khách vui lòng thử lại" - Button Thử lại | Quay về MH chọn giấy tờ tùy thân
 | 3 | Lỗi tap fail quá số lần | "Quý khách đã thực hiện quét NFC quá số lần quy định. Vui lòng thực hiện lại!" - Button Thử lại | Tính theo SKIP_NFC:
= 0,1,3 => đi tiếp mặt sau
= 2 => về MH chọn giấy tờ tùy thân
 | 4 | Lỗi lệch thông tin nhập và thông tin NFC
(VD: Tap chip CCCD khác CCCD đã chụp hoặc thông tin đọc được từ chip không match với thông tin key (đọc được từ QR/nhập tay)) | "Thông tin NFC không trùng khớp. Quý khách vui lòng thử lại"- Button Thử lại | Quay về MH chọn giấy tờ tùy thân
 | 5 | Lỗi chung (Andr) | "Thông tin quý khách không hợp lệ, xin vui lòng thử lại" - Button "Thử lại" | nếu chưa đạt ngưỡng maxtap --> tap lại
nếu đạt ngưỡng maxtap --> tương tự TH3

• Hợp lệ: Thông tin đọc NFC thành công, hiển thị MH Chụp mặt sau CCCD

##### Màn hình thực hiện NFC 2+ Màn hình thực hiện NFC 3
 | 
STT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Hủy bỏ | 
SDK Client
 | 
Quay về màn hình hướng dẫn NFC có nút đã hiểu

##### Quá trình đọc KH di chuyển giấy tờ ra ngoài vùng đọc + Màn hình khởi tạo phiên NFC không thành công (Chưa tạo được section NFC mới)
 | 
STT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 2 | Đóng | 
SDK Client
 | 
Quay về màn hình hướng dẫn NFC có nút đã hiểu

##### Chụp mặt sau CCCD
 | | 
STT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Click chọn “Chụp” | Hệ thống eKYC | 
Thực hiện chụp ảnh trong vùng hướng dẫn chụp ảnh (Vùng có đường viền xanh)

Sau khi chụp xong, chuyển màn hình hiển thị ảnh sau khi chụp

 | 2 | 
Nhấn “Xác nhận”
 | 
Hệ thống eKYC
 | 
Lưu ảnh đã được chụp tại client → Gửi yêu cầu sang Coree AI kiểm tra chất lượng ảnh GTTT trước khi hiển thị kết quả đọc giấy tờ

##### Kiểm tra tiền xử lý ảnh và đọc kết quả
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 
 | 
 | 
Hệ thống eKYC

 | 
1/ Kiểm tra tiền xử lý ảnh

• Nếu không hợp lệ (Giấy tờ không đúng, mất góc …) →  thông báo lỗi (Theo bảng mã lỗi https://docs.google.com/spreadsheets/d/1v_yFgKlDBT19LEy6-HIZ6oIjpHR7z9_xnbX3yQQCVKU/edit?pli=1#gid=0)
• Nếu hợp lệ →Trả kết quả đọc GTTT, độ tin cậy của từng thông tin trên GTTT và chuyển yêu cầu kiểm tra tỷ lệ cấu hình độ tin cậy cho phép
 | 
 | 
 | 
2/ Kiểm tra thông tin theo cấu hình

Không hợp lệ

• Độ tin cậy theo cấu hình Dưới ngưỡng tin cậy → Trả kết quả cho SDK eKYC thông báo lỗi, theo bảng mã lỗi (https://docs.google.com/spreadsheets/d/1v_yFgKlDBT19LEy6-HIZ6oIjpHR7z9_xnbX3yQQCVKU/edit?pli=1#gid=0)
• Giấy tờ hết hạn → Trả kết quả cho SDK eKYC thông báo lỗi, theo bảng mã lỗi (https://docs.google.com/spreadsheets/d/1v_yFgKlDBT19LEy6-HIZ6oIjpHR7z9_xnbX3yQQCVKU/edit?pli=1#gid=0)
• KH chưa đủ 18 tuổi
• KH đã eKYC sai liên tiếp quá số lần quy định trong ngày theo tham số "LIMIT_FAILED_EKYC"
Hợp lệ

• Lớn hơn hoặc bằng ngưỡng tin cậy → Trả kết quả Đạt
• Giấy tờ chưa hết hạn → Trả kết quả Đạt
• KH đủ 18 tuổi → Trả kết quả Đạt
• KH eKYC chưa quá số lần sai liên tiếp quy định trong ngày theo tham số "LIMIT_FAILED_EKYC" 
• Đồng thời trả ID của bản ghi eKYC (là SID) do hệ thống eKYC server sinh ra cho SDK eKYC
 | 
 | 
 | 
3/ Trả kết quả đọc giấy tờ, đồng thời trả ID của bản ghi eKYC cho Hệ thống MB

 | 
 | 
 | 
Hệ thống MB
 | 
Hiển thị MH4.6: KQ giấy tờ CCCD Chip

* Nếu lỗi giấy tờ: Back của thiết bị + Back của App + Submit (Chụp lại): đều về màn chụp CCCD mặt trước

##### Thực hiện Liveness
 | | STT | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Tại MH4.6: KQ giấy tờ CCCD Chip, bấm "Tiếp tục | 
Hệ thống MB
 | 
Kiểm tra thông tin dữ liệu nhận được từ eKYC và dữ liệu khách hàng

• Kiểm tra thông tin Họ tên, Ngày sinh, Giới tính phải trùng khớp với thông tin Khách hàng lưu trữ tại MB server (Mục đích để cho phép các KH đã đăng ký MB trước đó bằng CMND9 và Hộ chiếu vẫn được phép thu thập STH C06 để tiếp tục thực hiện giao dịch trên MB)
• Trường hợp corebank lưu giấy tờ = CMND9 nhưng nếu vẫn cho KH thu thập bằng CCCD Chip mới thì sẽ bị lệch thông tin giấy tờ giữa MB và Corebank → Đề xuất bank làm đồng bộ thông tin từ MB về Corebank (bank sẽ cấp API đồng bộ, sau 1/7)
• Lưu ý khi so khớp: 
• Check Họ tên ko dấu, ko phân biệt hoa thường (Bỏ dấu Tiếng việt và ký tự đặc biệt thường có ở tên người dân tộc, bao gồm các ký tự: Nháy thẳng ' , nháy chéo ’ , gạch ngang - , dấu huyền`, dấu ngã ~, dấu mũ trăng, dấu mũ nón)   
• Ví dụ:
• nếu có ký tự ' (H') → bỏ ký tự ' chỉ còn H, nếu có ký tự - (Y-) → bỏ - chỉ còn Y
• nếu có dấu mũ thì bỏ dấu: ŏ → o, ŭ → u, č → c, ĕ → e, ĭ → i, Ñ -> N
→ Thông tin không hợp lệ: Thông báo lỗi: "Thông tin khách hàng không hợp lệ. Vui lòng kiểm tra lại thông tin"

→ Thông tin hợp lệ: Hiển thị MH Xác thực khuôn mặt

 | 2 | Chụp ảnh khuôn mặt 

 | Hệ thống eKYC | 
Hệ thống eKYC thực hiện kiểm tra khuôn mặt của KH như:

• Không tìm

> ⚠️ *Nội dung đã cắt ngắn (17122 ký tự gốc). Xem đầy đủ trên Confluence.*


---

#### 8.2.4. Phạm vi đánh giá giải pháp OFF mã lỗi OCR để đáp ứng CCCD24

> **Page ID:** `521078141` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/521078141

### 1/ So sánh thông tin đọc được giữa CCCD21 và CCCD24

Các thông tin KH sẽ lấy từ QR và Chip như sau:

### 2/Đánh giá ảnh hưởng nếu OFF OCR
 | 
 | Luồng eKYC | Nội dung | Tác nhân | Mô tả
 | 1 | Onboarding+Thu thập | 
Nếu OFF OCR thì CCCD21 và CCCD24 sẽ không lấy được thông tin Nơi cấp 
 | Client | 
• Onboarding: Không hiển thị trường Nơi cấp tại MH "Xác thực giấy tờ" và màn hình "Thông tin đăng ký dịch vụ"
• Thu thập: Không hiển thị trường Nơi cấp tại Popup NĐ13 và MH "Xác thực giấy tờ"
→ Nếu Bank vẫn cần thông tin Nơi cấp thì có thể cho KH tự nhập tay, hoặc tự chọn nơi cấp từ Droplist gồm các giá trị fix sẵn như: Cục Cảnh sát, Bộ Công An, Cục QLTTXH ...

→ Bank chốt fix suy ra nơi cấp từ ngày cấp vì trên các biểu mẫu giấy tờ của Bank vẫn cần hiển thị Nơi cấp

 | 2 | 
 | 
 | BE | Cập nhận hiển thị ẩn cột tỷ lệ tương thích ở các Tab QR, NFC
 | 3 | 
 | Loại giấy tờ | 
 | 

 | 4 | 
 | 
 | App | 

 | 5 | 
 | Quản lý eKYC | BE | 

 | 6 | Onboarding+Thu thập | 
CCCD24 đọc thêm được trường:

• Số định danh cá nhân đã hủy(nếu có)
• Họ tên cha mẹ (đối với CCCD dưới 14 tuổi) | Bank | Bank đánh giá có cần lưu các thông tin này không? Nếu có sẽ lưu thêm vào DB eKYC
 | 7 | Thu thập | CCCD21 và CCCD24 sẽ thông lấy được thông tin Nơi cấp  | BE | 
• Báo cáo STH (Bank đang dùng để cập nhật thủ công thông tin KH vào core), trường Nơi cấp mới= Null
• Phiếu cập nhật thông tin KH, trường Nơi cấp = Null
 | 8 | Job đăng ký mở CIF | 
 | 
 | 

• Nếu ngày cấp < 01/07/2024 → Truyền loại giấy tờ = CCCD
• Nếu ngày cấp >= 01/07/2024 → Truyền loại giấy tờ = CC
 | 9 | 
 | 
 | 
 |

---

#### 8.2.5. Phạm vi cập nhật khi ON lại luồng OCR để đọc CCCD24

> **Page ID:** `571998989` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/571998989

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Thời gian cập nhật
 | 
 
 | A | HongLT | 
 | 
Tạo mới
 | V0.0.1 | 

 | 
 | Luồng eKYC | Nội dung | Tác nhân | Luồng cũ khi OFF OCR | Nếu ON OCR
 | 1 | Onboarding+Thu thập | 
Nếu OFF OCR thì CCCD21 và CCCD24 sẽ không lấy được thông tin Nơi cấp 
 | eKYC server | 
Bank chốt fix suy ra nơi cấp từ ngày cấp vì trên các biểu mẫu giấy tờ của Bank vẫn cần hiển thị Nơi cấp

eKYC server fix và trả ra cho Client hiển thị

- Nếu ngày cấp < 01/07/2024 trả giá trị =  CỤC CSQLHC VỀ TTXH

- Nếu ngày cấp >= 01/07/2024 trả giá trị = BỘ CÔNG AN
 | Nơi cấp: Vẫn fix theo ngày cấp giống luồng OFF OCR (do OCR đọc nơi cấp vẫn bị sai)
 | 2 | 
 | Tách riêng loại giấy tờ CCCD21 và CCC24 | Client | Màn hình kết quả đọc eKYC, hiển thị loại giấy tờ chung = CCCD gắn chip → Truyền chung cho MB server loại giấy tờ = CCCD21 | 
• eKYC server trả riêng 2 giá trị = CCCD21 và CCCD24
• Client hiển thị loại giấy tờ chung = CCCD gắn chip
• Riêng đối vớl luồng Onboarding: Client truyền cho MB server theo đúng giá trị loại giấy tờ eKYC server trả về vào bảng CUSTOMER_EKYC
 | 3 | 
 | 
 | BO | 
Chức năng Quản lý danh sách eKYC và Hậu kiểm eKYC:

• Ẩn cột tỷ lệ tương thích, tích xanh đỏ vàng ở các Tab QR, NFC | 
Chức năng Quản lý danh sách eKYC và Hậu kiểm eKYC:

• Hiển thị cột độ tương thích và tích xanh đỏ vàng ở tab QR, NFC
• Hiển thị Loại GTTT theo đúng loại giấy tờ eKYC server trả về:
- Type CCCD21: Hiển thị CCCD gắn chip

- Type CCCD24: Hiển thị Thẻ căn cước gắn chip

 | 4 | Onboarding → Job đăng ký mở CIF  | 
 | BO server | 
Fix truyền loại giấy tờ trong API:  createCifEkyc

• Nếu ngày cấp < 01/07/2024 → Truyền sang Bank loại giấy tờ = CCCD
• Nếu ngày cấp >= 01/07/2024 → Truyền loại giấy tờ = CC | 
• Bỏ fix truyền loại giấy tờ theo ngày cấp
• Truyền đúng theo loại giấy tờ (group type) đọc được từ eKYC server
 | 5 | 
 | 
 | 
 | 
 
 |

---

#### 8.2.6. Tích hợp Secure-Killer 3.0.0 trên Android cho dịch vụ eKYC/Thu thập STH/Facepay

> **Page ID:** `591692819` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/591692819

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 

 | A | 

 | -- | 
Tạo mới
 | v1 | 

Mục lục
none

### 1/ Tác nhân, điều kiện trước, kết quả mong muốn
greywhitewhite1greysolidTác nhân, điều kiện, kết quả mong muốn | 1. Mục đích: | Tích hợp Secure-Killer 3.0.0 trên Android cho dịch vụ eKYC/Thu thập STH/Facepay
 | 2. Phạm vi ảnh hưởng: | App Client, SDK eKYC, SDK Facepay, eKYC Server
 | 3. Phạm vi tính năng: | 
• Luồng kiểm tra thông tin NFC và hình ảnh 2 mặt thẻ CCCD (API check card)
• Luồng kiểm tra liveness (API check liveness)
• Luồng truy vấn cấu hình tham số (API get config)
 | 4. Điều kiện trước:
 | 
• Secure-Killer 3.0.0 đã được tích hợp thành công trên thiết bị đang sử dụng
• App Version, SDK eKYC và SDK Facepay đã được cập nhật lên phiên bản mới nhất
• App Version đã tích hợp SDK eKYC/SDK Facepay
 | 5. Kết quả mong muốn: | Client hiển thị thông báo lỗi kèm mã lỗi và nguồn lỗi theo cú pháp được cấu hình
 | 5. Configuration: | 
Bổ sung config sau trên BO eKYC:
 | Name | Value | Desc | Note
 | KILLER_APP_VER | 
 | Version nhỏ nhất trở lên của App Client cần phải check object chữ ký secure  | 

### 2/ Sơ đồ tuần tự

trueSecure-Killerfalseautotoptrue9431

### 3/ Luồng xử lý

• 
##### Lưu ý:

• Secure-Killer version 3.0.0 là version mới được tích hợp để thay thế hoàn toàn cho version 1.2 là version cũ dùng kiểm tra trạng thái thiết bị hợp lệ (Root/Hook) và có bổ sung thêm nghiệp vụ sinh chữ ký
• Đối với các phiên bản app version ≥ min app version được cấu hình tham số, Secure-Killer được tích hợp vào app chủ là version 3.0.0 và sinh chữ ký trả về eKYC Server kiểm tra chữ ký hợp lệ trước khi thực hiện các nghiệp vụ khác | STT | Thao tác | Tác nhân | Mô tả
 | 1 | KH thực hiện eKYC cho Onboarding/thu thập STH/Facepay | App Client | Mở SDK eKYC/SDK Facepay và thực hiện luồng xử lý như nghiệp vụ hiện tại
 | 2 | 
 | SKD eKYC/SDK Facepay | 
• Thực hiện luồng xử lý như nghiệp vụ hiện tại
• Bổ sung nghiệp vụ: Gửi yêu cầu kiểm tra trạng thái thiết bị sang ứng dụng Secure-Killer
 | 3 | 
 | Secure-Killer | 
• Kiểm tra trạng thái thiết bị hợp lệ và phản hồi:
• Hợp lệ: trả giá trị True
• Không hợp lệ: trả giá trị False
• Sinh object gồm kết quả kiểm tra trạng thái thiết bị hợp lệ và chữ ký xác thực, phản hồi kết quả về SDK eKYC/SDK Facepay
 | 4 | 
 | SDK eKYC/SDK Facepay | 
Nhận object phản hồi từ Secure-Killer và gửi yêu cầu kiểm tra sang eKYC Server tại trường secure

 | 5 | 
 | eKYC Server | 
5.1. Lấy giá trị config KILLER_APP_VER và so sánh với version hiện tại của App Client:

• KILLER_APP_VER ≤ appVersion: chuyển bước 5.2 tiếp tục thực hiện luồng xử lý
• KILLER_APP_VER > appVersion: bỏ qua thao tác check chữ ký secure, tiếp tục thực hiện luồng xử lý như nghiệp vụ hiện tại
5.2 Kiểm tra tính hợp lệ của chữ ký trong object tại trường secure và xử lý theo các trường hợp:

• Chữ ký hợp lệ: tiếp tục thực hiện kiểm tra tính hợp lệ của thiết bị:
• Thiết bị không hợp lệ:
• Phản hồi về SDK Client hiển thị thông báo "Thiết bị không hợp lệ. Quý khách vui lòng kiểm tra lại"
• Trả mã lỗi: VAL-ROOTHOOK-13
• Thiết bị hợp lệ: tiếp tục thực hiện luồng xử lý hiện tại
• Chữ ký không hợp lệ: phản hồi thông báo lỗi về SDK eKYC/SDK Facepay trả mã lỗi VAL-ROOTHOOK-13
 | 6 | 
 | SDK eKYC/SDK Facepay | 
Nhận phản hồi từ eKYC Server và hiển thị màn hình cho các trường hợp:

• Thiết bị hợp lệ: tiếp tục xử lý theo luồng nghiệp vụ hiện tại
• Thiết bị không hợp lệ: thông báo "Thiết bị không hợp lệ. Quý khách vui lòng kiểm tra lại"
• Chữ ký không hợp lệ: hiển thị thông báo lỗi

---

#### 8.2.7. Kiểm tra chip Clone/Tamper V2

> **Page ID:** `591692764` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/591692764

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | BA Leader reviewed
 | 
 | M | 

 | V1 | 
Tạo mới
 | V2 | 

Mục lục
none

## 1/ Tóm tắt Use Case
 | 
Mục đích
 | 
Thay đổi nghiệp vụ kiểm tra tính hợp lệ của dữ liệu NFC

 | 
Phạm vi cập nhật
 | 
• SDK eKYC: Bổ sung cơ chế xác thực chip bằng challengeCode do server truyền lên
• eKYC Server:
• Bổ sung cơ chế bóc tách thông tin NFC từ DG
• Bổ sung yêu cầu gen challengeCode sang VNPAY C06
• Check dataNotTamper, chipClone và chipAuthSucceeded
• Bổ sung input verify chip vào C06:
• Kết quả authen bằng challengeCode client truyền lên
• VNPAY C06:
• Bổ sung API gen challengeCode
• Bổ sung cơ chế check DS
• Bổ sung cơ chế check authen chip
• Bổ sung cơ chế check passive (DG Hash)
 | 
Tác nhân
 | 
MB Client, eKYC SDK

 | 
Điều kiện trước
 | 
eKYC SDK đã cập nhật lên phiên bản mới nhất

• iOS: 2.1
• AND: 1.4
eKYC server tích hợp API C06: API 4.5

 | 
Kết quả mong muốn
 | SDK check và trả thông tin về cho Server thông tin Clone/Tamper
 | 
Link bàn giao API
 | + API get ChallengeCode: 6. API 4.5 get ChallengeCode - eKYC - C06 - VNPAY Confluence (vnpaytest.vn)
+ API verify ChallengeCode: 7. API 4.5 verify ChallengeCode - eKYC - C06 - VNPAY Confluence (vnpaytest.vn)

## 2/ Logic xử lý
 | STT | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | KH bắt đầu thực hiện eKYC | eKYC SDK | Gửi yêu cầu truy vấn cấu hình tham số về eKYC Server (get-config)
 | 2 | 
 | eKYC Server | 
Xử lý và phản hồi các thông tin:

• Các cấu hình tham số sử dụng tại client (Theo nghiệp vụ hiện tại)
• Gửi yêu cầu truy vấn challengeCode sang VNPAY C06:

• Không thành công:
• Lỗi: Phản hồi lỗi SVC-COMMON-08
• Timeout
• Thành công: Phản hồi cấu hình tham số và challengeCode
 | 3 | KH nhấn Đã hiểu để bắt đầu thực hiện quét NFC | eKYC SDK | 
• Thực hiện xác thực chip bằng key:

• Không thành công: Hiển thị thông báo lỗi
• Thành công: Đọc dữ liệu NFC: DG1, DG2, DG13, DG14, DG15, SOD, COM
• Kiểm tra tính hợp lệ của chip:
• Kiểm tra Chip Clone, Chip Tamper theo nghiệp vụ hiện tại
• Thực hiện authen chip bằng challengeCode server gửi bước 2
• Gửi yêu cầu kiểm tra về eKYC Server, truyền lên các thông:

• Dữ liệu NFC: DG1, DG2, DG13, DG14, DG15, SOD, COM
• Kết quả authen chip: chipClone, dataNotTamper, challengeCodeSignature
 | 4 | 
 | eKYC Server | 
• Kiểm tra cờ chipClone và dataNotTamper:

• Không thành công: phản hồi cho client (chỉ check nếu mã lỗi ở trạng thái active)
 | STT | Trường | Giá trị | Mã lỗi
 | 1 | dataNotTamper | 0 | VAL-TAMPERINFO-67
 | 2 | chipClone | 0 hoặc -1 | VAL-CHIPCLONE-66

• Thành công: Tiếp tục thực hiện các nghiệp vụ khác
• Kiểm tra thông tin DG2 và challengeCodeSignature:
• Nếu DG2 ≠ null/empty và challengeCodeSignature ≠ null/empty: Gửi yêu cầu đến VNPAY C06 (API mới): (Chuyển bước 5)
• Các trường DG1, DG2, DG13, DG14, DG15, SOD,COM
• Kết quả authen chip bằng challengeCode (challengeCodeSignature)
• Trường hợp khác: eKYC Server gọi vào API verify C06 như hiện tại. (Sử dụng API cũ)
 | 5 | 
 | VNPAY C06 | 
Cập nhật kiểm tra thông tin:

• Kiểm tra ký Document Signature từ SOD:
• Chữ ký không hợp lệ: Phản hồi lỗi "DS is invalid"
• Chữ ký hợp lệ: chuyển sang 2
• Tính toán các DG Hash và so sánh với DG Hash trích suất từ SOD:
• Tồn tại DG Hash không khớp: Phản hồi lỗi 01
• Toàn bộ DG Hash trùng khớp: chuyển sang 3
• Kiểm tra dữ liệu xác thực chip (challengeCodeSignature):
• Dữ liệu không hợp lệ: Phản hồi lỗi 01
• Dữ liệu hợp lệ: Gửi yêu cầu kiểm tra chip sang Agent
• Phản hồi kết quả cho eKYC Server
 | 6 | 
 | eKYC Server | 
Nhận kết quả và phản hồi cho Client:

• Không thành công: bổ sung lỗi
• code = 01: Phản hồi sdk lỗi ERR-CHIPAUTHEN-01
• Thành công: phản hồi kết quả thành công SVC
 | 7 | 
 | eKYC SDK | 
Nhận kết quả và hiển thị theo nghiệp vụ

---

### 8.3. Thu thập STH kênh App- VneID

> **Page ID:** `677053853` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/677053853

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*3 trang con:*

#### 8.3.1. (Bank) SOW Thu thập STH qua VneID

> **Page ID:** `705400388` · **Version:** 9
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/705400388

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Thời gian cập nhật
 | 
 
 | A | HongLT | 
 | 
Tạo mới
 | V0.0.1 | 

### 1/ Tóm tắt Usecase
 | Use Case Name | Thu thập STH qua VNeID
 | Use Case ID | --
 | Use Case Description | 
• Cho phép KH lựa chọn hình thức thu thập STH thông qua:
        - VNeID (Luồng mới sẽ triển khai theo tài liệu này): Cho phép KH xác thực thông tin STH đã được định danh tại App VneID)

         - CCCD Chip (Luồng cũ đã triển khai: )

 | Actor | 
KH, MB App, eKYC SDK, MB Server, eKYC Server, Hệ thống VNeID

 | Priority | Medium
 | Trigger | 
KH chọn hình thức thu thập STH = VNeID

 | 
Pre-Condition
 | 
• KH có CCCD chip còn hạn
• KH đã được định danh điện tử mức độ 2 trở lên trên App VNeID
 | Post-Condition | 
KH được thu thập STH thành công, với nguồn thu thập = App VNeID

 | Bussiness Rules | 
1/ Giai đoạn hiện tại chỉ áp dụng thu thập STH qua Vneid với luồng thu thập STH chủ động

2/ Khi thực hiện Liveness cho phép kiểm tra bypass các mã lỗi dị tật theo CIF theo nghiệp vụ đã triển khai ()

3/ Sau khi xác thực STH thành công qua VNeID, lưu kho STH = Đã xác thực BCA và thực hiện FacePay như bình thường

(Phạm vi Bank sử dụng 2 dịch vụ tích dưới đây do VNeID cung cấp)

### 2/ Mockup cơ bản

<tham chiếu >

### 3/ Mô hình tích hợp

#### 3.1/ Môi trường test

trueUntitled Diagram-1746754254978falseautotoptrue11316021

#### 3.2/ Môi trường Production

trueUntitled Diagram-1746754402125falseautotoptrue11326041

### 4/ Phạm vi chức năng
 | 
 | Nhóm chức năng | Chức năng | Loại | Tác nhân | Mô tả cơ bản | Độ khó | Assign | Link
 | 1 | Thu thập STH trên kênh App | 
Thu thập qua App VNeID
 | 
RedThêm mới
 | MB App/ MB server/ eKYC server | 
• KH chọn thu thập STH qua App VNeID trên App CoopBank
• KH Thực hiện quét QR CCCD Chip trên App CoopBank
• KH Thực hiện liveness trên App CoopBank
• KH Đồng ý chia sẻ thông tin từ App VNeID trên App CoopBank
• KH Mở App VNeID và bấm Đồng ý chia sẻ
• KH quay về App CoopBank xác nhận thông tin KH vừa được VNeID chia sẻ
• Hệ thống CoopBank lưu thông tin thu thập STH từ VNeID = Đã xác thực BCA | 

 | 
ThaoCy
 | 

 | 2 | Quản lý dữ liệu thu thập | 
Báo cáo thu thập STH
 | 
BlueCẬP NHẬT
 | BO | 
Bổ sung cột nguồn thu thập gồm:

- NFC CCCD Chip

- App VNeID
 | 

 | 
ThaoCy
 | 

 | 3 | 
Quản lý eKYC
 | 
BlueCẬP NHẬT
 | BO | 
Bổ sung cột nguồn thu thập gồm:

• NFC CCCD Chip
• App VNeID
(Lưu ý: Với KH thu thập qua App VNeID không view được ảnh chụp mặt trước, chụp mặt sau và ảnh chân dung NFC do không có thông tin)
 | 

 | 
ThaoCy
 | 

 | 4 | Xác thực giao dịch bằng FacePay | 
Logic check FacePay
 | 
BlueCẬP NHẬT
 | eKYC server | 
Cập nhật logic so khớp ảnh khi FacePay: 

Ảnh liveness +ảnh thu thập+ ảnh NFC trên CHIP   (Bỏ so khớp ảnh NFC do VNeID không chia sẻ lại ảnh chip nên không có thông tin)
 | 

 | 
ThaoCy
 | 

### 5/ Đánh giá ảnh hưởng
 | 
 | Chức năng | Nội dung | Tác nhân | Đánh giá
 | 1 | Cài đặt thu thập STH trên App | 
Test ảnh hưởng hiển thị đối vớc

• Trạng thái= Đã xác thực BCA | App Client | Không ảnh hưởng, do logic khi thu thập STH qua App Vneid thành công sẽ lưu trạng thái= CHECKBIOMETRIC= 0 và StatusC06= đã xác thực nhưng vẫn nên test lại
 | 2 | FacePay | 
Xác thực bằng FacePay
 | eKYC server | 
 Do eKYC server sửa lại logic so sánh khuôn mặt với loại giấy tờ = Hộ chiếu.

- Test lại xác thực giao dịch tài chính = FacePay

- Test lại facepay tại login (đại diện 1 login type)

---

#### 8.3.2. Flow&Action Screen - Thu thập STH kênh App-VNeID

> **Page ID:** `710972546` · **Version:** 40
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/710972546

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThaoCY | 
 | 
Tạo mới tài liệu
 | 
V1.0.0

Mục lục

### 1/ Luồng màn hình

### 2/ Danh sách màn hình

##### MH1.1: Truy cập tính năng

##### MH1.2: Thu thập STH

##### MH2.1: Chọn hình thức thu thập STH <trường hợp chọn CCCD gắn chip>

##### MH2.2: Chọn hình thức thu thập STH <trường hợp chọn VNeID>

##### MH2.3: Chọn hình thức thu thập STH <trường hợp thiết bị không hỗ trợ NFC/không bật NFC>

##### 

##### MH3.1: Scan QR

##### MH3.2: Thông báo không khớp với thông tin lưu tại hệ thống MB

 MH4.1: Hướng dẫn liveness

 MH4.2: Thực hiện Liveness

 MH5.1: Xác nhận chia sẻ thông tin trên app CoopBank

##### MH5.2: Chờ xác nhận <trong phiên đăng nhập>

 MH6.1: Đăng nhập ứng dụng VNeID

 MH6.2: Xác nhận chia sẻ thông tin trên VNeID

##### MH7: Thông tin khách hàng

##### MH8.1: Kết quả thu thập STH <thất bại>

##### MH8.2: Kết quả thu thập STH <thành công>

##### MH9.1: Hết hạn xác nhận

##### MH9.2: Từ chối chia sẻ

### 3/ Mô tả màn hình

##### MH1.1: Truy cập tính năng

Tham chiếu Các chức năng Cài đặt

##### MH1.2: Thu thập STH

Tham chiếu 

##### MH2.1+2.2+2.3: Chọn hình thức thu thập 
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Text | ReadOnly | - | 
-
 | Chọn hình thức thu thập
 | 2 | Icon Back | Icon | Click | - | - | Click để quay lại màn hình cài đặt
 | 3 | Loại hình thức thu thập | Radio button | Click | Có | - | 
Gồm: 

• Căn cước công dân gắn chip (chỉ hiển thị trong trường hợp thiết bị có hỗ trợ NFC và đã bật NFC)
• Tài khoản định danh điện tử (VNeID) 
Mặc định chọn Căn cước công dân gắn chip

 | 4 | Text + Ảnh hướng dẫn | Label + Image | ReadOnly | - | - | 
Tùy thuộc vào lựa chọn hình thức thu thập sẽ hiển thị ảnh và nội dung hướng dẫn khác nhau:

• Nếu chọn Căn cước công dân gắn chip → Nội dung:
• Sử dụng thiết bị di động có hỗ trợ tính năng NFC để thực hiện đọc thông tin trong CCCD gắn chip
• Vui lòng sử dụng giấy tờ gốc (Bản chính) và còn hạn sử dụng
• Khách hàng không sử dụng Giấy tờ tùy thân giả mạo, không chính chủ. Khách hàng chịu hoàn toàn trách nhiệm trước pháp luật về thông tin giấy tờ tùy thân cung cấp cho ngân hàng.
• Nếu chọn Tài khoản định danh điện tử (VNeID) → Nội dung:
• Sử dụng tài khoản định danh điện tử (VNeID) mức 2 để thực hiện xác thực
• Vui lòng sử dụng giấy tờ gốc (Bản chính) và còn hạn sử dụng
• Khách hàng không sử dụng Giấy tờ tùy thân giả mạo, không chính chủ. Khách hàng chịu hoàn toàn trách nhiệm trước pháp luật về thông tin giấy tờ tùy thân cung cấp cho ngân hàng.
 | 5 | Tiếp tục | Button | Click | - | - | 
Tham chiếu logic xử lý

Luôn enable

##### MH3: Scan QR
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Icon Back | Icon | Click | - | - | Quay lại màn hình thao tác trước đó
 | 2 | Tiêu đề | Lable | ReadOnly | - | - | Scan QR
 | 3 | Nội dung | Lable | ReadOnly | - | - | Di chuyển camera để thấy rõ nét mã QR tại mặt trước của giấy tờ tùy thân. Hệ thống sẽ tự động quét mã QR
 | 4 | Vùng scan mã QR | Capture | View | - | - | 
Tự động scan mã QR

<Tham khảo luồng xử lý> 

 | 5 | Hướng dẫn quét QR | Lable | ReadOnly | - | - | 
Hiển thị thông tin hướng dẫn bằng hình ảnh và hướng dẫn bằng chữ

• Hướng camera vào vùng mã QR trên thẻ căn cước
 | 6 | Scan QR thành công | 
 | 
 | 
 | 
 | 
<Tham chiếu logic xử lý>

 | 7 | Scan QR thất bại | 
 | 
 | 
 | 
 | 
<Tham chiếu logic xử lý>

##### MH4.1: Hướng dẫn liveness

Tham chiếu 

##### MH4.2: Thực hiện Liveness
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề | Label | ReadOnly | - | - | Xác thực khuôn mặt
 | 2 | Hướng dẫn | Label | Auto action | - | - | 
Hướng dẫn xác thực:

• Label
 | 3 | Vùng chụp ảnh  | Capture | View | - | - | 
Tự động thực hiện quét khuôn mặt theo hướng dẫn thực hiện 

Hiển thị vòng trong oval xanh tương ứng với & hoàn tất hướng dẫn

Trong ảnh chụp ảnh, nế khuôn mặt thoát khỏi vùng định vị khuôn mặt (vòng tròn) thì reset quá trình quét khuôn mặt và lấy ngẫu nhiên các hướng dẫn khác để thực hiện xác thực khuôn măt

Hoàn thành 1 hướng dẫn thực hiện thì chuyển sang hướng dẫn thực hiện tiếp theo

 | 4 | Hướng dẫn hành động cần thực hiện | Label | ReadOnly | - | - | 
Danh sách các hành động cần thực hiện như sau:

• Di chuyển gần hơn 
• Di chuyển xa hơn
 | 5 | Hoàn thành | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hoàn thành

 | 6 | Nội dung hướng dẫn | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Nội dung được fix tại client: “Điều chỉnh khuôn mặt nằm trong khung hình”

##### MH5.1: Xác nhận chia sẻ thông tin trên app CoopBank
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề  | Text | ReadOnly | - | - | 
Xác nhận chia sẻ thông tin từ VNeID

 | 2 | Icon Back | Icon | Click | - | - | <tham chiếu logic xử lý>
 | 3 | Ảnh minh họa | Image | ReadOnly | - | - | Hình ảnh minh họa gồm Logo của CoopBank và VNeID, minh họa việc chia sẻ dữ liệu
 | 4 | Ghi chú | Text | ReadOnly | - | - | 
Bằng việc bấm chọn "Đồng ý chia sẻ thông tin", Quý khách đã xác nhận cho phép Co-opBank chia sẻ thông tin cá nhân và dữ liệu sinh trắc học tới hệ thống định danh điện tử VNeID

 | 5 | Đồng ý chia sẻ thông tin | Button | Click | - | - | 
Tham chiếu logic xử lý

Luôn enable

##### MH5.2: Chờ xác nhận <trong phiên đăng nhập>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề  | Text | ReadOnly | - | - | 
Xác nhận chia sẻ thông tin từ VNeID

 | 2 | Icon Back | Icon | Click | - | - | <tham chiếu logic xử lý>
 | 3 | Ảnh minh họa | Image | ReadOnly | - | - | Hình ảnh minh họa gồm Logo của CoopBank và VNeID, minh họa việc chia sẻ dữ liệu
 | 4 | Ghi chú | Text | ReadOnly | - | - | 
Chờ xác nhận

Co-opBank đã gửi yêu cầu tới hệ thống định danh điện tử VNeID. Quý khách vui lòng đăng nhập ứng dụng VNeID để xác nhận đồng ý chia sẻ thông tin với Co-opBank

 | 5 | Mở ứng dụng VNeID | Button | Click | - | - | 
<tham khảo logic xử lý>

##### MH7: Thông tin khách hàng
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tiêu đề màn hình
 | 
Text
 | 
ReadOnly
 | 
-
 | 
-
 | 
Xác nhận thông tin

 | 2 | 
Icon back
 | 
Icon
 | 
Click
 | 
-
 | 
-
 | 
Tham chiếu logic xử lý

 | 3 | 
Tiêu đề 2
 | 
Text
 | 
ReadOnly
 | 
-
 | 
-
 | 
Thông tin giấy tờ

 | 4 | 
Vùng hiển thị hình ảnh chân dung
 | 
Picture
 | 
Readonly
 | 
--
 | 
--
 | 
Hình ảnh chân dung khách hàng vừa thực hiện liveness

 | 5 | 
Loại giấy tờ
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị loại giấy tờ thực hiện eKYC

Mặc định: CCCD gắn chip

 | 6 | 
Số CCCD gắn chip
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Số CCCD gắn chip

Hiển thị thông tin VNeID trả về

citizenPid

 | 7 | 
Họ tên
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị họ tên khách hàng

Hiển thị thông tin VNeID trả về

fullName

 | 8 | 
Ngày sinh
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Định dạng hiển thị dd/mm/yyyy

Hiển thị thông tin VNeID trả về

birthDate

 | 9 | 
Giới tính
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị giới tính khách hàng

Hiển thị thông tin VNeID trả về

genderCode

1: Chưa rõ thông tin

2: Nam

3: Nữ

4: Khác

 | 10 | 
Quốc tịch
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị  từ GTTT

Hiển thị thông tin VNeID trả về

nationalityCode

• Nếu trả là "VN" → client hiển thị "Việt Nam"
• Nếu trả giá trị khác VN → client giữ nguyên
 | 11 | 
Nơi thường trú
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị nơi thường trú của khách hàng

Hiển thị thông tin VNeID trả về

permanentPlace

 | 12 | 
Nơi ở hiện tại
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị thông tin VNeID trả về

livingPlace

 | 13 | 
Ngày cấp
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Định dạng hiển thị dd/mm/yyyy

Hiển thị thông tin VNeID trả về

dateOfIssue

 | 14 | 
Nơi cấp
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị thông tin VNeID trả về

issuingAuthority

 | 15 | 
Có giá trị đến
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Hiển thị  từ GTTT

Hiển thị thông tin VNeID trả về

idCardExpireDate

 | 16 | 
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
Tham chiếu logic xử lý

Luôn enable

##### MH9.1: Hết hạn xác nhận
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề  | Text | ReadOnly | - | - | 
Xác nhận chia sẻ thông tin từ VNeID

 | 2 | 
Icon back
 | 
Icon
 | 
Click
 | 
-
 | 
-
 | 
Quay về MH chọn hình thức thu thập STH

 | 3 | Ảnh minh họa | Image | ReadOnly | - | - | Hình ảnh minh họa gồm Logo của CoopBank và VNeID, minh họa việc chia sẻ dữ liệu
 | 4 | Thông báo | Text | ReadOnly | - | - | 
Hết hạn xác nhận

Quý khách đã hết thời gian xác nhận chia sẻ thông tin từ VNeID. Vui lòng thực hiện lại.

 | 5 | Về trang chủ | Button | Click | - | - | 
Click quay về màn hình trang chủ 

Luôn enable

 | 6 | Thực hiện lại | Button | Click | - | - | 
Tham chiếu logic xử lý 

Luôn enable

##### MH9.2: Từ chối chia sẻ
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tiêu đề  | Text | ReadOnly | - | - | 
Xác nhận chia sẻ thông tin từ VNeID

 | 2 | 
Icon back
 | 
Icon
 | 
Click
 | 
-
 | 
-
 | 
Quay về MH chọn hình thức thu thập STH

 | 3 | Ảnh minh họa | Image | ReadOnly | - | - | Hình ảnh minh họa gồm Logo của CoopBank và VNeID, minh họa việc chia sẻ dữ liệu
 | 4 | Thông báo | Text | ReadOnly | - | - | 
Đã từ chối

Quý khách đã từ chối chia sẻ thông tin từ VNeID.

 | 5 | Về trang chủ | Button | Click | - | - | 
Click quay về màn hình trang chủ 

Luôn enable

---

#### 8.3.3. User action flow_Thu thập STH kênh App-VNeID (VNPAY-BANK)

> **Page ID:** `723157160` · **Version:** 11
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/723157160

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThaoCY | 
 | 
Tạo mới tài liệu
 | V1.0.0
Mục lục

### 1/ Mô tả Usecase
 | Use Case Name: | Thu thập STH kênh App-VNeID
 | Use Case ID: | UC_STH_VNeID
 | Use Case Description: | 
Là người dùng, tôi muốn thực hiện thêm mới/cập nhật dữ liệu sinh trắc học trên app CoopBank thông qua ứng dụng VNeID

 | Actor: | 
KH, Hệ thống MB, Hệ thống eKYC, SDK VNeID, App VNeID, VNeID server, GW Bank, GW VNeID

 | Priority: | Medium 
 | Trigger: | 
KH chọn hình thức thu thập STH = VNeID

 | Pre-Condition | 
1/ KH có CCCD chip còn hạn

2/ KH đã được định danh điện tử mức độ 2 trở lên trên App VNeID

 | Post-Condition: | 
KH được thu thập STH thành công, với nguồn thu thập = VNeID

 | Basic Flow: | 
1/ KH chọn Thu thập STH tại chức năng Cài đặt

2/ Hiển thị MH trạng thái STH của KH 

3/ KH chọn "Thu thập lại"

4/ Hiển thị màn hình chọn hình thức thu thập STH

Hệ thống MB kiểm tra:

• Nếu thiết bị không hỗ trợ NFC/không cài đặt NFC → Chỉ hiển thị lựa chọn Tài khoản định danh điện tử (VNeID)
• Nếu thiết bị có hỗ trợ NFC → Hiển thị 2 lựa chọn là Căn cước công dân gắn chip và Tài khoản định danh điện tử (VNeID)
5/ KH chọn hình thức thu thập 

• Nếu chọn Căn cước công dân gắn chip → Chuyển luồng 
• Nếu chọn Tài khoản định danh điện tử (VNeID) → Chuyển bước 6
6/ Thực hiện quét QR 

7/ Hệ thống MB so khớp thông tin đọc từ QR với thông tin KH lưu trữ tại MB

• Không hợp lệ → Hiển thị thông báo lỗi 
• Hợp lệ → Chuyển bước 8
8/ KH thực hiện Liveness

9/ Hệ thống eKYC check giả mạo

• Không hợp lệ → Hiển thị thông báo lỗi 
• Hợp lệ → Chuyển bước 10
10/ KH chọn Đồng ý chia sẻ

11/ Hệ thống MB gửi yêu cầu khởi tạo chia sẻ thông tin 

12/ VNeID server trả kết quả gồm transactionID

13/ Hệ thống MB hiển thị thông báo mời KH điều hướng đến mở app VNeID

14/ App VNeID: KH thực hiện đăng nhập, sau đó xác nhận chia sẻ thông tin 

15/ Hệ thống MB sinh nonce và truyền sang SDK VNeID: ảnh liveness, nonce

16/ SDK VNeID trích xuất đặc trưng và trả vector ảnh chân dung và ảnh kết quả về cho Hệ thống MB

17/ Hệ thống MB gửi yêu cầu lấy kết quả xác thực chia sẻ thông tin 

18/ VNeID server đối chiếu dữ liệu, trả kết quả xác thực

19/ Hệ thống MB hiển thị MH Thông tin KH

20/ KH nhấn Xác nhận

21/ Hệ thống MB so khớp thông tin KH do VNeID trả về với thông tin khách hàng lưu tại MB

• Không hợp lệ: Hiển thị thông báo lỗi 
• Hợp lệ: Chuyển sang 22
22/ Gửi yêu cầu lưu STH đến Hệ thống eKYC

23/ Hệ thống eKYC lưu STH KH và trả kết quả

24/ Hệ thống MB hiển thị MH thông báo thu thập STH thành công

 | Exception Flow: | 
1/ So khớp thông tin QR và thông tin KH trong DB không khớp → Trả kết quả lỗi 

2/ Từ chối chia sẻ thông tin trên ứng dụng VNeID

3/ So khớp thông tin từ app VNeID và thông tin KH trong DB không khớp → Trả kết quả lỗi

 | Bussiness Rules: | 
1/ Giai đoạn hiện tại chỉ áp dụng thu thập STH qua Vneid với luồng thu thập STH chủ động

2/ Khi thực hiện Liveness cho phép kiểm tra bypass các mã lỗi dị tật theo CIF theo nghiệp vụ đã triển khai (Quản lý danh sách khách hàng bypass mã lỗi eKYC)

3/ Sau khi xác thực STH thành công qua VNeID, lưu kho STH = Đã xác thực BCA và thực hiện FacePay như bình thường

(Phạm vi Bank sử dụng 2 dịch vụ tích dưới đây do VNeID cung cấp)

### 2/ Luồng nghiệp vụ

### 3/ Luồng xử lý

#### 3.1/ Truy cập chức năng

##### MH1.1: Truy cập chức năng

<tham chiếu tài liệu >
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Từ MH Cài đặt, chọn tính năng "Thu thập sinh trắc học" | Hệ thống MB | 
1/ Lấy Config hệ thống eKYC (thời gian scan QR, max tap NFC, vị trí đọc NFC theo thiết bị...), kiểm tra thông tin thiết bị, trạng thái thiết bị, lấy phiên thực hiện eKYC,..); lấy url video hướng dẫn NFC

2/ Kiểm tra thiết bị có hỗ trợ NFC hay không, nếu có hỗ trợ thì kiểm tra đã bật NFC chưa

• Thiết bị không hỗ trợ NFC/ có hỗ trợ nhưng chưa bật NFC → Cập nhật: KHÔNG hiển thị thông báo lỗi/thông báo yêu cầu bật NFC, chuyển sang 3
• Thiết bị có hỗ trợ NFC và đã bật NFC → chuyển sang 3
3/ Gửi yêu cầu kiểm tra trạng thái STH đến hệ thống eKYC theo CIF

 | Hệ thống eKYC | 
Nhận và xử lý 

• Không hợp lệ: Trả mã lỗi tương ứng 
• Hợp lệ: Kiểm tra trạng thái STH và loại GTTT tại Kho STH và trả kết quả cho hệ thống MB
• Với KH thu thập loại GTTT = CCCD chip
• Đối với KH đã thực hiện luồng eKYC Onboarding mói có tích hợp check C06
• Đã có dữ liệu STH check thành công C06 → CHECK_BIOMETRIC=0
• Đã có dữ liệu CCCD gắn chip, liveness nhưng chưa xác thực C06 → CHECK_BIOMETRIC=2
• Đối với KH chưa thực hiện luồng eKYC Onboarding mới có tích hợp check C06
• Chưa có dữ liệu STH → CHECK_BIOMETRIC=1
• Đã có dữ liệu CCCD gắn chip, liveness, chưa xác thực C06 → CHECK_BIOMETRIC=2
• 
Với KH thu thập loại GTTT = Hộ chiếu (chỉ có kênh quầy mới cho thu thập Hộ chiếu)

• Thu thập STH Hộ chiếu tại Quầy thành công ( Không check C06) →CHECK_BIOMETRIC=0
• Thu thập STH Hộ chiếu tại Quầy không thành công → CHECK_BIOMETRIC=1
 | Hệ thống MB | 
Nhận và hiển thị tương ứng

Không hợp lệ: Hiển thị mã lỗi 

Hợp lệ: 

•  Đã xác thực → Hiển thị MH 1.2 <Tham chiếu >  và hiển thị trạng thái xác thực BCA theo loại GTTT như sau:
• Thu thập = CCCD Chip: Trạng thái xác thực BCA= Đã xác thực BCA
• Thu thập = Hộ chiếu thành công (Chỉ áp dụng với kênh Quầy): Trạng thái xác thực BCA = Đã xác thực
• Chưa xác thực STH: Hiển thị MH 1.2 hoặc 1.3  <Tham chiếu > 
• KH chưa từng thực hiện luồng thu thập STH → Hiển thị MH 1.3.
• KH đã từng thực hiện luồng thu thập STH nhưng chưa xác thực thành công → Hiển thị MH 1.2 + Trạng thái xác thực = Chưa xác thực BCA

##### MH1.2: Thu thập STH
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn "Thu thập lại" | Hệ thống MB | 
Thực hiện kiểm tra

• Nếu thiết bị có hỗ trợ NFC và đã bật NFC → Hiển thị MH2.1
• Nếu thiết bị không hỗ trợ NFC/ không bật NFC → Hiển thị MH2.3 (mặc định chọn hình thức Tài khoản định danh điện tử (VNeID))
 | 2 | Chọn "Căn cước công dân gắn chip" | Hệ thống MB | Tham chiếu  >
 | 3 | Chọn "Tài khoản định danh điện tử (VNeID) | Hệ thống MB | Gửi yêu cầu khởi tạo eKYC SDK với hình thức thu thập là VNeID

#### 3.2/ Luồng chức năng chính

##### MH3.1: Scan QR
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Quét mã QR trên CCCD | Hệ thống MB/ Hệ thống eKYC | 
Hệ thống tự động quét mã QR cho đến khi nhận được thông tin hợp lệ theo đúng định dạng quy định:

• Không thành công: Hiển thị thông báo lỗi | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | QR sai định dạng | Định dạng mã QR không hợp lệ, Quý khách vui lòng thực hiện quét mã QR trên giấy tờ tùy thân | Hiển thị nút Đóng, click chọn "Đóng" → Tắt popup thông báo

Lưu ý
Luồng VNeID không check tham số ScanQR_Time

• Thành công: Hiển thị thông báo "Scan QR thành công". Đồng thời
• 1/ Lưu thông tin khách hàng đọc từ QR
• 2/ Gửi yêu cầu so khớp thông tin KH đọc được từ mã QR với thông tin lưu tại DB qua mid510Input
• Họ tên
• Ngày sinh
• Giới tính
 | Hệ thống MB | 
Kiểm tra thông tin dữ liệu nhận được với dữ liệu khách hàng: Họ tên, Ngày sinh, Giới tính phải trùng với thông tin khách hàng lưu trữ tại BD

• Lưu ý khi so khớp: 
• Check Họ tên ko dấu, ko phân biệt hoa thường (Bỏ dấu Tiếng việt và ký tự đặc biệt thường có ở tên người dân tộc, bao gồm các ký tự: Nháy thẳng ' , nháy chéo ’ , gạch ngang - , dấu huyền`, dấu ngã ~, dấu mũ trăng, dấu mũ nón)   
• Ví dụ:
• nếu có ký tự ' (H') → bỏ ký tự ' chỉ còn H, nếu có ký tự - (Y-) → bỏ - chỉ còn Y
• nếu có dấu mũ thì bỏ dấu: ŏ → o, ŭ → u, č → c, ĕ → e, ĭ → i, Ñ -> N
• Không hợp lệ: Hiển thị thông báo lỗi: "Thông tin khách hàng không hợp lệ. Vui lòng kiểm tra lại thông tin"Lưu ý
• Chọn Đóng → Tắt popup thông báo, giữ nguyên màn hình hiện tại (không giới hạn số lần cho phép scan lại QR)
• Với HĐH AND, sau khi scanQR xong, hiển thị màn hình Chọn hình thức thu thập ở trạng thái loading, đồng thời client gọi ngầm API so khớp thông tin KH đến server → Popup thông báo hiển thị trên MH Chọn hình thức thu thập STH
• Với HĐH iOS, client có thể gọi ngầm API so khớp thông tin KH đến server ngay tại màn hình scanQR → popup thông báo hiển thị trên màn hình scanQR
• Hợp lệ: Hiển thị MH liveness

##### MH4.2: Thực hiện Liveness
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chụp ảnh khuôn mặt | Hệ thống eKYC | 
Thực hiện Liveness theo yêu cầu

Hệ thống eKYC thực hiện kiểm tra khuôn mặt của KH như:

• Không tìm thấy khuôn mặt trong ảnh chân dung
• Phát hiện khuôn mặt giả mạo
• ...
→ Khuôn mặt không hợp lệ → Thông báo lỗi theo bảng mã lỗi tương ứng → Quay về bước chụp ảnh liveness

→ Khuôn mặt hợp lệ → Gửi kết quả liveness thành công cho Hệ thống MB

 | Hệ thống MB | 
Nhận kết quả

• Không hợp lệ: Hiển thị thông báo lỗi tương ứng.  Lỗi Liveness: Back của thiết bị + Back của App + Submit (Chụp lại): đều về màn Chọn hình thức thu thập STH
• Hợp lệ: Hiển thị MH Xác nhận chia sẻ thông tin trên app CoopBank

##### MH5.1: Xác nhận chia sẻ thông tin trên app CoopBank
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn icon Back | Hệ thống MB | Hiển thị thông báo: "Thông tin vừa xác nhận cập nhật sẽ không được lưu, Quý khách muốn hủy và thực hiện lại?" với 2 button: Đồng ý và Đóng
• Chọn Đóng: Tắt thông báo, giữ nguyên màn hình hiện tại
• Chọn Đồng ý: Điều hướng về màn hình Chọn hình thức thu thập STH
 | 2 | Chọn "Đồng ý chia sẻ thông tin" | Hệ thống MB | 
Gửi yêu cầu khởi tạo chia sẻ thông tin đến GW Bank qua API api/agent/init

Input: 

• Fullname
• birthDate
• citizenPid
 | GW Bank | 
Chuyển tiếp yêu cầu

 | GW VNeID | 
Chuyển tiếp yêu cầu

 | VNeID server | 
Xử lý và trả kết quả khởi tạo chia sẻ cho Hệ thống MB qua GW

• Không hợp lệ: Trả thông báo lỗi 
• Hợp lệ: Trả thông tin bao gồm:
• txnId 
• responseTime
 | GW VNeID | 
Chuyển tiếp kết quả

 | GW Bank | 
Chyển tiếp kết quả

 | Hệ thống MB | 
Nhận kết quả:

• Không thành công: Trả về thông báo lỗi: | Trường hợp | Nội dung thông báo | Xử lý nếu có
 | TO | Kết nối đến hệ thống ngân hàng bị gián đoạn. Quý khách vui lòng thử lại sau. | 

 | Các mã lỗi theo responeCode≠0 | Tham chiếu thông báo bảng mô tả mã lỗi mục 4 | 

 | 
Server kiểm tra giá trị trường responeTime 

• responseTime = Ngày hiện tại ở Server: Server thực hiện tính expireTime trả về cho client
• 
Thời gian hết hạn xác nhận chia sẻ: expireTime=responeTime + 5p (cấu hình tại tham số VNEID_EXPIRED_TIME, tính theo phút)

• responseTime # Ngày hiện tại ở Server: Server trả thông báo lỗi  | Dữ liệu không hợp lệ. Quý khách vui lòng thực hiện lại. | 

• Hợp lệ: Lưu cache lại thông tin cho bước tiếp theo. Hiển thị MH Popup điều hướng mở ứng dụng VNeID

#####  MH5.2: Chờ xác nhận + MH9.1: Hết hạn xác nhận
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Chọn "Mở ứng dụng VNeID" | Hệ thống MB | 
Điều hướng đến app VNeID theo urlApp được cấu hình tại server

Dựa theo giá trị expireTime, Hệ thống MB xử lý:

• Thời gian hiện tại trên app < expireTime: Tiếp tục hiển thị màn hình chờ xác nhận 
• Thời gian hiện tại trên app ≥ expireTime: Chưa nhận được kết quả phản hồi từ VNeID → Hiển thị màn hình Hết hạn xác nhận gồm 2 button
• Nhấn Về trang chủ: Quay về màn hình Home
• Nhấn Thực hiện lại: Quay về màn hình Chọn hình thức thu thập STHLưu ý
• Trong trường hợp KH thoát phiên đăng nhập trên app CoopBank, (hết phiên/đăng xuất/kill app) → Khi khách hàng đăng nhập lại sẽ cần thực hiện thu thập STH lại từ đầu
 | 2 | Chọn icon Back tại màn hình Chờ xác nhận | Hệ thống MB | Hiển thị thông báo: "Thông tin vừa xác nhận cập nhật sẽ không được lưu, Quý khách muốn hủy và thực hiện lại?" với 2 button: Đồng ý và Đóng
• Chọn Đóng: Tắt thông báo, giữ nguyên màn hình hiện tại
• Chọn Đồng ý: Điều hướng về màn hình Chọn hình thức thu thập STH

##### MH6.2: Xác nhận chia sẻ thông tin trên VNeID
 | 
 | Thao tác | Tác nhân | Mô tả
 | 1 | Thực hiện đăng nhập VNeID và xác nhận đồng ý/ không đồng ý chia sẻ thông tin trên App VNeID | App VNeID | 
Phản hồi điều hướng về lại app Co-opBank sau khi khách hàng xác thực chia sẻ thông tin theo cấu trúc quy định 
Lưu ý
VNPAY cung cấp cho VNeID deeplink để VNeID cấu hình điều hướng quay về lại app Co-opBank

 | Hệ thống MB | 
1/Nhận phản hồi:

• 
• Đồng ý chia sẻ → Tiếp tục luồng thu thập, chuyển sang 2
• Không đồng ý chia sẻ → Hiển thị màn hình Từ chốt chối chia sẻ
• Chọn Về trang chủ: Quay về màn hình Home
• Hết hạn chia sẻ: Hiển thị màn hình Hết hạn xác nhận gồm 2 button:
• Nhấn Về trang chủ: Quay về màn hình Home
• Nhấn Thực hiện lại: Quay về màn hình Chọn hình thức thu thập STH
Lưu ý

Cách xử lý khi hết hạn:

• Phía client tự kiểm tra thời gian hết hạn theo expireTime server trả về
• Nếu đã hết hiệu lực → Hiển thị màn hình Hết hạn xác nhận
• Nếu VNeID trả call sau thời điểm hết hạn → Client không quan tâm giá trị result. Hết hạn xác nhận sẽ dừng luồng
2/ Thực hiện gen nonce theo quy định 

3/ Gửi yêu cầu trích xuất ảnh gồm các thông tin: Ảnh liveness (truyền dạng base64), Nonce đến SDK VNeID

 | SDK VNeID | 
Nhận yêu cầu, xử lý dữ liệu và trả kết quả:
Output
• Dữ liệu khuôn mặt (encryptedFaceImages)
• Chữ ký xác thực dữ liệu (phục vụ verify data)
 | Hệ thống MB | 
Nhận kết quả:

• Trường hợp không nhận được kết quả của SDK (quá thời gian quy định, tạm thời config là 5ph): Hiển thị thông báo lỗi SDK: "Đã xảy ra lỗi trong quá trình thực hiện xử lý. Quý khách vui lòng thực hiện lại!".
• Button Đóng: Tắt thông báo, điều hướng về màn hình Chọn hình thức thu thập STH
• Trường hợp SDK trả kết quả lỗi: Hiển thị màn hình thông báo lỗi SDK

• Button Về trang chủ: Quay về màn hình Home
• Button Thử lại: Tắt thông báo, điều hướng về màn hình Chọn hình thức thu thập STH
• Trường hợp SDK trả kết quả thành công: Kiểm tra thông tin dữ liệu 2 trường (signature, startFaceAuthenWithFaceBase64)
• Không có giá trị: Hiển thị thông báo lỗi SDK
• Có giá trị: Gửi yêu xác thực chia sẻ thông tin đến GW Bank qua API /api/get-transaction
• Input
• transactionID
• faceImage (base64)
 | GW Bank | 
Chuyển tiếp yêu cầu

 | GW VNeID | 
Chuyển tiếp yêu cầu

 | VNeID server | 
Validate và đối chiếu thông tin KH từ dữ liệu lưu tại VNeID và dữ liệu do hệ thống MB truyền sang (ảnh được đối chiếu là ảnh lấy từ SDK VNeID trích xuất)

• Không hợp lệ: Trả về tỷ lệ so khớp ảnh và thông báo lỗi 
• Hợp lệ: Trả về tỷ lệ so khớp ảnh và các thông tin:
• Họ và tên
• Số CCCD
• Ngày sinh
• Giới tính
• Ngày cấp
• Nơi cấp
• Ngày hết hạn
• Quốc tịch
• Địa chỉ thường trú
• Nơi ở hiện tại
• Kết quả xác thực (result)
• Trọng số kết quả (score)
 | GW VNeID | 
Chuyển tiếp kết quả

 | GW Bank | 
Chuyển tiếp kết quả

 | Hệ thống MB | 
Nhận kết quả 

• Không hợp lệ: Trả thông báo lỗi tương ứng  | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | TO | Kết nối đến hệ thống ngân hàng bị gián đoạn. Quý khách vui lòng thử lại sau. | 

 | Các mã lỗi theo responeCode≠0 | Tham chiếu thông báo bảng mô tả mã lỗi mục 4 | 

• Hợp lệ: Hiển thị màn hình Thông tin khách hàng gồm các thông tin server trả về và ảnh chân dung hợp lệ KH đã chụp trước đóLưu ý
API /api/get-transaction trả về trường result tổng và result faceMatch. Co-opBank chỉ sử dụng dịch vụ facematch nên 2 trường này có ý nghĩa như nhau, và luôn trả v

> ⚠️ *Nội dung đã cắt ngắn (21419 ký tự gốc). Xem đầy đủ trên Confluence.*


---


## 35. Nghiệp vụ bảo mật

> **Page ID:** `825361904` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/825361904

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*2 trang con:*

### 35.1. Xác thực giao dịch nhận biết thiết bị rủi ro VNShield

> **Page ID:** `806521911` · **Version:** 1
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/806521911

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*1 trang con:*

#### 35.1.1. [BANK] Xác thực giao dịch nhận biết thiết bị rủi ro VNShield

> **Page ID:** `806521963` · **Version:** 19
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/806521963

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
  
 | A | ThaoCY | 
 | 
Tạo mới tài liệu
 | V.1.0.0
 | 
 
 | M | ThaoCY | V.1.0.0 | 
Cập nhật luồng xác thực thiết bị rủi ro

• Cập nhật lại tên tham số
• Đảo thứ tự bước sinh ShieldID và so sánh ShieldID trong cache lên trước bước Tính (Ngày giao dịch - Ngày kích hoạt lại app)
• Đảo thứ tự bước kiểm tra tham số Shieldid_ON_OFF lên trước bước kiểm tra Whitelist user
• Bỏ bước sinh dToken | V.1.0.1
Mục lục

### 1/ Tóm tắt usecase
 | Use Case Name | Xác nhận giao dịch từ thiết bị rủi ro theo giải pháp VNShield
 | Use Case ID | UC_XTGD_01
 | Use Case Description | 
KH thực hiện xác nhận giao dịch từ thiết bị rủi ro theo giải pháp VNShield  sẽ nhận được thông báo lỗi và ứng dụng điều hướng KH về trang chủ ứng dụng

 | Actor | 
User, App Client, App Server

 | Priority | 
High

 | Trigger | 
KH thực hiện xác nhận giao dịch

 | 
Pre-Condition
 | 
• KH thực hiện xác nhận giao dịch có MID thuộc danh sách MID cần kiểm tra rủi ro thiết bị
• Thiết bị KH thực hiện nằm trong danh sách rủi ro được phân tích & tổng hợp của VNShield
• KH không thuộc danh sách Whitelist VNShield
 | Post-Condition | 
• KH nhận được thông báo lỗi khi xác nhận giao dịch
• Giao dịch không thành công
 | Basic Flow | 
• KH thực hiện xác nhận giao dịch
• App Client gửi yêu cầu xác nhận giao dịch
• App Server kiểm tra thiết bị có rủi ro không
• Nếu không: Thực hiện tiếp nghiệp vụ hiện tại
• Nếu có: Dừng giao dịch, trả thông báo lỗi
• App Client hiển thị thông báo lỗi và điều hướng KH về màn hình trang chủ ứng dụng.
 | Alternative Flow | 
• Trên một thiết bị bị chặn giao dịch, sau khi hết thời gian chặn KH có thể thực hiện giao dịch như thông thường nếu thiết bị KH đã gỡ các phần mềm VNShield đánh giá có rủi ro (VNShiled không còn phát hiện rủi ro)
• KH tới CN hoặc gặp tư vấn viên để được yêu cầu add vào Whitelist, khi đó KH thực hiện giao dịch thông thường trên mọi thiết bị. 
 | Exception Flow | 
• Khi KH thực hiện login vào app MB, VNShield chủ động cập nhật rủi ro về thiết bị của KH và gửi thông tin về App Server. Nếu trong khoảng thời gian KH đang bị chặn, mỗi thời điểm VNShield phát hiện thiết bị KH có rủi ro thì App Server tăng thời gian chặn giao dịch của KH lên tương ứng.
 | Bussiness Rules | 
• BR1: Chỉ những phiên bản ứng dụng Android, iOS thuộc tham số cấu hình (VERSION_APP_MDS_IOS/VERSION_APP_MDS_ANDROID) thì mới kiểm tra rủi ro theo nghiệp vụ VNShield.
• BR2: Chỉ khi tham số kiểm tra rủi ro VNShield (FLAG_CHECK_MDS) ở trạng thái Bật thì mới kiểm tra rủi ro theo nghiệp vụ VNShield.
• BR3: Chỉ những MID thuộc tham số cấu hình (MID_CHECK_MDS) thì mới kiểm tra rủi ro theo nghiệp vụ VNShield.
• BR4: Giao dịch của KH theo BR3 bị chặn theo mức User trên mọi thiết bị khi: 
• Tham số chặn giao dịch (SHIELDID_ON_OFF) ở trạng thái Bật và;
• KH thuộc danh sách rủi ro và còn hiệu lực chặn và;
• KH không thuộc Whitelist hoặc Whitelist hết hiệu lực.
 | Non-Funtional Requirement | 
•  Hiệu năng: Phản hồi các bước < 2s.
 | Các lưu ý khác | 
• Thuật toán sinh shieldId và verify dToken do Dev Team của VNSHIELD và kênh ứng dụng thống nhất trên cơ sở nguyên tắc chung.

### 2/ Luồng sơ đồ

#### 2.1/ Luồng tổng quan

Mô hình tổng quan hệ thống

####  2.2/ Luồng kiểm tra thiết bị rủi ro từ App Server

trueUntitled Diagram-1759997154643falseautotoptrue74822143

### 3/ Mô tả luồng xử lý chi tiết
 | 
 | Tác nhân | Mô tả
 | 1 | KH | 
Thực hiện xác nhận giao dịch

 | 2 | App Client | 
Gửi yêu cầu xác nhận giao dịch

 | 3 | App Server | 
BƯỚC 1: Kiểm tra phiên bản ứng dụng

Điều kiện: So sánh phiên bản app với tham số VNSHIELD_VERSION_APP_IOS/ VNSHIELD_VERSION_APP_ANDROID
 | | 
Điều kiện
 | 
Hành động

 | 
Phiên bản < Tham số
 | 
TIẾP TỤC giao dịch như hiện tại

 | 
Phiên bản ≥ Tham số
 | 
CHUYỂN Bước 2

BƯỚC 2: Kiểm tra flag VNShield

Điều kiện: Kiểm tra tham số VNSHIELD_FLAG
 | | 
Giá trị
 | 
Hành động

 | 
OFF
 | 
TIẾP TỤC giao dịch như hiện tại

 | 
ON
 | 
CHUYỂN Bước 3

BƯỚC 3: Kiểm tra MID trong danh sách

Điều kiện: Kiểm tra MID có trong tham số VNSHIELD_CHECK_MID
 | | 
Điều kiện
 | 
Hành động

 | 
MID KHÔNG thuộc danh sách
 | 
TIẾP TỤC giao dịch như hiện tại

 | 
MID thuộc danh sách
 | 
CHUYỂN Bước 4

BƯỚC 4: Kiểm tra cache user rủi ro

Điều kiện: User đã tồn tại trong cache chưa?
 | | 
Trạng thái
 | 
Hành động

 | 
ĐÃ tồn tại
 | 
• Lưu lịch sử GD kiểm tra VNSHIELD 
• Chuyển bước 10
 | 
Không tồn tại
 | 
CHUYỂN Bước 5

BƯỚC 5:  App Server sinh ShieldID

• App Server kiểm tra thông tin và sinh ShieldID:
• Android: Phone + IMEI + Device Name
• iOS: Phone + PM + OV | Kết quả | Hành động
 | Thất bại | 
• Sinh ShieldID theo "UUID"
• Lưu lịch sử GD kiểm tra VNSHIELD 
• Tiếp tục giao dịch như hiện tại
 | Thành công | Chuyển bước 6

BƯỚC 6: So sánh ShieldId

Điều kiện: So sánh ShieldId do App Server sinh với ShieldId trong cache thiết bị rủi ro
 | Kết quả | Hành động
 | Tồn tại | 
• Lưu lịch sử GD kiểm tra VNSHIELD
• Lưu User vào Redis Cache user rủi ro
• Chuyển bước 10
 | Không tồn tại | Chuyển bước 7

BƯỚC 7: So sánh thời gian kích hoạt app cần kiểm tra dToken

Điều kiện: Lấy (ngày giao dịch hiện tại - ngày kích hoạt app) và so với tham số VNSHIELD_NUMBER_DAY_CHECK_DTOKEN_REACTIVATE

Thông tin ngày kích hoạt app của User có thể lưu vào Redis cache với thời gian hiệu lực cache là tính từ ngày kích hoạt cộng với tham số NUMBER_DAY_CHECK_DTOKEN_REACTIVATE để tối ưu truy vấn.
 | Kết quả | Hành động
 | 
Lớn hơn tham số
 | Tiếp tục giao dịch như hiện tại
 | 
Nhỏ hơn hoặc bằng tham số
 | Chuyển bước 8

BƯỚC 8: So sánh dToken

Điều kiện: Nhận kết quả so sánh dToken của client truyền lên và của lib
 | Kết quả | Hành động
 | Hợp lệ | Tiếp tục giao dịch như hiện tại
 | Không hợp lệ | 
• Lưu lịch sử GD kiểm tra VNSHIELD
• Chuyển bước 9

BƯỚC 9: Kiểm tra cờ dToken

Điều kiện: Kiểm tra tham số dToken: VNSHIELD_VERIFY_TOKEN
 | Kết quả | Hành động
 | OFF | Tiếp tục giao dịch như hiện tại
 | ON | Chuyển bước 10

BƯỚC 10: Kiểm tra tham số VNSHIELD_SHIELDID_ON_OFF

Điều kiện: Kiểm tra giá trị tham số VNSHIELD_SHIELDID_ON_OFF
 | Trường hợp | Giá trị tham số | Hành động
 | 
• User tồn tại trong cache rủi ro
hoặc;

• Shieldid tồn tại trong cache rủi ro
hoặc;

• Tham số dToken = ON | OFF | Tiếp tục giao dịch như hiện tại
 | 
• User tồn tại trong cache rủi ro
hoặc;

• Shieldid tồn tại trong cache rủi ro
hoặc;

• Tham số dToken = ON | ON | Chuyển bước 11

BƯỚC 11: Kiểm tra Whitelist User VNSHIELD

Điều kiện: User có trong Whitelist và còn hiệu lực?
 | Kết quả | Hành động
 | 
Thuộc Whitelist VÀ còn hiệu lực
 | 
Tiếp tục giao dịch như hiện tại

 | 
KHÔNG thuộc Whitelist HOẶC hết hiệu lực
 | 
Chuyển bước 12

 BƯỚC 12: Thực hiện chặn giao dịch
 | Trường hợp | Hành động
 | User đã tồn tại trong cache rủi ro (B4) Hoặc ShieldId tồn tại (B6) | 
• Thông báo chặn giao dịch với nội dung cấu hình:
Giao dịch bị CHẶN do hệ thống phát hiện ứng dụng Co-opBank hoặc thiết bị di động của Quý khách đang sử dụng không an toàn. Đề nghị Quý khách thực hiện các biện pháp đảm bảo an toàn: Gỡ bỏ ứng dụng Co-opBank hiện tại, cài đặt lại ứng dụng do Co-opBank phát hành từ chợ ứng dụng chính thức của hệ điều hành, đổi mật khẩu và không cung cấp thông tin (tên đăng nhập, mật khẩu, mã OTP) cho bất kỳ ai. Sau <x> phút, nếu thực hiện các biện pháp đảm bảo an toàn, Quý khách có thể sử dụng ứng dụng Co-opBank. Trường hợp có vướng mắc, vui lòng liên hệ Hotline 1900545554. hoặc đến CN/PGD Co-opBank gần nhất để được hỗ trợ.

• Trả kết quả cho App Client
 | User chưa tồn tại trong cache rủi ro (B4) Và ShieldId không tồn tại (B6) Và dToken không hợp lệ (B8) | 
• Lưu User vào Redis Cache user rủi ro
• Thông báo chặn giao dịch với nội dung cấu hình:
Giao dịch bị CHẶN do hệ thống phát hiện ứng dụng Co-opBank hoặc thiết bị di động của Quý khách đang sử dụng không an toàn. Đề nghị Quý khách thực hiện các biện pháp đảm bảo an toàn: Gỡ bỏ ứng dụng Co-opBank hiện tại, cài đặt lại ứng dụng do Co-opBank phát hành từ chợ ứng dụng chính thức của hệ điều hành, đổi mật khẩu và không cung cấp thông tin (tên đăng nhập, mật khẩu, mã OTP) cho bất kỳ ai. Sau <x> phút, nếu thực hiện các biện pháp đảm bảo an toàn, Quý khách có thể sử dụng ứng dụng Co-opBank. Trường hợp có vướng mắc, vui lòng liên hệ Hotline 1900545554. hoặc đến CN/PGD Co-opBank gần nhất để được hỗ trợ.

• Trả kết quả cho App Client

 | 4 | App Client | 
Không nhận được kết quả:

• Hiển thị thông báo lỗi timeout client → Đóng popup, xử lý điều hướng theo nghiệp vụ hiện tại.
Nhận được kết quả:

• Thành công: Xử lý như hiện tại
• Lỗi:
• Lỗi khác: Xử lý như hiện tại.
• Lỗi thiết bị rủi ro:
• Nội dung thông báo theo App Server trả về.
• Nút thao tác:
• Đóng: Nhấn nút, đóng popup và điều hướng KH về màn hình Trang chủ ứng dụng.

### 4/ Bảng dữ liệu tại cấu phần Mobile Banking

#### 4.1/ Bảng config
 | 
 | Mã tham số | Giá trị tham số | Mô tả | Tại sao cần?
 | 1 | VNSHIELD_VERSION_APP_IOS | <Theo phiên bản tại thời điểm tích hợp> | Phiên bản iOS có kiểm tra VNShield | 
• Đảm bảo phiên bản có tích hợp SDK VNShield mới cần kiểm tra.
 | 2 | VNSHIELD_VERSION_APP_ANDROID | <Theo phiên bản tại thời điểm tích hợp> | Phiên bản ANDROID có kiểm tra VNShield | 

 | 3 | VNSHIELD_FLAG | 
• ON
• OFF | Cờ on/off kiểm tra VNShield | 
• Đảm bảo cho nhu cầu kiểm tra của Ngân hàng ở mỗi thời điểm khi cần thiết.
 | 4 | VNSHIELD_CHECK_MID | Danh sách mid check MDS | Loại giao dịch | Mid xác nhận
 | Chuyển tiền nội bộ | 19
 | Chuyển tiền nội bộ cùng chủ | 39
 | Chuyển  tiền 247 qua số thẻ | 24
 | Chuyển tiền 247 qua số tài khoản | 24
 | Nạp tiền điện thoại | 33
 | Thanh toán hóa đơn | 41
 | Thanh toán truyền hình cáp | 45
 | Thanh toán cước di động trả sau | 47
 | Thanh toán vé máy bay | 49
 | Nạp tiền giao thông | 51
 | Thanh toán QR | 53,56
 | Danh sách MID cần check rủi ro thiết bị khi xác nhận giao dịch | 
• Chủ động tham số kiểm tra các giao dịch quan trọng, đặc biệt các giao dịch có trích nợ tài khoản nguồn.
• Bước xác nhận giao dịch là bước chặn chốt cuối cùng trong luồng giao dịch, là thời điểm quyết định việc trích nợ tài khoản. Ngoài ra, chặn ở bước này giúp hệ thống có thêm những log dữ liệu thu thập trước đó.
 | 5 | 
VNSHIELD_VERIFY_TOKEN
 | 
• ON
• OFF | 
Cờ on/off có kiểm tra dToken hay không

• ON: Có check
• OFF: Không check | 
• Đảm bảo khi việc kiểm tra dToken gặp lỗi nhiều thì có thể OFF để bypass
 | 6 | 
VNSHIELD_NUMBER_DAY_CHECK_DTOKEN_REACTIVATE
 | 5 | Khoảng thời gian kích hoạt lại user cần kiểm tra dToken | 
• Đảm bảo sau thời gian này, dToken sẽ không bị thay đổi khi kích hoạt lại.
 | 7 | 
VNSHIELD_SHIELDID_ON_OFF
 | 
• ON
• OFF | Cờ on/off có chặn giao dịch với VNShield không | 
• Đảm bảo cho nhu cầu của Ngân hàng ở mỗi thời điểm khi cần thiết.
 | 8 | VNSHIELD_TIME_EXPIRED_WHITELIST | 
7
 | Thời gian (ngày) hết hiệu lực Whitelist tính từ thời điểm thêm vào Whitelist | 
• Đảm bảo trong thời gian Whitelist, KH có thể thực hiện được các giao dịch và có thời gian để xử lý các vấn đề rủi ro của thiết bị.
 | 9 | VNSHIELD_TIME_EXPIRED_RISK | 180 | Thời gian (phút) hết hiệu lực chặn của thiết bị được nhận diện rủi ro từ VNShield | 
• Đảm bảo trong khoảng thời gian này, kẻ tấn công khó có thể sử dụng các hành vi tấn công khác vào ứng dụng.

---

### 35.2. Bảo mật_Key Default

> **Page ID:** `818547062` · **Version:** 16
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/818547062

Mục lục
 none

### 1/ Lịch sử thay đổi
Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | ThaoCY | 
 | 
Tạo mới tài liệu
 | V.1.0.0

### 2/ Bối cảnh & giải pháp
 | Bối cảnh | 
• Giao tiếp giữa app client và app server trong các MID Request có sử dụng "key default" và "key user", tuy nhiên "key default" ở phía app client đang sử dụng cho cả trường hợp MID sau khi kích hoạt user → chưa đảm bảo sự bảo mật (Chỉ với HĐH Andorid)
• Ứng dụng Android và iOS đang sử dụng 1 "key default" cho tất cả các phiên bản ứng dụng, có thể chưa an toàn.
 | Giải pháp | 
• Nâng cấp cơ chế sử dụng key default theo phiên bản ứng dụng (version app) và bổ sung logic xử lý check key default tại Server để nâng cao tính bảo mật
 | Đánh giá ảnh hưởng | 
• Việc cập nhật nghiệp vụ này sẽ áp dụng cho các phiên bản ứng dụng mới. Vì vậy, đối với các phiên bản app cũ (được hiểu là bản app chưa sử dụng key default theo version app) CẦN cập nhật lên phiên bản app mới.
 | Phạm vi tác nhân cập nhật | 
• App Client:
• Nâng cấp cơ chế sử dụng key default ở phiên bản ứng dụng mới, iOS từ phiên bản 1.3.2 và AND từ phiên bản  1.3.2 
• App Server:
• Bổ sung các logic check liên quan tới key default
• Quản lý cấu hình key default theo hệ điều hành, phiên bản ứng dụng
 | Phạm vi tính năng cập nhật | 
• Các tính năng có sử dụng MID Public khi chưa kích hoạt app
 | Luồng cơ bản | 
• KH thực hiện truy cập 1 tính năng khi chưa kích hoạt app
• Ứng dụng gửi thông tin request lên Server
• Server kiểm tra key default + hệ điều hành + phiên bản:
• Nếu key default ứng dụng gửi lên ko đúng: Trả thông báo lỗi yêu cầu KH cập nhật ứng dụng mới trên store.
• Nếu key default ứng dụng gửi lên đúng: Thực hiện tiếp nghiệp vụ hiện tại
 | Business rules | 
• Mỗi phiên bản dùng key default riêng 
• Sau khi kích hoạt thành công sẽ sử dụng key user cho các mid giao tiếp giữa client và server 

### 3/ Luồng sơ đồ

truequytrinh_check_defaut_keyfalseautotoptrue12061

### 4/ Luồng xử lý chi tiết

Lưu ý nghiệp vụ:

• Giả định phiên bản ứng dụng có sử dụng key default mới là x.y.z. Các trường hợp có thể xảy ra: | TH | Phiên bản đang sử dụng | Đã kích hoạt app? | Update phiên bản mới? | Phiên bản mới | Sử dụng key theo hiện trạng | Kết quả mong muốn
 | 1 | < x.y.z | Chưa | Không | -- | Key default cũ | KH kích hoạt app và sử dụng bình thường. Sau khi kích hoạt app sử dụng key như nghiệp vụ cũ (có thể sử dụng key default cũ hoặc key user ở từng bank)
 | 2 | < x.y.z | Đã | Không | -- | Key default cũ | 
KH sử dụng Key default cũ ở các MID ko phải Public sẽ không bảo mật. Server cần kiểm tra và trả thông báo lỗi yêu cầu cập nhật app mới. Sau khi cập nhật, App Client sẽ ở trạng thái kích hoạt app và sử dụng Key default mới. Sau khi kích hoạt xong, App Client phải sử dụng Key User.

(Một số bank gặp phải: Agribank, Oceanbank, VietinBank)

 | 3 | < x.y.z | Đã | Không | -- | Key User | KH sử dụng bình thường.
 | 4 | < x.y.z | Chưa | Có (cài đè) | x.y.z | Key default cũ | 
KH kích hoạt app và Server cần kiểm tra và trả thông báo yêu cầu cập nhật app mới. Sau khi cập nhật, App Client sẽ ở trạng thái Chưa kích hoạt và sử dụng Key default mới. Sau khi kích hoạt xong, App Client phải sử dụng Key User.

 | 5 | < x.y.z | Chưa | Có (gỡ app, cài trực tiếp) | x.y.z | Key default mới | KH kích hoạt app. Sau khi kích hoạt , App Client phải dùng Key User.
 | 6 | < x.y.z | Đã | Có (cài đè) | x.y.z | Key User | KH sử dụng bình thường. Sau khi kích hoạt, App Client phải dùng Key User.
 | 7 | < x.y.z | Đã | Có (gỡ app, cài trực tiếp) | x.y.z | Key default mới | KH kích hoạt app. Sau khi kích hoạt, App Client phải dùng Key User.
 | 8 | x.y.z | -- | -- | x.y.z+1 | Key default mới | App Client sử dụng Key default của phiên bản x.y.z+1

• Nếu KH chưa kích hoạt app: App Client dùng Key default trong các MID trước kích hoạt
• Nếu KH đã kích hoạt app: App Client dùng Key User trong tất cả các MID.
• Ngoài trường hợp 2, 4, 5 7 App Client phải sử dụng Key default mới, nếu trường hợp KH đã kích hoạt app sau đó đổi sang tài khoản khác thì App Client cũng phải sử dụng Key default mới | TT | Sự kiện | Tác nhân | Mô tả
 | 1 | 
App Client gửi request lên App Server đối với các MID Public:

• Mid 1 - Đăng nhập 
• Mid 2 - Kích hoạt tài khoản
• Mid 470 - Lấy danh sách white list accessibility
• Mid 204 - Cài đặt lưu pin soft
• Mid 393 - Lấy danh sách tin tức
• Mid 440 - Khởi tạo gen sms otp ekyc
• Mid 441 - Xác thực sms otp ekyc
• Mid 442 - Kiểm tra GTTT
• Mid 443 - Lấy danh sách quận huyện
• Mid 444 - Lấy danh sách phường xã
• Mid 8 - Gui lai otp
• Mid 6 - Đổi mật khẩu
• Mid 3 - Kich hoat lai tk tren thiet bi khac
• Mid 381- Lấy danh sách tỉnh thành
• Mid 382 - Lấy danh sách quận huyện
• MId 512 - Gửi SMS OTP theo usecase
• Mid 533 - Yêu cầu xác nhận chia sẻ thông tin sang VNEID
• Mid 534 - Tạo Nonce cho xác thực chia sẻ VNEID
• Mid 379 - Danh sách xã, phường theo thành phố
• Mid 448 - Kiểm tra mã đăng giới thiệu
• Mid 390 - Lấy danh sách chi nhánh phòng giao dịch
• Mid 391 - Khởi tạo quên mật khẩu màn login
• Mid 392 - Xác nhận quên mật khẩu màn login
• Mid 445 - Lấy danh sách ngành nghề kinh tế
• Mid 446 - Lấy danh sách quỹ tín dụng nhân dân
• Mid 447 - Đăng ký người dùng để chạy job
• Mid 510 - Kiểm tra thông tin số GTTT facepay
• Mid 530 - Lấy danh sách tài khoản voice ott | 
App Client
 | 
Gửi thông tin request lên App Server

 | 
App Server
 | 
1/ Kiểm tra request có sử dụng key default không?

• Nếu sử dụng key user: Thực hiện tiếp luồng nghiệp vụ hiện tại
• Nếu sử dụng key default: Chuyển 2
2/ Kiểm tra key default đang sử dụng:

• Nếu key default = 0000000001 và App Version < App Version ở phiên bản sử dụng key default mới: Thực hiện tiếp luồng nghiệp vụ hiện tại
• Nếu key default = 0000000001 và App Version >= App Version ở phiên bản sử dụng key default mới: Trả thông báo lỗi riêng để yêu cầu app client sử dụng key default mới và kích hoạt lại (trả mã lỗi 9991)
• Nếu key default khác 0000000001: Chuyển 3
3/ Kiểm tra key default client đang sử dụng có đúng key default theo phiên bản + hệ điều hành đã cấu hình ở App Server:

• Nếu không đúng: Trả thông báo lỗi yêu cầu update app (trả mã lỗi 526)
• Nếu đúng: Thực hiện tiếp theo nghiệp vụ hiện tại.
 | 
App Client
 | 
Nhận kết quả tương ứng theo các trường hợp phản hồi của App Server:

• Hợp lệ: Xử lý tiếp luồng nghiệp vụ hiện tại
• Không hợp lệ: | 
 | Trường hợp | Thông báo | Xử lý (nếu có)
 | 1 | 
key default = 0000000001 và App Version >= App Version ở phiên bản sử dụng key default mới (Trường hợp: KH update ứng dụng từ phiên bản cũ lên phiên bản mới theo hình thức cài đè)

→ Mã lỗi: 9991
 | Theo quy định chính sách bảo mật, Quý khách vui lòng thực hiện kích hoạt lại ứng dụng Co-opBank để tiếp tục sử dụng dịch vụ. | 
Tắt thông báo, ứng dụng client hiển thị màn hình kích hoạt app (client sử dụng key default mới)

 | 2 | 
IOS: MID Request không phải public và Key default khác 0000000001 và key default không đúng theo HĐH + App Version 

→ Mã lỗi: 526
 | Để sử dụng chức năng này, Quý khách vui lòng cập nhật phiên bản Ứng dụng mới nhất tại Appstore. | 
Hiển thị 2 button:

• Đóng: Tắt thông báo, hiển thị màn hình KH đang thao tác.
• Đồng ý: Tắt thông báo, refer đến địa chỉ tải app trên Appstore.
 | 3 | 
ANDROID: MID Request không phải public và Key default khác 0000000001 và key default không đúng theo HĐH + App Version

→ Mã lỗi: 526
 | Để sử dụng chức năng này, Quý khách vui lòng cập nhật phiên bản Ứng dụng mới nhất tại Google Play. | 
Hiển thị 2 button:

• Đóng: Tắt thông báo, hiển thị màn hình KH đang thao tác.
• Đồng ý: Tắt thông báo, refer đến địa chỉ tải app trên Google Play.
 | 4 | 
MID Request không phải public và key default khác 0000000001

→ 9990

(Dùng key default mới cho mid private)
 | Thông tin yêu cầu không hợp lệ.  | Tắt thông báo, hiển thị màn hình đang thao tác

### 5/ Bảng dữ liệu

#### 5.1/ Bảng quản lý key default
 | 
 | Tên trường | Mô tả | Giá trị thiết lập
 | 1 | ID | Số thứ tự | 
• Tăng dần
 | 2 | KEY_ID | Key ID default được cấu hình theo device_os và app_version tương ứng | 
• Gen theo tool
 | 3 | PRIVATE_KEY | Key giải mã/mã hóa của Server (serverPrivateKey) | 
• Gen theo tool
 | 4 | PUBLIC_KEY | Key giải mã/mã hóa của Client (clientPublicKey | 
• Gen theo tool
 | 5 | DEVICE_OS | Hệ điều hành thiết bị | 
Bao gồm 2 giá trị:

• AND
• IOS
 | 6 | APP_VERSION | Phiên bản ứng dụng cấu hình key default | Cấu hình theo quy tắc: x.y.z
 | 7 | STATUS | Trạng thái bản ghi | 

 | 8 | CREATE_TIME | Thời gian tạo bản ghi |

---


