#!/usr/bin/env python3
"""
fix_images.py — Post-generation image mapping repair tool.

7-strategy resolution chain for correcting image references in pitch-deck HTML:
 S1. Gap ref → Check # → image in check table
 S2. Direct .png in proposal text
 S3. Screen section "Images:" header
 S4. Artboard ID in UXP text → check table "Từ ảnh NNNN" → filename
 S5. Screen section → first gap check image
 S6. UXP screen → screen section → image list
 S7. Screen name fuzzy → filename
 S8. Proportional distribution (last resort)

Usage:
  python3 fix_images.py audit --base /path/to/project
  python3 fix_images.py fix --base /path/to/project [--dry]
"""
import re, sys, os, argparse
from typing import Any
from pathlib import Path


def find_pitch_decks(base: Path):
    results = []
    for root, dirs, files in os.walk(base):
        for f in files:
            if 'pitch-deck' in f and f.endswith('.html'):
                results.append(Path(root) / f)
    return sorted(results)


def parse_report_full(report_path, available_imgs):
    """
    Full parse of ux-review-report.md returning:
    - check_to_img: {check_num: actual_filename}
    - artboard_to_img: {artboard_id: actual_filename}
    - screen_sections: [{title, images, checks}]
    - uxp_proposals: [{id, screen, gap_refs, text_body, evidence_imgs}]
    """
    text = report_path.read_text(encoding='utf-8')
    lines = text.split('\n')

    check_to_img = {}
    artboard_to_img = {}
    screen_sections = []
    uxp_proposals = []

    current_screen: dict[str, Any] | None = None
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # ── Screen section headers ──
        scr_m = re.match(r'^###\s+\d+\.\s+(.+?)(?:\s*\(`?(SCR-[\w-]+)`?\))?\s*$', stripped)
        if scr_m:
            screen_title = scr_m.group(1).strip()
            current_screen: dict[str, Any] = {  # type: ignore[annotation-unchecked]
                'title': screen_title,
                'id': scr_m.group(2) or '',
                'images': [],
                'checks': [],
                'gap_checks': [],
            }
            screen_sections.append(current_screen)
            i += 1
            lookahead = i
            while lookahead < min(i + 5, len(lines)):
                peek = lines[lookahead].strip()  # type: ignore[index]
                if peek == '':
                    lookahead += 1  # type: ignore[operator]
                    continue
                if peek.startswith('>'):
                    scr_id_m = re.search(r'`(SCR-[\w-]+)`', peek)
                    if scr_id_m:
                        current_screen['id'] = scr_id_m.group(1)
                break
            continue

        # ── Screen metadata rows (Wireframes, Images, Artboards) ──
        if current_screen and ('Images:' in stripped or '**Wireframes**' in stripped or '**Artboards**' in stripped):
            imgs = re.findall(r'([\w.-]+\.png)', stripped)
            current_screen['images'].extend(imgs)  # type: ignore[index]
            if '**Artboards**' in stripped:
                artboard_nums = re.findall(r'(\d{3,5})', stripped)
                for anum in artboard_nums:
                    for wimg in current_screen['images']:  # type: ignore[index]
                        if wimg.startswith(anum + '-') or wimg.startswith(anum + '_'):
                            artboard_to_img[anum] = wimg
                            break
            i += 1
            continue

        # ── Check table rows ──
        check_m = re.match(r'^\|\s*(\d+)\s*\|(.+)', stripped)
        if check_m:
            check_num = int(check_m.group(1))
            rest = check_m.group(2)
            is_gap = '❌' in rest or 'Gap' in rest

            direct_imgs = re.findall(r'([\w.-]+\.png)', rest)
            artboard_refs = re.findall(r'Từ ảnh[:\s]*?(\d{3,5})', rest)

            best_img = None
            if direct_imgs:
                for dimg in direct_imgs:
                    if dimg in available_imgs:
                        best_img = dimg
                        break
                if not best_img:
                    for dimg in direct_imgs:
                        prefix = dimg.replace('.png', '')
                        for aimg in available_imgs:
                            if aimg.startswith(prefix):
                                best_img = aimg
                                break
                        if best_img:
                            break

            if not best_img and artboard_refs:
                for aid in artboard_refs:
                    for aimg in sorted(available_imgs):
                        if aimg.startswith(aid + '-') or aimg.startswith(aid + '_') or aimg.replace('.png', '') == aid:
                            best_img = aimg
                            artboard_to_img[aid] = aimg
                            break
                    if best_img:
                        break

            more_artboard = re.findall(r'Từ ảnh[:\s]*(\d{3,5})', rest)
            for aid in more_artboard:
                if aid not in artboard_to_img:
                    for aimg in sorted(available_imgs):
                        if aimg.startswith(aid + '-') or aimg.startswith(aid + '_') or aimg.replace('.png', '') == aid:
                            artboard_to_img[aid] = aimg
                            break

            if best_img:
                check_to_img[check_num] = best_img
                if current_screen:
                    current_screen['checks'].append({'num': check_num, 'img': best_img, 'gap': is_gap})  # type: ignore[index]
                    if is_gap:
                        current_screen['gap_checks'].append({'num': check_num, 'img': best_img})  # type: ignore[index]

            for aid in artboard_refs:
                if aid not in artboard_to_img and best_img:
                    artboard_to_img[aid] = best_img

            i += 1
            continue

        # ── UXP proposals (Format A/B) ──
        pm = re.match(r'^####\s+(UXP-[\w-]+)\s*·\s*(.+)', stripped)
        if pm:
            prop: dict[str, Any] = {
                'id': pm.group(1),
                'severity': pm.group(2).strip().lower(),
                'screen': '',
                'gap_refs': [],
                'text_body': '',
                'evidence_imgs': [],
            }
            i += 1
            while i < len(lines) and (lines[i].strip() == '' or re.match(r'^\|[-\s|]+\|$', lines[i].strip()) or lines[i].strip() == '| | |'):  # type: ignore[index]
                i += 1
            while i < len(lines) and lines[i].strip().startswith('|'):  # type: ignore[index]
                row = lines[i]  # type: ignore[index]
                if '**Màn hình**' in row or '**Man hinh**' in row:
                    split_key = '**Màn hình**' if '**Màn hình**' in row else '**Man hinh**'
                    m2 = re.search(r'\|\s*(.+?)\s*\|\s*$', row.split(split_key)[1])
                    if m2:
                        prop['screen'] = m2.group(1).strip().strip('|').strip()
                elif '**Gap ref**' in row:
                    m2 = re.search(r'\|\s*(.+?)\s*\|\s*$', row.split('**Gap ref**')[1])
                    if m2:
                        prop['gap_refs'] = [int(x) for x in re.findall(r'#(\d+)', m2.group(1))]
                prop['text_body'] += row + '\n'
                imgs = re.findall(r'([\w.-]+\.png)', row)
                prop['evidence_imgs'].extend(imgs)
                i += 1

            while i < len(lines):
                bline = lines[i].strip()  # type: ignore[index]
                if bline.startswith('#### UXP-') or (bline == '---' and i + 1 < len(lines) and re.match(r'^####\s+UXP-', lines[i + 1].strip())):  # type: ignore[index]
                    break
                sev_headers = ['### Critical', '### Major', '### Minor', '### 🔴', '### 🟡', '### ⚪']
                if bline.startswith('## ') or (bline.startswith('### ') and not any(bline.startswith(sh) for sh in sev_headers)):
                    break
                prop['text_body'] += bline + '\n'
                imgs = re.findall(r'([\w.-]+\.png)', bline)
                prop['evidence_imgs'].extend(imgs)
                if bline == '---':
                    i += 1
                    continue
                i += 1
            uxp_proposals.append(prop)
            continue

        # ── Format C: - **[UXP-NNN]** Screen: `SCR-XXX` | **Title** ──
        bm = re.match(r'^-\s*\*\*\[(UXP-[\w-]+)\]\*\*\s*Screen:\s*`?([\w-]+)`?\s*\|\s*\*\*(.+?)\*\*', stripped)
        if bm:
            desc = stripped
            imgs = re.findall(r'([\w.-]+\.png)', desc)
            uxp_proposals.append({
                'id': bm.group(1),
                'severity': 'minor',
                'screen': bm.group(2),
                'gap_refs': [],
                'text_body': desc,
                'evidence_imgs': imgs,
            })
            i += 1
            continue

        i += 1

    return check_to_img, artboard_to_img, screen_sections, uxp_proposals


