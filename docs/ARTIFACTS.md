# Artifact index

Every released artifact of the Farm Share Evidence Program, with its permanent
identifier. This is the index a reader, a reviewer, or an adjudicator uses to
check what the programme has actually produced.

**An artifact appears here only when it is released and resolvable.** Not when
it is drafted, not when it is submitted, not when it is accepted. Planned work
lives in `ROADMAP.md` and is marked as planned. This rule is standard 6 of the
charter and it has no exceptions.

---

## Released artifacts

Status as of 1 October 2026. **One** released research artifact.

| Released | Artifact | Type | Version | DOI (version) | DOI (concept) | Repository | Licence |
|---|---|---|---|---|---|---|---|
| 2026-09-21 | Retailer Churn and Food Access | Working paper + replication package (intermediation strand) | 0.1.0 | [10.5281/zenodo.22884651](https://doi.org/10.5281/zenodo.22884651) | [10.5281/zenodo.22884650](https://doi.org/10.5281/zenodo.22884650) | [Tlayem/retailer-churn](https://github.com/Tlayem/retailer-churn) | MIT (code), CC BY 4.0 (data, documents) |

> Adesiyan, T. F. (2026). *Retailer Churn and Food Access* (Version 0.1.0).
> Working paper. Zenodo. https://doi.org/10.5281/zenodo.22884651

Technical comments filed in public dockets in the maintainer's individual
capacity are added here once the agency has posted them publicly, with the
docket's own identifier in place of a DOI.

---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

---

## Preservation archive

Not an artifact, and deliberately listed separately: the register snapshot
archive is running infrastructure, not a release. It becomes a citable artifact
only when a version of it is packaged, documented, and deposited.

| Register | Snapshotting began | Cadence | Months held | Deposited |
|---|---|---|---|---|
| USDA Local Food Directories (5 registers) | 18 September 2026 | monthly | 1 complete (2026-09); 2026-10 partial backstop only, complete capture not yet taken | no |

**2026-09** holds five complete captures (`.xlsx`, browser download, 27,891
listings, matching USDA's published totals exactly) and five partial ones
(`.csv`, automated API run, 30–80% of each register). The complete capture is
the archive's; the partial one is kept because the provenance log records it.
See CHARTER.md standard 9.

Update this table from `data/raw/PROVENANCE.txt` at each release. The counts are
read from the provenance log, never typed from memory.

---

## How to cite the programme

The programme itself is deposited and citable, which is a different thing from
having released research artifacts. Those are listed above.

> Adesiyan, T. F. (2026). *The Farm Share Evidence Program* (Version v0.1.0)
> [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.22834814

Two DOIs exist and they are not interchangeable:

| | DOI | Resolves to |
|---|---|---|
| **Concept** | `10.5281/zenodo.22834813` | whatever the newest version is |
| **Version** | `10.5281/zenodo.22834814` | v0.1.0, permanently |

Cite the **concept DOI** when referring to the programme, so the citation does
not go stale. Cite the **version DOI** when the exact state of the work matters —
reproducing a result, or quoting a figure that a later version might revise.
