# 🧰 Maintenance Guide

## Routine maintenance

- Keep README, docs index, notebook narrative, and known-issues register aligned.
- Verify dataset source and license before changing or redistributing the CSV.
- Review Python and scikit-learn compatibility before dependency upgrades.
- Run dataset, docs, and pytest checks after relevant changes.
- Review GitHub workflow permissions and action updates.
- Remove stale outputs and accidental local metadata from notebooks.
- Keep the non-clinical-use statement visible.

## Dependency updates

Update dependencies deliberately. Review changelogs and breaking changes, run the checks, and record the tested Python/package versions. Do not claim reproducibility from an unpinned dependency list alone.

## Dataset updates

Treat data updates as high-impact changes. Record source, version, checksum, license, row counts, schema differences, transformations, and privacy review. Use the dataset change template.

## Documentation ownership

When a behavior changes, update the relevant guide, examples, diagrams, known issues, and changelog in the same pull request where practical.

## No production operations

There is no deployed service to monitor. Uptime, service-level objectives, on-call rotations, and disaster recovery for a production endpoint do not apply.
