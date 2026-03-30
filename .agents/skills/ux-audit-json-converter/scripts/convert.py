#!/usr/bin/env python3
"""
convert.py — Module Index → report-data.json converter.

Reads module-index.json (Lớp 2: canonical, single source of truth)
and assembles report-data.json (Lớp 3: consumer-ready for render_report.py).

This script ONLY reads module-index.json. It never touches raw markdown
or handoff files directly. All format normalization happens in index_module.py.

Usage:
    python3 convert.py --module /path/to/module/
    python3 convert.py --module /path/to/module/ --dry
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from score_engine import calculate_scores as _calc_scores, ScoreResult

# ═══════════════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════════════

HEURISTIC_CATEGORIES = [
    {"key": "flow",      "name_vi": "Luồng người dùng",     "name_en": "Flow & Navigation"},
    {"key": "component", "name_vi": "Thành phần",            "name_en": "Component & DDL"},
    {"key": "visual",    "name_vi": "Thiết kế trực quan",    "name_en": "Visual Design"},
    {"key": "content",   "name_vi": "Nội dung",              "name_en": "Content & Copy"},
    {"key": "a11y",      "name_vi": "Tiếp cận",              "name_en": "Accessibility"},
    {"key": "trust",     "name_vi": "Tin cậy & Bảo mật",     "name_en": "Trust & Security"},
]

CATEGORY_MAP = {
    'component': 'component', 'feature': 'flow', 'visual': 'visual',
    'content': 'content', 'accessibility': 'a11y', 'safety': 'trust',
    'security': 'trust', 'trust': 'trust', 'ux': 'flow', 'ux law': 'flow',
    'skill a': 'component', 'skill b': 'flow', 'skill c': 'visual',
    'ddl law': 'flow',
}


# ═══════════════════════════════════════════════════════════════════════
# HEURISTIC REFERENCE DB
# ═══════════════════════════════════════════════════════════════════════

_HEURISTIC_DB_PATH = Path(__file__).parent.parent / 'references' / 'heuristic-db.json'
_HEURISTIC_DB: dict[str, Any] = {}


def _load_heuristic_db() -> dict[str, Any]:
    """Load heuristic-db.json once (lazy singleton)."""
    global _HEURISTIC_DB
    if _HEURISTIC_DB:
        return _HEURISTIC_DB
    if _HEURISTIC_DB_PATH.exists():
        _HEURISTIC_DB = json.loads(
            _HEURISTIC_DB_PATH.read_text(encoding='utf-8'))
    return _HEURISTIC_DB


def _match_heuristic_ref(text: str) -> list[dict]:
    """Match heuristic/evidence text to official reference entries.

    Returns list of ref dicts: [{name, url, quote, source}, ...]
    """
    db = _load_heuristic_db()
    if not db:
        return []

    text_lower = text.lower()
    refs: list[dict] = []
    seen_keys: set[str] = set()

    # Nielsen match: "Nielsen #N" or "Heuristic N" or "H#N"
    for m in re.finditer(r'(?:nielsen|heuristic|h)\s*#?\s*(\d+)', text_lower):
        num = m.group(1)
        entry = db.get('nielsen', {}).get(num)
        key = f'nielsen.{num}'
        if entry and key not in seen_keys:
            refs.append(entry)
            seen_keys.add(key)

    # WCAG match: "WCAG X.Y.Z" or "SC X.Y.Z"
    for m in re.finditer(r'(?:wcag|sc)\s*([\d.]+)', text_lower):
        sc = m.group(1)
        entry = db.get('wcag', {}).get(sc)
        key = f'wcag.{sc}'
        if entry and key not in seen_keys:
            refs.append(entry)
            seen_keys.add(key)

    # Laws match by keyword
    laws_db = db.get('laws', {})
    law_keywords = {
        'fitts': 'fitts', 'hick': 'hick', 'jakob': 'jakob',
        'miller': 'miller', 'peak': 'peak_end', 'zeigarnik': 'zeigarnik',
        'von restorff': 'von_restorff', 'doherty': 'doherty',
        'aesthetic': 'aesthetic_usability',
    }
    for keyword, law_key in law_keywords.items():
        if keyword in text_lower:
            entry = laws_db.get(law_key)
            key = f'laws.{law_key}'
            if entry and key not in seen_keys:
                refs.append(entry)
                seen_keys.add(key)

    return refs


# ═══════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════

def _score_color(score: int) -> str:
    if score < 50:
        return '#b91c1c'
    if score < 70:
        return '#c2410c'
    return '#15803d'


def _score_offset(score: int) -> int:
    """Hero ring: r=51, circumference=320. offset = 320 * (1 - score/100)."""
    return round(320 * (1 - score / 100))


def _screen_score_offset(score: int) -> int:
    """For per-screen SVG rings: r=25, circumference=157."""
    return round(157 * (1 - score / 100))


# ═══════════════════════════════════════════════════════════════════════
# IMAGE RESOLUTION ENGINE v2 — 5-tier
# ═══════════════════════════════════════════════════════════════════════

_OVERLAY_KW = [
    'bottom sheet', 'dialog', 'confirm', 'popup', 'modal', 'overlay',
    'picker', 'otp', 'xác nhận', 'dropdown', 'action sheet', 'toast',
    'alert', 'cảnh báo',
]
_ERROR_KW = [
    'lỗi', 'error', 'invalid', 'thiếu', 'missing', 'validation',
    'sai', 'trống', 'chưa nhập', 'fail', 'case lỗi',
]
_SUCCESS_KW = ['thành công', 'success', 'hoàn tất', 'kết quả']


def _extract_evidence_signals(evidence_text: str,
                              uxp_fields: dict = None) -> dict:
    """Extract resolution signals from evidence and UXP fields.

    Signals: state_ordinal, filename_ref, artboard_ids,
             context_keywords, is_overlay/error/success_context.
    """
    signals = {
        'state_ordinal': None,
        'filename_ref': None,
        'artboard_ids': [],
        'context_keywords': [],
        'is_overlay_context': False,
        'is_error_context': False,
        'is_success_context': False,
    }

    all_text = evidence_text or ''
    if uxp_fields:
        all_text += ' ' + (uxp_fields.get('Vấn đề', '') or '')
        all_text += ' ' + (uxp_fields.get('Giải pháp', '') or '')

    if not all_text.strip():
        return signals

    # Signal 1: State ordinal — "Từ ảnh state 2:" or "state 2:"
    m = re.search(r'(?:Từ ảnh\s+)?state\s+(\d+)', all_text, re.IGNORECASE)
    if m:
        signals['state_ordinal'] = int(m.group(1))

    # Signal 2: Direct filename ref — multiple patterns
    # Pattern A: "Từ ảnh xxx.png" or "Từ ảnh: xxx.png"
    m = re.search(r'Từ ảnh[:\s]+([a-zA-Z0-9_.\-]+\.png)', all_text)
    if m:
        signals['filename_ref'] = m.group(1)
    # Pattern B: "ảnh xxx.png" or "ảnh: xxx.png" (without "Từ")
    if not signals['filename_ref']:
        m = re.search(r'ảnh[:\s]+([a-zA-Z0-9_.\-]+\.png)', all_text)
        if m:
            signals['filename_ref'] = m.group(1)
    # Pattern C: "From image xxx.png"
    if not signals['filename_ref']:
        m = re.search(r'From image[: ]+([a-zA-Z0-9_.\-]+\.png)', all_text)
        if m:
            signals['filename_ref'] = m.group(1)
    # Pattern D: bare "— xxx.png" or inline filename mention
    if not signals['filename_ref']:
        m = re.search(r'[\s—–-]+([a-zA-Z0-9_.\-]+\.png)', all_text)
        if m:
            signals['filename_ref'] = m.group(1)

    # Signal 3: Artboard IDs — "Vision 7001:" or inline 4-digit
    for m in re.finditer(r'Vision\s+(\d{4})', all_text):
        aid = m.group(1)
        if aid not in signals['artboard_ids']:
            signals['artboard_ids'].append(aid)
    # Also extract standalone 4-digit IDs from evidence
    if not signals['artboard_ids']:
        for m in re.finditer(r'\b(\d{4})\b', all_text):
            aid = m.group(1)
            if aid not in signals['artboard_ids']:
                signals['artboard_ids'].append(aid)

    # Signal 4: Context keywords
    stop = {'của', 'và', 'có', 'với', 'cho', 'các', 'trong', 'khi', 'là',
            'được', 'the', 'and', 'for', 'with', 'not', 'this', 'that',
            'không', 'pass', 'gap', 'một', 'này', 'từ', 'ảnh', 'state',
            'vision', 'ddl', 'uxg', 'comp', 'token'}
    words = re.findall(r'[a-zA-Z\u00C0-\u1EF9]{3,}', all_text.lower())
    signals['context_keywords'] = list(
        set(w for w in words if w not in stop)
    )[:30]

    # Signal 5: Context type
    text_lower = all_text.lower()
    signals['is_overlay_context'] = any(kw in text_lower for kw in _OVERLAY_KW)
    signals['is_error_context'] = any(kw in text_lower for kw in _ERROR_KW)
    signals['is_success_context'] = any(kw in text_lower for kw in _SUCCESS_KW)

    return signals


def _semantic_score(images: list[dict], signals: dict) -> str:
    """Score images using semantic overlap. Returns best filename or ''."""
    ctx_kw = set(signals.get('context_keywords', []))
    if not ctx_kw and not signals.get('is_overlay_context') \
            and not signals.get('is_error_context'):
        return ''

    scores: dict[str, int] = {}
    for img in images:
        if not img.get('on_disk'):
            continue
        fn = img['filename']
        role = img.get('role', '')
        score = 0

        # A. Role match (+10)
        if signals.get('is_overlay_context') and 'overlay' in role:
            score += 10
        elif signals.get('is_error_context') and (
                'error' in role or role.startswith('error')):
            score += 10
        elif signals.get('is_success_context') and 'success' in role:
            score += 10

        # B. Alt text keyword overlap (+5/word)
        alt_words = set(re.findall(
            r'[a-zA-Z\u00C0-\u1EF9]{3,}',
            (img.get('alt_text', '') or '').lower()
        ))
        score += len(ctx_kw & alt_words) * 5

        # C. Role keyword overlap (+3)
        role_words = set(
            role.replace(':', ' ').replace('_', ' ').lower().split()
        )
        score += len(ctx_kw & role_words) * 3

        # D. Image keywords overlap (+3/word)
        img_kw = set(img.get('keywords', []))
        score += len(ctx_kw & img_kw) * 3

        # E. Text elements overlap (+2/word) — from artboard-index
        if img.get('text_elements'):
            txt_words: set[str] = set()
            for t in img['text_elements']:
                txt_words.update(
                    w.lower() for w in re.findall(
                        r'[a-zA-Z\u00C0-\u1EF9]{3,}', t
                    )
                )
            score += len(ctx_kw & txt_words) * 2

        # F. Penalty: base when overlay/error context
        if role == 'base' and (
                signals.get('is_overlay_context')
                or signals.get('is_error_context')):
            score -= 5

        scores[fn] = score

    if not scores:
        return ''
    best = max(scores, key=lambda k: scores[k])
    return best if scores[best] >= 3 else ''


def _resolve_screenshot_v2(
    screen_id: str,
    image_map: dict,
    signals: dict,
    extra_artboard_ids: list = None,
) -> tuple[str, int]:
    """5-tier Resolution Engine for precise image mapping.

    Tiers:
      1. EXACT — filename ref directly from evidence
      2. ORDINAL — "state N" maps to ordinal N in SCR-MD order
      3. ARTBOARD — artboard ID prefix match on filename
      4. SEMANTIC — keyword scoring (role, alt_text, context)
      5. DEFAULT — base image or first available

    Returns: (screenshot_path, tier_used)
    """
    lt = image_map.get('image_lookup_table', {})
    lookup = lt.get(screen_id)

    # C-1: Defensive fallback — screen_id not in lookup table
    # Try regex extract SCR-ID from descriptive screen_id
    if not lookup and screen_id:
        # Attempt 1: Extract embedded SCR-ID
        m_scr = re.search(r'(SCR-\w+-\d+)', screen_id)
        if m_scr and m_scr.group(1) in lt:
            lookup = lt[m_scr.group(1)]
        # Attempt 2: Fuzzy match screen_id against lookup keys
        if not lookup:
            best_key = ''
            best_overlap = 0
            sid_words = set(re.findall(r'\w+', screen_id.lower()))
            for key in lt:
                key_words = set(re.findall(r'\w+', key.lower()))
                overlap = len(sid_words & key_words)
                if overlap > best_overlap:
                    best_overlap = overlap
                    best_key = key
            if best_key and best_overlap >= 1:
                lookup = lt[best_key]

    # C-2: Defensive fallback — lookup exists but has 0 images
    # Fall back to disk_files
    if (not lookup or not lookup.get('images')) and image_map.get('disk_files'):
        disk = image_map['disk_files']
        if disk:
            # Return first disk file as T5 fallback
            return f'ui/{disk[0]}', 5

    if not lookup or not lookup.get('images'):
        return '', 0

    images = lookup['images']
    by_filename = lookup.get('by_filename', {})
    by_ordinal = lookup.get('by_ordinal', {})
    by_role = lookup.get('by_role', {})

    # Merge artboard IDs
    artboard_ids = list(signals.get('artboard_ids', []))
    if extra_artboard_ids:
        artboard_ids.extend(
            aid for aid in extra_artboard_ids if aid not in artboard_ids
        )

    # Tier 1: EXACT — filename ref
    fn_ref = signals.get('filename_ref')
    if fn_ref:
        idx = by_filename.get(fn_ref)
        if idx is not None and images[idx].get('on_disk'):
            return f'ui/{fn_ref}', 1
        # C-1b: filename not in lookup but exists on disk
        if fn_ref in [f for f in image_map.get('disk_files', [])]:
            return f'ui/{fn_ref}', 1

    # Tier 2: ORDINAL — "state N" → ordinal N
    s_ord = signals.get('state_ordinal')
    if s_ord:
        idx = by_ordinal.get(str(s_ord))
        if idx is not None and images[idx].get('on_disk'):
            return f'ui/{images[idx]["filename"]}', 2

    # Tier 3: ARTBOARD — artboard ID → prefix match
    if artboard_ids:
        for aid in artboard_ids:
            for img in images:
                if img.get('artboard_id') == aid and img.get('on_disk'):
                    return f'ui/{img["filename"]}', 3

    # Tier 4: SEMANTIC — keyword scoring
    best_fn = _semantic_score(images, signals)
    if best_fn:
        return f'ui/{best_fn}', 4

    # Tier 5: DEFAULT — base image or first on_disk
    base_indices = by_role.get('base', [])
    if base_indices:
        img = images[base_indices[0]]
        if img.get('on_disk'):
            return f'ui/{img["filename"]}', 5
    for img in images:
        if img.get('on_disk'):
            return f'ui/{img["filename"]}', 5

    return '', 0


# ═══════════════════════════════════════════════════════════════════════
# ASSEMBLERS
# ═══════════════════════════════════════════════════════════════════════

def assemble_meta(index: dict) -> dict:
    """Build meta section from module-index report_meta."""
    rm = index['report_meta']
    return {
        'client_name': rm.get('client_name', '') or 'Co-opBank',
        'product_name': rm.get('product_name', '') or 'Co-opBank Mobile Banking',
        'module_name': rm.get('module_name', ''),
        'domain': rm.get('domain', '') or 'Banking',
        'section': rm.get('section', ''),
        'module_dir': index['_meta'].get('module_dir', ''),
    }


def assemble_stats(index: dict, score_result: 'ScoreResult | None' = None) -> dict:
    """Build stats section from score_block + screens + uxps.

    When score_result is provided (from score_engine), uses its re-counted
    values for accuracy. Falls back to score_block/claimed values otherwise.
    """
    sb = index['score_block']
    screens = index['screens']
    uxps = index['uxp_blocks']

    if score_result:
        # Use verified counts from score_engine
        total_pass = score_result.total_pass
        total_gap = score_result.total_gap
        total_checks = score_result.total_checks
        score = score_result.simple_score
        weighted = score_result.weighted_score
    else:
        # Fallback: calculate from index data
        total_pass = sb.get('pass', 0) or sum(s.get('pass_count', 0) for s in screens)
        total_gap = sb.get('gap', 0) or sum(s.get('gap_count', 0) for s in screens)
        total_checks = sb.get('total_checks', 0) or sum(s.get('check_count', 0) for s in screens)
        score = sb.get('score', 0)
        if not score and (total_pass + total_gap) > 0:
            score = round(total_pass / (total_pass + total_gap) * 100)
        weighted = score  # No weighted calc without engine

    # Severity counts from UXPs
    sev_counts = {'critical': 0, 'major': 0, 'minor': 0}
    for u in uxps:
        sev = u.get('severity', 'Major').lower()
        if sev in sev_counts:
            sev_counts[sev] += 1

    return {
        'screen_count': len(screens),
        'check_count': total_checks,
        'gap_count': total_gap,
        'pass_count': total_pass,
        'proposal_count': len(uxps),
        'overall_score': score,
        'overall_score_color': _score_color(score),
        'overall_score_offset': _score_offset(score),
        'overall_weighted_score': weighted,
        'severity_counts': sev_counts,
    }


def assemble_screens(index: dict,
                     score_result: 'ScoreResult | None' = None) -> list[dict]:
    """Build screens array from module-index screens data.

    When score_result is provided, uses re-counted scores including
    weighted_score per screen.
    """
    # Build lookup from score_result
    score_by_screen: dict[str, Any] = {}
    if score_result:
        for ss in score_result.screens:
            score_by_screen[ss.screen_id] = ss

    result = []
    for s in index['screens']:
        screen_id = s.get('screen_id', '')
        screen_name = s.get('screen_name', '')

        ss = score_by_screen.get(screen_id)
        if ss:
            # Use engine-verified scores
            score = ss.simple_score
            weighted = ss.weighted_score
        else:
            score = s.get('score', 0)
            weighted = score

        result.append({
            'id': screen_id,
            'name': f'{screen_name} (`{screen_id}`)' if screen_id else screen_name,
            'type': s.get('screen_type', ''),
            'score': score,
            'score_color': _score_color(score),
            'score_offset': _screen_score_offset(score),
            'weighted_score': weighted,
            'gap_count': s.get('gap_count', 0),
            'artboard_count': s.get('artboard_count', 0),
        })
    return result


def assemble_uxps(index: dict) -> list[dict]:
    """Build uxps array from module-index uxp_blocks."""
    image_map = index.get('image_map', {})
    result = []

    for u in index['uxp_blocks']:
        fields = u.get('fields', {})
        screen_tag = fields.get('Màn hình', u.get('screen_tag', ''))
        screen_id = u.get('screen_id', '')
        gap_ref = fields.get('Gap ref', '')

        # Parse check numbers from gap_ref
        check_nums = [int(n) for n in re.findall(r'#(\d+)', gap_ref)]

        # Collect evidence text + artboard IDs from related checks
        evidence_text = ''
        extra_artboard_ids: list[str] = []
        for screen_data in index['screens']:
            if screen_data.get('screen_id') == screen_id:
                for check in screen_data.get('checks', []):
                    if check.get('num') in check_nums:
                        evidence_text += ' ' + check.get('evidence', '')
                        extra_artboard_ids.extend(
                            check.get('_evidence_artboard_ids', [])
                        )

        # Extract signals from evidence + UXP fields
        signals = _extract_evidence_signals(evidence_text, fields)

        screenshot, tier = _resolve_screenshot_v2(
            screen_id, image_map, signals, extra_artboard_ids
        )

        # Resolve heuristic references
        heuristic_text = f'{gap_ref} {fields.get("DDL", "")}'
        matched_refs = _match_heuristic_ref(heuristic_text)

        result.append({
            'id': u['id'],
            'severity': u.get('severity', 'Major'),
            'screen_tag': screen_tag,
            'problem': fields.get('Vấn đề', ''),
            'gap_ref': gap_ref,
            'ddl_ref': fields.get('DDL', ''),
            'solution': fields.get('Giải pháp', ''),
            'screenshot_path': screenshot,
            '_img_tier': tier,
            'references': matched_refs,
        })
    return result


def assemble_gaps_by_screen(index: dict) -> list[dict]:
    """Build gaps_by_screen from check tables (verdict=gap)."""
    image_map = index.get('image_map', {})
    result = []

    for screen_data in index['screens']:
        screen_id = screen_data.get('screen_id', '')
        screen_name = screen_data.get('screen_name', '')
        screen_type = screen_data.get('screen_type', '')

        gaps = []
        for check in screen_data.get('checks', []):
            verdict = check.get('verdict', '').lower().strip()
            if verdict != 'gap':
                continue

            num = check.get('num', 0)
            evidence = check.get('evidence', '')

            # Resolve heuristic from category
            category = check.get('category', '').lower()
            heuristic_key = CATEGORY_MAP.get(category, 'flow')
            heuristic_name = ''
            for h in HEURISTIC_CATEGORIES:
                if h['key'] == heuristic_key:
                    heuristic_name = f"{h['name_en']} ({h['name_vi']})"
                    break

            # Extract DDL/UXG ref
            ref = check.get('ddl_ref', '')
            if not ref:
                ref_match = re.search(r'(UXG-\d+|COMP:\w+|TOKEN:\w+)', evidence)
                if ref_match:
                    ref = ref_match.group(1)

            severity = check.get('severity', 'Minor')

            # Screenshot resolution — v2 engine
            check_title = check.get('check', '')
            evidence_combined = f'{check_title} {evidence}'
            signals = _extract_evidence_signals(evidence_combined)
            extra_artboard_ids = check.get('_evidence_artboard_ids', [])

            screenshot, tier = _resolve_screenshot_v2(
                screen_id, image_map, signals, extra_artboard_ids
            )
            screenshot_filename = screenshot.replace('ui/', '') if screenshot else ''

            user_impact = check.get('check', '')

            # Resolve heuristic references
            ref_text = f'{ref} {heuristic_name} {evidence}'
            matched_refs = _match_heuristic_ref(ref_text)

            gaps.append({
                'num': num,
                'title': check.get('check', ''),
                'ref': ref,
                'severity': severity,
                'user_impact': user_impact,
                'heuristic': heuristic_name,
                'evidence': evidence,
                'screenshot': screenshot_filename,
                'screen_id': screen_id,
                'screen_name': screen_name,
                'screen_type': screen_type,
                'screenshot_path': screenshot,
                '_img_tier': tier,
                'description': evidence or check.get('check', ''),
                'ddl_evidence': check.get('ddl_ref', ''),
                'ref_count': len(matched_refs),
                'references': matched_refs,
            })

        if gaps:
            result.append({
                'screen_id': screen_id,
                'screen_name': f'{screen_name} (`{screen_id}`)' if screen_id else screen_name,
                'screen_type': screen_type,
                'gaps': gaps,
            })

    return result


def assemble_heuristics(index: dict) -> list[dict]:
    """Build heuristic scorecard from check tables."""
    # Count pass/gap per heuristic category
    cat_stats = {h['key']: {'pass': 0, 'gap': 0} for h in HEURISTIC_CATEGORIES}

    for screen_data in index['screens']:
        for check in screen_data.get('checks', []):
            verdict = check.get('verdict', '').lower().strip()
            if verdict not in ('pass', 'gap'):
                continue

            category = check.get('category', '').lower()
            heuristic_key = CATEGORY_MAP.get(category, 'flow')

            if heuristic_key in cat_stats:
                if verdict == 'pass':
                    cat_stats[heuristic_key]['pass'] += 1
                else:
                    cat_stats[heuristic_key]['gap'] += 1

    result = []
    for h in HEURISTIC_CATEGORIES:
        stats = cat_stats[h['key']]
        total = stats['pass'] + stats['gap']
        score = round(stats['pass'] / total * 100) if total > 0 else 100

        result.append({
            'key': h['key'],
            'name_vi': h['name_vi'],
            'name_en': h['name_en'],
            'score': score,
            'gap_count': stats['gap'],
        })

    return result


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════

def convert(index: dict) -> dict:
    """Assemble report-data.json from module-index.json."""
    # Run score engine for accurate simple + weighted scores
    score_result = _calc_scores(
        index.get('screens', []),
        index.get('uxp_blocks', []),
    )

    stats = assemble_stats(index, score_result)
    gaps_by_screen = assemble_gaps_by_screen(index)

    # Reconcile gap_count with actual gaps produced
    actual_gap_count = sum(len(sg['gaps']) for sg in gaps_by_screen)
    if stats['gap_count'] != actual_gap_count:
        stats['gap_count'] = actual_gap_count

    # Build discrepancies section if any
    discrepancies = []
    for d in score_result.discrepancies:
        discrepancies.append({
            'screen_id': d.screen_id,
            'field': d.field_name,
            'claimed': d.claimed,
            'actual': d.actual,
        })

    result = {
        'meta': assemble_meta(index),
        'stats': stats,
        'screens': assemble_screens(index, score_result),
        'uxps': assemble_uxps(index),
        'gaps_by_screen': gaps_by_screen,
        'heuristics': assemble_heuristics(index),
    }

    if discrepancies:
        result['_score_discrepancies'] = discrepancies

    return result


def main():
    parser = argparse.ArgumentParser(
        description='module-index.json → report-data.json converter'
    )
    parser.add_argument('--module', type=Path, required=True,
                        help='Path to module directory')
    parser.add_argument('--dry', action='store_true',
                        help='Print to stdout instead of writing file')
    args = parser.parse_args()

    module_dir = args.module.resolve()
    index_path = module_dir / 'module-index.json'

    if not index_path.exists():
        print(f'❌ {module_dir.name}: module-index.json not found. '
              f'Run index_module.py first.', file=sys.stderr)
        sys.exit(1)

    index = json.loads(index_path.read_text(encoding='utf-8'))
    report_data = convert(index)

    output_json = json.dumps(report_data, ensure_ascii=False, indent=2)

    if args.dry:
        print(output_json)
    else:
        out_path = module_dir / 'report-data.json'
        out_path.write_text(output_json, encoding='utf-8')

        stats = report_data['stats']
        n_uxps = stats['proposal_count']
        n_gaps = stats['gap_count']
        score = stats['overall_score']
        n_screens = stats['screen_count']
        n_imgs = sum(1 for u in report_data['uxps'] if u.get('screenshot_path'))
        n_gap_imgs = sum(
            1 for sg in report_data['gaps_by_screen']
            for g in sg['gaps']
            if g.get('screenshot_path')
        )

        weighted = stats.get('overall_weighted_score', score)
        n_disc = len(report_data.get('_score_discrepancies', []))

        print(f'✅ Converted: {module_dir.name}', file=sys.stderr)
        print(f'   Score: {score}% (simple) | {weighted}% (weighted) | Screens: {n_screens}', file=sys.stderr)
        print(f'   UXPs: {n_uxps} ({n_imgs} with screenshots)', file=sys.stderr)
        print(f'   Gaps: {n_gaps} ({n_gap_imgs} with screenshots)', file=sys.stderr)
        if n_disc > 0:
            print(f'   ⚠️  Discrepancies: {n_disc} (claimed vs actual)', file=sys.stderr)
        print(f'   Output: {out_path}', file=sys.stderr)


if __name__ == '__main__':
    main()
