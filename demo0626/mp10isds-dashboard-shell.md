# Shell #1: 🐚 DashboardShell — Home Dashboard composite 6-zone

> **Note:** Cross-app persistent — Zone A (HeaderInfo) embeds tier badge across all major screens; Zone F (VoiceAINav) bottom nav persists across ALL screens.

---

### Component Structure

```
🐚 DashboardShell (data-slot="dashboard-shell")
│
├── 🔌 HeaderInfo (data-slot="dashboard-header-info") — Zone A · sticky-top
│   │  📋 Accepts: M-01 TierBadgePersistent · M-02 GreetingHeader · M-03 WeatherMiniCard · M-04 FlightMiniCard · M-05 QuickActionCTA
│   │  📝 Contains: Tier identity + greeting + weather + active flight mini-card + 2 context-aware CTAs (always visible top of viewport)
│   │  📐 Layout: Vertical stack, full-width, sticky on scroll, max-height 280dp
│
├── 🔌 DCZ (data-slot="dashboard-dcz") — Zone B · scrollable
│   │  📋 Accepts: M-06 DCZCurrentTripCard · M-07 DCZContextActionPills · M-08 PredictiveRecommendation · M-09 CrossSaleModule
│   │  📝 Contains: Active trip overview WITH context actions OR predictive AI suggestions (mode toggle by trip_active state)
│   │  📐 Layout: Vertical stack, gap 16dp, padding 16dp horizontal
│
├── 🔌 RecentSearches (data-slot="dashboard-recent-searches") — Zone C · scrollable
│   │  📋 Accepts: M-10 RecentSearchChip
│   │  📝 Contains: Quick rebook chips for recent OR popular routes (cache + cloud sync)
│   │  📐 Layout: Horizontal scrollable chip row, 3-5 visible
│
├── 🔌 SmartSuggestions (data-slot="dashboard-smart-suggestions") — Zone D · scrollable
│   │  📋 Accepts: M-11 PromoBanner · M-12 LocalDiscoveryCard
│   │  📝 Contains: Tier-aware promos + cultural moment campaigns + post-arrival local discovery
│   │  📐 Layout: Vertical stack, card-based, gap 12dp
│
├── 🔌 LoyaltySnapshot (data-slot="dashboard-loyalty-snapshot") — Zone E · scrollable
│   │  📋 Accepts: M-13 MilesSnapshotCard · M-14 RewardOfferCard · M-15 TierLevelupPrompt · M-16 MillionMilerTribute
│   │  📝 Contains: Miles balance + tier ladder progress + reward offers + recovery warning + MM tribute (only D1=MillionMiler)
│   │  📐 Layout: Vertical stack, card group with subtle shadow, padding 16dp
│
└── 🔌 VoiceAINav (data-slot="dashboard-voice-ai-nav") — Zone F · sticky-bottom · CROSS-APP
    │  📋 Accepts: M-17 VoiceMicCenterNav · M-18 AISuggestionToast
    │  📝 Contains: Bottom navigation tab bar with center voice mic (oversize 56dp) + floating AI suggestion toast
    │  📐 Layout: Sticky bottom, full-width 60dp height + floating toast layer above

🔒 Footer: FooterTabBar (data-slot="dashboard-footer-tabbar")
   Pattern: Dashboard (vs PrimaryButton for Transaction Flow)
```

### Slot Fill Matrix

