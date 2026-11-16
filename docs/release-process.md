# 🚀 Release and Change Process

## Release principle

A repository release should be traceable and evidence-based. A release tag does not imply that the model is clinically validated or suitable for patient care.

## Before a release

- [ ] Review the README and safety notice.
- [ ] Verify dataset provenance and licensing notes.
- [ ] Run dataset validation.
- [ ] Run documentation validation.
- [ ] Run automated tests.
- [ ] State whether the notebook was executed from a clean kernel.
- [ ] Record Python and dependency versions used for verification.
- [ ] Review changed notebook outputs and metadata.
- [ ] Review security and privacy implications.
- [ ] Update CHANGELOG.md.
- [ ] Confirm no unsupported performance or medical claims.
- [ ] Record commit SHA and known limitations.

## Versioning

Use a clear version tag when a meaningful project snapshot is published. Explain whether a release changes documentation, data, notebook methodology, or tooling. Do not use a version number as a quality or regulatory claim.

## Rollback

For a defective documentation or code release, identify the affected commit and revert or patch it through a reviewed pull request. For a dataset rights or privacy issue, stop redistribution and coordinate a safe replacement or removal. For leaked credentials, rotate them immediately; history rewriting alone is not sufficient.
