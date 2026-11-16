"""Tests for the static educational CSV contract, not model performance."""
from pathlib import Path
import pandas as pd

CSV_PATH = Path(__file__).resolve().parents[1] / "breast-cancer.csv"

def load_frame():
    assert CSV_PATH.is_file(), f"Missing dataset: {CSV_PATH}"
    return pd.read_csv(CSV_PATH)

def test_expected_dataset_shape():
    frame = load_frame()
    assert frame.shape == (569, 32)

def test_expected_diagnosis_labels_and_counts():
    frame = load_frame()
    assert set(frame["diagnosis"].unique()) == {"B", "M"}
    assert frame["diagnosis"].value_counts().to_dict() == {"B": 357, "M": 212}

def test_no_missing_or_duplicate_rows():
    frame = load_frame()
    assert not frame.isna().any().any()
    assert not frame.duplicated().any()

def test_identifier_is_unique():
    frame = load_frame()
    assert frame["id"].is_unique

def test_predictor_boundary_excludes_id_and_target():
    frame = load_frame()
    features = frame.drop(columns=["id", "diagnosis"])
    target = frame["diagnosis"]
    assert features.shape == (569, 30)
    assert len(target) == len(features)
    assert "id" not in features.columns
    assert "diagnosis" not in features.columns
