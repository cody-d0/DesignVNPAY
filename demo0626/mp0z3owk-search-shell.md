# Shell #1: 🐚 SearchShell — Flight search inputs + flex pricing

### Component Structure

```
🐚 SearchShell (data-slot="search-shell")
├── 🔌 InputArea (data-slot="search-input-area")
│   📋 Accepts: M-01 OriginInputSmart · M-02 DestinationInput · M-03 PassengerCounter
│   📝 Contains: Origin (auto-detect GPS+recent) + Destination (typed/voice/promo) + Passenger counter (adult/child/infant)
│   📐 Layout: Vertical stack
└── 🔌 DateArea (data-slot="search-date-area")
    📋 Accepts: M-04 FlexPricingCalendar
    📝 Contains: Calendar with cheap-day heatmap + flexibility toggle (±3d / ±7d / monthly)
    📐 Layout: Calendar grid
```

### Slot Fill Matrix

| Slot | SF1 (Booking) |
|---|---|
| InputArea | M-01 ↔ OriginInputSmart `(auto)` · M-02 ↔ DestinationInput `(manual)` · M-03 ↔ PassengerCounter `(manual)` |
| DateArea | M-04 ↔ FlexPricingCalendar :pricing_view `(auto)` |

### Screen Layout

```
┌─────────────────────────────┐
│ Header: Tìm chuyến bay       │
├─────────────────────────────┤
│ Origin: SGN 📍 (auto)        │
│ Destination: HAN ▼            │
│ [🎤 voice option]             │
├─────────────────────────────┤
│ Calendar (flex heatmap)      │
│ Cheap days: green markers    │
├─────────────────────────────┤
│ Passengers: 2 NL + 1 trẻ     │
│ Class: Phổ thông ▼           │
├─────────────────────────────┤
│ [Tìm chuyến bay]             │ ← Primary CTA
└─────────────────────────────┘
```
