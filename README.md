<div align="center">

<img src="assets/banner.png" alt="YT Downloader Banner" width="100%"/>

<br/>

# YT Downloader

### Modern Desktop YouTube Video Downloader
**Built with Python · Flask · PySide6 · yt-dlp**

<br/>

[![Python](https://img.shields.io/badge/Python-3.11%2B-3572A5?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-Latest-ff4444?style=for-the-badge)](https://github.com/yt-dlp/yt-dlp)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![PySide6](https://img.shields.io/badge/PySide6-6.6%2B-5b8dee?style=for-the-badge&logo=qt&logoColor=white)](https://doc.qt.io/qtforpython/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blueviolet?style=for-the-badge)](https://github.com)
[![Downloads](https://img.shields.io/github/downloads/your-username/youtube-video-downloader/total?style=for-the-badge&color=orange)](https://github.com/your-username/youtube-video-downloader/releases)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)](https://github.com/your-username/youtube-video-downloader/releases)

<br/>

> A **modern, lightweight desktop application** for downloading YouTube videos at any quality from 144p to 1080p.  
> Powered by `yt-dlp`, wrapped in a beautiful `PySide6` window with a `Flask` backend API.

<br/>

[🚀 Get Started](#-installation) · [📸 Screenshots](#-screenshots) · [✨ Features](#-features) · [🗺 Roadmap](#-roadmap) · [❓ FAQ](#-faq)

</div>

---

## 📸 Screenshots

<div align="center">

### 🏠 Home Screen
<img src="assets/screenshot1.png" alt="YT Downloader - Home Screen" width="75%"/>

<br/>

### ⬇️ Downloading in Progress
<img src="assets/screenshot2.png" alt="YT Downloader - Downloading" width="75%"/>

</div>

---

## ✨ Features

| Feature | Status |
|---|---|
| HD Video Download (up to 1080p) | ✅ |
| Quality Selection: 144p · 360p · 480p · 720p · 1080p | ✅ |
| Real-time Progress Bar | ✅ |
| Download Speed Indicator | ✅ |
| Stop Download Mid-Way | ✅ |
| Multi-threaded Backend | ✅ |
| Flask REST API | ✅ |
| PySide6 Native Desktop Window | ✅ |
| FFmpeg Merge Support (video+audio) | ✅ |
| Automatic File Saving to `~/Downloads` | ✅ |
| Beautiful Modern UI | ✅ |
| Lightweight — No Electron | ✅ |
| Task Cleanup & Memory Management | ✅ |
| Concurrent Fragment Downloads | ✅ |

---

## 🚀 Installation

### Prerequisites

- **Python 3.11+** — [Download](https://www.python.org/downloads/)
- **pip** — included with Python
- **FFmpeg** *(optional but recommended for HD quality)* — see [FFmpeg Installation](#-ffmpeg-installation)

---

### 🪟 Windows

```bash
# 1. Clone the repository
git clone https://github.com/your-username/youtube-video-downloader.git
cd youtube-video-downloader

# 2. (Recommended) Create a virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python YouTubeVedioDownloader.py
```

---

### 🐧 Linux

```bash
# 1. Clone the repository
git clone https://github.com/your-username/youtube-video-downloader.git
cd youtube-video-downloader

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install system dependencies (Ubuntu/Debian)
sudo apt-get install -y python3-dev libglib2.0-0

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Run the app
python3 YouTubeVedioDownloader.py
```

---

### 🍎 macOS

```bash
# 1. Clone the repository
git clone https://github.com/your-username/youtube-video-downloader.git
cd youtube-video-downloader

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python3 YouTubeVedioDownloader.py
```

---

## 🎬 FFmpeg Installation

FFmpeg is **optional** but **highly recommended** for downloading HD content (720p, 1080p). Without it, the app falls back to pre-muxed progressive streams which may have lower quality.

### 🪟 Windows

1. Visit [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Download the latest **Windows build** (e.g., from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/))
3. Extract the archive (e.g., to `C:\ffmpeg`)
4. Add `C:\ffmpeg\bin` to your **System PATH**:
   - Open **Start** → search **Environment Variables**
   - Under **System Variables**, find `Path` → click **Edit**
   - Click **New** → enter `C:\ffmpeg\bin`
   - Click **OK** to save
5. Verify: open a new terminal and run `ffmpeg -version`

```
✅ ffmpeg version 6.x Copyright (c) ...
```

### 🐧 Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install ffmpeg -y
ffmpeg -version
```

### 🍎 macOS (Homebrew)

```bash
brew install ffmpeg
ffmpeg -version
```

> **Tip:** The app automatically detects whether FFmpeg is available at startup and adjusts download behavior accordingly. You'll see a log message if it's missing.

---

## 🎯 Usage

1. **Launch** the app — the desktop window opens automatically
2. **Paste** a YouTube URL into the input field
3. **Select** your preferred quality (144p → 1080p)
4. Click **Download** — the progress bar tracks download in real time
5. Find your video in `~/Downloads` when complete
6. Click **Stop** at any time to cancel the current download

---

## 🗺 Roadmap

### Version 1.0 ✅ (Current)
- [x] Core download engine via yt-dlp
- [x] Multi-quality selection (144p–1080p)
- [x] PySide6 native desktop window
- [x] Flask REST API backend
- [x] Real-time progress tracking
- [x] Stop/cancel downloads
- [x] FFmpeg merge support

### Version 1.1 🔜
- [ ] Playlist batch download support
- [ ] Audio-only download (MP3/AAC)
- [ ] Download history & log panel
- [ ] System tray icon support
- [ ] Custom output folder selection

### Version 1.2 🔮
- [ ] Subtitle download support
- [ ] Thumbnail preview before download
- [ ] Dark mode UI toggle
- [ ] Auto-update mechanism
- [ ] Packaging as standalone `.exe` (Windows) and `.dmg` (macOS)

---

## 🔮 Future Plans

- 🎵 **Audio Extractor** — rip MP3/AAC from any video
- 📋 **Playlist Downloader** — download entire YouTube playlists in one click
- 🌐 **Multi-platform Support** — support for Vimeo, Dailymotion, and more
- 📦 **Standalone Installer** — one-click `.exe` and `.dmg` builds via PyInstaller
- 🌙 **Dark Mode** — full dark theme with system preference detection
- 🔔 **Desktop Notifications** — notify when a download completes

---

## ❓ FAQ

See [docs/FAQ.md](docs/FAQ.md) for a full list of frequently asked questions.

**Quick answers:**

<details>
<summary>Do I need FFmpeg?</summary>

FFmpeg is optional but recommended. Without it, 720p and 1080p downloads may be of lower quality since separate video and audio streams can't be merged. The app works fine without it for 360p/480p.

</details>

<details>
<summary>Where are my downloaded files saved?</summary>

All downloads are saved to your home `~/Downloads` folder automatically. On Windows this is `C:\Users\YourName\Downloads`.

</details>

<details>
<summary>Is this app free?</summary>

Yes, completely free and open-source under the MIT License.

</details>

<details>
<summary>Can I download playlists?</summary>

Not yet — playlist support is planned for v1.1. Currently only single video URLs are supported.

</details>

<details>
<summary>Why is my 1080p download not available?</summary>

Make sure FFmpeg is installed. Without FFmpeg, the app cannot merge separate video and audio tracks required for 1080p. See the [FFmpeg Installation](#-ffmpeg-installation) section.

</details>

---

## 🤝 Contributing

Contributions are warmly welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 🔒 Security

If you discover a security vulnerability, please follow our [Security Policy](SECURITY.md) for responsible disclosure. Do **not** create a public GitHub issue for security bugs.

---

## 📜 Changelog

See [docs/CHANGELOG.md](docs/CHANGELOG.md) for a full version history.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

**Pakistan Code Center**

- 🌐 GitHub: [@your-username](https://github.com/your-username)
- 📧 Email: contact@pakistancodecenter.com
- 💬 Issues: [GitHub Issues](https://github.com/your-username/youtube-video-downloader/issues)

---

<div align="center">

Made with ❤️ by **Pakistan Code Center**

⭐ Star this repo if it helped you!

</div>
