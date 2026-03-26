#!/usr/bin/env python3
"""
reason_uxps.py — AI-Reasoned UXP Enrichment Pipeline

Enriches UXP cards in enriched-data.json with deep reasoning:
  1. Hiện trạng — detailed artboard evidence
  2. Tác động — domain-aware user impact
  3. Nguyên tắc bị vi phạm — official heuristic + WHY
  4. Đề xuất cải thiện — actionable fixes with DDL refs
  5. Tham chiếu kỹ thuật — official citations with URLs

Usage:
  python3 reason_uxps.py --report path/to/ux-review-report.md [--force] [--verify]

Reads:
  - ux-review-report.md     → UXP definitions
  - SCR-*.md                → screen context, OCR, user stories
  - enriched-data.json      → existing gap/DDL data
  - heuristics_db.json      → offline citation database

Writes:
  - enriched-data.json      → adds/updates 'uxps' dict

Design:
  - Deterministic template reasoning (no API calls needed)
  - Heuristic auto-matching via keyword scoring
  - Graceful: skips already-reasoned UXPs unless --force
  - Verifiable: --verify checks quality of reasoned output
"""

import json
import re
import sys
import argparse
from datetime import datetime
from pathlib import Path
from typing import Optional

# ── Constants ──

SCRIPT_DIR = Path(__file__).parent
HEURISTICS_DB_PATH = SCRIPT_DIR / 'heuristics_db.json'

MIN_HIEN_TRANG_LEN = 80    # reasoned hiện trạng must be >= 80 chars
MIN_TAC_DONG_LEN = 60      # reasoned tác động must be >= 60 chars
MIN_NGUYEN_TAC_LEN = 40    # nguyên tắc must include name + violation
MIN_SOURCES = 1             # at least 1 official source per UXP


# ── Helpers ──

def load_heuristics_db() -> dict:
    """Load offline heuristic reference database."""
    if not HEURISTICS_DB_PATH.exists():
        print(f'⚠️  heuristics_db.json not found at {HEURISTICS_DB_PATH}', file=sys.stderr)
        return {}
    return json.loads(HEURISTICS_DB_PATH.read_text('utf-8'))


def parse_uxps_from_report(report_path: Path) -> list[dict]:
    """Parse UXP definitions from ux-review-report.md."""
    text = report_path.read_text('utf-8')
    uxps = []

    # Split by UXP headers: #### UXP-NNN · [emoji] Severity
    parts = re.split(r'####\s+(UXP-\d+)\s*·\s*(?:🔴\s*|🟡\s*|⚪\s*)?(\w+)', text)

    for i in range(1, len(parts), 3):
        uid = parts[i]
        sev = parts[i + 1].lower()
        body = parts[i + 2] if i + 2 < len(parts) else ''

        # Parse table fields (support multiple name variants)
        fields = {}
        for m in re.finditer(r'\|\s*\*\*(\w[\w\s]*?)\*\*\s*\|\s*(.*?)\s*\|', body):
            key = m.group(1).strip()
            val = m.group(2).strip()
            fields[key] = val

        def _get(*keys: str) -> str:
            """Get first matching field from multiple key variants."""
            for k in keys:
                v = fields.get(k, '')
                if v:
                    return v
            return ''

        uxps.append({
            'id': uid,
            'severity': sev,
            'screen': _get('Màn hình'),
            'problem': _get('Vấn đề'),
            'current_state': _get('Hiện tại', 'Hiện trạng'),
            'proposal': _get('Đề xuất', 'Giải pháp'),
            'ddl_ref': _get('DDL Ref', 'DDL', 'DDL ref'),
            'heuristic': _get('Heuristic', 'Nguyên tắc', 'Heuristic Ref'),
            'effort': _get('Effort'),
            'gap_ref': _get('Gap ref', 'Gap Ref'),
        })

    return uxps


def load_screen_mds(report_dir: Path) -> dict[str, str]:
    """Load all SCR-*.md files from the report directory."""
    screens = {}
    for f in sorted(report_dir.glob('SCR-*.md')):
        scr_id_m = re.match(r'(SCR-\w+-\d+)', f.stem)
        scr_id = scr_id_m.group(1) if scr_id_m else f.stem
        screens[scr_id] = f.read_text('utf-8')
    return screens


