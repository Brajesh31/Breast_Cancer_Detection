# 🪪 Model Card and Intended-Use Statement

## Status

**No validated diagnosis model is currently released by this repository.** The existing notebook contains demonstrations with methodological defects. This document is an explicit status record, not a claim that a usable model exists.

## Project identity

- Project: Breast Cancer Detection & Data Analysis
- Artifact type: Educational notebook and tabular-data exploration
- Dataset snapshot: `breast-cancer.csv`
- Current model status: Not approved, not validated, not suitable for deployment

## Intended use

The repository may be used to learn data inspection, visualization, notebook workflows, and the principles of leakage-aware model evaluation.

## Out-of-scope use

Do not use this project or any output to screen, diagnose, rule out disease, estimate an individual's risk, triage patients, recommend treatment, or support clinical decisions.

## Data and population

The local CSV contains 569 rows and a diagnosis label. Its schema matches the UCI Breast Cancer Wisconsin (Diagnostic) dataset, but the exact acquisition history of this copy is not documented. Dataset-level representativeness and suitability for present-day clinical practice have not been established.

## Performance

No trustworthy model performance is reported. A score produced by copying known labels into predictions is tautological and must not be described as model accuracy.

## Known limitations

- No independent external validation.
- No clinical workflow evaluation.
- No subgroup fairness assessment.
- No calibration or decision-curve analysis.
- No prospective study or regulatory review.
- No established model artifact or inference service.

## Monitoring and change control

Any future experiment must have a documented data split, leakage review, preprocessing pipeline, class-specific metrics, uncertainty reporting, reproducible environment, and independent review. A future model card must identify the exact dataset version, code revision, model parameters, and evaluation cohort.

## Review checklist

- [ ] Intended use and prohibited use are explicit.
- [ ] Dataset provenance and permissions are verified.
- [ ] Target and features are separated correctly.
- [ ] Leakage and split integrity are reviewed.
- [ ] Metrics include sensitivity, specificity, precision, recall, and confusion matrix.
- [ ] Subgroup limitations and uncertainty are reported.
- [ ] Independent external validation is complete before any clinical claim.
