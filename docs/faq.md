# ❓ Frequently Asked Questions

## Is this a production breast cancer detection system?

No. It is a local educational notebook project. It is not clinically validated and must not be used for patient care.

## Does the repository currently contain a valid diagnosis classifier?

No. The current notebook has incorrect target selection, target leakage for the intended diagnosis task, and a toy section that copies labels into predictions.

## Why does the notebook show 1.0 accuracy?

The displayed value comes from a synthetic example where the predictions are set equal to the true labels. It is tautological and does not measure a trained model.

## What is the target column for a future diagnosis experiment?

The target would be `diagnosis`. The `id` field should be excluded from predictive features.

## Why is the dataset called Wisconsin Diagnostic?

The checked-in schema and row count match the UCI Breast Cancer Wisconsin (Diagnostic) dataset. The exact download provenance of this local file is not recorded.

## Does the MIT license cover the CSV?

Not automatically. Code licensing and dataset licensing are separate. Review [LICENSE-DATA.md](../LICENSE-DATA.md).

## Why does the notebook fail with a scikit-learn error?

The notebook uses `mean_squared_error(..., squared=False)`, an argument removed in scikit-learn 1.6. See [Troubleshooting](troubleshooting.md).

## Is there an API, web app, or database?

No. The current repository contains a notebook and local dataset, not a deployed application.

## How do I contribute?

Read [CONTRIBUTING.md](../CONTRIBUTING.md), follow the [Code of Conduct](../CODE_OF_CONDUCT.md), and open a focused pull request.
