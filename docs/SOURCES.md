# Source register

Every source the programme uses or intends to use, with its access terms
verified before it was written down here. A source that turns out to be
paywalled, gone, or restrictively licensed is not a setback to work around —
it is a different project, and the register is what stops that discovery
arriving late.

**All sources below were checked live on 15 September 2026.** Each entry records
what was confirmed on that date, not what is assumed to be true in general.
Re-verify before each release; note the check date in the release changelog.

Works of the U.S. federal government are not subject to domestic copyright
(17 U.S.C. § 105). That makes the underlying records freely usable, and it does
not remove the obligation to attribute them, which this programme does in every
artifact.

---

## 1. USDA ERS Food Dollar Series

The national benchmark the programme measures against, and the origin of the
term "farm share".

- **Host:** USDA Economic Research Service
- **URL:** https://www.ers.usda.gov/data-products/food-dollar
- **Summary findings:** https://www.ers.usda.gov/data-products/food-dollar/summary-findings
- **User's guide:** https://www.ers.usda.gov/data-products/food-dollar/documentation#guide
- **Underlying data:** Ag-FEDS, linked from the product page
- **Methodology of the 2026 revision:** *A More Detailed Food Dollar: Enhanced
  Accounting of U.S. Food Costs*, ERS report, publication 113904.
  https://www.ers.usda.gov/publications/pub-details?pubid=113904 — read this
  before making any claim that spans the revision.
- **Release:** March 2026 update, page updated 10 March 2026. Released 2024 data
  and revised prior years.
- **Latest data year:** 2024
- **Structure:** three series — marketing bill, industry group bill, primary
  factor bill
- **Key values, 2024 (post-revision):** farm share 11.8 cents per dollar spent by
  U.S. consumers on domestically produced food; marketing share 88.2 cents.
  2023 farm share 12.1 cents. Both are post-revision figures, so the 0.3-cent
  fall between them is a like-for-like comparison.
- **Vintage note — read before quoting any figure.** ERS revised the model in
  2026 and, as part of it, **broadened the definition of food** to include
  bottled water, soft drinks, coffee, tea, and beverage materials. Because the
  supply chains for those items use relatively few farm commodities, the
  broader definition lowered the reported farm share by itself:

  | Year | Pre-revision | Post-revision |
  |---|---|---|
  | 2024 | 12.3¢ | 11.8¢ |
  | 2023 | 12.5¢ | 12.1¢ |

  Half a cent of the 2024 figure moved because of a definitional decision, not
  because of anything that happened on a farm. **Never splice pre- and
  post-revision figures**, and state the vintage whenever a comparison spans
  2026.

### What the headline number hides — and why this programme exists

The 2024 release makes the case better than any argument could. All figures
below are ERS's own, from the Summary Findings page.

**The all-food farm share fell while the at-home farm share rose.**

| Measure, 2024 | Value | Change from 2023 |
|---|---|---|
| Farm share, all food | 11.8¢ | −0.3¢ |
| Farm share, food at home | 18.5¢ | **+0.1¢** |
| Farm share, food away from home | 7.1¢ | −0.4¢ |

The headline decline is substantially compositional. Food-away-from-home
spending rose 4.2% to $1.27 trillion while food-at-home rose 1.4% to $901
billion, and farmers receive 7.1 cents of a restaurant dollar against 18.5 cents
of a grocery dollar. So "the farm share is falling" is, in large part, a
statement about where people eat rather than about farmers losing ground within
any channel they sell into. **A single national ratio cannot distinguish those
two stories, and they have opposite policy implications.**

**Gross return is not net return.** From the industry group bill, farm value
added was 6.7¢ per food dollar in 2024 (crops 2.5¢, livestock 3.3¢, forestry,
fishing and agricultural services 0.9¢). The marketing bill's 11.8¢ farm share
is a *gross* return, so farms purchased roughly 5.1¢ of inputs per food dollar
(11.8 − 6.7). Agribusiness supplied 3.0¢ of that. Any claim about what farmers
"receive" must say which of these two numbers it means.

**Dispersion already exists in the published data.** ERS splits food-at-home
spending into 28 product accounts whose farm shares differ by supply-chain
structure — fresh fruit and vegetables run high because they are barely
processed; canned, frozen and dried run low. Of the 2024 accounts, 10 fell, 11
rose, and 7 moved less than a tenth of a cent. The aggregate conceals movement
in both directions.

