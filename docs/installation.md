# Installation

This guide sets up a local environment to inspect and run the Jupyter notebook.

## Requirements

- Python 3.
- pip, included with standard Python distributions.
- A terminal and a web browser.
- Internet access for the initial package installation.
- The repository files **Breast_Cancer.ipynb** and **breast-cancer.csv**.

The repository does not include **requirements.txt**, a Conda environment file, or a dependency lockfile, so a fresh install is not currently version-reproducible.

## Create a virtual environment

Run these commands from the repository root.

Windows PowerShell:

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

macOS or Linux:

    python3 -m venv .venv
    source .venv/bin/activate

Upgrade pip and install the packages imported by the notebook:

    python -m pip install --upgrade pip
    python -m pip install numpy pandas matplotlib seaborn scikit-learn notebook

Installing a newer scikit-learn may expose the notebook's outdated RMSE call: **mean_squared_error(..., squared=False)**. The **squared** parameter was deprecated in scikit-learn 1.4 and removed in 1.6; use **root_mean_squared_error** in updated code. See the official [scikit-learn 1.5 metric reference](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.mean_squared_error.html) and [current root mean squared error reference](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html).

## Start Jupyter

Start the notebook server from the repository root so its relative CSV path resolves:

    jupyter notebook

Open **Breast_Cancer.ipynb** in the browser and execute cells in order. Keep the Jupyter process running while using the notebook. The notebook has no command-line entry point.

## Deactivate

When finished, stop Jupyter with Ctrl+C in its terminal and leave the virtual environment with:

    deactivate

Remove the local **.venv/** directory only if you want to discard the installed environment; it can be recreated with the steps above.
