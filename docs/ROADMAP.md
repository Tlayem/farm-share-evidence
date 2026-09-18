# Roadmap

**Everything on this page is planned work. None of it exists.** Nothing here may
be described, cited, or listed anywhere as completed, in press, or under review
until it is genuinely at that stage, at which point it moves to
`ARTIFACTS.md` with its real title, date, venue, and identifier — which will
differ from anything written here.

Items are ordered by what unblocks what, not by calendar. Dates are omitted
deliberately: a roadmap with dates on it becomes a record of missed dates, and
the programme's standards care about sequence and honesty, not schedule
theatre.

---

## Now — running from v0.1.0

**Register preservation.** Monthly snapshots of the five USDA Local Food
Directories, with provenance logged on every fetch. Running infrastructure, not
a release. This is first because it is the only item whose value depends on
when it starts: every month not captured is permanently unrecoverable.

## Next — unblocked, buildable from verified sources

**A technical audit of USDA AMS Market News coverage.** Which price reports
exist, which commodities and markets they cover, and how far back each actually
goes. This is currently not documented in one place, which makes it both a
useful public contribution and the necessary precondition for any price
transmission work the programme does later. Requires a free MARS API key.
Natural output: a technical report with a DOI.

**A farm-share baseline note.** The ERS Food Dollar Series read carefully,
including what the 2026 model revision changed and why pre- and post-revision
figures cannot be spliced. Establishes the national benchmark the programme's
disaggregated work is measured against. Natural output: a short technical note.

## Then — the certification strand

**The Organic Certification Panel.** An operation-spell dataset built from AMS
monthly INTEGRITY snapshots and historical annual lists: certification start,
status changes, certifier identity, scope, commodities, geography, exit. The
substantive difficulty is entity resolution across snapshots. Natural outputs:
an open dataset with a codebook and full reconstruction code, and a data
descriptor paper.

> **Open decision — the panel's scope, and therefore its name.** USDA-NOP
> certifies operations worldwide, and INTEGRITY carries all of them (see
> `docs/SOURCES.md`, source 2). Three options, and the choice must be made
> before construction rather than after:
>
> 1. **U.S.-located operations only.** Matches the programme's U.S. spine and
>    the name originally planned. Smallest and simplest.
> 2. **All NOP-certified operations, worldwide.** A larger and arguably more
>    valuable dataset — certification entry and exit under a single regulatory
>    regime, observed across dozens of countries, is a natural experiment that
>    a U.S.-only panel throws away. It also feeds the comparative strand
>    directly, including the cocoa-economy work.
> 3. **Both, as one panel with a country field**, documented so users can
>    subset either way. Costs almost nothing extra once the pipeline exists.
>
> Option 3 is the obvious engineering answer and option 2 is the interesting
> research one; they are compatible. Whatever is chosen, the title must say it —
> "U.S." in the name of a worldwide dataset would be a misdescription, and the
> codebook must record which certification statuses were captured, since the
> INTEGRITY search defaults to currently-certified only.

**Certification spells analysis.** Entry, exit, and survival among certified
operations — who stops being certified, and what predicts it. Depends entirely
on the panel above. Natural output: an analysis paper.

## Then — the intermediation strand

**Marketing margin and price transmission tooling.** A reusable client and
analysis layer for AMS Market News, covering marketing margins and asymmetric
price transmission. Natural outputs: an open-source package and, if it meets
the bar for real, tested, documented software, a software paper.

**A local food intermediary inventory.** Built from the preservation archive
once it has enough time depth to show entry and exit. Cannot be rushed; the
archive has to age.

> **Blocked on a prior question.** AMS rebuilt the Local Food Directories
> platform and was still recruiting businesses onto it as of the 2026 baseline
> (see `docs/SOURCES.md`, source 4). Until the launch date is established and
> the recruitment ramp is visibly over, changes in listing counts confound real
> entry and exit with platform adoption. The first task in this strand is
> therefore not analysis but **dating the platform transition** — from the site,
> from the Internet Archive's captures of the old directories, or by asking AMS
> directly. A short technical note establishing that timeline would itself be a
> useful public contribution, and it is the precondition for everything else
> here.

## Then — the credit strand

**Farm credit coverage reconciliation.** CRA, FCA and NCUA use incompatible
definitions of agricultural lending. A published crosswalk, plus a measurement
of what share of the farm credit market CRA data actually observes. Natural
outputs: a technical report with a crosswalk, and an analysis paper.

## Comparative strand

**Cocoa marketing institutions, coded by country and year.** Marketing-chain
regime coding for cocoa economies, as a check on which findings are mechanisms
and which are artefacts of U.S. institutions. Connects to the maintainer's
existing published work on cocoa certification and marketing performance.
Natural outputs: a coded dataset with a codebook, and a comparative analysis
paper.

## Continuing — public record and synthesis

**Technical comments into federal rulemaking dockets** where the programme has
measurement to contribute, filed in the maintainer's individual capacity, on
data collection and reporting provisions within its competence.

**An annual synthesis report,** once there is enough released work to
synthesise. Not before — an annual report with nothing in it is not an annual
report.

---

## Possible automation of the Local Food Directories capture

**PLANNED, NOT ATTEMPTED.** The monthly capture is taken by hand because the
API's state sweep proved substantially incomplete (30–80% of each register; see
`SOURCES.md`, 18 September 2026) and the bulk download cannot be fetched by a
script. One route remains untried: the API also accepts `x`, `y` and `radius`,
and coordinates are present for 99.3% of listings in the bulk download. A grid
of overlapping radius queries — the documented maximum is 100 miles — covering
the United States might return what the state sweep misses, since it would not
depend on whatever address-derived field the state filter uses.

It is worth trying, on one condition that is not negotiable: it may only replace
the manual download if a grid capture is compared against a same-day bulk
download and matches it. An automation that is merely *better* than the state
sweep is not good enough, because the failure mode is a silent gap. Until such a
comparison passes, the manual download remains the archive's capture and any
automated route is labelled partial.

## Dependencies worth stating plainly

- Everything in the intermediation strand needs a MARS API key.
- The certification panel is the programme's largest single build and blocks two
  downstream outputs.
- The intermediary inventory cannot be produced early at any level of effort,
  because it depends on elapsed time in the preservation archive.
- Anything described as a paper depends on peer review, which the programme does
  not control and will not pre-announce.

## How this page changes

Reviewed at each release. Items that have been built move to `ARTIFACTS.md`.
Items that turned out to be infeasible, or that a check of the sources ruled
out, are deleted with a changelog note saying why — not quietly left in place
because they were once the intention.
