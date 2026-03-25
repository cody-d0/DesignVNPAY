#!/usr/bin/env python3
"""
enrich.py — DDL-grounded LLM reasoning for pitch deck content.

Loads DDL context first, then enriches each Gap and UXP with:
- Professional impact analysis
- Severity justification
- Heuristic/law references with descriptions
- Real category scores (replaces fake formula)

Usage:
    python3 enrich.py --report path/to/ux-review-report.md
    → Outputs enriched-data.json next to report
"""

import json, re, sys, argparse, hashlib
from typing import Any
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from generate import parse_proposals  # type: ignore[import-not-found]


# ═══════════════════════════════════════════════════════════
# DDL CONTEXT LOADER
# ═══════════════════════════════════════════════════════════

def load_ddl(report_path: Path) -> dict:
    """Load DDL context from .handoff/ddl-context.json relative to report."""
    ddl_path = report_path.parent / '.handoff' / 'ddl-context.json'
    if not ddl_path.exists():
        return {}
    return json.loads(ddl_path.read_text(encoding='utf-8'))


def build_ddl_lookups(ddl: dict) -> dict:
    """Build fast lookup maps from DDL data."""
    lookups: dict[str, Any] = {
        'guidelines': {},    # id → guideline dict
        'components': {},    # comp_id → spec dict
        'ux_laws': {},       # id → law dict
        'law_by_keyword': {},# keyword → law
        'screen_comps': {},  # SCR-XXX → [comp_ids]
        'tokens': {},        # token_name → resolved value
    }

    # Guidelines by ID
    for section in ['high_severity', 'web_interface']:
        for g in ddl.get('guidelines', {}).get(section, []):
            if isinstance(g, dict) and 'id' in g:
                lookups['guidelines'][g['id']] = g  # type: ignore[index]

    # Component specs
    for comp_id, spec in ddl.get('component_specs', {}).items():
        lookups['components'][comp_id] = spec

    # UX Laws
    for law in ddl.get('ux_laws', {}).get('all', []):
        if isinstance(law, dict):
            lookups['ux_laws'][law.get('id', '')] = law
            # Index by keyword fragments
            for kw in law.get('keywords', '').split():
                lookups['law_by_keyword'][kw.lower()] = law

    # Screen → components
    for scr_id, comps in ddl.get('screen_components', {}).items():
        if isinstance(comps, list):
            lookups['screen_comps'][scr_id] = comps
        elif isinstance(comps, dict):
            lookups['screen_comps'][scr_id] = list(comps.keys())

    # Resolved tokens
    lookups['tokens'] = ddl.get('resolved_tokens', {})

    return lookups


# ═══════════════════════════════════════════════════════════
# HEURISTIC / REFERENCE RESOLVER
# ═══════════════════════════════════════════════════════════

# Master heuristic knowledge base
HEURISTIC_KB = {
    # Nielsen 10
    'UXG-044': {'name': 'User Control & Freedom', 'nielsen': 3,
                'desc': 'Users can undo/redo and exit unwanted states easily'},
    'UXG-052': {'name': 'Aesthetic & Minimalist Design', 'nielsen': 8,
                'desc': 'Remove distracting content; focus on essential information'},
    'UXG-087': {'name': 'Real-time Validation Feedback', 'nielsen': 1,
                'desc': 'System provides immediate feedback on user input'},
    'UXG-112': {'name': 'Error Prevention', 'nielsen': 5,
                'desc': 'Prevent errors via constraints, confirmations, defaults'},
    'UXG-165': {'name': 'Consistency & Standards', 'nielsen': 4,
                'desc': 'Follow platform conventions; same words/actions mean same things'},
    'UXG-176': {'name': 'Error Feedback', 'nielsen': 9,
                'desc': 'Error messages in plain language, precisely indicate problem, suggest fix'},
    'UXG-183': {'name': 'ARIA Labels (WCAG)', 'category': 'Accessibility',
                'desc': 'Interactive elements must have accessible names for screen readers'},
    'UXG-243': {'name': 'WCAG AA Contrast', 'category': 'Accessibility',
                'desc': 'Text contrast ratio ≥ 4.5:1 for normal text, ≥ 3:1 for large text'},
    # UX Laws
    'fitts': {'name': "Fitts's Law", 'category': 'Motor',
              'desc': 'Time to reach target = f(distance/size). Touch targets ≥ 44×44px'},
    'hick': {'name': "Hick's Law", 'category': 'Cognitive',
             'desc': 'Decision time increases logarithmically with number of choices'},
    'zeigarnik': {'name': 'Zeigarnik Effect', 'category': 'Cognitive',
                  'desc': 'People remember incomplete tasks better. Progress indicators leverage this'},
    'miller': {'name': "Miller's Law", 'category': 'Cognitive',
               'desc': 'Working memory holds 7±2 items. Chunk information accordingly'},
    'jakob': {'name': "Jakob's Law", 'category': 'Behavioral',
              'desc': 'Users spend most time on other apps. Your app should work similarly'},
}

