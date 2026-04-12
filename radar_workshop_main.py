#!/usr/bin/env python3
"""
Radar Workshop — Standalone launcher
GTA radar map tile editor (III/VC/SA/LCS/VCS/SOL)

Usage:
    python3 radar_workshop_main.py [img_file]

Requires: PyQt6, Pillow
"""
import sys
import os

# Add this repo root to path so 'apps' package is found
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Radar Workshop")
    app.setOrganizationName("X-Seti")

    from apps.components.Radar_Editor.radar_workshop import RadarWorkshop
    win = RadarWorkshop(parent=None, main_window=None)
    win.show()

    # Auto-load if path given on command line
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.isfile(path):
            win._open_file(path)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
