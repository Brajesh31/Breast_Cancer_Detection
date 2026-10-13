# Architecture

## System overview

This repository is a local data-analysis project rather than a deployed application. The notebook reads a CSV from the current working directory, inspects and transforms a pandas DataFrame, and asks Jupyter to display tables, metrics, and plots.

    breast-cancer.csv
          |
          v
    pandas DataFrame
      |         |
      |         +--> summaries and plots in notebook output
      |
      +--> label mapping and exploratory normalization
      |
      +--> current split and model examples
             (not a valid diagnosis evaluation; see below)

No web server, user interface, API, database, background worker, model-serving endpoint, or cloud deployment configuration is present.

## Repository components

| Path | Role |
| --- | --- |
| **Breast_Cancer.ipynb** | Notebook source, markdown narrative, code cells, and saved cell outputs. |
| **breast-cancer.csv** | Local table containing sample ID, diagnosis, and 30 numeric attributes. |
| **README.md** | Project purpose, setup, dataset context, and known limitations. |
| **docs/** | Project-specific design, environment, data handling, and support guides. |

## Dataset shape and labels

The checked-in CSV has 569 rows and 32 columns: an identifier, a diagnosis label, and 30 real-valued measurements. Diagnosis uses **M** for malignant and **B** for benign. The checked-in row count and schema match the UCI Breast Cancer Wisconsin (Diagnostic) dataset, but the repository does not record the download source for this exact file. See [Data and persistence](database.md) and the [README's provenance note](../README.md#data-provenance-and-attribution).

## Notebook flow as currently written

The notebook loads the CSV, prints shape, columns, data types, duplicates, missing-value counts, and descriptive statistics, maps diagnosis to 1/0, and creates plots. It then splits the full DataFrame. The current assignments select every column except the final feature as inputs and use **fractal_dimension_worst** as the target; diagnosis remains in the inputs. Consequently this is not a diagnosis classifier and includes target leakage for the intended diagnosis task.

The section labeled “Logistic Regression” creates a separate eight-row toy DataFrame and sets its predictions equal to the target labels. Its displayed score is therefore a tautology, not a learned result. The next section fits linear regression to the earlier incorrectly selected target. The notebook also overwrites the name **data** with the toy dictionary after the split. These are current implementation facts, not recommended modeling practices.

## Runtime and data boundaries

- The notebook executes locally in a user-controlled Jupyter kernel.
- It reads only the relative CSV path and does not fetch data or send notebook inputs to a project API.
- It has no database or persistent application state.
- It imports NumPy, pandas, Matplotlib, Seaborn, and scikit-learn.
- Notebook cell outputs are stored in the **.ipynb** file when saved.
- The notebook's results are educational and must not guide clinical decisions.

## Intended extension points

A future corrected analysis should create an explicit feature matrix that excludes **id** and **diagnosis**, create a separate diagnosis target, fit all preprocessing on training data, and evaluate with a held-out stratified split or cross-validation. Any model result should include class-specific metrics and clear limitations. See [Development](development.md) and [Roadmap](../ROADMAP.md).
