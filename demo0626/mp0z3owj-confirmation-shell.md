# Shell #4: 🐚 ConfirmationShell — Booking success + share + Wallet

### Component Structure

```
🐚 ConfirmationShell (data-slot="confirmation-shell")
├── 🔌 MainContent (data-slot="confirmation-main-content")
│   📋 Accepts: M-11 BookingConfirmationCard
│   📝 Contains: Success header + PNR + miles earned celebration + auto-Wallet status
│   📐 Layout: Hero card centered
└── 🔌 ShareArea (data-slot="confirmation-share-area")
    📋 Accepts: M-12 TripShareToFamily
    📝 Contains: Native share sheet (Zalo/WhatsApp/SMS/Email/Calendar)
    📐 Layout: Bottom modal
```

### Slot Fill Matrix

| Slot | SF1 (Booking) |
|---|---|
| MainContent | M-11 ↔ BookingConfirmationCard :tier_celebration+:post_action `(auto)` |
| ShareArea | M-12 ↔ TripShareToFamily :share_channel `(manual)` |

### Screen Layout

```
┌─────────────────────────────┐
│ ✅ Đã đặt VN225 HAN→SGN      │
│    ngày 15/06/2026            │
│                               │
│ Mã đặt chỗ: ABC123            │
│                               │
│ ✨ +1,000 miles tích lũy      │
│ ✈️ Đã thêm vào Wallet         │
├─────────────────────────────┤
│ [Chia sẻ với gia đình]        │
│   • Zalo (default)            │
│   • WhatsApp / SMS / Email    │
├─────────────────────────────┤
│ [Thêm vào lịch]               │
│ [Xem chuyến bay]              │
└─────────────────────────────┘
```
