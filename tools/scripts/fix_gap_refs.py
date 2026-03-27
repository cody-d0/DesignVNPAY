#!/usr/bin/env python3
"""fix_gap_refs.py — Cross-reference UXP issues with check table Gap rows.

Reads each ux-review-report.md, matches UXP blocks to ❌ Gap rows using:
  1. Screen name alignment (UXP screen ⊆ check table section)
  2. DDL ref overlap
  3. Keyword similarity (key terms from UXP Vấn đề appear in gap evidence)

Only updates Gap ref fields. Does NOT touch any other content.

Usage:
  python3 tools/scripts/fix_gap_refs.py --batch COOPBANK/final
  python3 tools/scripts/fix_gap_refs.py --batch COOPBANK/final --dry-run
  python3 tools/scripts/fix_gap_refs.py <single-file>
"""
import re, sys, unicodedata
from pathlib import Path
from collections import defaultdict


# ════════════════════════════════════════════════════════════
# PARSING
# ════════════════════════════════════════════════════════════

def normalize(text):
    """Lowercase, strip accents for fuzzy matching."""
    text = text.lower().strip()
    # Remove markdown bold/italic
    text = re.sub(r'\*+', '', text)
    return text


def fold_accents(text):
    """Remove Vietnamese diacritics for cross-matching."""
    text = text.lower()
    # NFD decomposition then strip combining marks
    nfkd = unicodedata.normalize('NFKD', text)
    return ''.join(c for c in nfkd if not unicodedata.combining(c))


def extract_uxps(text):
    """Extract UXP blocks with their fields and line positions."""
    uxps = []
    # Find all UXP headers
    for m in re.finditer(r'^(#### (UXP-\d+)\s*·\s*\w+)', text, re.MULTILINE):
        uxp_id = m.group(2)
        start = m.start()
        
        # Find end of this UXP block (next #### or ## section)
        next_header = re.search(r'^#{2,4}\s', text[m.end():], re.MULTILINE)
        end = m.end() + next_header.start() if next_header else len(text)
        block = text[start:end]
        
        # Extract fields
        screen = ''
        issue = ''
        ddl = ''
        gap_ref_val = ''
        
        screen_m = re.search(r'\|\s*\*\*Màn hình\*\*\s*\|\s*(.+?)\s*\|', block)
        if screen_m:
            screen = screen_m.group(1).strip()
        
        issue_m = re.search(r'\|\s*\*\*Vấn đề\*\*\s*\|\s*(.+?)\s*\|', block)
        if issue_m:
            issue = issue_m.group(1).strip()
        
        ddl_m = re.search(r'\|\s*\*\*DDL\*\*\s*\|\s*(.+?)\s*\|', block)
        if ddl_m:
            ddl = ddl_m.group(1).strip()
        
        gapref_m = re.search(r'\|\s*\*\*Gap ref\*\*\s*\|\s*(.+?)\s*\|', block)
        if gapref_m:
            gap_ref_val = gapref_m.group(1).strip()
        
        # Extract DDL component/guideline refs
        ddl_refs = set()
        for ref in re.findall(r'(COMP:\S+|UXG-\d+)', ddl):
            ddl_refs.add(ref)
        # Also from issue text
        for ref in re.findall(r'(COMP:\S+|UXG-\d+)', issue):
            ddl_refs.add(ref)
        
        uxps.append({
            'id': uxp_id,
            'screen': screen,
            'issue': issue,
            'ddl': ddl,
            'ddl_refs': ddl_refs,
            'gap_ref': gap_ref_val,
            'block_start': start,
            'block_end': end,
        })
    
    return uxps


