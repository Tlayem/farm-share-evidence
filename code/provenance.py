"""Provenance logging for the Farm Share Evidence Program.

Every external file the programme fetches gets one line in
data/raw/PROVENANCE.txt at the moment of retrieval. A file in data/raw/ with no
provenance line is untrusted and is not used in any analysis.

See docs/STANDARDS.md section 1.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROVENANCE_PATH = REPO_ROOT / "data" / "raw" / "PROVENANCE.txt"

HEADER = (
    "# PROVENANCE LOG — Farm Share Evidence Program\n"
    "# One line per external fetch, appended at the moment of retrieval.\n"
    "# Format: JSON Lines. Fields: ts_utc, source_url, local_path, bytes,\n"
    "#   sha256, discovered_via, note\n"
    "# Never edit this file by hand. See docs/STANDARDS.md section 1.\n"
)


def sha256_of(path: Path) -> str:
    """SHA-256 of a file, read in chunks so large files do not load into RAM."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def log_fetch(
    local_path: Path,
    source_url: str,
    discovered_via: str = "",
    note: str = "",
) -> dict:
    """Append one provenance record for a fetched file. Returns the record.

    discovered_via matters when a host rotates its download URLs between
    refreshes: recording how the URL was found lets the next person rediscover
    it when the recorded one stops resolving.
    """
    local_path = Path(local_path)
    if not local_path.exists():
        raise FileNotFoundError(
            f"Cannot log provenance for a file that does not exist: {local_path}"
        )

    record = {
        "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_url": source_url,
        "local_path": str(local_path.relative_to(REPO_ROOT))
        if REPO_ROOT in local_path.parents
        else str(local_path),
        "bytes": local_path.stat().st_size,
        "sha256": sha256_of(local_path),
        "discovered_via": discovered_via,
        "note": note,
    }

    PROVENANCE_PATH.parent.mkdir(parents=True, exist_ok=True)
    is_new = not PROVENANCE_PATH.exists()
    with open(PROVENANCE_PATH, "a", encoding="utf-8") as handle:
        if is_new:
            handle.write(HEADER)
        handle.write(json.dumps(record) + "\n")

    return record


def read_log() -> list[dict]:
    """Every provenance record, oldest first. Empty list if nothing logged yet."""
    if not PROVENANCE_PATH.exists():
        return []
    records = []
    with open(PROVENANCE_PATH, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            records.append(json.loads(line))
    return records


def summarise() -> str:
    """Counts for the artifact index. Read from the log, never typed by hand."""
    records = read_log()
    if not records:
        return "No fetches logged. The preservation archive is empty."
    months = sorted({r["ts_utc"][:7] for r in records})
    total_bytes = sum(r["bytes"] for r in records)
    return (
        f"{len(records)} files logged across {len(months)} month(s) "
        f"({months[0]} to {months[-1]}), {total_bytes:,} bytes total."
    )


if __name__ == "__main__":
    print(summarise())
