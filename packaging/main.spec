# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller specification for PCC YouTube Video Downloader."""

from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

ROOT = Path(SPEC).resolve().parents[1]
SRC = ROOT / "src"
ARCHIVE = ROOT / "youtube-video-downloader.zip"

hiddenimports = []
for package in ("yt_dlp", "flask", "werkzeug", "jinja2", "PySide6"):
    hiddenimports.extend(collect_submodules(package))

datas = []
for package in ("yt_dlp", "flask", "jinja2", "PySide6"):
    try:
        datas.extend(collect_data_files(package))
    except Exception:
        pass
if ARCHIVE.is_file():
    datas.append((str(ARCHIVE), "."))

analysis = Analysis(
    [str(SRC / "youtube_downloader" / "main.py")],
    pathex=[str(SRC)],
    binaries=[], datas=datas, hiddenimports=hiddenimports,
    hookspath=[], hooksconfig={}, runtime_hooks=[], excludes=[], noarchive=False,
)
pyz = PYZ(analysis.pure)
exe = EXE(
    pyz, analysis.scripts, analysis.binaries, analysis.datas, [],
    name="PCC YouTube Video Downloader", debug=False,
    bootloader_ignore_signals=False, strip=False, upx=True,
    console=False, disable_windowed_traceback=False, argv_emulation=False,
)