**Scale, for context.** U.S. consumers spent $2.58 trillion on food in 2024
(+4.0%), of which $2.17 trillion was domestically produced (+3.0%). Farm
establishments received $256.7 billion from commodity sales into the food
system, up 1.0% ($2.7 billion) from $254.1 billion in 2023.

None of this is a criticism of ERS, whose method is documented and whose
decomposition is what makes the point visible at all. It is the argument for
measuring below the aggregate, at the operation level, where the mechanisms
actually operate.
- **Licence:** public domain, U.S. government work
- **Access:** direct download, no key
- **Status:** ✅ live, confirmed 15 September 2026

## 2. USDA AMS Organic INTEGRITY Database

The certification strand's primary register.

- **Host:** USDA Agricultural Marketing Service, National Organic Program
- **URL:** https://organic.ams.usda.gov/integrity/
- **Mirror / catalogue record:** https://agdatacommons.nal.usda.gov/articles/dataset/The_Organic_INTEGRITY_Database/24661722
- **What it holds:** certified operation records — program, operation name,
  certifier, status, city, state/province, **country**, and certified product
  scopes. Listings come from USDA and Trade Partner-Accredited Certifying
  Agents.
- **Historical depth:** AMS publishes monthly snapshots of the full dataset and
  historical annual lists of certified operations, via the database's Data
  History page. The search interface also offers **Export to Excel** directly.
- **Licence:** public domain, U.S. government work
- **Access:** bulk download and Excel export; no key required for search. Some
  features sit behind Log In / Register.

#### Two things that change how this source must be used

**1. It is not a U.S. register.** USDA-NOP certifies operations worldwide, and
the database carries them: a default search returns operations in Ukraine,
Kazakhstan, Mexico, Turkey and the Russian Federation alongside U.S. ones, plus
separate Trade Partner programs. "Certified under the U.S. National Organic
Program" and "located in the United States" are different populations, and the
country column is what separates them. Any panel built from this source must
state which it means, in its title and its codebook. See the scope decision
noted in `docs/ROADMAP.md`.

**2. The default status filter is `Certified`.** The search opens showing only
currently-certified operations. For a spell panel that is precisely the wrong
selection — exits are the observations that carry the information, and a
dataset built from the default view would be censored in the one direction that
matters, while looking complete. Every extract must explicitly include
surrendered, revoked and suspended statuses, and the codebook must record which
status values were captured.

- **Known difficulty:** operation identity is not stable across snapshots in a
  way that can be trusted naively. Renames, certifier changes, and record
  re-creation all occur. Entity resolution is the substantive work, not a
  preliminary step to it.
- **Status:** ✅ live, interface confirmed working by the maintainer on
  16 September 2026. (An automated check on 15 September hit an application
  error; that was transient and the note recording it as a possible defect was
  wrong.)

## 3. USDA AMS Market News (MARS API)

The intermediation strand's price backbone.

- **Host:** USDA Agricultural Marketing Service, My Market News (MMN)
- **Portal:** https://mymarketnews.ams.usda.gov/
- **API documentation home:** https://mymarketnews.ams.usda.gov/mymarketnews-api
  — sections for Getting Started, Authentication, Reports, Sorting, Filtering,
  Errors, Examples, FAQs, Basic Instructions, and **Change History**
- **API root:** https://marsapi.ams.usda.gov/services/v1.1/
- **Service contact:** mymarketnews@ams.usda.gov
- **What it holds:** shipping point, terminal market, retail and wholesale price
  reports across commodities, organised by commodity
- **Licence:** public domain, U.S. government work
- **Access:** **free personal API key required**, obtained by registering and
  logging in at the MMN portal. The API does not support open web browser calls
  — requests must carry the key from a client, not a browser address bar.
- **Non-API route:** the MMN home page offers direct downloads for one-off
  extracts. Use it for exploration; the API is for bulk and repeatable pulls.
- **Sibling service:** the LMPRS API (Livestock Mandatory Price Reporting)
  works similarly and has its own user guide, linked from the same page.