def match_heuristic(heur_text: str, db: dict, extra_context: str = '') -> Optional[dict]:
    """Auto-match a heuristic reference to the database via keyword scoring.
    
    Args:
        heur_text: the heuristic field value
        db: heuristics database
        extra_context: additional text to search (DDL refs, problem text)
    """
    if not db:
        return None

    # Combine all available text for matching
    combined = f'{heur_text} {extra_context}'.lower()
    heur_lower = heur_text.lower() if heur_text else ''

    if not combined.strip():
        return None

    # Direct Nielsen # match in any text
    nielsen_m = re.search(r'nielsen\s*#(\d+)', combined)
    if nielsen_m:
        num = nielsen_m.group(1)
        nielsen_db = db.get('nielsen', {})
        if num in nielsen_db:
            return nielsen_db[num]

    # UXG code to heuristic mapping (common DDL patterns)
    uxg_map = {
        'UXG-165': '1',   # System status visibility
        'UXG-175': '1',   # Loading state / feedback
        'UXG-178': '3',   # Close affordance / user control
        'UXG-180': '4',   # Color only / consistency
        'UXG-197': '4',   # Input labels / consistency
        'UXG-204': '4',   # Visual hierarchy / consistency
        'UXG-243': '4',   # CTA clarity / consistency
        'UXG-257': '9',   # Inline errors
    }
    for uxg_code, nielsen_num in uxg_map.items():
        if uxg_code.lower() in combined:
            nielsen_db = db.get('nielsen', {})
            if nielsen_num in nielsen_db:
                return nielsen_db[nielsen_num]

    # Keyword-based scoring (check DDL keywords like 'otp', 'error', etc.)
    best_score = 0
    best_entry = None
    for _num, entry in db.get('nielsen', {}).items():
        keywords = entry.get('keywords', []) + entry.get('keywords_vi', [])
        score = sum(1 for kw in keywords if kw.lower() in combined)
        if score > best_score:
            best_score = score
            best_entry = entry

    if best_entry and best_score >= 2:
        return best_entry

    # Last resort: check Laws of UX
    for law_key, law_entry in db.get('laws', {}).items():
        if law_key.lower() in combined or law_entry.get('name', '').lower() in combined:
            return {
                'name': law_entry['name'],
                'desc_en': law_entry['desc'],
                'desc_vi': law_entry['desc'],
                'sources': [{'name': law_entry['name'], 'url': law_entry['url'], 'quote': law_entry['quote']}]
            }

    return None


def find_artboard_id(text: str) -> str:
    """Extract artboard ID (4-5 digits) from text."""
    m = re.search(r'\b(\d{4,5})\b', text)
    return m.group(1) if m else ''


def build_hien_trang(uxp: dict, screens: dict[str, str]) -> str:
    """Build detailed hiện trạng from source data."""
    current = uxp.get('current_state', '')
    problem = uxp.get('problem', '')

    # Extract artboard ID
    artboard = find_artboard_id(current) or find_artboard_id(problem)

    # Find relevant screen context
    screen_context = ''
    screen_field = uxp.get('screen', '')
    for scr_id, scr_text in screens.items():
        # Check if this screen contains the artboard
        if artboard and artboard in scr_text:
            # Extract artboard description
            ab_m = re.search(rf'{artboard}\s*\(([^)]+)\)', scr_text)
            if ab_m:
                screen_context = ab_m.group(1)
            break

    parts = []
    if artboard and screen_context:
        parts.append(f'Trên artboard {artboard} ({screen_context})')
    elif artboard:
        parts.append(f'Trên artboard {artboard}')

    if current:
        # Clean up current state text
        cleaned = re.sub(r'\*\*', '', current)  # remove markdown bold
        parts.append(cleaned)
    elif problem:
        parts.append(problem)

    return ', '.join(parts) if parts else problem


def build_tac_dong(uxp: dict, domain: str = 'banking') -> str:
    """Build domain-aware user impact."""
    problem = uxp.get('problem', '')
    sev = uxp.get('severity', '')

    # Banking domain context
    domain_suffix = ''
    if domain == 'banking':
        ddl = uxp.get('ddl_ref', '').lower()
        if any(kw in ddl for kw in ['destructive', 'cancel', 'huỷ']):
            domain_suffix = ' Trong ngành banking, hành động phá huỷ cần rào cản tâm lý rõ ràng để bảo vệ người dùng.'
        elif any(kw in ddl for kw in ['otp', 'security', 'xác thực']):
            domain_suffix = ' Trong ngữ cảnh banking, đây là giao dịch nhạy cảm đòi hỏi feedback rõ ràng về trạng thái xác thực.'
        elif 'trust' in ddl:
            domain_suffix = ' Trong ngành banking, độ tin cậy của UI ảnh hưởng trực tiếp đến niềm tin của khách hàng.'

    heur = uxp.get('heuristic', '')
    current = uxp.get('current_state', '')

    # Infer impact based on severity + problem context
    if sev == 'critical':
        prefix = 'Người dùng bị chặn hoặc mất khả năng hoàn thành tác vụ: '
    elif sev == 'major':
        prefix = 'Trải nghiệm người dùng bị ảnh hưởng đáng kể: '
    else:
        prefix = 'Trải nghiệm người dùng có thể được cải thiện: '

    return prefix + problem + '.' + domain_suffix