# Category mapping for scorecard
CATEGORY_KEYWORDS = {
    'flow': {
        'keywords': ['flow', 'navigation', 'progress', 'step', 'zeigarnik', 'luồng',
                     'redirect', 'destination', 'sticky', 'cta', 'action', 'transition'],
        'name_vi': 'Luồng người dùng',
        'name_en': 'Flow & Navigation',
    },
    'error': {
        'keywords': ['error', 'validation', 'inline', 'modal', 'feedback', 'warning',
                     'red border', 'lỗi', 'catch', 'exception', 'fallback', 'empty state'],
        'name_vi': 'Xử lý lỗi',
        'name_en': 'Error Handling',
    },
    'status': {
        'keywords': ['status', 'loading', 'countdown', 'timer', 'attempt', 'lockout',
                     'resend', 'otp', 'state', 'skeleton', 'indicator', 'confirmation'],
        'name_vi': 'Trạng thái hệ thống',
        'name_en': 'System Status',
    },
    'touch': {
        'keywords': ['touch', 'target', 'fitts', '44px', '48px', 'tap', 'click',
                     'button', 'spacing', 'size', 'mobile', 'accessible'],
        'name_vi': 'Điểm chạm & Mục tiêu',
        'name_en': 'Touch & Target',
    },
    'consistency': {
        'keywords': ['consistency', 'standard', 'label', 'nhất quán', 'terminology',
                     'pattern', 'convention', 'platform', 'brand', 'uniform'],
        'name_vi': 'Nhất quán & Tiêu chuẩn',
        'name_en': 'Consistency & Standards',
    },
    'content': {
        'keywords': ['content', 'layout', 'typography', 'contrast', 'wcag', 'color',
                     'text', 'information', 'architecture', 'hierarchy', 'badge',
                     'helper', 'placeholder', 'mask', 'show/hide', 'eye icon',
                     'pii', 'security', 'sensitive'],
        'name_vi': 'Nội dung & Trình bày',
        'name_en': 'Content & Layout',
    },
}


def resolve_heuristic_ref(ref: str, lookups: dict) -> dict:
    """Resolve a DDL/heuristic reference to full description."""
    ref_clean = ref.replace('`', '').strip()

    # Skip severity-only refs — they are not heuristic references
    if ref_clean.lower() in {'critical', 'major', 'minor', '—', '-', ''}:
        return {'name': '', 'category': '', 'desc': ''}

    # 1. Try HEURISTIC_KB (hardcoded knowledge)
    if ref_clean in HEURISTIC_KB:
        return HEURISTIC_KB[ref_clean]

    # 2. Try UXG-NNN → DDL guideline
    m = re.search(r'UXG-(\d+)', ref_clean)
    if m:
        gid = int(m.group(1))
        gl = lookups['guidelines'].get(gid)
        if gl:
            return {
                'name': gl.get('issue', ref_clean),
                'category': gl.get('category', ''),
                'desc': gl.get('description', ''),
                'do': gl.get('do_example', ''),
                'dont': gl.get('dont_example', ''),
            }
        # Fallback to KB entry
        kb = HEURISTIC_KB.get(ref_clean)
        if kb:
            return kb

    # 3. Try COMP:xxx → component spec
    if ref_clean.startswith('COMP:'):
        comp_id = ref_clean.replace('COMP:', '')
        comp = lookups['components'].get(comp_id)
        if comp:
            return {
                'name': f'Component: {comp_id}',
                'category': 'Component Spec',
                'desc': comp.get('description', ''),
                'deps': comp.get('shadcnDeps', []),
            }

    # 4. Try keyword match in UX laws
    for kw in ref_clean.lower().split():
        law = lookups['law_by_keyword'].get(kw)
        if law:
            return {
                'name': law.get('name', ref_clean),
                'category': law.get('category', 'UX Law'),
                'desc': law.get('statement', ''),
            }

    return {'name': ref_clean, 'category': 'Unknown', 'desc': ''}


def classify_check_category(check_text: str, ref: str) -> str:
    """Classify a check into one of 6 scorecard categories."""
    combined = (check_text + ' ' + ref).lower()
    scores = {}
    for cat_id, cat_data in CATEGORY_KEYWORDS.items():
        score = sum(1 for kw in cat_data['keywords'] if kw in combined)
        if score > 0:
            scores[cat_id] = score

    if scores:
        return max(scores, key=lambda k: scores[k])
    return 'content'  # default fallback


# ═══════════════════════════════════════════════════════════
# IMPACT REASONING ENGINE (DDL-grounded, no external LLM)
# ═══════════════════════════════════════════════════════════

