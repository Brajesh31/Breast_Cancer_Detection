# 🔎 Dataset Provenance, Quality and Attribution

## 1. What is present

The repository includes `breast-cancer.csv`. Its 569-row, 32-column structure and diagnosis labels match the published UCI Breast Cancer Wisconsin (Diagnostic) dataset.

## 2. What is not verified

The repository does not preserve the exact URL used to obtain this copy, download date, original checksum, or acquisition log. It is therefore accurate to say the schema matches the UCI dataset, but not accurate to claim that this exact file has verified provenance.

## 3. Suggested source citation

Wolberg, W., Mangasarian, O., Street, N., & Street, N. (1993). *Breast Cancer Wisconsin (Diagnostic)* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5DW2B.

Canonical source: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic

UCI lists the dataset under CC BY 4.0. Verify that this precise local file is the same source artifact and check current license terms before redistribution.

## 4. Validation contract

The current repository contract expects:
- 569 rows and 32 columns.
- One identifier column named `id`.
- One diagnosis column named `diagnosis`.
- Diagnosis values limited to `B` and `M`.
- 357 benign and 212 malignant rows.
- No missing values, duplicate records, or duplicate identifiers.

These are checks against the current snapshot, not claims about every version of the upstream dataset.

## 5. Reproducible data changes

For a changed dataset, record:
1. Source title, publisher, URL, and version.
2. Retrieval date and acquisition method.
3. License and attribution.
4. File checksum.
5. Row and column counts before and after changes.
6. Cleaning, filtering, imputation, and relabeling steps.
7. Quality checks and exceptions.
8. Privacy and redistribution review.

Use [Dataset change template](templates/dataset-change-template.md).

## 6. Licensing boundary

The root MIT license does not automatically license the CSV or other third-party assets. Read [LICENSE-DATA.md](../LICENSE-DATA.md) before copying or redistributing the data.
