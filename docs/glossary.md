# 📚 Project Glossary

| Term | Meaning in this repository |
|---|---|
| Attribute / feature | An input column considered for descriptive analysis or a future model. |
| Benign | The dataset label `B`; it is not a guarantee about an individual. |
| Malignant | The dataset label `M`; it is not an individual diagnosis. |
| Target / label | The outcome a supervised learning experiment is designed to predict. |
| Identifier | A row key such as `id`; normally excluded from model features. |
| Data leakage | Information unavailable at the intended prediction time enters training or evaluation. |
| Train/test split | Separation of data used to fit a model from data reserved for evaluation. |
| Stratification | Preserving approximate class proportions when splitting data. |
| Pipeline | A sequence of transformations and an estimator fitted together. |
| Cross-validation | Repeated training and validation across folds to estimate variability. |
| Sensitivity / recall | Fraction of actual positive cases correctly identified. |
| Specificity | Fraction of actual negative cases correctly identified. |
| Precision | Fraction of predicted positive cases that are actually positive in the evaluation labels. |
| Calibration | Agreement between predicted probabilities and observed event frequencies. |
| External validation | Evaluation on data collected independently from the development dataset. |
| Model card | A structured description of a model's intended use, evaluation, limitations, and risks. |
| Clinical validation | Evidence that a system performs safely and usefully in a defined clinical context. |
| Reproducibility | Ability to reconstruct an analysis from recorded data, environment, code, and procedure. |

Terminology is educational. Metric definitions do not imply that a valid clinical model exists in this repository.
