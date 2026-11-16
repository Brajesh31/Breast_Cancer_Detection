# 🧪 Testing and Quality Assurance

## Testing scope

The repository quality checks cover the static dataset contract and Markdown documentation. They do not certify notebook execution, model validity, data correctness, or clinical safety.

## Local checks

```bash
python scripts/validate_dataset.py
python scripts/validate_docs.py
python -m pytest -q
```

## Test layers

| Layer | What is checked | What is not proven |
|---|---|---|
| Dataset script | File shape, columns, labels, nulls and duplicates | Label truth or representativeness |
| Documentation script | Local Markdown links and balanced code fences | Accuracy of every statement |
| Pytest | Dataset contract and feature boundary examples | Model performance |
| Notebook manual run | Cell execution and output review, when performed | Clinical validity |
| Workflow | Automated execution of configured checks | Production readiness |

## Notebook verification protocol

1. Create a clean virtual environment.
2. Install dependencies.
3. Start Jupyter at repository root.
4. Restart the kernel and run all cells.
5. Record Python and package versions.
6. Inspect warnings, plots, and outputs.
7. Record failures and untested sections.

Do not state that notebook execution passed unless it was actually performed in the target environment.

## Evidence format

Record commit SHA, date, operating system, Python version, command, exit code, result, and relevant logs. Remove secrets and personal data before sharing.
