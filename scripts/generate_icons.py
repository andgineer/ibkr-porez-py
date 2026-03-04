"""Generate app icon PNG and ICNS for Briefcase packaging.

Run once locally and commit the generated files:
    python scripts/generate_icons.py
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from ibkr_porez.gui.app_icon import export_icon_png

ICON_DIR = Path(__file__).parent.parent / "icon"
ICON_PNG = ICON_DIR / "ibkr_porez.png"
ICON_ICNS = ICON_DIR / "ibkr_porez.icns"
ICONSET_DIR = ICON_DIR / "ibkr_porez.iconset"

# Required sizes for macOS iconset (name → pixel size)
ICONSET_SIZES = {
    "icon_16x16.png": 16,
    "icon_16x16@2x.png": 32,
    "icon_32x32.png": 32,
    "icon_32x32@2x.png": 64,
    "icon_128x128.png": 128,
    "icon_128x128@2x.png": 256,
    "icon_256x256.png": 256,
    "icon_256x256@2x.png": 512,
    "icon_512x512.png": 512,
    "icon_512x512@2x.png": 1024,
}


def main() -> None:
    _ = QApplication.instance() or QApplication(sys.argv)  # must stay alive during rendering

    ICON_DIR.mkdir(parents=True, exist_ok=True)

    # Save master PNG at 1024×1024
    pixmap = export_icon_png(1024)
    if not pixmap.save(str(ICON_PNG)):
        raise RuntimeError(f"Failed to save icon to {ICON_PNG}")
    print(f"PNG saved to {ICON_PNG}")

    # Build iconset and convert to ICNS (macOS only)
    if sys.platform != "darwin":
        print("Skipping ICNS generation (macOS only)")
        return

    ICONSET_DIR.mkdir(exist_ok=True)
    for filename, size in ICONSET_SIZES.items():
        px = export_icon_png(size)
        if not px.save(str(ICONSET_DIR / filename)):
            raise RuntimeError(f"Failed to save {filename}")

    iconutil = shutil.which("iconutil")
    if not iconutil:
        raise RuntimeError("iconutil not found — run this script on macOS")
    subprocess.run(  # noqa: S603
        [iconutil, "-c", "icns", str(ICONSET_DIR), "-o", str(ICON_ICNS)],
        check=True,
    )
    shutil.rmtree(ICONSET_DIR)
    print(f"ICNS saved to {ICON_ICNS}")


if __name__ == "__main__":
    main()
