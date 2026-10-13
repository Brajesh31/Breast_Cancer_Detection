# Development

## Working environment

Create and activate a Python virtual environment using [Installation](installation.md), install the notebook dependencies, then start Jupyter from the repository root. The notebook opens **breast-cancer.csv** using a relative filename, so using another working directory may cause a file-not-found error.

## Notebook organization

The notebook currently imports data-science packages, reads and inspects the CSV, maps diagnosis labels, prints selected feature summaries, normalizes a small slice for display, creates plots, splits data, and runs example regression cells. Some imported names are unused. Global warning suppression may also hide compatibility or data-quality warnings.

Notebook cells share state. The name **data** first refers to the loaded and transformed pandas DataFrame; the synthetic “Logistic Regression” cell later reuses that name for a dictionary. Restart the kernel and run from the top when validating a notebook edit so stale variables do not conceal ordering problems.

## Current modeling defects

The existing modeling cells should not be used as a classifier benchmark:

1. The split passes the entire DataFrame rather than explicitly separating the target.
2. The assigned target is the final CSV column, **fractal_dimension_worst**, rather than **diagnosis**.
3. Diagnosis remains in the input columns, so a future diagnosis evaluation using this split would leak the answer into the features.
4. The “Logistic Regression” section uses a synthetic eight-row example and defines predictions as the true target.
5. The notebook reports a 1.0 value for that toy example, not an evaluated cancer model.
6. The linear regression section predicts a continuous feature and thresholds it; it does not evaluate diagnosis classification.

A corrected educational analysis should explicitly drop the identifier, map or encode **diagnosis**, create **X** from predictors only and **y** from diagnosis only, stratify the split, and fit scaling or other preprocessing on training data alone. Model selection should not use the held-out test set. Report sensitivity/recall by class, specificity or confusion-matrix counts, precision, and uncertainty alongside accuracy. A small public benchmark is not clinical validation.

## Editing and reviewing

- Keep descriptions and metric claims aligned with the actual notebook cells and outputs.
- Preserve the data file unless a documented change is intentional.
- Cite and record provenance for any changed or additional dataset.
- Check plots, labels, target encoding, split logic, and notebook execution order.
- Remove unrelated cell output and machine-specific metadata before committing.
- Do not commit credentials or private health data.
- There is no configured test suite, linter, or build step. State the manual checks performed in a contribution.

## Dependency compatibility

The repository has no locked environment. The notebook calls **mean_squared_error** with **squared=False**, which current scikit-learn releases no longer accept. Replace this with **root_mean_squared_error** when modernizing that cell, or otherwise record the supported environment accurately. See [Installation](installation.md).
