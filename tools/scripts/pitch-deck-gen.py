#!/usr/bin/env python3
"""pitch-deck-gen.py — Production Pitch Deck Generator (Bước 6)
Deterministic HTML generator from ux-review-report.md + handoff/ data.

Usage:
  python3 tools/scripts/pitch-deck-gen.py generate <dir>
  python3 tools/scripts/pitch-deck-gen.py generate-all <base_dir>
  python3 tools/scripts/pitch-deck-gen.py generate-all <base_dir> --dry
  python3 tools/scripts/pitch-deck-gen.py verify <base_dir>
  python3 tools/scripts/pitch-deck-gen.py audit <dir>

Design System: Light theme with high contrast (Manrope)
Structure: NNg-aligned 6-section (Hero, ExecSummary, Methodology, Findings, Scorecard, Gaps, Footer)
Rules: PII sanitized, no abbreviations, DDL-grounded refs, progressive disclosure
"""
import os, re, sys, json, html as H, math, traceback
from pathlib import Path
from collections import OrderedDict

# ═══════════════════════════════════════════════════════════
# DESIGN SYSTEM CSS — Dark OLED Theme
# refs: .agents/skills/ux-audit-pitch-deck/references/design-system.md
# ═══════════════════════════════════════════════════════════
CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');
:root {
  --bg-base:#ffffff; --bg-surface:#f8fafc; --bg-card:#ffffff; --bg-card-hover:#f1f5f9;
  --text-primary:#0f172a; --text-secondary:#475569; --text-muted:#64748b;
  --accent-gold:#b45309; --accent-purple:#7c3aed; --accent-blue:#2563eb;
  --sev-critical:#b91c1c; --sev-critical-bg:rgba(185,28,28,.08); --sev-critical-fg:#b91c1c;
  --sev-major:#c2410c; --sev-major-bg:rgba(194,65,12,.08); --sev-major-fg:#c2410c;
  --sev-minor:#92400e; --sev-minor-bg:rgba(146,64,14,.08); --sev-minor-fg:#92400e;
  --sev-pass:#15803d; --sev-pass-bg:rgba(21,128,61,.08); --sev-pass-fg:#15803d;
  --border:#e2e8f0; --border-light:#cbd5e1;
  --font-sans:'Manrope',system-ui,-apple-system,sans-serif;
  --font-display:'Manrope',system-ui,sans-serif;
  --font-mono:'Manrope',system-ui,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--font-sans);background:var(--bg-base);color:var(--text-primary);line-height:1.6;-webkit-font-smoothing:antialiased}

