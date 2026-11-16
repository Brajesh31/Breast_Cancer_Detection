.PHONY: install install-dev dataset-check docs-check test lint quality notebook

PYTHON ?= python

install:
	$(PYTHON) -m pip install -r requirements.txt

install-dev:
	$(PYTHON) -m pip install -r requirements.txt -r requirements-dev.txt

dataset-check:
	$(PYTHON) scripts/validate_dataset.py

docs-check:
	$(PYTHON) scripts/validate_docs.py

test:
	$(PYTHON) -m pytest -q

lint:
	$(PYTHON) -m ruff check .

quality: dataset-check docs-check lint test

notebook:
	$(PYTHON) -m jupyter notebook
