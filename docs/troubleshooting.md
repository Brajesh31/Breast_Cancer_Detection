# 🧯 Troubleshooting

## CSV file not found

**Cause:** Jupyter was started from a different working directory.

**Fix:** Open a terminal in the repository root and run `jupyter notebook` there.

## Module not found

**Cause:** The active Python interpreter does not have the project dependencies.

**Fix:**
```bash
python -m pip install -r requirements.txt
python -m pip show pandas scikit-learn notebook
```

## Notebook variables have unexpected values

**Cause:** Jupyter retains state between cell executions. This notebook also reuses the name `data` for different types.

**Fix:** Restart the kernel and run cells from the beginning. Do not run later cells against stale state.

## scikit-learn rejects squared=False

**Cause:** The `squared` parameter was removed from `mean_squared_error` in scikit-learn 1.6.

**Fix:** Use `root_mean_squared_error` in a compatible updated cell, or reproduce using a documented older environment.

## A 1.0 score appears

**Cause:** The toy logistic section copies true labels into predictions.

**Fix:** Do not interpret or quote this as model accuracy. See [Known issues](known-issues.md).

## Notebook warnings disappear

**Cause:** The notebook suppresses warnings globally.

**Fix:** Remove blanket suppression during debugging and address each warning.

## Tests fail after a dataset update

**Cause:** The static data contract expects 569 rows, 32 columns, and the documented class counts.

**Fix:** Verify the new source and license, inspect schema changes, update the validation contract and documentation, and include a dataset change record. Do not weaken checks just to force a green build.
