# 🔐 Security Overview

## Current attack surface

| Component | Security concern | Baseline control |
|---|---|---|
| Jupyter notebook | Arbitrary local Python execution | Review code and isolate runtime |
| CSV input | Malformed or altered values | Validate schema and integrity |
| Python packages | Supply-chain vulnerabilities | Review dependencies and audit |
| GitHub Actions | Token and workflow permissions | Minimal read-only permissions |
| Notebook outputs | Accidental secret/data disclosure | Review before committing |
| Project claims | Misleading medical interpretation | Explicit non-clinical boundary |

## Not present

There is no web server, API, database, authentication, user-upload service, or production inference endpoint. Security documentation must not imply these components exist.

## Contributor controls

- Do not commit secrets or sensitive health data.
- Review notebook code before execution.
- Use virtual environments.
- Review workflow changes and dependency updates.
- Report vulnerabilities privately.
- Do not expose an unauthenticated notebook server to untrusted networks.

See [SECURITY.md](../SECURITY.md) for reporting instructions and [Threat model](threat-model.md) for scenarios and mitigations.
