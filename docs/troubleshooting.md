# Troubleshooting

## The CSV cannot be found

The notebook reads **breast-cancer.csv** relative to the notebook process's current working directory. Start Jupyter from the repository root, where both **Breast_Cancer.ipynb** and **breast-cancer.csv** are located. Restart the kernel after changing directories.

## A Python package cannot be imported

Activate the intended virtual environment, then install notebook dependencies from [Installation](installation.md). In the notebook, verify that the selected kernel uses the same Python environment where the packages were installed. Restart the kernel after changing packages.

## The RMSE cell rejects the squared argument

The notebook calls **mean_squared_error(..., squared=False)**. Scikit-learn deprecated this parameter in version 1.4 and removed it in version 1.6. Update the cell to use **root_mean_squared_error**, or use a compatible older environment while clearly recording its versions. Refer to the official [scikit-learn 1.5 metric reference](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.mean_squared_error.html).

## The “Logistic Regression” result says 1.0

That section uses a synthetic eight-row toy dataset. It assigns the true target column directly to the variable called predictions, so accuracy is guaranteed to be 1.0 by construction. It does not fit LogisticRegression and does not evaluate the breast-cancer CSV. Do not cite this number as model performance.

## The linear regression output does not classify diagnosis

The existing split chooses the last CSV column, **fractal_dimension_worst**, as its target. It also leaves **diagnosis** in the input columns. This is not the intended classification task, and diagnosis would leak into predictors if used this way. The notebook needs a corrected feature/target split before any classifier score is meaningful.

## Results change between cells or the notebook behaves inconsistently

Notebook cells share mutable state. The synthetic example overwrites the variable **data**, which previously referred to the dataset DataFrame. Restart the kernel and run cells in order. Avoid running only selected cells unless their variables are defined by the current kernel state.

## Warnings do not appear

The notebook globally suppresses warnings. This can hide deprecation or data-quality notices. For debugging, remove or narrow the warning suppression and inspect the first relevant warning.

## Where should I ask for help?

See [Support](../SUPPORT.md). For suspected security issues, use the private reporting channel described in [SECURITY.md](../SECURITY.md).
