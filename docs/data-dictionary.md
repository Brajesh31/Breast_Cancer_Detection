# 📊 Dataset Dictionary

## Dataset shape

The checked-in CSV currently has 569 rows and 32 columns:
- `id`: sample identifier.
- `diagnosis`: class label, `M` or `B`.
- 30 numeric measurements organized into ten feature families.

Class counts currently documented for this file are 212 malignant and 357 benign. Run the dataset validation script to verify the file has not changed.

## Diagnosis label

| Value | Meaning | Current count |
|---|---|---:|
| `M` | Malignant | 212 |
| `B` | Benign | 357 |

The label is an outcome field, not a predictor. For a diagnosis classification task, it belongs in `y` and must be excluded from `X`.

## Measurement families

Each family contains a mean value, a standard error value (`_se`), and a worst value.

| Family | Typical column names | Description |
|---|---|---|
| Radius | `radius_mean`, `radius_se`, `radius_worst` | Mean distance from center to perimeter |
| Texture | `texture_mean`, `texture_se`, `texture_worst` | Gray-scale variation |
| Perimeter | `perimeter_mean`, `perimeter_se`, `perimeter_worst` | Perimeter measurement |
| Area | `area_mean`, `area_se`, `area_worst` | Area measurement |
| Smoothness | `smoothness_mean`, `smoothness_se`, `smoothness_worst` | Local variation in radius lengths |
| Compactness | `compactness_mean`, `compactness_se`, `compactness_worst` | Perimeter-related compactness measure |
| Concavity | `concavity_mean`, `concavity_se`, `concavity_worst` | Severity of concave portions |
| Concave points | `concave points_mean`, `concave points_se`, `concave points_worst` | Number/measure of concave points |
| Symmetry | `symmetry_mean`, `symmetry_se`, `symmetry_worst` | Symmetry measurement |
| Fractal dimension | `fractal_dimension_mean`, `fractal_dimension_se`, `fractal_dimension_worst` | Fractal-dimension measurement |

## Identifier handling

The `id` field identifies a record. It is not a biological measurement and should not be included as a predictive feature in an educational diagnosis experiment.

## Data limitations

The exact acquisition history of the local CSV copy is not recorded. Schema similarity does not prove provenance. See [Dataset provenance](dataset-provenance.md) and [LICENSE-DATA.md](../LICENSE-DATA.md).
