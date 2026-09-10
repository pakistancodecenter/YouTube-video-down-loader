@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
    echo Virtual environment not found. Run build.bat first.
    exit /b 1
)
call ".venv\Scripts\python.exe" -m youtube_downloader
endlocal
