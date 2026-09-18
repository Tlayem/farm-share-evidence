"""Register preservation harvester — USDA Local Food Directories.

WHY THIS RUNS BEFORE ANYTHING ELSE IS BUILT
-------------------------------------------
The USDA Local Food Directories (farmers markets, CSAs, food hubs, on-farm
markets, agritourism) are published as current-state listings. Entries that
lapse are removed, not retired, and there is no public historical archive. Every
month that passes without a snapshot is a month of entry and exit that no future
researcher can reconstruct at any price.

So this script is the programme's first commitment and it does not wait for the
analysis to be ready. Run it monthly. The archive's value is set by when it
started, not by how good the eventual paper is.

THE API IS THE ONLY AUTOMATABLE ROUTE — AND WHY
-----------------------------------------------
The Data Sharing page's download button cannot be used by a script. Verified on
16 September 2026: clicking it yields a `blob:` URL, which means the page runs
JavaScript that assembles the Excel file inside the browser and hands it over
locally. No server address returns that file, and the blob URL dies with the
tab. A human with a browser can download the directories; a program cannot,
short of driving a real browser.

So the API route is the default and the one the monthly workflow uses. It needs
a free key, which is a small price for an endpoint that is documented,
supported, and designed to be called by software.

The `--route csv` path is kept because USDA may yet publish real static files,
and if it does, this script will find and archive them. Today it will fail, and
its failure message says why.

USAGE
-----
    python code/01_snapshot_registers.py --dry-run      # show the plan, write nothing
    LOCALFOOD_API_KEY=xxxx python code/01_snapshot_registers.py
    python code/01_snapshot_registers.py --route csv    # will fail today; see above

A free API key: https://www.usdalocalfoodportal.com/fe/fregisterpublicapi/
Keys go in the environment, never in this file. See docs/STANDARDS.md § 10.

Files downloaded by hand in a browser are still worth keeping. Fold them into
the archive with honest provenance using code/00_adopt_manual_snapshot.py.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("This script needs the requests library.  pip install requests")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from provenance import log_fetch  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_ROOT = REPO_ROOT / "data" / "raw" / "snapshots"

PORTAL = "https://www.usdalocalfoodportal.com"
DIRECTORIES = ["agritourism", "csa", "farmersmarket", "foodhub", "onfarmmarket"]

# The API requires a location parameter on every call, so national coverage means
# iterating jurisdictions. States, DC, and the inhabited territories.
JURISDICTIONS = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
    "DC", "PR", "VI", "GU", "AS", "MP",
]

# Identified-crawler format. Still says plainly who this is and links to the
# programme, but uses the "Mozilla/5.0 (compatible; Name/version; +url)" shape
# that well-behaved bots have used for decades and that firewalls recognise.
# A bare custom token is the polite convention and is widely rejected by
# default WAF rules; this is the same honesty in a form that gets through.
USER_AGENT = (
    "Mozilla/5.0 (compatible; FarmShareEvidenceProgram/0.1.0; "
    "+https://tlayem.github.io/farm-share-evidence/site/)"
)
TIMEOUT = 60
PAUSE_SECONDS = 1.0  # courtesy delay between requests to a public service

# Fields dropped before anything is written to disk.
#
# This is the one place where this archive deliberately does not preserve what
# the agency published, so it is stated plainly rather than buried. USDA's API
# returns a contact email and telephone number for every listing. Most listings
# are small farms, where the "business" email is a personal address and the
# "business" telephone is a mobile.
#
# USDA publishes them behind a search box, one listing at a time. A public
# repository holding a downloadable file of tens of thousands of them, renewed
# monthly and kept for ever, is a different exposure, and the people who would
# bear the cost of it are the farmers this programme exists to serve.
#
# Nothing analytical is lost. Listings are tracked across snapshots by
# listing_id, which USDA assigns and which is stabler than an email address
# anyway. Every field bearing on certification, intermediation, credit, market
# channel or location is kept.
#
# Anyone who needs the contact fields can obtain them from USDA directly, on
# the same terms this programme did. See CHARTER.md section 4 and
# docs/STANDARDS.md section 10.
REDACTED_FIELDS = ("contact_email", "contact_phone")


def snapshot_dir(when: datetime) -> Path:
    return SNAPSHOT_ROOT / when.strftime("%Y-%m")


def session() -> requests.Session:
    s = requests.Session()
    s.headers.update({
        "User-Agent": USER_AGENT,
        # Some firewalls reject requests that send no Accept headers at all.
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
    })
    return s


# --------------------------------------------------------------------------
# Route 1: bulk CSV, no API key
# --------------------------------------------------------------------------

DATA_SHARING_URL = f"{PORTAL}/fe/datasharing/"


def discover_csv_url(sess: requests.Session, directory: str) -> tuple[str, str]:
    """Find a directory's CSV download link on the Data Sharing page.

    The downloads live on /fe/datasharing/, which states: "The CSV endpoint
    allows users to download the entire collection of data from the USDA local
    food directory. The separator for the dataset is |." Confirmed working
    without an API key on 16 September 2026.

    Returns (url, how_it_was_discovered). Scraping rather than hardcoding means
    a URL change breaks nothing while the link is still on the page, and the
    provenance log records how it was found so a future run can rediscover it.
    See docs/STANDARDS.md § 1.
    """
    pages = [DATA_SHARING_URL, f"{PORTAL}/fe/fdirectory_{directory}/"]
    tried = []

    for page_url in pages:
        try:
            response = sess.get(page_url, timeout=TIMEOUT)
            response.raise_for_status()
        except Exception as exc:  # noqa: BLE001 — try the next page
            tried.append(f"{page_url} ({type(exc).__name__})")
            continue

        # Prefer a link naming this directory; fall back to any csv/export link.
        patterns = [
            rf'href=["\']([^"\']*{re.escape(directory)}[^"\']*)["\']',
            r'href=["\']([^"\']*(?:csv|export|download)[^"\']*)["\']',
        ]
        for pattern in patterns:
            for href in re.findall(pattern, response.text, flags=re.IGNORECASE):
                if not re.search(r"csv|export|download", href, re.IGNORECASE):
                    continue
                url = href if href.startswith("http") else PORTAL + href
                return url, f"link scraped from {page_url}"
        tried.append(f"{page_url} (no matching link)")

    raise LookupError(
        f"No static download link found for '{directory}'. Tried: "
        f"{'; '.join(tried)}.\n"
        f"    This is expected. As of 16 September 2026 the Data Sharing page\n"
        f"    builds the file in the browser with JavaScript and serves it from a\n"
        f"    blob: URL, so there is no server address for a script to fetch.\n"
        f"    Use the API route instead: register a free key at\n"
        f"    {PORTAL}/fe/fregisterpublicapi/ and run with --route api.\n"
        f"    If USDA has since published real static files, pass one with --url."
    )


def detect_format(payload: bytes) -> tuple[str, str]:
    """Identify what the server actually sent. Returns (extension, description).

    The Data Sharing page calls these "CSV" with a `|` separator, but observed
    downloads on 16 September 2026 were genuine .xlsx workbooks. Rather than
    trust either the page text or the filename, look at the bytes: an .xlsx is a
    ZIP container and starts with PK\\x03\\x04.
    """
    if payload[:4] == b"PK\x03\x04":
        return "xlsx", "Excel workbook (ZIP container)"
    head = payload[:8192].decode("utf-8", errors="replace")
    if "|" in head:
        return "csv", "pipe-delimited text"
    if "," in head:
        return "csv", "comma-delimited text"
    return "dat", "unrecognised format — inspect before use"


def fetch_bulk(sess: requests.Session, directory: str, out_dir: Path,
               explicit_url: str | None, dry_run: bool) -> Path | None:
    """Fetch one directory and save the bytes exactly as served.

    Deliberately does not parse or convert. The archive's value is that it holds
    what the agency actually published, byte for byte, with a hash to prove it.
    Parsing belongs downstream, where it can be redone when the reading is found
    to be wrong.
    """
    if dry_run:
        # Dry run must not touch the network, so discovery is described, not done.
        planned = explicit_url or f"(discover download link on {DATA_SHARING_URL})"
        print(f"    would fetch {planned}")
        print(f"    would write {out_dir.relative_to(REPO_ROOT)}/{directory}.<detected>")
        return None

    if explicit_url:
        url, discovered_via = explicit_url, "supplied with --url"
    else:
        url, discovered_via = discover_csv_url(sess, directory)

    response = sess.get(url, timeout=TIMEOUT)
    response.raise_for_status()

    extension, description = detect_format(response.content)
    destination = out_dir / f"{directory}.{extension}"
    out_dir.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(response.content)

    record = log_fetch(
        destination,
        source_url=url,
        discovered_via=discovered_via,
        note=f"Local Food Directories bulk download: {directory}. "
             f"Format as served: {description}. Saved unmodified. "
             f"Current-state register; lapsed listings are removed, not retired.",
    )
    print(f"    {record['bytes']:,} bytes  {description}  "
          f"sha256 {record['sha256'][:12]}…")
    return destination


# --------------------------------------------------------------------------
# Route 2: the public API, needs a free key
# --------------------------------------------------------------------------

def fetch_via_api(sess: requests.Session, directory: str, out_dir: Path,
                  api_key: str, dry_run: bool) -> Path | None:
    """Sweep the API state by state. THIS DOES NOT CAPTURE THE WHOLE REGISTER.

    Measured 18 September 2026 against the same day's bulk download:

        directory        bulk     API    API got
        agritourism    13,569  10,389        77%
        farmersmarket   7,148   5,687        80%
        onfarmmarket    4,692   1,401        30%
        csa             2,002     753        38%
        foodhub           480     185        39%

    The bulk download matches USDA's own published totals exactly, with no
    duplicate identifiers, so the shortfall is the API's. It is not a result
    cap: no per-query limit from 50 to 1,000, applied to the real per-state
    distribution, reproduces this pattern, and for CSAs and food hubs the API
    returned fewer rows than a limit of 50 would have. The `state` parameter is
    evidently filtering on some field other than the free-text address, and
    populated for only part of the register — which cannot be swept around,
    because there is no way to see which records it is blind to.

    The API also returns about nine fields where the bulk download returns
    85 to 264, including every product, facility, season, production-method and
    sales-channel field the analysis actually needs.

    So this route is kept only as a backstop: an imperfect automatic capture in
    a month when nobody clicks is worth more than no capture at all. Its output
    is named `.partial.csv` and says so in its provenance line. The complete
    capture is the browser download, adopted with
    code/00_adopt_manual_snapshot.py. See CHARTER.md standard 9.
    """
    endpoint = f"{PORTAL}/api/{directory}/"
    # The filename itself carries the warning. Someone who finds this file in
    # ten years, with no documents to hand, still knows what they have.
    destination = out_dir / f"{directory}.partial.csv"

    if dry_run:
        print(f"    would call {endpoint} for {len(JURISDICTIONS)} jurisdictions")
        print(f"    would write {destination.relative_to(REPO_ROOT)}")
        return None

    rows: list[dict] = []
    seen: set[str] = set()
    failures: list[str] = []          # queries that did not get an answer
    empty: list[str] = []             # queries answered "nothing here"
    redacted: set[str] = set()        # fields dropped, recorded in provenance
    diagnostics: list[str] = []  # first few full failures, for debugging

    for code in JURISDICTIONS:
        try:
            response = sess.get(
                endpoint,
                # USDA's documentation shows this parameter lower-case
                # (&state=mi), and the API rejects upper-case codes.
                params={"apikey": api_key, "state": code.lower()},
                timeout=TIMEOUT,
            )
            response.raise_for_status()
            payload = response.json()
        except requests.HTTPError as exc:
            status = exc.response.status_code if exc.response is not None else "?"
            failures.append(f"{code}: HTTP {status}")
            if len(diagnostics) < 3:
                body = (exc.response.text[:300] if exc.response is not None else "")
                diagnostics.append(
                    f"      {code} → HTTP {status}\n"
                    f"      url:  {exc.response.url if exc.response is not None else endpoint}\n"
                    f"      body: {body!r}"
                )
            continue
        except Exception as exc:  # noqa: BLE001 — record and continue
            failures.append(f"{code}: {type(exc).__name__}")
            if len(diagnostics) < 3:
                diagnostics.append(f"      {code} → {type(exc).__name__}: {exc}")
            continue

        listings = payload.get("data", payload) if isinstance(payload, dict) else payload

        # A jurisdiction holding no listings comes back as {"data": ""} — an
        # empty string, not an empty list. Observed on 18 September 2026 in all
        # five directories: Guam in every one, Puerto Rico in three, and five
        # states in the food hub directory. That is an answer, not a failure,
        # and the archive must not confuse the two. A reader who finds no food
        # hubs in Wyoming needs to know the register was asked and said none —
        # otherwise a silent gap and a genuine zero look identical.
        if listings == "" or listings is None or listings == []:
            empty.append(code)
            time.sleep(PAUSE_SECONDS)
            continue

        if not isinstance(listings, list):
            failures.append(f"{code}: unexpected payload shape")
            if len(diagnostics) < 3:
                diagnostics.append(
                    f"      {code} → unexpected shape: {str(payload)[:300]!r}"
                )
            continue

        for item in listings:
            # listing_id where present; otherwise a composite key, so that a
            # jurisdiction appearing in two queries is not double-counted.
            key = str(
                item.get("listing_id")
                or item.get("id")
                or f"{item.get('listing_name','')}|{item.get('location_address','')}"
            )
            if key in seen:
                continue
            seen.add(key)
            # Drop the contact fields before the row is kept, so they are never
            # written to disk at all — not written and then cleaned, which would
            # leave them in the file's history. See REDACTED_FIELDS above.
            for field in REDACTED_FIELDS:
                if field in item:
                    item.pop(field)
                    redacted.add(field)
            item["_fsep_query_state"] = code
            rows.append(item)

        time.sleep(PAUSE_SECONDS)

    if not rows and not failures:
        # Every jurisdiction answered, and every answer was empty. That is not
        # a transport problem, so do not write a file with no columns and call
        # it a snapshot — something has changed at the source.
        raise RuntimeError(
            f"No rows for {directory}, and no query failed: all "
            f"{len(empty)} jurisdictions answered empty. Either the directory "
            f"has been emptied or retired at the source, or the query shape "
            f"has changed. Check {endpoint} in a browser before running again."
        )

    if not rows:
        # Summarise by distinct reason rather than listing 56 identical lines.
        from collections import Counter
        reasons = Counter(f.split(": ", 1)[1] for f in failures)
        summary = ", ".join(f"{reason} ×{n}" for reason, n in reasons.most_common())
        detail = ("\n" + "\n".join(diagnostics)) if diagnostics else ""
        raise RuntimeError(
            f"No rows for {directory}. All {len(failures)} jurisdiction queries "
            f"failed: {summary}.{detail}\n"
            f"      HTTP 401/403 means the key is wrong or not being accepted; "
            f"check the LOCALFOOD_API_KEY secret for stray spaces.\n"
            f"      HTTP 400 means the query parameters are wrong.\n"
            f"      HTTP 429 means too many requests — slow the script down."
        )

    fieldnames = sorted({k for row in rows for k in row.keys()})

    # Belt and braces. If a redacted field reaches this point the file must not
    # be written at all: a snapshot committed to a public repository cannot be
    # unpublished, so the failure has to happen before the write, not after.
    leaked = [f for f in REDACTED_FIELDS if f in fieldnames]
    if leaked:
        raise RuntimeError(
            f"Refusing to write {destination.name}: redacted field(s) "
            f"{', '.join(leaked)} survived into the output columns. "
            f"Fix the redaction in fetch_via_api before running again."
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    with open(destination, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="|")
        writer.writeheader()
        writer.writerows(rows)

    # Two facts a future reader needs, and they are not the same fact:
    # which jurisdictions held nothing, and which were never answered. The
    # first is data. The second is a hole in the archive. Recording them
    # together, or recording only a count, would let a genuine zero and a
    # failed query look alike for as long as this file exists.
    empty_note = (
        f"Jurisdictions answering empty ({len(empty)}): {', '.join(empty)}."
        if empty else "No jurisdiction answered empty."
    )
    if failures:
        from collections import Counter
        reasons = Counter(f.split(": ", 1)[1] for f in failures)
        failed_note = (
            f"NOT ANSWERED ({len(failures)}): "
            + ", ".join(f.split(": ", 1)[0] for f in failures)
            + " (" + "; ".join(f"{r} x{n}" for r, n in reasons.most_common()) + ")."
            + " Coverage for these jurisdictions is unknown, not zero."
        )
    else:
        failed_note = f"All {len(JURISDICTIONS)} jurisdictions answered."

    # The one departure from byte-for-byte fidelity, recorded in every line of
    # the log so it can never be discovered by surprise.
    redaction_note = (
        f"NOT A COMPLETE COPY: field(s) {', '.join(sorted(redacted))} were "
        f"dropped before writing, by policy (see REDACTED_FIELDS in "
        f"code/01_snapshot_registers.py)."
        if redacted else
        f"No fields redacted; none of {', '.join(REDACTED_FIELDS)} were present."
    )

    record = log_fetch(
        destination,
        source_url=endpoint,
        discovered_via=f"API, iterated {len(JURISDICTIONS)} jurisdictions",
        note=f"PARTIAL CAPTURE — NOT THE WHOLE REGISTER. Local Food "
             f"Directories API state sweep: {directory}, {len(rows)} unique "
             f"listings. Measured 18 Sept 2026, this route returns 30-80% of "
             f"the register depending on directory, and about nine fields "
             f"where the bulk download returns 85-264. The complete capture "
             f"for any month is the browser download adopted via "
             f"code/00_adopt_manual_snapshot.py; use that in preference to "
             f"this file wherever both exist. See CHARTER.md standard 9 and "
             f"docs/SOURCES.md. {failed_note} {empty_note} {redaction_note} "
             f"Current-state register; no public archive.",
    )
    print(f"    {len(rows):,} listings  {record['bytes']:,} bytes")
    if redacted:
        print(f"      redacted: {', '.join(sorted(redacted))}")
    if empty:
        print(f"      no listings in: {', '.join(empty)}")
    if failures:
        print(f"      NOT ANSWERED: {'; '.join(failures)}")
        if diagnostics:
            print("\n".join(diagnostics))
    return destination


# --------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--route", choices=["api", "csv"], default="api",
                        help="api (default; needs LOCALFOOD_API_KEY) or csv "
                             "(browser-only, see the note in this file)")
    parser.add_argument("--url", "--csv-url", dest="csv_url", default=None,
                        help="explicit download URL, skipping link discovery")
    parser.add_argument("--only", default=None,
                        help="one directory only, for testing")
    parser.add_argument("--dry-run", action="store_true",
                        help="show what would happen; write nothing")
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    out_dir = snapshot_dir(now)
    directories = [args.only] if args.only else DIRECTORIES
    if args.only and args.only not in DIRECTORIES:
        return print(f"Unknown directory: {args.only}. Choose from {DIRECTORIES}") or 2

    api_key = os.environ.get("LOCALFOOD_API_KEY", "")
    if args.route == "api" and not api_key:
        print("Route 'api' needs LOCALFOOD_API_KEY in the environment.")
        print("Free key: https://www.usdalocalfoodportal.com/fe/fregisterpublicapi/")
        return 2

    print(f"Farm Share Evidence Program — register snapshot")
    print(f"Snapshot month: {now.strftime('%Y-%m')}   route: {args.route}"
          + ("   DRY RUN" if args.dry_run else ""))
    print()

    sess = session()
    written, failed = [], []

    for directory in directories:
        print(f"  {directory}")
        try:
            if args.route == "api":
                path = fetch_via_api(sess, directory, out_dir, api_key, args.dry_run)
            else:
                path = fetch_bulk(sess, directory, out_dir, args.csv_url,
                                      args.dry_run)
            if path:
                written.append(path)
        except Exception as exc:  # noqa: BLE001 — report every failure, never swallow
            print(f"    FAILED: {type(exc).__name__}: {exc}")
            failed.append((directory, f"{type(exc).__name__}: {exc}"))
        print()

    print("—" * 60)
    if args.dry_run:
        print("Dry run. Nothing fetched, nothing written, nothing logged.")
        return 0

    print(f"Wrote {len(written)} of {len(directories)} registers to "
          f"{out_dir.relative_to(REPO_ROOT)}")
    if failed:
        print(f"\n{len(failed)} failed:")
        for directory, reason in failed:
            print(f"  {directory}: {reason}")
        if args.route == "api":
            print("\nEvery directory uses the same key and the same query shape, so")
            print("when all five fail identically the cause is the key or the")
            print("parameters, not the data. Read the HTTP status above.")
        else:
            print("\nThe keyless download is browser-only (blob: URL). Use --route api.")
        return 1

    print("Provenance logged to data/raw/PROVENANCE.txt")

    if args.route == "api":
        print()
        print("!" * 60)
        print("THESE ARE PARTIAL CAPTURES. The API state sweep returns roughly")
        print("30-80% of each register, and about nine fields where the bulk")
        print("download returns 85-264. Files are named *.partial.csv for that")
        print("reason.")
        print()
        print("The complete capture is the browser download:")
        print(f"  {PORTAL}/fe/datasharing/")
        print("Download all five directories, then:")
        print("  python code/00_adopt_manual_snapshot.py <folder> --month "
              f"{now.strftime('%Y-%m')}")
        print("Do that at least once a month. This automated run exists so a")
        print("month is never lost entirely, not to replace it.")
        print("!" * 60)

    print("\nNext: commit the provenance log, and update the snapshot count in")
    print("docs/ARTIFACTS.md by reading it from the log — never by hand.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
