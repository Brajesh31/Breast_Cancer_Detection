# 🧪 Data Validation

## Purpose

Data validation checks that the local CSV matches the structural assumptions documented by the project. It is not a label audit, scientific review, model evaluation, or clinical validation.

## Current snapshot contract

| Check | Expected value |
|---|---|
| Rows | 569 |
| Columns | 32 |
| Identifier | `id` |
| Target label | `diagnosis` |
| Allowed labels | `B`, `M` |
| Benign count | 357 |
| Malignant count | 212 |
| Missing values | 0 |
| Duplicate rows | 0 |
| Duplicate identifiers | 0 |

## Run validation

```bash
python scripts/validate_dataset.py
```

The script reports a non-zero exit code if the file is missing or does not match the documented contract. Update the contract only when a data change is intentional and supported by provenance and validation evidence.

## What the check cannot prove

- The diagnosis labels are medically correct.
- The data is representative of a current clinical population.
- The file was obtained from the claimed source.
- A model trained on it will generalize.
- The dataset is suitable for patient care.
