# September 2026 — what is in this folder

Two captures of the same registers, taken the same day by different routes.
They are not equivalent, and the difference is the point.

## Use these — the complete capture

`agritourism.xlsx` · `csa.xlsx` · `farmersmarket.xlsx` · `foodhub.xlsx` ·
`onfarmmarket.xlsx`

Downloaded by hand from the USDA Data Sharing page on 18 September 2026. Row
counts match USDA's own published totals exactly: 13,569 agritourism, 7,148
farmers market, 4,692 on-farm market, 2,002 CSA, 480 food hub. Between 85 and
264 fields each, including every product, facility, season, production-method
and sales-channel field. No contact email or telephone field exists in these.

## Not these — a partial capture, kept for the record

`agritourism.csv` · `csa.csv` · `farmersmarket.csv` · `foodhub.csv` ·
`onfarmmarket.csv`

Taken by the automated API run before the shortfall was measured. They hold
77%, 38%, 80%, 39% and 30% of their registers respectively, and about nine
fields each. They are kept because `../PROVENANCE.txt` records them with their
hashes, and a provenance log whose entries point at deleted files is worth less
than one that does not. **Do not analyse them.** Later runs write
`*.partial.csv`, which says so in the filename.

See `CHARTER.md` standard 9 and the 18 September entry in `docs/SOURCES.md`.