- **Track the Change History page.** The API documents its own changes over
  time. For a programme that dates and versions everything, this is the record
  that lets an extract be tied to the API behaviour in force when it was taken.
  Check it before each release and note the state in the release changelog.
- **Key handling:** the key is a credential. It goes in an environment variable
  (`MARS_API_KEY`), never in a file, never in a commit. `.gitignore` and the
  publish gate both check.
- **Coverage caveat:** historical depth varies substantially by report. Which
  reports go back how far is not documented in one place — establishing that is
  itself a planned programme artifact (see ROADMAP).
- **Status:** ✅ live, confirmed 15 September 2026

## 4. USDA Local Food Directories

The intermediation strand's register of intermediaries, and the programme's
preservation priority.

- **Host:** USDA AMS, via the Local Food Portal
- **URL:** https://www.usdalocalfoodportal.com/
- **Directories:** farmers market, CSA, food hub, on-farm market, agritourism
- **Data Sharing page:** https://www.usdalocalfoodportal.com/fe/datasharing/
- **Bulk download — works in a browser, CANNOT be automated.** All five
  directories download from the Data Sharing page without a key, and the files
  are good. But the page calls this a "CSV endpoint" with a `|` separator and
  actually serves **`.xlsx` Excel workbooks** named
  `{directory}_{YYYY}-{M}{DDHHMMSS}.xlsx` — and, more importantly, serves them
  from a **`blob:` URL**. A blob URL means the page's JavaScript assembles the
  file inside the browser and hands it over locally. **There is no server
  address that returns these files.** The blob URL is ephemeral, local to one
  tab, and useless to anything else.

  Consequence: a person can download the directories; a program cannot, short of
  driving a real browser. Verified 16 September 2026.

- **The API is therefore the only automatable route**, and is what the monthly
  workflow uses. This is the reverse of the assumption recorded on 15 September,
  which had the keyless bulk route as primary and the API as fallback.
- **API endpoints:** `https://www.usdalocalfoodportal.com/api/{directory}/` for
  agritourism, csa, farmersmarket, foodhub, onfarmmarket. Requires a free key
  from https://www.usdalocalfoodportal.com/fe/fregisterpublicapi/, and **a
  location parameter is mandatory** — `state`, `zip`, `zip`+`radius`,
  `city`+`state`, or `x`+`y`+`radius`, with radius capped at 100 miles. No
  location, no data. Returns JSON. National coverage therefore means iterating
  jurisdictions, which is what the harvester's API fallback does.

#### Fields — verified from the downloaded files, 16 September 2026

`listing_id` is column A in every directory, so the harvester's de-duplication
key exists and does not need the name-plus-address fallback. Column B is
`update_time`. Then `listing_name`, `location_address`, a block of
`orgnization_*` fields, `listing_desc`, `location_x` and `location_y`
(coordinates), and directory-specific columns.

**Note the spelling: the organisation fields are `orgnization_*`, not
`organization_*`.** That is how the field is named in the data. Code written
against the correct English spelling will silently return nothing.

IDs are block-allocated by directory: agritourism in the low four digits,
farmers market from 300000, food hub from 500000, on-farm market from 700000.
Within a directory they are not strictly chronological — on-farm market holds
both a 700000 series dated 2014 and a 701600 series dated 2022 — so **do not
infer age or ordering from the ID.**

Two directories carry fields worth more than their listing counts suggest.
**Food hub** records year established (values seen from 1982 to 2013) and legal
form — Producer Cooperative, Consumer Cooperative, Non-Profit, LLC, S Corp,
C Corp, B Corp. For the intermediation strand that is close to the heart of the
question: who owns the intermediary determines who keeps the margin.
**Agritourism** carries the affinity-group membership fields the platform
announcement mentioned, as binary flags plus named organisations (NAFDMA,
FarmStay, state associations such as OEFFA).

#### The preservation claim, corrected

The register said flatly that this source has no history. That was too strong,
and the correction matters in both directions.

**Each listing carries its own `update_time`, and those run from 2014 to 2026.**
So a single snapshot is not a flat cross-section: it tells you when every
surviving listing was last touched, which supports an age-structure analysis
today, before the archive has any depth at all.

