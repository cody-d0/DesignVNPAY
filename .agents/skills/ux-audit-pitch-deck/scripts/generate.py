#!/usr/bin/env python3
"""generate.py — Generic UX Audit Pitch Deck Generator

Usage:
  python3 generate.py --report PATH --output PATH [options]

Options:
  --report PATH       ux-review-report.md file path (required)
  --output PATH       Output HTML file path (required)
  --ui-dir PATH       Directory containing UI screenshots (default: {report_dir}/*/ui/)
  --product TEXT      Product name (default: extracted from report)
  --client TEXT       Client name (default: extracted from report)
  --module TEXT       Module name (default: extracted from report)
  --template PATH     Custom template HTML (default: bundled)
  --dry               Preview only, no write
"""
import argparse, json, os, re, sys, unicodedata
from typing import Any
import html as html_mod
from pathlib import Path


def vn_normalize(text):
    """Normalize Vietnamese text to ASCII for fuzzy matching."""
    text = unicodedata.normalize('NFD', text.lower())
    # Remove combining diacritical marks
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    # Handle đ/Đ which NFD doesn't decompose
    text = text.replace('đ', 'd').replace('Đ', 'D')
    return text


def vn_to_slug(text):
    """Convert Vietnamese text to URL-safe ASCII slug."""
    text = vn_normalize(text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text


def auto_output_name(report_path):
    """Generate pitch deck filename from folder hierarchy.
    Example: .../Dịch vụ thẻ/Kích hoạt thẻ/ux-review-report.md
             → dich-vu-the--kich-hoat-the--pitch-deck.html
    """
    folder = report_path.parent
    # Use up to 2 parent levels for unique naming
    parts = []
    current = folder
    for _ in range(2):
        parts.insert(0, current.name)
        current = current.parent
        # Stop if we hit a root-like dir (e.g. 'final', 'output', project root)
        if current.name.lower() in ('final', 'output', 'out', '') or current == current.parent:
            break
    slug = '--'.join(vn_to_slug(p) for p in parts)
    return f'{slug}--pitch-deck.html'


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
TEMPLATE_PATH = SKILL_DIR / 'assets' / 'template.html'

_FALLBACK_CSS = """
/* Minimal fallback CSS when template.html is not available */
:root {
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
  --bg: #fff; --surface: #f8fafc; --border: #e2e8f0;
  --text: #0f172a; --text-secondary: #475569; --text-muted: #94a3b8;
  --sev-critical-bg: #fef2f2; --sev-critical-fg: #b91c1c;
  --sev-major-bg: #fffbeb; --sev-major-fg: #c2410c;
  --sev-minor-bg: #f8fafc; --sev-minor-fg: #64748b;
}
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:var(--font-sans); color:var(--text); background:var(--bg);
  line-height:1.6; max-width:1100px; margin:0 auto; padding:24px; }
h1 { font-size:28px; font-weight:800; }
h3 { font-size:16px; margin-bottom:8px; }
h4 { font-size:13px; color:var(--text-secondary); margin-bottom:4px; }
p { font-size:14px; color:var(--text-secondary); }
.section { padding:32px 0; border-top:1px solid var(--border); }
.section-title { font-size:18px; font-weight:700; margin-bottom:20px; }
.icon { margin-right:6px; }
.hero { text-align:center; padding:48px 0 32px; }
.hero-label { font-size:11px; text-transform:uppercase; letter-spacing:2px; color:var(--text-muted); }
.hero-sub { font-size:14px; color:var(--text-secondary); margin-top:4px; }
.hero-stats { display:flex; justify-content:center; gap:32px; margin:24px 0; }
.stat-item { text-align:center; }
.stat-num { display:block; font-size:28px; font-weight:800; }
.stat-label { font-size:11px; color:var(--text-muted); }
.hero-score { margin:16px auto; }
.badge { display:inline-block; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:600; }
.badge.critical { background:var(--sev-critical-bg); color:var(--sev-critical-fg); }
.badge.major { background:var(--sev-major-bg); color:var(--sev-major-fg); }
.badge.minor { background:var(--sev-minor-bg); color:var(--sev-minor-fg); }
.nav { position:sticky; top:0; background:rgba(255,255,255,.95); backdrop-filter:blur(8px);
  padding:10px 0; display:flex; gap:16px; z-index:100; border-bottom:1px solid var(--border); }
.nav a { font-size:12px; color:var(--text-secondary); text-decoration:none; font-weight:500; }
.nav a:hover { color:var(--text); }
.scorecard-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(200px,1fr)); gap:16px; }
.score-item { display:flex; align-items:center; gap:12px; padding:16px;
  background:var(--surface); border-radius:12px; border:1px solid var(--border); }
.score-info h4 { font-size:13px; color:var(--text); font-weight:600; }
.score-info p { font-size:12px; color:var(--text-muted); margin:0; }
.method-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); gap:16px; }
.method-card { padding:20px; background:var(--surface); border-radius:12px;
  border:1px solid var(--border); }
.method-icon { font-size:24px; margin-bottom:8px; }
.method-card h4 { font-size:14px; margin-bottom:6px; }
.method-card p { font-size:12px; }
.finding-card { background:var(--surface); border-radius:12px; border:1px solid var(--border);
  overflow:hidden; margin-bottom:20px; }
.finding-accent { height:4px; }
.finding-accent.critical { background:var(--sev-critical-fg); }
.finding-accent.major { background:var(--sev-major-fg); }
.finding-accent.minor { background:var(--sev-minor-fg); }
.card-layout { display:grid; grid-template-columns:200px 1fr; gap:20px; padding:20px; }
.phone-frame { width:180px; border-radius:16px; overflow:hidden; border:2px solid var(--border); }
.phone-frame img { width:100%; display:block; }
.shot-overlay { font-size:11px; color:var(--text-muted); padding:6px 0; text-align:center; }
.card-top { display:flex; align-items:center; gap:8px; margin-bottom:8px; }
.card-id { font-family:var(--font-mono); font-size:11px; font-weight:700; color:var(--text-muted); }
.finding-section { margin-bottom:12px; }
.finding-section h4 { font-size:11px; text-transform:uppercase; letter-spacing:.5px;
  color:var(--text-muted); margin-bottom:2px; }
.finding-section p { font-size:13px; }
.finding-tags { display:flex; gap:6px; margin-top:8px; }
.card-tag { font-size:10px; padding:2px 8px; background:var(--border); border-radius:6px; }
.proposed-box { background:#f0fdf4; border-left:3px solid #16a34a; padding:8px 12px;
  border-radius:0 8px 8px 0; margin-top:8px; }
.proposed-box ul { margin:0; padding-left:16px; }
.proposed-box li { font-size:12px; color:#166534; }
details { margin-top:8px; }
summary { font-size:11px; color:var(--text-muted); cursor:pointer; }
.detail-content { font-size:11px; color:var(--text-muted); padding:6px 0; font-family:var(--font-mono); }
.gap-c { color:var(--sev-critical-fg); }
.gap-card { background:var(--surface); border:1px solid var(--border); border-radius:10px;
  padding:16px; margin-bottom:12px; }
.gap-num { display:inline-flex; align-items:center; justify-content:center; width:24px; height:24px;
  background:var(--border); border-radius:6px; font-size:11px; font-weight:700; }
.gap-screen { font-family:var(--font-mono); font-size:11px; padding:2px 8px; background:#EFF6FF;
  color:#2563EB; border-radius:4px; font-weight:600; }
.gap-grid { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:8px; }
.gap-full { grid-column:1/-1; }
.gap-label { font-size:11px; font-weight:600; color:var(--text-muted); margin-bottom:2px; }
.gap-ref { font-family:var(--font-mono); font-size:10px; padding:1px 6px; background:#F5F3FF;
  color:#7C3AED; border-radius:4px; }
footer { text-align:center; padding:32px 0; color:var(--text-muted); font-size:12px;
  border-top:1px solid var(--border); }
.reveal { opacity:0; transform:translateY(16px); transition:opacity .5s,transform .5s; }
.reveal.visible { opacity:1; transform:none; }
@media(max-width:768px) {
  .card-layout { grid-template-columns:1fr; }
  .gap-grid { grid-template-columns:1fr; }
  .hero-stats { flex-wrap:wrap; gap:16px; }
}
"""

# ═══════════════════════════════════════════════════════════
# i18n — Vietnamese labels for all UI elements
# ═══════════════════════════════════════════════════════════

I18N_VI = {
    # Section labels
    'DDL Reference': 'Tham chiếu DDL',
    'Component Spec': 'Thông số thành phần',

    # Heuristic categories (top-level)
    'Accessibility': 'Tiếp cận',
    'Cognitive': 'Nhận thức',
    'Motor': 'Vận động',
    'Behavioral': 'Hành vi',
    'Unknown': 'Chưa phân loại',

    # Heuristic sub-categories (from enriched gap labels)
    'Animation': 'Chuyển động',
    'Forms': 'Biểu mẫu',
    'Feedback': 'Phản hồi',
    'Interaction': 'Tương tác',
    'Process': 'Quy trình',
    'State': 'Trạng thái',
    'Touch': 'Điểm chạm',
    'Typography': 'Kiểu chữ',
    'Performance': 'Hiệu suất',
    'AI Interaction': 'Tương tác AI',

    # Heuristic sub-category patterns (full match)
    'Loading States': 'Trạng thái tải',
    'Loading Indicators': 'Chỉ báo tải',
    'Loading Buttons': 'Nút đang tải',
    'Input Labels': 'Nhãn trường nhập',
    'Inline Errors': 'Lỗi trực tiếp',
    'Never Block Paste': 'Không chặn dán',
    'Submit Feedback': 'Phản hồi khi gửi',
    'Confirm Destructive Actions': 'Xác nhận hành động nguy hiểm',
    'Touch Target Size': 'Kích thước vùng chạm',
    'Contrast Readability': 'Độ tương phản chữ',
    'Image Optimization': 'Tối ưu hình ảnh',
    'Design Based on Understanding (ISO 9241-210)': 'Thiết kế dựa trên hiểu biết (ISO 9241-210)',
    'Color Only': 'Chỉ dùng màu',
    'Alt Text': 'Văn bản thay thế',
    'Icon Button Labels': 'Nhãn nút biểu tượng',
    'Disclaimer': 'Tuyên bố miễn trừ',
    'Phản hồi lỗi': 'Phản hồi lỗi',

    # Heuristic name patterns
    'Consistency & Standards': 'Nhất quán & Tiêu chuẩn',
    'WCAG AA Contrast': 'Tương phản WCAG AA',
    'Error Prevention': 'Phòng ngừa lỗi',
    'Error Feedback': 'Phản hồi lỗi',
    'User Control & Freedom': 'Kiểm soát & Tự do người dùng',
    'Aesthetic & Minimalist Design': 'Thiết kế tối giản & Thẩm mỹ',
    'Real-time Validation Feedback': 'Phản hồi xác thực thời gian thực',
    'ARIA Labels (WCAG)': 'Nhãn ARIA (WCAG)',
    "Fitts's Law": 'Định luật Fitts',
    "Hick's Law": 'Định luật Hick',
    'Zeigarnik Effect': 'Hiệu ứng Zeigarnik',
    "Miller's Law": 'Định luật Miller',
    "Jakob's Law": 'Định luật Jakob',

    # Gap title fragments (EN → VI)
    'spec:': 'thông số:',
    'helper_text below input field': 'gợi ý (helper text) bên dưới trường nhập',
    'helper_text': 'gợi ý (helper text)',
    'mask_toggle': 'toggle hiện/ẩn',
    'canResend state': 'trạng thái gửi lại OTP',
    'canResend': 'gửi lại OTP',
    'timeLeft countdown timer': 'bộ đếm ngược thời gian OTP',
    'timeLeft': 'đếm ngược thời gian',
    'real-time validation': 'xác thực thời gian thực',
    'realtime_validation': 'xác thực thời gian thực',
    'eye icon': 'icon hiện/ẩn',
    'attempt counter': 'bộ đếm số lần thử',
    'lockout warning': 'cảnh báo khóa tài khoản',
    'visual affordance': 'tín hiệu trực quan',
    'show/hide toggle': 'nút hiện/ẩn',
    'show/hide PIN': 'hiện/ẩn mã PIN',
    'show/hide': 'hiện/ẩn',
    'touch targets': 'vùng chạm',
    'step dots': 'chấm tiến trình',
    'Progress indicator': 'Thanh tiến trình',
    'inline error': 'lỗi inline',
    'Error strategy': 'Chiến lược xử lý lỗi',
    'Error state': 'Trạng thái lỗi',
    'Information architecture': 'Kiến trúc thông tin',
    'Badge contrast': 'Tương phản badge',
    'CTA label': 'Nhãn nút hành động',
    'Security': 'Bảo mật',
    'Zeigarnik Effect compliance': 'tuân thủ hiệu ứng Zeigarnik',
    'empty state': 'trạng thái rỗng',
    'Empty State': 'Trạng thái rỗng',
    'Product Context': 'Bối cảnh sản phẩm',
    'Security-first': 'Ưu tiên bảo mật',
    'Confirm': 'Xác nhận',
    'Success': 'Thành công',

    # Component names
    'otp-input-1': 'nhập OTP',
    'text-input-1': 'trường nhập văn bản',
    'step-indicator-1': 'thanh tiến trình',
    'countdown-timer-1': 'bộ đếm ngược',
    'empty-state-1': 'trạng thái rỗng',
    'password-strength-1': 'độ mạnh mật khẩu',
    'receipt-preview-1': 'xem trước biên lai',

    'Layout': 'Bố cục',
    'Navigation': 'Điều hướng',
    'Content Jumping': 'Nội dung nhảy',
    'Back Button': 'Nút quay lại',

    # Gap label fragments discovered by audit
    'Minimum': 'Tối thiểu',
    'Target': 'Mục tiêu',
    'Keyboard': 'Bàn phím',
    'Heuristic': 'Heuristic',
    'Doherty Threshold': 'Ngưỡng Doherty',
    'loading-spinner-1': 'vòng tải',

    # DDL evidence patterns
    'DDL Component Spec': 'Thông số thành phần DDL',
    'DDL component spec': 'Thông số thành phần DDL',
    'defines this capability. Current implementation missing required feature.':
        'yêu cầu tính năng này. Thiết kế hiện tại chưa triển khai.',
    'DDL guideline': 'Nguyên tắc DDL',
    'Component:': 'Thành phần:',
}


def translate_label(text: str) -> str:
    """Translate a label/tag to Vietnamese using I18N_VI dict."""
    if not text:
        return text
    # Exact match first
    if text in I18N_VI:
        return I18N_VI[text]
    # Partial replacement
    result = text
    for en, vi in sorted(I18N_VI.items(), key=lambda x: -len(x[0])):
        if en in result:  # type: ignore[operator]
            result = result.replace(en, vi)  # type: ignore[union-attr]
    return result


def translate_gap_title(title: str) -> str:
    """Translate gap title to Vietnamese, preserving technical identifiers."""
    if not title:
        return title
    result = title
    # Apply longest-match-first replacements
    for en, vi in sorted(I18N_VI.items(), key=lambda x: -len(x[0])):
        if en in result:  # type: ignore[operator]
            result = result.replace(en, vi)  # type: ignore[union-attr]
    # Clean up remaining "spec" patterns
    result = re.sub(r'(\w+-\w+-\d+)\s+spec:', r'thông số \1:', result)
    return result


# ═══════════════════════════════════════════════════════════
# REPORT PARSER — 3 format support (A, B, C)
# ═══════════════════════════════════════════════════════════

def parse_gaps(report_path):
    """Parse ux-review-report.md, extract gaps grouped by screen."""
    if not report_path.exists():
        return [], []
    text = report_path.read_text(encoding='utf-8')
    gaps = []
    screens = []
    screen_images = {}
    current_screen = ''
    current_title = ''
    current_type = ''
    current_score = ''
    current_pass = 0
    current_gap = 0
    current_images = []

    for line in text.split('\n'):
        # Screen header format A: ### N. Title (`SCR-XXX-NNN`)
        hm = re.match(r'###\s*\d+\.\s*(.*?)\s*\(`?(SCR-\S+?)`?\)', line)
        if hm:
            current_title = hm.group(1).strip()
            current_screen = hm.group(2).strip()
            current_images = []
            continue

        # Screen header format C: ### N. SCR-XXX — Title
        hc = re.match(r'###\s*\d+\.\s*(SCR-\S+)\s*[—–-]\s*(.+)', line)
        if hc:
            current_screen = hc.group(1).strip()
            current_title = hc.group(2).strip()
            current_images = []
            continue

        # Screen header format B: ### N. Title (no SCR in heading)
        hm2 = re.match(r'###\s*\d+\.\s*(.+)', line)
        if hm2 and not any(line.strip().startswith(f'### {p}') for p in ['🔴', 'Critical', 'Major', 'Minor']):
            current_title = hm2.group(1).strip()
            current_images = []
            continue

        # Screen type: > `SCR-XXX` · type · N artboards
        tm = re.match(r'>\s*`?(SCR-\S+?)`?\s*·\s*(\w+)', line)
        if tm:
            current_screen = tm.group(1)
            current_type = tm.group(2)
            continue

        # Score line: **Score: 44% | Pass: 4 | Gap: 5**
        sm = re.search(r'\*\*Score:\s*(\d+)%\s*\|\s*Pass:\s*(\d+)\s*\|\s*Gap:\s*(\d+)', line)
        if sm:
            current_score = sm.group(1)
            current_pass = int(sm.group(2))
            current_gap = int(sm.group(3))
            img_m = re.search(r'Images?:\s*(.+?)(?:\*\*|\s*$)', line)
            if img_m:
                current_images = re.findall(r'([\w-]+\.png)', img_m.group(1))
            screen_images[current_screen] = current_images
            screens.append({
                'id': current_screen, 'title': current_title,
                'type': current_type, 'score': current_score,
                'pass': current_pass, 'gap': current_gap,
                'images': current_images,
            })
            continue

        # Gap row in table — both hard (❌) and soft (⚠️) gaps
        if ('❌ Gap' in line or '⚠️ Gap' in line) and '|' in line:
            cols = [c.strip() for c in line.split('|')]
            cols = [c for c in cols if c]
            if len(cols) >= 5:
                ev_text = cols[5] if len(cols) > 5 else ''
                ev_imgs = re.findall(r'([\w-]+\.png)', ev_text)
                if not ev_imgs:
                    ev_imgs = screen_images.get(current_screen, [])
                gaps.append({
                    'num': cols[0], 'screen': current_screen,
                    'check': cols[1], 'source': cols[2],
                    'ref': cols[3], 'evidence': ev_text,
                    'images': ev_imgs[:2],  # type: ignore[index]
                })
    return gaps, screens


def map_heuristic(source, ref):
    """Map Source + DDL Ref to human-readable heuristic name."""
    ref_clean = ref.replace('`', '').strip()
    heuristic_map = {
        'UXG-165': 'Consistency & Standards (Nielsen #4)',
        'UXG-243': 'Accessibility — WCAG 2.1 AA',
        'UXG-087': 'Real-time Validation Feedback',
        'UXG-052': 'Aesthetic & Minimalist Design (Nielsen #8)',
        'UXG-112': 'Error Prevention (Nielsen #5)',
        'UXG-044': 'User Control & Freedom (Nielsen #3)',
        'fitts': "Fitts's Law — Touch Target Size",
        'hick': "Hick's Law — Decision Complexity",
        'zeigarnik': 'Zeigarnik Effect — Completion Progress',
        'peak-end': 'Peak-End Rule — Experience Memory',
    }
    for key, val in heuristic_map.items():
        if key.lower() in ref_clean.lower():
            return val
    if 'COMP:' in ref_clean:
        comp_name = ref_clean.split('COMP:')[-1].strip()
        return f'Thông số DDL — {comp_name}'
    if 'TOKEN:' in ref_clean:
        return 'Tuân thủ Design Token'
    source_clean = source.replace('`', '').strip()
    if 'Skill A' in source_clean: return 'Đối chiếu thông số thiết kế'
    if 'Skill B' in source_clean: return 'Đánh giá Heuristic'
    if 'Skill C' in source_clean: return 'Kiểm tra trực quan'
    if 'DDL Law' in source_clean: return 'Nguyên tắc tâm lý UX'
    return 'Nguyên tắc UX'


def infer_user_impact(check, evidence):
    """Infer user impact from check description and evidence text."""
    combined = (check + ' ' + evidence).lower()
    impact_rules = [
        (r'helper.?text|hướng dẫn.*dưới',
         'Người dùng thiếu hướng dẫn ngữ cảnh khi nhập liệu, tăng khả năng nhập sai và tỷ lệ bỏ cuộc'),
        (r'modal.*error|error.*modal|modal.*interrupt|modal.*"thông báo"',
         'Luồng nhập liệu bị gián đoạn bởi popup, người dùng mất focus và phải thao tác thêm để quay lại trường đang nhập'),
        (r'progress.?indicator|step.?indicator|step.?dots|zeigarnik',
         'Người dùng không biết mình đang ở bước nào trong flow, gây lo lắng và tăng tỷ lệ thoát giữa chừng'),
        (r'contrast|wcag|FAIL|badge.*nhạt',
         'Người dùng khiếm thị hoặc trong điều kiện ánh sáng yếu không đọc được thông tin, vi phạm tiêu chuẩn trợ năng'),
        (r'cta.*nhất quán|label.*nhất quán|không nhất quán|terminology.*mismatch',
         'Người dùng bị nhầm lẫn khi cùng một hành động nhưng hiển thị khác nhau giữa các màn hình, tăng cognitive load'),
        (r'canresend|gửi lại|resend',
         'Khi OTP không đến, người dùng không có cách gửi lại mã — bị kẹt tại màn hình xác thực, buộc phải thoát app'),
        (r'countdown|timeleft|timer|track attempt',
         'Người dùng không biết còn bao lâu để chờ hoặc còn bao nhiêu lần thử, gây bất an và thao tác vội vàng'),
        (r'mask.?toggle|eye.?icon|show.?hide|ẩn.?hiện',
         'Người dùng không thể kiểm tra mã PIN/OTP đã nhập, tăng tỷ lệ nhập sai và phải thao tác lại'),
        (r'attempt.?counter|lockout|còn x lần|bị khóa',
         'Người dùng không biết còn bao nhiêu lần thử trước khi bị khóa, gây hoang mang và thao tác vội'),
        (r'real.?time.*validation|real.?time.*feedback|checklist.*dynamic',
         'Người dùng phải đoán xem dữ liệu nhập đã đúng hay chưa, chỉ biết khi submit và nhận lỗi'),
        (r'information.?architecture|lưu ý.*chiếm|block.*height|quá.*%.*height',
         'Nội dung phụ chiếm quá nhiều không gian, đẩy trường nhập liệu chính xuống ngoài tầm nhìn'),
        (r'error.?state|red.?border|visual.?affordance|border.*đỏ',
         'Khi nhập sai, người dùng không nhận biết được trường nào bị lỗi — thiếu tín hiệu thị giác rõ ràng'),
        (r'touch.?target|touch.?area|fitts|44\s?px|48\s?px',
         'Vùng chạm quá nhỏ, người dùng thao tác trên di động dễ bấm nhầm hoặc phải tap nhiều lần'),
        (r'empty.?state|trạng thái rỗng',
         'Khi không có dữ liệu, màn hình trống trơn không hướng dẫn, người dùng không biết phải làm gì tiếp'),
        (r'pii|mask.*số|sensitive|bảo mật|security|blur|readable|shoulder',
         'Thông tin nhạy cảm có thể bị lộ, ảnh hưởng trực tiếp đến bảo mật tài khoản người dùng'),
        (r'popup.*x.*icon|dismiss|escape|không có.*đóng|zero escape',
         'Người dùng không có cách thoát popup, bị kẹt trong trạng thái bắt buộc mà không có lựa chọn'),
        (r'long.?scroll|cuộn|viewport|scroll.*form',
         'Form quá dài buộc người dùng cuộn nhiều, tăng cognitive load và tỷ lệ bỏ cuộc'),
        (r'label.*placeholder|placeholder.*label|không có label|thiếu label',
         'Khi người dùng bắt đầu nhập liệu, placeholder biến mất và không còn gợi ý về trường đang nhập'),
        (r'password.?strength|mật khẩu.*mạnh|strength.?meter',
         'Người dùng không biết mật khẩu đã đủ mạnh chưa, dẫn đến submit fail và phải nhập lại'),
        (r'dropdown|select|picker|chọn',
         'Thao tác chọn không thuận tiện, tăng số bước cần thực hiện để hoàn thành tác vụ'),
    ]
    for pattern, impact in impact_rules:
        if re.search(pattern, combined, re.IGNORECASE):
            return impact
    if 'thiếu' in combined or 'không có' in combined:
        return 'Người dùng thiếu thông tin hoặc chức năng cần thiết, ảnh hưởng đến khả năng hoàn thành tác vụ'
    return 'Trải nghiệm người dùng bị ảnh hưởng, cần cải thiện để đạt chuẩn UX banking'


# ═══════════════════════════════════════════════════════════
# SVG HELPERS
# ═══════════════════════════════════════════════════════════

def score_ring_svg(score, size=110, font_size=24, stroke_width=8):
    """Generate SVG score ring."""
    r = (size - stroke_width) // 2
    cx = cy = size // 2
    circ = 2 * 3.14159 * r
    offset = circ * (1 - score / 100)
    if score >= 70: color = '#15803d'
    elif score >= 50: color = '#c2410c'
    else: color = '#b91c1c'
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#e2e8f0" stroke-width="{stroke_width}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="{stroke_width}" '
            f'stroke-dasharray="{int(circ)}" stroke-dashoffset="{int(offset)}" stroke-linecap="round" '
            f'transform="rotate(-90 {cx} {cy})"/>'
            f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="var(--font-sans)" '
            f'font-size="{font_size}" font-weight="800" fill="{color}">{score}%</text></svg>')


