@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" py -3.12 -m venv .venv
if errorlevel 1 exit /b %errorlevel%

call ".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 exit /b %errorlevel%
call ".venv\Scripts\python.exe" -m pip install -r requirements-dev.txt
if errorlevel 1 exit /b %errorlevel%
call ".venv\Scripts\python.exe" build.py
if errorlevel 1 exit /b %errorlevel%

echo Build completed successfully.
echo Output: dist\PCC YouTube Video Downloader\
endlocal
