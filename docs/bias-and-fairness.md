# ⚖️ Bias, Fairness, and Subgroup Evaluation

## Current status

No subgroup fairness or clinical-equity evaluation has been completed for this repository. The presence of a public benchmark dataset does not establish that it represents the people, institutions, devices, or workflows where a future system might be used.

## Why this matters

Medical datasets can encode selection effects, measurement differences, historical practice patterns, label noise, and population imbalance. Aggregate metrics can hide poor performance for smaller groups.

## Minimum future review

Before making any fairness or generalization claim, a future study must:

- Establish lawful access and documented provenance for all demographic or subgroup attributes.
- Explain why each subgroup variable is relevant and ethically appropriate.
- Predefine subgroup analyses rather than selecting them after seeing results.
- Report sample sizes and uncertainty for each subgroup.
- Compare sensitivity, specificity, false-negative rates, false-positive rates, calibration, and missingness where valid.
- Explain small-sample limitations and avoid overinterpreting unstable estimates.
- Obtain appropriate ethics, privacy, and domain-expert review.

## Do not infer sensitive attributes

Do not infer race, ethnicity, sex, gender, or other sensitive traits from names, images, or proxy variables. Do not add sensitive data to the repository without a lawful basis, documented purpose, safeguards, and appropriate review.

## Reporting standard

Describe observed disparities, confidence intervals, limitations, and unresolved questions. Do not claim a model is fair based on a single metric or because group-level differences were not statistically significant.

## Current conclusion

The repository has no evidence to support claims of fairness, clinical generalizability, or equitable performance. This is an open evaluation requirement, not a positive or negative finding about any population.
