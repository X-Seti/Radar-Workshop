#!/usr/bin/env python3
#this belongs in root /launch_radar_workshop.py - Version: 1
# X-Seti - April25 2026 - Radar Workshop - Root Launcher

import sys
from pathlib import Path

root_dir = Path(__file__).parent.resolve()
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

if __name__ == "__main__":
    try:
        print("Radar Workshop Starting...")
        from PyQt6.QtWidgets import QApplication
        from apps.components.Radar_Editor.radar_workshop import RadarWorkshop
        app = QApplication(sys.argv)
        workshop = RadarWorkshop()
        workshop.show()
        sys.exit(app.exec())
    except ImportError as e:
        print(f"ERROR: Failed to import radar_workshop: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Failed to start Radar Workshop: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)
