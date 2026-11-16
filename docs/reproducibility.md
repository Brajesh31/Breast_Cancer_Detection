# 🔁 Reproducibility and Experiment Provenance

Reproducibility means another contributor can identify the data, environment, code revision, procedure, and outputs behind an experiment. It does not mean that a repeatable result is clinically valid.

## Required experiment record

For every meaningful modeling or analysis change, record:

1. Git commit SHA and branch.
2. Dataset filename, checksum, source, license, and acquisition date when known.
3. Python and package versions.
4. Random seeds and split strategy.
5. Target column and exact feature inclusion/exclusion rules.
6. Preprocessing steps and where they are fitted.
7. Model family and hyperparameters.
8. Cross-validation design and held-out evaluation protocol.
9. Metrics, confusion matrix, confidence intervals where appropriate.
10. Known limitations, deviations, and reviewer.

Use [the experiment plan template](templates/experiment-plan-template.md) and [the test report template](templates/test-report-template.md).

## Environment capture

Create and activate a virtual environment, install the pinned or constrained dependencies, and record the output of:

```bash
python --version
python -m pip freeze
```

Do not commit virtual environments, local secrets, patient information, or large generated artifacts.

## Determinism

Set and record random seeds for randomized operations. Document library versions because numerical behavior can change between releases. Deterministic execution is a reproducibility aid, not a substitute for uncertainty analysis.

## Data integrity

Never silently replace the CSV. Verify its source, license, schema, row count, and checksum. A dataset update requires a completed dataset-change template and review of downstream results.

## Notebook hygiene

Restart the kernel and run all cells before treating notebook outputs as current. Clear misleading stale outputs. Review generated diffs because notebooks can contain large output payloads.

## Limits

This repository currently does not provide a fully reproducible, validated diagnosis-classification experiment. Follow the known-issues register and modeling methodology before adding performance claims.
