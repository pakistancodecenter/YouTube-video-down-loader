"""Repository entry point for the supplied downloader application.

The original application is retained in the repository's existing
``youtube-video-downloader.zip`` archive. This launcher keeps the package
entry point stable while avoiding a second copy of the large embedded UI.
"""

from __future__ import annotations

import runpy
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "youtube-video-downloader.zip"


def _find_main_file(extract_dir: Path) -> Path:
    candidates = [
        "YouTubeDownLoader.py",
        "YouTubeDownLoader(1).py",
        "YouTubeVedioDownloader.py",
        "YouTubeVideoDownloader.py",
    ]
    for name in candidates:
        matches = list(extract_dir.rglob(name))
        if matches:
            return matches[0]

    for path in extract_dir.rglob("*.py"):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if "import yt_dlp" in text and "PySide6" in text:
            return path
    raise FileNotFoundError("No downloader main Python file was found in the source archive.")


def main() -> None:
    if not ARCHIVE.is_file():
        raise FileNotFoundError(
            f"The original application archive is missing: {ARCHIVE}. "
            "Keep youtube-video-downloader.zip at the repository root."
        )

    with tempfile.TemporaryDirectory(prefix="pcc-ytdl-") as tmp:
        extract_dir = Path(tmp)
        with zipfile.ZipFile(ARCHIVE) as archive:
            archive.extractall(extract_dir)
        runpy.run_path(str(_find_main_file(extract_dir)), run_name="__main__")


if __name__ == "__main__":
    main()
