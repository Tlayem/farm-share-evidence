# Standards

The operational detail behind charter section 5. These are the rules a release
is checked against. A release that fails one does not go out; it gets fixed.

---

## 1. Provenance

Every fetch of an external file appends one line to `data/raw/PROVENANCE.txt`
at the moment of retrieval, containing: ISO timestamp, source URL, local path,
byte count, and SHA-256. Written by `code/provenance.py`, never by hand.

Where a host rotates download URLs between refreshes, the provenance entry
records *how the URL was discovered*, not just the URL, so the next person can
rediscover it when the old one 404s.

A file in `data/raw/` with no provenance line is treated as untrusted and is not
used in any analysis.

## 2. Reproducibility

Scripts are numbered in run order, each independently runnable, each idempotent
— running it twice produces the same result as running it once and does not
corrupt what the first run wrote.

The test of the repository is a stranger: someone who has never spoken to the
maintainer clones it, follows the README, runs the scripts top to bottom, and
gets the committed outputs. Not approximately. The same numbers.

Where exact reproduction is impossible because a source is a moving target — a
register that has changed since the snapshot — the snapshot is committed or
deposited so that the pipeline can be re-run against the fixed input.

## 3. The stats-file rule

No number is ever typed into prose.

Any document that quotes a figure — a paper, a report, a README summary, a
poster, a slide — reads that figure from a stats file the pipeline wrote
(`stats.json` or equivalent) and interpolates it at build time. The document is
built, not written-around-numbers.

This is not fastidiousness. It is the only mechanism that makes text and data
*unable* to disagree, and it turns "the data changed" from a proofreading
exercise into one command.

## 4. Quality assurance

Every dataset release ships a QA report, committed alongside the data, written
by the pipeline:

- row counts at each stage, and where rows were lost
- join and match rates, with unmatched cases enumerated rather than summarised
- range and sanity checks on every computed measure
- **named spot checks**: at least five specific units the maintainer verified by
  hand against the source, chosen to include easy cases, hard cases, and
  extremes
- the threshold counts that appear in any document, so a reader can check the
  document against the report

The QA report is read before the data is trusted, including by the maintainer.

## 5. Entity resolution

Where the programme links records across snapshots or sources, it publishes the
matching rule, the match rate, and a sample of both matches and near-misses. An
entity resolution that cannot be inspected cannot be believed, and it is usually
where the errors are.

Match decisions are never silently improved between versions; a changed rule is
a new version with a changelog entry and a restated match rate.

## 6. Draft stamping

Figures carry a visible DRAFT tag and documents carry a DRAFT banner from the
moment they are created until the verification gate passes. Figure and document
build scripts take a `--final` flag that removes it. `finalize.py` strips the
banners across the repository in one pass, and is only run after
`docs/VERIFY_CHECKLIST.md` is complete.

## 7. Nothing claimed before it exists

No artifact, DOI, identifier, download count, citation count, adoption, or
publication status appears in any programme document — repository, site,
report, CV, or correspondence — before it is real and independently verifiable.

Planned work is labelled as planned, in every document, without exception.
Submitted is not accepted. Accepted is not published. Deposited is not adopted.

Placeholders are written in a form the publish gate can detect, so that the
mechanical check catches any that survive to release.

## 8. Corrections

An error found after release is corrected in a new version with a changelog
entry naming what was wrong, what changed, and what it affects. Nothing is
silently edited. If a released figure was wrong, the correction says so in
those words.

Where a corrected artifact has a DOI, the new version gets its own DOI and the
concept DOI resolves to the corrected version.

## 9. Licensing

Code MIT. Data and documents CC BY 4.0. Underlying U.S. federal sources are
public domain and are attributed in every artifact regardless of whether
copyright requires it.

Nothing is released without a licence file. Unlicensed work cannot be reused,
and reuse is the point.

## 10. Credentials

API keys and tokens live in environment variables for the life of a session and
are never written to a file, never committed, never echoed into logs or output.
`.gitignore` excludes the usual carriers; the publish gate scans for key-shaped
strings before any push.

## 11. AI assistance

AI is used for code, data wrangling, literature triage, formatting, and drafting
mechanics. Every analytic decision is the maintainer's. Every published number
is verified by the maintainer against the source. Every venue's AI-disclosure
policy is followed in full at submission, and the disclosure statement in any
manuscript must remain literally true at the moment of submission.

The verification gate exists because this standard is only meaningful if
something enforces it.
