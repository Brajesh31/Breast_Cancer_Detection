#!/usr/bin/env python3
"""Validate the documented structural contract of the local educational CSV."""
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "breast-cancer.csv"
FAMILIES = [
    "radius", "texture", "perimeter", "area", "smoothness",
    "compactness", "concavity", "concave points", "symmetry",
    "fractal_dimension",
]
EXPECTED_COLUMNS = {"id", "diagnosis"} | {
    f"{family}_{suffix}"
    for family in FAMILIES
    for suffix in ("mean", "se", "worst")
}

def validate() -> list[str]:
    errors: list[str] = []
    if not CSV_PATH.is_file():
        return [f"Dataset file not found: {CSV_PATH}"]
    try:
        frame = pd.read_csv(CSV_PATH)
    except Exception as exc:
        return [f"Unable to read CSV: {exc}"]

    if frame.shape != (569, 32):
        errors.append(f"Expected 569 rows and 32 columns; found {frame.shape}.")
    missing = EXPECTED_COLUMNS - set(frame.columns)
    extra = set(frame.columns) - EXPECTED_COLUMNS
    if missing or extra:
        errors.append(f"Column mismatch. Missing={sorted(missing)}; extra={sorted(extra)}.")
    if "diagnosis" not in frame:
        return errors + ["Required column 'diagnosis' is missing."]
    if "id" not in frame:
        return errors + ["Required column 'id' is missing."]
    if frame.isna().any().any():
        errors.append("Null values are present.")
    if frame.duplicated().any():
        errors.append("Duplicate rows are present.")
    if frame["id"].duplicated().any():
        errors.append("Duplicate identifiers are present.")
    counts = frame["diagnosis"].value_counts().to_dict()
    if counts != {"B": 357, "M": 212}:
        errors.append(f"Expected label counts B=357 and M=212; found {counts}.")
    return errors

def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"❌ {error}", file=sys.stderr)
        return 1
    frame = pd.read_csv(CSV_PATH)
    print(f"✅ Dataset contract passed: {len(frame)} rows × {len(frame.columns)} columns.")
    print(f"📊 Diagnosis counts: {frame['diagnosis'].value_counts().to_dict()}")
    print("ℹ️ Structural validation only. This does not validate labels, models, or clinical safety.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
