from pathlib import Path
import ast
import json

ROOT = Path(__file__).resolve().parents[1]


def test_main_source_is_valid_python():
    source_candidates = [
        ROOT / "src" / "youtube_downloader" / "main.py",
        ROOT / "YouTubeDownLoader.py",
        ROOT / "YouTubeVedioDownloader.py",
    ]
    existing = [p for p in source_candidates if p.exists()]
    assert existing, "No downloader main source file found"
    source = existing[0].read_text(encoding="utf-8")
    ast.parse(source)


def test_project_manifests_are_valid():
    for name in ("project.json", "runtime.json"):
        data = json.loads((ROOT / name).read_text(encoding="utf-8"))
        assert isinstance(data, dict)


def test_required_files_exist():
    required = [
        "README.md", "requirements.txt", "requirements-dev.txt", "pyproject.toml",
        "build.py", "build.bat", "run.bat", "version.txt",
        "packaging/main.spec", "packaging/installer.iss",
    ]
    missing = [p for p in required if not (ROOT / p).exists()]
    assert not missing, missing