# ═══════════════════════════════════════════════════════════
# TEXT HELPERS
# ═══════════════════════════════════════════════════════════

def smart_title(text, max_len=100):
    """Extract a concise title from hiện_trạng text."""
    text = re.sub(r'^Từ ảnh[^:]*:\s*', '', text.strip())
    text = re.sub(r'\s*\([\w\-., ]*\.png[\w\-., ]*\)', '', text)
    text = re.sub(r'\s*[\w-]+\.png', '', text).strip()
    m = re.match(r'^(.+?)[.:—]\s', text)
    title = m.group(1).strip() if m else text
    title = re.sub(r'^(?:Màn hình|Form|Popup|Trang)\s+', '', title, count=1).strip()
    if title: title = title[0].upper() + title[1:]  # type: ignore[index]
    if len(title) > max_len:
        cut = title[:max_len].rfind(' ')  # type: ignore[index]
        title = title[:cut] + '…' if cut > 50 else title[:max_len] + '…'  # type: ignore[index]
    return title


def overlay_summary(text, max_len=65):
    """Generate concise overlay summary for phone frame."""
    text = re.sub(r'\s*\([\w\-., ]*\.png[\w\-., ]*\)', '', text.strip())
    text = re.sub(r'\s*[\w-]+\.png', '', text).strip()
    m = re.match(r'^(.+?)[.,:—]\s', text)
    summary = m.group(1).strip() if m else text
    summary = re.sub(r'^(?:Màn hình|Form|Popup|Trang|Mục|Banner quảng cáo)\s+', '', summary, count=1).strip()
    if summary: summary = summary[0].upper() + summary[1:]  # type: ignore[index]
    if len(summary) > max_len:
        cut = summary[:max_len].rfind(' ')  # type: ignore[index]
        summary = summary[:cut] + '…' if cut > 30 else summary[:max_len] + '…'  # type: ignore[index]
    return summary