**But exits remain unobservable retroactively, and that is what the archive is
for.** A listing that lapses is removed, taking its `update_time` with it. No
field in a current download tells you what used to be there. So the argument for
snapshotting now is unchanged: the surviving population carries partial history,
the departed population carries none, and only a series of snapshots recovers
the second.

One caution before leaning on `update_time`: its semantics are not documented.
It may mean record creation, last edit by the listing manager, or last touch by
AMS — and the three imply very different things. Establish which before using
it, alongside dating the platform transition.
- **Licence:** public domain, U.S. government work; site terms of use apply
- **Contact:** Americo J. Vega-Labiosa, Agricultural Marketing Specialist,
  AmericoJ.Vega-Labiosa@usda.gov
- **Preservation status:** ⚠️ **current-state only. No public historical
  archive.** Listings that lapse are removed, not retired. Data not captured is
  permanently unrecoverable. This is why snapshotting begins at v0.1.0 rather
  than when analysis is ready.
- **Status:** ✅ live, confirmed by the maintainer 16 September 2026

#### Baseline counts at the start of the archive

Recorded because they are the zero point of the preservation series, and because
they will be needed to interpret everything that follows.

| Directory | Listings, 16 Sept 2026 |
|---|---|
| Agritourism | 13,569 |
| Farmers Market | 7,148 |
| On-Farm Market | 4,692 |
| CSA | 2,002 |
| Food Hub | 480 |
| **Total** | **27,891** |

#### ⚠️ The platform was rebuilt, and early counts are not a clean baseline

AMS has moved the directories onto a **new platform**, which combines all
directories in one place, adds accounts so managers can update their own
listings, adds new fields including affinity groups, and introduces a **new
Agritourism directory** that did not previously exist. The launch announcement
states that AMS is "working with partners to add more businesses to the
directories."

This is the single most important caveat attached to any source in this
register, and it must appear in the codebook of anything built on these
snapshots:

1. **Rising counts will partly measure recruitment, not entry.** While AMS is
   actively adding businesses, a growing listing count reflects platform
   adoption as much as real new market formation. Reporting "farmers markets
   grew *n*% from 2026 to 2029" from this series, without separating those,
   would be wrong.
2. **Falling counts may partly measure non-migration.** Operations that existed
   on the old platform and never re-registered on the new one look like exits
   and are not.
3. **The Agritourism directory has no pre-platform history at all.** Its 13,569
   listings — the largest of the five — are new as a series, whatever their age
   as businesses.
4. **The launch date is not established.** The announcement seen on
   16 September 2026 is undated in the material reviewed and refers to "when
   summer rolls around" in the future tense, implying it was written before
   summer 2026. **Dating the platform launch, and establishing when recruitment
   stabilised, is a prerequisite** for any entry-or-exit claim from this source.
   Contact AMS if the date cannot be established from the site.

None of this argues against snapshotting — it argues for starting now and
labelling honestly. The archive remains the only way to observe what happens
from here. But the first year of it is a record of a register being populated as
much as of a sector changing, and an analysis that forgets this will produce a
confident, publishable, wrong number.

## 5. FFIEC CRA aggregate and disclosure flat files

The credit strand's primary source.

- **Host:** Federal Financial Institutions Examination Council
- **CRA main page:** https://www.ffiec.gov/data/cra (last updated 21 July 2026)
- **Data products:** https://www.ffiec.gov/data/cra/data-products
- **Disclosure reports:** https://www.ffiec.gov/data/cra/disclosure-reports
- **Aggregate reports:** https://www.ffiec.gov/data/cra/aggregate-reports
- **National aggregate reports:** https://www.ffiec.gov/data/cra/national-aggregate-reports
- **Reporting criteria per year:** https://www.ffiec.gov/data/cra/reporting-criteria
- **Data collection guide:** https://www.ffiec.gov/data/cra/data-collection-guide
  — the definitional document; what counts as a small farm loan is settled here
- **Geocoding system:** https://geomap.ffiec.gov/
- **Statutory basis:** Community Reinvestment Act 1977, 12 U.S.C. § 2901,
  implemented by 12 CFR parts 25, 228, 345 and 195. Examinations are run by the
  Federal Reserve, FDIC and OCC, each of which supervises a different slice of
  the reporting population.
- **What it holds:** small farm and small business loan originations, by county
  and reporting institution
- **Licence:** public domain, U.S. government work
- **Access:** direct download, no key

