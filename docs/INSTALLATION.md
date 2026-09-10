# Installation Guide

## Windows source setup

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m youtube_downloader
```

If PowerShell blocks script activation, run the application with the venv Python directly:

```powershell
.\.venv\Scripts\python.exe -m youtube_downloader
```

## Build a Windows executable

```powershell
pip install -r requirements-dev.txt
python build.py
```

The build uses the existing project archive as the application source and produces a windowed PyInstaller executable.

## FFmpeg setup

Install FFmpeg separately and expose `ffmpeg` on the system `PATH`, or place an appropriately licensed executable in one of the locations recognized by the application. Do not commit proprietary or unlicensed binaries to the repository.

## Verify the checkout

```powershell
python -m compileall -q src
pytest -q
```

The repository's GitHub Actions workflow performs the same source compilation and test checks on supported Python versions.
