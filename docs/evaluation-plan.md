# 📏 Evaluation Plan for Future Educational Experiments

## Status

No valid diagnosis-classification evaluation is currently established. This is a proposed plan and reporting standard, not a claim that experiments have been run.

## 1. Evaluation question

State the prediction task, target label, positive class, intended educational question, and what the experiment does not attempt to establish.

## 2. Data partitioning

- Confirm dataset provenance and schema.
- Inspect duplicate and missing-value patterns.
- Separate `diagnosis` from predictors and exclude `id`.
- Use a stratified train/test split where appropriate.
- Record the random seed and partition sizes.
- Keep the final test partition untouched during model selection.

## 3. Training and validation

Use training-only cross-validation for preprocessing and model selection. Learned transformations must be fitted inside each fold. Document all candidate models and tuning ranges. Avoid selecting a model based on the held-out test result.

## 4. Metrics

| Metric | Why report it | Caution |
|---|---|---|
| Confusion matrix | Counts of each outcome | Define class ordering |
| Recall / sensitivity | Missed positive cases | Specify positive class |
| Specificity | Correctly rejected negative cases | Depends on class definition |
| Precision | Reliability of positive predictions | Depends on prevalence |
| F1-score | Precision/recall balance | Hides some error trade-offs |
| ROC-AUC | Ranking across thresholds | Does not establish calibration |
| PR-AUC | Precision/recall trade-off | Sensitive to prevalence |

Report per-class metrics and sample counts. Do not publish a single headline accuracy without context.

## 5. Uncertainty and robustness

Where feasible, include confidence intervals or resampling-based uncertainty, sensitivity to split seed, and error analysis. Do not overstate stability from one small dataset. External validation on genuinely independent data would be needed for claims beyond this benchmark.

## 6. Reporting template

- Experiment ID and commit SHA:
- Dataset source, version and checksum:
- Python and dependency versions:
- Target and positive class:
- Excluded columns:
- Split method and seed:
- Preprocessing pipeline:
- Estimator and parameters:
- Cross-validation design:
- Held-out metrics:
- Confusion matrix:
- Uncertainty:
- Limitations:
- Reproduction command and evidence:

## 7. Interpretation

Metrics describe performance on the evaluated sample under the specified protocol. They do not establish clinical benefit, safety, or suitability for an individual. This repository is not a clinical decision support system.
