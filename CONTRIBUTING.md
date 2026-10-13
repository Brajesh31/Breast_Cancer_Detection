# Contributing

Thank you for considering a contribution. This repository is an educational notebook project. Contributions should improve clarity, reproducibility, data attribution, or the correctness and safety of the analysis.

## Before changing the project

- Read the [Code of Conduct](CODE_OF_CONDUCT.md), [Security Policy](SECURITY.md), and [License](LICENSE).
- Review the current [README](README.md) and [Roadmap](ROADMAP.md).
- Confirm the provenance and terms for any new data or artifacts. Never assume the repository's MIT license applies to a dataset.
- For substantial notebook or modeling changes, open an issue first to agree on scope and evaluation expectations.

## Development setup

Use Python 3 with a virtual environment. Install the notebook dependencies described in [Installation](docs/installation.md), then launch Jupyter from the repository root so the relative path to **breast-cancer.csv** works.

The repository currently has no requirements file, environment lock, automated test suite, or production training script. Record the environment and relevant package versions when proposing a result.

## Notebook and data practices

- Keep the notebook narrative consistent with what the executed cells actually do.
- Do not report toy examples or outputs using labels such as clinical accuracy.
- Split labels from features explicitly. Use **diagnosis** as the target only when that is the stated task; exclude **id** from predictive features.
- Fit preprocessing on training data only. Use a stratified split or cross-validation where appropriate, and avoid using held-out test data for tuning.
- Include meaningful classification metrics and class-specific results; explain the limits of the small, imbalanced benchmark.
- Do not claim clinical utility or make treatment or screening recommendations.
- Preserve the CSV unless a change is intentional and documented. Do not commit private, patient-identifiable, or otherwise restricted data.
- Clear irrelevant notebook outputs and metadata, but retain outputs when they are necessary to understand a documented result.

## Pull request checklist

Include a clear summary, motivation, and links to relevant issues. For analysis changes, explain the target, features, preprocessing, split strategy, random seed, evaluation metrics, and environment. State which notebook cells or checks you ran. Include provenance and required citation for data changes. Identify any privacy, security, or medical-use implications.

Keep each pull request focused and reviewable. Do not bundle unrelated notebook reformatting with model or data changes.
