#!/usr/bin/env python3
"""
index_images.py — Indexer chuyên biệt: image ↔ UXP/Gap mapping data.

Consumer target: evidence-img skill (hoặc bất kỳ tool nào cần map ảnh → finding).

Scan mỗi module và thu thập:
  1. ui/*.png — danh sách ảnh thực tế trên disk
  2. handoff/screen_inventory.json — wireframe_images (filename, role, node_id)
  3. artboard-index.json — artboard → SCR-ID → display_name mapping
  4. SCR-*.md — wireframe refs (![alt](ui/xxx.png))
  5. ux-review-report.md — evidence column refs ("Từ ảnh xxx.png:", "artboard xxx:")
  6. report-data.json — existing screenshot_path mappings (nếu đã chạy converter)

Output:
  - image-index.json   (structured index cho consumer)
  - Console report     (coverage + quality analysis)

Usage:
  python3 index_images.py --base /path/to/COOPBANK/final/
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional


# ═══════════════════════════════════════════════════════════
# SOURCE 1: UI FOLDER — actual image files on disk  
# ═══════════════════════════════════════════════════════════

def _index_ui_files(ui_dir: Path) -> list[dict]:
    """Liệt kê tất cả ảnh thực tế trong ui/ folder."""
    if not ui_dir.exists():
        return []

    images = []
    for f in sorted(ui_dir.iterdir()):
        if f.is_file() and f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"):
            # Trích artboard_id từ filename (4 chữ số đầu)
            artboard_match = re.match(r'^(\d{4})', f.stem)
            artboard_id = artboard_match.group(1) if artboard_match else None

            images.append({
                "filename": f.name,
                "stem": f.stem,
                "artboard_id": artboard_id,
                "size_kb": round(f.stat().st_size / 1024, 1),
                "path_relative": f"ui/{f.name}",
            })
    return images


# ═══════════════════════════════════════════════════════════
# SOURCE 2: SCREEN INVENTORY — wireframe_images
# ═══════════════════════════════════════════════════════════

def _index_inventory_images(inventory_path: Path) -> list[dict]:
    """Trích wireframe_images từ screen_inventory.json → mapping SCR-ID → images."""
    if not inventory_path.exists():
        return []

    try:
        data = json.loads(inventory_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []

    entries = []
    for scr in data.get("screens", []):
        scr_id = scr.get("id") or scr.get("screen_id", "?")
        scr_name = scr.get("display_name") or scr.get("screen_name", "")
        scr_type = scr.get("screen_type", "unknown")

        for img in scr.get("wireframe_images", []):
            filename = img.get("filename", "")
            artboard_match = re.match(r'^(\d{4})', Path(filename).stem) if filename else None

            entries.append({
                "screen_id": scr_id,
                "screen_name": scr_name,
                "screen_type": scr_type,
                "filename": filename,
                "artboard_id": artboard_match.group(1) if artboard_match else None,
                "role": img.get("role", ""),
                "node_id": img.get("node_id", ""),
            })
    return entries


# ═══════════════════════════════════════════════════════════
# SOURCE 3: ARTBOARD INDEX — artboard → SCR-ID mapping  
# ═══════════════════════════════════════════════════════════

def _index_artboard_index(ai_path: Path) -> dict:
    """Trích thông tin từ artboard-index.json."""
    if not ai_path.exists():
        return {"exists": False, "entries": []}

    try:
        data = json.loads(ai_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"exists": False, "error": "invalid JSON"}

    entries = []
    if isinstance(data, dict):
        for scr_id, info in data.items():
            display_name = info.get("display_name", "")
            artboards = info.get("artboards", {})
            for ab_filename, ab_info in artboards.items():
                entries.append({
                    "screen_id": scr_id,
                    "display_name": display_name,
                    "artboard_filename": ab_filename,
                    "artboard_name": ab_info.get("artboard_name", ""),
                    "role": ab_info.get("role", ""),
                    "keywords": ab_info.get("keywords", []),
                    "text_elements": ab_info.get("text_elements", []),
                    "states": ab_info.get("states", []),
                })

    return {"exists": True, "entry_count": len(entries), "entries": entries}


# ═══════════════════════════════════════════════════════════
# SOURCE 4: SCR-*.md — wireframe references
# ═══════════════════════════════════════════════════════════

def _index_scr_md_images(module_dir: Path) -> list[dict]:
    """Trích ảnh tham chiếu từ SCR-*.md files."""
    entries = []
    scr_files = sorted(module_dir.glob("SCR-*.md"))

    img_ref_re = re.compile(r'!\[([^\]]*)\]\(ui/([^)]+)\)')
    scr_id_re = re.compile(r'(SCR-\w+-\d+)')

    for scr_file in scr_files:
        # Lấy SCR-ID từ filename
        scr_match = scr_id_re.match(scr_file.stem)
        scr_id = scr_match.group(1) if scr_match else scr_file.stem

        try:
            content = scr_file.read_text(encoding="utf-8")
        except OSError:
            continue

        for m in img_ref_re.finditer(content):
            alt_text = m.group(1)
            filename = m.group(2)
            artboard_match = re.match(r'^(\d{4})', Path(filename).stem)

            # Phát hiện role từ alt text
            role = "base"
            alt_lower = alt_text.lower()
            if "overlay" in alt_lower:
                role = "overlay"
            elif "popup" in alt_lower:
                role = "overlay:popup"
            elif "bottom" in alt_lower and "sheet" in alt_lower:
                role = "overlay:bottom_sheet"
            elif "otp" in alt_lower:
                role = "overlay:otp"
            elif "success" in alt_lower:
                role = "overlay:success"
            elif "error" in alt_lower:
                role = "overlay:error"
            elif "variant" in alt_lower:
                role = "variant"

            entries.append({
                "source_file": scr_file.name,
                "screen_id": scr_id,
                "filename": filename,
                "artboard_id": artboard_match.group(1) if artboard_match else None,
                "alt_text": alt_text,
                "role": role,
            })

    return entries


# ═══════════════════════════════════════════════════════════
# SOURCE 5: REPORT — evidence column image references
# ═══════════════════════════════════════════════════════════

def _index_report_image_refs(report_path: Path) -> dict:
    """Trích tất cả tham chiếu ảnh từ ux-review-report.md."""
    if not report_path.exists():
        return {"pattern": "none", "refs": [], "check_image_map": []}

    try:
        content = report_path.read_text(encoding="utf-8")
        lines = content.splitlines()
    except OSError:
        return {"pattern": "none", "refs": [], "check_image_map": []}

    # Phát hiện pattern dùng trong evidence
    pattern_type = "none"
    if "Từ ảnh " in content:
        pattern_type = "vi_anh"       # "Từ ảnh xxx.png:"
    elif "From image" in content:
        pattern_type = "en_image"     # "From image xxx.png:"
    elif "Vision:" in content:
        pattern_type = "vision_colon" # "Vision: ..."
    elif ".png" in content:
        pattern_type = "bare_png"     # filename.png referenced directly

    # Trích filename refs
    image_refs = set()
    # Pattern: "Từ ảnh xxx.png" hoặc "Từ ảnh xxx:"
    for m in re.finditer(r'Từ ảnh\s+([a-zA-Z0-9_-]+(?:\.png)?)', content):
        ref = m.group(1)
        if not ref.endswith('.png'):
            ref += '.png'
        image_refs.add(ref)
    # Pattern: "From image xxx.png"
    for m in re.finditer(r'From image[: ]+([a-zA-Z0-9_-]+(?:\.png)?)', content):
        ref = m.group(1)
        if not ref.endswith('.png'):
            ref += '.png'
        image_refs.add(ref)
    # Pattern: bare filenames "xxxx-slug.png"
    for m in re.finditer(r'(\d{4}-[a-zA-Z0-9_-]+\.png)', content):
        image_refs.add(m.group(1))
    # Pattern: generic "filename.png" in evidence columns
    for m in re.finditer(r'([a-zA-Z][a-zA-Z0-9_-]*\.png)', content):
        image_refs.add(m.group(1))

    # Xây check_num → artboard mapping từ evidence column trong check tables
    check_image_map = []
    # Tìm các dòng table có Check # + Evidence
    check_row_re = re.compile(
        r'^\|\s*(\d+)\s*\|'   # Check #
        r'\s*(.+?)\s*\|'       # Check text
        r'(?:\s*.+?\s*\|){2,3}'  # Middle columns (2-3 extra)
        r'\s*(\w+)\s*\|'       # Verdict
        r'\s*(.+?)\s*\|'       # Evidence
        r'\s*$'
    )

    for line in lines:
        m = check_row_re.match(line.strip())
        if m:
            check_num = int(m.group(1))
            verdict = m.group(3).strip()
            evidence = m.group(4).strip()

            # Trích ảnh từ evidence text
            evidence_images = []
            for img_m in re.finditer(r'(\d{4}-[a-zA-Z0-9_-]+\.png)', evidence):
                evidence_images.append(img_m.group(1))
            for img_m in re.finditer(r'([a-zA-Z][a-zA-Z0-9_-]*\.png)', evidence):
                if img_m.group(1) not in evidence_images:
                    evidence_images.append(img_m.group(1))
            # Fallback: artboard IDs (4-digit)
            artboard_ids = []
            for aid_m in re.finditer(r'\b(\d{4})\b', evidence):
                aid = aid_m.group(1)
                if int(aid) >= 7000 and aid not in [str(x) for x in range(2020, 2030)]:
                    artboard_ids.append(aid)

            if evidence_images or artboard_ids:
                check_image_map.append({
                    "check_num": check_num,
                    "verdict": verdict,
                    "images": evidence_images,
                    "artboard_ids": artboard_ids,
                    "evidence_snippet": evidence[:120],
                })

    return {
        "pattern": pattern_type,
        "unique_image_refs": sorted(image_refs),
        "ref_count": len(image_refs),
        "check_image_map": check_image_map,
    }


# ═══════════════════════════════════════════════════════════
# SOURCE 6: EXISTING report-data.json — already mapped paths
# ═══════════════════════════════════════════════════════════

def _index_existing_mappings(report_data_path: Path) -> dict:
    """Trích screenshot_path đã map từ report-data.json."""
    if not report_data_path.exists():
        return {"exists": False}

    try:
        data = json.loads(report_data_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"exists": False, "error": "invalid JSON"}

    uxp_mappings = []
    for uxp in data.get("uxps", []):
        uxp_mappings.append({
            "uxp_id": uxp.get("id", "?"),
            "severity": uxp.get("severity", "?"),
            "screen_tag": uxp.get("screen_tag", ""),
            "screenshot_path": uxp.get("screenshot_path", ""),
            "has_image": bool(uxp.get("screenshot_path")),
        })

    gap_mappings = []
    for gs in data.get("gaps_by_screen", []):
        for g in gs.get("gaps", []):
            gap_mappings.append({
                "screen_id": gs.get("screen_id", "?"),
                "check_num": g.get("num"),
                "title": g.get("title", "")[:80],
                "screenshot": g.get("screenshot", ""),
                "screenshot_path": g.get("screenshot_path", ""),
                "has_image": bool(g.get("screenshot_path")),
            })

    # Enrichment metadata
    img_enrich = data.get("_image_enrichment", {})

    return {
        "exists": True,
        "uxp_count": len(uxp_mappings),
        "uxp_with_image": sum(1 for u in uxp_mappings if u["has_image"]),
        "gap_count": len(gap_mappings),
        "gap_with_image": sum(1 for g in gap_mappings if g["has_image"]),
        "uxp_mappings": uxp_mappings,
        "gap_mappings": gap_mappings,
        "enrichment_metadata": img_enrich,
    }


# ═══════════════════════════════════════════════════════════
# SOURCE 7: UXP block → image references
# ═══════════════════════════════════════════════════════════

def _index_uxp_image_refs(report_path: Path) -> list[dict]:
    """Trích artboard/image refs từ UXP blocks trong report."""
    if not report_path.exists():
        return []

    try:
        lines = report_path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []

    uxp_refs = []
    uxp_re = re.compile(r'^####\s+(UXP-\d+)\s*·\s*(.+)$')
    field_re = re.compile(r'^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|')

    current_uxp = None
    current_fields = {}

    for line in lines:
        stripped = line.strip()
        m = uxp_re.match(stripped)
        if m:
            # Lưu UXP trước đó
            if current_uxp:
                uxp_refs.append(_build_uxp_image_entry(current_uxp, current_fields))
            current_uxp = m.group(1)
            current_fields = {"severity": m.group(2).strip()}
            continue

        if current_uxp:
            fm = field_re.match(stripped)
            if fm:
                current_fields[fm.group(1)] = fm.group(2).strip()

    # Lưu UXP cuối cùng
    if current_uxp:
        uxp_refs.append(_build_uxp_image_entry(current_uxp, current_fields))

    return uxp_refs


def _build_uxp_image_entry(uxp_id: str, fields: dict) -> dict:
    """Xây image context entry cho 1 UXP."""
    screen_tag = fields.get("Màn hình", "")
    gap_ref = fields.get("Gap ref", "")
    evidence_text = fields.get("Vấn đề", "") + " " + fields.get("Giải pháp", "")

    # Trích SCR-ID từ screen_tag
    scr_match = re.search(r'(SCR-\w+-\d+)', screen_tag)
    scr_id = scr_match.group(1) if scr_match else None

    # Trích artboard IDs từ gap_ref
    gap_check_nums = []
    for m in re.finditer(r'#(\d+)', gap_ref):
        gap_check_nums.append(int(m.group(1)))

    # Trích artboard IDs từ screen_tag (e.g., "7201")
    artboard_ids = []
    for m in re.finditer(r'\b(\d{4})\b', screen_tag + " " + gap_ref + " " + evidence_text):
        aid = m.group(1)
        if int(aid) >= 7000 and int(aid) < 9999:
            if aid not in artboard_ids:
                artboard_ids.append(aid)

    # Trích image filenames
    image_filenames = []
    for m in re.finditer(r'([a-zA-Z0-9_-]+\.png)', evidence_text):
        if m.group(1) not in image_filenames:
            image_filenames.append(m.group(1))

    return {
        "uxp_id": uxp_id,
        "severity": fields.get("severity", ""),
        "screen_tag": screen_tag,
        "screen_id": scr_id,
        "gap_check_nums": gap_check_nums,
        "artboard_ids": artboard_ids,
        "image_filenames": image_filenames,
    }


# ═══════════════════════════════════════════════════════════
# MAIN MODULE INDEXER
# ═══════════════════════════════════════════════════════════

def index_module_images(module_dir: Path) -> dict:
    """Index toàn bộ image data cho 1 module."""
    report_path = module_dir / "ux-review-report.md"
    handoff_dir = module_dir / "handoff"
    ui_dir = module_dir / "ui"

    entry = {
        "module_dir": str(module_dir),
        "module_name": module_dir.name,
        "parent_section": module_dir.parent.name if module_dir.parent.name != "final" else "",
    }

    # Source 1: Ảnh thực trên disk
    entry["disk_images"] = _index_ui_files(ui_dir)

    # Source 2: Screen inventory wireframe_images
    entry["inventory_images"] = _index_inventory_images(
        handoff_dir / "screen_inventory.json"
    )

    # Source 3: Artboard index
    entry["artboard_index"] = _index_artboard_index(
        module_dir / "artboard-index.json"
    )

    # Source 4: SCR-*.md references
    entry["scr_md_images"] = _index_scr_md_images(module_dir)

    # Source 5: Report evidence refs
    entry["report_image_refs"] = _index_report_image_refs(report_path)

    # Source 6: Existing report-data.json mappings
    entry["existing_mappings"] = _index_existing_mappings(
        module_dir / "report-data.json"
    )

    # Source 7: UXP block image refs
    entry["uxp_image_refs"] = _index_uxp_image_refs(report_path)

    # Cross-source analysis
    entry["coverage"] = _analyze_coverage(entry)

    return entry


def _analyze_coverage(entry: dict) -> dict:
    """Phân tích coverage: bao nhiêu UXP/Gap có ảnh map được."""
    disk_files = {img["filename"] for img in entry.get("disk_images", [])}
    inventory_files = {img["filename"] for img in entry.get("inventory_images", [])}
    scr_md_files = {img["filename"] for img in entry.get("scr_md_images", [])}
    report_refs = set(entry.get("report_image_refs", {}).get("unique_image_refs", []))

    # Ảnh có trên disk nhưng không được tham chiếu bởi bất kỳ source nào
    all_referenced = inventory_files | scr_md_files | report_refs
    orphan_images = disk_files - all_referenced
    # Ảnh được tham chiếu nhưng không có trên disk
    missing_images = all_referenced - disk_files

    # UXP coverage
    existing = entry.get("existing_mappings", {})
    uxp_total = existing.get("uxp_count", 0)
    uxp_mapped = existing.get("uxp_with_image", 0)
    gap_total = existing.get("gap_count", 0)
    gap_mapped = existing.get("gap_with_image", 0)

    # SCR-ID → image coverage
    inventory_scr_ids = {img["screen_id"] for img in entry.get("inventory_images", [])}
    uxp_scr_ids = {ref["screen_id"] for ref in entry.get("uxp_image_refs", []) if ref["screen_id"]}
    scr_ids_without_images = uxp_scr_ids - inventory_scr_ids

    return {
        "disk_image_count": len(disk_files),
        "inventory_image_count": len(inventory_files),
        "scr_md_image_count": len(scr_md_files),
        "report_ref_count": len(report_refs),
        "orphan_images": sorted(orphan_images),
        "missing_images": sorted(missing_images),
        "uxp_total": uxp_total,
        "uxp_mapped": uxp_mapped,
        "uxp_coverage_pct": round(uxp_mapped / uxp_total * 100) if uxp_total > 0 else 0,
        "gap_total": gap_total,
        "gap_mapped": gap_mapped,
        "gap_coverage_pct": round(gap_mapped / gap_total * 100) if gap_total > 0 else 0,
        "scr_ids_without_images": sorted(scr_ids_without_images),
    }


# ═══════════════════════════════════════════════════════════
# REPORT GENERATOR
# ═══════════════════════════════════════════════════════════

def build_image_report(index: list[dict]) -> str:
    """Tạo báo cáo phân tích image mapping."""
    L = []
    L.append("=" * 90)
    L.append("  BÁO CÁO IMAGE INDEX — Pipeline UX Audit Co-opBank")
    L.append(f"  Ngày tạo: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    L.append(f"  Số modules: {len(index)}")
    L.append("=" * 90)

    # ── Tổng quan ──
    L.append("\n┌──────────────────────────────────────────────────────────┐")
    L.append("│  1. TỔNG QUAN                                            │")
    L.append("└──────────────────────────────────────────────────────────┘\n")

    total_disk = sum(len(m.get("disk_images", [])) for m in index)
    total_inv = sum(len(m.get("inventory_images", [])) for m in index)
    total_scr_md = sum(len(m.get("scr_md_images", [])) for m in index)
    total_artboard = sum(
        m.get("artboard_index", {}).get("entry_count", 0) for m in index
    )
    total_report_refs = sum(
        m.get("report_image_refs", {}).get("ref_count", 0) for m in index
    )

    total_uxp = sum(m.get("coverage", {}).get("uxp_total", 0) for m in index)
    total_uxp_mapped = sum(m.get("coverage", {}).get("uxp_mapped", 0) for m in index)
    total_gap = sum(m.get("coverage", {}).get("gap_total", 0) for m in index)
    total_gap_mapped = sum(m.get("coverage", {}).get("gap_mapped", 0) for m in index)

    L.append(f"  Ảnh trên disk (ui/):           {total_disk:>5}")
    L.append(f"  Wireframe entries (inventory):  {total_inv:>5}")
    L.append(f"  Artboard index entries:         {total_artboard:>5}")
    L.append(f"  SCR-*.md image refs:            {total_scr_md:>5}")
    L.append(f"  Report evidence refs:           {total_report_refs:>5}")
    L.append("")
    L.append(f"  UXP tổng / đã map ảnh:         {total_uxp_mapped}/{total_uxp}"
             f" ({round(total_uxp_mapped/total_uxp*100) if total_uxp else 0}%)")
    L.append(f"  Gap tổng / đã map ảnh:         {total_gap_mapped}/{total_gap}"
             f" ({round(total_gap_mapped/total_gap*100) if total_gap else 0}%)")

    # ── Bảng từng module ──
    L.append("\n┌──────────────────────────────────────────────────────────┐")
    L.append("│  2. CHI TIẾT TỪNG MODULE                                 │")
    L.append("└──────────────────────────────────────────────────────────┘\n")

    header = (f"  {'#':>2}  {'Module':<35}  {'Disk':>4}  {'Inv':>4}  {'AI':>3}  "
              f"{'SCR':>3}  {'Rpt':>3}  {'UXP':>9}  {'Gap':>9}  {'Pattern':<12}")
    L.append(header)
    L.append("  " + "─" * 100)

    for i, m in enumerate(index, 1):
        name = m["module_name"][:33]
        cov = m.get("coverage", {})
        disk = cov.get("disk_image_count", 0)
        inv = cov.get("inventory_image_count", 0)
        ai = m.get("artboard_index", {}).get("entry_count", 0)
        scr = cov.get("scr_md_image_count", 0)
        rpt = cov.get("report_ref_count", 0)
        uxp_str = f"{cov.get('uxp_mapped',0)}/{cov.get('uxp_total',0)}"
        gap_str = f"{cov.get('gap_mapped',0)}/{cov.get('gap_total',0)}"
        pattern = m.get("report_image_refs", {}).get("pattern", "?")

        L.append(f"  {i:>2}  {name:<35}  {disk:>4}  {inv:>4}  {ai:>3}  "
                 f"{scr:>3}  {rpt:>3}  {uxp_str:>9}  {gap_str:>9}  {pattern:<12}")

    # ── Phân tích data sources ──
    L.append("\n┌──────────────────────────────────────────────────────────┐")
    L.append("│  3. PHÂN TÍCH DATA SOURCES                               │")
    L.append("└──────────────────────────────────────────────────────────┘\n")

    # 3a. Evidence pattern
    patterns = {}
    for m in index:
        p = m.get("report_image_refs", {}).get("pattern", "none")
        patterns[p] = patterns.get(p, 0) + 1
    L.append("  3a. Evidence Pattern trong report:")
    for k, v in sorted(patterns.items(), key=lambda x: -x[1]):
        L.append(f"      {k:<20} {v:>3} modules")

    # 3b. Artboard index coverage
    has_ai = sum(1 for m in index if m.get("artboard_index", {}).get("exists"))
    L.append(f"\n  3b. Có artboard-index.json:  {has_ai}/{len(index)} modules")

    # 3c. SCR-*.md coverage
    has_scr = sum(1 for m in index if len(m.get("scr_md_images", [])) > 0)
    L.append(f"  3c. Có SCR-*.md image refs:  {has_scr}/{len(index)} modules")

    # 3d. Existing report-data.json
    has_rd = sum(1 for m in index if m.get("existing_mappings", {}).get("exists"))
    L.append(f"  3d. Có report-data.json:     {has_rd}/{len(index)} modules")

    # ── Data quality ──
    L.append("\n┌──────────────────────────────────────────────────────────┐")
    L.append("│  4. VẤN ĐỀ CHẤT LƯỢNG DỮ LIỆU ẢNH                      │")
    L.append("└──────────────────────────────────────────────────────────┘\n")

    # 4a. Orphan images (có trên disk nhưng không ai reference)
    L.append("  4a. Ảnh mồ côi (trên disk nhưng không được tham chiếu):")
    orphan_count = 0
    for m in index:
        orphans = m.get("coverage", {}).get("orphan_images", [])
        if orphans:
            orphan_count += len(orphans)
            L.append(f"      {m['module_name']}: {', '.join(orphans[:5])}"
                     f"{'...' if len(orphans) > 5 else ''} ({len(orphans)} ảnh)")
    if orphan_count == 0:
        L.append("      (không có)")
    L.append(f"      Tổng ảnh mồ côi: {orphan_count}")

    # 4b. Missing images (được reference nhưng không có trên disk)  
    L.append("\n  4b. Ảnh thiếu (được tham chiếu nhưng không có trên disk):")
    missing_count = 0
    for m in index:
        missing = m.get("coverage", {}).get("missing_images", [])
        if missing:
            missing_count += len(missing)
            L.append(f"      {m['module_name']}: {', '.join(missing[:5])}"
                     f"{'...' if len(missing) > 5 else ''} ({len(missing)} ảnh)")
    if missing_count == 0:
        L.append("      (không có)")
    L.append(f"      Tổng ảnh thiếu: {missing_count}")

    # 4c. UXP + Gap chưa map ảnh
    L.append("\n  4c. UXP chưa có ảnh (cần image mapping):")
    for m in index:
        cov = m.get("coverage", {})
        unmapped = cov.get("uxp_total", 0) - cov.get("uxp_mapped", 0)
        if unmapped > 0:
            L.append(f"      {m['module_name']}: {unmapped} UXP chưa map")

    L.append("\n  4d. Gap chưa có ảnh:")
    gap_unmapped_total = 0
    for m in index:
        cov = m.get("coverage", {})
        unmapped = cov.get("gap_total", 0) - cov.get("gap_mapped", 0)
        if unmapped > 0:
            gap_unmapped_total += unmapped
            L.append(f"      {m['module_name']}: {unmapped} gaps chưa map")
    if gap_unmapped_total == 0:
        L.append("      (tất cả gaps đã có ảnh)")
    L.append(f"      Tổng gaps chưa map: {gap_unmapped_total}")

    # ── Mapping strategy insights ──
    L.append("\n┌──────────────────────────────────────────────────────────┐")
    L.append("│  5. CHIẾN LƯỢC MAPPING CHO CONSUMER                     │")
    L.append("└──────────────────────────────────────────────────────────┘\n")

    L.append("  5a. Chuỗi ưu tiên data source (resolution chain):")
    L.append("      1. artboard-index.json  — SCR-ID → artboard → filename (cao nhất)")
    L.append("      2. screen_inventory.json → wireframe_images (filename + role)")
    L.append("      3. SCR-*.md → ![alt](ui/xxx.png) (có role từ alt text)")
    L.append("      4. report evidence column → 'Từ ảnh xxx.png' (direct ref)")
    L.append("      5. Gap ref check#N → check_image_map → artboard_id (indirect)")
    L.append("      6. Fallback: SCR-ID → base image từ inventory")

    L.append("\n  5b. Image role mapping:")
    all_roles = set()
    for m in index:
        for img in m.get("inventory_images", []):
            if img.get("role"):
                all_roles.add(img["role"])
        for img in m.get("scr_md_images", []):
            if img.get("role"):
                all_roles.add(img["role"])
    L.append(f"      Roles found: {sorted(all_roles)}")

    L.append("\n" + "=" * 90)
    return "\n".join(L)


# ═══════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Index toàn bộ image data cho image↔UXP/Gap mapping"
    )
    parser.add_argument("--base", type=Path, required=True,
                        help="Thư mục gốc chứa các module (vd: COOPBANK/final/)")
    parser.add_argument("--output", type=Path, default=None,
                        help="Thư mục đầu ra (mặc định: thư mục gốc)")
    args = parser.parse_args()

    if not args.base.exists():
        print(f"Lỗi: Không tìm thấy thư mục: {args.base}", file=sys.stderr)
        sys.exit(1)

    output_dir = args.output or args.base

    # Tìm modules
    report_files = sorted(args.base.rglob("ux-review-report.md"))
    module_dirs = [f.parent for f in report_files]

    print(f"📂 Tìm thấy {len(module_dirs)} modules\n", file=sys.stderr)

    # Index
    index = []
    for i, module_dir in enumerate(module_dirs, 1):
        rel = module_dir.relative_to(args.base)
        print(f"  [{i:>2}/{len(module_dirs)}] Indexing ảnh: {rel}", file=sys.stderr)
        entry = index_module_images(module_dir)
        index.append(entry)

    # Ghi file JSON
    index_path = output_dir / "image-index.json"
    index_path.write_text(
        json.dumps(index, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"\n📄 Index ghi tại: {index_path}", file=sys.stderr)
    print(f"   Kích thước: {index_path.stat().st_size / 1024:.1f} KB", file=sys.stderr)

    # Tạo và in báo cáo
    report = build_image_report(index)
    print("\n" + report)

    report_path = output_dir / "image-index-report.txt"
    report_path.write_text(report, encoding="utf-8")
    print(f"\n📄 Báo cáo lưu tại: {report_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