#### ⚠️ Unresolved: which flat files

The CRA main page links **Flat Files** to `https://www.ffiec.gov/data/census/flat-files`
— under *census*, described as FFIEC census data "that may be combined with the
appropriate year(s) of HMDA and CRA data." That is the census/demographic file
set, **not** the CRA disclosure and aggregate loan files this programme needs.
An earlier automated check recorded `https://www.ffiec.gov/data/cra/flat-files`,
which is a different path and may or may not still resolve.

Do not cite either URL until it is established which one serves the
loan-origination files. Start from Data Products and Disclosure Reports.

#### The reporter population changes every year — and that is the research question

Only institutions above an asset-size threshold must report, the threshold is
reset annually, and FFIEC publishes the criteria **per year** at the reporting
criteria page above. So the denominator of any CRA-based series moves for
regulatory reasons that have nothing to do with lending.

This is not a nuisance to control for; it is the planned analysis. The credit
strand's question — what share of the farm credit market CRA data actually
observes — is answered by pairing the annual reporting criteria with the
reported volumes, and the per-year criteria page is the spine of it. Read it
before touching the loan files.

- **Status:** ✅ live, confirmed by the maintainer 17 September 2026

---

## Sources intended but not yet verified

Listed so the gap is visible rather than forgotten. None of these is used by any
artifact until it has been checked and moved into the register above.

- **USDA FNS SNAP-authorised retailer data** — retailer spell construction for
  the intermediation strand. Historical availability not yet confirmed.
- **Farm Credit Administration call report data** — credit strand.
- **NCUA call report data** — credit strand, agricultural lending by credit
  unions.
- **USDA NASS Quick Stats** — denominators, farm counts, and commodity context.
- **USDA ERS Local Food Marketing Practices Survey** — channel-choice analysis;
  next release schedule not yet confirmed.
- **USDA Rural Business-Cooperative Service award data** (RCDG, VAPG, RBDG) —
  cooperative development strand.

## Re-verification log

Rows are **added, never edited or removed**. The log is a record of who checked
what and when, and overwriting it would destroy the thing it exists to show.
A row that later turned out to be wrong gets a new row saying so.

| Date | Checked by | Result |
|---|---|---|
| 2026-09-15 | AI-assisted build; not verified by the maintainer | Sources 1–5 confirmed live and openly licensed. INTEGRITY interactive interface returned an application error; bulk and catalogue routes reachable. |
| 2026-09-16 | T. F. Adesiyan (maintainer) | **Source 1 (ERS Food Dollar) verified personally.** Farm share 11.8¢ and marketing share 88.2¢ for 2024 confirmed on the Summary Findings page. Two corrections to the 15 Sept entry: the product URL is `/data-products/food-dollar`, not `/data-products/food-dollar-series`; and the 2026 revision broadened the definition of food to include bottled water, soft drinks, coffee, tea and beverage materials, restating 2024 from 12.3¢ to 11.8¢ and 2023 from 12.5¢ to 12.1¢. Both recorded above. Sources 2–5 not yet personally checked. |

| 2026-09-16 | T. F. Adesiyan (maintainer) | **Source 2 (Organic INTEGRITY) verified personally.** Search interface loads and works; the 15 Sept application error was transient, and the note calling it a possible defect has been withdrawn. Two findings recorded above: the database is **not U.S.-only** — USDA-NOP operations in Ukraine, Kazakhstan, Mexico, Turkey and the Russian Federation appear in a default search, alongside separate Trade Partner programs; and the **default status filter is `Certified`**, which would silently censor exactly the exits a spell panel exists to observe. Export to Excel is available from the search interface. Sources 3–5 not yet personally checked. |

| 2026-09-16 | T. F. Adesiyan (maintainer) | **Source 3 (AMS Market News) verified personally.** Documentation home confirmed at `/mymarketnews-api`, with Authentication, Reports, Sorting, Filtering, Errors, Examples and FAQs sections. Key still requires registration and login. Three additions recorded above: a **Change History** page that lets an extract be tied to the API behaviour in force when it was taken; a non-API download route on the MMN home page for one-off extracts; and the service contact, mymarketnews@ams.usda.gov. Sources 4–5 not yet personally checked. |

