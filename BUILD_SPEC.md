# Build spec — Farm Share Evidence Program, v0.1.0

Written 15 September 2026, before any code. If the program changes shape, this file changes first.

```
PROJECT:        The Farm Share Evidence Program.
                Archetype: research programme infrastructure — a public hub
                (archetype 3, interactive public resource) plus the governing
                documents and the register-preservation pipeline that the
                programme's later datasets, tools and reports depend on.

QUESTION:       How much of the value of what a farm produces actually reaches
                the farm, and what determines the answer — certification,
                intermediation, or credit?

SOURCES:        Verified live and openly licensed on 15 September 2026.
                See docs/SOURCES.md for the full register with access notes.
                1. USDA ERS Food Dollar Series — farm share of the consumer
                   food dollar. Latest data year 2024; model comprehensively
                   revised 2026. Public domain (17 U.S.C. 105).
                2. USDA AMS Organic INTEGRITY Database — certified operation
                   records; monthly full-dataset snapshots and historical
                   annual lists published by AMS. Public domain.
                3. USDA AMS Market News (MARS API) — shipping point, terminal
                   and retail price reports. Free personal API key required.
                   Public domain.
                4. USDA Local Food Directories — farmers market, CSA, food hub,
                   on-farm market, agritourism registers. Bulk pipe-delimited
                   CSV without a key; REST API with a free key. Current-state
                   only; no public historical archive. Public domain.
                5. FFIEC CRA aggregate and disclosure flat files — small farm
                   loan originations by county and lender. Public domain.

UNIT:           Varies by strand. Certification: the certified operation,
                observed as a spell. Intermediation: the commodity-market-week
                and the marketing channel. Credit: the county-year.

MEASURES:       v0.1.0 computes no measures. It establishes the programme, its
                standards, and the preservation pipeline. Measures are defined
                in each subsequent artifact's own spec.

OUTPUTS:        CHARTER.md            the programme's scope and commitments
                README.md             repository front door
                docs/SOURCES.md       verified source register
                docs/STANDARDS.md     reproducibility and publication standards
                docs/ARTIFACTS.md     artifact index (empty at v0.1.0, by design)
                docs/ROADMAP.md       planned work, marked as planned
                docs/VERIFY_CHECKLIST.md
                code/01_snapshot_registers.py   register preservation harvester
                code/provenance.py              fetch logging
                site/index.html       the public programme site

VENUES:         GitHub repository and Pages site (the project URL of record);
                Zenodo deposit with a concept DOI covering all versions.

VERIFY POINTS:  1. The charter describes a programme the author is willing to
                   be held to in public and at petition time.
                2. The scope boundary — U.S. spine plus a named comparative
                   strand — is the scope she actually wants.
                3. The artifact index claims nothing that does not exist.
                4. The licences are the ones she intends to grant.
                5. The harvester runs on her machine against the live
                   endpoints, which could not be tested from the build sandbox.

LICENSE:        Code: MIT. Data and documents: CC BY 4.0.

DECISIONS:      - Code under MIT; data and documents under CC BY 4.0.
                - U.S. measurement as the spine, with a named comparative strand
                  carrying the cocoa-economy and international certification
                  work, so that existing and planned comparative papers sit
                  inside the programme rather than outside it.
                - Repository under the maintainer's personal account at
                  github.com/Tlayem/farm-share-evidence, with the public site
                  served by GitHub Pages.
                - Monthly register snapshots run as a scheduled GitHub Actions
                  workflow rather than by hand, so the preservation archive does
                  not depend on anyone remembering.
                - No funding, no institutional sponsorship, no conflicts of
                  interest at the founding date.
```

## What v0.1.0 deliberately does not contain

No datasets, no DOIs, no download counts, no adoption figures, no software
releases, no reports. None of those existed on 15 September 2026, and the
programme's own standards forbid listing them before they do. The artifact
index is empty because an empty index that is true is worth more than a full
one that is not — and because this repository will be read, eventually, by
people whose job is to check.

*Updated 18 September 2026: v0.1.0 was released and deposited, and the programme
now has a DOI (10.5281/zenodo.22834813, concept). That is the charter and the pipeline being
citable. The artifact index is still empty, and still true.*
