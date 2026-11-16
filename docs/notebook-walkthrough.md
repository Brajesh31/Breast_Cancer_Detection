# 📓 Notebook Walkthrough

## Before running

Read the repository [README](../README.md) and [Known issues](known-issues.md). Use an isolated environment and start Jupyter from the repository root.

## Notebook sections

The notebook is an exploratory artifact. Its cell order and saved outputs may change. This guide describes the broad operations, not a guarantee that every output is current.

1. **Imports:** loads Python data-science libraries.
2. **CSV loading:** reads `breast-cancer.csv` with pandas.
3. **Initial inspection:** prints shape, column names, data types, null counts, duplicate checks, and descriptive summaries.
4. **Label transformation:** maps diagnosis values for numerical exploration.
5. **Feature exploration:** inspects selected columns and creates plots.
6. **Split and regression example:** currently selects the final measurement column as target rather than diagnosis.
7. **Toy logistic section:** creates a separate synthetic table and copies true labels into predictions. Its score is not a trained model result.

## Kernel state warning

Jupyter cells share variables. The notebook reuses the name `data` for different object types. Restart the kernel and run all cells in order when reviewing modifications.

## Interpretation warning

Do not interpret any notebook metric as a cancer-detection accuracy claim. The model examples need correction and a valid evaluation design before even an educational benchmark score can be reported.