def heuristic_display(ddl, ux_law, violation):
    """Map DDL + UX Law to human-readable heuristic string."""
    # Don't passthrough raw "Check #N" patterns — they're not human-readable
    if violation and not re.match(r'^(?:Check\s*)?#?\d+(?:\s*,\s*#?\d+)*(?:\s*\(SCR-[\w-]+\))?$', violation.strip()):
        return violation.rstrip('.')
    if 'COMP:' in ddl:
        comp_name = ddl.split('COMP:')[-1].strip()
        translated = translate_label(comp_name)
        return f'Thông số DDL — {translated}'
    uxg_map = {
        'UXG-165': 'Nhất quán & Tiêu chuẩn (Nielsen #4)',
        'UXG-243': 'Tiếp cận (WCAG 2.1 AA)',
        'UXG-78': 'Kiểm tra trực quan',
        'UXG-52': 'Kiểm tra trực quan',
        'UXG-087': 'Phản hồi xác thực thời gian thực',
        'UXG-112': 'Phòng ngừa lỗi (Nielsen #5)',
        'UXG-044': 'Kiểm soát & Tự do người dùng (Nielsen #3)',
        'UXG-176': 'Phản hồi lỗi (Nielsen #9)',
    }
    for key, val in uxg_map.items():
        if key in ddl: return val
    law_map = {
        'fitts': "Định luật Fitts — Kích thước vùng chạm",
        'hicks': "Định luật Hick — Độ phức tạp quyết định",
        'peak-end': 'Quy tắc Peak-End — Ký ức trải nghiệm',
        'zeigarnik': 'Hiệu ứng Zeigarnik — Tiến trình hoàn thành',
    }
    if ux_law and ux_law != '—':
        for key, val in law_map.items():
            if key in ux_law.lower(): return val
    return 'Kiểm tra trực quan'


# ═══════════════════════════════════════════════════════════
# SCREEN MD PARSER — Build check→image mapping from screen specs
# ═══════════════════════════════════════════════════════════

def parse_screen_specs(report_dir: Path) -> dict[str, Any]:
    """Parse all screen .md files in report directory.
    Returns: {screen_id: {wireframe_images: [str], states: [{name, desc, keywords}], overlays: [{name, desc, keywords}]}}
    """
    specs: dict[str, Any] = {}
    md_files = [f for f in report_dir.glob('*.md') if f.name != 'ux-review-report.md']

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
        except (UnicodeDecodeError, OSError):
            continue

        # Extract screen_id — supports: **screen_id**: / **Screen ID:** / # SCR-XXX / filename
        scr_m = re.search(r'\*\*(?:screen_id|Screen\s*ID)\*\*:\s*(SCR-[\w-]+)', content, re.IGNORECASE)
        if not scr_m:
            scr_m = re.search(r'^#\s+(SCR-[\w-]+)', content, re.MULTILINE)
        if not scr_m:
            fn_m = re.search(r'(SCR-[\w-]+)', md_file.stem, re.IGNORECASE)
            if fn_m:
                scr_m = fn_m
        if not scr_m:
            continue
        scr_id = scr_m.group(1).upper() if scr_m.group(1)[:3].lower() == 'scr' else scr_m.group(1)

        # Extract wireframe_images — supports: **wireframe_images**: / **Wireframe Images:**
        wf_images: list[str] = []
        wf_m = re.search(r'\*\*(?:wireframe_images|Wireframe\s*Images):?\*\*:?\s*(.+)', content, re.IGNORECASE)
        if wf_m:
            wf_images = re.findall(r'(?:ui/)([\w.-]+\.png)', wf_m.group(1))

        # Fallback: extract from **Artboards:** line (e.g. "7201 Name (main) + 7204 Name (overlay)")
        if not wf_images:
            ab_m = re.search(r'\*\*Artboards?:?\*\*:?\s*(.+)', content, re.IGNORECASE)
            if ab_m:
                artboard_ids = re.findall(r'(\d{4,5})', ab_m.group(1))
                ui_dir = report_dir / 'ui'
                if ui_dir.exists():
                    for png in sorted(ui_dir.glob('*.png')):
                        for aid in artboard_ids:
                            if aid in png.name:
                                wf_images.append(png.name)
                                break

        # Format D: extract from markdown image embeds ![caption](ui/xxx.png)
        if not wf_images:
            img_embeds = re.findall(r'!\[([^\]]*)\]\(ui/([\w.-]+\.png)\)', content)
            if img_embeds:
                for caption, img_file in img_embeds:
                    wf_images.append(img_file)

        # Also extract overlay/state info from image embed captions
        img_embeds_all = re.findall(r'!\[([^\]]*)\]\(ui/([\w.-]+\.png)\)', content)

        # Extract screen states
        states: list[dict[str, Any]] = []
        # Format A: ### State N: Name
        state_pattern = re.compile(
            r'###\s+State\s+(\d+):\s*(.+?)(?:\n|$)([\s\S]*?)(?=###\s+|---|\n##\s+|$)',
            re.MULTILINE
        )
        for sm in state_pattern.finditer(content):
            keywords = _extract_keywords(sm.group(2).strip() + ' ' + sm.group(3).strip())
            states.append({'num': sm.group(1), 'name': sm.group(2).strip(), 'desc': sm.group(3).strip(), 'keywords': keywords})

        # Format B: extract from **Artboards:** line entries (non-overlay)
        if not states and wf_images and not img_embeds_all:
            ab_m = re.search(r'\*\*Artboards?:?\*\*:?\s*(.+)', content, re.IGNORECASE)
            if ab_m:
                entries = re.split(r'\s*\+\s*', ab_m.group(1))
                for idx, entry in enumerate(entries):
                    entry = entry.strip()
                    if not entry or 'overlay' in entry.lower():
                        continue
                    name_m = re.match(r'(\d{4,5})\s+(.+?)(?:\s*\(([^)]+)\))?\s*$', entry)
                    if name_m:
                        keywords = _extract_keywords(name_m.group(2).strip() + ' ' + entry)
                        states.append({'num': str(idx + 1), 'name': name_m.group(2).strip(), 'desc': entry, 'keywords': keywords})

        # Format E: extract states from image embed captions ![caption](ui/xxx.png)
        if not states and img_embeds_all:
            for caption, img_file in img_embeds_all:
                caption_lower = caption.lower()
                if 'overlay' in caption_lower or 'bottom sheet' in caption_lower or 'popup' in caption_lower:
                    continue  # Skip overlays, handle below
                keywords = _extract_keywords(caption)
                states.append({
                    'num': str(len(states) + 1),
                    'name': caption,
                    'desc': caption,
                    'keywords': keywords,
                })

        # Extract overlays
        overlays: list[dict[str, Any]] = []
        # Format A: ### Overlay N: Name
        overlay_pattern = re.compile(
            r'###\s+Overlay\s*(\d*):\s*(.+?)(?:\n|$)([\s\S]*?)(?=###\s+|---|\n##\s+|$)',
            re.MULTILINE
        )
        for om in overlay_pattern.finditer(content):
            ov_num = om.group(1) or '1'
            keywords = _extract_keywords(om.group(2).strip() + ' ' + om.group(3).strip())
            overlays.append({'num': ov_num, 'name': om.group(2).strip(), 'desc': om.group(3).strip(), 'keywords': keywords})

        # Format B: ## Overlay:
        overlay2_pattern = re.compile(
            r'##\s+Overlay:\s*(.+?)(?:\n|$)([\s\S]*?)(?=\n##\s+|---\n\n##|$)',
            re.MULTILINE
        )
        for om in overlay2_pattern.finditer(content):
            keywords = _extract_keywords(om.group(1).strip() + ' ' + om.group(2).strip())
            overlays.append({'num': str(len(overlays) + 1), 'name': om.group(1).strip(), 'desc': om.group(2).strip(), 'keywords': keywords})

        # Format C: from **Artboards:** overlay entries
        if not overlays:
            ab_m = re.search(r'\*\*Artboards?:?\*\*:?\s*(.+)', content, re.IGNORECASE)
            if ab_m:
                entries = re.split(r'\s*\+\s*', ab_m.group(1))
                for entry in entries:
                    entry = entry.strip()
                    if 'overlay' in entry.lower():
                        name_m = re.match(r'(\d{4,5})\s+(.+?)(?:\s*\(([^)]+)\))?\s*$', entry)
                        if name_m:
                            ov_name = name_m.group(2).strip()
                            ov_tag = name_m.group(3) or 'overlay'
                            keywords = _extract_keywords(ov_name + ' ' + ov_tag)
                            overlays.append({'num': str(len(overlays) + 1), 'name': f'{ov_name} ({ov_tag})', 'desc': entry, 'keywords': keywords})

        # Format F: extract overlays from image embed captions
        if not overlays and img_embeds_all:
            for caption, img_file in img_embeds_all:
                caption_lower = caption.lower()
                if 'overlay' in caption_lower or 'bottom sheet' in caption_lower or 'popup' in caption_lower:
                    keywords = _extract_keywords(caption)
                    overlays.append({
                        'num': str(len(overlays) + 1),
                        'name': caption,
                        'desc': caption,
                        'keywords': keywords,
                    })

        # Format D: **Overlay:** in Flow section
        flow_m = re.search(r'\*\*Overlay:\*\*\s*(.+)', content)
        if flow_m and not overlays:
            ov_text = flow_m.group(1).strip()
            keywords = _extract_keywords(ov_text)
            overlays.append({'num': '1', 'name': ov_text, 'desc': ov_text, 'keywords': keywords})

        specs[scr_id] = {
            'wireframe_images': wf_images,
            'states': states,
            'overlays': overlays,
            'source': md_file.name,
        }


    return specs


def _extract_keywords(text: str) -> list[str]:
    """Extract meaningful keywords from state/overlay description."""
    text_lower = vn_normalize(text.lower()) if text else ''
    # Key domain terms for matching
    keyword_patterns = [
        'otp', 'pin', 'xac thuc', 'xac nhan', 'gui lai', 'resend', 'attempt', 'counter',
        'empty', 'trong', 'chua co', 'khong co',
        'khoa', 'locked', 'lock', 'bi khoa',
        'kich hoat', 'cho kich hoat', 'activate',
        'the phu', 'sub', 'phu',
        'mo rong', 'expand', 'chi tiet',
        'hoat dong', 'active', 'default',
        'date', 'picker', 'lich', 'calendar', 'ngay',
        'filter', 'loc', 'tim kiem',
        'tien vao', 'tien ra', 'credit', 'debit',
        'error', 'loi', 'fail', 'that bai',
        'success', 'thanh cong', 'ket qua',
        'confirm', 'xac nhan',
        'loading', 'tai', 'cho',
        'thong tin', 'info', 'detail',
        'toast', 'notification', 'thong bao',
        'carousel', 'swipe', 'slider',
    ]
    found = [kw for kw in keyword_patterns if kw in text_lower]
    return found


def build_check_image_map(
    report_path: Path,
    screen_specs: dict[str, Any],
    available_imgs: set[str],
) -> dict[str, str]:
    """Build mapping from "Check #N (SCR-XXX)" → best image file.

    Strategy:
    1. Parse check tables from report to get check content per (screen_id, check_num)
    2. Match check content keywords against state/overlay descriptions in screen MD
    3. Map matched state/overlay → wireframe_image by position + keyword overlap

    Returns: {"Check #4 (SCR-THE-001)": "danh-sach-the-xac-thuc-otp.png", ...}
    """
    if not screen_specs:
        return {}

    text = report_path.read_text(encoding='utf-8')
    result: dict[str, str] = {}

    # Parse check tables per screen
    # Pattern: ### N. Screen Name (SCR-XXX-NNN)
    # Then table rows: | N | Check content | Category | DDL | Evidence | Verdict |
    screen_sections = re.split(r'###\s+\d+\.\s+', text)

    for section in screen_sections[1:]:  # type: ignore[index]  # skip preamble
        # Extract screen ID from section header
        scr_m = re.search(r'\(?(SCR-[\w-]+)\)?', section[:200])
        if not scr_m:
            continue
        scr_id = scr_m.group(1)
        spec = screen_specs.get(scr_id)
        if not spec:
            continue

        wf_images = spec['wireframe_images']
        states = spec['states']
        overlays = spec['overlays']

        if not wf_images:
            continue

        # Build image→keywords mapping from wireframe filenames
        img_keyword_map: dict[str, list[str]] = {}
        for img in wf_images:
            img_lower = vn_normalize(img.replace('.png', '').replace('-', ' '))
            img_kws = _extract_keywords(img_lower)
            # Also add raw filename parts
            parts = img.replace('.png', '').split('-')
            img_kws.extend([p for p in parts if len(p) > 2])  # type: ignore[arg-type]
            img_keyword_map[img] = img_kws

        # Parse check table rows
        check_rows = re.findall(
            r'^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(\w+)',
            section, re.MULTILINE
        )

        for check_num_str, check_content, _category in check_rows:
            check_num = int(check_num_str)
            check_key = f'Check #{check_num} ({scr_id})'
            check_lower = vn_normalize(check_content.lower())
            check_keywords = _extract_keywords(check_content)

            best_img = None
            best_score = 0

            # Strategy 0: Direct artboard ID match from check content
            # If check mentions "(7203)" or "artboard 7100", map directly to *{id}*.png
            artboard_ids_in_check = re.findall(r'(?:\(|artboard\s+|ảnh\s+)(\d{4,5})', check_lower)
            if not artboard_ids_in_check:
                # Also match "bottom sheet (NNNN)" or standalone IDs like "7203"
                artboard_ids_in_check = re.findall(r'(\d{4,5})', check_content)
            for aid in artboard_ids_in_check:
                for img in wf_images:
                    if aid in img:
                        best_img = img
                        best_score = 100  # Highest priority — direct reference
                        break
                if best_score >= 100:
                    break

            # Strategy A: Match check content against state/overlay descriptions
            matched_section_imgs: list[str] = []

            for ov in overlays:
                ov_kws = ov['keywords']
                overlap = len(set(check_keywords) & set(ov_kws))
                # Also check if overlay name appears in check content
                ov_name_norm = vn_normalize(ov['name'].lower())
                name_bonus = 2 if any(w in check_lower for w in ov_name_norm.split() if len(w) > 3) else 0

                if overlap + name_bonus > 0:
                    # Overlays are typically at the END of wireframe_images
                    # Find best matching image from wf_images
                    for img in reversed(wf_images):  # overlays tend to be later images
                        img_kws = img_keyword_map.get(img, [])
                        img_score = len(set(ov_kws) & set(img_kws)) + name_bonus + overlap  # type: ignore[operator]
                        if img_score > best_score:
                            best_score = img_score
                            best_img = img

            for st in states:
                st_kws = st['keywords']
                overlap = len(set(check_keywords) & set(st_kws))
                st_name_norm = vn_normalize(st['name'].lower())
                name_bonus = 2 if any(w in check_lower for w in st_name_norm.split() if len(w) > 3) else 0

                if overlap + name_bonus > 0:
                    # States follow wireframe_images order
                    st_num = int(st['num']) if st['num'].isdigit() else 0
                    # Try to find image at position matching state number
                    if 0 < st_num <= len(wf_images):
                        img = wf_images[st_num - 1]  # type: ignore[index]
                        img_kws = img_keyword_map.get(img, [])  # type: ignore[arg-type]
                        img_score = len(set(st_kws) & set(img_kws)) + name_bonus + overlap  # type: ignore[operator]
                        if img_score > best_score:
                            best_score = img_score
                            best_img = img
                    # Also try keyword matching across all images
                    for img in wf_images:
                        img_kws = img_keyword_map.get(img, [])  # type: ignore[arg-type]
                        img_score = len(set(st_kws) & set(img_kws)) + overlap  # type: ignore[operator]
                        if img_score > best_score:
                            best_score = img_score
                            best_img = img

            # Strategy B: Direct keyword matching against image filenames
            if not best_img or best_score < 2:
                for img in wf_images:
                    img_kws = img_keyword_map.get(img, [])  # type: ignore[arg-type]
                    direct_score = len(set(check_keywords) & set(img_kws))
                    # Check raw content against filename
                    img_lower = vn_normalize(img.replace('.png', '').replace('-', ' '))
                    for word in check_lower.split():
                        if len(word) > 3 and word in img_lower:
                            direct_score += 1
                    if direct_score > best_score:
                        best_score = direct_score
                        best_img = img

            # Strategy C: Fallback — use first wireframe image (default state)
            if not best_img:
                best_img = wf_images[0]  # type: ignore[index]

            # Verify image exists in available_imgs
            if best_img and best_img in available_imgs:
                result[check_key] = best_img  # type: ignore[assignment]

    return result