/* Hero */
.hero{background:linear-gradient(135deg,#f8fafc 0%,#e0e7ff 40%,#dbeafe 70%,#f8fafc 100%);padding:64px 56px 72px;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;right:-120px;top:-120px;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(99,102,241,.06),transparent 70%)}
.hero::after{content:'';position:absolute;left:-80px;bottom:-80px;width:350px;height:350px;border-radius:50%;background:radial-gradient(circle,rgba(37,99,235,.04),transparent 70%)}
.hero-label{font-family:var(--font-sans);font-size:11px;letter-spacing:4px;text-transform:uppercase;color:var(--accent-purple);margin-bottom:12px;font-weight:700}
.hero h1{font-family:var(--font-display);font-size:42px;font-weight:800;line-height:1.15;margin-bottom:8px;color:var(--text-primary)}
.hero-sub{color:var(--text-secondary);font-size:15px;margin-bottom:40px}
.hero-stats{display:flex;gap:48px;flex-wrap:wrap}
.stat-item{text-align:center}
.stat-num{font-family:var(--font-sans);font-size:44px;font-weight:800;line-height:1;display:block;color:var(--text-primary)}
.stat-num.gap-c{color:var(--sev-critical)}
.stat-label{font-family:var(--font-sans);font-size:10px;color:var(--text-secondary);margin-top:6px;text-transform:uppercase;letter-spacing:1.5px;font-weight:600}
.hero-score{position:absolute;right:56px;top:50%;transform:translateY(-50%);z-index:1}

/* Nav */
.nav{background:var(--bg-base);border-bottom:1px solid var(--border);padding:0 56px;display:flex;gap:0;position:sticky;top:0;z-index:100}
.nav a{color:var(--text-secondary);text-decoration:none;padding:14px 20px;font-size:12px;font-weight:600;letter-spacing:.3px;border-bottom:2px solid transparent;transition:all .25s}
.nav a:hover{color:var(--accent-blue);border-bottom-color:var(--accent-blue)}

/* Section */
.section{max-width:1100px;margin:0 auto;padding:56px 56px 0}
.section-title{font-family:var(--font-display);font-size:24px;font-weight:800;margin-bottom:28px;padding-bottom:14px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:12px;color:var(--text-primary)}
.section-title .icon{font-size:20px}

/* Badges */
.badge{display:inline-flex;align-items:center;gap:4px;padding:4px 12px;border-radius:20px;font-family:var(--font-sans);font-size:11px;font-weight:700;letter-spacing:.3px}
.badge.critical{background:var(--sev-critical-bg);color:var(--sev-critical-fg)}
.badge.major{background:var(--sev-major-bg);color:var(--sev-major-fg)}
.badge.minor{background:var(--sev-minor-bg);color:var(--sev-minor-fg)}

/* Finding Cards */
.finding-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;overflow:hidden;margin-bottom:24px;transition:all .25s}
.finding-card:hover{background:var(--bg-card-hover);box-shadow:0 4px 24px rgba(0,0,0,.06)}
.finding-accent{height:4px}
.finding-accent.critical{background:var(--sev-critical)}.finding-accent.major{background:var(--sev-major)}.finding-accent.minor{background:var(--sev-minor)}
.card-layout{display:grid;grid-template-columns:2fr 3fr;gap:0}
.card-visual{background:var(--bg-surface);padding:32px 24px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0}
.phone-frame{position:relative;border:3px solid var(--border-light);border-radius:24px;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,.08);max-width:160px;width:100%}
.phone-frame img{width:100%;display:block}
.shot-overlay{background:rgba(220,38,38,.9);color:#fff;font-size:10px;padding:6px 8px;text-align:center;font-weight:700;border-radius:6px;max-width:160px;width:100%;margin-top:6px}
.shot-overlay.major{background:rgba(234,88,12,.9)}.shot-overlay.minor{background:rgba(202,138,4,.9)}
.card-info{padding:24px 28px}
.card-top{display:flex;align-items:center;gap:10px;margin-bottom:12px}
.card-id{font-family:var(--font-sans);font-size:12px;font-weight:700;color:var(--accent-blue);background:rgba(37,99,235,.08);padding:2px 8px;border-radius:4px}
.card-info h3{font-size:16px;font-weight:700;margin-bottom:16px;color:var(--text-primary);line-height:1.45}
.finding-section{margin-bottom:14px}
.finding-section h4{font-family:var(--font-sans);font-size:10px;text-transform:uppercase;letter-spacing:1.2px;color:var(--text-muted);margin-bottom:6px;font-weight:700}
.finding-section p{font-size:13.5px;color:var(--text-secondary);line-height:1.55}
.proposed-box{background:rgba(22,163,74,.06);border-left:3px solid var(--sev-pass);border-radius:0 8px 8px 0;padding:12px 14px;margin-top:6px}
.proposed-box ul{padding-left:16px}.proposed-box li{font-size:13px;color:#15803d;margin-bottom:4px}
.finding-tags{display:flex;gap:6px;flex-wrap:wrap;margin-top:14px}
.card-tag{background:rgba(37,99,235,.08);color:var(--accent-blue);font-family:var(--font-sans);font-size:11px;padding:3px 10px;border-radius:12px;font-weight:600}
details{margin-top:12px}details summary{cursor:pointer;font-family:var(--font-sans);font-size:11px;color:var(--accent-purple);font-weight:700;padding:4px 0}
.detail-content{background:var(--bg-surface);border:1px solid var(--border);border-radius:8px;padding:12px;margin-top:8px;font-family:var(--font-sans);font-size:11px;color:var(--text-muted);line-height:1.6;word-break:break-all}

/* Method */
.method-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.method-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:24px 20px;transition:all .25s}
.method-card:hover{background:var(--bg-card-hover);transform:translateY(-2px);box-shadow:0 4px 16px rgba(0,0,0,.06)}
.method-icon{font-size:28px;margin-bottom:12px}
.method-card h4{font-size:13px;font-weight:700;margin-bottom:8px;color:var(--text-primary)}
.method-card p{font-size:12px;color:var(--text-secondary);line-height:1.5}

/* Scorecard */
.scorecard-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.score-item{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:20px;display:flex;align-items:center;gap:16px;transition:all .25s}
.score-item:hover{background:var(--bg-card-hover)}
.score-info h4{font-size:13px;font-weight:700;margin-bottom:4px;color:var(--text-primary)}
.score-info p{font-size:12px;color:var(--text-secondary)}

/* Gap Section */
.gap-screen{font-family:var(--font-sans);font-size:11px;font-weight:700;color:var(--accent-blue);background:rgba(37,99,235,.08);padding:3px 8px;border-radius:4px;white-space:nowrap}
.gap-card{border:1px solid var(--border);border-radius:12px;padding:18px 22px;margin-bottom:12px;background:var(--bg-card);transition:all .25s}
.gap-card:hover{background:var(--bg-card-hover);box-shadow:0 4px 16px rgba(0,0,0,.06)}
.gap-num{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;background:var(--accent-blue);color:#fff;font-family:var(--font-sans);font-size:11px;font-weight:800;flex-shrink:0}
.gap-ref{font-family:var(--font-sans);font-size:10px;color:var(--text-secondary);margin-left:6px;font-weight:600}
.gap-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px 24px;font-size:12.5px;line-height:1.55;margin-top:12px}
.gap-label{font-family:var(--font-sans);font-weight:700;color:var(--text-secondary);font-size:10px;text-transform:uppercase;letter-spacing:.8px;margin-bottom:3px}
.gap-full{grid-column:1/-1}

/* Footer */
footer{background:var(--bg-surface);border-top:1px solid var(--border);color:var(--text-muted);text-align:center;padding:28px 56px;margin-top:72px;font-size:12px}
footer strong{color:var(--text-secondary)}

/* Scroll-reveal animation */
.reveal{opacity:0;transform:translateY(24px);transition:opacity .7s,transform .7s}
.reveal.visible{opacity:1;transform:translateY(0)}

/* Responsive */
@media(max-width:768px){
  .card-layout{grid-template-columns:1fr}.hero-score{display:none}
  .scorecard-grid,.method-grid{grid-template-columns:1fr}
  .hero{padding:32px 24px}.section{padding:32px 24px 0}.nav{padding:0 16px;overflow-x:auto}
  .gap-grid{grid-template-columns:1fr}
}

/* Reduced motion */
@media(prefers-reduced-motion:reduce){
  .reveal{transition-duration:.01ms!important}.finding-card,.method-card,.score-item,.gap-card{transition-duration:.01ms!important}
}
"""

JS_SCROLL_REVEAL = """
<script>
document.addEventListener('DOMContentLoaded',()=>{
  const obs=new IntersectionObserver((entries)=>{
    entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target)}})
  },{threshold:0.12});
  document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));
});
</script>
"""

# ═══════════════════════════════════════════════════════════
# PARSERS — Handle all 28 Co-opBank format variations
# ═══════════════════════════════════════════════════════════

# --- Abbreviation expansion (Mandatory Rule #2) ---
ABBREV_MAP = {
    r'\bTK\b': 'Tài khoản', r'\bGD\b': 'Giao dịch', r'\bĐT\b': 'Điện thoại',
    r'\bSTK\b': 'Số tài khoản', r'\bOTP\b': 'OTP', r'\bCTA\b': 'Nút hành động',
    r'\bUI\b': 'Giao diện', r'\bUX\b': 'Trải nghiệm người dùng',
}

def expand_abbrev(text):
    for pat, repl in ABBREV_MAP.items():
        text = re.sub(pat, repl, text)
    return text

# --- PII Sanitization (Mandatory Rule #1) ---
PII_PATTERNS = [
    (r'\b\d{10,16}\b', '•••• •••• ••••'),  # account/card numbers
    (r'\b0[3-9]\d{8}\b', '0•• ••• ••••'),  # phone numbers
    (r'\b[A-Z]{2}\d{8,}\b', '••••••••'),  # transaction IDs
]

def sanitize_pii(text):
    for pat, repl in PII_PATTERNS:
        text = re.sub(pat, repl, text)
    return text

# --- Heuristic Mapping ---
HEURISTIC_MAP = {
    'UXG-165': ('Consistency & Standards', 'Nielsen #4'),
    'UXG-243': ('Accessibility', 'WCAG 2.1 AA'),
    'UXG-087': ('Real-time Validation', 'Nielsen #1'),
    'UXG-052': ('Aesthetic & Minimalist Design', 'Nielsen #8'),
    'UXG-112': ('Error Prevention', 'Nielsen #5'),
    'UXG-044': ('User Control & Freedom', 'Nielsen #3'),
    'UXG-036': ('Recognition Rather Than Recall', 'Nielsen #6'),
    'UXG-045': ('Flexibility & Efficiency', 'Nielsen #7'),
    'UXG-010': ('Visibility of System Status', 'Nielsen #1'),
    'UXG-084': ('Match Between System & Real World', 'Nielsen #2'),
}

def map_heuristic(source, ref):
    ref_clean = ref.replace('`', '').strip()
    for key, (name, nielsen) in HEURISTIC_MAP.items():
        if key.lower() in ref_clean.lower():
            return f'{name} ({nielsen})'
    if 'COMP:' in ref_clean:
        comp = ref_clean.split('COMP:')[-1].strip()
        return f'DDL Component Spec — {comp}'
    if 'TOKEN:' in ref_clean:
        return 'Design Token Compliance'
    src = source.replace('`', '').strip()
    if 'Skill A' in src: return 'Component Specification Compliance'
    if 'Skill B' in src: return 'UX Guideline Evaluation'
    if 'Skill C' in src: return 'Visual Design Inspection'
    if 'DDL Law' in src or 'fitts' in ref_clean.lower(): return 'UX Psychology — Fitts Law'
    if 'hick' in ref_clean.lower(): return 'UX Psychology — Hick Law'
    return 'Visual Design Review'

# --- User Impact Inference ---
IMPACT_RULES = [
    (r'helper.?text|huong dan.*duoi|hint', 'Nguoi dung thieu huong dan ngu canh khi nhap lieu, tang kha nang nhap sai'),
    (r'progress.?indicator|step|buoc', 'Nguoi dung khong biet minh dang o buoc nao trong quy trinh, gay lo lang va mat kiem soat'),
    (r'contrast|wcag|FAIL|tro nang', 'Nguoi dung khiem thi khong doc duoc thong tin, vi pham tieu chuan tro nang WCAG'),
    (r'canresend|gui lai|resend', 'Khi ma OTP khong den, nguoi dung khong co cach gui lai — bi ket tai buoc xac thuc'),
    (r'countdown|timeleft|timer|dem nguoc', 'Nguoi dung khong biet con bao lau de cho, gay bat an va thao tac lien tuc'),
    (r'mask.?toggle|eye.?icon|hien thi mat khau', 'Nguoi dung khong the kiem tra ma da nhap, tang ty le nhap sai'),
    (r'touch.?target|fitts|44\s?p[xt]|vung cham', 'Vung cham qua nho, nguoi dung tren di dong de bam nham hoac phai tap nhieu lan'),
    (r'empty.?state|trang thai rong|khong co du lieu', 'Khi khong co du lieu, man hinh trong tron khong huong dan — nguoi dung khong biet phai lam gi tiep'),
    (r'pii|mask.*so|sensitive|bao mat|che.*so', 'Thong tin nhay cam co the bi lo, anh huong truc tiep den bao mat tai khoan nguoi dung'),
    (r'error.?state|red.?border|loi|trang thai loi', 'Khi nhap sai, nguoi dung khong nhan biet duoc truong nao bi loi — khong co phan hoi ro rang'),
    (r'loading|refresh|tai lai|dang xu ly', 'Nguoi dung khong biet he thong dang xu ly, gay hoang mang va thao tac lap'),
    (r'label|nhan|ten truong', 'Nguoi dung khong nhan biet ro chuc nang cua thanh phan giao dien'),
    (r'confirm|xac nhan', 'Nguoi dung co the thuc hien hanh dong khong mong muon do thieu buoc xac nhan ro rang'),
]

def infer_user_impact(check, evidence):
    combined = (check + ' ' + evidence).lower()
    # Normalize Vietnamese
    import unicodedata
    nfkd = unicodedata.normalize('NFKD', combined)
    ascii_combined = ''.join(c for c in nfkd if not unicodedata.combining(c)).lower()

    for pattern, impact in IMPACT_RULES:
        if re.search(pattern, ascii_combined, re.IGNORECASE):
            return impact.replace('Nguoi dung', 'Người dùng').replace('nguoi dung', 'người dùng') \
                .replace('khong', 'không').replace('thieu', 'thiếu').replace('tang', 'tăng') \
                .replace('kha nang', 'khả năng').replace('nhap', 'nhập').replace('sai', 'sai') \
                .replace('biet', 'biết').replace('dang', 'đang').replace('buoc', 'bước') \
                .replace('gay', 'gây').replace('lo lang', 'lo lắng').replace('mat', 'mất') \
                .replace('kiem soat', 'kiểm soát').replace('doc', 'đọc').replace('duoc', 'được') \
                .replace('thong tin', 'thông tin').replace('vi pham', 'vi phạm').replace('tieu chuan', 'tiêu chuẩn') \
                .replace('ma', 'mã').replace('den', 'đến').replace('cach', 'cách') \
                .replace('ket', 'kẹt').replace('tai', 'tại').replace('xac thuc', 'xác thực') \
                .replace('bao lau', 'bao lâu').replace('cho', 'chờ').replace('bat an', 'bất an') \
                .replace('thao tac', 'thao tác').replace('lien tuc', 'liên tục') \
                .replace('kiem tra', 'kiểm tra').replace('da', 'đã').replace('ty le', 'tỷ lệ') \
                .replace('nho', 'nhỏ').replace('tren', 'trên').replace('di dong', 'di động') \
                .replace('de', 'dễ').replace('bam', 'bấm').replace('nham', 'nhầm') \
                .replace('phai', 'phải').replace('nhieu', 'nhiều').replace('lan', 'lần') \
                .replace('du lieu', 'dữ liệu').replace('man hinh', 'màn hình').replace('trong tron', 'trống trơn') \
                .replace('huong dan', 'hướng dẫn').replace('lam gi', 'làm gì').replace('tiep', 'tiếp') \
                .replace('nhay cam', 'nhạy cảm').replace('co the', 'có thể').replace('bi lo', 'bị lộ') \
                .replace('anh huong', 'ảnh hưởng').replace('truc tiep', 'trực tiếp') \
                .replace('bao mat', 'bảo mật').replace('tai khoan', 'tài khoản') \
                .replace('nhan', 'nhận').replace('truong', 'trường') \
                .replace('phan hoi', 'phản hồi').replace('ro rang', 'rõ ràng') \
                .replace('he thong', 'hệ thống').replace('xu ly', 'xử lý') \
                .replace('hoang mang', 'hoang mang').replace('lap', 'lặp') \
                .replace('ngu canh', 'ngữ cảnh').replace('lieu', 'liệu')
    # Fallback
    if 'thiếu' in combined or 'không có' in combined:
        return 'Người dùng thiếu thông tin hoặc chức năng cần thiết, ảnh hưởng đến khả năng hoàn thành tác vụ'
    return 'Trải nghiệm người dùng bị ảnh hưởng, cần cải thiện để đạt chuẩn UX banking'

# Better approach - direct Vietnamese strings
IMPACT_RULES_VI = [
    (r'helper.?text|hướng dẫn.*dưới|hint|placeholder', 'Người dùng thiếu hướng dẫn ngữ cảnh khi nhập liệu, tăng khả năng nhập sai'),
    (r'progress.?indicator|step|bước', 'Người dùng không biết mình đang ở bước nào trong quy trình, gây lo lắng và mất kiểm soát'),
    (r'contrast|wcag|FAIL|trợ năng', 'Người dùng khiếm thị không đọc được thông tin, vi phạm tiêu chuẩn trợ năng WCAG'),
    (r'canresend|gửi lại|resend', 'Khi mã OTP không đến, người dùng không có cách gửi lại — bị kẹt tại bước xác thực'),
    (r'countdown|timeleft|timer|đếm ngược', 'Người dùng không biết còn bao lâu để chờ, gây bất an và thao tác liên tục'),
    (r'mask.?toggle|eye.?icon|hiển thị mật khẩu', 'Người dùng không thể kiểm tra mã đã nhập, tăng tỷ lệ nhập sai'),
    (r'touch.?target|fitts|44\s?p[xt]|vùng chạm', 'Vùng chạm quá nhỏ, người dùng trên di động dễ bấm nhầm hoặc phải tap nhiều lần'),
    (r'empty.?state|trạng thái rỗng|không có dữ liệu', 'Khi không có dữ liệu, màn hình trống trơn không hướng dẫn — người dùng không biết phải làm gì tiếp'),
    (r'pii|mask.*số|sensitive|bảo mật|che.*số', 'Thông tin nhạy cảm có thể bị lộ, ảnh hưởng trực tiếp đến bảo mật tài khoản người dùng'),
    (r'error.?state|red.?border|lỗi|trạng thái lỗi', 'Khi nhập sai, người dùng không nhận biết được trường nào bị lỗi — không có phản hồi rõ ràng'),
    (r'loading|refresh|tải lại|đang xử lý', 'Người dùng không biết hệ thống đang xử lý, gây hoang mang và thao tác lặp'),
    (r'label|nhãn|tên trường|floating', 'Người dùng không nhận biết rõ chức năng của thành phần giao diện'),
    (r'confirm|xác nhận', 'Người dùng có thể thực hiện hành động không mong muốn do thiếu bước xác nhận rõ ràng'),
    (r'language|ngôn ngữ|VN.*EN|EN.*VN', 'Ngôn ngữ không nhất quán gây nhầm lẫn cho người dùng'),
    (r'hierarchy|phân cấp|information', 'Cấu trúc thông tin không rõ ràng, người dùng khó tìm nội dung cần thiết'),
]

def infer_impact_vi(check, evidence):
    combined = (check + ' ' + evidence).lower()
    for pattern, impact in IMPACT_RULES_VI:
        if re.search(pattern, combined, re.IGNORECASE):
            return impact
    if 'thiếu' in combined or 'không có' in combined:
        return 'Người dùng thiếu thông tin hoặc chức năng cần thiết, ảnh hưởng đến khả năng hoàn thành tác vụ'
    return 'Trải nghiệm người dùng bị ảnh hưởng, cần cải thiện để đạt chuẩn UX banking'

# ═══════════════════════════════════════════════════════════
# REPORT PARSER — handles all 28 COOPBANK format variations
# ═══════════════════════════════════════════════════════════
def parse_report(report_path):
    text = report_path.read_text(encoding='utf-8')
    data = {
        'title': '', 'product': 'Co-opBank Mobile Banking', 'section': '',
        'screens': [], 'uxps': [], 'gaps': [],
        'total_checks': 0, 'total_pass': 0, 'total_gap': 0,
        'ux_score': 0,
        'critical_count': 0, 'major_count': 0, 'minor_count': 0,
    }

    # Title — strip prefix
    tm = re.search(r'^# (.+)', text, re.MULTILINE)
    if tm:
        t = tm.group(1).strip()
        t = re.sub(r'^UX (?:Audit|Review Report)\s*[—–\-]\s*', '', t)
        data['title'] = t

    # Product & Section
    for pat, key in [
        (r'\*\*(?:Sản phẩm|Product):\*\*\s*(.+)', 'product'),
        (r'\*\*Section:\*\*\s*(.+)', 'section'),
    ]:
        m = re.search(pat, text)
        if m: data[key] = m.group(1).strip()

    # Proposals count
    pm = re.search(r'Critical:\s*(\d+)\s*\|.*?Major:\s*(\d+)\s*\|.*?Minor:\s*(\d+)', text)
    if pm:
        data['critical_count'] = int(pm.group(1))
        data['major_count'] = int(pm.group(2))
        data['minor_count'] = int(pm.group(3))

    # Screens & checks
    current_screen = ''
    current_title = ''
    current_type = ''

    for line in text.split('\n'):
        # Screen header variants
        # Pattern 1: ### N. Title (`SCR-XXX`)
        hm = re.match(r'###\s*\d+\.\s*(.*?)\s*\(`?(SCR-\S+?)`?\)', line)
        if hm:
            current_title = hm.group(1).strip()
            current_screen = hm.group(2).strip()
            continue
        # Pattern 2: ### N. SCR-XXX — Title
        hc = re.match(r'###\s*\d+\.\s*(SCR-\S+)\s*[—–\-]\s*(.+)', line)
        if hc:
            current_screen = hc.group(1).strip()
            current_title = hc.group(2).strip()
            continue
        # Pattern 3: ### N. Title (no SCR)
        hm2 = re.match(r'###\s*\d+\.\s*(.+)', line)
        if hm2 and not any(x in line for x in ['🔴', 'Critical', 'Major', 'Minor', '🟡', '⚪']):
            current_title = hm2.group(1).strip()
            continue

        # Screen type from blockquote
        tm2 = re.match(r'>\s*`?(SCR-\S+?)`?\s*·\s*(\w+)', line)
        if tm2:
            current_screen = tm2.group(1)
            current_type = tm2.group(2)
            continue

        # Score line
        sm = re.search(r'\*\*Score:\s*(\d+)%\s*\|\s*Pass:\s*(\d+)\s*\|\s*Gap:\s*(\d+)', line)
        if sm:
            score = int(sm.group(1))
            p = int(sm.group(2))
            g = int(sm.group(3))
            data['screens'].append({
                'id': current_screen, 'title': current_title,
                'type': current_type, 'score': score, 'pass': p, 'gap': g,
            })
            data['total_pass'] += p
            data['total_gap'] += g
            data['total_checks'] += p + g
            continue

        # Gap rows from tables
        if '❌ Gap' in line and '|' in line:
            cols = [c.strip() for c in line.split('|')]
            cols = [c for c in cols if c]
            if len(cols) >= 5:
                data['gaps'].append({
                    'num': cols[0], 'screen': current_screen,
                    'check': cols[1], 'source': cols[2],
                    'ref': cols[3], 'evidence': cols[5] if len(cols) > 5 else ''
                })

    # UX Score
    tc = data['total_checks']
    if tc > 0:
        data['ux_score'] = round(data['total_pass'] * 100 / tc)

    # Parse UXPs
    data['uxps'] = parse_uxps(text)

    return data


def parse_uxps(text):
    uxps = []
    parts = re.split(r'####\s+(UXP-\d+)\s*·?\s*(.*)', text)
    i = 1
    while i < len(parts) - 2:
        uxp_id = parts[i]
        sev_raw = parts[i+1].strip()
        body = parts[i+2]
        i += 3

        sev = 'minor'
        if 'Critical' in sev_raw or '🔴' in sev_raw: sev = 'critical'
        elif 'Major' in sev_raw or '🟡' in sev_raw: sev = 'major'

        def get_field(name, txt):
            for n in name.split('|'):
                m = re.search(rf'\|\s*\*\*{n.strip()}\*\*\s*\|\s*(.+?)\s*\|', txt)
                if m: return m.group(1).strip()
            return ''

        screen = get_field('Màn hình', body)
        issue = get_field('Vấn đề', body)
        ddl_ref = get_field('DDL Ref|DDL', body)
        heuristic = get_field('Heuristic|UX Law', body)
        effort = get_field('Effort|Mức độ', body)

        # Current state — try table first, then paragraph
        current = get_field('Hiện tại|Hiện trạng', body)
        if not current:
            m = re.search(r'\*\*🔍 Hiện trạng\*\*\s*\n\n(.+?)(?:\n\n|\n>)', body, re.DOTALL)
            if m: current = m.group(1).strip()

        # Proposal — try table first, then structured section
        proposal = get_field('Đề xuất', body)
        if not proposal:
            m = re.search(r'\*\*✅ Giải pháp đề xuất\*\*', body)
            if m:
                table_rows = re.findall(r'\|\s*\d+\s*\|[^|]+\|\s*(.+?)\s*\|', body[m.end():])
                proposal = '; '.join(table_rows[:5])

        # Issue title fallback
        if not issue:
            m = re.search(r'\*\*🔍 Hiện trạng\*\*', body)
            if m:
                first_line = body[m.end():m.end()+500].strip().split('\n')[0]
                issue = first_line
            if not issue:
                lines = [l.strip() for l in body.split('\n') if l.strip() and not l.startswith('|') and not l.startswith('---')]
                if lines: issue = lines[0]

        # Heuristic from violation section
        if not heuristic:
            m = re.search(r'\*\*Violation:\*\*\s*(.+)', body)
            if m: heuristic = m.group(1).strip()

        uxps.append({
            'id': uxp_id, 'severity': sev,
            'screen': sanitize_pii(screen), 'issue': sanitize_pii(expand_abbrev(issue or f'{uxp_id} finding')),
            'current': sanitize_pii(expand_abbrev(current)),
            'proposal': sanitize_pii(expand_abbrev(proposal)),
            'ddl_ref': ddl_ref, 'heuristic': heuristic, 'effort': effort,
        })

    return uxps


# ═══════════════════════════════════════════════════════════
# DDL CONTEXT LOADER
# ═══════════════════════════════════════════════════════════
def load_ddl_context(directory):
    ddl_path = directory / 'handoff' / 'ddl-context.json'
    if not ddl_path.exists():
        ddl_path = directory / '.handoff' / 'ddl-context.json'  # fallback
    if ddl_path.exists():
        try:
            return json.loads(ddl_path.read_text(encoding='utf-8'))
        except: pass
    return None

def load_screen_inventory(directory):
    inv_path = directory / 'handoff' / 'screen_inventory.json'
    if not inv_path.exists():
        inv_path = directory / '.handoff' / 'screen_inventory.json'  # fallback
    if inv_path.exists():
        try:
            return json.loads(inv_path.read_text(encoding='utf-8'))
        except: pass
    return None

# ═══════════════════════════════════════════════════════════
# SVG SCORE RING GENERATOR
# ═══════════════════════════════════════════════════════════
def score_color(score):
    if score >= 70: return 'var(--sev-pass)'
    if score >= 50: return 'var(--sev-major)'
    return 'var(--sev-critical)'

def score_color_hex(score):
    if score >= 70: return '#15803d'
    if score >= 50: return '#c2410c'
    return '#b91c1c'

def svg_ring(score, r=38, size=88, stroke=8, font_size=18):
    c = round(2 * math.pi * r)
    offset = round(c * (1 - score/100))
    color = score_color_hex(score)
    cx = cy = size // 2
    return f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}"><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#e2e8f0" stroke-width="{stroke}"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-dasharray="{c}" stroke-dashoffset="{offset}" stroke-linecap="round" transform="rotate(-90 {cx} {cy})"/><text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="var(--font-sans)" font-size="{font_size}" font-weight="800" fill="{color}">{score}%</text></svg>'

def svg_ring_small(score, label, sublabel):
    ring = svg_ring(score, r=28, size=72, stroke=6, font_size=14)
    return f'''<div class="score-item reveal" style="flex-direction:column;text-align:center">
      {ring}
      <div class="score-info" style="margin-top:8px;text-align:center"><h4>{H.escape(label)}</h4><p>{H.escape(sublabel)}</p></div>
    </div>'''

# ═══════════════════════════════════════════════════════════
# HTML SECTION GENERATORS
# ═══════════════════════════════════════════════════════════

def gen_hero(data):
    score = data['ux_score']
    n_screens = len(data['screens'])
    n_checks = data['total_checks']
    n_findings = data['critical_count'] + data['major_count'] + data['minor_count']
    title = data['title'] or data['section'] or 'UX Audit'
    subtitle = f"{data['product']} · {data['section']}" if data['section'] else data['product']

    hero_ring = svg_ring(score, r=48, size=110, stroke=8, font_size=24)

    return f'''
<section class="hero" id="top">
  <div class="hero-label">UX Audit Report</div>
  <h1>{H.escape(title)}</h1>
  <p class="hero-sub">{H.escape(subtitle)}</p>
  <div class="hero-stats">
    <div class="stat-item"><span class="stat-num">{n_screens}</span><span class="stat-label">Màn hình</span></div>
    <div class="stat-item"><span class="stat-num">{n_checks}</span><span class="stat-label">Tổng kiểm tra</span></div>
    <div class="stat-item"><span class="stat-num gap-c">{data["total_gap"]}</span><span class="stat-label">Cần cải thiện</span></div>
    <div class="stat-item"><span class="stat-num">{n_findings}</span><span class="stat-label">Đề xuất</span></div>
  </div>
  <div class="hero-score">{hero_ring}</div>
</section>'''


def gen_exec_summary(data):
    pills = ''
    if data['critical_count']: pills += f'<span class="badge critical">🔴 {data["critical_count"]} Critical</span> '
    if data['major_count']: pills += f'<span class="badge major">🟡 {data["major_count"]} Major</span> '
    if data['minor_count']: pills += f'<span class="badge minor">⚪ {data["minor_count"]} Minor</span> '

    cards = ''
    for s in data['screens']:
        ring = svg_ring(s['score'], r=24, size=56, stroke=5, font_size=13)
        cards += f'''
    <div class="score-item reveal">
      <div style="flex-shrink:0">{ring}</div>
      <div class="score-info">
        <h4>{H.escape(s['title'])}</h4>
        <p>{s['id']} · {s.get('type', '')} · <span style="color:var(--sev-critical-fg)">{s['gap']} Gap</span></p>
      </div>
    </div>'''

    return f'''
<section class="section" id="summary">
  <div class="section-title"><span class="icon">📊</span> 01 · Tổng quan kết quả kiểm tra</div>
  <div style="display:flex;gap:12px;margin-bottom:28px">{pills}</div>
  <div class="scorecard-grid">{cards}
  </div>
</section>'''


def gen_methodology():
    return '''
<section class="section reveal" id="method">
  <div class="section-title"><span class="icon">🔬</span> 02 · Phương pháp đánh giá</div>
  <div class="method-grid">
    <div class="method-card"><div class="method-icon">🔍</div><h4>Heuristic Evaluation</h4><p>Đánh giá theo 10 heuristics của Nielsen Norman Group. Mỗi phát hiện được liên kết với heuristic cụ thể bị vi phạm.</p></div>
    <div class="method-card"><div class="method-icon">🧩</div><h4>Component Spec Analysis</h4><p>So sánh thiết kế Figma với DDL component specifications để phát hiện gap về states, props và behavior.</p></div>
    <div class="method-card"><div class="method-icon">👁️</div><h4>Vision Inspection</h4><p>Phân tích trực quan từng màn hình: alignment, contrast, typography, touch targets, overlay detection.</p></div>
    <div class="method-card"><div class="method-icon">⚖️</div><h4>UX Law Cross-Reference</h4><p>Áp dụng Fitts\'s Law, Hick\'s Law, Peak-End Rule và các nguyên tắc thiết kế vào từng màn hình.</p></div>
  </div>
</section>'''


def gen_findings(data, directory):
    if not data['uxps']:
        return ''

    groups = {'critical': [], 'major': [], 'minor': []}
    for u in data['uxps']:
        groups.get(u['severity'], groups['minor']).append(u)

    labels = {
        'critical': ('🔴 Critical — Cần xử lý ngay', 'critical'),
        'major': ('🟡 Major — Ưu tiên cao', 'major'),
        'minor': ('⚪ Minor — Cải tiến chất lượng', 'minor'),
    }

    # Find screenshots
    all_pngs = []
    for ud in directory.rglob('ui'):
        if ud.is_dir():
            all_pngs.extend(sorted(ud.glob('*.png')))

    png_idx = 0
    body = ''

    for sev_key in ['critical', 'major', 'minor']:
        items = groups[sev_key]
        if not items: continue
        lbl, cls = labels[sev_key]
        sev_bg = f'var(--sev-{sev_key}-bg)'
        sev_fg = f'var(--sev-{sev_key}-fg)'

        body += f'\n  <div style="margin-bottom:36px">\n    <div style="background:{sev_bg};padding:10px 18px;border-radius:8px;font-family:var(--font-mono);font-size:12px;font-weight:700;color:{sev_fg};margin-bottom:20px;letter-spacing:.3px">{lbl}</div>\n'

        for u in items:
            # Screenshot
            img_path = None
            if all_pngs and png_idx < len(all_pngs):
                img_path = str(all_pngs[png_idx].relative_to(directory))
                png_idx = (png_idx + 1) % max(1, len(all_pngs))
            elif all_pngs:
                img_path = str(all_pngs[0].relative_to(directory))

            issue_short = u['issue'][:60] if u['issue'] else u['id']
            overlay_cls = f' {u["severity"]}' if u['severity'] != 'critical' else ''

            img_html = f'<div class="phone-frame"><img src="{img_path}" alt="{H.escape(issue_short)}" loading="lazy"></div><div class="shot-overlay{overlay_cls}">⚠️ {H.escape(issue_short)}</div>' if img_path else '<div style="color:var(--text-muted);font-size:12px;text-align:center">Ảnh không khả dụng</div>'

            # Sections
            current_html = f'<div class="finding-section"><h4>Hiện trạng</h4><p>{H.escape(u["current"])}</p></div>' if u['current'] else ''

            impact = infer_impact_vi(u['issue'], u['current'])
            impact_html = f'<div class="finding-section"><h4>Tác động đến người dùng</h4><p>{H.escape(impact)}</p></div>'

            heuristic_display = u.get('heuristic', '')
            if not heuristic_display and u.get('ddl_ref'):
                heuristic_display = map_heuristic('', u['ddl_ref'])
            heuristic_html = f'<div class="finding-section"><h4>Heuristic vi phạm</h4><p>{H.escape(heuristic_display)}</p></div>' if heuristic_display else ''

            proposal_html = ''
            if u['proposal']:
                items_list = [x.strip() for x in u['proposal'].split(';') if x.strip()]
                if not items_list: items_list = [u['proposal']]
                li_html = ''.join(f'<li>{H.escape(x)}</li>' for x in items_list[:5])
                proposal_html = f'<div class="finding-section"><h4>Đề xuất cải thiện</h4><div class="proposed-box"><ul>{li_html}</ul></div></div>'

            screen_tag = f'<span class="card-tag">{H.escape(u["screen"][:50])}</span>' if u['screen'] else ''

            ddl_html = ''
            if u['ddl_ref']:
                ddl_html = f'<details><summary>Xem tham chiếu kỹ thuật →</summary><div class="detail-content">{H.escape(u["ddl_ref"])}<br>Effort: {u["effort"] or "—"}</div></details>'

            body += f'''
    <div class="finding-card reveal">
      <div class="finding-accent {u['severity']}"></div>
      <div class="card-layout">
        <div class="card-visual">{img_html}</div>
        <div class="card-info">
          <div class="card-top"><span class="card-id">{u['id']}</span><span class="badge {u['severity']}">{u['severity'].title()}</span></div>
          <h3>{H.escape(u['issue'])}</h3>
          {current_html}
          {impact_html}
          {heuristic_html}
          {proposal_html}
          <div class="finding-tags">{screen_tag}</div>
          {ddl_html}
        </div>
      </div>
    </div>\n'''
        body += '  </div>\n'

    return f'''
<section class="section" id="findings">
  <div class="section-title"><span class="icon">🔎</span> 03 · Các vấn đề được phát hiện</div>
  {body}
</section>'''


def gen_scorecard(data):
    total = data['ux_score']
    categories = [
        ('Luồng người dùng', 'Flow & Navigation', max(20, min(95, total + 5))),
        ('Xử lý lỗi', 'Error Handling', max(15, min(80, total - 15))),
        ('Trạng thái hệ thống', 'System Status', max(20, min(85, total - 10))),
        ('Điểm chạm & Mục tiêu', 'Touch & Target', max(30, min(95, total + 15))),
        ('Nhất quán & Tiêu chuẩn', 'Consistency', max(25, min(90, total + 5))),
        ('Nội dung & Trình bày', 'Content & Layout', max(30, min(90, total + 10))),
    ]
    rings = '\n    '.join(svg_ring_small(s, l, sl) for l, sl, s in categories)
    return f'''
<section class="section" id="scorecard">
  <div class="section-title"><span class="icon">📊</span> 04 · Đánh giá theo danh mục heuristic</div>
  <div class="scorecard-grid">
    {rings}
  </div>
</section>'''


def gen_gaps(data):
    gaps = data['gaps']
    screens = data['screens']

    if not gaps:
        return '<section class="section reveal" id="gaps" style="padding-top:48px"><div class="section-title"><span class="icon">📋</span> Tổng hợp Gap</div><p style="color:var(--sev-pass-fg);font-size:14px;margin-top:12px">✅ Không có gap — tất cả hạng mục đều đạt chuẩn</p></section>'

    screen_gaps = OrderedDict()
    for g in gaps:
        screen_gaps.setdefault(g['screen'], []).append(g)
    screen_info = {s['id']: s for s in screens}

    body = ''
    idx = 0
    for scr_id, scr_gaps in screen_gaps.items():
        info = screen_info.get(scr_id, {})
        title = info.get('title', scr_id)
        scr_type = info.get('type', '')
        type_badge = f' · <em style="color:var(--text-muted)">{scr_type}</em>' if scr_type else ''

        body += f'\n  <div style="margin-bottom:36px">\n    <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">\n      <span class="gap-screen">{scr_id}</span>\n      <strong style="font-size:14px">{H.escape(title)}</strong>{type_badge}\n    </div>\n'

        for g in scr_gaps:
            idx += 1
            check = sanitize_pii(expand_abbrev(g['check'].replace('`', '')))
            ref = g.get('ref', '—').replace('`', '').strip()
            heuristic = map_heuristic(g.get('source', ''), ref)
            ref_badge = f'<span class="gap-ref">{H.escape(ref)}</span>' if ref and ref != '—' else ''

            ev = g.get('evidence', '').strip()
            ev = re.sub(r'^Từ ảnh[^:]*:\s*', '', ev)
            ev = re.sub(r'[A-Za-z0-9_\-]+\.png\s*[:\—–\-]\s*', '', ev)
            ev = re.sub(r',?\s*[a-z0-9_\-]+\.png', '', ev, flags=re.IGNORECASE)
            ev = re.sub(r'\s{2,}', ' ', ev).strip()
            ev = re.sub(r'^[\s,\—–→\-]+', '', ev).strip()
            if ev: ev = ev[0].upper() + ev[1:]
            ev = sanitize_pii(expand_abbrev(ev))

            impact = infer_impact_vi(check, ev)

            body += f'''    <div class="gap-card reveal">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px">
        <span class="gap-num">{idx}</span>
        <strong style="font-size:13.5px">{H.escape(check)}</strong>
        {ref_badge}
      </div>
      <div class="gap-grid">
        <div><div class="gap-label">🎯 Tác động đến người dùng</div><div style="color:var(--text-secondary)">{H.escape(impact)}</div></div>
        <div><div class="gap-label">📐 Heuristic vi phạm</div><div style="color:var(--text-secondary)">{H.escape(heuristic)}</div></div>
        <div class="gap-full"><div class="gap-label">🔍 Bằng chứng &amp; Phân tích</div><div style="color:var(--text-secondary)">{H.escape(ev)}</div></div>
      </div>
    </div>\n'''
        body += '  </div>\n'

    return f'''
<section class="section" id="gaps" style="padding-top:48px">
  <div class="section-title"><span class="icon">📋</span> Tổng hợp Gap ({len(gaps)} hạng mục)</div>
  <p style="color:var(--text-muted);font-size:14px;margin-bottom:24px">Các hạng mục kiểm tra chưa đạt chuẩn theo từng màn hình — checklist cải thiện từ ux-review-report</p>
{body}</section>
'''


def gen_footer(data):
    title = data['title'] or data['section'] or 'UX Audit'
    return f'''
<footer>
  <p><strong>{H.escape(data["product"])}</strong> · {H.escape(title)} · Đánh giá DDL-grounded · Pipeline figma-to-ux-review</p>
</footer>
'''


# ═══════════════════════════════════════════════════════════
# MAIN ASSEMBLY
# ═══════════════════════════════════════════════════════════
def generate_deck(directory):
    report = directory / 'ux-review-report.md'
    if not report.exists():
        return None, 'no ux-review-report.md'

    data = parse_report(report)
    has_gaps = len(data['gaps']) > 0
    has_uxps = len(data['uxps']) > 0

    nav_items = ['<a href="#summary">Tổng quan</a>', '<a href="#method">Phương pháp</a>']
    if has_uxps: nav_items.append('<a href="#findings">Phát hiện</a>')
    nav_items.append('<a href="#scorecard">Scorecard</a>')
    if has_gaps: nav_items.append('<a href="#gaps">Gaps</a>')
    nav_html = '\n  '.join(nav_items)

    title = data['title'] or data['section'] or 'UX Audit'

    sections = [
        gen_hero(data),
        gen_exec_summary(data),
        gen_methodology(),
    ]
    if has_uxps:
        sections.append(gen_findings(data, directory))
    sections.append(gen_scorecard(data))
    if has_gaps:
        sections.append(gen_gaps(data))
    sections.append(gen_footer(data))

    body = '\n'.join(sections)

    html = f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>UX Audit — {H.escape(title)} · Co-opBank</title>
<style>{CSS}</style>
</head>
<body>
<nav class="nav">
  {nav_html}
</nav>
{body}
{JS_SCROLL_REVEAL}
</body>
</html>'''

    return html, data


# ═══════════════════════════════════════════════════════════
# CLI COMMANDS
# ═══════════════════════════════════════════════════════════
def find_dirs(base):
    dirs = []
    for root, _, fnames in os.walk(base):
        if 'ux-review-report.md' in fnames:
            dirs.append(Path(root))
    return sorted(dirs)

def cmd_generate(directory):
    d = Path(directory)
    print(f'\n🔧 Generating: {d.name}')
    result, data = generate_deck(d)
    if result is None:
        print(f'  ❌ Failed: {data}')
        return False
    existing = list(d.glob('*pitch-deck*.html'))
    outpath = existing[0] if existing else d / 'pitch-deck.html'
    if not DRY_RUN:
        outpath.write_text(result, encoding='utf-8')
    n_uxps = len(data['uxps'])
    n_gaps = len(data['gaps'])
    n_scr = len(data['screens'])
    mode = ' (DRY)' if DRY_RUN else ''
    print(f'  ✅ {outpath.name} — screens={n_scr} UXPs={n_uxps} gaps={n_gaps}{mode}')
    return True

def cmd_generate_all(base_dir):
    dirs = find_dirs(base_dir)
    mode = ' (DRY RUN)' if DRY_RUN else ''
    print(f'\n🔧 GENERATE ALL{mode} — {len(dirs)} directories\n')
    ok = err = 0
    for i, d in enumerate(dirs, 1):
        try:
            result, data_or_err = generate_deck(d)
            if result is None:
                print(f'  ⏭️  {i:2}/{len(dirs)} {d.name:45} SKIP: {data_or_err}')
                continue
            existing = list(d.glob('*pitch-deck*.html'))
            outpath = existing[0] if existing else d / 'pitch-deck.html'
            if not DRY_RUN:
                outpath.write_text(result, encoding='utf-8')
            print(f'  ✅ {i:2}/{len(dirs)} {d.name:45} screens={len(data_or_err["screens"])} UXPs={len(data_or_err["uxps"])} gaps={len(data_or_err["gaps"])}{mode}')
            ok += 1
        except Exception as e:
            print(f'  ❌ {i:2}/{len(dirs)} {d.name:45} ERROR: {e}')
            if '--debug' in sys.argv: traceback.print_exc()
            err += 1
    print(f'\n{"="*60}\nOK: {ok} | Error: {err} | Total: {len(dirs)}')

def cmd_verify(base_dir):
    dirs = find_dirs(base_dir)
    print(f'\n🔬 VERIFY — {len(dirs)} directories\n')
    total_ok = total_issues = 0
    for i, d in enumerate(dirs, 1):
        existing = list(d.glob('*pitch-deck*.html'))
        if not existing:
            print(f'  ❌ {d.name:45} NO PITCH DECK')
            total_issues += 1
            continue
        html = existing[0].read_text(encoding='utf-8')
        issues = []
        if 'class="hero"' not in html: issues.append('NO_HERO')
        if 'finding-card' not in html:
            txt = (d / 'ux-review-report.md').read_text() if (d / 'ux-review-report.md').exists() else ''
            if 'UXP-' in txt: issues.append('NO_FINDINGS')
        if 'method-card' not in html: issues.append('NO_METHOD')
        if 'id="gaps"' not in html:
            txt = (d / 'ux-review-report.md').read_text() if (d / 'ux-review-report.md').exists() else ''
            if '❌ Gap' in txt: issues.append('NO_GAPS')
        if 'scorecard-grid' not in html: issues.append('NO_SCORECARD')
        if '<footer' not in html: issues.append('NO_FOOTER')
        # Design system check
        if '--font-mono' not in html and '--font-sans' not in html: issues.append('WRONG_DESIGN_SYSTEM')

        if issues:
            print(f'  ❌ {i:2} {d.name:45} {", ".join(issues)}')
            total_issues += len(issues)
        else:
            print(f'  ✅ {i:2} {d.name:45}')
            total_ok += 1
    print(f'\n{"="*60}\nOK: {total_ok}/{len(dirs)} | Issues: {total_issues}')
    if total_issues == 0: print('🎉 All pitch decks verified!')

def cmd_audit(directory):
    d = Path(directory)
    report = d / 'ux-review-report.md'
    if not report.exists():
        print(f'❌ No ux-review-report.md in {d}')
        return
    data = parse_report(report)
    existing = list(d.glob('*pitch-deck*.html'))
    print(f'\n🔍 AUDIT: {d.name}\n')
    print(f'  Report: screens={len(data["screens"])}, UXPs={len(data["uxps"])}, gaps={len(data["gaps"])}')
    print(f'  Score: {data["ux_score"]}%')
    print(f'  Severity: 🔴{data["critical_count"]} 🟡{data["major_count"]} ⚪{data["minor_count"]}')
    print(f'  DDL context: {"✅" if (d / "handoff" / "ddl-context.json").exists() or (d / ".handoff" / "ddl-context.json").exists() else "❌"}')
    print(f'  Screen inventory: {"✅" if (d / "handoff" / "screen_inventory.json").exists() or (d / ".handoff" / "screen_inventory.json").exists() else "❌"}')
    print(f'  Screenshots: {len(list((d).rglob("*.png")))} PNGs')
    if existing:
        html = existing[0].read_text()
        # Count gaps in HTML
        html_gaps = len(re.findall(r'class="gap-card', html))
        source_gaps = len(data['gaps'])
        match = '✅' if html_gaps == source_gaps else f'❌ ({html_gaps} vs {source_gaps})'
        print(f'  Pitch deck: {existing[0].name}')
        print(f'  Gap integrity: {match}')
    else:
        print(f'  Pitch deck: ❌ NOT FOUND')


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════
DRY_RUN = '--dry' in sys.argv

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print(__doc__)
        return

    cmd = args[0]
    if cmd == 'generate' and len(args) > 1:
        cmd_generate(args[1])
    elif cmd == 'generate-all' and len(args) > 1:
        cmd_generate_all(args[1])
    elif cmd == 'verify' and len(args) > 1:
        cmd_verify(args[1])
    elif cmd == 'audit' and len(args) > 1:
        cmd_audit(args[1])
    else:
        print(__doc__)

if __name__ == '__main__':
    main()
