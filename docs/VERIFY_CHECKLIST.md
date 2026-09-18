# Verification checklist — v0.1.0

**Nothing in this repository is published until every box below is ticked by the
maintainer personally.**

This is not a formality. Everything here goes out under one person's name, into
records that are permanent and, in some contexts, consequential. An AI assistant
drafted this package; it did not verify it, and it cannot. The point of a gate
is that a person stands behind what passes through it.

Work through it, tick each box, sign at the bottom, then run `python
finalize.py` to strip the DRAFT banners. The publish gate refuses to proceed
while any banner, `[VERIFY]` tag, or unfilled placeholder remains — that is
deliberate, and the way past it is to resolve them, not to bypass the check.

---

## 1. The charter says what you mean

- [x] **Read in full by the maintainer, 18 September 2026.**
- [x] **Confirmed by the maintainer, 18 September 2026.** The purpose in section 1 is the
      programme she intends to run.
- [x] **Confirmed by the maintainer, 18 September 2026.** Three U.S. strands plus the named
      comparative strand is the intended scope.
- [x] **Confirmed by the maintainer, 18 September 2026**, including the two added that day:
      standard 8 (registers archived without contact details) and standard 9
      (completeness outranks automation).
- [x] **Confirmed true by the maintainer, 18 September 2026.** No funding, no sponsorship,
      no consulting, no conflicts. MTSU is named in full in section 6 and
      explicitly disclaimed.
- [x] **Confirmed true by the maintainer, 18 September 2026.** Self-funded, and the
      AI-assistance disclosure is accurate as written — every claim, figure and
      source checked by her against the original, which the week's source
      verification bears out.

## 2. The sources are real and you have seen them

- [x] **ERS Food Dollar — checked 16 September 2026.** Farm share 11.8 cents for
      2024, marketing share 88.2 cents, confirmed on the Summary Findings page.
      The check also caught two errors in the register, both now corrected: the
      product URL, and the fact that the 2026 revision broadened the definition
      of food (bottled water, soft drinks, coffee, tea) and restated 2024 from
      12.3¢ to 11.8¢. This is what personal verification is for.
- [x] **Organic INTEGRITY — checked 16 September 2026.** Interface works; the
      15 September error was transient. The check found that the database is not
      U.S.-only and that its search defaults to currently-certified operations
      — both recorded in the register, and the first now an open scope decision
      in `docs/ROADMAP.md`.
- [x] **AMS Market News — checked 16 September 2026.** Documentation home
      confirmed; key still requires registration. The check added the Change
      History page, the non-API download route, and the service contact to the
      register.
- [x] **Local Food Directories — checked 16 September 2026.** Site live;
      baseline counts recorded. The check found the platform has been rebuilt
      and is still being populated, which is now the register's most important
      caveat and blocks the intermediary-inventory strand until the launch date
      is established.
- [x] **FFIEC CRA — checked 17 September 2026.** Statutory basis, supervising
      agencies and data-product URLs recorded; the annual reporting-criteria
      page identified as the spine of the credit strand's coverage analysis.
      One item left open: the page links "Flat Files" to the *census* set, so
      the CRA loan-file location is unconfirmed and neither candidate URL is to
      be cited yet.
- [x] **Local Food Directories bulk download confirmed, 16 September 2026.**
      All five directories downloaded without a key; `listing_id` present. The
      files served were `.xlsx` workbooks, **not** the pipe-delimited CSV the
      page describes. Field inventory recorded in the register, including the
      `orgnization_*` spelling and the `update_time` column that corrected the
      no-history claim.
- [x] **Download URL checked, 16 September 2026 — and it settled the design.**
      The download comes from a `blob:` URL, meaning the file is built by
      JavaScript inside the browser. No server address exists for a script to
      fetch, so the keyless bulk route **cannot be automated**. The API became
      the workflow's route on that basis — a decision reversed on 18 September
      when the API turned out to return only 30-80% of each register. The
      download is the archive's capture; the API run is a backstop. See
      CHARTER.md standard 9.
- [x] **Local Food Directories API key obtained, 17 September 2026.** Required,
      not optional — without it the monthly snapshot cannot run at all.
