# 🤝 Contributing to Breast Cancer Detection

Thank you for considering a contribution. This repository is an educational Jupyter and data-analysis project. High-quality contributions make the work more reproducible, understandable, methodologically correct, accessible, and safe.

> [!IMPORTANT]
> This repository is **not a clinical product**. Do not add diagnostic recommendations, patient-facing prediction flows, treatment advice, or unsupported claims of clinical accuracy. Contributions must preserve this boundary.

## 📚 1. Read before contributing

Please review these project policies before opening a pull request:

- [README](README.md), project purpose and current limitations.
- [Code of Conduct](CODE_OF_CONDUCT.md), community expectations.
- [Security Policy](SECURITY.md), private vulnerability reporting.
- [Dataset provenance](docs/dataset-provenance.md), source and licensing requirements.
- [Safety and responsible use](docs/safety-and-responsible-use.md), medical-use boundary.
- [Architecture](docs/architecture.md), current repository design.
- [Roadmap](ROADMAP.md), potential future work.

## 🧭 2. Contribution areas

Useful contributions include:

| Area | Examples | Review expectations |
|---|---|---|
| 📓 Notebook | Clearer narrative, corrected cell order, reproducible analysis | Restart-and-run evidence; no stale outputs |
| 🧪 Methodology | Correct target separation, leakage prevention, validation design | Explicit X/y, training-only preprocessing, justified metrics |
| 📊 Data quality | Schema checks, data documentation, provenance | Source, license, checksum and change record |
| 📚 Documentation | Guides, diagrams, examples, glossary | Accurate, linked, detailed and project-specific |
| ♿ Accessibility | Plot labels, alt text, readable tables | Do not rely on color alone |
| 🔐 Security | Dependency hygiene, safer notebook workflow | Least privilege and no secrets |
| ⚙️ Automation | CI and repository checks | Minimal permissions and honest status reporting |

## 🛠️ 3. Development environment

Use Python 3.10 or newer. Python 3.11 is the CI target.

```bash
git clone https://github.com/Brajesh31/Breast_Cancer_Detection.git
cd Breast_Cancer_Detection
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pytest
```

Launch Jupyter from the repository root:

```bash
jupyter notebook
```

The notebook reads `breast-cancer.csv` by relative path. Starting Jupyter elsewhere can cause a file-not-found error.

## 🌿 4. Branch and commit conventions

Create a focused branch:

```bash
git checkout -b docs/describe-dataset-provenance
```

Suggested branch prefixes:
- `docs/` documentation-only work.
- `fix/` bug fixes.
- `feat/` additive educational functionality.
- `test/` test and validation changes.
- `ci/` automation and workflow changes.
- `refactor/` behavior-preserving code improvements.

Use clear commit messages, for example:

```text
docs: expand dataset provenance guide
fix: separate diagnosis target from predictors
test: validate dataset label distribution
ci: add documentation link checks
```

Keep changes logically grouped. Avoid mixing notebook reformatting, unrelated documentation rewrites, and modeling changes in one pull request.

## 🧬 5. Data and licensing requirements

Before adding, replacing, transforming, or redistributing data:

1. Record the original publisher and canonical source URL.
2. Record dataset version, access date, and acquisition method.
3. Verify license terms and whether redistribution is permitted.
4. Preserve required attribution and citation.
5. Record a checksum where practical.
6. Describe schema changes, filtering, transformations, and row counts.
7. Check for personal, sensitive, or restricted information.
8. Add or update the dataset change record in `docs/templates/dataset-change-template.md`.

The repository's MIT license covers original project code and documentation. It does not automatically cover third-party datasets, papers, images, or model weights. Never add patient-identifiable data or confidential records.

## 🧪 6. Notebook and modeling standards

### Notebook hygiene
- Restart the kernel and run cells from the top when checking a notebook change.
- Keep markdown explanations consistent with executed code.
- Use descriptive variable names and avoid reusing one name for unrelated object types.
- Avoid blanket warning suppression.
- Remove irrelevant output, temporary paths, credentials, and machine-specific metadata.
- Include random seeds where randomness is used.
- State whether a result was actually reproduced in the current environment.

### Target and feature separation
For a diagnosis classification experiment, the intended target is `diagnosis`. The identifier `id` is not a predictive measurement. A minimal separation example is:

```python
target_column = "diagnosis"
X = frame.drop(columns=["id", target_column])
y = frame[target_column]
```

This snippet only illustrates column separation. It is not a complete training or validation pipeline.

### Leakage prevention and evaluation
- Split the dataset before fitting learned transformations.
- Use stratification when appropriate for class labels.
- Fit scaling, imputation, feature selection, and other learned preprocessing only within training folds.
- Use cross-validation on training data for model selection.
- Do not tune repeatedly against the held-out test set.
- Report the class definition, confusion matrix, per-class precision/recall/F1, and justified additional metrics.
- Explain class imbalance, sample size, uncertainty, and known limitations.
- Do not imply that benchmark metrics establish clinical performance.

## 🧾 7. Documentation standards

Documentation contributions should:
- Use descriptive headings and a useful table of contents for long guides.
- Include concrete commands, expected behavior, prerequisites, and troubleshooting where relevant.
- Use Mermaid diagrams for workflows where they clarify real behavior.
- Include file trees where repository navigation is discussed.
- Use emojis consistently as navigational cues, not as decoration in every sentence.
- Distinguish current implementation from recommendations and future plans.
- Link to related repository documents using relative links.
- Avoid invented APIs, services, databases, deployment targets, screenshots, or test results.

Use the templates in [docs/templates](docs/templates/README.md) for architecture decisions, experiments, dataset changes, security reviews, and test reports.

## 🔍 8. Local quality checks

Run the checks relevant to your change:

```bash
python scripts/validate_dataset.py
python scripts/validate_docs.py
python -m pytest -q
```

For notebook changes, additionally:
1. Restart the Jupyter kernel.
2. Run all cells in order.
3. Inspect errors and warnings.
4. Confirm plots and outputs correspond to the current data.
5. Record the environment and exact execution result.

A passing data or documentation test is not a model evaluation or clinical validation.

## 📦 9. Pull request process

1. Open an issue first for broad or methodologically significant changes.
2. Explain the problem, proposed change, and alternatives.
3. Keep the pull request focused.
4. Complete the repository pull request template.
5. Include screenshots only when they genuinely clarify a plot or rendered document. Remove sensitive information.
6. List commands run and their actual outcomes.
7. Explain data provenance and license changes.
8. State any limitations or untested areas.
9. Respond to review feedback and update documentation as needed.

The maintainer may request revisions, additional evidence, or a narrower scope before accepting a contribution.

## ✅ 10. Pull request readiness checklist

- [ ] The change matches the educational scope.
- [ ] No secrets, credentials, patient records, or private data were added.
- [ ] Dataset source and license are documented when relevant.
- [ ] Notebook narrative matches the code and outputs.
- [ ] Diagnosis target and predictor columns are separated correctly for classification work.
- [ ] Preprocessing does not leak information across validation boundaries.
- [ ] Metrics and limitations are accurately described.
- [ ] Documentation links and diagrams are checked.
- [ ] Relevant tests were run and results are reported honestly.
- [ ] No clinical, regulatory, or performance claims are invented.

## 🆘 11. Need help?

For setup questions, see [Installation](docs/installation.md) and [Troubleshooting](docs/troubleshooting.md). For bugs or proposals, use [GitHub Issues](https://github.com/Brajesh31/Breast_Cancer_Detection/issues). For security concerns, follow [SECURITY.md](SECURITY.md).

Thank you for helping make this repository more reliable and responsible.