# Global tracker for per-gap impact uniqueness
_used_impacts: set[str] = set()


def reset_impact_tracker() -> None:
    """Reset used impacts tracker — call at start of each enrichment run."""
    global _used_impacts
    _used_impacts = set()


def reason_gap_impact(gap: dict, heuristic_info: dict, lookups: dict) -> dict:
    """Generate professional, DDL-grounded impact analysis for a gap.

    Guarantees unique impact text per gap via _used_impacts tracking.
    """
    check = gap.get('check', '')
    ref = gap.get('ref', '')
    screen = gap.get('screen', '')
    source = gap.get('source', '')

    # Get component context if available
    comp_context = ''
    comp_match = re.search(r'COMP:([\w-]+)', ref)
    if comp_match:
        comp_id = comp_match.group(1)
        comp = lookups['components'].get(comp_id, {})
        if comp:
            comp_context = comp.get('description', '')
            # Get the screen(s) using this component
            using_screens = [s for s, comps in lookups['screen_comps'].items()
                           if comp_id in comps]
            if using_screens:
                comp_context += f' (used in: {", ".join(using_screens)})'

    h_name = heuristic_info.get('name', '')
    h_desc = heuristic_info.get('desc', '')
    h_cat = heuristic_info.get('category', '')
    nielsen = heuristic_info.get('nielsen')

    # Build structured impact
    result: dict[str, Any] = {
        'heuristic_name': h_name,
        'heuristic_desc': h_desc,
        'heuristic_category': h_cat,
        'component_context': comp_context,
    }

    # Professional heuristic tag (Vietnamese-ready)
    if nielsen:
        result['heuristic_tag'] = f'Nielsen #{nielsen}: {h_name}'
    elif h_cat:
        result['heuristic_tag'] = f'{h_cat}: {h_name}'
    else:
        result['heuristic_tag'] = h_name

    # Impact reasoning — UNIQUE per gap
    impact = _generate_impact_text_unique(check, ref, h_name, h_cat, comp_context, screen, gap.get('num', 0))
    result['impact'] = impact

    # Hiện trạng — per-gap specific description (for 4-block card)
    result['hiện_trạng'] = _generate_hien_trang(check, ref, screen, comp_context)

    # Evidence grounding — Vietnamese
    if comp_context:
        comp_id_str = comp_match.group(1) if comp_match else ref
        result['ddl_evidence'] = (
            f'Thông số DDL [{comp_id_str}] yêu cầu tính năng này. '
            f'Thiết kế hiện tại chưa triển khai.'
        )
    elif h_desc:
        result['ddl_evidence'] = f'Nguyên tắc DDL: "{h_desc}"'

    return result


def _generate_hien_trang(check: str, ref: str, screen: str, comp_ctx: str) -> str:
    """Generate a specific 'hiện trạng' description for a gap."""
    check_lower = check.lower()

    # Map check patterns to specific hiện trạng descriptions
    hien_trang_patterns = [
        (r'helper.?text', f'Trường nhập trên {screen} chỉ có label phía trên, không có helper text hướng dẫn bên dưới theo thông số component.'),
        (r'canresend|gửi lại', f'Màn hình OTP ({screen}) không có nút "Gửi lại OTP" — khi mã không đến, người dùng không có cách lấy mã mới.'),
        (r'countdown|timeleft|timer', f'Màn hình OTP ({screen}) không hiển thị bộ đếm thời gian — người dùng không biết OTP còn hiệu lực bao lâu.'),
        (r'mask.?toggle|eye.?icon|show.?hide', f'Trường nhập PIN/OTP trên {screen} không có icon hiện/ẩn — người dùng không thể kiểm tra đã nhập đúng.'),
        (r'attempt.?counter|lockout', f'Màn hình {screen} có cảnh báo "bị khóa sau N lần" nhưng không hiển thị bộ đếm số lần thử còn lại.'),
        (r'real.?time.*validation|checklist.*dynamic', f'Quy tắc validation trên {screen} hiển thị dạng text tĩnh ("Lưu ý"), không phản hồi real-time khi người dùng nhập.'),
        (r'progress.?indicator|step.?indicator|zeigarnik', f'Flow nhiều bước qua {screen} không có thanh tiến trình — người dùng không biết đang ở bước mấy.'),
        (r'modal.*error|error.*modal', f'Lỗi trên {screen} hiển thị qua modal popup thay vì inline error bên dưới trường nhập.'),
        (r'inline.*error|red.?border|visual.?affordance', f'Trường nhập trên {screen} thiếu viền đỏ và icon cảnh báo khi lỗi — không có tín hiệu trực quan.'),
        (r'contrast|wcag', f'Thành phần trên {screen} có tỷ lệ tương phản chưa đạt WCAG AA (tối thiểu 4.5:1).'),
        (r'nhất quán|consistency|cta.*label', f'Nhãn nút hành động trên các màn hình không nhất quán (VD: "Tiếp tục" vs "Xác nhận").'),
        (r'block.*height|information.?architecture', f'Khối nội dung phụ trên {screen} chiếm diện tích lớn, đẩy form nhập chính xuống dưới viewport.'),
        (r'empty.?state', f'Màn hình {screen} thiếu trạng thái rỗng (empty state) khi không có dữ liệu.'),
        (r'touch.?target|fitts', f'Vùng chạm trên {screen} nhỏ hơn 44×44px theo khuyến nghị.'),
        (r'pii|mask.*số|sensitive', f'Thông tin nhạy cảm trên {screen} hiển thị rõ ràng, chưa có cơ chế che giấu (masking).'),
    ]

    for pattern, description in hien_trang_patterns:
        if re.search(pattern, check_lower + ' ' + ref.lower(), re.IGNORECASE):
            return description

    # Fallback: use check title as hiện trạng
    return f'{check.strip().rstrip(".")} — trên màn hình {screen}.'