- [x] **Key stored as a GitHub secret, 18 September 2026**, named exactly
      `LOCALFOOD_API_KEY`, and proven by a successful workflow run. Rotated the
      same day after the value passed through a chat window during debugging;
      the replacement was verified by a further run. Never put in a file; the
      publish gate scans for key-shaped strings and reports clear.
- [x] **September's manual download folded in, 18 September 2026.** All five
      directories, complete: 13,569 agritourism, 7,148 farmers market, 4,692
      on-farm market, 2,002 CSA, 480 food hub — 27,891 listings, matching USDA's
      published totals exactly. Adopted with `code/00_adopt_manual_snapshot.py`,
      which recorded honestly that a person downloaded them. Every file's hash
      and byte count in `data/raw/PROVENANCE.txt` was checked against the
      committed file.
- [x] All five sources load, are what the register says they are, and are
      openly licensed.
- [x] Rows added to the re-verification log in `docs/SOURCES.md` for every
      source, appended rather than overwriting earlier entries.

## 3. Nothing is claimed that does not exist

- [x] **Checked 18 September 2026.** `docs/ARTIFACTS.md` lists no released
      artifacts; the table is present but empty, with a note saying the absence
      is a fact about the programme's age. The preservation-archive table was
      updated the same day from `data/raw/PROVENANCE.txt` — it had still said
      "not yet started, 0 snapshots" after the archive had begun.
- [x] **Checked 18 September 2026** by search across every document, the site,
      `CITATION.cff` and `AUTHORS.json`. No DOI, download count, citation count,
      user count or adoption figure appears anywhere. Every mention of "DOI" is
      a rule about when one will exist, or the pending line in `CHARTER.md`.
- [x] **Checked 18 September 2026.** `docs/ROADMAP.md` opens with "Everything
      on this page is planned work. None of it exists," and the new automation
      section is headed "PLANNED, NOT ATTEMPTED".
- [x] **Searched 18 September 2026.** Every hit for published / released /
      accepted / under review describes a rule, a federal source, or the absence
      of output. None asserts work completed by this programme.

## 4. Identity and attribution

- [x] **Confirmed by the maintainer, 18 September 2026.** Name of record Taiwo Fausiyat
      Adesiyan; correspondence name Taiwo Adesiyan; citation form
      Adesiyan, T. F.
- [x] **Checked digit by digit, 18 September 2026.** 0000-0002-2023-3624 is
      identical in `AUTHORS.json`, `CITATION.cff`, `CHARTER.md` and the site.
- [x] **Checked 18 September 2026.** `Adesiyan, T. F.` is the citation form in
      `AUTHORS.json`, the suggested citation in `README.md`, `docs/ARTIFACTS.md`
      and the site. `CITATION.cff` carries family/given names that render to the
      same form.
- [x] **Searched 18 September 2026.** No "Ph.D.", "PhD" or "Dr." appears in any
      document, the site, or the metadata files.
- [x] **Confirmed by the maintainer, 18 September 2026.** The affiliation states where she
      is, not who backs the work; section 6 and the site footer both disclaim
      Middle Tennessee State University by name.

## 5. The snapshot is real and complete

The archive's capture is the browser download, not the automated API run. See
CHARTER.md standard 9 for why. Both may exist for a month; the download is the
one that counts.

- [x] **Done 18 September 2026.** All five directories downloaded from
      https://www.usdalocalfoodportal.com/fe/datasharing/ and folded in with
      `code/00_adopt_manual_snapshot.py`.
- [x] **Verified 18 September 2026.** `data/raw/snapshots/2026-09/` holds five
      `.xlsx` files. Each was fetched back from GitHub and its SHA-256 and byte
      count compared against the provenance log — all five match exactly.
- [x] **Counted 18 September 2026, row by row: 13,569 / 7,148 / 4,692 / 2,002 /
      480 — exact matches to USDA's published totals**, 27,891 listings in all.
      This check is why the API route was abandoned: it returned 77%, 80%, 30%,
      38% and 39% of these while reporting success.
