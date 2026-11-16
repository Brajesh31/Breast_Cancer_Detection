# 🗃️ Data Directory Policy

The current dataset snapshot remains at the repository root as `breast-cancer.csv` to preserve compatibility with the existing notebook.

Use this directory only for future, clearly named, licensed data artifacts or metadata that have passed review. Do not move or silently replace the current CSV.

## Before adding data

1. Record source, author or custodian, download date, license, and permitted uses.
2. Verify whether redistribution is allowed.
3. Record schema, row count, checksum, and any transformation.
4. Remove direct identifiers and ensure no personal or confidential health data is included.
5. Update the data dictionary, provenance record, and validation tests.
6. Obtain review before committing.

Large, restricted, sensitive, or externally hosted data should not be committed. Use a documented retrieval process where permitted.

## Current state

No additional data artifact is stored in this directory. The canonical repository CSV is still `../breast-cancer.csv`.