def extract_artboard_ids(text):
    """Extract ALL artboard ID numbers from UXP text."""
    ids = []
    ids.extend(re.findall(r'\((\d{3,5})\)', text))
    ids.extend(re.findall(r'(?:artboard|overlay|popup|bottom.?sheet|screen|màn|form|SCR)[\s\-:]*(\d{3,5})', text, re.IGNORECASE))
    ids.extend(re.findall(r'(?:^|\|\s*)(\d{4,5})\s', text, re.MULTILINE))
    ids.extend(re.findall(r'(?:^|\s)(\d{3,5})[-–]', text))
    ids.extend(re.findall(r'ảnh\s+(\d{3,5})', text))
    ids.extend(re.findall(r'case.?loi.?(\d+)', text, re.IGNORECASE))
    seen = set()
    return [x for x in ids if not (x in seen or seen.add(x))]


def match_screen_to_section(screen_text, screen_sections):
    if not screen_text or not screen_sections:
        return None
    screen_lower = screen_text.lower().strip()

    if screen_text.startswith('SCR-'):
        for sec in screen_sections:
            if sec.get('id', '') == screen_text:
                return sec

    for sec in screen_sections:
        if sec['title'].lower() in screen_lower or screen_lower in sec['title'].lower():
            return sec

    parts = re.split(r'[›/]', screen_text)
    key_part = parts[-1].strip().lower() if parts else screen_lower
    for sec in screen_sections:
        sec_parts = re.split(r'[›/]', sec['title'])
        sec_key = sec_parts[-1].strip().lower() if sec_parts else sec['title'].lower()
        if key_part in sec_key or sec_key in key_part:  # type: ignore[operator]
            return sec

    key_words = set(re.findall(r'\w{3,}', screen_lower))
    best_match = None
    best_overlap = 0
    for sec in screen_sections:
        sec_words = set(re.findall(r'\w{3,}', sec['title'].lower()))
        overlap = len(key_words & sec_words)
        if overlap > best_overlap:
            best_overlap = overlap
            best_match = sec
    return best_match if best_overlap >= 2 else None