- [x] **Checked 18 September 2026.** `listing_id` is unique within every file:
      distinct identifiers equal row counts in all five.
- [x] **Verified 18 September 2026.** 15 records, all valid JSON: five MANUAL
      browser downloads and ten from the API backstop. Every path named in the
      log exists in the repository with the logged hash and byte count.
- [x] **Understood and labelled, 18 September 2026.** The five `.csv` files in
      `2026-09` predate the naming change, so they lack the `.partial` marker;
      `data/raw/snapshots/2026-09/README.md` names them individually and says
      not to analyse them. Runs from now on write `*.partial.csv`. Nothing in
      this repository treats either as a full register.
- [x] **A reminder exists, built into the repository, 18 September 2026.**
      `.github/workflows/monthly-reminder.yml` opens an issue on the first of
      each month setting out the capture steps, and GitHub emails the repository
      owner when an issue is opened. The issue stays open until closed by hand,
      so one still open a month later is itself the signal that a month was
      missed. **This replaces the calendar reminder this item originally asked
      for**, and the substitution is recorded rather than assumed: a reminder
      inside the repository is more durable than one in a calendar app, and less
      independent of the thing it watches. See the next item for what it cannot
      do.
- [x] **Understood and covered, 18 September 2026 — but read the limit.**
      GitHub disables scheduled workflows after about 60 days of repository
      inactivity, and a disabled workflow cannot announce its own disabling, so
      the reminder above is not its own safety net. Three things cover it
      instead. First, doing the monthly capture commits to the repository, which
      resets the 60-day clock — so the risk only materialises after a month has
      *already* been missed. Second, the absence of the monthly issue on the
      first is itself visible, once you expect it. Third, GitHub emails the
      repository owner when it switches a workflow off; that email is the real
      backstop and is to be treated as urgent rather than as noise.
      **This is weaker than an out-of-repository reminder and is knowingly
      accepted as such**, which is why it is written down here instead of being
      quietly ticked.

## 6. Placeholders are filled

- [x] **Checked 18 September 2026.** `Tlayem` appears in `README.md`,
      `CITATION.cff`, `BUILD_SPEC.md` and `site/index.html`, spelled identically
      in every one. Both addresses were fetched and resolve to this repository
      and its site, which is stronger evidence than reading the spelling.
- [x] **Checked 18 September 2026.** Only two forms appear anywhere:
      `github.com/Tlayem` and `tlayem.github.io`. Both resolve; the asymmetry is
      correct.
- [x] **Checked 18 September 2026 — and this one had failed.** The gate passed
      a repository still containing `[project URL]` in `BUILD_SPEC.md` and
      `[repository URL]` in `docs/ARTIFACTS.md`, because its scan listed
      placeholders by name and neither name was on the list. Both are now
      filled, and `finalize.py` catches placeholders by shape instead. The only
      one left is the DOI line at the foot of `CHARTER.md`.
- [x] **Checked 18 September 2026.** The publish gate's secret scan reports
      clear across all tracked text files. The API key lives only in the GitHub
      repository secret, and was rotated after passing through a chat window.

## 7. Read it as a stranger would

- [x] **Read on the live site by the maintainer, 18 September 2026.** A reader comes away
      with the programme as new, self-funded, and having released nothing. A
      sceptical re-read the same day found two documents that had stopped being
      true and both were corrected: the site said "Seven commitments" after a
      ninth was added, and listed the Local Food Directories access route as the
      API after the browser download replaced it.
- [x] **Confirmed by the maintainer, 18 September 2026.** The status line follows the title
      and is accurate: not yet released, no research artifacts published.
- [x] **Confirmed by the maintainer, 18 September 2026**, after an independent adversarial
      read of the charter, the site and the source register. Two inconsistencies
      were found and fixed before this box was ticked; nothing else in the
      repository overstates what the programme has done.

---

## Sign-off

I have personally completed every check above. The claims in this repository are
true as of the date below, the numbers have been verified against their sources,
and I can defend every statement in it.

**Name:** ______________________________________

**Date:** ______________________________________

Then: `python finalize.py`, and follow your publish guide.