def build_check_content_map(report_path: Path) -> dict[str, str]:
    """Parse check tables from report to build Check #N (SCR-XXX) → check content.

    Returns: {"Check #3 (SCR-THE-001)": "otp-input-1: canResend state missing", ...}
    """
    text = report_path.read_text(encoding='utf-8')
    result: dict[str, str] = {}
    screen_sections = re.split(r'###\s+\d+\.\s+', text)

    for section in screen_sections[1:]:  # type: ignore[index]
        scr_m = re.search(r'\(?(SCR-[\w-]+)\)?', section[:200])
        if not scr_m:
            continue
        scr_id = scr_m.group(1)

        check_rows = re.findall(
            r'^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(\w+)',
            section, re.MULTILINE
        )
        for check_num_str, check_content, _category in check_rows:
            check_key = f'Check #{check_num_str} ({scr_id})'
            result[check_key] = check_content.strip().rstrip('|').strip()

    return result


def augment_uxp_hien_trang(
    hien_trang: str,
    prop: dict[str, Any],
    screen_specs: dict[str, Any],
    check_content_map: dict[str, str],
) -> str:
    """Augment shallow UXP hiện trạng with screen MD context.

    When hiện_trạng is shallow (< 100 chars, typically from Format D table-only reports),
    this function expands it using:
    1. State/overlay enumeration from screen .md files
    2. Artboard count for the referenced screen
    3. Check content context from the report table

    If hiện_trạng is already detailed (≥ 100 chars, typically Format A/B),
    it is returned unchanged to preserve report author intent.

    Returns: augmented hiện trạng string
    """
    # Don't augment if already detailed (Format A/B reports write rich text)
    if len(hien_trang) >= 100:
        return hien_trang

    if not screen_specs:
        return hien_trang

    # Extract screen ID from UXP fields
    scr_id = ''
    gap_ref = prop.get('violation', '') or ''
    screen_field = prop.get('screen', '') or ''
    combined_ref = gap_ref + ' ' + screen_field

    scr_m = re.search(r'(SCR-[\w-]+)', combined_ref)
    if scr_m:
        scr_id = scr_m.group(1)

    if not scr_id or scr_id not in screen_specs:
        return hien_trang

    spec = screen_specs[scr_id]
    wf_images = spec.get('wireframe_images', [])
    states = spec.get('states', [])
    overlays = spec.get('overlays', [])
    artboard_count = len(wf_images)

    # Extract check references from Gap ref (multi-check aware)
    check_refs: list[tuple[str, str]] = []
    multi_m = re.search(r'Check\s+((?:#\d+(?:\s*,\s*)?)+)\s*\((SCR-[\w-]+)\)', gap_ref)
    if multi_m:
        scr_id_ref = multi_m.group(2)
        all_nums = re.findall(r'#(\d+)', multi_m.group(1))
        check_refs = [(n, scr_id_ref) for n in all_nums]
    else:
        check_refs = re.findall(r'Check\s*#(\d+)\s*\((SCR-[\w-]+)\)', gap_ref)

    # Determine context: is this check about a state or overlay?
    hien_lower = vn_normalize(hien_trang.lower())
    check_keywords = _extract_keywords(hien_trang)

    # Build augmentation parts
    parts: list[str] = []
    relevant_states: list[str] = []
    relevant_overlays: list[str] = []

    # Determine if issue is overlay-specific or screen-wide
    overlay_specific = False
    if overlays:
        # High-confidence overlay indicators in the check text
        explicit_ov_terms = bool(re.search(r'\boverlay\b|\bpopup\b|\bbottom.?sheet\b|\botp\b|\bpin\b.*(?:input|overlay|auth)',
                                            hien_lower, re.IGNORECASE))
        for ov in overlays:
            ov_kws = ov.get('keywords', [])  # type: ignore[union-attr]
            overlap = set(check_keywords) & set(ov_kws)
            # Accept ≥2 keyword overlap, OR ≥1 overlap when text explicitly mentions overlay/otp terms
            if len(overlap) >= 2 or (len(overlap) >= 1 and explicit_ov_terms):
                relevant_overlays.append(ov.get('name', ''))  # type: ignore[union-attr]
                overlay_specific = True

    # Part 1: State/overlay context (mutually exclusive)
    if overlay_specific and relevant_overlays:
        # Issue is about overlay — describe overlay, NOT all states
        ov_names = ', '.join(relevant_overlays[:2])  # type: ignore[index]
        parts.append(f'Overlay "{ov_names}" trên {scr_id}')
    elif states and not overlay_specific:
        # Check if the issue spans multiple states
        matching_state_count = 0
        for st in states:
            st_kws = st.get('keywords', [])  # type: ignore[union-attr]
            if set(check_keywords) & set(st_kws):
                matching_state_count += 1  # type: ignore[operator]
                relevant_states.append(st.get('name', ''))  # type: ignore[union-attr]

        # If issue affects ALL or MOST states, enumerate them
        if matching_state_count == 0:
            # Issue likely affects all states (generic issue like "thiếu error state")
            state_names = [s.get('name', '') for s in states if s.get('name')]  # type: ignore[union-attr]
            if state_names and len(state_names) >= 2:
                state_list = ', '.join(state_names[:4])  # type: ignore[index]
                if len(state_names) > 4:
                    state_list += f' và {len(state_names) - 4} trạng thái khác'
                parts.append(f'Tất cả {len(state_names)} trạng thái ({state_list}) đều')
        elif matching_state_count >= 2:
            state_list = ', '.join(relevant_states[:4])  # type: ignore[index]
            parts.append(f'{matching_state_count} trạng thái ({state_list}) đều')

    # Part 2: Core issue (original hiện trạng)
    core_issue = hien_trang.rstrip('.')

    # Part 3: Artboard evidence — only for "missing state" type issues
    artboard_clause = ''
    missing_state_indicators = ['thiếu', 'missing', 'không có', 'thiếu trạng thái',
                                  'error state', 'validation', 'empty state']
    is_missing_state = any(ind in hien_lower for ind in missing_state_indicators)

    if artboard_count > 0 and is_missing_state:
        overlay_count = len(overlays)
        if overlay_count > 0:
            artboard_clause = f'Trong {artboard_count} artboard (+{overlay_count} overlay) của biên {scr_id}'
        else:
            artboard_clause = f'Trong {artboard_count} artboard của biên {scr_id}'

    # Part 4: Get specific check content for richer context
    check_detail = ''
    if check_refs:
        details = []
        for cn, cs in check_refs:
            ck = f'Check #{cn} ({cs})'
            content = check_content_map.get(ck, '')
            if content and content.lower() != hien_lower:
                content = re.sub(r'\s*\|.*$', '', content).strip()
                if len(content) > 10:
                    details.append(content)
        if details:
            check_detail = '; '.join(details[:2])  # type: ignore[index]

    # Assemble augmented text
    augmented = ''

    if parts and not overlay_specific:
        # States enumeration + core issue (lowercase first letter of core issue)
        lower_core = core_issue[0].lower() + core_issue[1:] if core_issue and core_issue[0].isupper() and len(core_issue) > 20 else core_issue  # type: ignore[index]
        augmented = f'{parts[0]} {lower_core}'
    elif parts and overlay_specific:
        # Overlay context: "Overlay 'Name': core issue"
        augmented = f'{parts[0]}: {core_issue}'
    else:
        augmented = core_issue

    if artboard_clause:
        augmented += f'. {artboard_clause}, không có artboard nào thể hiện trạng thái này'

    augmented += '.'

    # Only return augmented if it's meaningfully longer
    if len(augmented) > len(hien_trang) + 20:
        return augmented

    return hien_trang


# ═══════════════════════════════════════════════════════════
# PROPOSAL PARSER
# ═══════════════════════════════════════════════════════════