def resolve_best_image(prop, check_to_img, artboard_to_img, screen_sections, available_imgs):
    """Multi-strategy resolution with artboard ID support."""

    # S1: Gap ref → check_to_img
    for check_num in prop['gap_refs']:  # type: ignore[index]
        if check_num in check_to_img:
            img = check_to_img[check_num]
            if img in available_imgs:
                return img, f'S1:check#{check_num}'

    # S2: Direct .png in proposal
    for img in prop['evidence_imgs']:
        if img in available_imgs:
            return img, 'S2:direct'

    # S4: Artboard ID in text
    artboard_ids = extract_artboard_ids(prop['text_body'])
    if artboard_ids:
        for aid in artboard_ids:
            if aid in artboard_to_img and artboard_to_img[aid] in available_imgs:
                return artboard_to_img[aid], f'S4:artboard({aid})'
            for img in sorted(available_imgs):
                img_base = img.replace('.png', '')
                if img_base.startswith(aid + '-') or img_base.startswith(aid + '_') or img_base == aid:  # type: ignore[operator]
                    return img, f'S4:prefix({aid})'

    # S3: Screen section Images header
    matched_section = match_screen_to_section(prop['screen'], screen_sections)
    if matched_section and matched_section['images']:
        for img in matched_section['images']:
            if img in available_imgs:
                return img, f'S3:screen-hdr'

    # S5: Screen → check table → first gap/check image
    if matched_section:
        if matched_section['gap_checks']:
            img = matched_section['gap_checks'][0]['img']
            if img in available_imgs:
                return img, 'S5:gap-check'
        if matched_section['checks']:
            img = matched_section['checks'][0]['img']
            if img in available_imgs:
                return img, 'S5:first-check'

    # S6: screen check images
    if matched_section:
        all_screen_imgs = set()
        for c in matched_section['checks']:
            all_screen_imgs.add(c['img'])
        for img in sorted(all_screen_imgs):
            if img in available_imgs:
                return img, 'S6:screen-check'

    # S8: Proportional distribution
    if matched_section and available_imgs:
        sec_idx = next((i for i, s in enumerate(screen_sections) if s is matched_section), -1)
        if sec_idx >= 0 and len(screen_sections) > 0:
            sorted_imgs = sorted(available_imgs)
            n_imgs = len(sorted_imgs)
            n_secs = len(screen_sections)
            start_idx = (sec_idx * n_imgs) // n_secs
            if start_idx < n_imgs:
                img = sorted_imgs[min(start_idx, n_imgs - 1)]
                return img, f'S8:proportional(sec{sec_idx + 1}/{n_secs})'

    # S7: Screen name fuzzy
    screen_text = prop.get('screen', '').lower()
    screen_words = [w for w in re.split(r'[\s›/]+', screen_text) if len(w) > 2]
    if screen_words:
        best_match_img = None
        best_score = 0
        for img in sorted(available_imgs):
            img_base = img.replace('.png', '').replace('-', ' ').replace('_', ' ').lower()
            matches = sum(1 for w in screen_words if w in img_base)
            if matches > best_score:
                best_score = matches
                best_match_img = img
        if best_score >= 2 or (best_score >= 1 and len(screen_words) <= 2):
            return best_match_img, 'S7:fuzzy'

    return None, 'UNRESOLVED'


