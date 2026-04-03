window.__MOLECULE_DATA__ = {
  "meta": {
    "domain_name": "TRANSFER — Chuyển tiền",
    "domain_id": "transfer",
    "version": "v2.1",
    "date": "2026-04-02",
    "shell_count": 5,
    "total_molecules": 45,
    "described_count": 45,
    "total_states": 116,
    "complex_count": 22,
    "complex_ids": "M-01, M-03, M-04, M-05, M-07, M-08, M-10, M-15, M-20, M-21, M-22, M-23, M-30, M-32, M-33, M-34, M-35, M-36, M-38, M-39, M-43, M-45",
    "cross_domain_count": 3,
    "cross_domain_ids": "M-32, M-33, M-34"
  },
  "molecules": [
    {
      "id": "M-01",
      "name": "AccountSelector",
      "shell": "InitShell",
      "slot": "SourceAccount",
      "category": "🔁 SHARED (75% SFs)",
      "phase": 1,
      "states": 6,
      "pattern": "Shared combobox",
      "data_slot": "account-selector",
      "sub_slots": [
        "account-selector-trigger",
        "account-selector-content",
        "account-selector-item"
      ],
      "mockup": "mockups/m01_accountselector.png",
      "context": {
        "problem": "Người dùng Co-opBank thường sở hữu 2-5 tài khoản (thanh toán, tiết kiệm, thẻ) nhưng giao diện hiện tại không phân biệt rõ loại tài khoản và số dư khả dụng, dẫn đến chọn nhầm nguồn tiền.",
        "trigger": "Audit 28 modules — 64% thiếu clear account identification (EXECUTIVE-SUMMARY §2)",
        "problem_space": "User phải nhớ số TK 13 chữ số để xác định đúng tài khoản — cognitive load cao, đặc biệt với persona Bà Hoa (60+, thị giác yếu)",
        "origin": "Competitive analysis — Toss/VCB hiện account card với badge loại TK + số dư real-time (gap 2.9 điểm). Internal audit — 6/8 SFs cần chọn TK nguồn",
        "predecessor": "Không có — molecule nền tảng (foundation)"
      },
      "intent": {
        "quote": "Molecule này giúp người dùng mọi lứa tuổi chọn đúng tài khoản nguồn trong ≤2 taps khi bắt đầu bất kỳ giao dịch chuyển tiền nào.",
        "primary_goal": "Giảm lỗi chọn nhầm TK nguồn xuống 0% thông qua visual differentiation",
        "personas": "Bà Hoa (60+, cần badge lớn + số dư rõ) · Anh Tuấn (35-45, cần nhanh + chính xác)",
        "context_of_use": "Entry point mọi SF — xuất hiện đầu tiên trên InitShell",
        "principles": "#2 3-Tap Rule (chọn TK ≤ 2 taps) · #1 Trust First (số dư real-time tăng tin cậy)",
        "value_pyramid": "Level 2 (Usability) — giảm friction cốt lõi"
      },
      "insight": {
        "title": "Badge-First Recognition",
        "description": "Người dùng không nhớ số TK — họ nhớ loại tài khoản (\"cái TK lương\", \"cái thẻ Visa\"). Badge màu (TT/TK/Thẻ) kích hoạt pattern recognition nhanh hơn 3× so với đọc số.",
        "core_pattern": "Account Card Pattern (Toss, Revolut) — compact card thay thế dropdown text-only",
        "behavioral": "Recognition over Recall (Nielsen) — badge visual cho phép scan 2-5 TK trong <1s",
        "differentiation": "App thông thường dùng dropdown text \"092xxxx - Thanh toán\". Molecule này dùng card với color-coded badge + số dư formatted, cho phép quyết định chọn TK dựa trên context (số dư đủ không?)",
        "state_machine": "3 selectionState × 3 accountType = 9 combinations, pruned → 6 canonical"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "75% SFs (6/8) cần chọn TK nguồn — molecule reuse cao nhất",
          "source": "molecules.md Group A"
        },
        {
          "type": "📊",
          "claim": "Competitive gap 2.9/5 — 0/10 đối thủ dùng text-only dropdown cho account selection",
          "source": "EXECUTIVE-SUMMARY §3"
        },
        {
          "type": "🏦",
          "claim": "Toss Bank: account card + real-time balance → task success 95%+",
          "source": "Competitive analysis"
        }
      ],
      "sim_notes": [
        "API: Fetch account list + real-time balance on mount",
        "PII: Account number partial masking (hiện 4 số cuối) — toggle reveal",
        "A11Y: Badge cần triple encoding (color + text + icon) per LV-08",
        "State: Combobox popup cần scroll cho >5 accounts"
      ]
    },
    {
      "id": "M-02",
      "name": "SourceAccountBlock",
      "shell": "InitShell",
      "slot": "SourceAccount",
      "category": "⭐ SF8 only",
      "phase": 1,
      "states": 2,
      "pattern": "Block wrapper",
      "data_slot": "source-account-block",
      "sub_slots": [
        "reuse M-01 internal slots"
      ],
      "mockup": "mockups/m02_sourceaccountblock.png",
      "context": {
        "problem": "SF8 (Chuyển tiền định kỳ) cần visual hierarchy khác biệt so với các SF khác — M-01 đơn lẻ không đủ context để user nhận biết đây là flow đặt lịch.",
        "trigger": "SF8 analysis — schedule flow cần block-based layout consistency",
        "problem_space": "Without explicit block wrapper, user không phân biệt SF8 form sections với SF thường",
        "origin": "Shell architecture — ScheduleListShell cần visual parity với InitShell sections",
        "predecessor": "M-01 AccountSelector (reuse nguyên vẹn bên trong)"
      },
      "intent": {
        "quote": "Molecule này giúp người dùng đặt lịch nhận diện section \"Tài khoản nguồn\" trong context schedule khi thiết lập chuyển tiền định kỳ SF8.",
        "primary_goal": "Visual consistency cho SF8 block-based layout",
        "personas": "Anh Tuấn (35-45, dùng schedule cho lương) · Chị Mai (30-40, batch recurring)",
        "context_of_use": "SF8 InitShell — thay thế M-01 standalone",
        "principles": "#3 Clarity Over Features (section headers rõ ràng)",
        "value_pyramid": "Level 2 (Usability) — structural clarity"
      },
      "insight": {
        "title": "Block Framing Effect",
        "description": "Khi form dài (schedule có nhiều fields hơn SF thường), chia thành blocks có header giúp giảm perceived complexity 40%. User scan header → skip block nếu đã fill → focus block cần điền.",
        "core_pattern": "Section Block (Material Design) — header + content + divider",
        "behavioral": "Chunking (Miller) — chia form 15+ fields thành 4-5 blocks giảm cognitive load",
        "differentiation": "Chỉ wrap thêm header + divider, KHÔNG duplicate M-01. Zero code duplication",
        "state_machine": "2 blockStyle (default, highlighted khi schedule hint active)"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "SF8 form có 15+ fields — vượt cognitive load limit ELD-08 (68% fail)",
          "source": "SCROLL-BUDGET.md §3"
        },
        {
          "type": "📐",
          "claim": "Miller (1956) — chunking giảm cognitive load 40-60% cho forms >10 fields",
          "source": "Cognitive Psychology"
        }
      ],
      "sim_notes": [
        "Compose: Wrap M-01, không render logic riêng",
        "highlighted state: border glow khi schedule panel active",
        "A11Y: BlockHeader phải là heading level (h3)"
      ]
    },
    {
      "id": "M-03",
      "name": "CardReceiverSection",
      "shell": "InitShell",
      "slot": "DestinationFields",
      "category": "⭐ SF2 only",
      "phase": 1,
      "states": 6,
      "pattern": "Napas query",
      "data_slot": "card-receiver",
      "sub_slots": [
        "card-receiver-input",
        "card-receiver-name",
        "card-receiver-save"
      ],
      "mockup": "mockups/m03_cardreceiversection.png",
      "context": {
        "problem": "Chuyển tiền qua số thẻ (SF2) yêu cầu query Napas để xác minh — nhưng hiện tại không có loading indicator khi query, user không biết app đang xử lý hay bị đơ.",
        "trigger": "Systemic Issue #3 — 57% modules thiếu loading states (EXECUTIVE-SUMMARY §2)",
        "problem_space": "User nhập 16 số thẻ → chờ 2-5s Napas response → không có feedback → tap submit → \"Lỗi hệ thống\"",
        "origin": "App review \"ứng dụng bị đơ\" (22% phàn nàn). Napas API latency 1-5s documented",
        "predecessor": "Không có"
      },
      "intent": {
        "quote": "Molecule này giúp người chuyển tiền qua thẻ xác minh người nhận đúng trước khi gửi khi nhập số thẻ ATM/Visa/Mastercard trong SF2.",
        "primary_goal": "Auto-fill tên người nhận từ Napas → user confirm visual trước khi tiếp tục",
        "personas": "Anh Tuấn (35-45, chuyển tiền hàng ngày) · Minh (25-30, expect instant feedback)",
        "context_of_use": "SF2 DestinationFields — exclusive molecule",
        "principles": "#4 State Completeness (loading + error + success) · #1 Trust First (auto-verify receiver)",
        "value_pyramid": "Level 1 (Functional) → Level 2 (Usability) — core transaction safety"
      },
      "insight": {
        "title": "Verification-Before-Commit",
        "description": "Hiện tên người nhận auto-filled TRƯỚC khi user confirm giúp giảm chuyển nhầm người 80%+. Pattern này là mandatory cho regulatory compliance (SBV circular) nhưng UX execution quyết định trust perception.",
        "core_pattern": "Inline Verification (Toss, VCB) — query → display result → confirm",
        "behavioral": "Confirmation Bias mitigation — showing name forces user to mentally verify \"đúng người này không?\"",
        "differentiation": "App thường chỉ validate format số thẻ. Molecule này query Napas real-time + hiện tên",
        "state_machine": "4 cardState × 2 saveContact = 8, pruned → 6 canonical"
      },
      "evidence": [
        {
          "type": "📊",
          "claim": "22% app reviews phàn nàn \"app bị đơ\" — thiếu loading state",
          "source": "EXECUTIVE-SUMMARY §4"
        },
        {
          "type": "🔍",
          "claim": "20/28 modules thiếu error states — systemic issue #2",
          "source": "EXECUTIVE-SUMMARY §2"
        },
        {
          "type": "🏦",
          "claim": "Toss Bank: inline name verification → chuyển nhầm giảm 85%",
          "source": "Competitive analysis"
        }
      ],
      "sim_notes": [
        "API: Napas card lookup (1-5s latency) — cần timeout 10s + retry",
        "Save contact: conditional field, nickname persists across sessions",
        "PII: Card number masked after query (hiện 4 số cuối)"
      ]
    },
    {
      "id": "M-04",
      "name": "AccountReceiverSection",
      "shell": "InitShell",
      "slot": "DestinationFields",
      "category": "⭐ SF3 only",
      "phase": 1,
      "states": 10,
      "pattern": "Bank selector",
      "data_slot": "account-receiver",
      "sub_slots": [
        "account-receiver-input",
        "account-receiver-bank-trigger",
        "account-receiver-bank-content",
        "account-receiver-name"
      ],
      "mockup": "mockups/m04_accountreceiversection.png",
      "context": {
        "problem": "Chuyển tiền liên ngân hàng (SF3) cần chọn NH thụ hưởng từ 40+ ngân hàng — giao diện hiện tại dùng dropdown dài không search, user phải scroll tìm.",
        "trigger": "Competitive gap — VCB/Toss có smart bank search với logo + tên viết tắt",
        "problem_space": "40+ NH trong 1 dropdown → scroll 8-10 lần. Persona Bà Hoa bỏ cuộc ở bước này",
        "origin": "UX audit score thấp nhất ở bank selection. Journey map — Transfer flow 6 taps (target: 3)",
        "predecessor": "Không có"
      },
      "intent": {
        "quote": "Molecule này giúp người chuyển liên ngân hàng tìm và chọn ngân hàng thụ hưởng trong ≤3 giây khi nhập thông tin người nhận SF3.",
        "primary_goal": "Giảm thời gian chọn NH từ 15s (scroll) xuống 3s (search + logo recognition)",
        "personas": "Chị Mai (30-40, chuyển nhiều NH khác nhau) · Bà Hoa (60+, chỉ biết tên NH)",
        "context_of_use": "SF3 DestinationFields — after SourceAccount selected",
        "principles": "#2 3-Tap Rule · #3 Clarity Over Features (logo > text)",
        "value_pyramid": "Level 2 (Usability) — search + visual recognition"
      },
      "insight": {
        "title": "Logo-First Bank Recognition",
        "description": "User không nhớ tên chính thức (\"Ngân hàng TMCP Ngoại thương Việt Nam\") — họ nhận dạng bằng LOGO. BankSelector với logo + abbreviated name giảm selection time 5×.",
        "core_pattern": "Searchable Listbox + Logo (VCB, MoMo)",
        "behavioral": "Picture Superiority Effect — logo recognition 65% after 3 days vs 10% text-only",
        "differentiation": "Thêm KeyboardToggle 🔢↔🔤 cho user nhập STK số hoặc STK chữ+số",
        "state_machine": "4 queryState × 2 bankSelected × 2 keyboardMode × 2 saveContact = 32 → pruned 8 canonical"
      },
      "evidence": [
        {
          "type": "📊",
          "claim": "Transfer flow hiện tại 6 bước vs target 3 bước",
          "source": "EXECUTIVE-SUMMARY §8"
        },
        {
          "type": "🏦",
          "claim": "VCB: bank search with logo → selection time 3s avg",
          "source": "Competitive analysis"
        },
        {
          "type": "🔍",
          "claim": "STATE-PRUNING.md §2.4: 32 → 8 canonical states",
          "source": "insight-validation/"
        }
      ],
      "sim_notes": [
        "API: Bank list cached locally, NH lookup via Napas/CITAD",
        "Keyboard toggle: persist preference per session",
        "Empty state: \"Không tìm thấy ngân hàng\" + gợi ý kiểm tra tên"
      ]
    },
    {
      "id": "M-05",
      "name": "GTTTReceiverSection",
      "shell": "InitShell",
      "slot": "DestinationFields",
      "category": "⭐ SF4 only",
      "phase": 1,
      "states": 10,
      "pattern": "Instance Swap",
      "data_slot": "gttt-receiver",
      "sub_slots": [
        "gttt-receiver-type-trigger",
        "gttt-receiver-noicap",
        "gttt-receiver-name",
        "gttt-receiver-phone"
      ],
      "mockup": "mockups/m05_gtttreceiversection.png",
      "context": {
        "problem": "Chuyển tiền giấy tờ tùy thân (SF4) có 5 loại GTTT, mỗi loại drive layout khác nhau cho trường \"Nơi cấp\" — hiện tại dùng 1 textbox chung cho tất cả, gây nhập sai dữ liệu.",
        "trigger": "URD §16.4 — 5 GtttType với NoiCapField khác nhau (ENTITY-REGISTRY.md)",
        "problem_space": "CCCD đã có nơi cấp từ eKYC (auto-fill) nhưng UI vẫn cho sửa → data inconsistency. HC cần chọn quốc gia nhưng UI dùng textbox → typo",
        "origin": "URD corpus mining — 68 entities, 17 missing, GtttType mapping là critical gap",
        "predecessor": "Không có"
      },
      "intent": {
        "quote": "Molecule này giúp người gửi tiền GTTT nhập đúng thông tin giấy tờ người nhận không có TK khi thực hiện chuyển tiền SF4.",
        "primary_goal": "Đảm bảo data accuracy 100% cho NoiCapField qua Instance Swap pattern",
        "personas": "Anh Tuấn (35-45, gửi tiền cho người thân ở quê) · Chị Mai (30-40, gửi GTTT cho đối tác)",
        "context_of_use": "SF4 exclusive — phức tạp nhất trong DestinationFields",
        "principles": "#1 Trust First (eKYC pre-fill tăng accuracy) · #4 State Completeness",
        "value_pyramid": "Level 1 (Functional) — regulatory mandatory data capture"
      },
      "insight": {
        "title": "Instance Swap Pattern",
        "description": "Thay vì 1 textbox chung bị fill sai, mỗi GtttType SWAP hoàn toàn component con (NoiCapField): CMND→Textbox, HC→Combobox quốc gia, CCCD→Disabled pre-fill, GKS→Hidden. Pattern này impossible to fill wrong vì UI constraint = business constraint.",
        "core_pattern": "Instance Swap (Figma native) — component slot thay đổi theo variant",
        "behavioral": "Poka-Yoke (error-proofing) — UI constraint prevents wrong input instead of validating after",
        "differentiation": "App khác validation sau submit. Molecule này prevent wrong input at source",
        "state_machine": "5 gtttType × 2 saveContact = 10 (noiCapMode 1:1 với gtttType → pruned per STATE-PRUNING.md §2.3)"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "STATE-PRUNING.md §2.3: 40 → 10 canonical, noiCapMode derived",
          "source": "insight-validation/"
        },
        {
          "type": "🔍",
          "claim": "ENTITY-REGISTRY.md: 5 GtttType entities mapped, NoiCapField = critical gap",
          "source": "insight-validation/"
        },
        {
          "type": "📐",
          "claim": "Poka-Yoke (Shingo, 1986) — error-proofing qua constraint thay vì detection",
          "source": "Industrial Design"
        }
      ],
      "sim_notes": [
        "eKYC: CCCD auto-fill from national ID database — disabled field",
        "Instance Swap: Figma uses component property swap, code uses conditional render",
        "ReceiverName: manual input (khác SF2/SF3 auto-query) — no API dependency",
        "Phone: optional field, validate VN format 10 digits"
      ]
    },
    {
      "id": "M-06",
      "name": "SameOwnerDestSection",
      "shell": "InitShell",
      "slot": "DestinationFields",
      "category": "⭐ SF5 only",
      "phase": 1,
      "states": 2,
      "pattern": "Auto-filter",
      "data_slot": "same-owner-dest",
      "sub_slots": [
        "same-owner-dest-trigger",
        "same-owner-dest-content"
      ],
      "mockup": "mockups/m06_phonereceiversection.png",
      "context": {
        "problem": "Chuyển tiền cùng chủ (SF5) cần chọn TK đích từ danh sách TK của chính user — nhưng phải auto-exclude TK nguồn để tránh chuyển cho chính nó.",
        "trigger": "SF5 analysis — simplest destination flow nhưng cần smart filtering",
        "problem_space": "Nếu hiện TK nguồn trong danh sách đích → user chọn → lỗi \"Không thể chuyển cùng TK\"",
        "origin": "URD §16.5 — auto-exclude rule mandatory",
        "predecessor": "M-01 AccountSelector (reuse visual pattern, different data source)"
      },
      "intent": {
        "quote": "Molecule này giúp chủ tài khoản chọn TK đích trong danh sách TK cá nhân đã lọc khi chuyển tiền nội bộ cùng chủ SF5.",
        "primary_goal": "Zero-error account selection qua auto-exclude filter",
        "personas": "Anh Tuấn (35-45, chuyển giữa TK lương↔tiết kiệm)",
        "context_of_use": "SF5 after SourceAccount selected — dynamic filter applies",
        "principles": "#2 3-Tap Rule (1 tap select) · #1 Trust First",
        "value_pyramid": "Level 2 (Usability) — impossible to select wrong"
      },
      "insight": {
        "title": "Constraint-Driven Simplicity",
        "description": "Molecule đơn giản nhất (2 states) nhưng value cao nhất per-state — auto-exclude biến lỗi logic thành impossible state. Không cần validation message vì wrong option không tồn tại.",
        "core_pattern": "Filtered Selector — exclude source from options",
        "behavioral": "Choice Architecture (Thaler) — remove wrong options > warn about wrong options",
        "differentiation": "No SaveContact (chuyển cho chính mình) — UI simpler than SF2-4",
        "state_machine": "2 selectionState (empty, selected) — minimal"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "SF5 score cao nhất trong audit — 83/100",
          "source": "EXECUTIVE-SUMMARY §2"
        },
        {
          "type": "📐",
          "claim": "Thaler & Sunstein (2008) — Choice Architecture: restrict options > educate",
          "source": "Nudge Theory"
        }
      ],
      "sim_notes": [
        "Filter: exclude M-01 selected account from list, real-time update",
        "No SaveContact, no ReceiverName query — simplest DestinationFields molecule",
        "Min 2 accounts required — otherwise show empty state M-33"
      ]
    },
    {
      "id": "M-07",
      "name": "MultiRecipientSection",
      "shell": "InitShell",
      "slot": "DestinationFields",
      "category": "⭐ SF6 only",
      "phase": 2,
      "states": 16,
      "pattern": "Per-person state",
      "data_slot": "multi-recipient",
      "sub_slots": [
        "multi-recipient-avatar-list",
        "multi-recipient-input",
        "multi-recipient-name"
      ],
      "mockup": "mockups/m07_charityreceiversection.png",
      "context": {
        "problem": "Chuyển tiền đa người nhận (SF6) quản lý state per-person — mỗi người có inputType, queryState, saveToggle riêng. Giao diện hiện tại không có avatar list để navigate giữa các người nhận.",
        "trigger": "INTERACTION-MAP.md — SF6 critical flow chain, state explosion risk",
        "problem_space": "User nhập thông tin 3-5 người nhận nhưng không có overview → quên người nào đã điền, người nào chưa",
        "origin": "URD §16.6 — multi-recipient support mandatory. Toss/Grab có avatar-based navigation",
        "predecessor": "Không có — pattern mới cho Co-opBank"
      },
      "intent": {
        "quote": "Molecule này giúp người chuyển tiền cho nhiều người quản lý và track tiến độ nhập liệu per-person khi thực hiện SF6 chuyển tiền đa người nhận.",
        "primary_goal": "Clear per-person progress tracking qua RecipientAvatarList",
        "personas": "Chị Mai (30-40, chia tiền nhóm kinh doanh) · Minh (25-30, chia tiền bạn bè)",
        "context_of_use": "SF6 DestinationFields — 2+ recipients",
        "principles": "#4 State Completeness (per-person states) · #3 Clarity",
        "value_pyramid": "Level 2 (Usability) — multi-person UX"
      },
      "insight": {
        "title": "Avatar-as-Progress",
        "description": "AvatarList không chỉ navigate — nó ENCODE trạng thái mỗi người (default=chưa điền, selected=đang điền, error=có lỗi). User scan 1 hàng avatar = biết ngay ai cần attention. Pattern này biến N-person form thành visual dashboard.",
        "core_pattern": "Avatar Navigation + State Badge (Slack, Figma multiplayer)",
        "behavioral": "Status-at-a-Glance — peripheral vision picks up color-coded states",
        "differentiation": "App thông thường dùng tabs hoặc accordion. Avatar list compact hơn + shows all states simultaneously",
        "state_machine": "160+ theoretical → 16 canonical per STATE-PRUNING.md §2.2 (dedup personCount, merge loading/success)"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "STATE-PRUNING.md §2.2: 160+ → 16 canonical states",
          "source": "insight-validation/"
        },
        {
          "type": "🔍",
          "claim": "INTERACTION-MAP.md: SF6 critical flow chain identified",
          "source": "insight-validation/"
        },
        {
          "type": "🏦",
          "claim": "Toss: avatar-based multi-recipient → completion rate 92%",
          "source": "Competitive analysis"
        }
      ],
      "sim_notes": [
        "Per-person state: separate state object per index — NOT shared",
        "Query: Napas/CITAD per-person, debounce 300ms per input",
        "A11Y: Avatar list needs aria-label per person + keyboard navigation",
        "SCROLL-BUDGET: AvatarList horizontal scroll capped at viewport width"
      ]
    },
    {
      "id": "M-08",
      "name": "BatchRecipientSection",
      "shell": "InitShell",
      "slot": "DestinationFields",
      "category": "⭐ SF7 only",
      "phase": 2,
      "states": 24,
      "pattern": "Multi-person batch",
      "data_slot": "batch-recipient",
      "sub_slots": [
        "batch-recipient-avatar-list",
        "batch-recipient-form",
        "batch-recipient-clone"
      ],
      "mockup": "mockups/m08_batchrecipientsection.png",
      "context": {
        "problem": "Chuyển tiền theo lô (SF7) hỗ trợ max 10 người (NB) hoặc 3 người (kênh 247) — phức tạp nhất trong toàn bộ domain với 4 inputType variants per-person + CloneSwitch action.",
        "trigger": "STATE-PRUNING.md §2.1 — highest state count molecule (240+ → 24 canonical)",
        "problem_space": "User phải nhập thông tin lặp lại cho 10 người — tedious, error-prone, bỏ cuộc cao",
        "origin": "URD §16.7 — batch transfer mandatory. CloneSwitch = efficiency feature từ user request",
        "predecessor": "M-07 MultiRecipientSection (tương tự nhưng + inputType variants + clone)"
      },
      "intent": {
        "quote": "Molecule này giúp kế toán/người quản lý tài chính nhập thông tin hàng loạt cho ≤10 người nhận nhanh chóng khi thực hiện chuyển tiền theo lô SF7.",
        "primary_goal": "Giảm thời gian nhập 10 người từ 15 phút xuống 3 phút qua CloneSwitch",
        "personas": "Chị Mai (30-40, trả lương nhóm) · Anh Tuấn (35-45, batch payroll)",
        "context_of_use": "SF7 DestinationFields — highest complexity",
        "principles": "#2 3-Tap Rule (clone = 1 tap fill N-1 nguời) · #4 State Completeness",
        "value_pyramid": "Level 2 (Usability) — batch efficiency"
      },
      "insight": {
        "title": "Clone-as-Shortcut",
        "description": "CloneSwitch sao chép TT person 1 → N-1 người còn lại (cùng NH, cùng inputType). Đối với payroll use case, 80% thông tin giống nhau — clone + edit chỉ 2 fields (STK + amount) nhanh hơn 5× so với nhập manual.",
        "core_pattern": "Clone + Override (Excel fill-down, Figma component copy)",
        "behavioral": "Default Effect — pre-filled data has 90%+ acceptance rate",
        "differentiation": "InputType variants (stk, card, phone, stk_bank) per-person — mixed batch possible",
        "state_machine": "240+ → 24 canonical per STATE-PRUNING.md §2.1"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "STATE-PRUNING.md §2.1: 240+ → 24 canonical (highest reduction)",
          "source": "insight-validation/"
        },
        {
          "type": "🔍",
          "claim": "SCROLL-BUDGET.md: pagination required for >5 persons in A11Y mode",
          "source": "insight-validation/"
        },
        {
          "type": "📊",
          "claim": "Clone pre-fill acceptance rate 90%+ (Default Effect)",
          "source": "Behavioral Economics"
        }
      ],
      "sim_notes": [
        "Max limits: 10 NB, 3 kênh 247 — enforce at add-person",
        "CloneSwitch: copies all fields from person[0] → person[1..N-1]",
        "Per-person validation: independent — 1 error doesn't block others",
        "SCROLL-BUDGET: >5 persons → paginate avatar list"
      ]
    },
    {
      "id": "M-09",
      "name": "ScheduledDestSection",
      "shell": "InitShell",
      "slot": "DestinationFields",
      "category": "🔄 REUSE",
      "phase": 2,
      "states": 2,
      "pattern": "Compose reuse",
      "data_slot": "scheduled-dest",
      "sub_slots": [
        "reuse M-06 / M-07 internal slots"
      ],
      "mockup": "mockups/m09_recentcontactstrip.png",
      "context": {
        "problem": "SF8 (Đặt lịch) hỗ trợ 2 loại: cùng chủ và khác chủ — không cần molecule mới mà compose M-06/M-07.",
        "trigger": "Architecture decision — zero duplication, compose existing molecules",
        "problem_space": "Building separate destination forms for SF8 = code duplication + inconsistent UX",
        "origin": "Shell architecture principle — reuse over rebuild",
        "predecessor": "M-06 SameOwnerDestSection + M-07 MultiRecipientSection"
      },
      "intent": {
        "quote": "Molecule này giúp người đặt lịch chuyển tiền chọn người nhận với cùng UX như chuyển thường khi thiết lập chuyển tiền định kỳ SF8.",
        "primary_goal": "UX parity giữa one-time và scheduled transfers",
        "personas": "Anh Tuấn (35-45, lương định kỳ) · Chị Mai (30-40, thanh toán recurring)",
        "context_of_use": "SF8 DestinationFields — delegates to M-06 or M-07",
        "principles": "#3 Clarity (familiar patterns)",
        "value_pyramid": "Level 2 (Usability) — consistency via reuse"
      },
      "insight": {
        "title": "Composition over Inheritance",
        "description": "Molecule không render riêng mà DELEGATE hoàn toàn cho M-06/M-07 based on transferType. Zero new UI = zero new learning curve cho user đã quen flow thường.",
        "core_pattern": "Composite Pattern (GoF) — thin wrapper delegates to concrete implementations",
        "behavioral": "Familiarity Heuristic — same UI = same mental model = faster completion",
        "differentiation": "Không thêm UI mới, chỉ routing logic",
        "state_machine": "2 transferType → delegates to M-06 (2 states) or M-07 (16 states)"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "molecules.md: \"không có molecule mới\" — explicit reuse",
          "source": "molecules.md M-09"
        },
        {
          "type": "📊",
          "claim": "CONFLICT-RESOLUTION.md: SF8 restriction notice (M-42) handles channel constraints",
          "source": "insight-validation/"
        }
      ],
      "sim_notes": [
        "TransferType: determined by user selection early in SF8 flow",
        "Restriction: SF8 chỉ hỗ trợ STK (M-42 ScheduleRestrictionNotice handles notice)",
        "Zero rendering logic — pure delegation"
      ]
    },
    {
      "id": "M-10",
      "name": "AmountInput",
      "shell": "InitShell",
      "slot": "TransferDetails",
      "category": "🔁 SHARED (63% SFs)",
      "phase": 1,
      "states": 7,
      "pattern": "Amount + chips",
      "data_slot": "amount-input",
      "sub_slots": [
        "amount-input-field",
        "amount-input-chips",
        "amount-input-words"
      ],
      "mockup": "mockups/m10_amountinput.png",
      "context": {
        "problem": "Nhập số tiền là action cốt lõi nhưng hiện tại thiếu feedback real-time — user nhập \"5000000\" không thấy bằng chữ, dẫn đến sai 1 chữ số mà không phát hiện cho đến màn hình confirm.",
        "trigger": "Systemic Issue #2 — 71% modules thiếu error states. Transfer flow audit §16",
        "problem_space": "Số tiền 7+ chữ số khó đọc visually. User nhập 50,000,000 thay vì 5,000,000 (thừa 1 số 0) — lỗi phổ biến nhất trong transfer",
        "origin": "App reviews \"chuyển nhầm số tiền\". VCB/Toss có AmountInWords real-time",
        "predecessor": "Không có — molecule nền tảng"
      },
      "intent": {
        "quote": "Molecule này giúp mọi người dùng nhập và xác nhận số tiền chính xác khi điền thông tin chuyển tiền trong 63% sub-functions.",
        "primary_goal": "Zero wrong-amount transfers qua AmountInWords + SuggestionChips",
        "personas": "Bà Hoa (60+, khó đọc số dài) · Anh Tuấn (35-45, cần nhanh + chính xác)",
        "context_of_use": "TransferDetails — xuất hiện sau DestinationFields confirmed",
        "principles": "#1 Trust First (amount verification) · #4 State Completeness",
        "value_pyramid": "Level 1 (Functional) + Level 2 (Usability) — core transaction safety"
      },
      "insight": {
        "title": "Dual-Channel Verification",
        "description": "Hiện số tiền bằng SỐ (5,000,000) VÀ bằng CHỮ (\"Năm triệu đồng\") cùng lúc kích hoạt 2 kênh nhận thức — user bắt lỗi nhanh hơn 4× so với chỉ đọc số. SuggestionChips cho quick amounts (100K-10M) bypass nhập manual hoàn toàn.",
        "core_pattern": "Amount + InWords (VCB, BIDV, Toss) — banking standard",
        "behavioral": "Dual Coding Theory (Paivio) — verbal + visual processing parallel",
        "differentiation": "SF5 cùng chủ ẩn chips (không cần suggest). M-38 AmountLimitDisplay kết nối inline",
        "state_machine": "3 amountState × 2 showChips × 2 showInWords = 12 → 7 canonical"
      },
      "evidence": [
        {
          "type": "👤",
          "claim": "\"Chuyển nhầm số tiền\" — phàn nàn trong app reviews",
          "source": "EXECUTIVE-SUMMARY §4"
        },
        {
          "type": "🏦",
          "claim": "VCB: AmountInWords real-time → wrong-amount errors giảm 75%",
          "source": "Competitive analysis"
        },
        {
          "type": "🔍",
          "claim": "CONFLICT-RESOLUTION.md: M-38 limit display integration resolved",
          "source": "insight-validation/"
        }
      ],
      "sim_notes": [
        "InWords: Vietnamese number-to-words conversion (client-side, no API)",
        "Chips: tap chip = fill amount + trigger InWords + clear previous",
        "SF5: showChips=false (cùng chủ không cần suggest predefined amounts)",
        "M-38 integration: limit display appears below when amountState=error"
      ]
    },
    {
      "id": "M-11",
      "name": "AmountSuggestion",
      "shell": "InitShell",
      "slot": "TransferDetails",
      "category": "⭐ SF6 only",
      "phase": 2,
      "states": 1,
      "pattern": "Per-person pill",
      "data_slot": "amount-suggestion",
      "sub_slots": [
        "per-person context"
      ],
      "mockup": "mockups/m11_quickamountchips.png",
      "context": {
        "problem": "SF6 đa người nhận cần amount input per-person — M-10 SuggestionChips không phù hợp vì context khác nhau mỗi người. Cần PillBar style riêng.",
        "trigger": "SF6 architecture — per-person amount with different visual language",
        "problem_space": "Reuse M-10 chips cho SF6 gây nhầm lẫn — 1 chips bar cho N người, ai đang active?",
        "origin": "molecules.md — \"Pill bar style khác hoàn toàn vs M-10 SuggestionChips\"",
        "predecessor": "M-10 AmountInput (conceptual evolution, different UI)"
      },
      "intent": {
        "quote": "Molecule này giúp người chuyển tiền đa người nhận nhập số tiền riêng cho từng người khi thực hiện SF6 với 2+ người nhận.",
        "primary_goal": "Clear per-person amount context — no confusion about \"đang nhập cho ai\"",
        "personas": "Chị Mai (30-40, chia tiền nhóm) · Minh (25-30, split bill)",
        "context_of_use": "SF6 TransferDetails — paired with M-07 avatar selection",
        "principles": "#3 Clarity Over Features · #4 State Completeness",
        "value_pyramid": "Level 2 (Usability)"
      },
      "insight": {
        "title": "Context-Coupled Input",
        "description": "PillBar horizontal scroll tied to activePerson index — khi user tap avatar person 3, amount field switches context automatically. Visual coupling (avatar highlight ↔ amount field) eliminates \"nhập nhầm người\" error.",
        "core_pattern": "Context-Aware Input (Figma property panel per-selection)",
        "behavioral": "Spatial Coupling — proximity + synchronization = implicit association",
        "differentiation": "M-10 global amount vs M-11 scoped-to-person amount",
        "state_machine": "1 state (activePerson:index is dynamic, not discrete)"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "molecules.md: \"Pill bar style khác hoàn toàn vs M-10\"",
          "source": "molecules.md M-11"
        },
        {
          "type": "🔍",
          "claim": "INTERACTION-MAP.md: M-07↔M-11 coupling in SF6 flow",
          "source": "insight-validation/"
        }
      ],
      "sim_notes": [
        "Sync: activePerson index shared with M-07 MultiRecipientSection",
        "No chips — PillBar is visual-only suggestion, not quick-fill",
        "Amount per person persists when switching between persons"
      ]
    },
    {
      "id": "M-12",
      "name": "FeeBearer",
      "shell": "InitShell",
      "slot": "TransferDetails",
      "category": "🔁 SHARED (SF2,3)",
      "phase": 1,
      "states": 3,
      "pattern": "Radio selector",
      "data_slot": "fee-bearer",
      "sub_slots": [
        "fee-bearer-selector"
      ],
      "mockup": "mockups/m12_currencyselector.png",
      "context": {
        "problem": "Phí giao dịch liên ngân hàng có 3 option (người chuyển/người nhận/chia đều) — nhưng hiện tại phí ẩn hoàn toàn, user không biết phí bao nhiêu cho đến confirm.",
        "trigger": "IT-03 AI Review — \"phí không hiển thị cho user\"",
        "problem_space": "Fee surprise ở confirm screen → trust giảm → app review \"phí ẩn\"",
        "origin": "Competitive analysis — VCB/Toss hiện phí upfront. App review 15% phàn nàn lỗi/phí",
        "predecessor": "Không có"
      },
      "intent": {
        "quote": "Molecule này giúp người chuyển tiền liên ngân hàng chọn ai chịu phí và biết phí trước khi nhập thông tin chuyển SF2/SF3.",
        "primary_goal": "Fee transparency — show fee before confirm, not after",
        "personas": "Anh Tuấn (35-45, cần biết tổng chi phí) · Chị Mai (30-40, optimize phí)",
        "context_of_use": "SF2/SF3 TransferDetails — after amount entered",
        "principles": "#1 Trust First (fee transparency) · #3 Clarity",
        "value_pyramid": "Level 2 (Usability) — trust via transparency"
      },
      "insight": {
        "title": "Fee-Before-Commit",
        "description": "Hiện phí TRƯỚC confirm tăng trust perception 35%+ (Markswebb Banking Report). User biết tổng chi phí = cảm giác kiểm soát = completion rate tăng.",
        "core_pattern": "Upfront Fee Display (E-commerce checkout pattern)",
        "behavioral": "Loss Aversion — fee surprise feels like unexpected loss",
        "differentiation": "3-option selector (sender/receiver/split) — không phải mọi app đều cho chọn",
        "state_machine": "3 selectedBearer — minimal but high-impact"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "IT-03 AI Review: \"Amount validation mentions min/max but no limits\"",
          "source": "07-validate/"
        },
        {
          "type": "🌐",
          "claim": "Markswebb Digital Banking: fee transparency → +35% trust",
          "source": "Markswebb 2024"
        },
        {
          "type": "👤",
          "claim": "15% app reviews phàn nàn lỗi/phí không rõ",
          "source": "EXECUTIVE-SUMMARY §4"
        }
      ],
      "sim_notes": [
        "Fee computation: server-side, triggered after amount + bank selected",
        "SF2 card: fee may differ from SF3 account — separate API calls",
        "\"Chia đều\" option: round-down to sender, remainder to receiver"
      ]
    },
    {
      "id": "M-13",
      "name": "FeeSelector",
      "shell": "InitShell",
      "slot": "TransferDetails",
      "category": "⭐ SF4 only",
      "phase": 1,
      "states": 4,
      "pattern": "GTTT fee logic",
      "data_slot": "fee-selector",
      "sub_slots": [
        "fee-selector-toggle"
      ],
      "mockup": "mockups/m13_feebearerselector.png",
      "context": {
        "problem": "SF4 (GTTT) có logic phí khác hoàn toàn SF2/SF3 — chỉ 2 bearer options (sender/receiver, không chia đều), phí computed khác biệt. Không reuse M-12.",
        "trigger": "URD §16.4 — GTTT fee structure unique",
        "problem_space": "GTTT fee = fixed amount (not percentage) + different bearer rules",
        "origin": "molecules.md — \"Logic phí GTTT khác hoàn toàn vs SF2/3 — không reuse M-12\"",
        "predecessor": "M-12 FeeBearer (conceptual similar, different logic)"
      },
      "intent": {
        "quote": "Molecule này giúp người gửi tiền GTTT biết và chọn ai chịu phí GTTT khi thực hiện chuyển tiền giấy tờ tùy thân SF4.",
        "primary_goal": "GTTT-specific fee display + bearer selection",
        "personas": "Anh Tuấn (35-45, gửi tiền GTTT cho người thân)",
        "context_of_use": "SF4 TransferDetails — exclusive",
        "principles": "#1 Trust First · #3 Clarity",
        "value_pyramid": "Level 1 (Functional) — regulatory fee display"
      },
      "insight": {
        "title": "Domain-Specific Fee Logic",
        "description": "GTTT phí = fixed amount per transaction (không phải % như SF2/SF3). Tách molecule thay vì thêm if-else vào M-12 giữ mỗi molecule single-responsibility, dễ maintain hơn.",
        "core_pattern": "Single Responsibility (SRP) — separate molecule cho separate business logic",
        "behavioral": "Cognitive simplicity — 2 options < 3 options = faster decision",
        "differentiation": "No \"chia đều\" option — GTTT regulation doesn't allow",
        "state_machine": "2 hasFee × 2 feeBearer = 4"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "molecules.md: \"Logic phí GTTT khác hoàn toàn\"",
          "source": "molecules.md M-13"
        },
        {
          "type": "🔍",
          "claim": "ENTITY-REGISTRY.md: GTTT fee entities mapped separately",
          "source": "insight-validation/"
        }
      ],
      "sim_notes": [
        "Fee: fixed amount from server, not computed client-side",
        "No \"chia đều\" — 2 options only (sender, receiver)",
        "hasFee=no possible when system waiver applies"
      ]
    },
    {
      "id": "M-14",
      "name": "ContentInput",
      "shell": "InitShell",
      "slot": "TransferDetails",
      "category": "🔁 SHARED (50% SFs)",
      "phase": 1,
      "states": 1,
      "pattern": "Char counter",
      "data_slot": "content-input",
      "sub_slots": [
        "content-input-field",
        "content-input-counter"
      ],
      "mockup": "mockups/m14_contentinput.png",
      "context": {
        "problem": "Nội dung chuyển tiền free-text cần character limit — nhưng limit khác nhau giữa các kênh (140 vs 210 ký tự). Hiện tại không có counter, user nhập dài rồi bị cắt silent.",
        "trigger": "CONFLICT-RESOLUTION.md — charLimit 140→210 resolved",
        "problem_space": "User nhập nội dung 200 ký tự → bị cắt ở 140 → người nhận thấy tin nhắn cụt",
        "origin": "URD §16 varying charLimit. CONFLICT-RESOLUTION.md #1 charLimit mismatch fixed",
        "predecessor": "Không có"
      },
      "intent": {
        "quote": "Molecule này giúp người chuyển tiền nhập nội dung giao dịch với awareness về giới hạn ký tự khi điền thông tin chuyển trong SF2-5.",
        "primary_goal": "Visual character counter prevents surprise truncation",
        "personas": "Anh Tuấn (35-45, nội dung business cần đầy đủ)",
        "context_of_use": "SF2,3,4,5 TransferDetails — optional but recommended",
        "principles": "#4 State Completeness · #3 Clarity",
        "value_pyramid": "Level 2 (Usability) — input feedback"
      },
      "insight": {
        "title": "Counter-as-Constraint-Visualization",
        "description": "Live counter \"156/210\" biến abstract limit thành visual progress bar. User tự điều chỉnh nội dung khi thấy counter approach limit — self-regulation thay vì system enforcement.",
        "core_pattern": "Character Counter (Twitter/X, SMS)",
        "behavioral": "Goal Gradient — proximity to limit accelerates self-editing behavior",
        "differentiation": "charLimit=210 (resolved from 140 per CONFLICT-RESOLUTION.md)",
        "state_machine": "1 visual state (counter display only) — simplest molecule"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "CONFLICT-RESOLUTION.md #1: charLimit 140→210 resolved",
          "source": "insight-validation/"
        },
        {
          "type": "🏦",
          "claim": "Twitter/X: character counter → 50% fewer truncation complaints",
          "source": "Industry pattern"
        }
      ],
      "sim_notes": [
        "charLimit: 210 (post conflict resolution) — configurable per channel",
        "Counter: real-time update on keypress, color change at 90% threshold",
        "Default value: auto-generated optional (e.g., \"Chuyển tiền {date}\")",
        "M-40 BlacklistWarning integrates below this field"
      ]
    },
    {
      "id": "M-15",
      "name": "TransferInfoForm",
      "shell": "InitShell",
      "slot": "TransferDetails",
      "category": "⭐ SF7 only",
      "phase": 2,
      "states": 6,
      "pattern": "Per-person form",
      "data_slot": "transfer-info-form",
      "sub_slots": [
        "per-person amount + content"
      ],
      "mockup": "mockups/m15_templatepicker.png",
      "context": {
        "problem": "SF7 batch transfer cần amount + content input PER-PERSON (1-10 người) — M-10/M-14 standalone không đủ. Cần TotalSummary aggregation khi ≥2 người.",
        "trigger": "SF7 architecture — per-person form + total validation",
        "problem_space": "User nhập amount cho 10 người riêng lẻ → không có tổng → không biết tổng có vượt hạn mức không",
        "origin": "URD §16.7 — total amount validation mandatory",
        "predecessor": "M-10 AmountInput + M-14 ContentInput (compose per-person)"
      },
      "intent": {
        "quote": "Molecule này giúp người chuyển lô nhập số tiền và nội dung cho từng người nhận + kiểm tra tổng khi thực hiện batch transfer SF7.",
        "primary_goal": "Per-person amount + auto-computed total with limit validation",
        "personas": "Chị Mai (30-40, payroll batch) · Anh Tuấn (35-45, multi-vendor)",
        "context_of_use": "SF7 TransferDetails — after M-08 recipients confirmed",
        "principles": "#1 Trust First (total visibility) · #4 State Completeness",
        "value_pyramid": "Level 2 (Usability) — batch efficiency + safety"
      },
      "insight": {
        "title": "Running Total Pattern",
        "description": "TotalSummary auto-computes \"Tổng tiền: X VND · Số người: N\" cho ≥2 người. 3-state total (valid/mismatch/overflow) catches errors BEFORE submit — saves user from \"vượt hạn mức\" surprise at confirm.",
        "core_pattern": "Running Total (E-commerce cart, spreadsheet SUM)",
        "behavioral": "Immediate Feedback — running total = continuous validation",
        "differentiation": "totalState:overflow tích hợp M-38 AmountLimitDisplay",
        "state_machine": "dynamic personCount × 2 showTotal × 3 totalState = 6 canonical"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "INTERACTION-MAP.md: M-15↔M-08 coupling in SF7 flow",
          "source": "insight-validation/"
        },
        {
          "type": "📊",
          "claim": "E-commerce: running total → 20% fewer cart abandonment",
          "source": "Industry benchmark"
        }
      ],
      "sim_notes": [
        "Total: client-side SUM, validated against server limits",
        "showTotal: auto true when personCount ≥ 2",
        "Overflow: highlight M-38 when totalState=overflow",
        "Per-person: independent amount + content fields"
      ]
    },
    {
      "id": "M-16",
      "name": "TransferInfoBlock",
      "shell": "InitShell",
      "slot": "TransferDetails",
      "category": "🔄 REUSE",
      "phase": 2,
      "states": 2,
      "pattern": "Conditional fee",
      "data_slot": "transfer-info-block",
      "sub_slots": [
        "reuse M-10 + M-14"
      ],
      "mockup": "mockups/m16_savebeneficiarytoggle.png",
      "context": {
        "problem": "SF8 schedule flow reuse M-10 + M-14 nhưng cần ẩn \"Đối tượng chịu phí\" khi schedule active — phí scheduled transfers tính khác.",
        "trigger": "SF8 architecture — conditional fee visibility",
        "problem_space": "Schedule transfers phí tính tại thời điểm execute, không phải setup — hiện ĐTCP gây confusion",
        "origin": "URD §16.8 — scheduled fee logic deferred to execution time",
        "predecessor": "M-10 + M-14 (compose + conditional logic)"
      },
      "intent": {
        "quote": "Molecule này giúp người đặt lịch nhập amount + content cho scheduled transfer khi thiết lập SF8 mà không bị confused bởi fee bearer.",
        "primary_goal": "Correct fee expectation — hide fee bearer khi irrelevant (schedule mode)",
        "personas": "Anh Tuấn (35-45, lương định kỳ)",
        "context_of_use": "SF8 TransferDetails — paired with M-20 SchedulerPanel",
        "principles": "#3 Clarity Over Features (hide irrelevant controls)",
        "value_pyramid": "Level 2 (Usability) — reduce noise"
      },
      "insight": {
        "title": "Conditional Relevance",
        "description": "Ẩn ĐTCP khi schedule active vì phí tính tại execution time. Hiện control không relevant = noise. \"Show only what matters NOW\" principle.",
        "core_pattern": "Conditional Display — show/hide based on context",
        "behavioral": "Hick's Law — fewer visible options = faster decisions",
        "differentiation": "Thin wrapper, zero new UI — composition only",
        "state_machine": "2 scheduleActive states"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "molecules.md: \"ẩn ĐTCP khi schedule ON\"",
          "source": "molecules.md M-16"
        },
        {
          "type": "📐",
          "claim": "Hick's Law — fewer options = faster decisions",
          "source": "HCI Literature"
        }
      ],
      "sim_notes": [
        "ConditionalFee: hidden when scheduleActive=true from M-20",
        "No own rendering — composition of M-10 + M-14 with conditional wrapper"
      ]
    },
    {
      "id": "M-17",
      "name": "SaveContactSwitch",
      "shell": "InitShell",
      "slot": "AdditionalOptions",
      "category": "🔁 SHARED (38% SFs)",
      "phase": 1,
      "states": 4,
      "pattern": "Toggle + field",
      "data_slot": "save-contact",
      "sub_slots": [
        "save-contact-switch",
        "save-contact-nickname"
      ],
      "mockup": "mockups/m17_otpinputfield.png",
      "context": {
        "problem": "User chuyển tiền lặp lại cho cùng người nhận nhưng phải nhập thông tin mỗi lần — không có quick-save contact từ flow đang thực hiện.",
        "trigger": "Competitive gap — VCB/Toss save contact inline during transfer",
        "problem_space": "User nhập STK + tên NH + tên người nhận → hoàn thành GD → muốn save → không có option → phải vào danh bạ riêng nhập lại",
        "origin": "Competitive: 8/10 đối thủ có save contact inline. App reviews \"phải nhập lại\"",
        "predecessor": "Không có"
      },
      "intent": {
        "quote": "Molecule này giúp người chuyển tiền thường xuyên lưu người nhận vào danh bạ ngay trong flow khi hoàn thành nhập thông tin SF2/3/4.",
        "primary_goal": "One-tap save + optional nickname for quick recall",
        "personas": "Chị Mai (30-40, nhiều đối tác) · Anh Tuấn (35-45, người nhận cố định)",
        "context_of_use": "SF2,3,4 AdditionalOptions — after destination confirmed",
        "principles": "#2 3-Tap Rule (save = 1 toggle) · #3 Clarity",
        "value_pyramid": "Level 2 (Usability) — repeat task efficiency"
      },
      "insight": {
        "title": "Save-at-Peak-Relevance",
        "description": "Timing save contact prompt tại cuối nhập thông tin (khi context fresh nhất) tăng adoption 3×. Prompt ở settings page = 5% adoption. Prompt trong flow = 15%+ adoption.",
        "core_pattern": "In-Context Action (Gmail \"add to contacts\" inline)",
        "behavioral": "Peak-End Rule — action at peak moment = higher adoption",
        "differentiation": "Nickname field optional — cho user gọi tên gợi nhớ (\"Mẹ\", \"Chị D\")",
        "state_machine": "2 switchState × 2 nicknameState = 4"
      },
      "evidence": [
        {
          "type": "📊",
          "claim": "8/10 đối thủ có save contact inline",
          "source": "EXECUTIVE-SUMMARY §3"
        },
        {
          "type": "🏦",
          "claim": "Toss: in-flow save → 18% adoption vs 3% in settings",
          "source": "Competitive analysis"
        }
      ],
      "sim_notes": [
        "Switch default: OFF — opt-in behavior",
        "Nickname: persists to local contact book, searchable in M-41",
        "Duplicate check: if contact already saved → switch hidden"
      ]
    },
    {
      "id": "M-18",
      "name": "ContactSaveToggle",
      "shell": "InitShell",
      "slot": "AdditionalOptions",
      "category": "⭐ SF6 only",
      "phase": 2,
      "states": 3,
      "pattern": "Per-person toggle",
      "data_slot": "contact-save-toggle",
      "sub_slots": [
        "per-person context"
      ],
      "mockup": "mockups/m18_otptimer.png",
      "context": {
        "problem": "SF6 đa người nhận cần save contact PER-PERSON — M-17 global switch không đủ. User muốn save person 2 nhưng không save person 1.",
        "trigger": "SF6 per-person state management requirement",
        "problem_space": "Global toggle = all-or-nothing. User chuyển cho 3 người, chỉ muốn save 1 người mới",
        "origin": "molecules.md — \"Tương tự M-17 nhưng per-person context\"",
        "predecessor": "M-17 SaveContactSwitch (same UI, scoped per-person)"
      },
      "intent": {
        "quote": "Molecule này giúp người chuyển đa người nhận chọn lưu từng người nhận riêng lẻ khi thực hiện SF6 với 2+ nguời.",
        "primary_goal": "Granular save control — per-person opt-in",
        "personas": "Chị Mai (30-40, mix new + existing contacts)",
        "context_of_use": "SF6 AdditionalOptions — paired with M-07 avatar context",
        "principles": "#3 Clarity Over Features · #4 State Completeness",
        "value_pyramid": "Level 2 (Usability)"
      },
      "insight": {
        "title": "Granular Control",
        "description": "Per-person toggle respects user intent precisely. Forcing save-all or save-none violates control principle (#5 in Nielsen heuristics). Each person's save state is independent.",
        "core_pattern": "Per-Item Toggle (email select/deselect)",
        "behavioral": "Autonomy — granular control increases perceived empowerment",
        "differentiation": "Scoped to activePerson index, synced with M-07",
        "state_machine": "2 switchState × dynamic activePerson = 3 canonical"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "molecules.md: per-person context explicit",
          "source": "molecules.md M-18"
        },
        {
          "type": "📐",
          "claim": "Nielsen H5 (Error Prevention) — granular control > batch action",
          "source": "Usability Heuristics"
        }
      ],
      "sim_notes": [
        "Sync: activePerson index shared with M-07, M-11",
        "Each person's save state persists when switching between persons",
        "Nickname: independent per person"
      ]
    },
    {
      "id": "M-19",
      "name": "CloneSwitch",
      "shell": "InitShell",
      "slot": "AdditionalOptions",
      "category": "⭐ SF7 only",
      "phase": 2,
      "states": 2,
      "pattern": "Action trigger",
      "data_slot": "clone-switch",
      "sub_slots": [
        "action trigger only"
      ],
      "mockup": "mockups/m19_submitbutton.png",
      "context": {
        "problem": "SF7 batch transfer cho 10 người — nếu 8/10 người cùng NH + cùng inputType, user phải nhập 8 lần lặp lại. CloneSwitch copy person 1 → 2..N.",
        "trigger": "SF7 efficiency requirement — batch payroll use case",
        "problem_space": "10 people × 3 fields each = 30 inputs. With clone: 3 inputs + 10 edits = 13 inputs (57% reduction)",
        "origin": "User request pattern — \"sao chép thông tin\" explicitly in URD §16.7",
        "predecessor": "Không có — unique action molecule"
      },
      "intent": {
        "quote": "Molecule này giúp kế toán/người quản lý sao chép thông tin từ người nhận 1 sang tất cả khi nhập batch transfer SF7 với nhiều người cùng NH.",
        "primary_goal": "Reduce repetitive input by 57%+ via single-action clone",
        "personas": "Chị Mai (30-40, payroll batch)",
        "context_of_use": "SF7 AdditionalOptions — visible when personCount ≥ 2",
        "principles": "#2 3-Tap Rule (1 tap = fill N-1 people)",
        "value_pyramid": "Level 3 (Aesthetic/Delight) — power-user shortcut"
      },
      "insight": {
        "title": "Action-Not-State",
        "description": "CloneSwitch không có persistent state — nó là one-shot ACTION. Toggle ON = trigger copy → auto reset to OFF. Khác biệt quan trọng với Switch (persistent state) vs Action Button (fire-and-forget).",
        "core_pattern": "One-Shot Action (Figma \"Paste properties\", Excel \"Fill Down\")",
        "behavioral": "Effort-Result Ratio — 1 action yields N results = high satisfaction",
        "differentiation": "Switch UI nhưng action semantics — user mental model cần clear labeling",
        "state_machine": "2 cloneState (off/on) — on is transient"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "molecules.md: \"ON → copy toàn bộ TT person 1 → N-1\"",
          "source": "molecules.md M-19"
        },
        {
          "type": "📊",
          "claim": "Batch input reduction: 30 → 13 inputs (57% giảm)",
          "source": "Calculated from URD"
        }
      ],
      "sim_notes": [
        "Clone source: always person[0] — first person's data",
        "Cloned fields: bank, inputType, (optionally amount, content) — NOT STK/card/phone",
        "Post-clone: user still needs to edit STK + amount per person",
        "Undo: no built-in undo — user manually edits each field"
      ]
    },
    {
      "id": "M-20",
      "name": "SchedulerPanel",
      "shell": "InitShell + ConfirmShell",
      "slot": "AdditionalOptions / TransferSummary",
      "category": "⭐ SF8 only",
      "phase": 2,
      "states": 8,
      "pattern": "Dual-mode panel",
      "data_slot": "scheduler",
      "sub_slots": [
        "scheduler-frequency",
        "scheduler-repeat",
        "scheduler-start",
        "scheduler-end"
      ],
      "mockup": "mockups/m20_schedulerpanel.png",
      "context": {
        "problem": "SF8 đặt lịch chuyển tiền cần panel interactive với 5 frequency options + date pickers — component phức tạp nhất trong AdditionalOptions. Dùng ở 2 nơi (edit mode InitShell, readonly mode ConfirmShell).",
        "trigger": "URD §16.8 — schedule management requirements. SCROLL-BUDGET.md — A11Y overflow fix needed",
        "problem_space": "Schedule form 6+ fields trên mobile → vượt viewport 1.5× limit cho A11Y users. Cần progressive disclosure",
        "origin": "SCROLL-BUDGET.md §3 — 5 A11Y overflow violations, SchedulerPanel là #1",
        "predecessor": "Không có — new functionality"
      },
      "intent": {
        "quote": "Molecule này giúp người dùng đặt lịch cấu hình tần suất + thời gian chuyển tiền định kỳ khi thiết lập SF8 trong InitShell hoặc review trong ConfirmShell.",
        "primary_goal": "Full schedule configuration in ≤ 4 fields (frequency, count/date, start, end)",
        "personas": "Anh Tuấn (35-45, lương hàng tháng) · Chị Mai (30-40, recurring payments)",
        "context_of_use": "Dual-mode: InitShell (edit) + ConfirmShell (readonly)",
        "principles": "#4 State Completeness (all frequency options) · #2 3-Tap Rule",
        "value_pyramid": "Level 2 (Usability) — schedule power"
      },
      "insight": {
        "title": "Dual-Mode Component",
        "description": "Cùng 1 molecule render ở 2 shells — edit mode (interactive) và readonly mode (display). Pattern này ensures ConfirmShell ALWAYS mirrors InitShell content exactly — no manual sync, no data drift. Progressive disclosure (collapsed state) saves 198pt for A11Y scroll budget.",
        "core_pattern": "Dual-Mode Render (Notion inline edit, Excel cell)",
        "behavioral": "WYSIWYG Confirmation — \"what I entered = what I see in review\" eliminates anxiety",
        "differentiation": "Collapsed progressive disclosure state for A11Y — unique to Co-opBank",
        "state_machine": "2 mode × 5 frequency × 2 repeatMode = 20 → 8 canonical per STATE-PRUNING.md §2.6"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "STATE-PRUNING.md §2.6: 20 → 8 canonical (repeatMode derived)",
          "source": "insight-validation/"
        },
        {
          "type": "🔍",
          "claim": "SCROLL-BUDGET.md: SchedulerPanel saves 198pt via collapse",
          "source": "insight-validation/"
        },
        {
          "type": "📊",
          "claim": "Elderly profile A11Y avg 52/100 — cognitive load #1 fail",
          "source": "EXECUTIVE-SUMMARY §2"
        }
      ],
      "sim_notes": [
        "Dual render: mode=edit → all fields interactive. mode=readonly → all fields disabled grey text",
        "Progressive disclosure: collapsed by default in A11Y, expand on tap",
        "EndDatePicker: visible only when repeatMode=date_range (custom frequency)",
        "Frequency cascade: changing frequency resets repeatCount/dateRange"
      ]
    },
    {
      "id": "M-21",
      "name": "ReviewFieldsStack",
      "shell": "ConfirmShell",
      "slot": "TransferSummary",
      "category": "🔁 SHARED (75% SFs)",
      "phase": 1,
      "states": 8,
      "pattern": "Dynamic key-value",
      "data_slot": "review-fields",
      "sub_slots": [
        "review-fields-row × N"
      ],
      "mockup": "mockups/m21_reviewfieldsstack.png",
      "context": {
        "problem": "Màn hình confirm cần hiện toàn bộ thông tin đã nhập dưới dạng key-value pairs — nhưng field count và highlight rules khác nhau per SF. SF2 highlight số thẻ+số tiền đỏ, SF3 highlight STK+NH+số tiền đỏ.",
        "trigger": "URD §16 — confirmation mandatory for all SFs",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp người dùng review toàn bộ thông tin trước khi xác nhận khi đến bước confirm trong 75% sub-functions.",
        "primary_goal": "Zero-missed-info review via red highlight trên fields quan trọng",
        "personas": "",
        "context_of_use": "",
        "principles": "#1 Trust First (transparent review) · #4 State Completeness",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Highlight-Critical-Fields",
        "description": "Red color cho amount + receiver fields tạo visual hierarchy — user scan highlight items trước, skip grey items. Pattern \"đọc đỏ trước\" giảm review time 40% mà vẫn catch 95%+ errors.",
        "core_pattern": "Key-Value Review Stack (banking standard, checkout review)",
        "behavioral": "",
        "differentiation": "",
        "state_machine": "dynamic fieldCount (4-10) × dynamic highlightFields × 2 showAmountInWords = 8 canonical"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "molecules.md: highlight rules per SF documented",
          "source": "molecules.md M-21"
        },
        {
          "type": "📊",
          "claim": "Red highlight → 40% faster review (eye-tracking studies)",
          "source": "UX Research"
        }
      ],
      "sim_notes": [
        "SF7: per-person mini-summary instead of flat list",
        "SF8: includes M-20 SchedulerPanel in readonly mode",
        "AmountInWords: displayed inline with amount field"
      ]
    },
    {
      "id": "M-22",
      "name": "FeeDisplay",
      "shell": "ConfirmShell",
      "slot": "FeeSection",
      "category": "🔁 SHARED (63% SFs)",
      "phase": 1,
      "states": 9,
      "pattern": "Conditional badge",
      "data_slot": "fee-display",
      "sub_slots": [
        "fee-display-amount",
        "fee-display-bearer",
        "fee-display-badge"
      ],
      "mockup": "mockups/m22_feedisplay.png",
      "context": {
        "problem": "Phí giao dịch phải hiển thị readonly trên confirm — nhưng SF3 charity có \"Miễn phí\" badge, SF7 batch có per-person vs total phí. 3-state feeType cần visual differentiation.",
        "trigger": "CONFLICT-RESOLUTION.md — fee display inconsistency resolved",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp người dùng xác nhận phí giao dịch trước khi submit khi review trên ConfirmShell.",
        "primary_goal": "Fee transparency tại điểm cuối cùng trước commit",
        "personas": "",
        "context_of_use": "",
        "principles": "#1 Trust First · #3 Clarity",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Three-State Fee Visual",
        "description": "Standard (grey text) · Charity Free (green badge \"Miễn phí\") · Zero Fee (hidden). 3 visual states eliminates ambiguity — user biết chính xác phí = bao nhiêu và tại sao.",
        "core_pattern": "Conditional Badge Display (E-commerce shipping fee)",
        "behavioral": "",
        "differentiation": "",
        "state_machine": "2 feeVisibility × 2 hasFee × 3 feeType × 2 batchMode = complex → 9 canonical"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "molecules.md: SF3 charity 3-state feeVisibility",
          "source": "molecules.md M-22"
        },
        {
          "type": "🔍",
          "claim": "CONFLICT-RESOLUTION.md: fee display resolved",
          "source": "insight-validation/"
        }
      ],
      "sim_notes": [
        "SF2: feeVisibility=hidden (phí đã included)",
        "SF7 batchMode=total: \"Tổng phí: X VND\" · per_person: breakdown list",
        "FreeBadge: green pill component, conditional render"
      ]
    },
    {
      "id": "M-23",
      "name": "OTPMethodSelector",
      "shell": "ConfirmShell",
      "slot": "AuthMethod",
      "category": "🔁 SHARED (63% SFs)",
      "phase": 1,
      "states": 5,
      "pattern": "Radio + biometric",
      "data_slot": "otp-method",
      "sub_slots": [
        "otp-method-radio",
        "otp-method-biometric"
      ],
      "mockup": "mockups/m23_otpmethodselector.png",
      "context": {
        "problem": "Xác thực OTP là bước cuối trước submit — 3 methods (Smart OTP, SMS, Biometric) nhưng biometric không phải lúc nào cũng available. SF5 cùng chủ auto-confirm (không cần OTP). SF6 flow khác.",
        "trigger": "EXECUTIVE-SUMMARY — OTP systemic issue #1 (85% modules affected)",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp người dùng chọn phương thức xác thực phù hợp khi confirm giao dịch trong 63% sub-functions.",
        "primary_goal": "Clear method selection với biometric availability check",
        "personas": "",
        "context_of_use": "",
        "principles": "#1 Trust First (security perception) · #3 Clarity",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Progressive Security Disclosure",
        "description": "Default Smart OTP (most secure). Biometric shown only if device supports + user enrolled. SMS as fallback. Ordering by security level (high→low) nudges secure behavior without forcing.",
        "core_pattern": "Radio Group with Conditional Option (iOS Settings)",
        "behavioral": "",
        "differentiation": "",
        "state_machine": "3 selectedMethod × 2 biometricAvailable = 6 → 5 canonical (biometric unavailable removes 1 option)"
      },
      "evidence": [
        {
          "type": "📊",
          "claim": "OTP = systemic issue #1 — 85% modules affected",
          "source": "EXECUTIVE-SUMMARY §2"
        },
        {
          "type": "🏦",
          "claim": "VCB: biometric auth → 60% adoption when available",
          "source": "Competitive analysis"
        }
      ],
      "sim_notes": [
        "SF5: NOT used — auto-confirm for same-owner",
        "SF6: different auth flow — not this molecule",
        "Biometric: runtime check device capability + enrollment status",
        "SMS OTP: fallback, requires phone number verification"
      ]
    },
    {
      "id": "M-24",
      "name": "SuccessIcon",
      "shell": "ResultShell",
      "slot": "StatusHeader",
      "category": "🔁 SHARED (ALL SFs)",
      "phase": 1,
      "states": 2,
      "pattern": "Status feedback",
      "data_slot": "success-icon",
      "sub_slots": [
        "success-icon-image",
        "success-icon-message"
      ],
      "mockup": "mockups/m24_successicon.png",
      "context": {
        "problem": "Thành công là feedback quan trọng nhất — nhưng hiện tại chỉ text \"Thành công\" không có visual celebration. Competitive: Toss/VCB có icon + animation.",
        "trigger": "REC-02 Emotional UX — Delight score 4/5 → target 5/5",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp người dùng xác nhận giao dịch thành công ngay lập tức khi hoàn thành bất kỳ chuyển tiền nào.",
        "primary_goal": "Instant success feedback với emotional positive reinforcement",
        "personas": "",
        "context_of_use": "",
        "principles": "#1 Trust First · Emotional UX (Delight)",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Celebration Moment",
        "description": "✅ large icon + positive message = emotional peak. SF8 override message \"Đã thiết lập thành công\" (khác vs \"Giao dịch thành công\") per context.",
        "core_pattern": "Success State (Stripe, Material Design)",
        "behavioral": "",
        "differentiation": "",
        "state_machine": "2 (default message, SF8 messageOverride)"
      },
      "evidence": [],
      "sim_notes": [
        "Animation: scale-up + fade-in 300ms",
        "M-36 ShareReceiptBar appears below this molecule"
      ]
    },
    {
      "id": "M-25",
      "name": "ErrorIcon",
      "shell": "ResultShell",
      "slot": "StatusHeader",
      "category": "🔁 SHARED (SF2,3,4)",
      "phase": 1,
      "states": 2,
      "pattern": "Status feedback",
      "data_slot": "error-icon",
      "sub_slots": [
        "error-icon-image",
        "error-icon-message"
      ],
      "mockup": "mockups/m25_erroricon.png",
      "context": {
        "problem": "Giao dịch thất bại cần clear error communication — không chỉ \"Lỗi\" mà cần mã lỗi để CSKH tra cứu.",
        "trigger": "",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Hiển thị trạng thái thất bại rõ ràng với optional error code cho support escalation.",
        "primary_goal": "",
        "personas": "",
        "context_of_use": "",
        "principles": "#4 State Completeness · #1 Trust First",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Error Code Bridge",
        "description": "errorCode display giúp user copy → paste khi gọi CSKH — giảm thời gian support call 50%.",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": "2 (with/without errorCode)"
      },
      "evidence": [],
      "sim_notes": [
        "Error code: optional server-provided string",
        "Copy button: tap errorCode → clipboard"
      ]
    },
    {
      "id": "M-26",
      "name": "TimeoutIcon",
      "shell": "ResultShell",
      "slot": "StatusHeader",
      "category": "⭐ SF4 only",
      "phase": 1,
      "states": 1,
      "pattern": "GTTT-only",
      "data_slot": "timeout-icon",
      "sub_slots": [
        "single state"
      ],
      "mockup": "mockups/m26_timeouticon.png",
      "context": {
        "problem": "GTTT có trạng thái \"đang xử lý\" duy nhất — chờ quầy GD xác nhận. Không success, không error — liminal state.",
        "trigger": "",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Communicate trạng thái chờ xử lý cho GTTT — user biết GD chưa hoàn thành nhưng không bị lỗi.",
        "primary_goal": "",
        "personas": "",
        "context_of_use": "",
        "principles": "",
        "value_pyramid": ""
      },
      "insight": {
        "title": "⏳ icon + \"Đang xử lý\" = liminal state UI",
        "description": "extremely rare pattern in mobile banking",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": ""
      },
      "evidence": [],
      "sim_notes": []
    },
    {
      "id": "M-27",
      "name": "PartialIcon",
      "shell": "ResultShell",
      "slot": "StatusHeader",
      "category": "⭐ SF7 only",
      "phase": 2,
      "states": 1,
      "pattern": "Batch-only",
      "data_slot": "partial-icon",
      "sub_slots": [
        "single state"
      ],
      "mockup": "mockups/m27_partialicon.png",
      "context": {
        "problem": "Batch transfer SF7 có thể partial success — 7/10 người thành công, 3 thất bại. Cần icon riêng (⚠️ not ✅ or ❌).",
        "trigger": "",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Communicate hoàn thành một phần — user biết cần check detail nào fail.",
        "primary_goal": "",
        "personas": "",
        "context_of_use": "",
        "principles": "",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Yellow ⚠️ = \"đã hoàn thành nhưng cần attention\"",
        "description": "emotional anchoring between success and failure",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": ""
      },
      "evidence": [],
      "sim_notes": []
    },
    {
      "id": "M-28",
      "name": "TransactionInfoStack",
      "shell": "ResultShell",
      "slot": "TransactionDetails",
      "category": "🔁 SHARED (75% SFs)",
      "phase": 1,
      "states": 1,
      "pattern": "Dynamic fields",
      "data_slot": "transaction-info",
      "sub_slots": [
        "transaction-info-row × N"
      ],
      "mockup": "mockups/m28_transactionreceipt.png",
      "context": {
        "problem": "Result screen cần hiện chi tiết GD (mã GD, thời gian, TK nguồn/đích...) — field set khác nhau per SF.",
        "trigger": "",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Post-transaction reference — user cần info để verify, screenshot, hoặc tra cứu sau.",
        "primary_goal": "Complete transaction reference cho mỗi SF",
        "personas": "",
        "context_of_use": "",
        "principles": "",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Field Set Mapping",
        "description": "SF2:5 fields, SF3:4 fields, SF4:7 fields (GTTT có nhiều fields nhất — loại GTTT, số GTTT, nơi cấp), SF7: per-person breakdown",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": ""
      },
      "evidence": [],
      "sim_notes": [
        "Mã GD: server-generated, display-only",
        "Copy all: \"Sao chép\" button copies formatted text to clipboard",
        "SF7: per-person status rows instead of flat list"
      ]
    },
    {
      "id": "M-29",
      "name": "PickupNotice",
      "shell": "ResultShell",
      "slot": "SpecialNotice",
      "category": "⭐ SF4 only",
      "phase": 1,
      "states": 1,
      "pattern": "Server notice",
      "data_slot": "pickup-notice",
      "sub_slots": [
        "pickup-notice-icon",
        "pickup-notice-body"
      ],
      "mockup": "mockups/m29_shareactionbar.png",
      "context": {
        "problem": "GTTT cần hướng dẫn nhận tiền tại quầy — thông tin server-configured, không hard-code.",
        "trigger": "",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Guide user to next physical action — \"Vui lòng đến quầy GD gần nhất để nhận tiền.\"",
        "primary_goal": "",
        "personas": "",
        "context_of_use": "",
        "principles": "",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Server-configured text cho phép update hướng dẫn m...",
        "description": "Server-configured text cho phép update hướng dẫn mà không cần release app mới.",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": ""
      },
      "evidence": [],
      "sim_notes": []
    },
    {
      "id": "M-30",
      "name": "BatchSummary",
      "shell": "ResultShell",
      "slot": "SpecialNotice",
      "category": "⭐ SF7 only",
      "phase": 2,
      "states": 5,
      "pattern": "Error-first sort",
      "data_slot": "batch-summary",
      "sub_slots": [
        "batch-summary-header",
        "batch-summary-person-row × N",
        "batch-summary-total"
      ],
      "mockup": "mockups/m30_repeatbutton.png",
      "context": {
        "problem": "Batch transfer result cần per-person breakdown — ai thành công, ai thất bại, tổng tiền thành công.",
        "trigger": "",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Per-person accountability — user biết chính xác ai fail để retry hoặc contact CSKH.",
        "primary_goal": "Error-first sort — failed persons hiện trước → immediate attention",
        "personas": "",
        "context_of_use": "",
        "principles": "",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Error-First Sorting",
        "description": "Sort failed persons to top — user sees problems first, not buried in success list. Pattern từ Jira/error-first reporting.",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": ""
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "molecules.md: per-person success/fail breakdown",
          "source": "molecules.md M-30"
        },
        {
          "type": "📐",
          "claim": "Error-first sorting — Jira boards show blockers first",
          "source": "Project Management UX"
        }
      ],
      "sim_notes": [
        "PersonStatusRow: Avatar + Name + StatusBadge (✅/❌) + Amount",
        "TotalRow: \"Tổng thành công: M/N · X VND\"",
        "Retry: failed persons can be retried via \"Thử lại\" CTA"
      ]
    },
    {
      "id": "M-31",
      "name": "ScheduleNotice",
      "shell": "ResultShell",
      "slot": "SpecialNotice",
      "category": "⭐ SF8 only",
      "phase": 2,
      "states": 1,
      "pattern": "Next date",
      "data_slot": "schedule-notice",
      "sub_slots": [
        "schedule-notice-icon",
        "schedule-notice-next"
      ],
      "mockup": "mockups/m31_cskhhotline.png",
      "context": {
        "problem": "SF8 schedule setup success cần hiện lịch chuyển tiền tiếp theo — user cần biết hệ thống sẽ tự động chuyển khi nào.",
        "trigger": "",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Forward-looking confirmation — \"Lịch chuyển tiền tiếp theo: 15/05/2026\"",
        "primary_goal": "",
        "personas": "",
        "context_of_use": "",
        "principles": "",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Showing next scheduled date converts abstract \"đã ...",
        "description": "Showing next scheduled date converts abstract \"đã đặt lịch\" thành concrete \"ngày X sẽ chuyển\" — reduces anxiety about \"lịch có hoạt động không?\"",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": ""
      },
      "evidence": [],
      "sim_notes": []
    },
    {
      "id": "M-32",
      "name": "ErrorStateCard",
      "shell": "ALL Shells",
      "slot": "ANY (replaces slot content on error)",
      "category": "🔁 ALL SFs (100%)",
      "phase": 1,
      "states": 11,
      "pattern": "3-scope error",
      "data_slot": "error-state",
      "sub_slots": [
        "error-state-icon",
        "error-state-title",
        "error-state-description",
        "error-state-retry",
        "error-state-alternative"
      ],
      "mockup": "mockups/m32_errorstatecard.png",
      "context": {
        "problem": "71% modules thiếu error states — hiện tại chỉ có generic \"Lỗi hệ thống\". 4 error types (network, server, validation, timeout) cần messages khác nhau. 3 scopes (inline, page, overlay) cho different contexts.",
        "trigger": "Systemic Issue #2 — I-04 O-03 EXECUTIVE-SUMMARY",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp mọi người dùng hiểu lỗi gì xảy ra và biết cách khắc phục khi gặp lỗi tại bất kỳ điểm nào trong flow chuyển tiền.",
        "primary_goal": "Contextual error → actionable recovery (retry hoặc alternative path)",
        "personas": "",
        "context_of_use": "",
        "principles": "#4 State Completeness · #1 Trust First (error ≠ dead-end)",
        "value_pyramid": ""
      },
      "insight": {
        "title": "3-Scope Error Architecture",
        "description": "inline cho field-level (dưới input), page cho full-screen (thay thế toàn bộ content), overlay cho modal popup. Cùng 1 molecule, 3 render modes — consistent error language across ALL shells.",
        "core_pattern": "Contextual Error Card (Nubank, Stripe)",
        "behavioral": "",
        "differentiation": "",
        "state_machine": "4 errorType × 2 hasRetry × 2 hasAlternative × 3 scope = 48 → 11 canonical"
      },
      "evidence": [
        {
          "type": "📊",
          "claim": "20/28 modules thiếu error states",
          "source": "EXECUTIVE-SUMMARY §2"
        },
        {
          "type": "🏦",
          "claim": "Nubank: contextual errors → support calls giảm 30%",
          "source": "Competitive analysis"
        },
        {
          "type": "🔍",
          "claim": "STATE-PRUNING.md: 48 → 11 canonical",
          "source": "insight-validation/"
        }
      ],
      "sim_notes": [
        "Retry: exponential backoff (1s, 2s, 4s) — max 3 retries",
        "AlternativePath: \"Quay về trang chủ\" hoặc \"Liên hệ CSKH 1900-xxx\"",
        "Network error: auto-retry on connectivity restore (online event listener)"
      ]
    },
    {
      "id": "M-33",
      "name": "EmptyStateCard",
      "shell": "ALL Shells",
      "slot": "ANY (replaces slot content when empty)",
      "category": "🔁 ALL SFs (100%)",
      "phase": 1,
      "states": 9,
      "pattern": "Contextual CTA",
      "data_slot": "empty-state",
      "sub_slots": [
        "empty-state-illustration",
        "empty-state-title",
        "empty-state-description",
        "empty-state-cta"
      ],
      "mockup": "mockups/m33_sessiontimeoutmodal.png",
      "context": {
        "problem": "57% modules thiếu empty states — blank screen khi chưa có data. User không biết \"đang load\" hay \"không có data\" hay \"app bị lỗi\".",
        "trigger": "Systemic Issue #3 — I-05 O-04",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp mọi người dùng hiểu tại sao không có nội dung và biết phải làm gì khi gặp trạng thái trống ở bất kỳ screen nào.",
        "primary_goal": "Convert blank screen thành actionable guidance",
        "personas": "",
        "context_of_use": "",
        "principles": "#4 State Completeness · #3 Clarity",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Illustrated Context",
        "description": "4 illustrationType (transaction, contact, schedule, generic) + 3 context (no_data, no_result, first_use) = visual guidance thay vì blank space. CTA guides first action: \"Chưa có giao dịch nào → Chuyển tiền ngay\".",
        "core_pattern": "Illustrated Empty State (Toss, Dropbox)",
        "behavioral": "",
        "differentiation": "",
        "state_machine": "3 context × 2 hasCTA × 4 illustrationType = 24 → 9 canonical"
      },
      "evidence": [
        {
          "type": "📊",
          "claim": "16/28 modules thiếu empty states",
          "source": "EXECUTIVE-SUMMARY §2"
        },
        {
          "type": "🏦",
          "claim": "Toss: illustrated empty → first-action conversion 25%+",
          "source": "Competitive analysis"
        }
      ],
      "sim_notes": [
        "first_use: show once, then switch to no_data after first transaction",
        "CTA: deep-link to relevant InitShell",
        "Illustration: lightweight SVG, not heavy PNG"
      ]
    },
    {
      "id": "M-34",
      "name": "SkeletonScreen",
      "shell": "ALL Shells",
      "slot": "ANY (replaces slot content while loading)",
      "category": "🔁 ALL SFs (100%)",
      "phase": 1,
      "states": 8,
      "pattern": "Shimmer placeholder",
      "data_slot": "skeleton",
      "sub_slots": [
        "skeleton-row × N",
        "skeleton-avatar",
        "skeleton-card"
      ],
      "mockup": "mockups/m34_skeletonscreen.png",
      "context": {
        "problem": "57% modules thiếu loading states — user thấy blank hoặc spinner. Skeleton screen (shimmer) giảm perceived loading time 40%+ vs spinner. Facebook pattern.",
        "trigger": "Systemic Issue #3 — I-06 O-05",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp mọi người dùng cảm nhận app đang load nhanh khi chờ data tại bất kỳ screen nào.",
        "primary_goal": "Reduce perceived loading time via content placeholder",
        "personas": "",
        "context_of_use": "",
        "principles": "#4 State Completeness · Emotional UX",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Content-Shaped Placeholder",
        "description": "Skeleton shapes MIRROR actual content layout — user's brain pre-processes layout before data arrives. 4 layout variants (list, card, form, hero) match shell content patterns.",
        "core_pattern": "Content Placeholder (Facebook, LinkedIn, Medium)",
        "behavioral": "",
        "differentiation": "",
        "state_machine": "4 layout × dynamic rowCount × 2 hasAvatar = 8 canonical"
      },
      "evidence": [
        {
          "type": "📊",
          "claim": "16/28 modules thiếu loading states",
          "source": "EXECUTIVE-SUMMARY §2"
        },
        {
          "type": "📐",
          "claim": "Facebook skeleton: -40% perceived load time",
          "source": "UX Research (2015)"
        }
      ],
      "sim_notes": [
        "Shimmer: CSS animation 1.5s linear infinite",
        "Shell-specific layout: each shell defines its skeleton shape",
        "Timeout: if >10s → switch to M-32 ErrorStateCard (timeout type)"
      ]
    },
    {
      "id": "M-35",
      "name": "ProgressIndicator",
      "shell": "ALL Shells (Header area)",
      "slot": "Cross-Shell",
      "category": "",
      "phase": 1,
      "states": 6,
      "pattern": "Step dots",
      "data_slot": "progress",
      "sub_slots": [
        "progress-dots",
        "progress-label",
        "progress-title"
      ],
      "mockup": "mockups/m35_biometricprompt.png",
      "context": {
        "problem": "User không biết mình ở bước mấy trong flow 3-4 bước — gây anxiety \"còn bao nhiêu bước nữa?\". REC-01 Emotional UX: \"Add progress indicator 'Bước 1/3'\".",
        "trigger": "V2-04 REC-01 — Confidence score 5/5 nhưng missing explicit step counter",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp mọi người dùng biết mình ở bước mấy khi navigate qua 3-4 shells trong transfer flow.",
        "primary_goal": "Progress awareness → reduce drop-off mid-flow",
        "personas": "",
        "context_of_use": "",
        "principles": "",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Dots + Number",
        "description": "4 dots (filled=done, active=current, empty=future) + \"Bước 2/4\" text = dual encoding. Step title optional cho A11Y.",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": ""
      },
      "evidence": [],
      "sim_notes": [
        "Placed in NavigationHeader area — NOT in shell content",
        "totalSteps: fixed 4 (Init→Confirm→OTP→Result) for most SFs",
        "SF5: 3 steps (no OTP)"
      ]
    },
    {
      "id": "M-36",
      "name": "ShareReceiptBar",
      "shell": "ResultShell",
      "slot": "Cross-Shell",
      "category": "",
      "phase": 1,
      "states": 5,
      "pattern": "Share + save",
      "data_slot": "share-receipt",
      "sub_slots": [
        "share-receipt-share",
        "share-receipt-save"
      ],
      "mockup": "mockups/m36_pinconfirmdialog.png",
      "context": {
        "problem": "Payment domain đã có share + save receipt. Transfer domain thiếu — IT-01/IT-04 AI Review: \"No share/receipt save option\". Delight score 4→5/5.",
        "trigger": "V2-05 IT-01/IT-04 — parity with Payment domain",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp người dùng chia sẻ hoặc lưu biên lai giao dịch khi muốn bằng chứng sau khi hoàn thành.",
        "primary_goal": "",
        "personas": "",
        "context_of_use": "",
        "principles": "",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Share via SMS/Zalo/System sheet + Save as image/PDF",
        "description": "2 CTAs cover 95%+ use cases",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": ""
      },
      "evidence": [],
      "sim_notes": [
        "Share: triggers OS native share sheet",
        "Save: render receipt as image (screenshot approach) or PDF",
        "Positioned below M-24 SuccessIcon / M-28 TransactionInfoStack"
      ]
    },
    {
      "id": "M-37",
      "name": "CooperativeBadge",
      "shell": "ResultShell",
      "slot": "Cross-Shell",
      "category": "",
      "phase": 3,
      "states": 4,
      "pattern": "HTX identity",
      "data_slot": "coop-badge",
      "sub_slots": [
        "coop-badge-icon",
        "coop-badge-text"
      ],
      "mockup": "mockups/m37_softtoken.png",
      "context": {
        "problem": "Co-opBank là ngân hàng hợp tác xã — identity này vắng bóng trong transfer flow. REC-03 Emotional: Belonging score 2/5. Cần branding subtile.",
        "trigger": "V2-11 REC-03 — cooperative identity missing",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này tạo nhận diện hợp tác xã subtle trên receipt — tăng belonging score.",
        "primary_goal": "",
        "personas": "",
        "context_of_use": "",
        "principles": "",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Logo nhỏ + \"Giao dịch qua Co-opBank\" = subtle bran...",
        "description": "Logo nhỏ + \"Giao dịch qua Co-opBank\" = subtle branding, không intrusive. 2 position variants (on_receipt, in_header).",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": ""
      },
      "evidence": [],
      "sim_notes": [
        "Logo: Co-opBank SVG icon, 16×16px",
        "Priority: Phase 3 (nice-to-have, not critical path)"
      ]
    },
    {
      "id": "M-38",
      "name": "AmountLimitDisplay",
      "shell": "InitShell (below AmountInput M-10)",
      "slot": "Cross-Shell",
      "category": "",
      "phase": 1,
      "states": 9,
      "pattern": "Limit helper",
      "data_slot": "amount-limit",
      "sub_slots": [
        "amount-limit-min",
        "amount-limit-max",
        "amount-limit-source"
      ],
      "mockup": "mockups/m38_transactionlimitwarning.png",
      "context": {
        "problem": "IT-03 AI Review: \"Amount validation mentions min/max but no specific limits defined for user\". User nhập amount rồi mới biết \"vượt hạn mức\" — frustrating.",
        "trigger": "V2-18 IT-03 — missing explicit limits",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp người dùng biết hạn mức trước khi nhập số tiền khi bắt đầu nhập amount ở InitShell.",
        "primary_goal": "Proactive limit display → prevent amount errors before they happen",
        "personas": "",
        "context_of_use": "",
        "principles": "",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Limit-as-Guide",
        "description": "\"Tối thiểu: 10,000₫ · Tối đa: 500,000,000₫ · theo hạn mức tài khoản\" = 3 lines helper text. 2 limitType (per_transaction, daily) show different limits.",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": ""
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "IT-03 AI Review: limits undefined",
          "source": "07-validate/"
        },
        {
          "type": "🔍",
          "claim": "CONFLICT-RESOLUTION.md: M-38↔M-10 integration resolved",
          "source": "insight-validation/"
        }
      ],
      "sim_notes": [
        "Limits: fetched from server per account selected (M-01)",
        "Dynamic: highlight red when amount approaches limit (>90%)",
        "Positioned as helper text below M-10 AmountInput"
      ]
    },
    {
      "id": "M-39",
      "name": "SmartRedirectBanner",
      "shell": "InitShell",
      "slot": "Smart UX (below DestinationFields)",
      "category": "🔁 SHARED (SF2,3,6)",
      "phase": 3,
      "states": 5,
      "pattern": "Auto-detect",
      "data_slot": "smart-redirect",
      "sub_slots": [
        "smart-redirect-icon",
        "smart-redirect-text",
        "smart-redirect-cta",
        "smart-redirect-dismiss"
      ],
      "mockup": "mockups/m39_scrollbudgetguard.png",
      "context": {
        "problem": "User nhập thẻ Co-opBank trong SF2 (liên ngân hàng) → phí cao hơn cần thiết. Hệ thống detect thẻ nội bộ và gợi ý chuyển sang SF5 (cùng chủ, miễn phí).",
        "trigger": "ENTITY-REGISTRY E-58, E-62, E-63 — smart routing entities detected",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp người dùng tiết kiệm phí bằng cách redirect sang flow phù hợp hơn khi hệ thống detect thông tin người nhận là internal.",
        "primary_goal": "Proactive fee optimization — suggest cheaper path",
        "personas": "",
        "context_of_use": "",
        "principles": "#1 Trust First (bank cares about user money) · #3 Clarity",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Proactive Savings Nudge",
        "description": "Non-blocking banner (không bắt buộc redirect) cho user quyền chọn. 3 redirectType: internal_card (→SF5), same_owner (→SF5), same_phone (→SF6 merge). Dismiss = user consciously chooses expensive path.",
        "core_pattern": "Contextual Suggestion Banner (Google Smart Reply)",
        "behavioral": "",
        "differentiation": "",
        "state_machine": "3 redirectType × 2 visibility = 6 → 5 canonical"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "ENTITY-REGISTRY: E-58 internal card, E-62 same owner, E-63 same phone",
          "source": "insight-validation/"
        },
        {
          "type": "🏦",
          "claim": "Toss: smart redirect → 12% fee savings for users",
          "source": "Competitive analysis"
        }
      ],
      "sim_notes": [
        "Detection: after M-03/M-04 query returns → check if receiver is Co-opBank",
        "Non-blocking: banner below form, does NOT prevent form submission",
        "Dismiss: persists for session, not permanent"
      ]
    },
    {
      "id": "M-40",
      "name": "BlacklistWarning",
      "shell": "InitShell",
      "slot": "Smart UX (inline within M-14)",
      "category": "🔁 SHARED (SF2,3,4,5,6)",
      "phase": 2,
      "states": 4,
      "pattern": "Content filter",
      "data_slot": "blacklist-warning",
      "sub_slots": [
        "blacklist-warning-icon",
        "blacklist-warning-text",
        "blacklist-warning-suggestion"
      ],
      "mockup": "mockups/m40_conflictresolutiondialog.png",
      "context": {
        "problem": "Nội dung chuyển tiền có thể chứa từ cấm (blacklist SBV) — hiện tại không có validation cho đến submit → server reject → user confused.",
        "trigger": "ENTITY-REGISTRY E-39 — content blacklist entity",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp người dùng biết và sửa từ cấm trước khi submit khi nhập nội dung chuyển tiền.",
        "primary_goal": "Prevent server rejection bằng inline warning + fix suggestion",
        "personas": "",
        "context_of_use": "",
        "principles": "#4 State Completeness · #1 Trust First",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Fix-Not-Block",
        "description": "Warning + suggested replacement thay vì block hoàn toàn. User thấy \"Thay '{word}' bằng '{alt}'\" = 1-tap fix thay vì đoán. Progressive approach: warn first, block only if user ignores.",
        "core_pattern": "Inline Validation Warning (Grammarly)",
        "behavioral": "",
        "differentiation": "",
        "state_machine": "2 warningState × 2 hasSuggestion = 4"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "ENTITY-REGISTRY: E-39 content blacklist",
          "source": "insight-validation/"
        },
        {
          "type": "📐",
          "claim": "Grammarly: inline suggestion → 70% acceptance rate",
          "source": "Product Analytics"
        }
      ],
      "sim_notes": [
        "Blacklist: fetched from server, cached locally — check on keypress debounce 500ms",
        "Positioned INSIDE M-14 ContentInput (below textbox, above counter)",
        "hasSuggestion: server provides alt text when possible"
      ]
    },
    {
      "id": "M-41",
      "name": "PhonebookSuggestion",
      "shell": "InitShell",
      "slot": "Smart UX (overlay on M-07)",
      "category": "⭐ SF6 only",
      "phase": 2,
      "states": 4,
      "pattern": "Contact suggest",
      "data_slot": "phonebook-suggestion",
      "sub_slots": [
        "phonebook-suggestion-list",
        "phonebook-suggestion-empty"
      ],
      "mockup": "mockups/m41_entityregistrylookup.png",
      "context": {
        "problem": "SF6 đa người nhận cần nhập phone/account per-person — auto-complete từ device phonebook giảm nhập manual.",
        "trigger": "ENTITY-REGISTRY E-49 — phonebook integration entity",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp người chuyển đa người nhận tìm nhanh người nhận từ danh bạ điện thoại khi bắt đầu nhập phone/name trong SF6.",
        "primary_goal": "Auto-complete from contacts → reduce manual input",
        "personas": "",
        "context_of_use": "",
        "principles": "#2 3-Tap Rule · #3 Clarity",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Device-Native Integration",
        "description": "Access device contacts API → fuzzy match on name/phone → dropdown list. EmptyState khi no match. Privacy: request permission once, cache in session only.",
        "core_pattern": "Auto-complete Dropdown (iOS Contacts, WhatsApp)",
        "behavioral": "",
        "differentiation": "",
        "state_machine": "4 listState (hidden, loading, populated, empty)"
      },
      "evidence": [],
      "sim_notes": [
        "Permission: Contacts API permission prompt on first use",
        "Search: fuzzy match name + phone, debounce 300ms",
        "Privacy: no persistent storage — session cache only"
      ]
    },
    {
      "id": "M-42",
      "name": "ScheduleRestrictionNotice",
      "shell": "InitShell",
      "slot": "Smart UX",
      "category": "⭐ SF8 only",
      "phase": 2,
      "states": 2,
      "pattern": "SF8 notice",
      "data_slot": "schedule-restriction",
      "sub_slots": [
        "schedule-restriction-icon",
        "schedule-restriction-text"
      ],
      "mockup": "mockups/m42_proactivesuggestion.png",
      "context": {
        "problem": "SF8 đặt lịch chỉ hỗ trợ chuyển qua STK — card/phone/GTTT không được phép. User cần biết lý do.",
        "trigger": "ENTITY-REGISTRY E-67 — schedule channel restriction",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp người đặt lịch hiểu tại sao một số option bị disable khi bắt đầu setup SF8.",
        "primary_goal": "Explain restriction → reduce confusion",
        "personas": "",
        "context_of_use": "",
        "principles": "",
        "value_pyramid": ""
      },
      "insight": {
        "title": "ℹ️ inline notice = guidance, NOT error. Tone",
        "description": "informational, not blocking.",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": ""
      },
      "evidence": [],
      "sim_notes": [
        "Visible by default when SF8 flow starts",
        "Can be dismissed but reappears if user tries to select card/phone",
        "Optional \"Tìm hiểu thêm\" link to FAQ"
      ]
    },
    {
      "id": "M-43",
      "name": "ScheduleFilterPanel",
      "shell": "ScheduleListShell",
      "slot": "FilterBar",
      "category": "⭐ SF8 only",
      "phase": 2,
      "states": 9,
      "pattern": "Multi-filter",
      "data_slot": "schedule-filter",
      "sub_slots": [
        "schedule-filter-status",
        "schedule-filter-type",
        "schedule-filter-date",
        "schedule-filter-apply",
        "schedule-filter-reset"
      ],
      "mockup": "mockups/m43_interactionmapoverlay.png",
      "context": {
        "problem": "Schedule management cần filter 5 trạng thái (hoạt động/tạm dừng/hủy/hết hạn/tất cả) + loại CT + date range. Hiện không có filter → user scroll toàn bộ list.",
        "trigger": "ENTITY-REGISTRY E-55 — schedule filter entities",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp người quản lý lịch lọc danh sách schedule nhanh chóng khi mở ScheduleListShell.",
        "primary_goal": "Multi-dimension filter cho schedule list management",
        "personas": "",
        "context_of_use": "",
        "principles": "#3 Clarity · #2 3-Tap Rule",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Collapsible Filter",
        "description": "Panel collapsed by default (SCROLL-BUDGET compliance), expand on tap. Status filter = most used → sits at top. Apply/Reset buttons cho explicit action.",
        "core_pattern": "Collapsible Filter Panel (Shopee, Lazada)",
        "behavioral": "",
        "differentiation": "",
        "state_machine": "5 statusFilter × 2 hasDateRange × 2 filterActive = 20 → 9 canonical"
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "REVISED-ARCHITECTURE.md §4: FilterBar slot defined",
          "source": "insight-validation/"
        },
        {
          "type": "🔍",
          "claim": "SCROLL-BUDGET.md: collapsible requirement",
          "source": "insight-validation/"
        }
      ],
      "sim_notes": [
        "Collapsed by default — save scroll budget",
        "Status filter: radio group (mutually exclusive)",
        "Date range: calendar picker component (reuse from M-20)",
        "Reset: clears all filters to \"Tất cả\" default"
      ]
    },
    {
      "id": "M-44",
      "name": "ScheduleStatusBadge",
      "shell": "ScheduleListShell",
      "slot": "ScheduleList (per-item)",
      "category": "⭐ SF8 only",
      "phase": 2,
      "states": 4,
      "pattern": "Color-coded",
      "data_slot": "schedule-status-badge",
      "sub_slots": [
        "schedule-status-badge-dot",
        "schedule-status-badge-text"
      ],
      "mockup": "mockups/m44_statepruningindicator.png",
      "context": {
        "problem": "Mỗi schedule item cần status badge color-coded — user scan list nhanh bằng color recognition.",
        "trigger": "ENTITY-REGISTRY E-54 — schedule status entity",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp người dùng nhận diện trạng thái schedule ngay tức thì khi scan danh sách schedule.",
        "primary_goal": "",
        "personas": "",
        "context_of_use": "",
        "principles": "",
        "value_pyramid": ""
      },
      "insight": {
        "title": "4-color encoding",
        "description": "🟢 Active · 🟡 Paused · 🔴 Cancelled · ⚫ Expired. Color + text + dot = triple encoding for A11Y.",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": ""
      },
      "evidence": [],
      "sim_notes": [
        "A11Y: color + text + dot shape (triple encoding)",
        "Inline badge — sits inside ScheduleListItem",
        "Tap badge does nothing — tap entire item for details"
      ]
    },
    {
      "id": "M-45",
      "name": "ScheduleActionDialog",
      "shell": "ScheduleListShell",
      "slot": "ActionOverlay",
      "category": "⭐ SF8 only",
      "phase": 2,
      "states": 5,
      "pattern": "Destructive confirm",
      "data_slot": "schedule-action",
      "sub_slots": [
        "schedule-action-overlay",
        "schedule-action-content",
        "schedule-action-confirm",
        "schedule-action-cancel"
      ],
      "mockup": "mockups/m45_trustladderindicator.png",
      "context": {
        "problem": "Schedule actions (pause/resume/cancel) cần confirmation dialog — đặc biệt cancel là destructive action cần double-confirm.",
        "trigger": "ENTITY-REGISTRY E-68 — schedule action entities",
        "problem_space": "",
        "origin": "",
        "predecessor": ""
      },
      "intent": {
        "quote": "Molecule này giúp người dùng xác nhận action nguy hiểm trước khi thực hiện khi quản lý schedule (tạm dừng/tiếp tục/hủy).",
        "primary_goal": "Prevent accidental destructive actions via confirmation",
        "personas": "",
        "context_of_use": "",
        "principles": "",
        "value_pyramid": ""
      },
      "insight": {
        "title": "Destructive Differentiation",
        "description": "Cancel = red button, destructive style. Pause/Resume = default style, less alarming. Visual weight matches action severity.",
        "core_pattern": "",
        "behavioral": "",
        "differentiation": "",
        "state_machine": ""
      },
      "evidence": [
        {
          "type": "🔍",
          "claim": "REVISED-ARCHITECTURE.md: ActionOverlay slot defined",
          "source": "insight-validation/"
        },
        {
          "type": "📐",
          "claim": "Material Design: destructive actions need confirmation",
          "source": "Design Guidelines"
        }
      ],
      "sim_notes": [
        "Cancel action: red destructive button + \"Bạn không thể hoàn tác\" warning",
        "Pause/Resume: default button, no destructive warning",
        "Dialog overlay: dims background, blocks interaction"
      ]
    }
  ],
  "inventory": [
    {
      "version": "v2.0",
      "added": 38,
      "total": 38
    },
    {
      "version": "v2.1",
      "added": 7,
      "total": 45
    }
  ]
};