# 🚀 Getting Started

## Prerequisites
- Python 3.10 or newer.
- pip.
- Git.
- A browser for Jupyter Notebook.

## Clone and enter the project

```bash
git clone https://github.com/Brajesh31/Breast_Cancer_Detection.git
cd Breast_Cancer_Detection
```

## Create an isolated environment

Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install packages and launch

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter notebook
```

Open `Breast_Cancer.ipynb`. Start Jupyter from the repository root so the relative CSV path resolves.

## First-run checklist
- [ ] Confirm Python version.
- [ ] Confirm the notebook and CSV are present.
- [ ] Review the non-clinical-use warning.
- [ ] Restart the kernel before running all cells.
- [ ] Record package versions if reproducing an experiment.

This setup launches a local educational notebook. It does not start a web service or diagnostic application.