def resolve_gap_image(check_title: str, gap_num: int, check_to_img: dict,
                      screen_sections: list, available_imgs: set, screen_id: str = '') -> tuple:
    """Resolve best image for a specific gap card based on check context.

    Returns (best_img, source_strategy) or (None, 'UNRESOLVED').
    """
    check_lower = check_title.lower()

    # Strategy G1: gap_num matches check_num in check_to_img
    if gap_num in check_to_img:
        img = check_to_img[gap_num]
        if img in available_imgs:
            return img, f'G1:check#{gap_num}'

    # Strategy G2: keyword match in check_to_img evidence
    keywords = [w for w in re.split(r'[\s:_\-]+', check_lower) if len(w) >= 4]
    for cnum, cimg in check_to_img.items():
        if isinstance(cimg, str) and cimg in available_imgs:
            # check if check_num text matches keywords
            for kw in keywords:
                if kw in str(cnum).lower():
                    return cimg, f'G2:keyword({kw})'

    # Strategy G3: screen section → gap_checks specific to this gap's screen
    if screen_id:
        for sec in screen_sections:
            if sec.get('id') == screen_id:
                # Find gap-specific check images
                if sec.get('gap_checks'):
                    # Try to find variation — don't always pick first
                    gap_check_imgs = [gc['img'] for gc in sec['gap_checks'] if gc['img'] in available_imgs]
                    if gap_check_imgs:
                        # Distribute among gap checks — use gap_num as offset
                        idx = (gap_num - 1) % len(gap_check_imgs)
                        return gap_check_imgs[idx], f'G3:gap-check(idx={idx})'
                # Fallback to any screen check images
                if sec.get('checks'):
                    check_imgs = list({c['img'] for c in sec['checks'] if c['img'] in available_imgs})
                    if check_imgs:
                        idx = (gap_num - 1) % len(check_imgs)
                        return sorted(check_imgs)[idx], f'G3:screen-check(idx={idx})'
                if sec.get('images'):
                    for img in sec['images']:
                        if img in available_imgs:
                            return img, 'G3:screen-hdr'
                break

    # Strategy G4: fuzzy match check_title keywords → available image filenames
    if keywords:
        best_match_img = None
        best_score = 0
        for img in sorted(available_imgs):
            img_base = img.replace('.png', '').replace('-', ' ').replace('_', ' ').lower()
            matches = sum(1 for kw in keywords if kw in img_base)
            if matches > best_score:
                best_score = matches
                best_match_img = img
        if best_score >= 2:
            return best_match_img, f'G4:fuzzy(score={best_score})'

    return None, 'UNRESOLVED'


