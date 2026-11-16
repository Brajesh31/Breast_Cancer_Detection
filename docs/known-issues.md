# 🐛 Known Issues and Technical Limitations

This register records known defects and missing capabilities. It should be updated when a verified fix is merged.

| ID | Priority | Issue | Impact | Suggested resolution |
|---|---|---|---|---|
| KI-01 | Critical | Split target is `fractal_dimension_worst`, not `diagnosis` | Not a diagnosis classifier | Define explicit X/y |
| KI-02 | Critical | Diagnosis remains in predictors | Target leakage for intended task | Drop diagnosis from X |
| KI-03 | Critical | Toy logistic example copies labels into predictions | Misleading 1.0 score | Remove claim and replace with a real, validated educational pipeline |
| KI-04 | High | Linear regression example is not diagnosis classification | Wrong task framing | Remove or clearly label as unrelated demonstration |
| KI-05 | Medium | Variable `data` is reused for different object types | Notebook state confusion | Use descriptive variable names |
| KI-06 | Medium | Global warning suppression | Useful warnings may be hidden | Address warnings individually |
| KI-07 | Medium | `mean_squared_error(..., squared=False)` removed in scikit-learn 1.6+ | Compatibility failure | Use `root_mean_squared_error` where appropriate |
| KI-08 | Medium | No locked dependency environment | Reproduction drift | Record tested versions and add a reviewed lock strategy |
| KI-09 | High | Exact CSV acquisition history is missing | Provenance uncertainty | Verify source, checksum and license |
| KI-10 | High | No independent or clinical validation | No clinical-use evidence | Keep clinical use explicitly prohibited |

## Issue lifecycle

When an issue is fixed, link the pull request, describe the changed behavior, add tests where appropriate, and record any remaining limitation. Do not silently delete unresolved limitations from the documentation.
