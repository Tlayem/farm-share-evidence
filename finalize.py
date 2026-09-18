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
#
# Every `.` here is written `[^\n]` on purpose. These substitutions run under
# re.DOTALL, where `.` matches newlines, and on 18 September 2026 the charter
# pattern below — then written with plain `.` — matched from the banner to the
# end of the file and deleted 222 of CHARTER.md's 231 lines. The script reported
# success. Nothing but a copy taken seconds earlier saved the document.
#
# The lesson is in the guardrail under strip_drafts() rather than in this
# comment: a script that edits files irreversibly must refuse a change far
# larger than the one it was written to make.
DRAFT_BLOCKS = [
    # CHARTER.md blockquote banner — line-anchored, cannot run past the quote
    (r"> \*\*DRAFT — pending author verification\.\*\*[^\n]*\n(?:>[^\n]*\n)*\n", ""),
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


# The general net, added because the specific list above failed. On 18 September
# 2026 this gate passed a repository containing '[repository URL]' and
# '[project URL]' — neither in the list, because the list held '[URL]' exactly.
# A gate that only catches the mistakes someone thought of in advance is not a
# gate, so placeholders are now caught by shape rather than by name.
#
# Deliberately narrow in shape, not in vocabulary: a bracketed phrase that
# begins with a letter, contains a space, and holds nothing but letters,
# digits, spaces and . - _ — which is what a human writes when leaving a blank
# to fill ('[project URL]', '[your name here]', '[DOI pending first deposit]')
# and is not what code looks like. A first attempt without the space and
# character rules flagged Python slices and 'github-actions[bot]'.
GENERIC_PLACEHOLDER = re.compile(r"\[[A-Za-z][A-Za-z0-9 ._-]*\]")

# Only prose is scanned by the general net. Code legitimately contains brackets.
GENERIC_SCAN_SUFFIXES = {".md", ".html", ".cff", ".txt"}


def _is_real_placeholder(text: str, match: re.Match) -> bool:
    """Filter the bracketed things that are legitimately not placeholders."""
    token = match.group(0)
    if " " not in token:
        return False                      # '[bot]', '[MIT]' — not a blank to fill
    after = text[match.end(): match.end() + 1]
    if after in ("(", ":"):
        return False                      # markdown link, or link-reference definition
    return True


def check_placeholders(files: list[Path]) -> list[str]:
    problems = []
    seen = set()
    for path in files:
        rel = path.relative_to(REPO_ROOT).as_posix()
        if rel in EXEMPT_FROM_PLACEHOLDER_SCAN:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")

        def record(match):
            line = text[: match.start()].count("\n") + 1
            key = (rel, line, match.group(0))
            if key in seen:
                return
            seen.add(key)
            problems.append(
                f"{rel}:{line}  unfilled placeholder {match.group(0)!r}"
            )

        for pattern in PLACEHOLDER_PATTERNS:
            for match in re.finditer(pattern, text):
                record(match)
        if path.suffix.lower() in GENERIC_SCAN_SUFFIXES:
            for match in GENERIC_PLACEHOLDER.finditer(text):
                if _is_real_placeholder(text, match):
                    record(match)
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


# A DRAFT stamp is a banner: a handful of lines at most. Removing one should
# never take a meaningful bite out of a document. If a substitution wants more
# than this, the pattern has escaped its intended match and the right response
# is to refuse and say so — not to write the file and let the author discover it
# later, or never.
MAX_LINES_REMOVED = 12


def strip_drafts(files: list[Path], dry: bool) -> tuple[list[str], list[str]]:
    changed, refused = [], []
    for path in files:
        if path.name == "finalize.py":
            continue
        original = path.read_text(encoding="utf-8")
        text = original
        for pattern, replacement in DRAFT_BLOCKS:
            text = re.sub(pattern, replacement, text, flags=re.DOTALL)
        if text == original:
            continue

        removed = original.count("\n") - text.count("\n")
        if removed > MAX_LINES_REMOVED:
            refused.append(
                f"{path.relative_to(REPO_ROOT)}: a DRAFT pattern wanted to "
                f"remove {removed} lines (limit {MAX_LINES_REMOVED}). The file "
                f"was NOT written. A pattern has escaped its intended match — "
                f"fix DRAFT_BLOCKS, do not raise the limit."
            )
            continue

        changed.append(str(path.relative_to(REPO_ROOT)))
        if not dry:
            path.write_text(text, encoding="utf-8")
    return changed, refused


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

    changed, refused = strip_drafts(files, dry=args.check)

    if refused:
        print("REFUSING to strip — a pattern matched far more than a banner:\n")
        for problem in refused:
            print(f"  {problem}")
        print("\nNo file was written. Nothing is published.")
        return 1

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