def parse_proposals(report_path):
    """Parse UXP proposals from ux-review-report.md.
    Returns: (meta_dict, proposals_list, gaps_list, screens_list)
    """
    text = report_path.read_text(encoding='utf-8')
    lines = text.split('\n')

    # ── Meta (from report header only — first ~30 lines) ──
    meta: dict[str, Any] = {'title': '', 'screens': 0, 'checks': 0, 'pass': 0, 'gap': 0,
            'proposals': 0, 'score': 0, 'critical': 0, 'major': 0, 'minor': 0}
    # Only scan header lines (before first ### section)
    header_lines = []
    for line in lines:
        if line.strip().startswith('### ') or line.strip().startswith('## 2'):
            break
        header_lines.append(line)
    
    for line in header_lines:
        m = re.match(r'^# (?:UX (?:Review Report|Audit(?: Report)?)).*?[—–-]\s*(.+)', line)
        if m:
            meta['title'] = m.group(1).strip()
        # Only match: **Screens**: N  or  Screens reviewed: N  (at line/field start)
        m = re.search(r'(?:\*\*Screens?\*\*|^Screens?(?: reviewed)?)\s*[:\s]\s*(\d+)', line)
        if m: meta['screens'] = int(m.group(1))
        m = re.search(r'(?:\*\*)?(?:Tổng check|Total checks)(?:\*\*)?[:\s]*(\d+)', line)
        if m: meta['checks'] = int(m.group(1))
        m = re.search(r'Pass[:\s]*(\d+)\s*\|?\s*(?:\*\*)?Gap[:\s]*(\d+)', line)
        if m: meta['pass'] = int(m.group(1)); meta['gap'] = int(m.group(2))
        m = re.search(r'(?:UX )?Score\s*(?:\(Simple\))?[:\s]*(\d+)%', line)
        if m: meta['score'] = int(m.group(1))
        # Severity: only from summary lines, not checklist
        m = re.search(r'(?:🔴\s*)?Critical[:\s]*(\d+)', line)
        if m and '|' not in line: meta['critical'] = int(m.group(1))  # type: ignore[operator]
        m = re.search(r'(?:🟡\s*)?Major[:\s]*(\d+)', line)
        if m and '|' not in line: meta['major'] = int(m.group(1))
        m = re.search(r'(?:⚪\s*)?Minor[:\s]*(\d+)', line)
        if m and '|' not in line: meta['minor'] = int(m.group(1))
        # Total proposals - only match header line with Total context
        m = re.search(r'\*\*Total\*\*\s*\|\s*\*\*(\d+)\*\*', line)
        if m: meta['proposals'] = int(m.group(1))
        m = re.search(r'Total[:\s]*(\d+)\s*\|', line)
        if m: meta['proposals'] = int(m.group(1))

    # ── Build check evidence map from checklist table ──
    # Dual-key: (scr_id, local_num) for screen-scoped, global_num for flat
    check_evidence_map: dict[Any, Any] = {}       # global check_num → data
    check_evidence_scoped: dict[Any, Any] = {}    # (scr_id, local_num) → data
    current_checklist_screen = ''
    current_checklist_scr_id = ''
    current_wireframe_imgs = []
    running_check_counter = 0
    for line in lines:
        # Track screen context — Format A: ### N. Title (`SCR-XXX`)
        hm = re.match(r'###\s*\d+\.\s*(.*?)\s*\(`?(SCR-\S+?)`?\)', line)
        if hm:
            current_checklist_screen = hm.group(1).strip()
            current_checklist_scr_id = hm.group(2).strip()
            current_wireframe_imgs = []
            continue
        # Format B: ### N. SCR-XXX — Title
        hc = re.match(r'###\s*\d+\.\s*(SCR-\S+)\s*[—–-]\s*(.+)', line)
        if hc:
            current_checklist_scr_id = hc.group(1).strip()
            current_checklist_screen = hc.group(2).strip()
            current_wireframe_imgs = []
            continue
        # Wireframes line: **Wireframes:** `ui/foo.png`, `ui/bar.png`
        wf = re.match(r'\*\*Wireframes?:\*\*\s*(.+)', line)
        if wf:
            current_wireframe_imgs = re.findall(r'([\w-]+\.png)', wf.group(1))
            continue
        # Parse checklist rows — both formats
        if '|' in line and ('Pass' in line or 'Gap' in line):
            cols = [c.strip() for c in line.split('|')]
            cols = [c for c in cols if c]
            if len(cols) >= 5:
                try:
                    check_num = int(cols[0])
                except (ValueError, IndexError):
                    continue
                running_check_counter += 1  # type: ignore[operator]
                # Find evidence column
                ev_text = ''
                for ci in range(1, len(cols)):
                    col_text = cols[ci]
                    if any(kw in col_text.lower() for kw in ['từ ảnh', 'vision:', 'ddl ', 'evidence:', 'screenshot']):
                        ev_text = col_text; break
                    if '.png' in col_text:
                        ev_text = col_text; break
                    if len(col_text) > len(ev_text) and col_text not in ('✅ Pass', '❌ Gap', '⚠️ Gap', '⚠️ Unverifiable'):
                        ev_text = col_text
                ev_imgs = re.findall(r'([\w-]+\.png)', ev_text)
                if not ev_imgs and current_wireframe_imgs:
                    ev_imgs = current_wireframe_imgs[:2]  # type: ignore[index]
                data: dict[str, Any] = {
                    'images': ev_imgs,
                    'evidence': ev_text,
                    'screen': current_checklist_screen,
                }
                # Store with both keys
                check_evidence_map[running_check_counter] = data
                check_evidence_map[check_num] = data  # may overwrite for dup nums
                if current_checklist_scr_id:
                    check_evidence_scoped[(current_checklist_scr_id, check_num)] = data

    # ── Proposals ──
    proposals = []
    current_severity_ctx = ''
    i = 0
    while i < len(lines):
        line_stripped = lines[i].strip()  # type: ignore[index]

        # Track severity context
        if re.match(r'^###\s*(?:🔴\s*)?Critical', line_stripped):
            current_severity_ctx = 'critical'; i += 1; continue
        if re.match(r'^###\s*(?:🟡\s*|🟠\s*)?Major', line_stripped):
            current_severity_ctx = 'major'; i += 1; continue
        if re.match(r'^###\s*(?:⚪\s*)?Minor', line_stripped):
            current_severity_ctx = 'minor'; i += 1; continue

        # Format A+B: #### UXP-XXX · severity
        pm = re.match(r'^####\s+(UXP-[\w-]+)\s*·\s*(.+)', lines[i])  # type: ignore[index]
        if pm:
            prop: dict[str, Any] = {
                'id': pm.group(1), 'severity_raw': pm.group(2).strip(),
                'severity': '', 'screen': '', 'ddl': '', 'ux_law': '',
                'hiện_trạng': '', 'hậu_quả': '', 'user_impact': '',
                'business_impact': '', 'violation': '', 'giải_pháp': [],
                'evidence_img': '',
            }
            sev_text = prop['severity_raw'].lower()
            if 'critical' in sev_text: prop['severity'] = 'critical'
            elif 'major' in sev_text: prop['severity'] = 'major'
            else: prop['severity'] = 'minor'

            i += 1
            # Skip blank lines and title line between header and table
            while i < len(lines) and (not lines[i].strip() or (re.match(r'^\*\*[^*]+\*\*$', lines[i].strip()) and not lines[i].strip().startswith('|'))):  # type: ignore[index]
                # Capture standalone bold title line (Format B/C)
                title_line = lines[i].strip()  # type: ignore[index]
                if title_line and re.match(r'^\*\*[^*]+\*\*$', title_line):
                    prop['_title_override'] = title_line.strip('* ')
                i += 1
            # Parse table rows — supports Format A (bold) and Format B (non-bold field names)
            while i < len(lines) and lines[i].strip().startswith('|'):  # type: ignore[index]
                row = lines[i]  # type: ignore[index]
                # Format A: **Màn hình** / **DDL** / **UX Law** / **Vấn đề**
                for field, key in [('**Màn hình**','screen'),('**DDL**','ddl'),('**UX Law**','ux_law'),('**Vấn đề**','hiện_trạng')]:
                    if field in row:
                        m2 = re.search(r'\|\s*(.+?)\s*\|\s*$', row.split(field)[1])
                        if m2: prop[key] = m2.group(1).strip().strip('|').strip()
                # Format B: Screen / DDL Ref / Heuristic / UX Law (non-bold)
                row_stripped = row.strip()
                if re.match(r'^\|\s*(?:Screen|Heuristic|DDL Ref|UX Law)\s*\|', row_stripped):
                    cols = [c.strip() for c in row_stripped.split('|')]
                    cols = [c for c in cols if c]
                    if len(cols) >= 2:
                        field_name = cols[0].strip()
                        value = cols[1].strip()
                        if field_name == 'Screen' and not prop['screen']:  # type: ignore[index]
                            prop['screen'] = value  # type: ignore[index]
                        elif field_name == 'DDL Ref' and not prop['ddl']:  # type: ignore[index]
                            prop['ddl'] = value  # type: ignore[index]
                        elif field_name == 'Heuristic' and not prop['violation']:  # type: ignore[index]
                            prop['violation'] = value  # type: ignore[index]
                        elif field_name == 'UX Law' and not prop['ux_law']:  # type: ignore[index]
                            prop['ux_law'] = value  # type: ignore[index]
                # Format A + D: **Giải pháp** or **Đề xuất** in table row
                for gp_key in ['**Giải pháp**', '**Đề xuất**']:
                    if gp_key in row:
                        m2 = re.search(r'\|\s*(.+?)\s*\|\s*$', row.split(gp_key)[1])
                        if m2: prop['giải_pháp'].append(m2.group(1).strip().strip('|').strip())  # type: ignore[index,union-attr]
                # Extract **Tác động** from table row (Format D)
                if '**Tác động**' in row and not prop['user_impact']:  # type: ignore[index]
                    m2 = re.search(r'\|\s*(.+?)\s*\|\s*$', row.split('**Tác động**')[1])
                    if m2: prop['user_impact'] = m2.group(1).strip().strip('|').strip()
                if '**Gap ref**' in row and not prop['violation']:
                    m2 = re.search(r'\|\s*(.+?)\s*\|\s*$', row.split('**Gap ref**')[1])
                    if m2: prop['violation'] = m2.group(1).strip().strip('|').strip()
                # Format B/D: DDL Ref in bold table row
                if '**DDL Ref**' in row and not prop['ddl']:
                    m2 = re.search(r'\|\s*(.+?)\s*\|\s*$', row.split('**DDL Ref**')[1])
                    if m2: prop['ddl'] = m2.group(1).strip().strip('|').strip()
                i += 1

            # Parse body sections — supports 4 report formats:
            # Format A: **🔍 Hiện trạng** / **⚠️ Hậu quả** / **✅ Giải pháp đề xuất** (section headers)
            # Format B: **Hiện trạng:** inline / **Tác động:** bullets / **Đề xuất:** bullets (inline headers)
            # Format C: **Hiện trạng (Current State)** / **Hệ quả (Consequences)** / **Đề xuất giải pháp (Proposed Solution)**
            # Format D: All data in single table rows (handled above in table parser)
            current_section = ''
            while i < len(lines):
                line = lines[i].strip()
                if line.startswith('#### UXP-') or (line == '---' and i + 1 < len(lines) and re.match(r'^####\s+UXP-', lines[i+1].strip())):
                    break
                if line == '---': i += 1; continue

                # ── Format A section headers ──
                if line.startswith('**🔍 Hiện trạng**'): current_section = 'hien_trang'; i += 1; continue
                elif line.startswith('**⚠️ Hậu quả**'): current_section = 'hau_qua'; i += 1; continue
                elif line.startswith('**✅ Giải pháp đề xuất**'): current_section = 'giai_phap'; i += 1; continue
                elif line.startswith('### ') or line.startswith('## '): break

                # ── Format C section headers ──
                if re.match(r'^\*\*Hiện trạng\s*\(', line): current_section = 'hien_trang'; i += 1; continue
                elif re.match(r'^\*\*(?:Hệ quả|Consequences)', line): current_section = 'tac_dong'; i += 1; continue
                elif re.match(r'^\*\*Đề xuất giải pháp', line): current_section = 'de_xuat'; i += 1; continue
                # Standalone **Tác động** as section header (no colon)
                elif line == '**Tác động**': current_section = 'tac_dong'; i += 1; continue

                # ── Format B: inline **Hiện trạng:** ──
                ht_m = re.match(r'^\*\*Hiện trạng:\*\*\s*(.*)', line)
                if ht_m:
                    ht_text = ht_m.group(1).strip()
                    if ht_text:
                        prop['hiện_trạng'] = ht_text
                        # Extract evidence image from inline text
                        img_m = re.search(r'(?:ảnh|image)\s+([\w-]+\.png)', ht_text, re.IGNORECASE)
                        if img_m and not prop['evidence_img']:
                            prop['evidence_img'] = img_m.group(1)
                    current_section = 'hien_trang'
                    i += 1; continue

                # ── Format B: **Tác động:** ──
                td_m = re.match(r'^\*\*Tác động:\*\*\s*(.*)', line)
                if td_m:
                    inline_impact = td_m.group(1).strip()
                    if inline_impact and not prop['user_impact']:
                        prop['user_impact'] = inline_impact
                    current_section = 'tac_dong'
                    i += 1; continue

                # ── Format B: **Đề xuất:** ──
                dx_m = re.match(r'^\*\*Đề xuất:\*\*\s*(.*)', line)
                if dx_m:
                    inline_dx = dx_m.group(1).strip()
                    if inline_dx:
                        prop['giải_pháp'].append(inline_dx)  # type: ignore[union-attr]
                    current_section = 'de_xuat'
                    i += 1; continue

                # ── Format B: Title line (bold text after UXP header, before table) ──
                if re.match(r'^\*\*[^*]+\*\*$', line) and not prop.get('_title_override') and current_section == '':
                    prop['_title_override'] = line.strip('* ')
                    i += 1; continue

                # ── Content processing based on current section ──
                if current_section == 'hien_trang' and line and not line.startswith('|') and not line.startswith('>'):
                    if prop['hiện_trạng']: prop['hiện_trạng'] += ' '
                    prop['hiện_trạng'] += line
                elif current_section == 'hien_trang' and line.startswith('>'):
                    ev = line.lstrip('> ').strip()
                    img_m = re.search(r'(?:ảnh|image)\s+([\w-]+\.png)', ev, re.IGNORECASE)
                    if img_m and not prop['evidence_img']: prop['evidence_img'] = img_m.group(1)
                    if not prop['evidence_img']:
                        img_m2 = re.search(r'(?:^|\s|:)([\w-]+\.png)', ev)
                        if img_m2: prop['evidence_img'] = img_m2.group(1)
                elif current_section == 'hau_qua':
                    if '**User impact:**' in line:
                        prop['user_impact'] = re.sub(r'\*\*User impact:\*\*\s*', '', line).strip().rstrip('.')
                    elif '**Business impact:**' in line:
                        prop['business_impact'] = re.sub(r'\*\*Business impact:\*\*\s*', '', line).strip()
                    elif '**Violation:**' in line:
                        prop['violation'] = re.sub(r'\*\*Violation:\*\*\s*', '', line).strip()
                elif current_section == 'tac_dong' and line.startswith('- '):
                    impact_item = line.lstrip('- ').strip()
                    if impact_item:
                        if prop['user_impact']:
                            prop['user_impact'] += '; ' + impact_item
                        else:
                            prop['user_impact'] = impact_item
                elif current_section == 'tac_dong' and line and not line.startswith('|') and not line.startswith('#'):
                    # Paragraph text in tác động section
                    if prop['user_impact']:
                        prop['user_impact'] += ' ' + line
                    else:
                        prop['user_impact'] = line
                elif current_section == 'de_xuat' and line.startswith('- '):
                    dx_item = line.lstrip('- ').strip()
                    if dx_item:
                        prop['giải_pháp'].append(dx_item)  # type: ignore[union-attr]
                elif current_section == 'de_xuat' and line and not line.startswith('|') and not line.startswith('#'):
                    # Paragraph text in đề xuất section
                    prop['giải_pháp'].append(line)  # type: ignore[union-attr]
                elif current_section == 'giai_phap' and '|' in line and line.count('|') >= 4:
                    cols = [c.strip() for c in line.split('|')]
                    cols = [c for c in cols if c]
                    if len(cols) >= 3 and not cols[0].startswith('#') and not cols[0].startswith('-'):
                        prop['giải_pháp'].append(cols[2] if len(cols) > 2 else cols[1])
                i += 1

            all_imgs = re.findall(r'([\w-]+\.png)', prop['hiện_trạng'])
            if not prop['evidence_img'] and all_imgs: prop['evidence_img'] = all_imgs[0]
            prop['all_imgs'] = all_imgs

            # ── Cross-reference Gap ref → checklist evidence for images ──
            gap_ref = prop.get('violation', '')
            if not gap_ref:
                # Also check if Gap ref was parsed into a different field
                for row_text in [prop.get('hiện_trạng', ''), prop.get('ddl', '')]:
                    gm = re.findall(r'Check\s*#?(\d+)', row_text)
                    if gm:
                        gap_ref = ', '.join(f'#{n}' for n in gm)
                        break
            if gap_ref and (check_evidence_map or check_evidence_scoped):
                # Extract SCR-ID from Gap ref if present (e.g. "Check #3 (SCR-THE-001)")
                scr_in_ref = re.search(r'\((SCR-[\w-]+)\)', gap_ref)
                ref_scr_id = scr_in_ref.group(1) if scr_in_ref else ''
                check_nums = [int(n) for n in re.findall(r'(\d+)', gap_ref.split('(')[0] if '(' in gap_ref else gap_ref)]
                ref_imgs = []
                for cn in check_nums:
                    # Try screen-scoped first
                    if ref_scr_id and (ref_scr_id, cn) in check_evidence_scoped:
                        ref_imgs.extend(check_evidence_scoped[(ref_scr_id, cn)]['images'])  # type: ignore[index]
                    elif cn in check_evidence_map:
                        ref_imgs.extend(check_evidence_map[cn]['images'])  # type: ignore[index]
                if ref_imgs:
                    seen = set()
                    unique_imgs = []
                    for img in ref_imgs:
                        if img not in seen:
                            seen.add(img)
                            unique_imgs.append(img)
                    if not prop['evidence_img']:
                        prop['evidence_img'] = unique_imgs[0]
                    prop['all_imgs'] = unique_imgs + [i for i in all_imgs if i not in seen]

            # Extract UX Law from DDL field if present (e.g. "Law:zeigarnik")
            if not prop.get('ux_law') or prop['ux_law'] == '—':
                law_m = re.search(r'Law[:\s]*(\w+)', prop.get('ddl', ''))
                if law_m:
                    prop['ux_law'] = law_m.group(1)

            if not prop['user_impact'] and prop['hiện_trạng']:
                prop['user_impact'] = infer_user_impact(prop['hiện_trạng'], '')
            proposals.append(prop)
            continue

        # Format E: - **[UXP-NNN]** Screen: `SCR-XXX` | **Title** (— Description)?
        bm = re.match(r'^-\s*\*\*\[(UXP-[\w-]+)\]\*\*\s*Screen:\s*`?([\w-]+)`?\s*\|\s*\*\*(.+?)\*\*(?:\s*[—–-]\s*(.+))?', line_stripped)
        if bm:
            desc = (bm.group(4) or bm.group(3)).strip()
            title = bm.group(3).strip()
            prop: dict[str, Any] = {
                'id': bm.group(1), 'severity_raw': current_severity_ctx or 'minor',
                'severity': current_severity_ctx or 'minor',
                'screen': bm.group(2), 'ddl': '', 'ux_law': '',
                'hiện_trạng': desc, 'hậu_quả': '',
                'user_impact': infer_user_impact(title + ' ' + desc, ''),
                'business_impact': '', 'violation': '',
                'giải_pháp': [desc], 'evidence_img': '',
                'all_imgs': re.findall(r'([\w-]+\.png)', desc),
                '_title_override': title,
            }
            if prop['all_imgs']: prop['evidence_img'] = prop['all_imgs'][0]
            proposals.append(prop)
            i += 1; continue

        # Format C variant: - **[UXP-NNN]** Screen: `SCR-XXX` | **Title only**
        bm2 = re.match(r'^-\s*\*\*\[(UXP-[\w-]+)\]\*\*\s*Screen:\s*`?([\w-]+)`?\s*\|\s*\*\*(.+?)\*\*\s*$', line_stripped)
        if bm2:
            title_text = bm2.group(3).strip()
            prop = {
                'id': bm2.group(1), 'severity_raw': current_severity_ctx or 'minor',
                'severity': current_severity_ctx or 'minor',
                'screen': bm2.group(2), 'ddl': '', 'ux_law': '',
                'hiện_trạng': title_text, 'hậu_quả': '',
                'user_impact': infer_user_impact(title_text, ''),
                'business_impact': '', 'violation': '',
                'giải_pháp': [], 'evidence_img': '',
                'all_imgs': re.findall(r'([\w-]+\.png)', title_text),
                '_title_override': title_text,
            }
            if prop['all_imgs']: prop['evidence_img'] = prop['all_imgs'][0]
            proposals.append(prop)
            i += 1; continue

        i += 1

    # Auto-compute meta
    if meta['proposals'] == 0: meta['proposals'] = len(proposals)
    if meta['critical'] == 0: meta['critical'] = sum(1 for p in proposals if p['severity'] == 'critical')
    if meta['major'] == 0: meta['major'] = sum(1 for p in proposals if p['severity'] == 'major')
    if meta['minor'] == 0: meta['minor'] = sum(1 for p in proposals if p['severity'] == 'minor')

    gaps, screens = parse_gaps(report_path)

    # ── Recalculate meta from screen data (header values are often stale) ──
    if screens:
        total_pass = sum(s.get('pass', 0) for s in screens)
        total_gap = sum(s.get('gap', 0) for s in screens)
        total_checks = total_pass + total_gap  # type: ignore[operator]
        avg_score = sum(int(s['score']) for s in screens) // len(screens)  # type: ignore[arg-type]

        # Always prefer calculated values over header
        if total_checks > 0:  # type: ignore[operator]
            meta['checks'] = total_checks
            meta['pass'] = total_pass
            meta['gap'] = total_gap
        elif meta['checks'] == 0:
            meta['checks'] = total_checks
            meta['pass'] = total_pass
            meta['gap'] = total_gap

        if meta['score'] == 0 or (avg_score > 0 and abs(meta['score'] - avg_score) > 15):
            meta['score'] = avg_score

        if meta['screens'] == 0:
            meta['screens'] = len(screens)

    # Severity counts from proposals if not in header
    if meta['critical'] == 0 and meta['major'] == 0:
        meta['critical'] = sum(1 for p in proposals if p['severity'] == 'critical')
        meta['major'] = sum(1 for p in proposals if p['severity'] == 'major')
        meta['minor'] = sum(1 for p in proposals if p['severity'] == 'minor')

    # Always use actual parsed proposals count — header 'Total' is ambiguous
    if proposals:
        meta['proposals'] = len(proposals)

    return meta, proposals, gaps, screens


