# Shell #3: 🐚 PaymentShell — 1-tap biometric payment

### Component Structure

```
🐚 PaymentShell (data-slot="payment-shell")
├── 🔌 ActionArea (data-slot="payment-action-area")
│   📋 Accepts: M-09 OneTapPayBiometric
│   📝 Contains: Saved card display + biometric prompt + Apple/Google Pay quick option
│   📐 Layout: Centered card stack
└── 🔌 AddCardArea (data-slot="payment-add-card-area")
    📋 Accepts: M-10 AddNewCardFlow
    📝 Contains: Camera scan + manual entry + save toggle + billing address (PCI fields)
    📐 Layout: Vertical form
```

### Slot Fill Matrix

| Slot | SF1 (Booking) |
|---|---|
| ActionArea | M-09 ↔ OneTapPayBiometric :auth_method+:saved_card `(auto)` |
| AddCardArea | M-10 ?visible (when no saved card OR user adds) |

### Screen Layout

```
┌─────────────────────────────┐
│ Header: Thanh toán           │
├─────────────────────────────┤
│ [Visa **** 1234]             │ ← saved card
│ [👆 Face ID to pay]          │
├─────────────────────────────┤
│ — OR —                       │
│ [🍎 Apple Pay]                │
│ [G Google Pay]                │
├─────────────────────────────┤
│ [+ Thêm thẻ mới]              │
└─────────────────────────────┘
```
