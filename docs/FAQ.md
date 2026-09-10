# Frequently Asked Questions

## Where are downloaded files saved?

The application saves completed downloads to the current user's `Downloads` directory.

## Is FFmpeg required?

FFmpeg is not required for every download, but it is important when the selected format needs separate video/audio streams to be merged and for MP3 extraction. The application detects FFmpeg from the system `PATH` and supported locations beside the executable.

## Why is a quality missing?

The quality selector is populated from formats available for the specific source. If a requested quality is unavailable, choose another quality shown by **Check Quality**.

## Can I cancel a download?

Yes. Click **Stop** while a download is active. The application exposes a stop endpoint and tracks the task state.

## Does the application download playlists?

The supplied implementation is configured with `noplaylist=True`, so it handles a single video rather than downloading a playlist.

## Does the application need an external server?

No external application server is required. Flask runs locally on `127.0.0.1`, and the interface is displayed in the PySide6 WebEngine desktop window.

## What does the repository contain?

The repository contains the existing project archive plus package metadata, dependency definitions, tests, build configuration, installer configuration and documentation. The `src/youtube_downloader/main.py` launcher provides a stable Python module entry point to the supplied application archive.

## Why does a download fail?

Common causes include an unavailable/private video, a temporary network or server error, an unsupported URL, rate limiting, missing FFmpeg, or a source format that is no longer available. The application converts many common yt-dlp errors into user-friendly messages.