# ═══════════════════════════════════════════════════════════
# GAP HTML GENERATOR
# ═══════════════════════════════════════════════════════════

def generate_gap_html(gaps, screens, enriched_gaps=None):
    """Generate gap section HTML grouped by screen."""
    if enriched_gaps is None:
        enriched_gaps = {}
    if not gaps:
        return ''
    from collections import OrderedDict
    screen_gaps = OrderedDict()
    for g in gaps:  # type: ignore[union-attr]
        screen_gaps.setdefault(g['screen'], []).append(g)
    screen_info = {s['id']: s for s in screens}

    body = ''
    idx = 0
    for scr_id, scr_gaps in screen_gaps.items():
        info = screen_info.get(scr_id, {})
        title = info.get('title', scr_id)
        scr_type = info.get('type', '')
        type_badge = f' · <em>{scr_type}</em>' if scr_type else ''

        body += f'''
  <div style="margin-bottom:36px">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">
      <span class="gap-screen">{scr_id}</span>
      <strong style="font-size:14px">{title}</strong>{type_badge}
    </div>
'''
        for g in scr_gaps:
            idx += 1  # type: ignore[operator]
            check_text = translate_gap_title(g['check'].replace('`', ''))
            source = g.get('source', '')
            ref = g.get('ref', '—')
            heuristic = map_heuristic(source, ref)
            ref_clean = ref.replace('`', '').strip()
            # Suppress ref badge if it's just a severity label (not a real heuristic ref)
            _sev_words = {'critical', 'major', 'minor', 'nghiêm trọng', 'quan trọng', 'cải thiện'}
            ref_badge = f'<span class="gap-ref">{ref_clean}</span>' if ref_clean and ref_clean != '—' and ref_clean.lower() not in _sev_words else ''

            ev_raw = g.get('evidence', '').strip()
            gap_imgs = g.get('images', [])
            if not gap_imgs:
                gap_imgs = re.findall(r'([\w-]+\.png)', ev_raw)[:2]  # type: ignore[index]
            ev_img_ref = ', '.join(gap_imgs[:2]) if gap_imgs else ''

            ev_clean = ev_raw
            ev_clean = re.sub(r'^Từ ảnh[^:]*:\s*', '', ev_clean)
            ev_clean = re.sub(r'^(?:Screenshots?|Vision|Design)[\s:]+', '', ev_clean)
            ev_clean = re.sub(r'\s*[A-Za-z0-9_-]+\.png', '', ev_clean)
            ev_clean = re.sub(r'\s{2,}', ' ', ev_clean).strip()
            ev_clean = re.sub(r'^[\s,\—–→:-]+', '', ev_clean).strip()
            if ev_clean: ev_clean = ev_clean[0].upper() + ev_clean[1:]  # type: ignore[index]

            img_citation = ''
            if ev_img_ref:
                img_citation = f' <span style="display:inline-block;background:#EFF6FF;color:#2563EB;font-size:10px;padding:1px 6px;border-radius:4px;font-family:monospace;margin-left:4px">📸 {ev_img_ref}</span>'

            # Use enriched data if available, fallback to regex
            # Try composite key first, then sequential index  
            _ekey = f"{g['screen']}:{g['check'][:80]}"
            eg: dict[str, Any] = enriched_gaps.get(_ekey, {})  # type: ignore[union-attr]
            user_impact = eg.get('impact', '') or infer_user_impact(check_text, ev_clean)
            h_tag = translate_label(eg.get('heuristic_tag', '') or heuristic)  # type: ignore[arg-type]
            ddl_evidence = translate_label(eg.get('ddl_evidence', ''))  # type: ignore[arg-type]
            comp_ctx = eg.get('component_context', '')  # type: ignore[arg-type]
            gap_hien_trang = eg.get('hiện_trạng', '')  # type: ignore[arg-type]

            # DDL evidence badge (Vietnamese label)
            ddl_badge = ''
            if ddl_evidence:
                ddl_label = I18N_VI.get('DDL Reference', 'Tham chiếu DDL')
                ddl_badge = f'''\n        <div class="gap-full">
          <div class="gap-label">📋 {ddl_label}</div>
          <div style="color:var(--text-muted);font-size:12px;font-style:italic">{ddl_evidence}</div>
        </div>'''

            # Gap hiện trạng section (from enriched data)
            hien_trang_section = ''
            if gap_hien_trang:
                hien_trang_section = f'''\n        <div class="gap-full">
          <div class="gap-label">📝 Hiện trạng</div>
          <div style="color:var(--text-secondary)">{gap_hien_trang}</div>
        </div>'''

            body += f'''    <div class="gap-card reveal">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px">
        <span class="gap-num">{idx}</span>
        <strong style="font-size:13.5px">{check_text}</strong>
        {ref_badge}
      </div>
      <div class="gap-grid">{hien_trang_section}
        <div>
          <div class="gap-label">🎯 Tác động đến người dùng</div>
          <div style="color:var(--text-secondary)">{user_impact}</div>
        </div>
        <div>
          <div class="gap-label">📐 {h_tag}</div>
          <div style="color:var(--text-secondary)">{heuristic}</div>
        </div>
        <div class="gap-full">
          <div class="gap-label">🔍 Bằng chứng &amp; Phân tích{img_citation}</div>
          <div style="color:var(--text-secondary)">{ev_clean}</div>
        </div>{ddl_badge}
      </div>
    </div>
'''
        body += '  </div>\n'

    return f'''
<section class="section" id="gaps" style="padding-top:48px">
  <div class="section-title"><span class="icon">📋</span> Tổng hợp Gap ({len(gaps)} hạng mục)</div>
  <p style="color:var(--text-muted);font-size:14px;margin-bottom:20px">Các hạng mục kiểm tra chưa đạt chuẩn theo từng màn hình — checklist cải thiện từ ux-review-report</p>
{body}</section>
'''


# ═══════════════════════════════════════════════════════════
# MAIN GENERATOR
# ═══════════════════════════════════════════════════════════

def read_css_from_template():
    """Read CSS from the bundled template.html."""
    if not TEMPLATE_PATH.exists():
        return None
    html = TEMPLATE_PATH.read_text(encoding='utf-8')
    m = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    return m.group(1).strip() if m else None


