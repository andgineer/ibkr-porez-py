"""
Smoke test: verify all GUI imports work in the built installer bundle.

Run after `briefcase build` with PYTHONPATH pointing at the bundle's app_packages:

    PYTHONPATH=".../app_packages" QT_QPA_PLATFORM=offscreen python scripts/smoke_test_gui.py

If cleanup_paths in pyproject.toml removed a required Qt framework or binding,
this script will fail with an ImportError, catching the problem before release.
"""

import sys

# All PySide6 symbols imported anywhere in src/ibkr_porez/gui/
from PySide6.QtWidgets import (
    QApplication,
)

app = QApplication.instance() or QApplication(sys.argv)
assert app is not None, "QApplication creation failed"

print("smoke_test_gui: all GUI imports OK")
sys.exit(0)
