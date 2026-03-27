#!/usr/bin/env python3
"""
index_handoff.py — Indexer toàn bộ handoff data cho 28 Co-opBank modules.

Scan mỗi module folder và index:
  1. ux-review-report.md: format variant, metadata, table headers, UXP format
  2. handoff/handoff-manifest.json: keys, screen/artboard counts, phases
  3. handoff/flow_graph.json: edge count, trigger types, overlay events
  4. handoff/screen_inventory.json: screen count, OCR fields, images
  5. handoff/ddl-context.json: size, component count
  6. ui/*.png: image inventory
  7. SCR-*.md: screen spec files

Output:
  - handoff-index.json  (structured index for converter)
  - Console report       (variance analysis)

Usage:
  python3 index_handoff.py --base /path/to/COOPBANK/final/
  python3 index_handoff.py --base /path/to/COOPBANK/final/ --output /path/to/output/
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional


# ═══════════════════════════════════════════════════════════
# REPORT PARSER — Detect format variants
# ═══════════════════════════════════════════════════════════

def _detect_meta_format(lines: list[str]) -> dict:
    """Detect metadata format variant from report header lines."""
    result = {
        "h1_format": "unknown",
        "meta_style": "unknown",
        "key_language": "unknown",
        "has_tong_quan": False,
        "has_methodology": False,
        "section_order": [],
        "score_in_header": False,
    }

    h1 = ""
    for line in lines[:5]:
        if line.startswith("# "):
            h1 = line.strip()
            break

    # H1 format detection
    if " — " in h1 and " | " in h1:
        result["h1_format"] = "title-dash-pipe"  # Report — Module | Product
    elif " — " in h1 and " · " in h1:
        result["h1_format"] = "title-dash-dot"   # Audit — Module · Product
    elif " — " in h1:
        result["h1_format"] = "title-dash"        # Report — Module
    else:
        result["h1_format"] = "other"

    # Meta style detection
    has_blockquote_meta = False
    has_bold_meta = False
    has_vn_keys = False

    for line in lines[:30]:
        stripped = line.strip()
        if stripped.startswith("> **") and ":**" in stripped:
            has_blockquote_meta = True
        elif stripped.startswith("**") and ":**" in stripped and not stripped.startswith("> "):
            has_bold_meta = True
        # VN key detection
        if "**Sản phẩm:**" in stripped or "**Ngày audit:**" in stripped:
            has_vn_keys = True
        # Score in header
        if "**Simple Score:**" in stripped or "**Weighted Score:**" in stripped:
            result["score_in_header"] = True

    if has_blockquote_meta:
        result["meta_style"] = "blockquote"
    elif has_bold_meta:
        result["meta_style"] = "bold-inline"
    
    result["key_language"] = "VN" if has_vn_keys else "EN"

    # Section order detection
    section_names = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## "):
            section = stripped[3:].strip()
            section_names.append(section)

    result["section_order"] = section_names
    result["has_tong_quan"] = any("Tổng quan" in s for s in section_names)
    result["has_methodology"] = any("Methodology" in s or "Phương pháp" in s for s in section_names)

    return result


def _detect_table_format(lines: list[str]) -> dict:
    """Detect check table header format."""
    result = {
        "header_variants": [],
        "column_count": 0,
    }

    seen_headers = set()
    for line in lines:
        stripped = line.strip()
        # Match table header rows with Check + Verdict columns (real headers only)
        if stripped.startswith("|") and "Check" in stripped and "Verdict" in stripped:
            # Normalize whitespace
            cols = [c.strip() for c in stripped.split("|") if c.strip()]
            header_key = " | ".join(cols)
            if header_key not in seen_headers:
                seen_headers.add(header_key)
                result["header_variants"].append(cols)
                result["column_count"] = max(result["column_count"], len(cols))

    return result


def _detect_uxp_format(lines: list[str]) -> dict:
    """Detect UXP proposal block format."""
    result = {
        "uxp_count": 0,
        "has_emoji_severity": False,
        "has_screen_in_heading": False,
        "severity_values": [],
        "field_keys": set(),
        "uxp_ids": [],
    }

    uxp_re = re.compile(r'^####\s+(UXP-\d+)\s*·\s*(.+)$')
    field_re = re.compile(r'^\|\s*\*\*(.+?)\*\*\s*\|')

    for line in lines:
        stripped = line.strip()
        m = uxp_re.match(stripped)
        if m:
            result["uxp_count"] += 1
            result["uxp_ids"].append(m.group(1))
            sev_text = m.group(2).strip()
            if "🔴" in sev_text or "🟡" in sev_text or "⚪" in sev_text:
                result["has_emoji_severity"] = True
            # Extract clean severity
            clean_sev = sev_text.replace("🔴", "").replace("🟡", "").replace("⚪", "").strip()
            if clean_sev not in result["severity_values"]:
                result["severity_values"].append(clean_sev)

        fm = field_re.match(stripped)
        if fm:
            result["field_keys"].add(fm.group(1))

    result["field_keys"] = sorted(result["field_keys"])
    return result


def _detect_screen_sections(lines: list[str]) -> dict:
    """Detect screen section format and extract SCR-IDs."""
    result = {
        "screen_count": 0,
        "scr_ids": [],
        "has_inline_scr_id": True,
        "score_in_screen": False,
        "heading_formats": [],
    }

    heading_re = re.compile(r'^###\s+\d+\.\s+(.+)$')
    scr_meta_re = re.compile(r'^>\s*`(SCR-\w+-\d+)`')

    for i, line in enumerate(lines):
        stripped = line.strip()
        m = heading_re.match(stripped)
        if m:
            result["screen_count"] += 1
            heading_text = m.group(1)
            result["heading_formats"].append(heading_text[:80])

            # Check if SCR-ID is in heading
            scr_in_heading = re.search(r'\(`?(SCR-\w+-\d+)`?\)', heading_text)
            if scr_in_heading:
                result["scr_ids"].append(scr_in_heading.group(1))
            else:
                result["has_inline_scr_id"] = False
                # Try next line for SCR-ID
                if i + 2 < len(lines):
                    next_m = scr_meta_re.match(lines[i + 1].strip())
                    if not next_m:
                        next_m = scr_meta_re.match(lines[i + 2].strip())
                    if next_m:
                        result["scr_ids"].append(next_m.group(1))

        # Score in screen header
        if "**Score:" in stripped and "Pass:" in stripped:
            result["score_in_screen"] = True

    return result


def _extract_scores(lines: list[str]) -> dict:
    """Extract score values from report."""
    result = {
        "total_checks": None,
        "pass_count": None,
        "gap_count": None,
        "unverifiable_count": None,
        "simple_score": None,
        "weighted_score": None,
    }

    for line in lines:
        s = line.strip()
        # **Total checks:** N
        m = re.search(r'\*\*Total checks:\*\*\s*(\d+)', s)
        if m: result["total_checks"] = int(m.group(1))
        m = re.search(r'Tổng check\s*\|\s*(\d+)', s)
        if m: result["total_checks"] = int(m.group(1))
        
        # **Pass:** N | **Gap:** M
        m = re.search(r'\*\*Pass:\*\*\s*(\d+)', s)
        if m: result["pass_count"] = int(m.group(1))
        m = re.search(r'\*\*Gap:\*\*\s*(\d+)', s)
        if m: result["gap_count"] = int(m.group(1))
        m = re.search(r'\*\*Unverifiable:\*\*\s*(\d+)', s)
        if m: result["unverifiable_count"] = int(m.group(1))

        m = re.search(r'\*\*Simple Score:\*\*\s*(\d+)%', s)
        if m: result["simple_score"] = int(m.group(1))
        m = re.search(r'\*\*Weighted Score:\*\*\s*(\d+)%', s)
        if m: result["weighted_score"] = int(m.group(1))

        # Table format: | Pass | N |
        m = re.search(r'Pass\s*\|\s*(\d+)', s)
        if m and result["pass_count"] is None: result["pass_count"] = int(m.group(1))
        m = re.search(r'Gap\s*\|\s*(\d+)', s)
        if m and result["gap_count"] is None: result["gap_count"] = int(m.group(1))

    return result


# ═══════════════════════════════════════════════════════════
# HANDOFF JSON INDEXER
# ═══════════════════════════════════════════════════════════

def _index_manifest(path: Path) -> Optional[dict]:
    """Index handoff-manifest.json."""
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"error": "invalid JSON"}

    return {
        "keys": sorted(data.keys()),
        "schema_version": data.get("schema_version"),
        "screen_count": data.get("screen_count") or data.get("screens_count"),
        "artboard_count": data.get("artboard_count") or data.get("artboards_count"),
        "overlay_count": data.get("overlay_count") or data.get("overlays_detected"),
        "has_gate_results": "gate_results" in data,
        "phases_completed": data.get("phases_completed", []),
        "domain": data.get("domain"),
        "has_subsection": "subsection" in data,
        "has_output_structure": "output_structure" in data,
        # Track key name variants for variance report
        "_key_variants": {
            "screen_key": "screen_count" if "screen_count" in data else ("screens_count" if "screens_count" in data else None),
            "artboard_key": "artboard_count" if "artboard_count" in data else ("artboards_count" if "artboards_count" in data else None),
            "overlay_key": "overlay_count" if "overlay_count" in data else ("overlays_detected" if "overlays_detected" in data else None),
        }
    }


def _index_flow_graph(path: Path) -> Optional[dict]:
    """Index flow_graph.json."""
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"error": "invalid JSON"}

    edges = data.get("edges", [])
    trigger_types = set()
    has_trigger_label_vi = False
    has_trigger_label = False
    has_overlay_path = False

    for edge in edges:
        trigger_types.add(edge.get("type", "unknown"))
        if "trigger_label_vi" in edge:
            has_trigger_label_vi = True
        if "trigger_label" in edge:
            has_trigger_label = True
        if "overlay_path" in edge:
            has_overlay_path = True

    return {
        "edge_count": len(edges),
        "trigger_types": sorted(trigger_types),
        "has_overlay_events": "overlay_events" in data,
        "overlay_event_count": len(data.get("overlay_events", [])),
        "has_boundary_flags": "boundary_flags" in data,
        "has_trigger_label": has_trigger_label,
        "has_trigger_label_vi": has_trigger_label_vi,
        "has_overlay_path_in_edges": has_overlay_path,
    }


def _index_screen_inventory(path: Path) -> Optional[dict]:
    """Index screen_inventory.json."""
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"error": "invalid JSON"}

    screens = data.get("screens", [])
    screen_fields = set()
    has_ocr_full_table = False
    has_consumer_payload = False
    has_ocr_round2 = False
    total_images = 0
    screen_types = []

    for scr in screens:
        screen_fields.update(scr.keys())
        if "ocr_full_table" in scr:
            has_ocr_full_table = True
        if "consumer_payload" in scr:
            has_consumer_payload = True
        if "ocr_round2_icons" in scr:
            has_ocr_round2 = True
        total_images += len(scr.get("wireframe_images", []))
        screen_types.append(scr.get("screen_type", "unknown"))

    return {
        "screen_count": len(screens),
        "total_images": total_images,
        "screen_types": screen_types,
        "has_ocr_full_table": has_ocr_full_table,
        "has_consumer_payload": has_consumer_payload,
        "has_ocr_round2": has_ocr_round2,
        "field_keys": sorted(screen_fields),
        "scr_ids": [s.get("id") or s.get("screen_id") for s in screens],
    }


def _index_ddl_context(path: Path) -> Optional[dict]:
    """Index ddl-context.json (size + structure only)."""
    if not path.exists():
        return None
    try:
        size = path.stat().st_size
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"error": "invalid JSON"}

    return {
        "size_bytes": size,
        "size_kb": round(size / 1024, 1),
        "top_keys": sorted(data.keys()) if isinstance(data, dict) else ["(list)"],
        "component_count": len(data.get("components", [])) if isinstance(data, dict) else 0,
        "token_count": len(data.get("tokens", [])) if isinstance(data, dict) else 0,
        "guideline_count": len(data.get("guidelines", [])) if isinstance(data, dict) else 0,
    }


def _index_ui_folder(ui_dir: Path) -> dict:
    """Index UI screenshots folder."""
    if not ui_dir.exists():
        return {"exists": False, "image_count": 0, "images": []}

    images = sorted(
        f.name for f in ui_dir.iterdir()
        if f.is_file() and f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")
    )
    total_size = sum(
        f.stat().st_size for f in ui_dir.iterdir()
        if f.is_file() and f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")
    )

    return {
        "exists": True,
        "image_count": len(images),
        "images": images,
        "total_size_kb": round(total_size / 1024, 1),
    }


def _index_scr_files(module_dir: Path) -> dict:
    """Index SCR-*.md screen spec files."""
    scr_files = sorted(
        f.name for f in module_dir.iterdir()
        if f.is_file() and f.name.startswith("SCR-") and f.name.endswith(".md")
    )
    return {
        "count": len(scr_files),
        "files": scr_files,
        "scr_ids": [re.match(r"(SCR-\w+-\d+)", f).group(1) for f in scr_files if re.match(r"SCR-\w+-\d+", f)],
    }


# ═══════════════════════════════════════════════════════════
# MAIN INDEXER
# ═══════════════════════════════════════════════════════════

def index_module(module_dir: Path) -> dict:
    """Index a single module directory."""
    report_path = module_dir / "ux-review-report.md"
    handoff_dir = module_dir / "handoff"
    ui_dir = module_dir / "ui"

    entry: dict[str, Any] = {
        "module_dir": str(module_dir),
        "module_name": module_dir.name,
        "parent_section": module_dir.parent.name if module_dir.parent.name != "final" else "",
        "has_report": report_path.exists(),
        "has_handoff": handoff_dir.exists(),
        "has_ui": ui_dir.exists(),
    }

    # Report analysis
    if report_path.exists():
        lines = report_path.read_text(encoding="utf-8").splitlines()
        entry["report"] = {
            "size_bytes": report_path.stat().st_size,
            "line_count": len(lines),
            "meta_format": _detect_meta_format(lines),
            "table_format": _detect_table_format(lines),
            "uxp_format": _detect_uxp_format(lines),
            "screen_sections": _detect_screen_sections(lines),
            "scores": _extract_scores(lines),
        }

    # Handoff data
    if handoff_dir.exists():
        entry["handoff"] = {
            "manifest": _index_manifest(handoff_dir / "handoff-manifest.json"),
            "flow_graph": _index_flow_graph(handoff_dir / "flow_graph.json"),
            "screen_inventory": _index_screen_inventory(handoff_dir / "screen_inventory.json"),
            "ddl_context": _index_ddl_context(handoff_dir / "ddl-context.json"),
        }

    # UI images
    entry["ui"] = _index_ui_folder(ui_dir)

    # SCR spec files
    entry["scr_files"] = _index_scr_files(module_dir)

    return entry


def build_variance_report(index: list[dict]) -> str:
    """Generate human-readable variance analysis from index."""
    lines = []
    lines.append("=" * 80)
    lines.append("  HANDOFF INDEX REPORT — Co-opBank UX Audit Pipeline")
    lines.append(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"  Modules indexed: {len(index)}")
    lines.append("=" * 80)

    # ── Section 1: Overview ──
    lines.append("\n┌─────────────────────────────────────────────────────┐")
    lines.append("│  1. OVERVIEW                                        │")
    lines.append("└─────────────────────────────────────────────────────┘\n")

    total_screens = sum(
        m.get("report", {}).get("screen_sections", {}).get("screen_count", 0)
        for m in index
    )
    total_uxps = sum(
        m.get("report", {}).get("uxp_format", {}).get("uxp_count", 0)
        for m in index
    )
    total_images = sum(m.get("ui", {}).get("image_count", 0) for m in index)
    total_scr = sum(m.get("scr_files", {}).get("count", 0) for m in index)

    lines.append(f"  Modules:          {len(index)}")
    lines.append(f"  Total screens:    {total_screens}")
    lines.append(f"  Total UXPs:       {total_uxps}")
    lines.append(f"  Total UI images:  {total_images}")
    lines.append(f"  Total SCR-*.md:   {total_scr}")

    # ── Section 2: Module Table ──
    lines.append("\n┌─────────────────────────────────────────────────────┐")
    lines.append("│  2. MODULE SUMMARY                                  │")
    lines.append("└─────────────────────────────────────────────────────┘\n")

    lines.append(f"  {'#':>2}  {'Module':<40}  {'SCR':>3}  {'UXP':>3}  {'Gap':>3}  {'Score':>5}  {'Imgs':>4}  {'Handoff':>7}")
    lines.append("  " + "─" * 90)

    for i, m in enumerate(index, 1):
        name = m["module_name"][:38]
        scr = m.get("report", {}).get("screen_sections", {}).get("screen_count", 0)
        uxp = m.get("report", {}).get("uxp_format", {}).get("uxp_count", 0)
        scores = m.get("report", {}).get("scores", {})
        gap = scores.get("gap_count", "?")
        score = scores.get("simple_score")
        score_str = f"{score}%" if score is not None else "?"
        imgs = m.get("ui", {}).get("image_count", 0)
        handoff = "✅" if m.get("has_handoff") else "❌"
        lines.append(f"  {i:>2}  {name:<40}  {scr:>3}  {uxp:>3}  {str(gap):>3}  {score_str:>5}  {imgs:>4}  {handoff:>7}")

    # ── Section 3: Format Variance ──
    lines.append("\n┌─────────────────────────────────────────────────────┐")
    lines.append("│  3. REPORT FORMAT VARIANCE                          │")
    lines.append("└─────────────────────────────────────────────────────┘\n")

    # 3a. Metadata format
    h1_formats = {}
    meta_styles = {}
    key_langs = {}
    for m in index:
        mf = m.get("report", {}).get("meta_format", {})
        h1 = mf.get("h1_format", "?")
        h1_formats[h1] = h1_formats.get(h1, 0) + 1
        ms = mf.get("meta_style", "?")
        meta_styles[ms] = meta_styles.get(ms, 0) + 1
        kl = mf.get("key_language", "?")
        key_langs[kl] = key_langs.get(kl, 0) + 1

    lines.append("  3a. H1 Format:")
    for k, v in sorted(h1_formats.items(), key=lambda x: -x[1]):
        lines.append(f"      {k:<25} {v:>3} modules")

    lines.append("\n  3b. Metadata Style:")
    for k, v in sorted(meta_styles.items(), key=lambda x: -x[1]):
        lines.append(f"      {k:<25} {v:>3} modules")

    lines.append("\n  3c. Key Language:")
    for k, v in sorted(key_langs.items(), key=lambda x: -x[1]):
        lines.append(f"      {k:<25} {v:>3} modules")

    # 3d. Table header variants
    lines.append("\n  3d. Check Table Header Variants:")
    all_headers = set()
    for m in index:
        tf = m.get("report", {}).get("table_format", {})
        for hv in tf.get("header_variants", []):
            all_headers.add(tuple(hv))
    for hv in sorted(all_headers):
        lines.append(f"      | {' | '.join(hv)} |")

    # 3e. UXP severity format
    has_emoji = sum(1 for m in index if m.get("report", {}).get("uxp_format", {}).get("has_emoji_severity"))
    no_emoji = len(index) - has_emoji
    lines.append(f"\n  3e. UXP Severity Emoji:")
    lines.append(f"      With emoji (🔴🟡⚪):  {has_emoji:>3} modules")
    lines.append(f"      Without emoji:        {no_emoji:>3} modules")

    # 3f. UXP field keys
    all_uxp_fields = set()
    for m in index:
        for fk in m.get("report", {}).get("uxp_format", {}).get("field_keys", []):
            all_uxp_fields.add(fk)
    lines.append(f"\n  3f. UXP Field Keys (union): {sorted(all_uxp_fields)}")

    # 3g. Section ordering
    lines.append("\n  3g. Section Orders (unique):")
    section_orders = {}
    for m in index:
        so = m.get("report", {}).get("meta_format", {}).get("section_order", [])
        key = " → ".join(so) if so else "(none)"
        section_orders[key] = section_orders.get(key, 0) + 1
    for k, v in sorted(section_orders.items(), key=lambda x: -x[1]):
        lines.append(f"      [{v:>2}×] {k[:100]}")

    # 3h. Screen ID in heading
    inline_scr = sum(1 for m in index if m.get("report", {}).get("screen_sections", {}).get("has_inline_scr_id"))
    lines.append(f"\n  3h. SCR-ID in screen heading:")
    lines.append(f"      Inline (in heading):  {inline_scr:>3} modules")
    lines.append(f"      Fallback (next line): {len(index) - inline_scr:>3} modules")

    # ── Section 4: Handoff Data Variance ──
    lines.append("\n┌─────────────────────────────────────────────────────┐")
    lines.append("│  4. HANDOFF DATA VARIANCE                           │")
    lines.append("└─────────────────────────────────────────────────────┘\n")

    # 4a. Manifest key variants
    screen_keys = {}
    artboard_keys = {}
    overlay_keys = {}
    for m in index:
        manifest = m.get("handoff", {}).get("manifest")
        if manifest and "_key_variants" in manifest:
            kv = manifest["_key_variants"]
            sk = kv.get("screen_key") or "(missing)"
            screen_keys[sk] = screen_keys.get(sk, 0) + 1
            ak = kv.get("artboard_key") or "(missing)"
            artboard_keys[ak] = artboard_keys.get(ak, 0) + 1
            ok = kv.get("overlay_key") or "(missing)"
            overlay_keys[ok] = overlay_keys.get(ok, 0) + 1

    lines.append("  4a. Manifest Key Names:")
    lines.append(f"      screen count key:   {dict(sorted(screen_keys.items(), key=lambda x: -x[1]))}")
    lines.append(f"      artboard count key: {dict(sorted(artboard_keys.items(), key=lambda x: -x[1]))}")
    lines.append(f"      overlay count key:  {dict(sorted(overlay_keys.items(), key=lambda x: -x[1]))}")

    # 4b. Flow graph features
    has_overlay_events = sum(
        1 for m in index
        if m.get("handoff", {}).get("flow_graph", {}).get("has_overlay_events")
    )
    has_label_vi = sum(
        1 for m in index
        if m.get("handoff", {}).get("flow_graph", {}).get("has_trigger_label_vi")
    )
    lines.append(f"\n  4b. Flow Graph Features:")
    lines.append(f"      Has overlay_events[]:    {has_overlay_events:>3} modules")
    lines.append(f"      Has trigger_label_vi:    {has_label_vi:>3} modules")

    # 4c. Trigger types across all modules
    all_trigger_types = set()
    for m in index:
        fg = m.get("handoff", {}).get("flow_graph", {})
        for tt in fg.get("trigger_types", []):
            all_trigger_types.add(tt)
    lines.append(f"      Trigger types (union): {sorted(all_trigger_types)}")

    # 4d. Screen inventory
    has_ocr_table = sum(
        1 for m in index
        if m.get("handoff", {}).get("screen_inventory", {}).get("has_ocr_full_table")
    )
    has_consumer = sum(
        1 for m in index
        if m.get("handoff", {}).get("screen_inventory", {}).get("has_consumer_payload")
    )
    lines.append(f"\n  4c. Screen Inventory Features:")
    lines.append(f"      Has ocr_full_table:      {has_ocr_table:>3} modules")
    lines.append(f"      Has consumer_payload:    {has_consumer:>3} modules")

    # 4e. DDL context sizes
    ddl_sizes = []
    for m in index:
        ddl = m.get("handoff", {}).get("ddl_context")
        if ddl and "size_kb" in ddl:
            ddl_sizes.append(ddl["size_kb"])
    if ddl_sizes:
        lines.append(f"\n  4d. DDL Context Sizes:")
        lines.append(f"      Min: {min(ddl_sizes):.1f} KB  Max: {max(ddl_sizes):.1f} KB  Avg: {sum(ddl_sizes)/len(ddl_sizes):.1f} KB")

    # ── Section 5: Missing Data ──
    lines.append("\n┌─────────────────────────────────────────────────────┐")
    lines.append("│  5. MISSING DATA / QUALITY ISSUES                   │")
    lines.append("└─────────────────────────────────────────────────────┘\n")

    issues = []
    for m in index:
        name = m["module_name"]
        if not m.get("has_handoff"):
            issues.append(f"  ⚠️  {name}: NO handoff/ folder")
        if not m.get("has_ui") or m.get("ui", {}).get("image_count", 0) == 0:
            issues.append(f"  ⚠️  {name}: NO ui/ images")
        if m.get("scr_files", {}).get("count", 0) == 0:
            issues.append(f"  ⚠️  {name}: NO SCR-*.md files")
        
        scores = m.get("report", {}).get("scores", {})
        if scores.get("simple_score") is None:
            issues.append(f"  ⚠️  {name}: Score NOT extracted")
        if scores.get("total_checks") is None:
            issues.append(f"  ⚠️  {name}: Total checks NOT extracted")

        # SCR-ID mismatch: report vs inventory
        report_scrs = set(m.get("report", {}).get("screen_sections", {}).get("scr_ids", []))
        inv_scrs = set(m.get("handoff", {}).get("screen_inventory", {}).get("scr_ids", []) or [])
        if report_scrs and inv_scrs and report_scrs != inv_scrs:
            diff = report_scrs.symmetric_difference(inv_scrs)
            issues.append(f"  ⚠️  {name}: SCR-ID mismatch report↔inventory: {diff}")

    if issues:
        for issue in issues:
            lines.append(issue)
    else:
        lines.append("  ✅ No quality issues detected")

    # ── Section 6: Summary stats ──
    lines.append("\n┌─────────────────────────────────────────────────────┐")
    lines.append("│  6. CONVERTER REQUIREMENTS SUMMARY                  │")
    lines.append("└─────────────────────────────────────────────────────┘\n")

    lines.append(f"  Report format variants to handle:  {len(h1_formats)} H1 × {len(meta_styles)} meta × {len(key_langs)} lang = {len(h1_formats) * len(meta_styles) * len(key_langs)} combos")
    lines.append(f"  Table header variants:             {len(all_headers)}")
    lines.append(f"  Section orderings:                 {len(section_orders)}")
    lines.append(f"  Manifest key name variants:        screen={len(screen_keys)} artboard={len(artboard_keys)} overlay={len(overlay_keys)}")
    lines.append(f"  Quality issues found:              {len(issues)}")

    lines.append("\n" + "=" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Index all handoff data across UX audit modules"
    )
    parser.add_argument("--base", type=Path, required=True,
                        help="Base directory containing module folders (e.g., COOPBANK/final/)")
    parser.add_argument("--output", type=Path, default=None,
                        help="Output directory for index files (default: base dir)")
    args = parser.parse_args()

    if not args.base.exists():
        print(f"Error: Base directory not found: {args.base}", file=sys.stderr)
        sys.exit(1)

    output_dir = args.output or args.base

    # Find all modules (dirs containing ux-review-report.md)
    report_files = sorted(args.base.rglob("ux-review-report.md"))
    module_dirs = [f.parent for f in report_files]

    print(f"📂 Found {len(module_dirs)} modules with ux-review-report.md\n", file=sys.stderr)

    # Index each module
    index = []
    for i, module_dir in enumerate(module_dirs, 1):
        rel = module_dir.relative_to(args.base)
        print(f"  [{i:>2}/{len(module_dirs)}] Indexing: {rel}", file=sys.stderr)
        entry = index_module(module_dir)
        index.append(entry)

    # Write index JSON
    index_path = output_dir / "handoff-index.json"
    index_path.write_text(
        json.dumps(index, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"\n📄 Index written: {index_path}", file=sys.stderr)
    print(f"   Size: {index_path.stat().st_size / 1024:.1f} KB", file=sys.stderr)

    # Generate and print variance report
    report = build_variance_report(index)
    print("\n" + report)

    # Also save report as text file
    report_path = output_dir / "handoff-index-report.txt"
    report_path.write_text(report, encoding="utf-8")
    print(f"\n📄 Report saved: {report_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
