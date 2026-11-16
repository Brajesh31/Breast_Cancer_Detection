# 🗂️ Project Structure and File Responsibilities

This document explains the intended repository layout. It distinguishes existing project artifacts from documentation and quality tooling added around them. It does not imply that the repository has an application server, database, API, or production model.

## 🌳 Directory tree

```text
Breast_Cancer_Detection/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── feature_request.yml
│   │   ├── documentation.yml
│   │   ├── data_issue.yml
│   │   ├── experiment_report.yml
│   │   ├── security_report.yml
│   │   └── config.yml
│   ├── DISCUSSION_TEMPLATE/
│   │   ├── ideas.yml
│   │   └── questions.yml
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── docs-validation.yml
│   │   └── dependency-audit.yml
│   ├── dependabot.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── assets/
│   │   ├── current-notebook-flow.svg
│   │   └── recommended-experiment-flow.svg
│   ├── templates/
│   │   ├── adr-template.md
│   │   ├── experiment-plan-template.md
│   │   ├── dataset-change-template.md
│   │   ├── test-report-template.md
│   │   ├── risk-assessment-template.md
│   │   └── release-checklist.md
│   ├── README.md
│   ├── project-overview.md
│   ├── architecture.md
│   ├── data-dictionary.md
│   ├── dataset-provenance.md
│   ├── modeling-methodology.md
│   ├── evaluation-plan.md
│   ├── known-issues.md
│   ├── testing.md
│   ├── security-overview.md
│   ├── threat-model.md
│   ├── safety-and-responsible-use.md
│   ├── maintenance.md
│   └── release-process.md
├── scripts/
│   ├── validate_dataset.py
│   └── validate_docs.py
├── tests/
│   └── test_dataset_contract.py
├── Breast_Cancer.ipynb
├── breast-cancer.csv
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── SUPPORT.md
├── CHANGELOG.md
├── LICENSE
├── LICENSE-DATA.md
├── requirements.txt
└── pyproject.toml
```

## 📦 Root files

| File | Responsibility |
|---|---|
| `README.md` | Project landing page, safety warning, setup, diagrams and documentation links |
| `Breast_Cancer.ipynb` | Existing interactive exploratory notebook |
| `breast-cancer.csv` | Existing tabular dataset snapshot |
| `requirements.txt` | Direct Python dependencies for notebook execution |
| `pyproject.toml` | Basic project metadata and pytest configuration |
| `LICENSE` | MIT terms for original project code/documentation |
| `LICENSE-DATA.md` | Dataset-specific licensing and attribution notice |
| `CONTRIBUTING.md` | Contribution workflow and technical standards |
| `CODE_OF_CONDUCT.md` | Community behavior expectations |
| `SECURITY.md` | Private vulnerability reporting and security guidance |
| `CHANGELOG.md` | Notable changes |
| `CITATION.cff` | Citation metadata, where applicable |

## ⚙️ Tooling directories

- `.github/ISSUE_TEMPLATE/`: structured issue forms for reproducible reports.
- `.github/workflows/`: automated repository checks. These do not establish clinical validity.
- `docs/assets/`: original SVG workflow illustrations.
- `docs/templates/`: reusable engineering and experiment records.
- `scripts/`: repository validation commands.
- `tests/`: automated tests of the static data contract.

## 🚫 Deliberately absent components

There is no `src/api/`, `frontend/`, database migration, model registry, inference server, authentication service, or deployment infrastructure because these do not exist in the current notebook project. Do not add empty folders or documentation claiming such components are implemented.
