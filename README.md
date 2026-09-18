# The Farm Share Evidence Program

**Status: v0.1.0 — released. No research artifacts published yet; see `docs/ARTIFACTS.md`.**

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

There are **no datasets, no reports and no research artifacts**.
[`docs/ARTIFACTS.md`](docs/ARTIFACTS.md) is empty because there is genuinely
nothing to list, and [`docs/ROADMAP.md`](docs/ROADMAP.md) is labelled throughout
as plans rather than work.

The programme itself is deposited and has a DOI — that is the charter and the
pipeline being citable, not a research output. The distinction matters and
`docs/ARTIFACTS.md` keeps it.

```
CHARTER.md                        scope, standards, governance
BUILD_SPEC.md                     what was built and why
code/00_adopt_manual_snapshot.py  fold in browser-downloaded files
code/01_snapshot_registers.py     monthly snapshot script
code/provenance.py                fetch logging
.github/workflows/snapshot.yml    monthly API backstop, run by GitHub
.github/workflows/monthly-reminder.yml  opens the monthly capture issue
docs/SOURCES.md                   verified source register
docs/STANDARDS.md                 reproducibility and publication standards
docs/ARTIFACTS.md                 artifact index (empty by design)
docs/ROADMAP.md                   planned work, marked as planned
docs/VERIFY_CHECKLIST.md          pre-release checklist
site/index.html                   the public programme site
```

## Taking the monthly snapshot

The real snapshot is taken by hand, once a month, and it takes about five
minutes. Go to https://www.usdalocalfoodportal.com/fe/datasharing/, download all
five directories, and fold them into the archive:

```bash
python code/00_adopt_manual_snapshot.py ~/Downloads/usda --month 2026-09
```

That copies them into `data/raw/snapshots/YYYY-MM/` and writes a provenance line
per file recording that a person downloaded them, not a script. Then commit.

I would rather this were automatic, and for a while I thought it was. It is not,
and the reason matters enough to state plainly here rather than bury.

The Data Sharing page builds its files in the browser and serves them from a
`blob:` URL, so no script can fetch them. USDA also publishes an API, which a
script *can* call, and the obvious move was to use it. On 18 September 2026 I
compared the two on the same day:

| directory | full download | API sweep | API got |
|---|---|---|---|
| agritourism | 13,569 | 10,389 | 77% |
| farmers market | 7,148 | 5,687 | 80% |
| on-farm market | 4,692 | 1,401 | 30% |
| CSA | 2,002 | 753 | 38% |
| food hub | 480 | 185 | 39% |

The download matches USDA's own totals exactly. The API does not, it is not a
result cap, and I cannot tell which records it is blind to. It also returns
about nine fields where the download returns 85 to 264 — every product,
facility, season and sales-channel field lives only in the download.

So the API run still happens, monthly, from `.github/workflows/snapshot.yml`,
because a thin capture in a month I am ill or travelling beats no capture at
all. Its files are named `*.partial.csv` and say so in their provenance. Prefer
the `.xlsx` for any month that has one.

If you want to run the API route yourself you need Python 3.9 or later and a
free key from https://www.usdalocalfoodportal.com/fe/fregisterpublicapi/, saved
as a repository secret called `LOCALFOOD_API_KEY`:

```bash
git clone https://github.com/Tlayem/farm-share-evidence.git
cd farm-share-evidence
pip install requests
LOCALFOOD_API_KEY=your-key python code/01_snapshot_registers.py
```

Add `--dry-run` to see what it would do without writing anything.

One thing the API route deliberately does not keep. It returns a contact email
and phone number with every listing, and the snapshot drops both before writing.
These directories are mostly small farms, and a monthly public file of tens of
thousands of personal addresses and mobile numbers is not the same thing as
USDA's own search box, whatever the licence permits. Listings are matched
between months by `listing_id` instead, so nothing analytical is lost.
[`CHARTER.md`](CHARTER.md) standard 8 has the full reasoning. The bulk download
carries no contact fields at all, which is one more reason to prefer it.

Files you download by hand are still worth keeping. `code/00_adopt_manual_snapshot.py`
folds them into the archive and records that a person fetched them, not a script.

One thing to watch. GitHub switches off scheduled workflows after about 60 days
of quiet in a repository. Committing each month's capture resets that clock, so
the risk only arrives after a month has already been missed — but if the monthly
reminder issue does not appear on the first, that is the sign, and GitHub emails
me when it disables a workflow.

`.github/workflows/monthly-reminder.yml` opens that issue. It exists because the
capture is a thing a person has to remember to do, for years, and a risk that
size does not belong in anyone's memory.

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

See [`CITATION.cff`](CITATION.cff).

> Adesiyan, T. F. (2026). *The Farm Share Evidence Program* (Version v0.1.0)
> [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.22834814

Concept DOI [`10.5281/zenodo.22834813`](https://doi.org/10.5281/zenodo.22834813) resolves to the newest
version; version DOI [`10.5281/zenodo.22834814`](https://doi.org/10.5281/zenodo.22834814) resolves to v0.1.0
permanently. Cite the concept DOI for the programme, the version DOI when the
exact state matters.
