# The Farm Share Evidence Program

**Charter, version 0.1.0 — 15 September 2026**

> **DRAFT — pending author verification.** This charter has not yet been
> reviewed and signed off by the author. It is not published, cited, or
> circulated until `docs/VERIFY_CHECKLIST.md` is complete. Run
> `python finalize.py` to remove this banner once it is.

Founder and maintainer: Taiwo Fausiyat Adesiyan (ORCID
[0000-0002-2023-3624](https://orcid.org/0000-0002-2023-3624)), Middle Tennessee
State University, Murfreesboro, Tennessee, USA.

---

## 1. Purpose

The Farm Share Evidence Program is open measurement infrastructure for U.S.
farm price realisation: how much of the value of what a farm produces actually
reaches the farm, and what determines the answer.

It exists because the question is asked constantly — by producers, cooperative
managers, extension agents, and legislators — and answered, almost always, with
a single national average that was not built to bear the weight.

## 2. The measurement problem

USDA's Economic Research Service reports that U.S. farms received 11.8 cents of
each dollar consumers spent on domestically produced food in 2024, down from
12.1 cents in 2023. The remaining 88.2 cents pays for everything that happens
after the farm gate. That series is carefully constructed and it is the right
instrument for the question it was built to answer: the aggregate division of
the national food dollar between farm and marketing sectors.

Read only that far and you would conclude that farmers lost ground in 2024. ERS
publishes the decomposition that shows why you would be wrong to stop there. The
farm share of food bought for the home *rose*, from 18.4 cents to 18.5. The farm
share of food bought away from home fell, from 7.5 cents to 7.1. What moved the
national figure was where people ate: spending on food away from home grew 4.2
per cent to $1.27 trillion while food-at-home spending grew 1.4 per cent to $901
billion, and a farmer receives about seven cents of a restaurant dollar against
about eighteen and a half cents of a grocery dollar. "The farm share is falling"
is therefore, in large part, a sentence about restaurant habits rather than
about farmers losing ground in any market they actually sell into. Those two
readings call for entirely different responses, and a single national ratio
cannot tell them apart.

It is worth noticing what happened to that number in 2026. ERS revised the model
and, as part of the revision, broadened the definition of food to include
bottled water, soft drinks, coffee, tea and beverage materials — items whose
supply chains use relatively few farm commodities. That change alone restated
the 2024 farm share from 12.3 cents to 11.8, and 2023 from 12.5 to 12.1. Half a
cent moved because of a decision about what counts as food, not because of
anything that happened on a farm. This is not a criticism of ERS, whose
reasoning is published and sound. It is the point: headline measures are
constructions, and a programme that wants to say anything durable about farm
price realisation has to understand how its instruments are built.

What the aggregate cannot do is answer the question in the form producers
actually ask it. Does certification raise the share I realise, or only my costs?
If I sell through a food hub instead of a terminal market, does more of the
retail price come back to me? When credit is tight, do I take the first offer
because I cannot afford to hold the crop? Those are questions about mechanisms
operating between the farm gate and the consumer, and answering them requires
operation-level data observed over time — not a national ratio.

Much of that data exists. It exists as **operational registers**: administrative
compliance databases that agencies maintain to do their jobs, not to support
research. A register tells you who is certified organic *today*, which farmers
markets are operating *now*, which retailers are authorised *at present*. It is
a lookup, maintained in the present tense. Entry, exit, survival, and churn —
the dynamics that determine whether a mechanism actually works for producers —
are not what a register is for, and mostly not what it preserves.

## 3. What the programme contributes

Two things, and it is worth keeping them distinct because they are different
kinds of work with different urgency.

**Reconstruction.** Where an agency does publish its register over time, the raw
material for a longitudinal panel exists but the panel does not. USDA AMS
publishes monthly full-dataset snapshots of the Organic INTEGRITY Database and
historical annual lists of certified operations. Nobody has assembled them into
an operation-spell panel — certification start, status changes, certifier
identity, scope, exit — with identity resolved consistently across snapshots.
That resolution is the hard part and it is the contribution: an operation that
changes certifier, renames itself, or is recorded differently in two consecutive
months is one operation, and only careful entity resolution makes it so.

**Preservation.** Where an agency does not archive its register, the data is
being lost continuously and cannot be recovered retroactively. The USDA Local
Food Directories are published as current-state listings with no public
historical archive. Every month that passes without a snapshot is a month of
entry and exit that no future researcher can reconstruct at any price. This
programme therefore begins snapshotting on the day it is founded, before it
has published anything, because the value of a preservation archive is set
entirely by when it started and not at all by how good the eventual analysis is.

The programme's first commitment is the boring one: capture the registers now,
log provenance on every fetch, and keep the archive whether or not the papers
ever get written.

## 4. Scope

Three measurement strands, each a mechanism standing between farm and consumer.

**Certification.** Whether third-party certification changes what producers
realise, who enters certification, and — the question the entry literature
mostly skips — who stops. Primary register: USDA Organic INTEGRITY.

**Intermediation.** How the spread between farm gate and retail is divided, how
it moves, and whether marketing channel choice changes the producer's share.
Primary sources: USDA AMS Market News price reports; the Local Food Directories
as a register of intermediaries; SNAP-authorised retailers as a register of
food-access infrastructure. Platform and contract intermediation — where the
take rate is the marketing margin, set by a firm rather than discovered in a
market — belongs in this strand.

**Credit.** Whether credit access determines a producer's capacity to hold
product, invest in certification, or bargain at all. Primary sources: FFIEC CRA
small farm loan data, alongside Farm Credit Administration and NCUA reporting,
which use incompatible definitions that must be reconciled before they can be
read together.

**Comparative strand.** U.S. measurement is the spine. A named comparative
strand carries cocoa-economy and international certification work, where
marketing-chain institutions differ sharply enough from the U.S. case to
discipline claims about what is mechanism and what is merely American. The
strand is part of the programme, not an appendix to it.

## 5. Standards

The programme binds itself to these. They are not aspirations; a release that
fails one is not released.

1. **Everything public.** Every dataset, every line of code, every report, under
   an open licence, with no embargo and no "available on request".
2. **Reproducible from the README alone.** A stranger who has never spoken to
   the maintainer runs the scripts in order and gets the committed outputs.
3. **Provenance on every fetch.** Filename, byte count, SHA-256, source URL, and
   access date, logged at the moment of retrieval.
4. **Numbers come from the pipeline, never from a keyboard.** Any document that
   quotes a figure interpolates it from a stats file the pipeline wrote. Text
   and data cannot disagree because the text cannot be typed.
5. **Limitations written before conclusions.** Every artifact carries a
   limitations document written before its discussion section, so the discussion
   cannot outrun what the data supports.
6. **Nothing is claimed before it exists.** No dataset, DOI, download count,
   adoption, or publication appears in any programme document until it is real
   and verifiable. Planned work is labelled as planned, everywhere, without
   exception.
7. **Corrections are public and versioned.** An error found after release is
   fixed in a new version with a documented changelog entry, never silently.
8. **Registers are archived without their contact details.** The snapshots keep
   every field bearing on certification, intermediation, credit, channel and
   location, and drop the contact email and telephone number before writing.
   These registers list small farms, where the business contact is usually a
   personal address and a mobile number. An agency publishing them one listing
   at a time is not the same act as a public repository holding a downloadable
   file of tens of thousands of them, renewed monthly and kept indefinitely, and
   the people who would carry the cost of the difference are the producers this
   programme exists to serve. Nothing analytical is given up: listings are
   tracked between snapshots by the identifier the agency assigns. This is the
   single point where the archive does not preserve what was published, it is
   recorded in the provenance line of every affected file, and the script
   refuses to write a file at all if the redaction fails.
9. **Completeness outranks automation.** Where an agency offers both a
   convenient machine route and a complete one, the complete route is the
   archive's capture and the convenient one is at most a backstop, labelled as
   partial in its filename and its provenance. This programme learned the rule
   the hard way: its first automated harvester captured between 30 and 80 per
   cent of each register, and about nine fields where the full download carries
   85 to 264, while reporting success. A partial capture presented as a
   snapshot is worse than a missing month, because a missing month announces
   itself and a quiet gap does not.

## 6. What the programme is not

It is not funded, sponsored, affiliated with, or speaking for USDA, Middle
Tennessee State University, or any agency whose data it uses. It does not
consult for, accept payment from, or advocate on behalf of firms in the
industries it measures. It does not hold, purchase, or redistribute proprietary
or licensed data. It is not a policy advocacy organisation: it files technical
comments into public dockets where it has measurement to contribute, in the
maintainer's individual capacity, and it does not campaign.

It is also, at version 0.1.0, one researcher with an archive that started today
and no published outputs. That is stated plainly here so it cannot be read as
anything else.

## 7. Governance, funding and independence

Self-funded. No grants, no institutional support, no sponsorship, no conflicts
of interest to declare as of 15 September 2026. Sole maintainer: the founder.
Should that change — funding received, collaborators added, conflicts arising —
this section is updated in the same commit that makes the change true, and the
change appears in the changelog.

AI assistance was used substantially in building this version: the documents,
the public site, and the code in this repository were drafted with an AI
assistant from the maintainer's brief. Every claim, figure, and source in them
has been checked by the maintainer against the original; every analytic decision
is the maintainer's; and nothing is released until the checklist in
`docs/VERIFY_CHECKLIST.md` is complete and signed. AI assistance continues on
the same terms for code, data wrangling, literature triage, and drafting. Each
venue's AI-disclosure policy is followed in full at submission.

This is stated plainly because the programme asks readers to check what it
claims, and a disclosure that understated what happened would be the first thing
to fail that test.

## 8. Status and versioning

**Version 0.1.0, 15 September 2026.** Programme founded; charter, standards, and
source register established; register preservation begun. No research artifacts
released. See `docs/ARTIFACTS.md`, which is empty, and `docs/ROADMAP.md`, which
says what is planned and marks it as planned.

The charter is versioned with the repository. Every subsequent release states
what changed and why.

---

*Cite as: Adesiyan, T. F. (2026). The Farm Share Evidence Program: Charter,
version 0.1.0. [DOI pending first Zenodo deposit]*
