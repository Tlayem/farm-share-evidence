"""Fold browser-downloaded directory files into the archive, honestly.

THIS IS THE ARCHIVE'S CAPTURE. Run it every month.

The Data Sharing page builds its downloads in the browser (see the note at the
top of 01_snapshot_registers.py), so files obtained by clicking cannot be
obtained by a script. For a while this script was the tidy-up for files
downloaded before the automation existed. It is not that any more.

Measured 18 September 2026, the same day by both routes, the browser download
returned 13,569 agritourism / 7,148 farmers market / 4,692 on-farm market /
2,002 CSA / 480 food hub listings, matching USDA's published totals exactly. The
automated API sweep returned 77% / 80% / 30% / 38% / 39% of those, with about
nine fields against the download's 85 to 264. So the inconvenient route is the
complete one, and the convenient route is a backstop. CHARTER.md standard 9 sets
that out as a rule: completeness outranks automation.

This script copies those files into the right month's folder and writes a
provenance record that says plainly how they were obtained. It does not pretend
they were fetched programmatically. A provenance log that quietly blurs the
difference between a machine fetch and a human download is worth less than one
that records both accurately.

USAGE
-----
    python code/00_adopt_manual_snapshot.py ~/Downloads/usda --month 2026-09
    python code/00_adopt_manual_snapshot.py ~/Downloads/usda --month 2026-09 --dry-run

Files are matched to directories by name: any file whose name contains
"foodhub" is taken as the food hub directory, and so on. Anything unmatched is
reported and skipped rather than guessed at.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from provenance import log_fetch  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_ROOT = REPO_ROOT / "data" / "raw" / "snapshots"
DIRECTORIES = ["agritourism", "csa", "farmersmarket", "foodhub", "onfarmmarket"]
PORTAL = "https://www.usdalocalfoodportal.com"


def match_directory(filename: str) -> str | None:
    """Which of the five directories is this file? None if it cannot be told."""
    lowered = filename.lower()
    # Check longer names first so "onfarmmarket" is not matched by "farmersmarket".
    for directory in sorted(DIRECTORIES, key=len, reverse=True):
        if directory in lowered:
            return directory
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_dir", help="folder holding the downloaded files")
    parser.add_argument("--month", required=True,
                        help="the month these represent, as YYYY-MM "
                             "(the month they were DOWNLOADED, not today)")
    parser.add_argument("--downloaded-on", default=None,
                        help="date of download as YYYY-MM-DD, if not the "
                             "first of --month")
    parser.add_argument("--dry-run", action="store_true",
                        help="show what would happen; write nothing")
    args = parser.parse_args()

    if not re.fullmatch(r"\d{4}-\d{2}", args.month):
        return print(f"--month must look like 2026-09, got {args.month!r}") or 2

    source = Path(args.source_dir).expanduser()
    if not source.is_dir():
        return print(f"Not a folder: {source}") or 2

    destination_dir = SNAPSHOT_ROOT / args.month
    downloaded_on = args.downloaded_on or f"{args.month}-01"

    files = [p for p in sorted(source.iterdir()) if p.is_file()]
    if not files:
        return print(f"No files found in {source}") or 2

    print(f"Adopting manual snapshot for {args.month}"
          + ("   DRY RUN" if args.dry_run else ""))
    print(f"From: {source}")
    print(f"Into: {destination_dir.relative_to(REPO_ROOT)}\n")

    adopted, skipped = [], []

    for path in files:
        directory = match_directory(path.name)
        if directory is None:
            print(f"  ?  {path.name} — cannot tell which directory; skipped")
            skipped.append(path.name)
            continue

        target = destination_dir / f"{directory}{path.suffix.lower()}"
        print(f"  →  {path.name}")
        print(f"     as {target.relative_to(REPO_ROOT)}")

        if args.dry_run:
            adopted.append(directory)
            continue

        destination_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)

        record = log_fetch(
            target,
            source_url=f"{PORTAL}/fe/datasharing/",
            discovered_via="MANUAL browser download (blob: URL, built client-side)",
            note=(
                f"Local Food Directories: {directory}. "
                f"Downloaded by hand in a browser on {downloaded_on}; the Data "
                f"Sharing page assembles the file client-side and serves it from "
                f"a blob: URL, so no script could have fetched it. Original "
                f"filename: {path.name}. Saved unmodified."
            ),
        )
        print(f"     {record['bytes']:,} bytes  sha256 {record['sha256'][:12]}…")
        adopted.append(directory)

    print("\n" + "—" * 60)
    missing = [d for d in DIRECTORIES if d not in adopted]
    if args.dry_run:
        print(f"Dry run. Would adopt {len(adopted)} file(s), write nothing.")
    else:
        print(f"Adopted {len(adopted)} file(s) into {args.month}.")
    if missing:
        print(f"Not present: {', '.join(missing)} — the month is incomplete, "
              f"which is fine as long as the gap is known.")
    if skipped:
        print(f"Skipped (unrecognised): {', '.join(skipped)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
