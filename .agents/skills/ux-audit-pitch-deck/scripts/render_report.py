#!/usr/bin/env python3
"""
render_report.py — JSON→HTML renderer for ux-audit-pitch-deck.

Reads report-data.json (produced by convert_report.py) and template.html,
then produces a single self-contained HTML pitch deck.

This script ONLY renders. It never parses markdown, never resolves images,
never mutates existing HTML. It reads JSON, applies template, outputs HTML.

Usage:
  python3 render_report.py --module path/to/module/
  python3 render_report.py --base path/to/final/
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# Path to template relative to this script
SCRIPT_DIR = Path(__file__).parent
TEMPLATE_PATH = SCRIPT_DIR.parent / 'assets' / 'template.html'


def _score_color(score: int) -> str:
    if score < 50:
        return '#b91c1c'
    if score < 70:
        return '#c2410c'
    return '#15803d'


def _severity_class(severity: str) -> str:
    s = severity.lower()
    if 'critical' in s:
        return 'critical'
    if 'major' in s:
        return 'major'
    return 'minor'


def _severity_label(severity: str) -> str:
    s = severity.lower()
    if 'critical' in s:
        return '🔴 Critical — Cần xử lý ngay'
    if 'major' in s:
        return '🟡 Major — Ưu tiên cao'
    return '⚪ Minor — Cải thiện'


def _severity_badge(severity: str) -> str:
    cls = _severity_class(severity)
    label = severity.capitalize()
    return f'<span class="badge {cls}">{label}</span>'


def _escape(text: str) -> str:
    """Escape HTML special characters."""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;'))


# ═══════════════════════════════════════════════════════════════════════
# HTML BUILDERS
# ═══════════════════════════════════════════════════════════════════════

def _build_hero(data: dict) -> str:
    """Build Section 1: Hero / Executive Summary."""
    meta = data['meta']
    stats = data['stats']
    score = stats['overall_score']
    color = stats['overall_score_color']
    offset = stats['overall_score_offset']
    sev = stats['severity_counts']

    return f'''<section class="hero" id="top">
  <div class="hero-label">UX Audit Report</div>
  <h1>{_escape(meta['client_name'])} · {_escape(meta['module_name'])}</h1>
  <p class="hero-sub">{_escape(meta['product_name'])}</p>
  <div class="hero-stats">
    <div class="stat-item"><span class="stat-num">{stats['screen_count']}</span><span class="stat-label">Màn hình</span></div>
    <div class="stat-item"><span class="stat-num">{stats['check_count']}</span><span class="stat-label">Tổng kiểm tra</span></div>
    <div class="stat-item"><span class="stat-num gap-c">{stats['gap_count']}</span><span class="stat-label">Cần cải thiện</span></div>
    <div class="stat-item"><span class="stat-num">{stats['proposal_count']}</span><span class="stat-label">Đề xuất</span></div>
  </div>
  <div class="hero-score"><svg width="110" height="110" viewBox="0 0 110 110"><circle cx="55" cy="55" r="51" fill="none" stroke="#e2e8f0" stroke-width="8"/><circle cx="55" cy="55" r="51" fill="none" stroke="{color}" stroke-width="8" stroke-dasharray="320" stroke-dashoffset="{offset}" stroke-linecap="round" transform="rotate(-90 55 55)"/><text x="55" y="60" text-anchor="middle" font-family="var(--font-sans)" font-size="24" font-weight="800" fill="{color}">{score}%</text></svg></div>
</section>'''


def _build_summary(data: dict) -> str:
    """Build Section 2: Summary with screen scores."""
    stats = data['stats']
    sev = stats['severity_counts']

    badges = ''
    if sev['critical']:
        badges += f'<span class="badge critical">🔴 {sev["critical"]} Critical</span>'
    if sev['major']:
        badges += f'<span class="badge major">🟡 {sev["major"]} Major</span>'
    if sev['minor']:
        badges += f'<span class="badge minor">⚪ {sev["minor"]} Minor</span>'

    screen_cards = ''
    for screen in data['screens']:
        color = screen['score_color']
        offset = screen['score_offset']
        score = screen['score']
        name = _escape(screen['name'])
        sid = screen['id']
        stype = screen['type']
        gaps = screen['gap_count']

        screen_cards += f'''    <div class="score-item reveal">
      <div style="flex-shrink:0"><svg width="56" height="56" viewBox="0 0 56 56"><circle cx="28" cy="28" r="25" fill="none" stroke="#e2e8f0" stroke-width="5"/><circle cx="28" cy="28" r="25" fill="none" stroke="{color}" stroke-width="5" stroke-dasharray="157" stroke-dashoffset="{offset}" stroke-linecap="round" transform="rotate(-90 28 28)"/><text x="28" y="33" text-anchor="middle" font-family="var(--font-sans)" font-size="13" font-weight="800" fill="{color}">{score}%</text></svg></div>
      <div class="score-info">
        <h4>{name}</h4>
        <p>{sid} · {stype} · <span style="color:var(--sev-critical-fg)">{gaps} Gap</span></p>
      </div>
    </div>
'''

    return f'''<section class="section" id="summary">
  <div class="section-title"><span class="icon">📊</span> 01 · Tổng quan kết quả kiểm tra</div>
  <div style="display:flex;gap:12px;margin-bottom:28px">
    {badges}
  </div>
  <div class="scorecard-grid">
{screen_cards}  </div>
</section>'''


def _build_methodology() -> str:
    """Build Section 3: Methodology (static)."""
    return '''<section class="section reveal" id="method">
  <div class="section-title"><span class="icon">🔬</span> 02 · Phương pháp đánh giá</div>
  <div class="method-grid">
    <div class="method-card"><div class="method-icon">🔍</div><h4>Heuristic Evaluation</h4><p>Đánh giá theo 10 heuristics của Nielsen Norman Group. Mỗi phát hiện được liên kết với heuristic cụ thể bị vi phạm.</p></div>
    <div class="method-card"><div class="method-icon">🧩</div><h4>Component Spec Analysis</h4><p>So sánh thiết kế Figma với DDL component specifications để phát hiện gap về states, props và behavior.</p></div>
    <div class="method-card"><div class="method-icon">👁️</div><h4>Vision Inspection</h4><p>Phân tích trực quan từng màn hình: alignment, contrast, typography, touch targets, overlay detection.</p></div>
    <div class="method-card"><div class="method-icon">⚖️</div><h4>UX Law Cross-Reference</h4><p>Áp dụng Fitts's Law, Hick's Law, Peak-End Rule và các nguyên tắc thiết kế vào từng màn hình.</p></div>
  </div>
</section>'''


def _build_findings(data: dict) -> str:
    """Build Section 4: Detailed Findings (UXP cards)."""
    uxps = data['uxps']
    if not uxps:
        return ''

    # Group by severity
    groups: dict[str, list] = {'Critical': [], 'Major': [], 'Minor': []}
    for uxp in uxps:
        sev = uxp.get('severity', 'Major')
        if sev not in groups:
            sev = 'Major'
        groups[sev].append(uxp)

    html = '''<section class="section" id="findings">
  <div class="section-title"><span class="icon">🔎</span> 03 · Các vấn đề được phát hiện</div>
'''

    for severity in ['Critical', 'Major', 'Minor']:
        items = groups.get(severity, [])
        if not items:
            continue

        cls = _severity_class(severity)
        label = _severity_label(severity)

        html += f'''  <div style="margin-bottom:36px">
    <div style="background:var(--sev-{cls}-bg);padding:10px 18px;border-radius:8px;font-family:var(--font-mono);font-size:12px;font-weight:700;color:var(--sev-{cls}-fg);margin-bottom:20px;letter-spacing:.3px">{label}</div>
'''

        for uxp in items:
            img_src = uxp.get('screenshot_path', '')
            img_alt = _escape(uxp.get('problem', '')[:80])
            problem = _escape(uxp.get('problem', ''))
            solution = uxp.get('solution', '')
            screen_tag = _escape(uxp.get('screen_tag', ''))
            ddl_ref = _escape(uxp.get('ddl_ref', ''))
            uxp_id = uxp['id']

            # Enriched fields (from evidence-info)
            narrative = _escape(uxp.get('_enriched_narrative', ''))
            sev_justification = _escape(uxp.get('_enriched_severity', ''))
            enriched_ref = uxp.get('_enriched_ref', {})
            enriched_practices = uxp.get('_enriched_practices', [])

            # Use narrative as richer "hiện trạng" if available
            hien_trang = narrative if narrative else problem

            # Image section
            img_html = ''
            if img_src:
                onclick = f'onclick="openLightbox(\'{img_src}\')"'
                img_html = f'<div class="phone-frame" {onclick}><img src="{img_src}" alt="{img_alt}" loading="lazy"></div>'
                img_html += f'\n          <div class="shot-overlay {cls}">⚠️ {_escape(uxp.get("problem", "")[:60])}</div>'
            else:
                img_html = '<div style="color:var(--text-muted);font-size:12px;text-align:center">Ảnh không khả dụng</div>'

            # Solution list
            solution_html = ''
            if solution:
                sol_items = solution.split(';')
                li_items = ''.join(f'<li>{_escape(s.strip())}</li>' for s in sol_items if s.strip())
                if li_items:
                    solution_html = f'<div class="proposed-box"><ul>{li_items}</ul></div>'

            # Enriched reference citation
            ref_cite_html = ''
            if enriched_ref and isinstance(enriched_ref, dict):
                ref_name = _escape(enriched_ref.get('name', ''))
                ref_url = enriched_ref.get('url', '')
                ref_quote = _escape(enriched_ref.get('quote', ''))
                ref_source = _escape(enriched_ref.get('source', ''))
                if ref_url:
                    ref_cite_html = f'<div style="margin-top:8px;padding:8px 12px;background:#f0f9ff;border-left:3px solid #2563eb;border-radius:4px;font-size:11.5px"><strong>{ref_name}</strong>'
                    if ref_quote:
                        ref_cite_html += f'<br><em style="color:#64748b">"{ref_quote}"</em>'
                    ref_cite_html += f'<br><a href="{ref_url}" target="_blank" style="color:#2563eb;text-decoration:none">{ref_source} →</a></div>'

            # DDL section with enriched ref
            ddl_section = ddl_ref if ddl_ref else '—'

            html += f'''    <div class="finding-card reveal">
      <div class="finding-accent {cls}"></div>
      <div class="card-layout">
        <div class="card-visual">
          {img_html}
        </div>
        <div class="card-info">
          <div class="card-top"><span class="card-id">{uxp_id}</span>{_severity_badge(severity)}</div>
          <h3>{problem}</h3>
          <div class="finding-section"><h4>Hiện trạng</h4><p>{hien_trang}</p></div>
          <div class="finding-section"><h4>Nguyên tắc bị vi phạm</h4><p>{ddl_section}</p>{ref_cite_html}</div>
          {solution_html}
          <div class="finding-tags"><span class="card-tag">{screen_tag}</span></div>
          <details><summary>Xem tham chiếu kỹ thuật →</summary><div class="detail-content">{ddl_ref}<br>Gap ref: {_escape(uxp.get('gap_ref', ''))}{('<br>Severity: ' + sev_justification) if sev_justification else ''}</div></details>
        </div>
      </div>
    </div>
'''
        html += '  </div>\n'

    html += '</section>'
    return html


def _build_scorecard(data: dict) -> str:
    """Build Section 5: Heuristic Scorecard."""
    heuristics = data.get('heuristics', [])
    if not heuristics:
        return ''

    cards = ''
    for h in heuristics:
        score = h['score']
        color = _score_color(score)
        offset = round(207 * (1 - score / 100))

        cards += f'''    <div class="score-item reveal" style="flex-direction:column;text-align:center">
      <svg width="72" height="72" viewBox="0 0 72 72"><circle cx="36" cy="36" r="33" fill="none" stroke="#e2e8f0" stroke-width="6"/><circle cx="36" cy="36" r="33" fill="none" stroke="{color}" stroke-width="6" stroke-dasharray="207" stroke-dashoffset="{offset}" stroke-linecap="round" transform="rotate(-90 36 36)"/><text x="36" y="41" text-anchor="middle" font-family="var(--font-sans)" font-size="14" font-weight="800" fill="{color}">{score}%</text></svg>
      <div class="score-info" style="margin-top:8px;text-align:center"><h4>{_escape(h['name_vi'])}</h4><p>{_escape(h['name_en'])}</p></div>
    </div>
'''

    return f'''<section class="section" id="scorecard">
  <div class="section-title"><span class="icon">📊</span> 04 · Đánh giá theo danh mục heuristic</div>
  <div class="scorecard-grid">
{cards}  </div>
</section>'''


def _build_gaps(data: dict) -> str:
    """Build Section 6: Gaps Detail."""
    gaps_by_screen = data.get('gaps_by_screen', [])
    total_gaps = sum(len(sg['gaps']) for sg in gaps_by_screen)

    if not gaps_by_screen:
        return ''

    html = f'''<section class="section" id="gaps" style="padding-top:48px">
  <div class="section-title"><span class="icon">📋</span> Tổng hợp Gap ({total_gaps} hạng mục)</div>
  <p style="color:var(--text-muted);font-size:14px;margin-bottom:20px">Các hạng mục kiểm tra chưa đạt chuẩn theo từng màn hình — checklist cải thiện từ ux-review-report</p>
'''

    for sg in gaps_by_screen:
        sid = sg['screen_id']
        sname = _escape(sg['screen_name'])
        stype = sg['screen_type']

        html += f'''  <div class="gap-screen-group" style="margin-bottom:32px">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px">
      <span class="gap-screen">{sid}</span>
      <strong style="font-size:14px">{sname}</strong> · <em>{stype}</em>
    </div>
'''

        for gap in sg['gaps']:
            num = gap['num']
            title = _escape(gap['title'])
            ref = _escape(gap.get('ref', ''))
            # Enriched impact overrides baseline
            impact = _escape(gap.get('_enriched_impact', '') or gap.get('user_impact', ''))
            # Enriched heuristic name overrides if richer
            heuristic = _escape(gap.get('heuristic', ''))
            evidence = _escape(gap.get('evidence', ''))
            screenshot = gap.get('screenshot', '')
            screenshot_path = gap.get('screenshot_path', '')

            # Enriched sources (from evidence-info)
            enriched_sources = gap.get('_enriched_sources', [])
            enriched_ref = gap.get('_enriched_ref', {})

            # Screenshot citation
            img_cite = ''
            if screenshot:
                if screenshot_path:
                    img_cite = f'<span class="img-cite" onclick="openLightbox(\'{screenshot_path}\')">📸 {screenshot}</span>'
                else:
                    img_cite = f'<span style="display:inline-block;background:#EFF6FF;color:#2563EB;font-size:10px;padding:1px 6px;border-radius:4px;font-family:monospace;margin-left:4px">📸 {screenshot}</span>'

            # Enriched reference citation for gap
            gap_ref_cite = ''
            if enriched_ref and isinstance(enriched_ref, dict):
                ref_name = _escape(enriched_ref.get('name', ''))
                ref_url = enriched_ref.get('url', '')
                ref_source = _escape(enriched_ref.get('source', ''))
                if ref_url:
                    gap_ref_cite = f' · <a href="{ref_url}" target="_blank" style="color:#2563eb;text-decoration:none;font-size:10px">{ref_source} →</a>'

            # Heuristic with sources
            heuristic_display = heuristic
            if enriched_sources and isinstance(enriched_sources, list):
                src_tags = ' '.join(f'<span style="background:#e2e8f0;padding:1px 5px;border-radius:3px;font-size:9px;margin-left:3px">{_escape(str(s))}</span>' for s in enriched_sources[:2])
                heuristic_display = f'{heuristic} {src_tags}'

            html += f'''    <div style="border:1px solid #e5e7eb;border-radius:10px;padding:16px 20px;margin-bottom:12px;background:#fafbfc">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;background:#1e3a5f;color:#fff;font-size:12px;font-weight:700;flex-shrink:0">{num}</span>
        <strong style="font-size:13.5px;color:#1a1a2e">{title}</strong>
        <span class="gap-ref" style="margin-left:6px;font-size:10px;vertical-align:middle">{ref}{gap_ref_cite}</span>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px 20px;font-size:12.5px;line-height:1.55">
        <div>
          <div style="font-weight:600;color:#6b7280;font-size:11px;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:3px">🎯 Tác động đến người dùng</div>
          <div style="color:#444">{impact}</div>
        </div>
        <div>
          <div style="font-weight:600;color:#6b7280;font-size:11px;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:3px">📐 Heuristic vi phạm</div>
          <div style="color:#444">{heuristic_display}</div>
        </div>
        <div style="grid-column:1/-1">
          <div style="font-weight:600;color:#6b7280;font-size:11px;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:3px">🔍 Bằng chứng &amp; Phân tích {img_cite}</div>
          <div style="color:#444">{evidence}</div>
        </div>
      </div>
    </div>
'''

        html += '  </div>\n'

    html += '</section>'
    return html


def _build_footer(data: dict) -> str:
    """Build footer."""
    meta = data['meta']
    return f'''<footer>
  <p><strong>{_escape(meta['product_name'])}</strong> · {_escape(meta['module_name'])} · Đánh giá DDL-grounded</p>
</footer>'''


# ═══════════════════════════════════════════════════════════════════════
# MAIN RENDER
# ═══════════════════════════════════════════════════════════════════════

def render(data: dict, template: str) -> str:
    """Render JSON data into HTML using template.

    Strategy: Extract CSS + JS from template, build HTML sections from data.
    This avoids fragile {{placeholder}} substitution.
    """
    # Extract style block from template
    style_match = re.search(r'(<style>.*?</style>)', template, re.DOTALL)
    style_block = style_match.group(1) if style_match else ''

    # Extract all script blocks from template
    script_blocks = re.findall(r'(<script>.*?</script>)', template, re.DOTALL)
    scripts = '\n'.join(script_blocks)

    # Extract lightbox HTML
    lightbox_match = re.search(r'(<div class="lightbox-overlay".*?</div>\s*</div>)', template, re.DOTALL)
    lightbox = lightbox_match.group(1) if lightbox_match else ''

    meta = data['meta']
    title = f"UX Audit — {meta['module_name']} | {meta['product_name']} · {meta['client_name']}"

    # Build all sections
    nav = '''<nav class="nav">
  <a href="#summary">Tổng quan</a>
  <a href="#method">Phương pháp</a>
  <a href="#findings">Phát hiện</a>
  <a href="#scorecard">Scorecard</a>
  <a href="#gaps">Gaps</a>
</nav>'''

    sections = [
        nav,
        _build_hero(data),
        _build_summary(data),
        _build_methodology(),
        _build_findings(data),
        _build_scorecard(data),
        _build_gaps(data),
        _build_footer(data),
    ]

    body = '\n\n'.join(s for s in sections if s)

    return f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{_escape(title)}</title>
{style_block}
</head>
<body>
{body}

{scripts}

{lightbox}
</body>
</html>'''


def _slugify(name: str) -> str:
    """Create URL-safe slug from module name."""
    import unicodedata
    s = unicodedata.normalize('NFKD', name.lower())
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s).strip('-')
    return s


def render_module(module_dir: Path, template: str) -> str | None:
    """Render a single module from its report-data.json."""
    data_path = module_dir / 'report-data.json'
    if not data_path.exists():
        print(f'  ⚠️ {module_dir.name}: No report-data.json (run convert_report.py first)', file=sys.stderr)
        return None

    data = json.loads(data_path.read_text(encoding='utf-8'))
    return render(data, template)


def main():
    parser = argparse.ArgumentParser(
        description='JSON→HTML renderer for ux-audit-pitch-deck'
    )
    parser.add_argument('--module', type=Path, help='Single module directory')
    parser.add_argument('--base', type=Path, help='Base directory containing modules')
    parser.add_argument('--template', type=Path, default=TEMPLATE_PATH, help='Template HTML file')
    args = parser.parse_args()

    if not args.template.exists():
        print(f'Error: Template not found: {args.template}', file=sys.stderr)
        sys.exit(1)

    template = args.template.read_text(encoding='utf-8')

    if args.module:
        modules = [args.module]
    elif args.base:
        modules = sorted(p.parent for p in args.base.rglob('report-data.json'))
    else:
        print('Error: --base or --module required', file=sys.stderr)
        sys.exit(1)

    print(f'📂 Found {len(modules)} modules with report-data.json', file=sys.stderr)

    success = 0
    for module_dir in modules:
        html = render_module(module_dir, template)
        if html is None:
            continue

        # Generate output filename
        data = json.loads((module_dir / 'report-data.json').read_text(encoding='utf-8'))
        section = data['meta'].get('section', '')
        module_name = data['meta']['module_name']

        if section:
            slug = _slugify(section) + '--' + _slugify(module_name)
        else:
            slug = _slugify(module_name)

        out_name = f'{slug}--pitch-deck.html'
        out_path = module_dir / out_name
        out_path.write_text(html, encoding='utf-8')

        uxp_count = len(data['uxps'])
        gap_count = data['stats']['gap_count']
        print(f'  ✅ {module_dir.name} → {out_name} ({uxp_count} UXPs, {gap_count} gaps)', file=sys.stderr)
        success += 1

    print(f'\n✅ {success}/{len(modules)} rendered', file=sys.stderr)


if __name__ == '__main__':
    main()
