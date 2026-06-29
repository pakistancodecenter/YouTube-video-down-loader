# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅ Yes             |
| < 1.0   | ❌ No              |

## Reporting a Vulnerability

**Please do NOT create a public GitHub issue for security vulnerabilities.**

If you discover a security vulnerability in this project, please follow responsible disclosure:

1. **Email us directly** at: `security@pakistancodecenter.com`
2. **Include in your report:**
   - A description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact assessment
   - Any suggested fix (optional)

### What to expect

- **Acknowledgement:** within 48 hours
- **Status update:** within 5 business days
- **Resolution:** we aim to patch critical issues within 14 days

We will credit you in the release notes (unless you prefer to remain anonymous).

## Scope

This policy applies to the `YouTubeVedioDownloader.py` source code and its dependencies as specified in `requirements.txt`.

### In scope
- Remote code execution vulnerabilities
- Path traversal or directory escape bugs
- Flask route injection or SSRF issues
- Dependency vulnerabilities with direct exploitability

### Out of scope
- Vulnerabilities in third-party tools (yt-dlp, FFmpeg, PySide6) — please report those upstream
- Issues requiring physical access to the user's machine
- Social engineering attacks

## Dependency Security

We recommend keeping dependencies up to date:

```bash
pip install --upgrade -r requirements.txt
```

Check for known vulnerabilities with:

```bash
pip install pip-audit
pip-audit
```
