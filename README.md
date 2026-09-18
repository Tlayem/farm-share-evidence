# The Farm Share Evidence Program

**Status: v0.1.0 — DRAFT, pending author verification. Not yet released. No
research artifacts published.**

Open measurement infrastructure for U.S. farm price realisation: certification,
intermediation, and credit. Self-funded, and everything it produces is public.

Maintainer: Taiwo Fausiyat Adesiyan, Middle Tennessee State University
· ORCID [0000-0002-2023-3624](https://orcid.org/0000-0002-2023-3624)

---

## What this is

USDA reports that farms received 11.8 cents of every dollar Americans spent on
domestically produced food in 2024. It is a careful number, and it cannot answer
the questions farmers actually ask. Does getting certified raise the share I
keep, or just my costs? If I sell through a food hub instead of a terminal
market, does more of the retail price come back to me? When credit is tight, do
I take the first offer because I cannot afford to wait?

Answering those needs data on individual operations, watched over time. A lot of
that data already exists, but only as what I call operational registers:
databases agencies keep to do their jobs, always showing the present moment. They
tell you who is certified today and which markets are open now. They were never
built to show who left, or when.

So this programme does two things. Where an agency publishes its register month
by month, I assemble those into panels. Where an agency keeps no history at all,
I take snapshots before the record disappears.

[`CHARTER.md`](CHARTER.md) sets out the full scope and the standards I hold the
work to.

## What is here at v0.1.0

The programme itself, and nothing else yet: a charter, standards, a source
register I have checked personally, a roadmap, and the script that takes the
monthly snapshots.

There are **no datasets, no software releases, no reports and no DOIs**.
[`docs/ARTIFACTS.md`](docs/ARTIFACTS.md) is empty because there is genuinely
nothing to list, and [`docs/ROADMAP.md`](docs/ROADMAP.md) is labelled throughout
as plans rather than work.

```
CHARTER.md                        scope, standards, governance
BUILD_SPEC.md                     what was built and why
code/00_adopt_manual_snapshot.py  fold in browser-downloaded files
code/01_snapshot_registers.py     monthly snapshot script
code/provenance.py                fetch logging
.github/workflows/snapshot.yml    monthly snapshot, run by GitHub
docs/SOURCES.md                   verified source register
docs/STANDARDS.md                 reproducibility and publication standards
docs/ARTIFACTS.md                 artifact index (empty by design)
docs/ROADMAP.md                   planned work, marked as planned
docs/VERIFY_CHECKLIST.md          pre-release checklist
site/index.html                   the public programme site
```

## Running the snapshot

It runs on its own. `.github/workflows/snapshot.yml` fires on the first of each
month, calls the Local Food Directories API from GitHub's servers, and commits
whatever comes back. You can also start it by hand from the Actions tab. Nothing
has to be installed.

You do need a free API key. Register at
https://www.usdalocalfoodportal.com/fe/fregisterpublicapi/ and save it as a
repository secret called `LOCALFOOD_API_KEY`. It is the only route a script can
use; the keyless download on the Data Sharing page works in a browser and
nowhere else, for reasons set out in [`docs/SOURCES.md`](docs/SOURCES.md).

To run it yourself you need Python 3.9 or later:

```bash
git clone https://github.com/Tlayem/farm-share-evidence.git
cd farm-share-evidence
pip install requests
LOCALFOOD_API_KEY=your-key python code/01_snapshot_registers.py
```

It fetches all five directories into `data/raw/snapshots/YYYY-MM/` and writes one
provenance line per file to `data/raw/PROVENANCE.txt`. Add `--dry-run` to see
what it would do without writing anything.

One thing it deliberately does not keep. USDA returns a contact email and phone
number with every listing, and the snapshot drops both before writing. These
directories are mostly small farms, and a monthly public file of tens of
thousands of personal addresses and mobile numbers is not the same thing as
USDA's own search box, whatever the licence permits. Listings are matched
between months by `listing_id` instead, so nothing analytical is lost.
[`CHARTER.md`](CHARTER.md) standard 8 has the full reasoning.

Files you download by hand are still worth keeping. `code/00_adopt_manual_snapshot.py`
folds them into the archive and records that a person fetched them, not a script.

Two things to watch. GitHub switches off scheduled workflows after about 60 days
of quiet in a repository, so check the Actions tab every couple of months. And
the snapshot script has never run against the live USDA endpoints from the
environment it was written in, which blocks those hosts, so its first real run is
mine.

## Sources

Five, all U.S. government works in the public domain: the ERS Food Dollar Series
(2024 data, model revised in 2026), AMS Organic INTEGRITY, AMS Market News
through the MARS API, the USDA Local Food Directories, and FFIEC CRA data. I
opened each one myself between 15 and 17 September 2026 and wrote down what I
found, including the places where the documentation and the data disagree.

[`docs/SOURCES.md`](docs/SOURCES.md) has the detail: access terms, the awkward
parts, and a log of who checked what and when.

Every artifact this programme releases credits the agency the data came from,
whether or not copyright requires it.

## Limitations

One researcher, no funding, founded on 15 September 2026, with an archive that
starts from empty. The registers I depend on have real identity-resolution
problems, which are written down per source in
[`docs/SOURCES.md`](docs/SOURCES.md) rather than left to be discovered later.

## Licence

Code under [MIT](LICENSE). Data and documents under [CC BY 4.0](LICENSE-DATA).
The underlying federal sources are public domain, and I credit them anyway.

## Citation

See [`CITATION.cff`](CITATION.cff). Until the first Zenodo deposit:

> Adesiyan, T. F. (2026). *The Farm Share Evidence Program: Charter, version
> 0.1.0.* https://github.com/Tlayem/farm-share-evidence
