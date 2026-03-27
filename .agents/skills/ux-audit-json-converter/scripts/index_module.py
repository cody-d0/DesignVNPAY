#!/usr/bin/env python3
"""
index_module.py — Per-module deep indexer.

Reads ALL raw sources from a single module directory, normalizes biến thiên
formats into a canonical module-index.json (Lớp 2: single source of truth).

Usage:
    python3 index_module.py --module /path/to/module/
    python3 index_module.py --module /path/to/module/ --dry  # print, don't write

Architecture:
    Raw Sources (7+ nguồn, 12+ format variants)
        → index_module.py (detect format, normalize, merge)
        → module-index.json (canonical, single source of truth)
        → convert.py reads ONLY module-index.json
        → report-data.json (consumer-ready for render_report.py)

Self-learning:
    When a format doesn't match any known template in format-registry.md,
    the script logs a structured error. The agent then:
    1. Reads the error log
    2. Reasons about the new format
    3. Updates format-registry.md with a new FMT-XXX entry
    4. Re-runs this indexer
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, Optional

# ═══════════════════════════════════════════════════════════════════════
# CONSTANTS — Alias maps derived from format-registry.md
# ═══════════════════════════════════════════════════════════════════════

# H1 patterns (FMT-001, FMT-002, FMT-003)
H1_PATTERNS = [
    # FMT-001: # UX Review Report — {Module}
    (r'^#\s+UX\s+Review\s+Report\s+—\s+(.+)$', 'FMT-001'),
    # FMT-002: # UX Audit — {Module} · {Product}
    (r'^#\s+UX\s+Audit\s+—\s+(.+?)\s+·\s+(.+)$', 'FMT-002'),
    # FMT-003: # UX Review Report — {Module} | {Product}
    (r'^#\s+UX\s+Review\s+Report\s+—\s+(.+?)\s+\|\s+(.+)$', 'FMT-003'),
]

# Metadata key aliases (FMT-010, FMT-011, FMT-012)
# Maps raw key (lowercase) → canonical key
META_ALIASES = {
    # EN keys
    'product': 'product_name', 'client': 'client_name',
    'section': 'section', 'module': 'module_name',
    'domain': 'domain', 'generated': 'generated_at',
    'screens reviewed': 'screen_count', 'screens': 'screen_count',
    'artboards': 'artboard_count',
    'overlays detected': 'overlay_count', 'overlays': 'overlay_count',
    'total checks': 'check_count', 'figma': 'figma_ref',
    # VN keys
    'sản phẩm': 'product_name',
    'ngày audit': 'generated_at',
    'tổng check': 'check_count',
    'tổng màn hình': 'screen_count',
    'pipeline': '_pipeline_info',
}

# Check table column name → canonical name
COLUMN_ALIASES = {
    '#': 'num',
    'check': 'check',
    'category': 'category',
    'source': 'category',  # FMT-022: Source maps to category
    'severity': 'severity',
    'ddl ref': 'ddl_ref',
    'verdict': 'verdict',
    'evidence': 'evidence',
}

# Category → heuristic key mapping
CATEGORY_MAP = {
    'component': 'component', 'feature': 'flow', 'visual': 'visual',
    'content': 'content', 'accessibility': 'a11y', 'safety': 'trust',
    'security': 'trust', 'trust': 'trust', 'ux': 'flow', 'ux law': 'flow',
    # From Source column (FMT-022)
    'skill a': 'component', 'skill b': 'flow', 'skill c': 'visual',
    'ddl law': 'flow',
}

# Manifest key aliases (FMT-070, FMT-071)
MANIFEST_ALIASES = {
    'screen_count': 'screen_count',
    'screens_count': 'screen_count',
    'artboard_count': 'artboard_count',
    'artboards_count': 'artboard_count',
    'overlay_count': 'overlay_count',
    'overlays_detected': 'overlay_count',
}

# Evidence image reference patterns (FMT-060..063)
EVIDENCE_IMG_PATTERNS = [
    (r'[Tt]ừ ảnh\s+([a-zA-Z0-9_.-]+\.png)', 'FMT-060'),
    (r'[Ff]rom image[: ]+([a-zA-Z0-9_.-]+\.png)', 'FMT-061'),
    (r'Vision(?:\s+\d+)?:\s', 'FMT-062'),  # No direct image ref
]


# ═══════════════════════════════════════════════════════════════════════
# CORE PARSERS
# ═══════════════════════════════════════════════════════════════════════

def _read_lines(path: Path) -> list[str]:
    """Read file lines, stripping trailing newline."""
    if not path.exists():
        return []
    return path.read_text(encoding='utf-8').splitlines()


def _read_json(path: Path) -> Optional[dict]:
    """Read JSON file, return None if not found."""
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        _log_issue('json_parse_error', str(path), str(e))
        return None


# ═══════════════════════════════════════════════════════════════════════
# ISSUE LOGGING (for self-learning)
# ═══════════════════════════════════════════════════════════════════════

_issues: list[dict] = []


def _log_issue(trigger: str, context: str, detail: str,
               line_num: int = 0, raw_text: str = ''):
    """Log a format issue for self-learning."""
    _issues.append({
        'trigger': trigger,
        'context': context,
        'detail': detail,
        'line_num': line_num,
        'raw_text': raw_text[:200],
    })


# ═══════════════════════════════════════════════════════════════════════
# PARSER: Report Metadata (H1 + blockquote/bold metadata)
# ═══════════════════════════════════════════════════════════════════════

def parse_report_meta(lines: list[str]) -> dict:
    """Parse H1 title and metadata block from report markdown.

    Handles FMT-001/002/003 (H1) and FMT-010/011/012 (meta keys).
    Returns canonical report_meta dict.
    """
    result = {
        'h1_raw': '',
        'h1_format': '',
        'client_name': 'Co-opBank',  # default
        'product_name': '',
        'module_name': '',
        'domain': '',
        'section': '',
        'generated_at': '',
        'figma_file': '',
        'figma_node': '',
        'screen_count': 0,
        'artboard_count': 0,
        'overlay_count': 0,
    }

    formats_detected = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        # ── H1 detection ──
        if stripped.startswith('# ') and not stripped.startswith('## '):
            result['h1_raw'] = stripped
            matched = False
            for pattern, fmt_id in H1_PATTERNS:
                m = re.match(pattern, stripped)
                if m:
                    result['h1_format'] = fmt_id
                    formats_detected.append(fmt_id)
                    if fmt_id == 'FMT-001':
                        result['module_name'] = m.group(1).strip()
                    elif fmt_id in ('FMT-002', 'FMT-003'):
                        result['module_name'] = m.group(1).strip()
                        result['product_name'] = m.group(2).strip()
                    matched = True
                    break

            if not matched:
                _log_issue('h1_unknown', 'report_meta',
                           f'H1 does not match known patterns',
                           line_num=i+1, raw_text=stripped)
            continue

        # ── H2 (subtitle) ──
        if stripped.startswith('## ') and i < 5:
            h2_text = stripped[3:].strip()
            # Extract product name from H2 if present
            if not result['product_name'] and '·' in h2_text:
                parts = h2_text.split('·')
                result['product_name'] = parts[0].strip()
            continue

        # ── Metadata lines (blockquote or bare) ──
        meta_line = stripped
        meta_fmt = 'FMT-010'

        # Strip blockquote prefix
        if meta_line.startswith('>'):
            meta_line = meta_line.lstrip('>').strip()
            meta_fmt = 'FMT-011'

        # Match **Key:** Value pattern
        m = re.match(r'^\*\*(.+?):\*\*\s*(.+)$', meta_line)
        if not m:
            # Also try **Key:** Value with backticks
            m = re.match(r'^\*\*(.+?)\*\*\s*(.+)$', meta_line)
        if m:
            raw_key = m.group(1).strip().rstrip(':').lower()
            raw_val = m.group(2).strip()

            canonical = META_ALIASES.get(raw_key)
            if canonical:
                if meta_fmt not in formats_detected:
                    formats_detected.append(meta_fmt)

                if canonical in ('screen_count', 'artboard_count', 'overlay_count'):
                    # Extract number from value like "4 | **Artboards:** 9"
                    nums = re.findall(r'\d+', raw_val)
                    if nums:
                        result[canonical] = int(nums[0])
                elif canonical == 'figma_ref':
                    # Parse Figma file + node
                    fm = re.search(r'`([a-zA-Z0-9]+)`', raw_val)
                    if fm:
                        result['figma_file'] = fm.group(1)
                    nm = re.search(r'node\s*`([^`]+)`', raw_val)
                    if nm:
                        result['figma_node'] = nm.group(1)
                elif canonical != '_pipeline_info':
                    result[canonical] = raw_val
            else:
                # Check if it's a known but unmapped key
                if raw_key not in ('pass', 'gap', 'unverifiable',
                                   'simple score', 'weighted score',
                                   'total checks'):
                    _log_issue('meta_key_unknown', 'report_meta',
                               f'Key "{raw_key}" not in META_ALIASES',
                               line_num=i+1, raw_text=stripped)

        # ── Inline stats: **Total checks:** 45
        m = re.match(r'^\*\*Total checks:\*\*\s*(\d+)', meta_line, re.I)
        if m:
            result['_total_checks_inline'] = int(m.group(1))

        # Stop parsing after encountering --- or ## section headers
        if stripped == '---' and i > 3:
            break
        if stripped.startswith('## ') and i > 5:
            break

    result['_formats_detected'] = formats_detected
    return result


# ═══════════════════════════════════════════════════════════════════════
# PARSER: Score Block (Tổng quan table)
# ═══════════════════════════════════════════════════════════════════════

def parse_score_block(lines: list[str]) -> dict:
    """Parse overall score from Tổng quan / summary table.

    Looks for table with Pass/Gap/Unverifiable/Score rows.
    """
    result = {
        'total_checks': 0,
        'pass': 0,
        'gap': 0,
        'unverifiable': 0,
        'score': 0,
    }

    # Also try to parse inline stats above tables
    for i, line in enumerate(lines):
        stripped = line.strip()

        # Pattern: **Total checks:** 45
        m = re.match(r'\*\*Total checks:\*\*\s*(\d+)', stripped, re.I)
        if m:
            result['total_checks'] = int(m.group(1))

        m = re.match(r'\*\*Pass:\*\*\s*(\d+)', stripped, re.I)
        if m:
            result['pass'] = int(m.group(1))

        m = re.match(r'\*\*(?:Gap|Gaps?):\*\*\s*(\d+)', stripped, re.I)
        if m:
            result['gap'] = int(m.group(1))

        m = re.match(r'\*\*(?:Simple |Weighted )?Score:\*\*\s*(\d+)', stripped, re.I)
        if m:
            result['score'] = int(m.group(1))

    # Parse Tổng quan table: | Metric | Value |
    in_summary = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.search(r'##\s+Tổng quan', stripped, re.I):
            in_summary = True
            continue
        if in_summary and stripped.startswith('|'):
            # | Tổng check | 42 |
            m = re.match(r'\|\s*(.+?)\s*\|\s*(\d+)\s*\|', stripped)
            if m:
                key = m.group(1).strip().lower()
                val = int(m.group(2))
                if 'tổng' in key and 'check' in key:
                    result['total_checks'] = val
                elif key == 'pass':
                    result['pass'] = val
                elif key == 'gap':
                    result['gap'] = val
                elif 'unverifiable' in key:
                    result['unverifiable'] = val
                elif 'score' in key or 'ux score' in key:
                    result['score'] = val
        elif in_summary and stripped.startswith('#'):
            break
        elif in_summary and stripped == '---':
            # Continue — might have more
            pass

    # Derive score if not found
    if result['score'] == 0 and (result['pass'] + result['gap']) > 0:
        result['score'] = round(result['pass'] / (result['pass'] + result['gap']) * 100)

    return result


# ═══════════════════════════════════════════════════════════════════════
# PARSER: Screen Sections + Check Tables
# ═══════════════════════════════════════════════════════════════════════

def parse_screens_and_checks(lines: list[str]) -> list[dict]:
    """Parse screen sections with their check tables.

    Handles FMT-030 (inline SCR-ID) and FMT-031 (fallback SCR-ID).
    Handles FMT-020/021/022 (table header variants).
    """
    screens = []
    current_screen = None
    in_table = False
    column_map = {}
    header_format = ''

    for i, line in enumerate(lines):
        stripped = line.strip()

        # ── Screen heading detection ──
        # FMT-030: ### 1. Screen Name (`SCR-XXX-001`)
        m = re.match(r'^###\s+\d+\.\s+(.+?)\s*\(`?(SCR-\w+-\d+)`?\)', stripped)
        if m:
            if current_screen:
                screens.append(current_screen)
            current_screen = {
                'screen_name': m.group(1).strip(),
                'screen_id': m.group(2),
                'screen_type': '',
                'artboard_count': 0,
                'score': 0,
                'pass_count': 0,
                'gap_count': 0,
                'heading_format': 'FMT-030',
                'header_format': '',
                'column_map': {},
                'checks': [],
            }
            in_table = False
            continue

        # FMT-031: ### 1. Screen Name (no SCR-ID in heading)
        m = re.match(r'^###\s+\d+\.\s+(.+)$', stripped)
        if m and not stripped.startswith('### 🔴') and not stripped.startswith('### 🟡') and not stripped.startswith('### ⚪'):
            # Check if this is a screen heading (not a severity section)
            name_candidate = m.group(1).strip()
            if not any(kw in name_candidate.lower() for kw in ['critical', 'major', 'minor', 'đề xuất', 'methodology']):
                if current_screen:
                    screens.append(current_screen)
                current_screen = {
                    'screen_name': name_candidate,
                    'screen_id': '',
                    'screen_type': '',
                    'artboard_count': 0,
                    'score': 0,
                    'pass_count': 0,
                    'gap_count': 0,
                    'heading_format': 'FMT-031',
                    'header_format': '',
                    'column_map': {},
                    'checks': [],
                }
                in_table = False
                continue

        # ── Screen meta line (fallback SCR-ID + type) ──
        # > `SCR-DKV-001` · list · 2 artboards
        if current_screen and stripped.startswith('>'):
            meta_line = stripped.lstrip('>').strip()
            m = re.match(r'`(SCR-\w+-\d+)`\s*·\s*(\w+)\s*·\s*(\d+)\s*artboard', meta_line)
            if m:
                if not current_screen['screen_id']:
                    current_screen['screen_id'] = m.group(1)
                current_screen['screen_type'] = m.group(2)
                current_screen['artboard_count'] = int(m.group(3))
                continue

        # ── Per-screen score line ──
        # **Score: 50% | Pass: 4 | Gap: 2**
        if current_screen:
            m = re.match(r'\*\*Score:\s*(\d+)%\s*\|\s*Pass:\s*(\d+)\s*\|\s*Gap:\s*(\d+)\*\*', stripped)
            if m:
                current_screen['score'] = int(m.group(1))
                current_screen['pass_count'] = int(m.group(2))
                current_screen['gap_count'] = int(m.group(3))
                continue

        # ── Table header detection ──
        if current_screen and stripped.startswith('|') and '---' not in stripped:
            cols = [c.strip().lower() for c in stripped.split('|')[1:-1]]

            # Check if this is a header row (has known column names)
            if any(c in ('check', 'verdict', 'evidence') for c in cols):
                column_map = {}
                for idx, col in enumerate(cols):
                    canonical = COLUMN_ALIASES.get(col)
                    if canonical:
                        column_map[idx] = canonical
                    elif col:
                        _log_issue('column_unknown', 'check_table',
                                   f'Column "{col}" not in COLUMN_ALIASES',
                                   line_num=i+1, raw_text=stripped)

                # Detect header format
                col_set = set(cols)
                if 'category' in col_set and 'severity' in col_set:
                    header_format = 'FMT-020'
                elif 'category' in col_set and 'ddl ref' in col_set:
                    header_format = 'FMT-021'
                elif 'source' in col_set and 'ddl ref' in col_set:
                    header_format = 'FMT-022'
                else:
                    header_format = 'FMT-020-unknown'
                    _log_issue('header_unknown', 'check_table',
                               f'Header pattern not recognized: {cols}',
                               line_num=i+1, raw_text=stripped)

                current_screen['header_format'] = header_format
                current_screen['column_map'] = {str(k): v for k, v in column_map.items()}
                in_table = True
                continue

        # ── Table separator (skip) ──
        if stripped.startswith('|') and re.match(r'^\|[\s|:-]+\|$', stripped):
            continue

        # ── Table data rows ──
        if in_table and current_screen and stripped.startswith('|'):
            cols = [c.strip() for c in stripped.split('|')[1:-1]]
            if len(cols) >= 3:
                row = {}
                for idx, val in enumerate(cols):
                    key = column_map.get(idx)
                    if key:
                        if key == 'num':
                            try:
                                row[key] = int(val)
                            except ValueError:
                                row[key] = val
                        else:
                            row[key] = val

                # Validate row has minimum fields
                if 'verdict' in row and row.get('check'):
                    # Extract evidence image references
                    evidence = row.get('evidence', '')
                    img_refs = []
                    for pattern, fmt_id in EVIDENCE_IMG_PATTERNS:
                        m_img = re.search(pattern, evidence)
                        if m_img:
                            ref_entry = {'pattern': fmt_id}
                            if m_img.lastindex and m_img.lastindex >= 1:
                                ref_entry['filename'] = m_img.group(1)
                            img_refs.append(ref_entry)

                    # Extract artboard IDs from evidence (e.g., "Vision 7001:" or "7001/7003:")
                    artboard_ids = re.findall(r'\b(\d{4})\b', evidence)
                    if artboard_ids:
                        row['_evidence_artboard_ids'] = list(set(artboard_ids))

                    row['_evidence_img_refs'] = img_refs
                    current_screen['checks'].append(row)
            continue

        # ── End of table ──
        if in_table and not stripped.startswith('|') and stripped != '':
            if stripped != '---':
                in_table = False

        # ── Section break (## heading) ──
        if stripped.startswith('## ') and current_screen:
            section_name = stripped[3:].strip().lower()
            if any(kw in section_name for kw in ['đề xuất', 'proposal', 'methodology', 'phương pháp']):
                screens.append(current_screen)
                current_screen = None
                in_table = False

    # Don't forget last screen
    if current_screen:
        screens.append(current_screen)

    return screens


# ═══════════════════════════════════════════════════════════════════════
# PARSER: UXP Blocks
# ═══════════════════════════════════════════════════════════════════════

def parse_uxp_blocks(lines: list[str]) -> list[dict]:
    """Parse UXP proposal blocks from report markdown.

    Handles FMT-040 (with emoji) and FMT-041 (without emoji).
    UXP fields: FMT-050 (key-value table).
    """
    uxps = []
    current_uxp = None

    for i, line in enumerate(lines):
        stripped = line.strip()

        # ── UXP heading ──
        # FMT-040/041: #### UXP-001 · [🔴] Critical
        m = re.match(r'^####\s+(UXP-\d+)\s*·\s*(?:🔴\s*|🟡\s*|⚪\s*)?(Critical|Major|Minor)',
                      stripped, re.IGNORECASE)
        if m:
            if current_uxp:
                uxps.append(current_uxp)
            uxp_id = m.group(1)
            severity = m.group(2).capitalize()
            has_emoji = any(e in stripped for e in ('🔴', '🟡', '⚪'))

            current_uxp = {
                'id': uxp_id,
                'severity': severity,
                'heading_format': 'FMT-040' if has_emoji else 'FMT-041',
                'screen_tag': '',
                'screen_id': '',
                'fields': {},
            }
            continue

        # ── UXP field rows (FMT-050) ──
        # | **Màn hình** | Screen Name (SCR-ID) |
        if current_uxp:
            m = re.match(r'^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|', stripped)
            if m:
                key = m.group(1).strip()
                val = m.group(2).strip()
                current_uxp['fields'][key] = val

                # Extract screen_id from Màn hình field
                if key == 'Màn hình':
                    current_uxp['screen_tag'] = val
                    scr_match = re.search(r'(SCR-\w+-\d+)', val)
                    if scr_match:
                        current_uxp['screen_id'] = scr_match.group(1)
                continue

            # End of UXP block (next heading or ---)
            if stripped.startswith('#') or (stripped == '---' and current_uxp['fields']):
                uxps.append(current_uxp)
                current_uxp = None

    if current_uxp:
        uxps.append(current_uxp)

    return uxps


# ═══════════════════════════════════════════════════════════════════════
# PARSER: SCR-*.md Screen Specs
# ═══════════════════════════════════════════════════════════════════════

def parse_scr_md_files(module_dir: Path) -> list[dict]:
    """Parse SCR-*.md screen spec files for image references."""
    results = []

    for md_file in sorted(module_dir.glob('SCR-*.md')):
        entry = {
            'filename': md_file.name,
            'screen_id': '',
            'images': [],
        }

        lines = _read_lines(md_file)
        for line in lines:
            stripped = line.strip()

            # Extract screen ID
            m = re.match(r'\*\*Screen ID:\*\*\s*(SCR-\w+-\d+)', stripped)
            if m:
                entry['screen_id'] = m.group(1)

            # Extract wireframe images: ![Alt text](ui/filename.png)
            m = re.match(r'!\[(.+?)\]\((.+?)\)', stripped)
            if m:
                alt = m.group(1)
                path = m.group(2)
                filename = path.split('/')[-1] if '/' in path else path
                entry['images'].append({
                    'alt': alt,
                    'path': path,
                    'filename': filename,
                })

        results.append(entry)

    return results


# ═══════════════════════════════════════════════════════════════════════
# PARSER: Handoff Data
# ═══════════════════════════════════════════════════════════════════════

def parse_handoff(module_dir: Path) -> dict:
    """Parse handoff directory: manifest, inventory, flow_graph."""
    handoff_dir = module_dir / 'handoff'
    result = {
        'manifest': {},
        'inventory_screens': [],
        'flow_edges': [],
        'overlay_events': [],
    }

    # ── Manifest ──
    manifest = _read_json(handoff_dir / 'handoff-manifest.json')
    if manifest:
        # Normalize key aliases
        normalized = {}
        for key, val in manifest.items():
            canonical = MANIFEST_ALIASES.get(key, key)
            normalized[canonical] = val
        result['manifest'] = normalized

    # ── Screen Inventory ──
    inv = _read_json(handoff_dir / 'screen_inventory.json')
    if inv:
        raw_screens = inv.get('screens', inv if isinstance(inv, list) else [])
        if isinstance(inv, dict) and 'screens' in inv:
            raw_screens = inv['screens']
        elif isinstance(inv, list):
            raw_screens = inv

        for scr in raw_screens:
            entry = {
                'screen_id': scr.get('screen_id', scr.get('id', '')),
                'screen_name': scr.get('display_name_vi', scr.get('screen_name_vi',
                               scr.get('screen_name', ''))),
                'screen_type': scr.get('screen_type', ''),
                'wireframe_images': scr.get('wireframe_images', []),
                'artboard_node_ids': scr.get('artboard_node_ids', []),
            }
            result['inventory_screens'].append(entry)

    # ── Flow Graph ──
    flow = _read_json(handoff_dir / 'flow_graph.json')
    if flow:
        result['flow_edges'] = flow.get('edges', [])
        result['overlay_events'] = flow.get('overlay_events', [])

    return result


# ═══════════════════════════════════════════════════════════════════════
# IMAGE MAP BUILDER
# ═══════════════════════════════════════════════════════════════════════

def build_image_map(module_dir: Path, screens: list[dict],
                    check_tables: list[dict],
                    inventory_screens: list[dict],
                    scr_md_data: list[dict]) -> dict:
    """Build comprehensive image map from all sources."""
    ui_dir = module_dir / 'ui'

    result = {
        'disk_files': [],
        'inventory_images': [],
        'scr_md_images': [],
        'evidence_refs': [],
        'artboard_index': [],
        'orphan_images': [],
        'missing_images': [],
    }

    # 1. Disk files
    if ui_dir.exists():
        result['disk_files'] = sorted(
            f.name for f in ui_dir.iterdir()
            if f.suffix.lower() in ('.png', '.jpg', '.jpeg', '.webp')
            and not f.name.startswith('.')
        )

    disk_set = set(result['disk_files'])

    # 2. Inventory images
    referenced = set()
    for scr in inventory_screens:
        for img in scr.get('wireframe_images', []):
            fn = img.get('filename', '')
            if fn:
                result['inventory_images'].append({
                    'screen_id': scr['screen_id'],
                    'filename': fn,
                    'role': img.get('role', 'base'),
                })
                referenced.add(fn)

    # 3. SCR-*.md images
    for scr_md in scr_md_data:
        for img in scr_md.get('images', []):
            fn = img.get('filename', '')
            if fn:
                result['scr_md_images'].append({
                    'screen_id': scr_md['screen_id'],
                    'alt': img.get('alt', ''),
                    'filename': fn,
                })
                referenced.add(fn)

    # 4. Evidence refs from check tables
    for screen_data in check_tables:
        for check in screen_data.get('checks', []):
            for ref in check.get('_evidence_img_refs', []):
                fn = ref.get('filename', '')
                entry = {
                    'check_num': check.get('num', 0),
                    'screen_id': screen_data.get('screen_id', ''),
                    'image_ref': fn if fn else None,
                    'pattern': ref.get('pattern', ''),
                }
                result['evidence_refs'].append(entry)
                if fn:
                    referenced.add(fn)

    # 5. Artboard index
    ai_path = module_dir / 'artboard-index.json'
    ai_data = _read_json(ai_path)
    if ai_data:
        result['artboard_index'] = ai_data if isinstance(ai_data, list) else []

    # 6. Orphan images (on disk, not referenced)
    result['orphan_images'] = sorted(disk_set - referenced)

    # 7. Missing images (referenced, not on disk)
    result['missing_images'] = sorted(referenced - disk_set)

    return result


# ═══════════════════════════════════════════════════════════════════════
# MAIN: Assemble module-index.json
# ═══════════════════════════════════════════════════════════════════════

def index_module(module_dir: Path) -> dict:
    """Index a single module → canonical module-index.json."""
    global _issues
    _issues = []

    module_dir = module_dir.resolve()
    report_path = module_dir / 'ux-review-report.md'

    if not report_path.exists():
        print(f'❌ {module_dir.name}: ux-review-report.md not found', file=sys.stderr)
        return {}

    lines = _read_lines(report_path)

    # ── Parse all sources ──
    report_meta = parse_report_meta(lines)
    score_block = parse_score_block(lines)
    screen_checks = parse_screens_and_checks(lines)
    uxp_blocks = parse_uxp_blocks(lines)
    scr_md_data = parse_scr_md_files(module_dir)
    handoff = parse_handoff(module_dir)

    # ── Resolve UXP screen_id from screen_tag vs screen names ──
    # When Màn hình field has no SCR-ID, fuzzy match against screen names
    for uxp in uxp_blocks:
        if uxp['screen_id']:
            continue  # Already has SCR-ID from regex
        tag = uxp.get('screen_tag', '').lower()
        if not tag:
            continue

        best_match = ''
        best_score = 0
        for scr in screen_checks:
            name = scr.get('screen_name', '').lower()
            # Count word overlap
            tag_words = set(re.findall(r'\w+', tag))
            name_words = set(re.findall(r'\w+', name))
            overlap = len(tag_words & name_words)
            if overlap > best_score:
                best_score = overlap
                best_match = scr.get('screen_id', '')

        if best_match and best_score >= 2:
            uxp['screen_id'] = best_match
        elif screen_checks:
            # Fallback: if only 1-2 screens, assign first screen
            _log_issue('uxp_screen_unresolved', f'UXP {uxp["id"]}',
                       f'screen_tag="{uxp["screen_tag"]}" could not be matched '
                       f'to any parsed screen (best_score={best_score})')

    # ── Merge screen data from inventory ──
    inv_map = {s['screen_id']: s for s in handoff['inventory_screens']}
    for screen in screen_checks:
        sid = screen.get('screen_id', '')
        inv = inv_map.get(sid, {})
        if not screen['screen_type'] and inv:
            screen['screen_type'] = inv.get('screen_type', '')
        if not screen['artboard_count'] and inv:
            screen['artboard_count'] = len(inv.get('wireframe_images', []))

    # ── Build image map ──
    image_map = build_image_map(
        module_dir, screen_checks, screen_checks,
        handoff['inventory_screens'], scr_md_data
    )

    # ── Derive section from folder path ──
    if not report_meta['section']:
        parent = module_dir.parent.name
        if parent not in ('final', 'COOPBANK'):
            report_meta['section'] = parent

    # ── Build format fingerprint ──
    all_formats = list(report_meta.get('_formats_detected', []))
    for s in screen_checks:
        hf = s.get('header_format', '')
        if hf and hf not in all_formats:
            all_formats.append(hf)
        sf = s.get('heading_format', '')
        if sf and sf not in all_formats:
            all_formats.append(sf)
    for u in uxp_blocks:
        uf = u.get('heading_format', '')
        if uf and uf not in all_formats:
            all_formats.append(uf)

    # ── Source files list ──
    source_files = ['ux-review-report.md']
    for f in ['handoff/screen_inventory.json', 'handoff/flow_graph.json',
              'handoff/handoff-manifest.json', 'handoff/ddl-context.json']:
        if (module_dir / f).exists():
            source_files.append(f)
    for md in module_dir.glob('SCR-*.md'):
        source_files.append(md.name)
    if (module_dir / 'artboard-index.json').exists():
        source_files.append('artboard-index.json')

    tz = timezone(timedelta(hours=7))

    # ── Assemble ──
    index = {
        '_meta': {
            'indexed_at': datetime.now(tz).strftime('%Y-%m-%dT%H:%M:%S%z'),
            'source_files': source_files,
            'format_fingerprint': '+'.join(all_formats),
            'module_dir': str(module_dir),
            'issues': _issues,
            'issue_count': len(_issues),
        },
        'report_meta': {k: v for k, v in report_meta.items()
                        if not k.startswith('_')},
        'score_block': score_block,
        'screens': [
            {
                'screen_id': s['screen_id'],
                'screen_name': s['screen_name'],
                'screen_type': s['screen_type'],
                'artboard_count': s['artboard_count'],
                'score': s['score'],
                'pass_count': s['pass_count'],
                'gap_count': s['gap_count'],
                'heading_format': s['heading_format'],
                'header_format': s['header_format'],
                'column_map': s['column_map'],
                'check_count': len(s['checks']),
                'checks': s['checks'],
            }
            for s in screen_checks
        ],
        'uxp_blocks': uxp_blocks,
        'scr_md_data': scr_md_data,
        'handoff': {
            'manifest': handoff['manifest'],
            'inventory_screens': handoff['inventory_screens'],
            'flow_edges': handoff['flow_edges'],
            'overlay_events': handoff['overlay_events'],
        },
        'image_map': image_map,
    }

    return index


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='Per-module deep indexer → module-index.json'
    )
    parser.add_argument('--module', type=Path, required=True,
                        help='Path to module directory')
    parser.add_argument('--dry', action='store_true',
                        help='Print to stdout instead of writing file')
    parser.add_argument('--output', type=Path, default=None,
                        help='Output path (default: module/module-index.json)')
    args = parser.parse_args()

    module_dir = args.module.resolve()
    if not module_dir.is_dir():
        print(f'❌ Not a directory: {module_dir}', file=sys.stderr)
        sys.exit(1)

    # Run indexer
    index = index_module(module_dir)
    if not index:
        sys.exit(1)

    output_json = json.dumps(index, ensure_ascii=False, indent=2)

    if args.dry:
        print(output_json)
    else:
        out_path = args.output or (module_dir / 'module-index.json')
        out_path.write_text(output_json, encoding='utf-8')

        # Print summary
        meta = index['_meta']
        n_screens = len(index['screens'])
        n_checks = sum(s['check_count'] for s in index['screens'])
        n_uxps = len(index['uxp_blocks'])
        n_issues = meta['issue_count']
        disk_imgs = len(index['image_map']['disk_files'])
        orphans = len(index['image_map']['orphan_images'])
        missing = len(index['image_map']['missing_images'])

        print(f'✅ Indexed: {module_dir.name}', file=sys.stderr)
        print(f'   Formats: {meta["format_fingerprint"]}', file=sys.stderr)
        print(f'   Sources: {len(meta["source_files"])} files', file=sys.stderr)
        print(f'   Screens: {n_screens} | Checks: {n_checks} | UXPs: {n_uxps}', file=sys.stderr)
        print(f'   Images: {disk_imgs} disk | {orphans} orphan | {missing} missing', file=sys.stderr)
        if n_issues:
            print(f'   ⚠️  Issues: {n_issues} (self-learning needed)', file=sys.stderr)
            for iss in meta['issues']:
                print(f'      → [{iss["trigger"]}] {iss["detail"]}', file=sys.stderr)
        print(f'   Output: {out_path}', file=sys.stderr)


if __name__ == '__main__':
    main()
