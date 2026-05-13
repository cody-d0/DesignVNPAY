# Shell #2: 🐚 BookingShell — 4-step booking flow

### Component Structure

```
🐚 BookingShell (data-slot="booking-shell")
├── 🔌 ResultsList (data-slot="booking-results-list")
│   📋 Accepts: M-05 FlightOptionCard
│   📝 Contains: Flight option cards with timeline + fare class + tier discount + amenities
│   📐 Layout: Vertical scrollable list
├── 🔌 AddOnsArea (data-slot="booking-addons-area")
│   📋 Accepts: M-07 SeatPicker · M-08 MealSelector
│   📝 Contains: Seat picker (tier-aware) + Meal selector (dietary categories)
│   📐 Layout: Tabbed step interface
└── 🔌 PriceArea (data-slot="booking-price-area")
    📋 Accepts: M-06 TotalPriceUpfront
    📝 Contains: Base + taxes + ancillaries breakdown + miles preview + tier discount
    📐 Layout: Sticky bottom card
```

### Slot Fill Matrix

| Slot | SF1 (Booking) |
|---|---|
| ResultsList | M-05 ×N FlightOptionCard :fare_class+:tier_aware_pricing `(auto)` |
| AddOnsArea | M-07 ↔ SeatPicker :tier+:availability `(auto)` · M-08 ↔ MealSelector :category `(manual)` |
| PriceArea | M-06 ↔ TotalPriceUpfront :fees_breakdown `(auto)` ?voucher_applied |

### Screen Layout

```
┌─────────────────────────────┐
│ Step 1: Chọn ghế             │
│ [Aircraft seat map]          │
│ Gold+ premium FREE 💎        │
├─────────────────────────────┤
│ Step 2: Bữa ăn               │
│ [Meal categories]            │
├─────────────────────────────┤
│ Step 3: Hành lý              │
│ [+] Thêm vali                │
├─────────────────────────────┤
│ Step 4: Tổng kết             │
│ Base: 2,500K                 │
│ Taxes: 350K                  │
│ Bag: 200K                    │
│ ────────────                 │
│ Tổng: 3,050,000đ             │
│ ✨ +1,000 miles tích lũy     │
└─────────────────────────────┘
│ [Tiếp tục thanh toán]        │ ← sticky bottom
```
