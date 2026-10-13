# Roadmap

This roadmap describes possible project improvements. It is not a schedule or a claim that these features are already implemented.

## Current baseline

The repository contains one Jupyter notebook and a local CSV with 569 samples and 30 numeric measurements. The notebook is exploratory and has a synthetic placeholder “Logistic Regression” example plus a regression section that does not use diagnosis as the target. Its displayed 1.0 score is not evidence of model performance.

## Potential improvements

### Correct and reproducible analysis

- Separate diagnosis from the feature matrix and exclude the identifier.
- Replace the synthetic logistic-regression demonstration with a real classifier trained on the dataset.
- Use a stratified train/test split, fit preprocessing on training data only, and report class-specific metrics and a confusion matrix.
- Add cross-validation and uncertainty discussion without repeatedly tuning against the test set.
- Replace deprecated metric usage and record a reproducible dependency environment.

### Data provenance and documentation

- Record the exact source and version for the checked-in CSV and verify its license and attribution.
- Add a clear data citation and document any changes to the data.
- Explain all 30 measurements and the target encoding in the notebook.

### Maintainability and responsible use

- Extract reusable analysis into a small Python module only if it improves clarity.
- Add lightweight checks for the data schema and target labels.
- State limitations and non-clinical intended use wherever results are displayed.
- Review accessibility and readability of generated plots and notebook narrative.

## Proposing work

Open an issue with the user need, expected scope, validation approach, and any new data or package dependencies. Any future clinical or patient-facing use would require a separate, rigorous validation and governance process and is outside this notebook's current scope.
