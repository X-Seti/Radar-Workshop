# Radar Workshop

GTA radar map tile editor — part of IMG Factory 1.6, also runs standalone.

Supports GTA III / VC / SA / LCS / VCS (PC, PS2, Xbox) and GTA SOL.

## Features
- Load radar tiles from `.img` archives (VER2 and V1+dir)
- Auto-detect game by tile count: 64=8×8, 144=12×12, 1296=36×36
- Multi-platform TXD decode: PC DXT1, PS2 PAL8/PAL4/RGB565, Xbox DXT1
- Export/import full map as PNG or BMP
- Per-tile export/import/delete via right-click
- Tile zoom tabs (press E or double-click) — all tools stay accessible
- Draw tools: pencil, line, fill, colour picker
- Transform: rotate ±90°, flip H/V
- Undo/redo (Ctrl+Z / Ctrl+Y, 20 levels)
- Copy/paste tiles
- Tile search (by name or index range e.g. 64-95)
- Map statistics (unique colours, duplicate tiles)
- 🧩 Boredom! — sliding puzzle with your radar tiles
- Recent files, window geometry remembered

## Running standalone

```bash
pip install PyQt6 Pillow
python3 radar_workshop_main.py
python3 radar_workshop_main.py /path/to/gta3.img
```

## Directory layout
```
apps/
  components/Radar_Editor/radar_workshop.py   # main application
  methods/imgfactory_svg_icons.py             # SVG icon factory
  themes/                                     # colour themes (.json)
  utils/app_settings_system.py               # theme/settings system
  core/theme_utils.py                        # dialog theming
radar_workshop_main.py                        # standalone launcher
```

## Author
X-Seti — Apr 2026