def get_current_images(html_path):
    html = html_path.read_text(encoding='utf-8')
    result: dict[str, Any] = {}
    for card_match in re.finditer(r'<div class="finding-card[^"]*">[\s\S]*?(?=<div class="finding-card|</section>)', html):
        card_html = card_match.group(0)
        img_m = re.search(r'<img src="([^"]*)"', card_html)
        id_m = re.search(r'<span class="card-id">(UXP-[\w-]+)</span>', card_html)
        if img_m and id_m:
            result[id_m.group(1)] = img_m.group(1)
    return result


def get_gap_citations(html_path):
    """Extract current image citations from gap-cards.

    Two-pass approach:
    1. Find all screen group headers (gap-screen spans) and their positions
    2. Find gap-card divs and assign screen_id from nearest preceding header

    Returns: list of dicts with gap_num, current_imgs, screen_id, check_title.
    """
    html = html_path.read_text(encoding='utf-8')
    gap_cards: list[dict[str, Any]] = []

    # Pass 1: Find screen group headers and their positions
    screen_positions: list[tuple[int, str]] = []  # (position, SCR-ID)
    for sm in re.finditer(r'<span class="gap-screen">(SCR-[\w-]+)</span>', html):
        screen_positions.append((sm.start(), sm.group(1)))

    def find_screen_id(pos: int) -> str:
        """Find the nearest preceding screen_id for a given position."""
        result = ''
        for sp, sid in screen_positions:
            if sp < pos:
                result = sid
            else:
                break
        return result

    # Pass 2: Find gap-card divs
    for card_match in re.finditer(r'<div class="gap-card[\s\S]*?</div>\s*</div>\s*</div>', html):
        card_html = card_match.group(0)
        # Extract gap number
        num_m = re.search(r'<span class="gap-num">(\d+)</span>', card_html)
        if not num_m:
            continue
        gap_num = int(num_m.group(1))
        # Extract check title
        title_m = re.search(r'font-size:13\.5px">(.*?)</strong>', card_html)
        check_title = title_m.group(1) if title_m else ''
        # Extract current image citation (📸 badge in evidence section)
        citation_m = re.search(r'📸\s*([\w,-]+\.png(?:,\s*[\w,-]+\.png)*)', card_html)
        current_imgs = citation_m.group(1).split(',') if citation_m else []
        current_imgs = [img.strip() for img in current_imgs]
        # Get screen_id from parent context (pass 1 lookup)
        screen_id = find_screen_id(card_match.start())
        # Extract impact text
        impact_m = re.search(r'Tác động đến người dùng</div>\s*<div[^>]*>([^<]+)', card_html)
        impact_text = impact_m.group(1).strip() if impact_m else ''

        gap_cards.append({
            'num': gap_num,
            'check_title': check_title,
            'current_imgs': current_imgs,
            'screen_id': screen_id,
            'impact_text': impact_text,
            'start': card_match.start(),
            'end': card_match.end(),
        })

    return gap_cards


def fix_gap_citations(html: str, gap_cards: list, check_to_img: dict,
                      screen_sections: list, available_imgs: set) -> tuple:
    """Fix image citations in gap cards to be evidence-specific.

    Returns (fixed_html, list_of_changes).
    """
    changes: list[dict[str, Any]] = []
    # Process in reverse order to preserve positions
    for gap in reversed(gap_cards):
        best_img, source = resolve_gap_image(
            gap['check_title'], gap['num'], check_to_img,
            screen_sections, available_imgs, gap.get('screen_id', ''))

        if not best_img:
            continue

        current_str = ', '.join(gap['current_imgs']) if gap['current_imgs'] else ''
        if best_img == current_str:
            continue  # Already correct

        # Find and replace the 📸 citation in this card's HTML region
        card_html = html[gap['start']:gap['end']]
        citation_pattern = r'(📸\s*)([\w,-]+\.png(?:,\s*[\w,-]+\.png)*)'
        citation_m = re.search(citation_pattern, card_html)

        if citation_m:
            old_citation = citation_m.group(2)
            new_card_html = card_html[:citation_m.start(2)] + best_img + card_html[citation_m.end(2):]
            html = html[:gap['start']] + new_card_html + html[gap['end']:]
            changes.append({
                'gap_num': gap['num'],
                'old': old_citation,
                'new': best_img,
                'source': source,
            })

    return html, changes


