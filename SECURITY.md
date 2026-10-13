# Security Policy

## Scope

This repository contains a Jupyter notebook and a local CSV dataset. It does not provide a deployed application, service endpoint, authentication system, database, or online prediction API. Reports about repository code, unsafe notebook behavior, dependency risks, or accidental exposure of restricted data are still welcome.

## Report a vulnerability

Please do not publish unpatched vulnerability details, private data, or exploit instructions in a public issue. Use GitHub's private vulnerability reporting for this repository if it is enabled: [Report a vulnerability](https://github.com/Brajesh31/Breast_Cancer_Detection/security/advisories/new). If that channel is unavailable, contact the maintainer privately through [@brajesh31](https://github.com/brajesh31) and request a private reporting channel.

Include affected files or dependency versions, the conditions needed to reproduce the issue, likely impact, and a suggested mitigation. Do not attach real patient information, credentials, or unrelated secrets.

## Response

The maintainer will acknowledge reports when reasonably able, investigate the affected revision, and coordinate a fix and disclosure with the reporter. This personal project does not promise a response-time or service-level commitment.

## Safe use

- Treat notebooks as executable code; review cells before running notebooks from untrusted sources.
- Do not commit credentials, private datasets, or personally identifiable health information.
- Review dependency changes and use a virtual environment.
- Do not deploy the exploratory notebook as a clinical decision system. It has no validated clinical model.
