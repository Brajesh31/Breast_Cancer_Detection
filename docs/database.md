# Database and data handling

## Storage model

There is no database or persistent application service. The repository stores its input table in **breast-cancer.csv** and analysis code and outputs in **Breast_Cancer.ipynb**. Notebook variables live in the Jupyter kernel's memory while it is running. Saved cell outputs and execution metadata are stored in the notebook file when it is saved.

## Dataset columns

The CSV contains 569 samples and 32 columns:

- **id**: sample identifier; it should not be used as a predictive feature.
- **diagnosis**: source label, with **M** meaning malignant and **B** meaning benign.
- 30 numeric measurements: ten cell-nucleus characteristics (radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, and fractal dimension), each represented as mean, standard error, and worst value.

The local file has 357 **B** records and 212 **M** records. The notebook maps **M** to 1 and **B** to 0 in memory; this mapping is not written back to the CSV.

## Data origin and rights

The row count and schema correspond to the UCI Machine Learning Repository's [Breast Cancer Wisconsin (Diagnostic)](https://archive.ics.uci.edu/dataset/17/breast-cancer) dataset. The repository does not document the origin of this particular CSV copy, so its exact provenance remains unverified. UCI identifies its dataset as CC BY 4.0 and provides the citation in the [project README](../README.md#data-provenance-and-attribution). Verify the origin and applicable terms for this exact file before redistribution.

The MIT license in the repository applies to the project's original code and documentation, not automatically to the dataset or other third-party material.

## Privacy and handling

This repository is a static educational dataset and does not collect visitor or patient submissions. Do not replace the file with identifiable patient data or add private health information. If future work introduces data collection or persistent storage, document purpose, lawful basis, consent where applicable, retention, access controls, deletion, backups, and security review before implementation.