def build_nguyen_tac(uxp: dict, db: dict) -> dict:
    """Build heuristic violation with official citation."""
    heur_text = uxp.get('heuristic', '')
    # Also search DDL refs and problem text for heuristic clues
    extra = f"{uxp.get('ddl_ref', '')} {uxp.get('problem', '')} {uxp.get('gap_ref', '')}"
    matched = match_heuristic(heur_text, db, extra_context=extra)

    if matched:
        return {
            'name': matched['name'],
            'violation': f"Thiết kế hiện tại vi phạm nguyên tắc: \"{matched['desc_en']}\"",
            'sources': matched.get('sources', [])
        }

    # Fallback: use raw heuristic text
    return {
        'name': heur_text or uxp.get('ddl_ref', ''),
        'violation': '',
        'sources': []
    }


def build_de_xuat(uxp: dict) -> list[str]:
    """Parse proposal into actionable bullet points."""
    proposal = uxp.get('proposal', '')
    if not proposal:
        return []

    # Split on sentence boundaries or explicit separators
    items = re.split(r'(?<=[.!?])\s+(?=[A-ZĐT])|;\s*', proposal)
    return [item.strip() for item in items if item.strip()]


def build_tham_chieu(uxp: dict, db: dict) -> dict:
    """Build technical reference with official source links."""
    heur_text = uxp.get('heuristic', '')
    ddl_ref = uxp.get('ddl_ref', '')
    problem = uxp.get('problem', '')
    extra = f'{ddl_ref} {problem}'
    matched = match_heuristic(heur_text, db, extra_context=extra)

    sources = []
    if matched:
        sources = list(matched.get('sources', []))

    # Add WCAG sources if relevant keywords present
    combined = f'{heur_text} {ddl_ref} {problem}'.lower()
    wcag_db = db.get('wcag', {})
    if any(kw in combined for kw in ['error', 'validation', 'lỗi', 'form', 'inline']):
        for sc_id in ['3.3.1', '3.3.3']:
            sc = wcag_db.get(sc_id)
            if sc:
                sources.append({'name': sc['name'], 'url': sc['url'], 'quote': sc['quote']})
    if any(kw in combined for kw in ['destructive', 'financial', 'legal', 'huỷ', 'banking']):
        sc = wcag_db.get('3.3.4')
        if sc:
            sources.append({'name': sc['name'], 'url': sc['url'], 'quote': sc['quote']})
    if any(kw in combined for kw in ['touch', 'target', 'touch target', 'fitts']):
        sc = wcag_db.get('2.5.8')
        if sc:
            sources.append({'name': sc['name'], 'url': sc['url'], 'quote': sc['quote']})

    # Build text summary
    text_parts = []
    if matched:
        text_parts.append(f"{matched['name']} — {matched.get('desc_vi', '')}")
    if ddl_ref:
        text_parts.append(f'DDL ref: {ddl_ref}')

    return {
        'text': '. '.join(text_parts) if text_parts else ddl_ref,
        'sources': sources
    }


def reason_single_uxp(uxp: dict, screens: dict[str, str], db: dict) -> dict:
    """Produce full 5-block reasoning for one UXP."""
    return {
        'hiện_trạng': build_hien_trang(uxp, screens),
        'tác_động': build_tac_dong(uxp),
        'nguyên_tắc': build_nguyen_tac(uxp, db),
        'đề_xuất': build_de_xuat(uxp),
        'tham_chiếu': build_tham_chieu(uxp, db),
    }


def verify_reasoning(reasoned: dict, uid: str) -> list[str]:
    """Quality check for reasoned UXP data. Returns list of issues."""
    issues = []

    ht = reasoned.get('hiện_trạng', '')
    if len(ht) < MIN_HIEN_TRANG_LEN:
        issues.append(f'{uid}: hiện_trạng too short ({len(ht)} < {MIN_HIEN_TRANG_LEN})')

    td = reasoned.get('tác_động', '')
    if len(td) < MIN_TAC_DONG_LEN:
        issues.append(f'{uid}: tác_động too short ({len(td)} < {MIN_TAC_DONG_LEN})')

    nt = reasoned.get('nguyên_tắc', {})
    if not nt.get('name'):
        issues.append(f'{uid}: nguyên_tắc missing name')
    if not nt.get('sources'):
        issues.append(f'{uid}: nguyên_tắc has no sources')

    dx = reasoned.get('đề_xuất', [])
    if not dx:
        issues.append(f'{uid}: đề_xuất is empty')

    tc = reasoned.get('tham_chiếu', {})
    if len(tc.get('sources', [])) < MIN_SOURCES:
        issues.append(f'{uid}: tham_chiếu has < {MIN_SOURCES} sources')

    return issues


