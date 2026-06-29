# Contributing to YT Downloader

Thank you for considering contributing! This document walks you through everything you need to know to submit a quality pull request.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

---

## Code of Conduct

By participating in this project you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

---

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/youtube-video-downloader.git
   cd youtube-video-downloader
   ```
3. **Add the upstream remote** so you can pull future changes:
   ```bash
   git remote add upstream https://github.com/your-username/youtube-video-downloader.git
   ```
4. **Create a branch** for your work:
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## Development Setup

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Run the app in development mode:
```bash
python YouTubeVedioDownloader.py
```

---

## How to Contribute

### Bug Fixes
- Check the [Issues](https://github.com/your-username/youtube-video-downloader/issues) tab for open bugs
- Comment on the issue to let others know you're working on it
- Submit a pull request with a clear description and reference the issue number

### New Features
- Open a **Feature Request** issue first to discuss the idea
- Wait for a maintainer to approve the direction before building
- Keep features focused — one feature per pull request

### Documentation
- Typo fixes and documentation improvements are always welcome
- No approval needed for purely documentation changes

---

## Coding Standards

- **Python version:** 3.11+
- **Style:** Follow [PEP 8](https://peps.python.org/pep-0008/)
- **Type hints:** Use them for all new functions
- **Docstrings:** Add docstrings to all public functions and classes
- **Logging:** Use the existing `logger` — do not use bare `print()` statements
- **Thread safety:** Any shared state must be protected with `state_lock`

---

## Commit Messages

Use clear, descriptive commit messages in the imperative mood:

```
✅ Add playlist download support
✅ Fix progress bar not resetting after stop
✅ Update FFmpeg detection logic

❌ fixed stuff
❌ WIP
❌ changes
```

---

## Pull Request Process

1. Ensure your branch is up to date with `upstream/main`:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
2. Run the app manually and verify your change works end-to-end
3. Update `docs/CHANGELOG.md` with a note about your change under `[Unreleased]`
4. Open a Pull Request against the `main` branch
5. Fill out the Pull Request template completely
6. A maintainer will review within 3–5 business days

---

## Reporting Bugs

Use the **Bug Report** issue template. Include:
- Your OS and Python version
- Steps to reproduce the problem
- Expected vs actual behaviour
- Any error output from the terminal

---

## Suggesting Features

Use the **Feature Request** issue template. Describe:
- The problem you're trying to solve
- Your proposed solution
- Alternatives you considered

---

Thank you for helping make YT Downloader better! 🎉