def _generate_impact_text_unique(check: str, ref: str, h_name: str, h_cat: str, comp_ctx: str, screen: str = '', gap_num: int = 0) -> str:
    """Generate UNIQUE impact text per gap.

    Uses _used_impacts set to guarantee no two gaps share identical impact text.
    When a base pattern matches a previously assigned impact, falls back to
    check-title-specific differentiation.
    """
    global _used_impacts
    combined = (check + ' ' + ref + ' ' + comp_ctx).lower()

    # Granular patterns — each check keyword gets its OWN unique impact
    # Ordered from most specific to least specific
    patterns = [
        # OTP/Authentication — DIFFERENTIATED per feature
        (r'canresend|gửi lại|resend',
         'Khi OTP không đến, người dùng không có cách gửi lại mã — bị kẹt tại màn hình xác thực, buộc phải thoát app và bắt đầu lại.'),

        (r'timeleft|countdown(?!.*attempt)',
         'Người dùng không biết OTP còn hiệu lực bao lâu — dẫn đến nhập vội hoặc nhập code đã hết hạn mà không hay biết.'),

        (r'attempt.?counter',
         'Người dùng không biết còn bao nhiêu lần thử trước khi bị khóa — thiếu cảnh báo "Còn X lần" dẫn đến khóa tài khoản bất ngờ.'),

        (r'lockout|bị khóa',
         'Người dùng không được cảnh báo rõ ràng về giới hạn số lần thử — risk khóa tài khoản → gọi hotline → tăng chi phí hỗ trợ.'),

        (r'mask.?toggle.*otp|otp.*mask.?toggle|eye.?icon.*otp',
         'Người dùng không thể kiểm tra mã OTP đã nhập — tăng tỷ lệ nhập sai và phải yêu cầu gửi lại mã mới.'),

        (r'mask.?toggle.*pin|pin.*mask.?toggle|show.?hide.*pin|eye.?icon',
         'Người dùng không thể kiểm tra mã PIN đã nhập — tăng tỷ lệ nhập sai và phải thao tác lại từ đầu.'),

        (r'mask.?toggle|show.?hide|ẩn.?hiện',
         'Người dùng không thể kiểm tra dữ liệu nhạy cảm đã nhập — nhập blind tăng tỷ lệ lỗi và thao tác lặp lại.'),

        (r'real.?time.*validation|checklist.*dynamic',
         'Người dùng phải đoán xem dữ liệu nhập đã đúng hay chưa — chỉ biết khi submit và nhận lỗi, gây frustration loop.'),

        # Form & Input
        (r'helper.?text|hướng dẫn|hint',
         'Thiếu gợi ý ngữ cảnh dưới trường nhập → người dùng không biết format yêu cầu. Tăng error rate và thời gian hoàn thành form.'),

        (r'label.*placeholder|placeholder.*label|thiếu label',
         'Khi focus vào trường, placeholder biến mất → người dùng quên trường đang nhập gì. WCAG 2.1 yêu cầu persistent label.'),

        # Error Handling
        (r'modal.*error|error.*modal|modal.*interrupt',
         'Lỗi hiển thị qua modal popup → gián đoạn luồng nhập liệu. Người dùng phải: đọc popup → tap đóng → tìm lại trường sai.'),

        (r'inline.*error|error.*inline|red.?border|border.*đỏ|visual.?affordance',
         'Thiếu tín hiệu trực quan khi lỗi (viền đỏ, icon cảnh báo) → người dùng không nhận biết trường nào cần sửa.'),

        # Navigation & Flow
        (r'progress.?indicator|step.?indicator|step.?dots',
         'Người dùng không biết mình đang ở bước nào trong flow nhiều bước — gây lo lắng và tăng tỷ lệ thoát giữa chừng.'),

        (r'zeigarnik',
         'Flow nhiều bước thiếu thanh tiến trình — vi phạm Zeigarnik Effect: progress indicator tăng completion rate 20-30%.'),

        (r'sticky.*cta|cta.*sticky|fixed.*button',
         'Nút hành động chính bị ẩn khi cuộn — người dùng quyết định xong nhưng không tìm thấy nút để thực hiện.'),

        (r'destination|redirect|navigate',
         'Điểm tương tác không define đích đến → tap vào không có phản hồi hoặc chuyển sai màn hình.'),

        # Accessibility & Visual
        (r'contrast|wcag|4\.5|3:1|badge.*nhạt',
         'Tỷ lệ tương phản không đạt WCAG AA (4.5:1 cho text). ~15% người dùng thị lực yếu không đọc được thông tin quan trọng.'),

        (r'aria|screen.?reader|accessible.?label',
         'Thành phần thiếu nhãn trợ năng → trình đọc màn hình không thể diễn giải đúng. Vi phạm WCAG 2.1 Level A.'),

        (r'pii|mask.*số|sensitive|bảo mật|security',
         'Thông tin nhạy cảm hiển thị rõ trên màn hình → rủi ro lộ thông tin. Banking compliance yêu cầu PII masking.'),

        # Layout & Content
        (r'block.*height|chiếm.*%|quá.*height|whitespace|information.?architecture',
         'Bố cục chưa tối ưu: nội dung phụ chiếm diện tích lớn, đẩy trường nhập chính ra ngoài viewport.'),

        (r'empty.?state|trạng thái rỗng',
         'Khi không có dữ liệu, màn hình trống không hướng dẫn → người dùng không biết phải làm gì tiếp.'),

        (r'nhất quán|consistency|terminology',
         'Không nhất quán wording/UI patterns giữa các màn hình → tăng cognitive load cho người dùng.'),

        # Data & Interaction
        (r'group.*date|daily.*total|sort|filter',
         'Danh sách flat không phân nhóm → khó tìm kiếm khi có nhiều mục. Cần group by + summary header.'),

        (r'dropdown|select|picker|chọn',
         'Thao tác chọn không tối ưu cho ngữ cảnh → tăng số bước để hoàn thành tác vụ.'),

        (r'scroll|pagination|lazy.*load',
         'Nội dung quá dài không có phân trang → hiệu suất chậm và người dùng mất phương hướng.'),
    ]

    for pattern, impact in patterns:
        if re.search(pattern, combined, re.IGNORECASE):
            if impact not in _used_impacts:
                _used_impacts.add(impact)
                return impact
            # Impact already used → differentiate using check title + screen + gap_num
            check_short = check.strip().rstrip('.')[:60]  # type: ignore[index]
            scr_tag = f' ({screen})' if screen else ''
            # Include gap_num for guaranteed uniqueness when same screen has repeated patterns
            unique_impact = f'{check_short}{scr_tag}: {impact[:120]}'  # type: ignore[index]
            if unique_impact in _used_impacts:
                unique_impact = f'{check_short}{scr_tag} [#{gap_num}]: {impact[:100]}'  # type: ignore[index]
            _used_impacts.add(unique_impact)
            return unique_impact

    # Fallback — use DDL context + check-specific differentiation
    check_short = check.strip().rstrip('.')[:60]  # type: ignore[index]
    scr_tag = f' ({screen})' if screen else ''
    if comp_ctx:
        # Include check title for uniqueness when multiple gaps share same component
        fb = (f'{check_short}{scr_tag}: Thành phần thiết kế chưa triển khai đầy đủ thông số DDL. '
              'Người dùng không có đủ tính năng cần thiết để hoàn thành tác vụ một cách hiệu quả và an toàn.')
    elif h_name:
        fb = (f'{check_short}{scr_tag}: Vi phạm nguyên tắc khả dụng {h_name}. '
              'Ảnh hưởng trực tiếp đến trải nghiệm và khả năng hoàn thành giao dịch của người dùng.')
    else:
        fb = (f'{check_short}{scr_tag}: Tác động tiêu cực đến trải nghiệm người dùng '
              'và khả năng hoàn thành luồng giao dịch.')

    # Ensure fallback is also unique — add counter suffix if still collides
    if fb in _used_impacts:
        suffix = 2
        while f'{fb} ({suffix})' in _used_impacts:
            suffix += 1
        fb = f'{fb} ({suffix})'
    _used_impacts.add(fb)
    return fb


