# 🔄 Data Flow

## Current implementation

```mermaid
flowchart LR
 A[breast-cancer.csv] --> B[pandas read_csv]
 B --> C[DataFrame]
 C --> D[Inspection]
 C --> E[Descriptive statistics]
 C --> F[Exploratory plots]
 C --> G[Incomplete model examples]
 D --> H[Notebook output]
 E --> H
 F --> H
 G --> H
```

The current modeling branch is not a valid diagnosis classification pipeline. See [Modeling methodology](modeling-methodology.md).

## Recommended future analysis

```mermaid
flowchart TD
 A[Dataset + provenance] --> B[Schema validation]
 B --> C[Define diagnosis target]
 C --> D[Exclude id and target from X]
 D --> E[Stratified partition]
 E --> F[Training-only pipeline]
 F --> G[Cross-validation]
 G --> H[Freeze choices]
 H --> I[Held-out evaluation]
 I --> J[Transparent report]
```

## Data boundaries

The notebook reads a local static file. There is no network ingestion, user upload endpoint, database, or patient record system in the current repository.
