# Frequently asked questions

## What is in this repository?

A Jupyter notebook and a CSV table for an educational exploration of the Breast Cancer Wisconsin Diagnostic dataset. It is not a web application or a deployable diagnostic service.

## What does the CSV contain?

It has 569 rows, one sample ID column, one diagnosis column, and 30 numeric measurements. The labels are **M** for malignant and **B** for benign. The local class counts are 212 malignant and 357 benign.

## Where did the data come from?

The row count and schema match the UCI Machine Learning Repository's Breast Cancer Wisconsin (Diagnostic) dataset. The repository does not record the download source for its exact CSV copy, so its provenance has not been verified. UCI lists its dataset under CC BY 4.0; review the [README data note](../README.md#data-provenance-and-attribution) and verify the copy's terms before redistribution.

## Is the displayed 1.0 accuracy valid?

No. The section labeled “Logistic Regression” uses a synthetic example and copies the known labels into predictions. The score is therefore tautological and is not a breast-cancer model result.

## Does the notebook currently train a valid cancer classifier?

No. The later model split uses the last feature, **fractal_dimension_worst**, as its target and retains diagnosis among the input columns. It does not correctly evaluate diagnosis. See [Architecture](architecture.md) and [Development](development.md).

## Can I use this for diagnosis or treatment?

No. The notebook is an unfinished educational exercise and has not been clinically validated. Do not use it for screening, diagnosis, treatment, or patient-care decisions.

## How do I run the notebook?

Create a Python virtual environment, install the packages in [Installation](installation.md), and launch Jupyter from the repository root. The notebook needs the CSV file to be available at its relative path.

## Why does a recent scikit-learn version fail in the RMSE cell?

The notebook uses the removed **squared=False** argument to **mean_squared_error**. Replace it with **root_mean_squared_error** when updating the notebook. Details are in [Troubleshooting](troubleshooting.md).

## Does this project store personal data or expose an API?

No. There is no database, data submission flow, or project API. The checked-in CSV is a local benchmark dataset; do not add identifiable patient data.
