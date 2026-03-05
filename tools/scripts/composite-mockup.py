#!/usr/bin/env python3
"""
Composite content-only wireframe into device frame for hand-drawn mockups.

Usage:
  python composite-mockup.py <device_frame.png> <content.png> <output.png>
  python composite-mockup.py --batch <device_frame.png> <content_dir> <output_dir>

Inner content rect is computed at runtime from device image size per
handdrawn-mockup-common/DEVICE_FRAME_REUSE.md: device = full image; inner content
= padding 6% L+R, 4% T+B within image (i.e. 88%×92% of image).
"""

import argparse
import sys
from pathlib import Path

# Percentages from DEVICE_FRAME_REUSE.md (no fixed px)
DEVICE_PADDING_H = 0.06  # 6% left and right
DEVICE_PADDING_V = 0.04  # 4% top and bottom
CONTENT_WIDTH_RATIO = 1.0 - 2 * DEVICE_PADDING_H   # 0.88
CONTENT_HEIGHT_RATIO = 1.0 - 2 * DEVICE_PADDING_V  # 0.92


def composite_one(device_path: Path, content_path: Path, output_path: Path) -> None:
    try:
        from PIL import Image
    except ImportError:
        print("Pillow required: pip install Pillow", file=sys.stderr)
        sys.exit(1)

    device = Image.open(device_path).convert("RGBA")
    content = Image.open(content_path).convert("RGBA")

    # Compute inner content rect from device image size (ratio 1:2 vertical)
    w, h = device.size
    content_x = int(w * DEVICE_PADDING_H)
    content_y = int(h * DEVICE_PADDING_V)
    content_w = int(w * CONTENT_WIDTH_RATIO)
    content_h = int(h * CONTENT_HEIGHT_RATIO)

    # Resize content to inner rect size (aspect ~1:2.09)
    content_resized = content.resize((content_w, content_h), Image.Resampling.LANCZOS)

    # Paste content onto device at inner rect (overwrite pixels)
    device.paste(content_resized, (content_x, content_y))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    device.save(output_path)
    print(f"Saved {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Composite content into device frame")
    parser.add_argument("device_frame", type=Path, help="Path to device-frame.png")
    parser.add_argument("content", type=Path, help="Path to content.png or directory for batch")
    parser.add_argument("output", type=Path, help="Path to output.png or directory for batch")
    parser.add_argument("--batch", action="store_true", help="content = dir of *-content.png, output = dir for *-mockup.png")
    args = parser.parse_args()

    if args.batch:
        content_dir = args.content
        output_dir = args.output
        if not content_dir.is_dir():
            print(f"With --batch, content must be a directory: {content_dir}", file=sys.stderr)
            sys.exit(1)
        output_dir.mkdir(parents=True, exist_ok=True)
        for content_path in sorted(content_dir.glob("*-content.png")):
            base = content_path.stem.replace("-content", "")
            out_path = output_dir / f"{base}-mockup.png"
            composite_one(args.device_frame, content_path, out_path)
    else:
        composite_one(args.device_frame, args.content, args.output)


if __name__ == "__main__":
    main()