def extract_check_sections(text):
    """Extract per-screen check table sections with their gap rows.
    
    Handles multiple check table formats:
    1. Canonical: | # | Check | Source | DDL | Verdict(❌ Gap) | Evidence |
    2. Alt-1: | # | Check | Source | DDL | Evidence | Verdict(Gap) |  (verdict last)
    3. Alt-2: | # | Check | Category | Severity | Evidence | Verdict |  (no emoji)
    4. Compact: | # | Check | Source | DDL | Verdict(Gap/Pass) | Evidence |  (text-only)
    """
    sections = []
    
    # Find screen sections (### N. Screen Name)
    headers = list(re.finditer(
        r'^###\s+\d+\.\s+(.+?)$', text, re.MULTILINE
    ))
    
    for i, hdr in enumerate(headers):
        screen_name = hdr.group(1).strip()
        start = hdr.end()
        end = headers[i+1].start() if i+1 < len(headers) else len(text)
        section_text = text[start:end]
        
        # Find all gap rows in this section — try multiple patterns
        gaps = []
        
        for line in section_text.split('\n'):
            # Must be a table row starting with | number |
            num_m = re.match(r'\|\s*(\d+)\s*\|', line)
            if not num_m:
                continue
            
            check_num = num_m.group(1)
            
            # Detect gap: any cell containing "Gap" (with or without ❌)
            # But NOT rows that are headers or contain "Gap ref" or "Gap:" as label
            cells = [c.strip() for c in line.split('|')[1:]]  # Split by pipe, skip first empty
            
            is_gap = False
            for cell in cells:
                # Cell is a verdict cell if it's short and contains "Gap"
                cell_clean = cell.strip()
                if re.match(r'^(❌\s*)?Gap$', cell_clean, re.IGNORECASE):
                    is_gap = True
                    break
            
            if not is_gap:
                continue
            
            # Extract check description (2nd cell) and full row
            check_desc = cells[1] if len(cells) > 1 else ''
            full_row = line
            
            # Extract DDL refs from the row  
            ddl_refs = set()
            for ref in re.findall(r'(COMP:\S+|UXG-\d+)', full_row):
                ddl_refs.add(ref)
            
            gaps.append({
                'check_num': check_num,
                'check_desc': check_desc,
                'evidence': full_row,  # Use full row as evidence for matching
                'full_row': full_row,
                'ddl_refs': ddl_refs,
                'screen_name': screen_name,
            })
        
        if gaps:
            sections.append({
                'screen_name': screen_name,
                'gaps': gaps,
            })
    
    return sections


# ════════════════════════════════════════════════════════════
# MATCHING
# ════════════════════════════════════════════════════════════

def screen_match(uxp_screen, gap_screen):
    """Check if UXP screen name overlaps with gap section screen name."""
    if not uxp_screen or not gap_screen:
        return False
    
    u = normalize(uxp_screen)
    g = normalize(gap_screen)
    # Strip SCR-XXX-NNN pattern from section name
    g = re.sub(r'\(\s*`?scr-[^)]+`?\s*\)', '', g).strip()
    
    # Direct containment
    if u in g or g in u:
        return True
    
    # Accent-folded containment
    uf = fold_accents(u)
    gf = fold_accents(g)
    if uf in gf or gf in uf:
        return True
    
    # Extract key part after › 
    u_parts = [p.strip() for p in u.split('›')]
    g_parts = [p.strip() for p in g.split('›')]
    
    # Compare last parts (most specific)
    if u_parts and g_parts:
        if u_parts[-1] in g_parts[-1] or g_parts[-1] in u_parts[-1]:
            return True
        # Accent-folded last part
        uf_last = fold_accents(u_parts[-1])
        gf_last = fold_accents(g_parts[-1])
        if uf_last in gf_last or gf_last in uf_last:
            return True
    
    # Fuzzy: >40% word overlap (accent-folded)
    u_words = set(fold_accents(u).split())
    g_words = set(fold_accents(g).split())
    common = {'›', '·', '-', '—'}
    u_words -= common
    g_words -= common
    if u_words and g_words:
        overlap = len(u_words & g_words) / min(len(u_words), len(g_words))
        if overlap > 0.4:
            return True
    
    return False


def keyword_similarity(uxp_issue, gap_row):
    """Score keyword overlap between UXP issue and gap row evidence."""
    if not uxp_issue or not gap_row:
        return 0.0
    
    u = normalize(uxp_issue)
    g = normalize(gap_row)
    
    # Extract meaningful keywords (>3 chars, not common words)
    stop_words = {
        'không', 'thiếu', 'hiển', 'thị', 'hiện', 'trạng', 'thái',
        'người', 'dùng', 'user', 'screen', 'field', 'button',
        'check', 'pass', 'gap', 'evidence', 'from', 'with', 'the',
        'của', 'trong', 'cho', 'được', 'khi', 'theo', 'bằng',
        'trên', 'dưới', 'cùng', 'khác', 'mỗi', 'các', 'một',
        'skill', 'comp', 'uxg', 'law',
    }
    
    u_words = {w for w in re.findall(r'[\w]+', u) if len(w) > 3 and w not in stop_words}
    g_words = {w for w in re.findall(r'[\w]+', g) if len(w) > 3 and w not in stop_words}
    
    if not u_words or not g_words:
        return 0.0
    
    overlap = u_words & g_words
    score = len(overlap) / min(len(u_words), len(g_words))
    return score