def reason_uxp_enrichment(prop: dict, gaps: list, lookups: dict) -> dict:
    """Generate enriched UXP data with professional reasoning."""
    pid = prop['id']
    sev = prop['severity']
    screen = prop.get('screen', '')
    hien_trang = prop.get('hiện_trạng', '')
    giai_phap = prop.get('giải_pháp', [])
    gap_ref = prop.get('gap_ref', '')

    # Find related gaps
    related_gaps = []
    if gap_ref:
        for ref_num in re.findall(r'#(\d+)', str(gap_ref)):
            for g in gaps:
                if str(g['num']) == ref_num:
                    related_gaps.append(g)

    # Collect DDL references from related gaps
    ddl_refs = set()
    comp_refs = set()
    for g in related_gaps:
        ref = g.get('ref', '')
        if 'UXG-' in ref or ref in HEURISTIC_KB:
            ddl_refs.add(ref.replace('`', '').strip())
        if 'COMP:' in ref:
            comp_refs.add(ref.replace('`', '').replace('COMP:', '').strip())

    # Resolve heuristics
    heuristic_details = []
    for ref in ddl_refs:
        info = resolve_heuristic_ref(ref, lookups)
        if info.get('desc'):
            heuristic_details.append(info)

    # Component context
    comp_details = []
    for comp_id in comp_refs:
        comp = lookups['components'].get(comp_id, {})
        if comp:
            comp_details.append({
                'id': comp_id,
                'description': comp.get('description', ''),
                'tier': comp.get('tier', ''),
            })

    # Severity justification
    sev_justification = _justify_severity(sev, hien_trang, related_gaps, heuristic_details)

    # Impact narrative
    impact_narrative = _build_impact_narrative(
        sev, hien_trang, screen, related_gaps, comp_details, heuristic_details)

    # Best practice reference
    best_practice = _build_best_practice(hien_trang, heuristic_details, comp_details)

    return {
        'id': pid,
        'severity_justification': sev_justification,
        'impact_narrative': impact_narrative,
        'best_practice': best_practice,
        'related_gap_nums': [g['num'] for g in related_gaps],
        'ddl_refs': list(ddl_refs),
        'comp_refs': [{'id': c['id'], 'desc': c['description']} for c in comp_details],
        'heuristics': [{'name': h['name'], 'desc': h['desc']} for h in heuristic_details],
    }