def deduplicate_gap_impacts(html: str) -> tuple:
    """Detect and annotate duplicate gap impact texts.

    Returns (fixed_html, list_of_duplicates_found).
    Note: This doesn't rewrite impact text (that's enrich.py's job),
    but adds HTML comments for auditing.
    """
    # Find all impact texts in gap cards
    impact_pattern = r'(Tác động đến người dùng</div>\s*<div[^>]*>)([^<]+)'
    impacts: list[tuple[int, int, str]] = []
    for m in re.finditer(impact_pattern, html):
        text = m.group(2).strip()
        impacts.append((m.start(2), m.end(2), text))

    # Find duplicates
    seen: dict[str, list[int]] = {}
    for idx, (start, end, text) in enumerate(impacts):
        seen.setdefault(text, []).append(idx)

    duplicates = {text: indices for text, indices in seen.items() if len(indices) > 1}

    if not duplicates:
        return html, []

    # Add HTML comments to flag duplicates (non-destructive)
    dup_list: list[dict[str, Any]] = []
    for text, indices in duplicates.items():
        dup_list.append({
            'text_preview': text[:80],
            'count': len(indices),
            'gap_positions': indices,
        })

    return html, dup_list


def apply_fix(html_path, fixes, dry_run=False):
    html = html_path.read_text(encoding='utf-8')
    changed = False

    for uxp_id, (old_src, new_src) in fixes.items():
        if old_src == new_src:
            continue
        id_pos = html.find(f'>{uxp_id}<')  # type: ignore[attr-defined]
        if id_pos < 0:
            continue
        card_start = html.rfind('<div class="finding-card', 0, id_pos)  # type: ignore[attr-defined]
        if card_start < 0:
            continue
        card_block = html[card_start:id_pos]  # type: ignore[index]
        img_match = re.search(r'<img src="([^"]*)"', card_block)
        if not img_match:
            continue
        abs_start = card_start + img_match.start()
        abs_end = card_start + img_match.end()
        old_tag = img_match.group(0)
        new_tag = old_tag.replace(img_match.group(1), new_src)
        html = html[:abs_start] + new_tag + html[abs_end:]  # type: ignore[operator]
        changed = True

    if changed and not dry_run:
        html_path.write_text(html, encoding='utf-8')
    return changed


def process_one(html_path, mode='audit'):
    folder = html_path.parent
    report = folder / 'ux-review-report.md'
    if not report.exists():
        return None

    ui_dir = folder / 'ui'
    available_imgs = set()
    if ui_dir.exists():
        available_imgs = {f.name for f in ui_dir.iterdir() if f.suffix == '.png'}

    check_to_img, artboard_to_img, screen_sections, uxp_proposals = parse_report_full(report, available_imgs)
    current_map = get_current_images(html_path)

    if not uxp_proposals:
        return None

    fixes = {}
    issues = []
    correct = 0

    for prop in uxp_proposals:
        uxp_id = prop['id']
        best_img, source = resolve_best_image(prop, check_to_img, artboard_to_img, screen_sections, available_imgs)

        current_src = current_map.get(uxp_id, '')
        current_img = current_src.replace('ui/', '') if current_src else ''

        if best_img and current_img != best_img:
            fixes[uxp_id] = (current_src, f'ui/{best_img}')
            issues.append({
                'id': uxp_id,
                'current': current_img,
                'correct': best_img,
                'source': source,
            })
        elif best_img and current_img == best_img:
            correct += 1
        elif best_img is None:
            issues.append({
                'id': uxp_id,
                'current': current_img,
                'correct': '???',
                'source': source,
            })

    # ── Gap card analysis ──
    gap_cards = get_gap_citations(html_path)
    gap_issues: list[dict[str, Any]] = []
    gap_fixes_count = 0
    gap_correct_count = 0

    for gap in gap_cards:
        best_img, source = resolve_gap_image(
            gap['check_title'], gap['num'], check_to_img,
            screen_sections, available_imgs, gap.get('screen_id', ''))

        current_str = ', '.join(gap['current_imgs']) if gap['current_imgs'] else ''

        if best_img and best_img != current_str:
            gap_issues.append({
                'gap_num': gap['num'],
                'current': current_str or '(none)',
                'correct': best_img,
                'source': source,
            })
            gap_fixes_count += 1
        elif best_img and best_img == current_str:
            gap_correct_count += 1
        elif not best_img:
            gap_issues.append({
                'gap_num': gap['num'],
                'current': current_str or '(none)',
                'correct': '???',
                'source': source,
            })

    # ── Impact deduplication check ──
    html_content = html_path.read_text(encoding='utf-8')
    _, dup_impacts = deduplicate_gap_impacts(html_content)

    return_val: dict[str, Any] = {
        'folder': folder.name,
        'html_path': html_path,
        'total_uxp': len(uxp_proposals),
        'correct': correct,
        'issues': issues,
        'fixes': fixes,
        'artboard_map': artboard_to_img,
        # Gap card data
        'gap_cards': gap_cards,
        'gap_issues': gap_issues,
        'gap_fixes_count': gap_fixes_count,
        'gap_correct_count': gap_correct_count,
        'gap_dup_impacts': dup_impacts,
        # Pass resolution data for gap fixing
        '_check_to_img': check_to_img,
        '_screen_sections': screen_sections,
        '_available_imgs': available_imgs,
    }
    return return_val


