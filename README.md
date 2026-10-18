# Breast Cancer Classification Notebook

This repository contains an exploratory Jupyter notebook and a CSV copy of the Breast Cancer Wisconsin Diagnostic dataset. It is a small educational machine-learning exercise, not a clinical system, validated diagnostic model, or source of medical advice.

## Important limitations

The current notebook does not correctly train and evaluate a breast-cancer classifier. Its section labeled “Logistic Regression” builds a tiny synthetic dataset and sets predictions equal to the known labels, so its displayed 1.0 accuracy is tautological and says nothing about the breast-cancer data. The later train/test split uses the last CSV feature, fractal_dimension_worst, as the target, while diagnosis remains among the input columns. That is not the intended diagnosis task and leaks diagnosis into the inputs. The README's former 100% performance claim has therefore been removed.

Treat the notebook as an unfinished exploration. Do not use its outputs to make medical, screening, treatment, or patient-care decisions. A valid model would require a corrected target/features split, training-only preprocessing, appropriate evaluation, independent validation, and clinical review.

## Repository contents

- **Breast_Cancer.ipynb** — the analysis notebook, with exploratory summaries, plots, preprocessing attempts, and incomplete model examples.
- **breast-cancer.csv** — 569 rows with an ID, a diagnosis label, and 30 numeric measurements.
- **docs/** — repository-specific architecture, installation, development, deployment, data, API, troubleshooting, and FAQ documentation.

The diagnosis labels are **M** (malignant) and **B** (benign). The CSV includes 30 measurements derived from cell nuclei: ten characteristics (radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, and fractal dimension), each represented by mean, standard error, and “worst” values. It contains 569 samples: 212 malignant and 357 benign.

## Set up a notebook environment

Use Python 3 and create a virtual environment from the repository root. For example:

    python -m venv .venv

Activate it on Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

On macOS or Linux:

    source .venv/bin/activate

Install the packages imported by the notebook and Jupyter:

    python -m pip install --upgrade pip
    python -m pip install numpy pandas matplotlib seaborn scikit-learn notebook

Start Jupyter:

    jupyter notebook

Open **Breast_Cancer.ipynb** and run cells in order. The notebook reads **breast-cancer.csv** using a relative path, so start Jupyter with the repository as its working directory.

There is no dependency lockfile or requirements file. The notebook uses the scikit-learn argument **squared=False** in **mean_squared_error**; that argument was deprecated in scikit-learn 1.4 and removed in 1.6. With newer releases, replace it with **root_mean_squared_error** before running that cell. See [Troubleshooting](docs/troubleshooting.md) and the official [scikit-learn metric documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html).

## Data provenance and attribution

The CSV schema and its 569-row count match the UCI Machine Learning Repository's [Breast Cancer Wisconsin (Diagnostic)](https://archive.ics.uci.edu/dataset/17/breast-cancer) dataset. This repository does not record where its particular CSV copy was downloaded from, so that match is an informed identification rather than verified file provenance. UCI lists its dataset under CC BY 4.0 and provides a citation to Wolberg, Mangasarian, and Street. Confirm the source and applicable terms for this exact copy before redistributing it; attribution for the UCI dataset does not place the project's code under that dataset license.

Suggested dataset citation: Wolberg, W., Mangasarian, O., Street, N., & Street, W. (1993). *Breast Cancer Wisconsin (Diagnostic)* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5DW2B.

The project code and documentation are licensed under MIT; see [LICENSE](LICENSE). The CSV dataset may have separate terms, as described above.

## Documentation

- [Architecture](docs/architecture.md)
- [Installation](docs/installation.md)
- [Development](docs/development.md)
- [Deployment](docs/deployment.md)
- [API and network behavior](docs/api.md)
- [Database and data handling](docs/database.md)
- [Troubleshooting](docs/troubleshooting.md)
- [FAQ](docs/faq.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Support](SUPPORT.md)
- [Roadmap](ROADMAP.md)

## Maintainer

Brajesh Kumar — GitHub [@brajesh31](https://github.com/brajesh31).

Last updated: 2026-10-18 02:09 UTC