| 2026-09-16 | T. F. Adesiyan (maintainer) | **Source 4 (Local Food Directories) verified personally.** Site live; baseline counts recorded above (27,891 listings across five directories). **Material finding:** the platform has been rebuilt — all directories combined, accounts added, a new Agritourism directory created, and AMS stating it is still "working with partners to add more businesses." Early snapshots therefore measure recruitment and migration alongside real entry and exit, and the launch date is not yet established. Recorded as the register's most important caveat. Contact recorded. **The bulk CSV download route was not exercised** — still unconfirmed. |

| 2026-09-16 | T. F. Adesiyan (maintainer) | **Local Food Directories checked; the automation assumption was wrong.** All five directories download in a browser without a key, and `listing_id` is present as column A. But the files served are `.xlsx` workbooks, not the pipe-delimited CSV the page describes, and they arrive from a **`blob:` URL** — assembled by JavaScript in the browser, with no server address a script can fetch. **The keyless bulk route cannot be automated at all**; the API, previously recorded as the fallback, is the only machine route and is now the workflow's default. Field inventory recorded above, including the `orgnization_*` spelling, block-allocated IDs, and the food hub legal-form and agritourism affinity-group fields. **Further correction to the 15 Sept entry:** the claim that this source carries no history was too strong — each listing has an `update_time`, with values from 2014 to 2026. Exits remain unobservable retroactively, so the preservation argument stands. |

| 2026-09-17 | T. F. Adesiyan (maintainer) | **Source 5 (FFIEC CRA) verified personally. All five sources now checked by the maintainer.** CRA main page live, last updated 21 July 2026. Statutory basis, supervising agencies, and the full set of data-product URLs recorded above. **One unresolved item:** the page links "Flat Files" to `/data/census/flat-files`, which is the census/demographic set, not the CRA loan files — the `/data/cra/flat-files` path recorded on 15 September is unconfirmed. Neither URL is to be cited until the loan-file location is established. **Most useful finding:** FFIEC publishes reporting criteria per year, and the asset-size threshold resets annually, so the reporter population moves for regulatory reasons. That page is the spine of the planned coverage analysis rather than a caveat to it. |

| 2026-09-18 | T. F. Adesiyan (maintainer) | **First machine-taken snapshot of Source 4, and two findings about the API.** The monthly workflow captured all five directories — 18,415 unique listings — from GitHub's servers. **First finding: the API is behind a firewall that rejects unconventional user agents.** The identical key, URL and query returned data in a browser but HTTP 403 from GitHub for all 56 jurisdictions of all five directories; nothing changed but the `User-Agent` header, from a bare `FarmShareEvidenceProgram/0.1.0` token to the conventional `Mozilla/5.0 (compatible; …; +url)` crawler form, and every query succeeded. The programme is still identified by name and URL in the header. **Second finding, and the one that matters for reading the data: a jurisdiction with no listings answers `{"data": ""}` — an empty string, not an empty list.** Fourteen such answers were returned: Guam in all five directories, Puerto Rico in three, the District of Columbia in agritourism, and Delaware, Maine, New Jersey, Washington and Wyoming in the food hub directory. These are genuine zeros, not failed queries, and the harvester now records the two separately in the provenance log. A count of zero in this archive means the register was asked and said none; a jurisdiction that was never answered is named as such and its coverage recorded as unknown. |

| 2026-09-18 | T. F. Adesiyan (maintainer) | **Decision: contact details are not archived.** The API returns `contact_email` and `contact_phone` for every listing. These are dropped before the snapshot is written and do not enter the repository. Reasoning in CHARTER.md standard 8: these registers are mostly small farms, whose business contact is usually a personal address and a mobile number, and a monthly, permanent, bulk-downloadable file of tens of thousands of them is a materially different exposure from USDA's own search interface. Entity resolution between snapshots uses `listing_id`, which USDA assigns, so no analytical capability is lost. Recorded here because it is the only point at which this archive knowingly does not preserve what the agency published. The two snapshots taken on 18 September that did contain these fields were discarded, and the repository rebuilt, before the data was left in a public git history. |

**All five sources are now maintainer-verified.** The register's remaining open
items are the flat-file path above, the Local Food Directories platform launch
date, and the semantics of `update_time`.

Re-verify before each release and add a row each time.