def generate(args):
    """Generate pitch-deck.html from ux-review-report.md."""
    report = Path(args.report)
    if not report.exists():
        print(f'❌ Report not found: {report}', file=sys.stderr)
        return False

    meta, proposals, gaps, screens = parse_proposals(report)
    if not proposals:
        print(f'⚠️ No proposals found in {report.name}', file=sys.stderr)
        return False

    # Resolve names
    title = args.module or meta['title'] or report.parent.name
    product = args.product or 'Mobile Banking'
    client = args.client or ''
    hero_title = f'{client} · {title}' if client else title
    score = meta['score']
    e = html_mod.escape

    # CSS — from template or inline
    css = read_css_from_template()
    if not css:
        print('⚠️ Template not found, using inline CSS', file=sys.stderr)
        css = _FALLBACK_CSS

    # Available images
    ui_dirs = []
    if args.ui_dir:
        ui_dirs = [Path(args.ui_dir)]
    else:
        # Auto-discover: look for ui/ subdirs
        for d in report.parent.rglob('ui'):
            if d.is_dir():
                ui_dirs.append(d)
    available_imgs = set()
    ui_base = ''
    for ud in ui_dirs:
        for f in ud.iterdir():
            if f.suffix == '.png':
                available_imgs.add(f.name)
        if not ui_base:
            try:
                ui_base = str(ud.relative_to(report.parent))
            except ValueError:
                ui_base = str(ud)

    if not ui_base:
        ui_base = 'ui'

    # ── Load screen_inventory.json for scr→image mapping ──
    scr_image_map = {}  # SCR-XXX → [filename1, filename2, ...]
    inventory_path = report.parent / '.handoff' / 'screen_inventory.json'
    if inventory_path.exists():
        try:
            inv_data = json.loads(inventory_path.read_text(encoding='utf-8'))
            for scr in inv_data.get('screens', []):
                scr_id = scr.get('screen_id', '')
                wf_imgs = [Path(w.get('filename', '')).name for w in scr.get('wireframe_images', []) if w.get('filename')]
                if scr_id and wf_imgs:
                    scr_image_map[scr_id] = wf_imgs
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError) as exc:
            print(f'  ⚠️ screen_inventory.json load failed: {exc}', file=sys.stderr)

    # ── Parse screen .md specs for check→image mapping ──
    screen_specs = parse_screen_specs(report.parent)
    check_image_map: dict[str, str] = {}
    check_content_map: dict[str, str] = {}
    if screen_specs and available_imgs:
        check_image_map = build_check_image_map(report, screen_specs, available_imgs)
        check_content_map = build_check_content_map(report)
        if check_image_map:
            print(f'  ✅ Screen MD specs: {len(screen_specs)} screens, {len(check_image_map)} check→image mappings', file=sys.stderr)

    # ── Load enriched-data.json (DDL-grounded reasoning) ──
    enriched = {}
    enriched_path = report.parent / 'enriched-data.json'
    if enriched_path.exists():
        try:
            enriched = json.loads(enriched_path.read_text(encoding='utf-8'))
            print(f'  ✅ Loaded enriched-data.json ({len(enriched.get("gaps", []))} gaps, '
                  f'{len(enriched.get("proposals", []))} UXPs, '
                  f'{len(enriched.get("category_scores", {}))} categories)', file=sys.stderr)
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError) as exc:
            print(f'  ⚠️ enriched-data.json load failed: {exc}', file=sys.stderr)
            enriched = {}

    # Build enriched lookup maps
    # Use composite key (screen:check) and sequential index for reliable matching
    enriched_gaps = {}  # composite_key → enriched data
    enriched_gaps_seq = []  # sequential list for index-based fallback
    for eg in enriched.get('gaps', []):
        enr_data = eg.get('enriched', {})
        # Primary key: screen + check text (guaranteed unique)
        scr = eg.get('screen', '')
        chk = eg.get('check', '')[:80]
        enriched_gaps[f'{scr}:{chk}'] = enr_data
        # Sequential fallback
        enriched_gaps_seq.append(enr_data)
    enriched_uxps = {}  # UXP-ID → enriched data
    for ep in enriched.get('proposals', []):
        enriched_uxps[ep.get('id', '')] = ep
    enriched_cats = enriched.get('category_scores', {})

    # ── Build sections ──
    nav_html = '<nav class="nav">\n  <a href="#summary">Tổng quan</a>\n  <a href="#method">Phương pháp</a>\n  <a href="#findings">Phát hiện</a>\n  <a href="#scorecard">Scorecard</a>\n'
    if gaps:
        nav_html += '  <a href="#gaps">Gaps</a>\n'
    nav_html += '</nav>'

    hero_ring = score_ring_svg(score)
    hero_html = f'''<section class="hero" id="top">
  <div class="hero-label">UX Audit Report</div>
  <h1>{e(hero_title)}</h1>
  <p class="hero-sub">{e(product)}</p>
  <div class="hero-stats">
    <div class="stat-item"><span class="stat-num">{meta['screens']}</span><span class="stat-label">Màn hình</span></div>
    <div class="stat-item"><span class="stat-num">{meta['checks']}</span><span class="stat-label">Tổng kiểm tra</span></div>
    <div class="stat-item"><span class="stat-num gap-c">{meta['gap']}</span><span class="stat-label">Cần cải thiện</span></div>
    <div class="stat-item"><span class="stat-num">{meta['proposals']}</span><span class="stat-label">Đề xuất</span></div>
  </div>
  <div class="hero-score">{hero_ring}</div>
</section>'''

    # Summary
    summary_cards = ''
    for scr in screens:
        scr_score = int(scr['score'])  # type: ignore[arg-type]
        ring = score_ring_svg(scr_score, size=56, font_size=13, stroke_width=5)
        gap_count = scr['gap']
        sev_color = 'var(--sev-critical-fg)' if gap_count >= 4 else 'var(--sev-major-fg)' if gap_count >= 2 else 'var(--sev-minor-fg)'  # type: ignore[operator]
        summary_cards += f'''    <div class="score-item reveal">
      <div style="flex-shrink:0">{ring}</div>
      <div class="score-info">
        <h4>{e(scr["title"])}</h4>
        <p>{scr["id"]} · {scr["type"]} · <span style="color:{sev_color}">{gap_count} hạng mục cần cải thiện</span></p>
      </div>
    </div>\n'''

    summary_html = f'''<section class="section" id="summary">
  <div class="section-title"><span class="icon">📊</span> 01 · Tổng quan kết quả kiểm tra</div>
  <div style="display:flex;gap:12px;margin-bottom:28px">
    <span class="badge critical">🔴 {meta["critical"]} Nghiêm trọng</span>
    <span class="badge major">🟡 {meta["major"]} Quan trọng</span>
    <span class="badge minor">⚪ {meta["minor"]} Cải thiện</span>
  </div>
  <div class="scorecard-grid">
{summary_cards}  </div>
</section>'''

    method_html = '''<section class="section reveal" id="method">
  <div class="section-title"><span class="icon">🔬</span> 02 · Phương pháp đánh giá</div>
  <div class="method-grid">
    <div class="method-card"><div class="method-icon">🔍</div><h4>Đánh giá Heuristic</h4><p>Kiểm tra theo 10 nguyên tắc khả dụng của Nielsen Norman Group. Mỗi phát hiện được truy vết đến heuristic cụ thể bị vi phạm cùng mức độ ảnh hưởng.</p></div>
    <div class="method-card"><div class="method-icon">🧩</div><h4>Đối chiếu thông số thiết kế</h4><p>So sánh thiết kế Figma với thông số thành phần DDL (Design Data Layer) để phát hiện sai lệch về trạng thái, thuộc tính và hành vi tương tác.</p></div>
    <div class="method-card"><div class="method-icon">👁️</div><h4>Kiểm tra trực quan</h4><p>Phân tích từng màn hình: căn chỉnh bố cục, tương phản màu sắc, font chữ, vùng chạm tối thiểu, và phát hiện lớp phủ (overlay).</p></div>
    <div class="method-card"><div class="method-icon">⚖️</div><h4>Đối chiếu nguyên tắc UX</h4><p>Áp dụng Định luật Fitts, Định luật Hick, Hiệu ứng Peak-End và các nguyên tắc thiết kế tương tác vào từng màn hình.</p></div>
  </div>
</section>'''

    # Findings
    findings_html = '<section class="section" id="findings">\n  <div class="section-title"><span class="icon">🔎</span> 03 · Các vấn đề được phát hiện</div>\n'
    severity_labels = {
        'critical': ('🔴 Nghiêm trọng — Cần xử lý ngay', 'sev-critical'),
        'major': ('🟡 Quan trọng — Ưu tiên cao', 'sev-major'),
        'minor': ('⚪ Cải thiện — Nâng cao trải nghiệm', 'sev-minor'),
    }
    # Track used images for deduplication across ALL UXPs (not per severity)
    used_images_global: set[str] = set()

    for sev in ['critical', 'major', 'minor']:
        sev_props = [p for p in proposals if p['severity'] == sev]
        if not sev_props: continue
        label, css_var = severity_labels[sev]
        findings_html += f'''\n  <div style="margin-bottom:36px">
    <div style="background:var(--{css_var}-bg);padding:10px 18px;border-radius:8px;font-family:var(--font-mono);font-size:12px;font-weight:700;color:var(--{css_var}-fg);margin-bottom:20px;letter-spacing:.3px">{label}</div>\n'''

        # ── Build screen→prefix mapping for image pool filtering ──
        scr_to_prefix: dict[str, list[str]] = {}
        if available_imgs:
            prefix_groups: dict[str, list[str]] = {}
            for _img_name in sorted(available_imgs):
                parts = _img_name.replace('.png', '').split('-')
                if len(parts) >= 2:
                    prefix = '-'.join(parts[:2])  # type: ignore[index]
                    prefix_groups.setdefault(prefix, []).append(_img_name)
            for prop_item in sev_props:
                scr_m = re.search(r'(SCR-[\w-]+)', prop_item.get('screen', '') + ' ' + prop_item.get('violation', ''))
                if scr_m:
                    scr_id = scr_m.group(1)
                    if scr_id not in scr_to_prefix:
                        inv_imgs = scr_image_map.get(scr_id, []) if scr_image_map else []  # type: ignore[union-attr]
                        if inv_imgs:
                            for inv_img in inv_imgs:
                                parts = inv_img.replace('.png', '').split('-')
                                if len(parts) >= 2:
                                    pfx = '-'.join(parts[:2])
                                    if pfx in prefix_groups:
                                        scr_to_prefix[scr_id] = prefix_groups[pfx]  # type: ignore[index]
                                        break


        for prop in sev_props:
            card_title = prop.get('_title_override') or smart_title(prop['hiện_trạng'])
            heur = heuristic_display(prop['ddl'], prop['ux_law'], prop['violation'])
            impact = prop['user_impact'] or infer_user_impact(prop['hiện_trạng'], '')

            # Image resolution — 5-tier strategy (state-aware prioritized)
            img_src = ''
            # Tier 1: evidence_img from report parsing (explicit .png reference)
            img_name = prop['evidence_img']
            if img_name and img_name in available_imgs:  # type: ignore[operator]
                img_src = f'{ui_base}/{img_name}'
            # Tier 0.5: Direct artboard ID from hiện trạng text
            # If text mentions "(7203)" or "popup (7100)", map directly to *{id}*.png
            if not img_src:
                ht_text = prop.get('hiện_trạng', '') or ''
                artboard_ids = re.findall(r'\b(\d{4,5})\b', ht_text)
                for aid in artboard_ids:
                    for a_img in sorted(available_imgs):
                        if aid in a_img:
                            img_src = f'{ui_base}/{a_img}'
                            break
                    if img_src:
                        break
            # Tier 1.5: Screen MD-based check→image mapping (authoritative)
            # Uses Gap ref "Check #N1, #N2 (SCR-XXX)" → parsed from screen .md
            if not img_src and check_image_map:
                gap_ref = prop.get('violation', '') or ''
                combined_ref = gap_ref + ' ' + (prop.get('screen', '') or '')
                # 2-step: extract SCR-ID + all check numbers from multi-check format
                check_refs: list[tuple[str, str]] = []
                # Handle "Check #1, #2, #3 (SCR-XXX)" — extract SCR-ID, then all #N
                multi_m = re.search(r'Check\s+((?:#\d+(?:\s*,\s*)?)+)\s*\((SCR-[\w-]+)\)', combined_ref)
                if multi_m:
                    scr_id_ref = multi_m.group(2)
                    all_nums = re.findall(r'#(\d+)', multi_m.group(1))
                    check_refs = [(n, scr_id_ref) for n in all_nums]
                else:
                    # Fallback: single "Check #N (SCR-XXX)"
                    check_refs = re.findall(r'Check\s*#(\d+)\s*\((SCR-[\w-]+)\)', combined_ref)
                for check_num, check_scr_id in check_refs:
                    ck = f'Check #{check_num} ({check_scr_id})'
                    if ck in check_image_map:
                        mapped_img = check_image_map[ck]
                        if mapped_img not in used_images_global or not img_src:  # type: ignore[operator]
                            img_src = f'{ui_base}/{mapped_img}'
                            break
            # Tier 2: all_imgs from cross-reference
            if not img_src and prop.get('all_imgs'):
                for c in prop['all_imgs']:
                    if c in available_imgs:  # type: ignore[operator]
                        img_src = f'{ui_base}/{c}'; break
            # Tier 2.5: Artboard ID from text patterns (broader than Tier 0.5 — also checks screen field)
            if not img_src:
                combined_text = (prop.get('hiện_trạng', '') + ' ' + prop.get('screen', '') + ' ' + prop.get('violation', ''))
                artboard_ids = re.findall(r'\b(\d{4,5})\b', combined_text)
                for aid in artboard_ids:
                    for img in sorted(available_imgs):
                        if img.startswith(aid + '-') or img.startswith(aid + '_'):
                            img_src = f'{ui_base}/{img}'; break
                    if img_src: break
            # Tier 3: State-Aware Image Resolution (BEFORE generic screen mapping)
            # Two-phase: (1) Narrow images by screen prefix, (2) Score by context match
            if not img_src:
                uxp_context = (prop.get('hiện_trạng', '') + ' ' +
                               prop.get('_title_override', '') + ' ' +
                               prop.get('user_impact', '')).lower()

                # Phase 1: Get screen prefix from screen field → narrow image pool
                screen_field = prop.get('screen', '')
                scr_prefix = ''
                # Extract meaningful prefix from screen path like "Dịch vụ thẻ › Danh sách thẻ"
                scr_parts = re.split(r'[›/]', screen_field)
                if len(scr_parts) >= 2:
                    last_part = vn_normalize(scr_parts[-1].strip())
                    scr_prefix = last_part.replace(' ', '-')[:20]  # type: ignore[index]

                # Phase 2: State scoring — each pattern has specificity weight
                state_rules = [
                    # (pattern, file_keywords, specificity_weight)
                    # Higher weight = more specific = prioritized

                    # ── High specificity (10) — unique state indicators ──
                    (r'date[\s_-]?picker|calendar|chọn[\s_-]?ngày', ['date-picker', 'calendar'], 10),
                    (r'empty[\s_-]?state|trạng[\s_-]?thái[\s_-]?rỗng|không[\s_-]?có[\s_-]?dữ[\s_-]?liệu', ['trong', 'empty', 'rong'], 10),
                    (r'filter|lọc|bộ[\s_-]?lọc', ['filter', 'loc', 'bo-loc'], 10),
                    (r'expired|hết[\s_-]?hạn|quá[\s_-]?hạn', ['expired', 'het-han'], 10),

                    # ── High specificity (9) — auth/security states ──
                    (r'otp[\s_-]?input|nhập[\s_-]?otp|canResend|xác[\s_-]?thực', ['xac-thuc', 'otp', 'xac-nhan'], 9),
                    (r'(?:đang|thẻ)[\s_-]?(?:khoá|khóa|bị[\s_-]?khoá)|\bẩn\b.{0,15}kh', ['yang-khoa', 'khoa', 'locked'], 9),
                    (r'chờ[\s_-]?kích[\s_-]?hoạt|chưa[\s_-]?kích', ['cho-kich-hoat', 'pending'], 9),
                    (r'case[\s_-]?lỗi|modal[\s_-]?error|popup[\s_-]?lỗi|thất[\s_-]?bại|fail', ['case-loi', 'loi', 'fail', 'error'], 9),
                    (r'huỷ|cancel|từ[\s_-]?chối', ['cancel', 'huy', 'tu-choi'], 9),
                    (r'face[\s_-]?id|biometric|vân[\s_-]?tay', ['face-id', 'biometric', 'van-tay'], 9),
                    (r'change[\s_-]?password|đổi[\s_-]?mật[\s_-]?khẩu', ['change-password', 'doi-mat-khau'], 9),

                    # ── Medium specificity (8) — form/flow states ──
                    (r'thẻ[\s_-]?phụ|sub[\s_-]?card', ['the-phu'], 8),
                    (r'\bpopup\b|\bmodal\b|bottom[\s_-]?sheet', ['popup', 'modal', 'noti', 'thong-bao'], 8),
                    (r'form[\s_-]?empty|form[\s_-]?trống|thiếu[\s_-]?field', ['empty', 'form-empty'], 8),
                    (r'form[\s_-]?filled|đã[\s_-]?điền|nhập[\s_-]?đầy', ['filled', 'form-filled'], 8),
                    (r'\bexpanded\b|mở[\s_-]?rộng', ['expanded', 'mo-rong', 'expand'], 8),
                    (r'settings|cài[\s_-]?đặt|tuỳ[\s_-]?chọn', ['settings', 'cai-dat'], 8),

                    # ── Medium specificity (7) — result/confirmation states ──
                    (r'kết[\s_-]?quả|result|thành[\s_-]?công|success', ['ket-qua', 'result', 'thanh-cong', 'success'], 7),
                    (r'xác[\s_-]?nhận|confirm|review', ['xac-nhan', 'confirm', 'review'], 7),
                    (r'receipt|biên[\s_-]?lai', ['chi-tiet', 'ket-qua', 'detail', 'receipt'], 7),
                    (r'hạn[\s_-]?mức|tín[\s_-]?dụng|dư[\s_-]?nợ|thông[\s_-]?tin[\s_-]?thẻ', ['thong-tin-the', 'chi-tiet'], 7),
                    (r'chữ[\s_-]?ký|signature|ký[\s_-]?số', ['chu-ky', 'signature'], 7),
                    (r'phương[\s_-]?thức|method|chọn[\s_-]?phương', ['phuong-thuc', 'method'], 7),

                    # ── Lower specificity (6) — list/history views ──
                    (r'transaction|lịch[\s_-]?sử|giao[\s_-]?dịch', ['lsgd', 'giao-dich', 'transaction'], 6),
                    # Removed: danh sách too generic for Vietnamese
                    (r'attempt[\s_-]?counter|lockout|bộ[\s_-]?đếm', ['case-loi', 'loi'], 6),

                    # ── Low specificity (3-4) — generic states ──
                    (r'pin[\s_-]?overlay|nhập[\s_-]?pin|xác[\s_-]?nhận[\s_-]?pin', ['xac-thuc', 'otp', 'pin'], 8),
                    (r'\bpin\b|mã[\s_-]?pin', ['pin', 'mat-khau'], 4),
                    (r'hoạt[\s_-]?động|active', ['hoat-yong', 'hoat-dong', 'active'], 3),
                    # Removed: chi tiết/thông tin too generic for Vietnamese
                ]

                # Determine image search pool: screen-filtered first, then all
                scr_id_for_pool = re.search(r'(SCR-[\w-]+)', prop.get('screen', '') + ' ' + prop.get('violation', ''))
                screen_pool = scr_to_prefix.get(scr_id_for_pool.group(1), []) if scr_id_for_pool else []  # type: ignore[union-attr]
                # Use screen-filtered pool if available, else all images
                search_pool = screen_pool if screen_pool else sorted(available_imgs)

                best_score = 0
                best_state_img = None
                for pattern, file_keywords, weight in state_rules:
                    m = re.search(pattern, uxp_context, re.IGNORECASE)
                    if m:
                        # Find best matching image (prefer unused)
                        for img in search_pool:
                            img_lower = img.replace('.png', '').lower()
                            for kw in file_keywords:
                                if kw in img_lower:  # type: ignore[operator]
                                    # Bonus: image prefix matches screen prefix
                                    prefix_bonus = 2 if scr_prefix and scr_prefix[:8] in img_lower else 0  # type: ignore[index,operator]
                                    # Penalty: already used by another UXP
                                    dedup_penalty = -3 if img in used_images_global else 0
                                    score = weight + prefix_bonus + dedup_penalty
                                    if score > best_score:
                                        best_score = score
                                        best_state_img = img
                                    break

                # Fallback: Sequential index mapping for numbered files
                # If no state matched, try to map UXP-NNN to the Nth image file
                if not best_state_img:
                    # Use screen pool for sequential fallback too
                    seq_pool = screen_pool if screen_pool else sorted(available_imgs)
                    uxp_num = re.search(r'UXP-0*(\d+)', prop.get('id', ''))
                    if uxp_num and seq_pool:
                        idx = int(uxp_num.group(1)) - 1
                        if 0 <= idx < len(seq_pool):
                            best_state_img = seq_pool[idx]

                if best_state_img:
                    # If best image already used, try to find RELEVANT unused alternative
                    if best_state_img in used_images_global and best_score > 0:  # type: ignore[operator]
                        # Only replace if we find an unused image that also matches a state keyword
                        # (don't fall back to a random unrelated image)
                        scr_id_dedup = re.search(r'(SCR-[\w-]+)', prop.get('screen', '') + ' ' + prop.get('violation', ''))
                        scr_pool_dedup = scr_to_prefix.get(scr_id_dedup.group(1), []) if scr_id_dedup else []
                        alt_pool = scr_pool_dedup if scr_pool_dedup else search_pool
                        # Collect all keywords that matched for this UXP
                        matched_kws: set[str] = set()
                        for pattern, file_keywords, weight in state_rules:
                            if re.search(pattern, uxp_context, re.IGNORECASE):
                                matched_kws.update(file_keywords)
                        # Find unused image that shares any matched keyword
                        for alt_img in alt_pool:
                            if alt_img not in used_images_global:  # type: ignore[operator]
                                alt_lower = alt_img.replace('.png', '').lower()
                                if any(kw in alt_lower for kw in matched_kws):
                                    best_state_img = alt_img
                                    break
                        # If no relevant alternative found, keep the duplicate (better than random)
                    img_src = f'{ui_base}/{best_state_img}'
                    used_images_global.add(best_state_img)  # type: ignore[union-attr]


            # Tier 4: screen_inventory.json generic scr→image mapping (fallback)
            if not img_src and scr_image_map:
                scr_id_m = re.search(r'(SCR-[\w-]+)', prop.get('violation', '') + ' ' + prop.get('screen', ''))
                if scr_id_m:
                    scr_id = scr_id_m.group(1)
                    inv_imgs = scr_image_map.get(scr_id, [])
                    for inv_img in inv_imgs:
                        if inv_img in available_imgs:  # type: ignore[operator]
                            img_src = f'{ui_base}/{inv_img}'; break

            # Tier 5: Fuzzy screen name match (last resort)
            if not img_src:
                screen_text = vn_normalize(prop.get('screen', ''))
                for img in sorted(available_imgs):
                    img_base = img.replace('.png', '').replace('-', ' ').lower()
                    words = [w for w in re.split(r'[\s›/]+', screen_text) if len(w) >= 4]
                    matched = sum(1 for w in words if w in img_base)
                    if matched >= 2:
                        img_src = f'{ui_base}/{img}'; break
                if not img_src and available_imgs:
                    img_src = f'{ui_base}/{sorted(available_imgs)[0]}'

            ovl = overlay_summary(prop['hiện_trạng'])
            ovl_class = f'shot-overlay {sev}' if sev != 'critical' else 'shot-overlay'

            tech_ref = prop['ddl']
            if prop['ux_law'] and prop['ux_law'] != '—':
                tech_ref += f", Law:{prop['ux_law']}"

            # ── 4-Block Card: Hiện trạng → Tác động → Heuristic → Đề xuất ──

            # Block 1: Hiện trạng — from enriched data or parsed field
            uxp_enr = enriched_uxps.get(prop['id'], {})
            hien_trang_text = prop.get('hiện_trạng', card_title)
            if not hien_trang_text or hien_trang_text == card_title:
                hien_trang_text = card_title

            # Augment shallow hiện trạng with screen MD context
            if screen_specs:
                hien_trang_text = augment_uxp_hien_trang(
                    hien_trang_text, prop, screen_specs, check_content_map
                )

            # Block 2: Tác động — enriched impact or inferred
            tac_dong_text = impact

            # Block 3: Heuristic vi phạm — full name + description from enriched data
            heur_full = heur
            heur_details = uxp_enr.get('heuristics', [])
            if heur_details:
                h0 = heur_details[0]
                h_name = h0.get('name', '')
                h_desc = h0.get('desc', '')
                if h_name and h_desc:
                    heur_full = f'{h_name} — {h_desc}'
                elif h_name:
                    heur_full = h_name

            # Block 4: Đề xuất cải thiện — with explicit label
            proposed = ''
            if prop['giải_pháp']:
                items = ''.join(f'<li>{e(s)}</li>' for s in prop['giải_pháp'])
                proposed = f'''
          <div class="finding-section"><h4>Đề xuất cải thiện</h4>
            <div class="proposed-box"><ul>{items}</ul></div>
          </div>'''

            _sev_vi = {'critical': 'Nghiêm trọng', 'major': 'Quan trọng', 'minor': 'Cải thiện'}.get(sev, sev)

            findings_html += f'''    <div class="finding-card reveal">
      <div class="finding-accent {sev}"></div>
      <div class="card-layout">
        <div class="card-visual"><div class="phone-frame"><img src="{img_src}" alt="{e(ovl)}" loading="lazy"></div><div class="{ovl_class}">⚠️ {e(ovl)}</div></div>
        <div class="card-info">
          <div class="card-top"><span class="card-id">{prop["id"]}</span><span class="badge {sev}">{_sev_vi}</span></div>
          <h3>{e(card_title)}</h3>
          <div class="finding-section"><h4>Hiện trạng</h4><p>{e(hien_trang_text)}</p></div>
          <div class="finding-section"><h4>Tác động</h4><p>{e(tac_dong_text)}</p></div>
          <div class="finding-section"><h4>Nguyên tắc bị vi phạm</h4><p>{e(heur_full)}</p></div>{proposed}
          <div class="finding-tags"><span class="card-tag">{e(prop["screen"])}</span></div>
          <details><summary>Xem tham chiếu kỹ thuật →</summary><div class="detail-content">{e(tech_ref)}</div></details>
        </div>
      </div>
    </div>\n'''
        findings_html += '  </div>\n'
    findings_html += '</section>'

    # Scorecard — use real category scores from enriched data if available
    cat_order = ['flow', 'error', 'status', 'touch', 'consistency', 'content']
    cat_fallback = [
        ('flow', 'Luồng người dùng', 'Flow & Navigation'),
        ('error', 'Xử lý lỗi', 'Error Handling'),
        ('status', 'Trạng thái hệ thống', 'System Status'),
        ('touch', 'Điểm chạm & Mục tiêu', 'Touch & Target'),
        ('consistency', 'Nhất quán & Tiêu chuẩn', 'Consistency'),
        ('content', 'Nội dung & Trình bày', 'Content & Layout'),
    ]
    scorecard_items = ''
    for i, (cat_id, fb_vi, fb_en) in enumerate(cat_fallback):
        cat_data: dict[str, Any] = enriched_cats.get(cat_id, {})  # type: ignore[union-attr]
        if cat_data:
            cat_score = cat_data.get('score', score)
            vi_name = cat_data.get('name_vi', fb_vi)
            en_name = cat_data.get('name_en', fb_en)
            cat_total = cat_data.get('total', 0)
            cat_pass = cat_data.get('pass', 0)
            cat_gap = cat_data.get('gap', 0)
            est = cat_data.get('estimated', False)
        else:
            # Fallback: use old formula when no enriched data
            cat_score = max(20, min(100, score + (i * 7 - 15) % 25 - 10))  # type: ignore[operator]
            vi_name = fb_vi
            en_name = fb_en
            cat_total = 0
            cat_pass = 0
            cat_gap = 0
            est = True

        ring = score_ring_svg(cat_score, size=72, font_size=14, stroke_width=6)
        breakdown = ''
        if cat_total > 0:
            breakdown = f'<p style="font-size:11px;color:var(--text-muted);margin:2px 0 0">{cat_pass}✅ {cat_gap}❌ / {cat_total} hạng mục</p>'
        elif est:
            breakdown = f'<p style="font-size:11px;color:var(--text-muted);margin:2px 0 0;opacity:0.6">ước tính</p>'

        scorecard_items += f'''    <div class="score-item reveal" style="flex-direction:column;text-align:center">
      {ring}
      <div class="score-info" style="margin-top:8px;text-align:center"><h4>{e(vi_name)}</h4><p>{e(en_name)}</p>{breakdown}</div>
    </div>\n'''

    scorecard_html = f'''<section class="section" id="scorecard">
  <div class="section-title"><span class="icon">📊</span> 04 · Đánh giá theo danh mục heuristic</div>
  <div class="scorecard-grid">
{scorecard_items}  </div>
</section>'''

    gap_html = generate_gap_html(gaps, screens, enriched_gaps)

    footer_html = f'''<footer>
  <p><strong>{e(product)}</strong> · {e(title)} · Đánh giá trải nghiệm người dùng dựa trên thông số thiết kế (DDL)</p>
</footer>'''

    script_html = '''<script>
document.addEventListener('DOMContentLoaded',()=>{
  const obs=new IntersectionObserver((entries)=>{
    entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target)}})
  },{threshold:0.12});
  document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));
});
</script>'''

    # Assemble
    full_html = f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>UX Audit — {e(title)} | {e(product)}</title>
