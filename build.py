"""Build the PCC YouTube Video Downloader with PyInstaller."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SPEC = ROOT / "packaging" / "main.spec"


def main() -> None:
    if sys.version_info < (3, 10):
        raise SystemExit("Python 3.10 or newer is required.")
    if not shutil.which("pyinstaller"):
        raise SystemExit("PyInstaller is not installed. Run: pip install -r requirements-dev.txt")
    subprocess.run(
        [sys.executable, "-m", "PyInstaller", "--clean", "--noconfirm", str(SPEC)],
        cwd=ROOT,
        check=True,
    )
    print("Build complete: dist/PCC YouTube Video Downloader/")


if __name__ == "__main__":
    main()
