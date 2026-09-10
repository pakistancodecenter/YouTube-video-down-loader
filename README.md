# PCC YouTube Video Downloader

A desktop video downloader developed by **Pakistan Code Center (PCC)** using Python, Flask, PySide6 and yt-dlp.

## Features

- Video URL input with available-format/quality probing
- Quality selection up to 4K when the source provides it
- Audio-only MP3 conversion
- Real-time progress, speed and ETA reporting
- Stop/cancel support
- Automatic saving to the user's `Downloads` folder
- Local Flask backend embedded in a PySide6 WebEngine desktop window
- FFmpeg discovery from `PATH` and common application locations
- Friendly error messages for common download failures

## Project structure

```text
.
├── .github/workflows/ci.yml
├── assets/
├── packaging/
│   ├── installer.iss
│   └── main.spec
├── src/youtube_downloader/
│   ├── __init__.py
│   ├── __main__.py
│   └── main.py
├── tests/
│   └── test_project.py
├── .gitignore
├── build.bat
├── build.py
├── project.json
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── run.bat
├── run.py
├── runtime.json
└── version.txt
```

## Installation

### Prerequisites

- Python 3.10–3.13
- pip
- FFmpeg recommended; it is required for operations that need video/audio merging or MP3 conversion

Create and activate a virtual environment:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the application:

```powershell
python -m youtube_downloader
```

or:

```text
run.bat
```

## Build a Windows executable

Install development/build dependencies:

```powershell
pip install -r requirements-dev.txt
```

Then run:

```powershell
python build.py
```

or:

```text
build.bat
```

The PyInstaller output is placed under `dist/PCC YouTube Video Downloader/`.

### FFmpeg

The application searches for FFmpeg on `PATH` and in common locations beside the executable. The repository does not commit a third-party FFmpeg binary. If you want a bundled Windows build, place an appropriately licensed `ffmpeg.exe` in the repository's `assets/` directory before building.

## Installer

The Inno Setup script is located at `packaging/installer.iss`. Build the application first, then compile the installer with Inno Setup on Windows.

## Development checks

```powershell
pip install -r requirements-dev.txt
python -m compileall -q src
pytest -q
```

GitHub Actions also runs compilation and tests on supported Python versions.

## Architecture

The supplied downloader remains centered in `src/youtube_downloader/main.py`. It contains the Flask routes, yt-dlp download engine, embedded HTML/CSS/JavaScript interface, and PySide6 desktop shell. Supporting packaging and repository files are kept separate so the application can be cloned, installed, tested and packaged without a risky rewrite of the working UI/backend implementation.

## Usage

1. Launch the application.
2. Paste a video URL.
3. Click **Check Quality** if you want the source-specific quality list.
4. Select the desired quality or MP3.
5. Click **Download**.
6. Completed files are saved to the user's Downloads folder.
7. Use **Stop** to cancel an active download.

## Legal and responsible use

This software is a downloader interface. Users are responsible for complying with applicable laws, copyright/licensing requirements and the terms of service of the websites and content they access. Download only content you are authorized to download.

## License

The repository retains the existing project license file. See `LICENSE` for the applicable terms.

## Maintainer

**Pakistan Code Center (PCC)**
