# 📦 Installation and Environment Setup

## Supported environment

Python 3.10+ is specified in project metadata. CI is configured for Python 3.11. This is not a guarantee that every dependency combination has been tested across all operating systems.

## Virtual environment

```bash
python -m venv .venv
```

Activate on Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

Activate on macOS/Linux:
```bash
source .venv/bin/activate
```

## Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Verify installation

```bash
python --version
python -m pip list
jupyter --version
```

## Compatibility note

The existing notebook calls `mean_squared_error(..., squared=False)`. scikit-learn removed this argument in version 1.6. If the affected cell is executed with a newer release, replace it with `root_mean_squared_error` or use a documented compatible environment.

## Reproducibility

`requirements.txt` declares direct dependencies but does not pin every transitive dependency. For a reproducible experiment, record the OS, Python version, package versions, and repository commit. A future lockfile should be generated and tested rather than fabricated by hand.
