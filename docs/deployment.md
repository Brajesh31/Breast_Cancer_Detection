# Deployment

## Current status

This repository does not define an application that can be deployed as a service. It has no web interface, prediction endpoint, server process, model artifact, API, database, authentication, monitoring, or deployment workflow. The Jupyter notebook is an exploratory artifact.

## Sharing the notebook

For educational sharing, publish the source repository and its documentation. A notebook viewer may render saved markdown, code, and cell outputs without executing the code. Before sharing:

- Remove unintended personal paths, credentials, and sensitive cell output.
- Make clear that the analysis is not a clinically validated diagnostic model.
- Correct the target split and evaluation before reporting any model result.
- Include the exact data citation and verify the checked-in CSV's source and terms.
- Record the Python and package versions used for any reproducible result.

Running an interactive Jupyter server is different from publishing a static notebook. Do not expose an unauthenticated notebook server to the public internet; notebook kernels can execute arbitrary code with the server user's permissions.

## Model or clinical deployment

The current notebook must not be deployed for screening, diagnosis, treatment, triage, or other patient-care use. Its model examples do not validly evaluate diagnosis and no clinical validation is supplied. Turning this project into a patient-facing or clinical system would require a separate design, privacy and security assessment, data governance, independent validation, monitoring, and appropriate regulatory and clinical review. None of those capabilities are implemented here.

## Rollback

Each documentation change is committed separately. A maintainer can revert an individual documentation commit or restore the last known-good repository revision.
