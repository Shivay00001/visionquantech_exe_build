# VisionQuantech Exe Build

**Desktop GUI app (tkinter)** — "VisionQuantech Pro" full-stack website builder, same family as `visionquantech_builder`. Includes PyInstaller config for producing a Windows `.exe`.

## Run

```bash
python visionquantech_builder.py                            # launch the desktop GUI
pyinstaller visionquantech_builder.py --onefile --windowed  # build a Windows exe (run on Windows)
```

## Deps

```bash
pip install Pillow pyinstaller
```

## Notes

- Boot verified under `xvfb-run` (main window opens, no traceback).
- Fixed 2026-09-24: `root.state('zoomed')` is Windows-only; wrapped in try/except so the app boots on Linux too.
- Desktop app — needs a display; not a web service.