<style>
{css}
</style>
</head>
<body>
{nav_html}

{hero_html}

{summary_html}

{method_html}

{findings_html}

{scorecard_html}

{gap_html}

{footer_html}

{script_html}

</body>
</html>
'''

    output = Path(args.output)
    if not args.dry:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(full_html, encoding='utf-8')

    # JSON summary to stdout — count actual image usage in HTML
    images_mapped = len(set(re.findall(r'src="' + re.escape(ui_base) + r'/([^"]+)"', full_html)))
    result = {
        'screens': meta['screens'], 'checks': meta['checks'],
        'gaps': meta['gap'], 'proposals': len(proposals),
        'score': score, 'critical': meta['critical'],
        'major': meta['major'], 'minor': meta['minor'],
        'gap_items': len(gaps),
        'images_mapped': images_mapped,
        'images_available': len(available_imgs),
        'output': str(output),
        'dry_run': args.dry,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return True


# ═══════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='Generate UX Audit Pitch Deck from ux-review-report.md',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__  # type: ignore[name-defined]
    )
    parser.add_argument('--report', required=True, help='Path to ux-review-report.md')
    parser.add_argument('--output', default='', help='Output HTML file path (auto-generated from folder if omitted)')
    parser.add_argument('--ui-dir', help='Directory containing UI screenshots')
    parser.add_argument('--product', default='', help='Product name')
    parser.add_argument('--client', default='', help='Client name')
    parser.add_argument('--module', default='', help='Module name')
    parser.add_argument('--template', help='Custom template HTML path')
    parser.add_argument('--dry', action='store_true', help='Preview only')

    args = parser.parse_args()

    if args.template:
        global TEMPLATE_PATH
        TEMPLATE_PATH = Path(args.template)

    # Auto-generate output name if not specified
    if not args.output:
        report = Path(args.report)
        args.output = str(report.parent / auto_output_name(report))  # type: ignore[attr-defined]
        print(f'📝 Auto output: {args.output}', file=sys.stderr)

    success = generate(args)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
