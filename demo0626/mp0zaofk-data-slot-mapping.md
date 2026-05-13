# 🔗 Data-Slot Mapping — BOOKING (Vietnam Airlines)

## Shell-Level

| Shell | data-slot | Semantic Role |
|---|---|---|
| 🐚 SearchShell | `data-slot="search-shell"` | screen |
| 🐚 BookingShell | `data-slot="booking-shell"` | screen |
| 🐚 PaymentShell | `data-slot="payment-shell"` | screen |
| 🐚 ConfirmationShell | `data-slot="confirmation-shell"` | screen |

## Slot-Level

| Shell | Slot | data-slot | Role |
|---|---|---|---|
| SearchShell | InputArea | `data-slot="search-input-area"` | container |
| SearchShell | DateArea | `data-slot="search-date-area"` | container |
| BookingShell | ResultsList | `data-slot="booking-results-list"` | container |
| BookingShell | AddOnsArea | `data-slot="booking-addons-area"` | container |
| BookingShell | PriceArea | `data-slot="booking-price-area"` | container |
| PaymentShell | ActionArea | `data-slot="payment-action-area"` | action |
| PaymentShell | AddCardArea | `data-slot="payment-add-card-area"` | input |
| ConfirmationShell | MainContent | `data-slot="confirmation-main-content"` | container |
| ConfirmationShell | ShareArea | `data-slot="confirmation-share-area"` | overlay |

## Molecule-Level

| Molecule | data-slot | Role |
|---|---|---|
| M-01 OriginInputSmart | `data-slot="origin-input"` | input |
| M-02 DestinationInput | `data-slot="destination-input"` | input |
| M-03 PassengerCounter | `data-slot="passenger-counter"` | input |
| M-04 FlexPricingCalendar | `data-slot="flex-pricing-calendar"` | display |
| M-05 FlightOptionCard | `data-slot="flight-option-card"` | display |
| M-06 TotalPriceUpfront | `data-slot="total-price"` | display |
| M-07 SeatPicker | `data-slot="seat-picker"` | input |
| M-08 MealSelector | `data-slot="meal-selector"` | input |
| M-09 OneTapPayBiometric | `data-slot="one-tap-pay"` | action |
| M-10 AddNewCardFlow | `data-slot="add-card-flow"` | input |
| M-11 BookingConfirmationCard | `data-slot="booking-confirmation"` | display |
| M-12 TripShareToFamily | `data-slot="trip-share"` | overlay |

## Sub-Slot (max 2-level)

| Parent | Sub-element | data-slot |
|---|---|---|
| M-01 | GPSLocationBadge | `data-slot="origin-input-gps"` |
| M-04 | CheapDayHighlight | `data-slot="flex-pricing-calendar-cheap"` |
| M-09 | BiometricPrompt | `data-slot="one-tap-pay-biometric"` |
| M-09 | ApplePayGooglePayButton | `data-slot="one-tap-pay-applepay"` |

## Validation: 25 nodes mapped (4 shell + 9 slot + 12 molecule) — kebab-case + max 2-level ✅
