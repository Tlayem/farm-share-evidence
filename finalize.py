"""Publish gate — removes DRAFT status once the checklist is genuinely done.

Run this only after docs/VERIFY_CHECKLIST.md is complete and signed.

It refuses to proceed while unfilled placeholders remain, while the checklist is
unsigned, or while anything key-shaped is sitting in a tracked file. The refusal
is the feature: the way past it is to fix what it names, not to work around it.

    python finalize.py --check     # report only, change nothing
    python finalize.py             # strip DRAFT stamps if all checks pass
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent

TEXT_SUFFIXES = {".md", ".html", ".py", ".cff", ".json", ".txt", ".yml", ".yaml"}
SKIP_DIRS = {".git", "__pycache__", "data", ".venv", "venv", "node_modules"}

# Files whose job is to talk *about* placeholders and draft stamps. Scanning
# them for placeholder syntax finds the instructions, not a defect.
EXEMPT_FROM_PLACEHOLDER_SCAN = {
    "finalize.py",
    "docs/PUBLISH_GUIDE.md",
    "docs/VERIFY_CHECKLIST.md",
}

PLACEHOLDER_PATTERNS = [
    r"\[GITHUB-HANDLE\]",
    r"\[DOI[^\]]*\]",
    r"\[insert[^\]]*\]",
    r"\[TODO[^\]]*\]",
    r"\[VERIFY\]",
    r"\[n\]",
    r"\[title\]",
    r"\[URL\]",
]

SECRET_PATTERNS = [
    (r"(?i)\bapi[_-]?key\s*=\s*[\"'][^\"'\s]{12,}", "hardcoded API key"),
    (r"(?i)\btoken\s*=\s*[\"'][^\"'\s]{16,}", "hardcoded token"),
    (r"\bghp_[A-Za-z0-9]{20,}", "GitHub personal access token"),
    (r"(?i)\bpassword\s*=\s*[\"'][^\"'\s]{6,}", "hardcoded password"),
]

# The DRAFT blocks this script knows how to remove.
DRAFT_BLOCKS = [
    # CHARTER.md blockquote banner
    (r"> \*\*DRAFT — pending author verification\.\*\*.*?\n(?:>.*\n)*\n", ""),
    # README status line
    (
        r"\*\*Status: v0\.1\.0 — DRAFT, pending author verification\. Not yet "
        r"released\. No\nresearch artifacts published\.\*\*",
        "**Status: v0.1.0 — released. No research artifacts published yet; see "
        "`docs/ARTIFACTS.md`.**",
    ),
    # Site banner
    (r'\s*<div class="draft-banner">.*?</div>\n', "\n"),
]


def tracked_text_files() -> list[Path]:
    files = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(REPO_ROOT).parts):
            continue
        files.append(path)
    return sorted(files)


def check_placeholders(files: list[Path]) -> list[str]:
    problems = []
    for path in files:
        if path.relative_to(REPO_ROOT).as_posix() in EXEMPT_FROM_PLACEHOLDER_SCAN:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in PLACEHOLDER_PATTERNS:
            for match in re.finditer(pattern, text):
                line = text[: match.start()].count("\n") + 1
                problems.append(
                    f"{path.relative_to(REPO_ROOT)}:{line}  unfilled placeholder "
                    f"{match.group(0)!r}"
                )
    return problems


def check_secrets(files: list[Path]) -> list[str]:
    problems = []
    for path in files:
        if path.name == "finalize.py":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern, label in SECRET_PATTERNS:
            for match in re.finditer(pattern, text):
                line = text[: match.start()].count("\n") + 1
                problems.append(f"{path.relative_to(REPO_ROOT)}:{line}  {label}")
    return problems


def check_signed() -> list[str]:
    checklist = REPO_ROOT / "docs" / "VERIFY_CHECKLIST.md"
    if not checklist.exists():
        return ["docs/VERIFY_CHECKLIST.md is missing"]

    text = checklist.read_text(encoding="utf-8")
    problems = []

    unticked = len(re.findall(r"^- \[ \]", text, flags=re.MULTILINE))
    if unticked:
        problems.append(
            f"docs/VERIFY_CHECKLIST.md has {unticked} unticked item(s). "
            f"Tick them as you actually do them."
        )

    if re.search(r"\*\*Name:\*\*\s*_{3,}", text):
        problems.append("docs/VERIFY_CHECKLIST.md is unsigned (Name line is blank)")
    if re.search(r"\*\*Date:\*\*\s*_{3,}", text):
        problems.append("docs/VERIFY_CHECKLIST.md is undated (Date line is blank)")

    return problems


def strip_drafts(files: list[Path], dry: bool) -> list[str]:
    changed = []
    for path in files:
        if path.name == "finalize.py":
            continue
        original = path.read_text(encoding="utf-8")
        text = original
        for pattern, replacement in DRAFT_BLOCKS:
            text = re.sub(pattern, replacement, text, flags=re.DOTALL)
        if text != original:
            changed.append(str(path.relative_to(REPO_ROOT)))
            if not dry:
                path.write_text(text, encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="report only; change nothing")
    args = parser.parse_args()

    files = tracked_text_files()
    print(f"Publish gate — {len(files)} text files\n")

    blocking = []
    for label, problems in (
        ("Verification checklist", check_signed()),
        ("Unfilled placeholders", check_placeholders(files)),
        ("Secrets", check_secrets(files)),
    ):
        if problems:
            blocking.extend(problems)
            print(f"  {label}: {len(problems)} problem(s)")
            for problem in problems[:12]:
                print(f"    - {problem}")
            if len(problems) > 12:
                print(f"    … and {len(problems) - 12} more")
        else:
            print(f"  {label}: clear")
    print()

    if blocking:
        print("REFUSING to finalize. Fix the items above and run again.")
        print("Do not edit this script to get past it.")
        return 1

    changed = strip_drafts(files, dry=args.check)
    if args.check:
        print(f"Checks pass. Would strip DRAFT stamps from {len(changed)} file(s):")
    else:
        print(f"Checks pass. Stripped DRAFT stamps from {len(changed)} file(s):")
    for name in changed:
        print(f"  {name}")

    if not args.check:
        print("\nReady to publish. Follow your publish guide.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