def match_uxp_to_gaps(uxp, all_sections):
    """Find the best matching gap rows for a UXP."""
    candidates = []
    
    for section in all_sections:
        for gap in section['gaps']:
            score = 0.0
            reasons = []
            
            # Factor 1: Screen name match (strong signal)
            if screen_match(uxp['screen'], gap['screen_name']):
                score += 3.0
                reasons.append('screen')
            else:
                # Screen mismatch — unlikely match unless very strong signals
                continue
            
            # Factor 2: DDL ref overlap (strong signal)
            ddl_overlap = uxp['ddl_refs'] & gap['ddl_refs']
            if ddl_overlap:
                score += 2.0 * len(ddl_overlap)
                reasons.append(f'ddl={",".join(ddl_overlap)}')
            
            # Factor 3: Keyword similarity
            kw_score = keyword_similarity(uxp['issue'], gap['full_row'])
            if kw_score > 0.2:
                score += kw_score * 2.0
                reasons.append(f'kw={kw_score:.2f}')
            
            if score >= 3.0:  # At minimum need screen match
                candidates.append({
                    'check_num': gap['check_num'],
                    'score': score,
                    'reasons': reasons,
                })
    
    # Sort by score descending
    candidates.sort(key=lambda x: -x['score'])
    
    # Return top matches (max 3, score > threshold)
    results = []
    for c in candidates:
        if c['score'] >= 4.0 or (c['score'] >= 3.0 and len(results) == 0):
            results.append(c)
        if len(results) >= 3:
            break
    
    return results


# ════════════════════════════════════════════════════════════
# FILE PROCESSING
# ════════════════════════════════════════════════════════════

def process_file(filepath, dry_run=False):
    """Process a single file: match UXPs to gaps, update Gap ref fields."""
    text = Path(filepath).read_text(encoding='utf-8')
    
    uxps = extract_uxps(text)
    if not uxps:
        return 0, 0
    
    sections = extract_check_sections(text)
    if not sections:
        return 0, 0
    
    updated = 0
    total_empty = 0
    
    for uxp in uxps:
        if uxp['gap_ref'] and uxp['gap_ref'] != '—' and uxp['gap_ref'] != '–':
            continue  # Already has gap ref
        
        total_empty += 1
        matches = match_uxp_to_gaps(uxp, sections)
        
        if matches:
            gap_ref = ', '.join(f'Check #{m["check_num"]}' for m in matches)
            
            if dry_run:
                reasons = '; '.join(f'#{m["check_num"]}({",".join(m["reasons"])})' for m in matches)
                print(f'    {uxp["id"]}: → {gap_ref}  [{reasons}]')
            else:
                # Replace in text — find the exact Gap ref line for this UXP
                # Build pattern: after this UXP header, find Gap ref row
                uxp_block = text[uxp['block_start']:uxp['block_end']]
                old_line = '| **Gap ref** | — |'
                new_line = f'| **Gap ref** | {gap_ref} |'
                if old_line in uxp_block:
                    new_block = uxp_block.replace(old_line, new_line, 1)
                    text = text[:uxp['block_start']] + new_block + text[uxp['block_end']:]
                    # Recalculate positions for remaining UXPs
                    offset = len(new_block) - len(uxp_block)
                    for other in uxps:
                        if other['block_start'] > uxp['block_start']:
                            other['block_start'] += offset
                            other['block_end'] += offset
                    uxp['block_end'] += offset
                    updated += 1
        else:
            if dry_run:
                print(f'    {uxp["id"]}: ⚠️  no match found (screen="{uxp["screen"][:40]}")')
    
    if not dry_run and updated > 0:
        Path(filepath).write_text(text, encoding='utf-8')
    
    return total_empty, updated


# ════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════

if __name__ == '__main__':
    dry_run = '--dry-run' in sys.argv
    args = [a for a in sys.argv[1:] if a != '--dry-run']
    
    if not args or args[0] in ('-h', '--help'):
        print(__doc__)
        sys.exit(0)
    
    if args[0] == '--batch':
        base = Path(args[1])
        files = sorted(base.rglob('ux-review-report.md'))
        grand_empty = 0
        grand_updated = 0
        
        for f in files:
            name = str(f.relative_to(base))
            empty, updated = process_file(f, dry_run=dry_run)
            if empty > 0:
                status = f'→ {updated}/{empty} filled' if not dry_run else f'{empty} empty'
                print(f'📄 {name}: {status}')
            grand_empty += empty
            grand_updated += updated
        
        print()
        mode = 'DRY RUN' if dry_run else 'DONE'
        print(f'[{mode}] Empty: {grand_empty} | Filled: {grand_updated} | Remaining: {grand_empty - grand_updated}')
    else:
        filepath = args[0]
        print(f'📄 {filepath}')
        empty, updated = process_file(filepath, dry_run=dry_run)
        print(f'Empty: {empty} | Filled: {updated}')
