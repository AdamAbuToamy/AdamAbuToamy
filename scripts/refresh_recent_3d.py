#!/usr/bin/env python3
"""Refresh the compact cyber 3D profile card from the real generated GitHub SVG.

No synthetic contributions are inserted. The last 112 daily cells are retained.
"""
from pathlib import Path
import re

BASE = Path("profile-3d-contrib")
SOURCE = BASE / "profile-green-animate.svg"
DESTINATION = BASE / "recent-16-weeks.svg"

def main() -> None:
    original = SOURCE.read_text(encoding="utf-8")
    compact = DESTINATION.read_text(encoding="utf-8")
    pattern = r'<g transform="translate\(([-.\d]+) ([-.\d]+)\)">([\s\S]*?)</g>'
    groups = [m for m in re.finditer(pattern, original) if "cont-top" in m.group(3)]
    if len(groups) < 112:
        raise ValueError(f"Expected at least 112 real contribution cells, got {len(groups)}")
    recent = groups[-112:]
    active = sum('cont-top-0"' not in match.group(3) for match in recent)
    min_x = min(float(m.group(1)) for m in recent)
    min_y = min(float(m.group(2)) for m in recent)
    offset_x = round(60 - min_x * 1.25)
    offset_y = round(145 - min_y * 1.25)
    content = '\n'.join(m.group(0) for m in recent)
    start = compact.index('<g transform="translate(', compact.index('<!-- start:recent -->') if '<!-- start:recent -->' in compact else compact.index('LAST 16 WEEKS'))
    end = compact.index('</g>\n<rect x="746"', start)
    compact = compact[:start] + f'<g transform="translate({offset_x} {offset_y}) scale(1.25)">\n' + content + '\n</g>\n' + compact[end + len('</g>\n'):]
    compact = re.sub(
        r'(<text x="786" y="288"[^>]*>)[0-9]+(</text>)',
        lambda m: m.group(1) + str(active) + m.group(2),
        compact,
        count=1,
    )
    DESTINATION.write_text(compact, encoding="utf-8")
    print(f"Rendered last 112 actual days; {active} active days")

if __name__ == "__main__":
    main()