# ── Main ──

def main():
    parser = argparse.ArgumentParser(description='UXP Deep Reasoning Pipeline')
    parser.add_argument('--report', required=True, help='Path to ux-review-report.md')
    parser.add_argument('--force', action='store_true', help='Re-reason even if already enriched')
    parser.add_argument('--verify', action='store_true', help='Quality check + report')
    parser.add_argument('--domain', default='banking', help='Domain context (default: banking)')
    args = parser.parse_args()

    report_path = Path(args.report)
    if not report_path.exists():
        print(f'❌ Report not found: {report_path}', file=sys.stderr)
        sys.exit(1)

    report_dir = report_path.parent

    # Step 1: Load heuristic DB
    db = load_heuristics_db()
    print(f'📚 Heuristics DB: {len(db.get("nielsen", {}))} Nielsen, '
          f'{len(db.get("wcag", {}))} WCAG, '
          f'{len(db.get("laws", {}))} Laws', file=sys.stderr)

    # Step 2: Parse UXPs from report
    uxps = parse_uxps_from_report(report_path)
    print(f'📋 Parsed {len(uxps)} UXPs from report', file=sys.stderr)

    # Step 3: Load screen MDs
    screens = load_screen_mds(report_dir)
    print(f'📱 Loaded {len(screens)} screen MDs', file=sys.stderr)

    # Step 4: Load existing enriched-data.json
    enriched_path = report_dir / 'enriched-data.json'
    enriched = {}
    if enriched_path.exists():
        try:
            enriched = json.loads(enriched_path.read_text('utf-8'))
        except (json.JSONDecodeError, UnicodeDecodeError):
            enriched = {}

    existing_uxps = enriched.get('uxps', {})
    if not isinstance(existing_uxps, dict):
        existing_uxps = {}

    # Step 5: Reason each UXP
    reasoned_count = 0
    skipped_count = 0
    all_issues: list[str] = []

    for uxp in uxps:
        uid = uxp['id']

        # Skip if already reasoned (unless --force)
        if not args.force and uid in existing_uxps:
            existing = existing_uxps[uid]
            if existing.get('hiện_trạng') and len(existing['hiện_trạng']) >= MIN_HIEN_TRANG_LEN:
                skipped_count += 1
                if args.verify:
                    issues = verify_reasoning(existing, uid)
                    all_issues.extend(issues)
                continue

        reasoned = reason_single_uxp(uxp, screens, db)
        existing_uxps[uid] = reasoned
        reasoned_count += 1

        if args.verify:
            issues = verify_reasoning(reasoned, uid)
            all_issues.extend(issues)

        status = '✅' if not verify_reasoning(reasoned, uid) else '⚠️'
        print(f'  {status} {uid}: {len(reasoned["hiện_trạng"])}ch HT, '
              f'{len(reasoned["tham_chiếu"].get("sources", []))} sources', file=sys.stderr)

    # Step 6: Save to enriched-data.json
    enriched['uxps'] = existing_uxps
    enriched['_reasoning_engine'] = 'reason_uxps.py/deterministic'
    enriched['_reasoning_timestamp'] = datetime.now().isoformat()

    enriched_path.write_text(json.dumps(enriched, ensure_ascii=False, indent=2), encoding='utf-8')

    # Report
    print(f'\n✅ Reasoned: {reasoned_count} UXPs, Skipped: {skipped_count}', file=sys.stderr)
    print(f'📁 Saved to: {enriched_path}', file=sys.stderr)

    if args.verify:
        if all_issues:
            print(f'\n⚠️  Quality issues ({len(all_issues)}):', file=sys.stderr)
            for issue in all_issues:
                print(f'  • {issue}', file=sys.stderr)
        else:
            print(f'\n✅ All {len(uxps)} UXPs pass quality checks', file=sys.stderr)

    # JSON summary to stdout
    summary = {
        'uxps_total': len(uxps),
        'reasoned': reasoned_count,
        'skipped': skipped_count,
        'issues': len(all_issues),
        'output': str(enriched_path),
    }
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