def _justify_severity(sev: str, hien_trang: str, gaps: list, heuristics: list) -> str:
    """Generate severity justification."""
    gap_count = len(gaps)
    h_names = [h.get('name', '') for h in heuristics]

    if sev == 'critical':
        reasons = []
        if any(kw in hien_trang.lower() for kw in ['block', 'kẹt', 'không thể', 'thiếu']):
            reasons.append('Chặn luồng chính — người dùng không thể hoàn thành tác vụ')
        if any(kw in hien_trang.lower() for kw in ['otp', 'pin', 'xác thực', 'bảo mật']):
            reasons.append('Ảnh hưởng flow xác thực/bảo mật — rủi ro cao nhất')
        if gap_count >= 3:
            reasons.append(f'Liên quan {gap_count} gap items — vấn đề hệ thống')
        if not reasons:
            reasons.append('Ảnh hưởng trực tiếp đến completion rate của core flow')
        return ' · '.join(reasons)

    elif sev == 'major':
        if gap_count >= 2:
            return f'Ảnh hưởng đáng kể đến UX ({gap_count} gaps liên quan). Không block flow nhưng giảm chất lượng trải nghiệm rõ rệt.'
        return 'Giảm chất lượng trải nghiệm đáng kể. Không block flow nhưng tạo friction cho người dùng.'

    else:  # minor
        return 'Cải thiện UX nhỏ — polish và consistency. Không ảnh hưởng chức năng chính.'


def _build_impact_narrative(sev, hien_trang, screen, gaps, comps, heuristics):
    """Build rich impact narrative."""
    parts: list[str] = []

    # What's wrong
    parts.append(f'**Hiện trạng**: {hien_trang}')

    # Why it matters (from heuristics)
    if heuristics:
        h = heuristics[0]
        parts.append(f'**Nguyên tắc vi phạm**: {h["name"]} — {h["desc"]}')

    # Component spec gap
    if comps:
        comp_strs = [f'`{c["id"]}` ({c["description"]})' for c in comps[:2]]
        parts.append(f'**DDL Component**: {"; ".join(comp_strs)}')

    # Scope
    if gaps:
        gap_nums = [f'#{g["num"]}' for g in gaps]
        parts.append(f'**Phạm vi**: {len(gaps)} checklist items ({", ".join(gap_nums)})')

    return '\n'.join(parts)