def apply_gap_fixes(html_path, gap_cards, check_to_img, screen_sections,
                    available_imgs, dry_run=False):
    """Apply gap card citation fixes to HTML file.

    Returns (changed, n_fixed).
    """
    html = html_path.read_text(encoding='utf-8')
    fixed_html, changes = fix_gap_citations(
        html, gap_cards, check_to_img, screen_sections, available_imgs)

    if changes and not dry_run:
        html_path.write_text(fixed_html, encoding='utf-8')

    return bool(changes), len(changes)


def main():
    parser = argparse.ArgumentParser(
        description='Fix image mapping in pitch-deck HTML files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,  # type: ignore[name-defined]
    )
    parser.add_argument('command', choices=['audit', 'fix'], help='audit: preview changes, fix: apply changes')
    parser.add_argument('--base', required=True, help='Base directory containing pitch-deck HTML files')
    parser.add_argument('--dry', action='store_true', help='Dry run — preview only, no write')

    args = parser.parse_args()
    base = Path(args.base)
    cmd = args.command

    files = find_pitch_decks(base)
    print(f"\n{'🔍' if cmd == 'audit' else '🔧'} IMAGE {'AUDIT' if cmd == 'audit' else 'FIX'} — {len(files)} files\n")

    total_issues = 0
    total_fixed = 0
    total_uxp = 0
    total_correct = 0
    total_unresolved = 0
    total_gap_issues = 0
    total_gap_fixed = 0
    total_gap_correct = 0
    total_dup_impacts = 0

    for f in files:
        result = process_one(f, cmd)
        if result is None:
            continue

        short = result['folder']
        n_uxp = result['total_uxp']
        issues = result['issues']
        n_correct = result['correct']
        total_uxp += n_uxp
        total_correct += n_correct

        # Gap card stats
        gap_issues = result.get('gap_issues', [])
        gap_correct = result.get('gap_correct_count', 0)
        dup_impacts = result.get('gap_dup_impacts', [])
        total_gap_issues += len(gap_issues)
        total_gap_correct += gap_correct
        total_dup_impacts += len(dup_impacts)

        has_uxp_issues = bool(issues)
        has_gap_issues = bool(gap_issues)

        if not has_uxp_issues and not has_gap_issues:
            n_gaps = len(result.get('gap_cards', []))
            print(f"  ✅ {short:<45} {n_uxp} UXP, {n_gaps} gaps — all correct")
            continue

        n_fixable = sum(1 for i in issues if i['correct'] != '???')
        n_unresolved = sum(1 for i in issues if i['correct'] == '???')
        total_issues += len(issues)  # type: ignore[operator]
        total_unresolved += n_unresolved  # type: ignore[operator]

        if cmd == 'audit':
            # UXP findings
            if has_uxp_issues:
                status = '⚠️' if n_fixable > 0 else '❓'
                print(f"  {status}  {short:<45} {n_uxp} UXP — {n_correct}✅ {n_fixable}🔧 {n_unresolved}❓:")
                for iss in issues:
                    marker = '→' if iss['correct'] != '???' else '✗'
                    print(f"      {iss['id']}: {iss['current'] or '(none)':<40} {marker} {iss['correct']:<40} ({iss['source']})")

            # Gap card citations
            if has_gap_issues:
                n_gap_fixable = sum(1 for i in gap_issues if i['correct'] != '???')
                n_gap_unresolved = sum(1 for i in gap_issues if i['correct'] == '???')
                print(f"  📋 {short:<45} {len(result.get('gap_cards', []))} gaps — {gap_correct}✅ {n_gap_fixable}🔧 {n_gap_unresolved}❓:")
                for gi in gap_issues:
                    marker = '→' if gi['correct'] != '???' else '✗'
                    print(f"      Gap#{gi['gap_num']}: {gi['current']:<40} {marker} {gi['correct']:<40} ({gi['source']})")

            # Impact duplicates
            if dup_impacts:
                print(f"  ⚠️  {short:<45} {len(dup_impacts)} duplicate impact texts:")
                for dup in dup_impacts:
                    print(f"      {dup['count']}× same text: \"{dup['text_preview']}...\"")

        elif cmd == 'fix':
            # Note: UXP finding card images are now handled by generate.py's
            # state-aware resolution (Tier 3). fix_images.py should NOT replace
            # UXP images as it uses simpler screen-level mapping that destroys
            # the more accurate state-specific artboard matches.
            # ── Skip UXP image replacement ──
            if result['fixes']:
                skipped_count = len(result['fixes'])
                print(f"  ⏭️  {short:<45} {skipped_count} UXP images — skipped (state-aware from generate.py)")
                if n_unresolved > 0:
                    print(f"      ⚠️  {n_unresolved} UXP still unresolved")

            # Fix gap card citations
            gap_fixable = [gi for gi in gap_issues if gi['correct'] != '???']
            if gap_fixable and result.get('gap_cards'):
                g_changed, n_g_fixed = apply_gap_fixes(
                    f, result['gap_cards'],
                    result['_check_to_img'], result['_screen_sections'],
                    result['_available_imgs'], dry_run=args.dry)
                total_gap_fixed += n_g_fixed
                status = '✅' if g_changed else '⏭️'
                if args.dry:
                    status = '🔍'
                print(f"  {status} {short:<45} {n_g_fixed} gap {'would fix' if args.dry else 'fixed'}:")
                for gi in gap_fixable:
                    print(f"      Gap#{gi['gap_num']}: {gi['current']} → {gi['correct']} ({gi['source']})")

            elif n_unresolved > 0 and not result['fixes']:
                print(f"  ❓ {short:<45} {n_unresolved} unresolved")

    print(f"\n{'=' * 70}")
    print(f"{'─' * 25} UXP CARDS {'─' * 25}")
    print(f"Total UXP cards:    {total_uxp}")
    print(f"Already correct:    {total_correct}")
    print(f"Image issues:       {total_issues}")
    if cmd == 'fix':
        print(f"Fixed:              {total_fixed}")
    print(f"Unresolved:         {total_unresolved}")
    resolved = total_correct + total_issues - total_unresolved  # type: ignore[operator]
    pct = (resolved / total_uxp * 100) if total_uxp > 0 else 0
    print(f"Coverage:           {pct:.0f}% ({resolved}/{total_uxp})")

    print(f"\n{'─' * 25} GAP CARDS {'─' * 25}")
    print(f"Gap issues:         {total_gap_issues}")
    print(f"Gap correct:        {total_gap_correct}")
    if cmd == 'fix':
        print(f"Gap fixed:          {total_gap_fixed}")
    print(f"Impact duplicates:  {total_dup_impacts}")

    print(f"\n{'─' * 25} SUMMARY {'─' * 26}")
    all_issues = total_issues + total_gap_issues
    if all_issues == 0:
        print("🎉 All images correctly mapped!")
    elif total_unresolved == 0 and total_gap_issues == 0:
        print("✅ All fixable — run 'fix' to apply")
    else:
        print(f"⚠️  {total_unresolved} UXP + {sum(1 for gi in [] if gi.get('correct') == '???')} gap unresolved")


if __name__ == '__main__':
    main()
