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

- [ ] Read `CHARTER.md` start to finish, out loud if it helps.
- [ ] The purpose in section 1 is the programme you actually intend to run.
- [ ] The scope in section 4 — three U.S. strands plus a named comparative
      strand — is the scope you want. If you want U.S. only, or a different
      split, change it now; it is much harder once the charter has a DOI.
- [ ] The standards in section 5 are ones you are willing to be held to in
      public. Standard 6 in particular: nothing claimed before it exists.
- [ ] Section 6, what the programme is not, is accurate — no funding, no
      sponsorship, no consulting, no conflicts.
- [ ] Section 7's independence and AI-assistance statements are true as written.

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
      fetch, so the keyless bulk route **cannot be automated**. The API is now
      the workflow's only route.
- [x] **Local Food Directories API key obtained, 17 September 2026.** Required,
      not optional — without it the monthly snapshot cannot run at all.
- [ ] **Store the key as a GitHub secret.** Repository → Settings → Secrets and
      variables → Actions → New repository secret, named exactly
      `LOCALFOOD_API_KEY`. Never put it in a file; the publish gate scans for
      key-shaped strings.
- [ ] **Fold in September's manual download.** You saved the four files to a
      folder — that is a legitimate first month of the archive, taken before the
      automation existed. `python code/00_adopt_manual_snapshot.py <folder>
      --month 2026-09 --downloaded-on 2026-09-15` copies them in and records
      honestly that they came from a browser, not a script. (The CSA directory
      was not among them; the month will be recorded as incomplete, which is
      correct.)
- [x] All five sources load, are what the register says they are, and are
      openly licensed.
- [x] Rows added to the re-verification log in `docs/SOURCES.md` for every
      source, appended rather than overwriting earlier entries.

## 3. Nothing is claimed that does not exist

- [ ] `docs/ARTIFACTS.md` lists no released artifacts. It should not, because
      there are none.
- [ ] No DOI, download count, citation count, user count, or adoption appears
      anywhere in the repository or on the site.
- [ ] Every item in `docs/ROADMAP.md` is unmistakably labelled as planned.
- [ ] Search the whole repository for anything that reads as a claim about work
      already done: `grep -ri "published\|released\|accepted\|under review" .`
      and check each hit is describing a rule, not an accomplishment.

## 4. Identity and attribution

- [ ] `AUTHORS.json` spells your name exactly as it should appear, everywhere.
- [ ] The ORCID is correct: 0000-0002-2023-3624. Check it digit by digit.
- [ ] The byline form is `Adesiyan, T. F.`, matching your existing publications,
      so the new record joins the old one rather than starting a second profile.
- [ ] No "Ph.D." post-nominal appears anywhere. The degree is not conferred yet.
- [ ] The affiliation statement does not imply MTSU sponsors or endorses the
      programme, because it does not.

## 5. The snapshot actually runs

This can be done entirely in the browser — Actions tab, **Monthly register
snapshot**, **Run workflow** — or locally with Python if you prefer. Either
satisfies this section. Step 8 of your publish guide (kept separately, outside
this repository) has both routes.

- [ ] The snapshot has been run at least once, by either route.
      **It has never been run against the live USDA endpoints** — the build
      environment blocked those hosts — so this is a real test, not a
      confirmation. Expect it to need adjusting.
- [ ] It fetched all five directories (agritourism, csa, farmersmarket,
      foodhub, onfarmmarket), with plausible sizes for each.
- [ ] The API route was used, with `LOCALFOOD_API_KEY` set. There is no other
      automatable route; the keyless download is browser-only.
- [ ] `data/raw/snapshots/YYYY-MM/` exists and holds five files.
- [ ] The row counts look plausible against the site's own totals — roughly
      13,569 agritourism, 7,148 farmers market, 4,692 on-farm market, 2,002 CSA,
      480 food hub as of 16 September 2026. A directory returning far fewer means
      the state iteration is dropping jurisdictions.
- [ ] `data/raw/PROVENANCE.txt` has one line per fetched file, with plausible
      byte counts and hashes.
- [ ] A calendar reminder exists to check the Actions tab every two months,
      because GitHub disables scheduled workflows after about 60 days of
      repository inactivity and does so quietly enough to miss.

## 6. Placeholders are filled

- [ ] The handle `Tlayem` is correct everywhere it appears — `README.md`,
      `CITATION.cff` and `site/index.html`. It has been
      filled in for you; check the spelling is right, because these become
      permanent citation addresses.
- [ ] The Pages address `https://tlayem.github.io/...` is lower-case and the
      repository address `https://github.com/Tlayem/...` is not. That asymmetry
      is correct; GitHub Pages addresses are always lower-case.
- [ ] No other bracketed placeholder survives anywhere. The only one left by
      design is the DOI line at the foot of `CHARTER.md`, which you fill in
      after Zenodo mints it.
- [ ] No API key, token, or password is in any file. `git status` shows nothing
      you did not mean to commit.

## 7. Read it as a stranger would

- [ ] Open `site/index.html` in a browser. It says the programme is new, has
      released nothing, and is self-funded — and a reader would come away with
      exactly that impression, not a grander one.
- [ ] The README's first line is the status line, and it is accurate.
- [ ] Nothing anywhere would embarrass you if a sceptical reader — a reviewer,
      an editor, an adjudicator, a colleague — read it closely.

---

## Sign-off

I have personally completed every check above. The claims in this repository are
true as of the date below, the numbers have been verified against their sources,
and I can defend every statement in it.

**Name:** ______________________________________

**Date:** ______________________________________

Then: `python finalize.py`, and follow your publish guide.