def _build_best_practice(hien_trang, heuristics, comps):
    """Build best practice reference."""
    refs: list[str] = []

    combined = hien_trang.lower()
    if 'otp' in combined:
        refs.append('NIST SP 800-63B (Digital Identity Guidelines)')
        refs.append('Apple HIG: Verification Codes')
    if 'pin' in combined:
        refs.append('PCI DSS: PIN entry best practices')
    if 'contrast' in combined or 'wcag' in combined:
        refs.append('WCAG 2.1 Level AA: Contrast Minimum (1.4.3)')
    if 'error' in combined:
        refs.append('Nielsen Norman Group: Error Message Guidelines')
    if 'touch' in combined or 'fitts' in combined or 'target' in combined:
        refs.append('Apple HIG: Touch target ≥ 44pt')
        refs.append('Material Design: Touch target ≥ 48dp')

    for h in heuristics:
        nielsen = h.get('nielsen')
        if nielsen:
            refs.append(f'Nielsen Heuristic #{nielsen}: {h["name"]}')

    if not refs and comps:
        refs.append('DDL Component Spec Compliance')

    return refs[:3]  # type: ignore[index]  # Max 3 references


# ═══════════════════════════════════════════════════════════
# CATEGORY SCORE CALCULATOR (replaces fake formula)
# ═══════════════════════════════════════════════════════════

def calculate_category_scores(gaps: list, screens: list, report_path: Path) -> dict:
    """Calculate real per-category scores from checklist data."""
    # Read full report to get ALL check rows (pass + gap)
    report = report_path.read_text(encoding='utf-8')

    # Parse all checklist rows
    all_checks = []
    current_screen = ''
    for line in report.split('\n'):
        # Track current screen
        sm = re.match(r'###\s*\d+\.\s*(.+?)(?:\s*\(`?(SCR-\S+?)`?\)|\s*(SCR-\S+)\s*[—–-])', line)
        if sm:
            current_screen = sm.group(2) or sm.group(3) or ''
            continue
        sm = re.match(r'###\s*\d+\.\s*(SCR-\S+)\s*[—–-]', line)
        if sm:
            current_screen = sm.group(1)
            continue

        # Check row: | N | description | source | ref | ✅/❌ verdict | evidence |
        # Verdict can be in any column — look for ✅ or ❌ in the full line
        if '|' in line and ('✅' in line or '❌' in line or '⚠️' in line):
            cols = [c.strip() for c in line.split('|')]
            cols = [c for c in cols if c]
            # First column should be a number
            first = cols[0].strip() if cols else ''
            if first and re.match(r'^\d+$', first) and len(cols) >= 5:
                # Find which column has the verdict
                is_pass = False
                is_gap = False
                for col in cols:
                    if '✅' in col and ('Pass' in col or 'pass' in col or '✅' == col.strip()):
                        is_pass = True
                    if ('❌' in col or '⚠️' in col) and ('Gap' in col or 'gap' in col):
                        is_gap = True

                # Simpler: just check if line has pass/gap markers
                if not is_pass and not is_gap:
                    full_line = line
                    is_pass = '✅ Pass' in full_line or '✅Pass' in full_line
                    is_gap = '❌ Gap' in full_line or '⚠️ Gap' in full_line

                if is_pass or is_gap:
                    check_text = cols[1] if len(cols) > 1 else ''
                    source = cols[2] if len(cols) > 2 else ''
                    ref = cols[3] if len(cols) > 3 else ''

                    category = classify_check_category(check_text + ' ' + source, ref)

                    all_checks.append({
                        'num': int(first),
                        'check': check_text,
                        'source': source,
                        'ref': ref,
                        'screen': current_screen,
                        'is_pass': is_pass,
                        'category': category,
                    })

    # Aggregate by category
    cat_results: dict[str, Any] = {}
    for cat_id, cat_data in CATEGORY_KEYWORDS.items():
        cat_checks = [c for c in all_checks if c['category'] == cat_id]
        total = len(cat_checks)
        passed = sum(1 for c in cat_checks if c['is_pass'])
        score = round(passed / total * 100) if total > 0 else -1

        cat_results[cat_id] = {
            'name_vi': cat_data['name_vi'],
            'name_en': cat_data['name_en'],
            'total': total,
            'pass': passed,
            'gap': total - passed,
            'score': score,
            'checks': [{'num': c['num'], 'check': c['check'][:60], 'pass': c['is_pass']}  # type: ignore[index]
                       for c in cat_checks],
        }

    # Handle categories with no checks → estimate from overall
    overall_score = sum(int(s.get('score', 0)) for s in screens) // max(len(screens), 1)
    for cat_id in cat_results:
        if cat_results[cat_id]['score'] == -1:
            cat_results[cat_id]['score'] = overall_score
            cat_results[cat_id]['estimated'] = True

    return cat_results


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

