#!/usr/bin/env python3
"""
backfill_overlay_events.py — Backfill overlay_events[] into flow_graph.json files.

Root cause: The Phase 2 schema spec did not define overlay_events[], so the pipeline
only generated it for 1/28 modules (Đăng ký Voice). However, 20/28 modules already 
have overlay_trigger edges that contain enough data to reconstruct overlay_events[].

Strategy:
  1. Read flow_graph.json edges with type "overlay_trigger"
  2. Read screen_inventory.json for overlay screen context
  3. Read handoff-manifest.json for overlay_count
  4. Synthesize overlay_events[] from available data
  5. Inject into flow_graph.json (preserving existing data)

Usage:
  python3 backfill_overlay_events.py --base /path/to/COOPBANK/final/
  python3 backfill_overlay_events.py --base /path/to/COOPBANK/final/ --dry-run
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


# ═══════════════════════════════════════════════════════════
# OVERLAY TYPE INFERENCE
# ═══════════════════════════════════════════════════════════

# Keywords in trigger text → overlay_type mapping
OVERLAY_TYPE_PATTERNS = [
    # OTP / Auth
    (r"(?i)otp|xác thực|xác nhận|pin|biometric|face.?id|touch.?id|vân tay", "bottom_sheet"),
    # Popup / Dialog
    (r"(?i)popup|dialog|thông báo|cảnh báo|error|lỗi|fail|warning|thành công|success", "popup"),
    # Picker / Selector  
    (r"(?i)picker|chọn|danh bạ|contact|ic_contact|drop_blue|ngân hàng|filter|lọc|chip", "picker"),
    # Bottom sheet (general)
    (r"(?i)bottom.?sheet|toggle|đồng ý|confirm|menu|vertical.?dot|more|chức năng", "bottom_sheet"),
    # Modal (general)
    (r"(?i)modal|overlay|search|tìm kiếm", "modal"),
]


def infer_overlay_type(trigger_text: str) -> str:
    """Infer overlay type from trigger text using pattern matching."""
    for pattern, overlay_type in OVERLAY_TYPE_PATTERNS:
        if re.search(pattern, trigger_text):
            return overlay_type
    return "bottom_sheet"  # default fallback


def infer_overlay_name(trigger_text: str) -> str:
    """Generate a human-readable overlay name from trigger text."""
    # Clean up common suffixes
    name = trigger_text
    name = re.sub(r"\s*\(overlay_trigger\)\s*$", "", name)
    name = re.sub(r"\s*\(overlay\)\s*$", "", name)
    name = re.sub(r"\s*\(confirm\)\s*$", "", name)
    
    # Map common patterns to better names
    name_mappings = {
        "ic_contact": "Danh bạ thụ hưởng",
        "drop_blue (Ngân hàng)": "Chọn ngân hàng",
        "drop_blue": "Chọn ngân hàng",
        "touch-id icon": "Xác thực Touch ID",
        "touch-id": "Xác thực Touch ID",
        "face-id": "Xác thực Face ID",
        "avatar tap": "Thay đổi ảnh đại diện",
        "vertical-dot icon": "Menu thao tác",
        "search_focus": "Tìm kiếm",
        "chip filter tap": "Bộ lọc",
    }
    
    if name.strip() in name_mappings:
        return name_mappings[name.strip()]
    
    return name.strip()


# ═══════════════════════════════════════════════════════════
# BACKFILL LOGIC
# ═══════════════════════════════════════════════════════════

def extract_overlay_events(flow_graph: dict, screen_inv: dict | None) -> list[dict]:
    """Extract overlay_events from overlay_trigger edges."""
    events = []
    edges = flow_graph.get("edges", [])
    
    for edge in edges:
        edge_type = edge.get("type", "")
        if "overlay" not in edge_type.lower():
            continue
        
        # Extract trigger text (try multiple keys)
        trigger = (
            edge.get("trigger") 
            or edge.get("trigger_label_vi") 
            or edge.get("action") 
            or "unknown"
        )
        
        host_screen = edge.get("from_screen", edge.get("from", ""))
        
        # Build overlay event
        event = {
            "host_screen": host_screen,
            "overlay_name": infer_overlay_name(trigger),
            "overlay_type": infer_overlay_type(trigger),
            "trigger": trigger,
        }
        
        # Add trigger_icon if available
        if "trigger_icon" in edge:
            event["trigger_icon"] = edge["trigger_icon"]
            
        # Add evidence if available
        if "evidence" in edge:
            event["evidence"] = edge["evidence"]
        
        events.append(event)
    
    return events


def process_module(handoff_dir: Path, dry_run: bool = False) -> dict:
    """Process a single module's handoff directory."""
    fg_path = handoff_dir / "flow_graph.json"
    si_path = handoff_dir / "screen_inventory.json"
    
    if not fg_path.exists():
        return {"status": "skip", "reason": "no flow_graph.json"}
    
    try:
        flow_graph = json.loads(fg_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        return {"status": "error", "reason": f"invalid JSON: {e}"}
    
    # Already has overlay_events — skip
    if "overlay_events" in flow_graph and len(flow_graph["overlay_events"]) > 0:
        return {
            "status": "skip",
            "reason": "already has overlay_events",
            "existing_count": len(flow_graph["overlay_events"]),
        }
    
    # Load screen inventory for context
    screen_inv = None
    if si_path.exists():
        try:
            screen_inv = json.loads(si_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    
    # Extract overlay events from edges
    events = extract_overlay_events(flow_graph, screen_inv)
    
    if not events:
        return {"status": "skip", "reason": "no overlay_trigger edges found"}
    
    # Inject overlay_events into flow_graph
    flow_graph["overlay_events"] = events
    
    if not dry_run:
        fg_path.write_text(
            json.dumps(flow_graph, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    
    return {
        "status": "backfilled",
        "event_count": len(events),
        "events": events,
    }


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Backfill overlay_events[] into flow_graph.json files"
    )
    parser.add_argument("--base", type=Path, required=True,
                        help="Base directory containing module folders")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without writing files")
    args = parser.parse_args()
    
    if not args.base.exists():
        print(f"Error: Base directory not found: {args.base}", file=sys.stderr)
        sys.exit(1)
    
    # Find all flow_graph.json files
    fg_files = sorted(args.base.rglob("handoff/flow_graph.json"))
    
    print(f"{'🔍 DRY RUN' if args.dry_run else '🔧 BACKFILL'} — overlay_events[] into flow_graph.json")
    print(f"  Base: {args.base}")
    print(f"  Found: {len(fg_files)} flow_graph.json files")
    print(f"  Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    stats = {"backfilled": 0, "skip_existing": 0, "skip_no_data": 0, "error": 0}
    total_events = 0
    
    for fg_path in fg_files:
        handoff_dir = fg_path.parent
        module_rel = handoff_dir.parent.relative_to(args.base)
        
        result = process_module(handoff_dir, dry_run=args.dry_run)
        status = result["status"]
        
        if status == "backfilled":
            stats["backfilled"] += 1
            total_events += result["event_count"]
            prefix = "✅" if not args.dry_run else "🔍"
            print(f"  {prefix} {module_rel} → {result['event_count']} overlay events")
            for ev in result["events"]:
                print(f"      · [{ev['overlay_type']}] {ev['overlay_name']} (host: {ev['host_screen']})")
        elif status == "skip":
            reason = result["reason"]
            if "already has" in reason:
                stats["skip_existing"] += 1
                print(f"  ⏭️  {module_rel} → already has {result.get('existing_count', '?')} events")
            else:
                stats["skip_no_data"] += 1
                print(f"  ⬜ {module_rel} → {reason}")
        else:
            stats["error"] += 1
            print(f"  ❌ {module_rel} → {result.get('reason', 'unknown error')}")
    
    # Summary
    print("\n" + "=" * 70)
    print(f"  📊 Summary:")
    print(f"     Backfilled:        {stats['backfilled']}")
    print(f"     Total events:      {total_events}")
    print(f"     Already existed:   {stats['skip_existing']}")
    print(f"     No overlay data:   {stats['skip_no_data']}")
    print(f"     Errors:            {stats['error']}")
    
    if args.dry_run:
        print("\n  ⚠️  DRY RUN — no files were modified. Remove --dry-run to apply changes.")


if __name__ == "__main__":
    main()