| Slot | SF0 (HOME) |
|---|---|
| HeaderInfo | M-01 ↔ TierBadgePersistent :tier=`(auto)` · M-02 ↔ GreetingHeader :tier+:cultural+:lang `(auto)` · M-03 ↔ WeatherMiniCard :weather `(auto)` · M-04 ?visible (when trip_active=true) · M-05 ↔ QuickActionCTA :tier+:phase `(auto)` |
| DCZ | M-06 ?visible (when trip_active=true) · M-07 ↔ DCZContextActionPills :tier `(auto)` · M-08 ↔ PredictiveRecommendation ?visible (when ML triggered + within frequency cap) · M-09 ↔ CrossSaleModule :trigger `(auto)` |
| RecentSearches | M-10 ×N (max 5) data="recent" `(auto)` |
| SmartSuggestions | M-11 ↔ PromoBanner :tier+:promo_type `(auto)` · M-12 ?visible (post-arrival mode) |
| LoyaltySnapshot | M-13 ↔ MilesSnapshotCard :tier+:auth+:recovery `(auto)` · M-14 ↔ RewardOfferCard :eligibility `(auto)` · M-15 ?visible (when within 5 segments/miles upgrade) · M-16 ?visible (only when D1=MillionMiler) |
| VoiceAINav | M-17 ↔ VoiceMicCenterNav :mic_state `(auto)` · M-18 ?visible (when AI ML triggered, dismissable) |

### Screen Layout (vertical scroll)

```
┌─────────────────────────────────────────┐ ← sticky top
│  Zone A: HeaderInfo                      │
│  • TierBadge "🪁 Titanium · 12,450 miles"│
│  • Greeting "Chào anh Tuấn 🪁"           │
│  • Weather "SGN 28°C ☀️"                  │
│  • [✈️ VN225 SGN→HAN · 2h45m · Gate D2]  │ ← FlightMiniCard (when trip_active)
│  • [Check-in] [Add bag]                   │ ← QuickActionCTA
├─────────────────────────────────────────┤ ← scrollable
│  Zone B: DCZ                              │
│  • Current trip detail OR predictive      │
│  • Context action pills (WiFi/Bag/Lounge)│
│  • "Bạn thường mua Wi-Fi — thêm 80MB?"   │
│  • Hotel near destination cross-sale      │
├─────────────────────────────────────────┤
│  Zone C: Recent Searches                  │
│  [HAN ↔ SGN] [HAN ↔ DAD] [SGN ↔ PQC]    │
├─────────────────────────────────────────┤
│  Zone D: Smart Suggestions                │
│  • Promo banner (tier-aware)             │
│  • Local discovery (post-arrival mode)   │
├─────────────────────────────────────────┤
│  Zone E: Loyalty                          │
│  • Miles snapshot "12,450 / Titanium"    │
│  • To Gold gauge "Còn 18,000 miles"      │
│  • Reward offer "500 miles → Wi-Fi"      │
│  • [Tier recovery warning if 90/60/30d]  │
│  • [MillionMiler tribute if MM tier]     │
├─────────────────────────────────────────┤ ← sticky bottom · CROSS-APP
│  Zone F: VoiceAINav                       │
│  [Home] [Trips] [🎤56dp] [Tools] [Profile]│
│  [Floating: "Check-in ngay?" toast]       │
└─────────────────────────────────────────┘
```

### 🔒 Navigation

- Zone A.QuickActionCTA → routes to Booking flow (Search), Check-in flow, Trip Detail (depending on context)
- Zone B.DCZCurrentTripCard tap → Trip Detail screen
- Zone E.MilesSnapshotCard tap → Lotusmiles full screen
- Zone F.VoiceMicCenterNav → activates voice listening overlay (in-place, no navigation)
- Zone F.AISuggestionToast accept → routes per intent (e.g., Check-in flow)

### State Dimensions Effect on Slot Fills

| Dimension | Affected Molecules |
|---|---|
| D1 tier | M-01, M-02, M-05, M-07, M-11, M-13, M-14, M-15, M-16, M-17 |
| D2 trip_active | M-04 (visibility), M-06 (mode), M-07 (visibility), M-09 (cross-sale trigger) |
| D3 trip_phase | M-04 status pill, M-05 CTA logic, M-06 timeline |
| D4 cultural_theme | M-02 greeting suffix, M-11 promo theme |
| D5 language | All copy molecules (M-02, M-08, M-09, M-11, M-12, M-13, M-15, M-17, M-18) |
| D6 tier_recovery_state | M-13 warning visibility |
| D7 weather_state | M-03 icon + delay risk, M-09 advisory |
| D8 voice_state | M-17 mic animation, M-18 visibility |