def validate_enriched_output(data: dict) -> list[str]:
    """Validate enriched-data.json against schema. Returns list of violations."""
    violations: list[str] = []

    # Check gap impact uniqueness
    impact_texts = [g.get('enriched', {}).get('impact', '') for g in data.get('gaps', [])]
    seen: dict[str, list[str]] = {}
    for i, t in enumerate(impact_texts):
        if t:
            seen.setdefault(t, []).append(str(i + 1))
    duplicates = {t: nums for t, nums in seen.items() if len(nums) > 1}
    if duplicates:
        for text, nums in duplicates.items():
            nums_str = ', '.join(nums)
            text_preview = text[:60]  # type: ignore[index]
            violations.append(
                f'DUPLICATE_IMPACT: Gaps [{nums_str}] share same impact: "{text_preview}..."'
            )

    # Check required fields per gap
    for gap in data.get('gaps', []):
        enriched = gap.get('enriched', {})
        for field in ['impact', 'heuristic_tag', 'hiện_trạng']:
            if not enriched.get(field):
                violations.append(f'MISSING_FIELD: Gap #{gap.get("num")} missing \'{field}\'')

    # Check required fields per proposal
    for prop in data.get('proposals', []):
        if not prop.get('impact_narrative'):
            violations.append(f'MISSING_FIELD: UXP {prop.get("id")} missing \'impact_narrative\'')

    return violations


def enrich(report_path: Path) -> dict:
    """Main enrichment pipeline."""
    # Reset uniqueness tracker for fresh run
    reset_impact_tracker()

    # Parse report
    meta, proposals, gaps, screens = parse_proposals(report_path)

    # Load DDL
    ddl = load_ddl(report_path)
    lookups = build_ddl_lookups(ddl)

    # Compute file hash for cache validation
    report_hash = hashlib.md5(report_path.read_bytes()).hexdigest()[:12]  # type: ignore[index]

    result: dict[str, Any] = {
        '_version': '2.0.0',
        '_report_hash': report_hash,
        '_ddl_loaded': bool(ddl),
        '_ddl_components': len(lookups['components']),
        '_ddl_guidelines': len(lookups['guidelines']),
        'gaps': [],
        'proposals': [],
        'category_scores': {},
    }

    # Enrich gaps (with uniqueness tracking)
    for gap in gaps:
        ref = gap.get('ref', '').replace('`', '').strip()
        heuristic_info = resolve_heuristic_ref(ref, lookups)
        impact_data = reason_gap_impact(gap, heuristic_info, lookups)

        result['gaps'].append({
            'num': gap['num'],
            'screen': gap['screen'],
            'check': gap['check'],
            'ref': ref,
            'source': gap['source'],
            'enriched': impact_data,
        })

    # Enrich proposals
    for prop in proposals:
        enriched = reason_uxp_enrichment(prop, gaps, lookups)
        result['proposals'].append(enriched)

    # Category scores
    result['category_scores'] = calculate_category_scores(gaps, screens, report_path)

    # Validation gate
    violations = validate_enriched_output(result)
    if violations:
        result['_violations'] = violations
        result['_violations_count'] = len(violations)
        print(f'⚠️ {len(violations)} schema violations detected:', file=sys.stderr)
        for v in violations[:8]:
            print(f'  → {v}', file=sys.stderr)
    else:
        print('✅ Schema validation passed — all gaps unique, all fields present', file=sys.stderr)

    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)  # type: ignore[name-defined]
    parser.add_argument('--report', required=True, help='Path to ux-review-report.md')
    parser.add_argument('--force', action='store_true', help='Force re-enrichment even if cache is valid')
    args = parser.parse_args()

    report_path = Path(args.report)
    if not report_path.exists():
        print(f'Error: {report_path} not found', file=sys.stderr)
        sys.exit(1)

    out_path = report_path.parent / 'enriched-data.json'

    # Cache validation — skip if report unchanged
    if not args.force and out_path.exists():
        try:
            cached = json.loads(out_path.read_text(encoding='utf-8'))
            current_hash = hashlib.md5(report_path.read_bytes()).hexdigest()[:12]  # type: ignore[index]
            if cached.get('_report_hash') == current_hash:
                print(json.dumps({
                    'status': 'cached',
                    'output': str(out_path),
                    'gaps_enriched': len(cached.get('gaps', [])),
                    'proposals_enriched': len(cached.get('proposals', [])),
                    'categories': len(cached.get('category_scores', {})),
                    'ddl_loaded': cached.get('_ddl_loaded', False),
                }, indent=2))
                return
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError):
            pass  # Cache invalid — proceed with enrichment

    enriched = enrich(report_path)

    # Save next to report
    out_path.write_text(json.dumps(enriched, ensure_ascii=False, indent=2), encoding='utf-8')

    # Summary
    print(json.dumps({
        'status': 'ok',
        'output': str(out_path),
        'gaps_enriched': len(enriched['gaps']),
        'proposals_enriched': len(enriched['proposals']),
        'categories': len(enriched['category_scores']),
        'ddl_loaded': enriched['_ddl_loaded'],
    }, indent=2))


if __name__ == '__main__':
    main()
