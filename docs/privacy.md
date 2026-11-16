# 🔏 Privacy and Data Handling

## Current data handling

The current project uses a static CSV in the repository and a local Jupyter notebook. It does not provide patient registration, user uploads, an online database, an API, or a hosted prediction service.

## Prohibited repository content

Do not commit:
- Patient names, contact details, dates of birth, record numbers, or identifiable medical histories.
- Medical images or records obtained without explicit rights and authorization.
- Credentials, API keys, access tokens, private keys, or session cookies.
- Confidential institutional or research data.
- Data whose license or redistribution terms are unknown.

## Notebook privacy

Notebook outputs can retain data values, file paths, environment details, and accidental secrets. Review outputs and metadata before committing. Treat notebook cells as executable code and use an isolated environment.

## New data sources

Before adding any dataset, document the source, license, collection context, permitted use, privacy risks, and retention requirements. Do not assume that public availability means unrestricted redistribution.

## Incident response

If sensitive information is committed, restrict further exposure, notify the maintainer privately, and rotate any exposed credentials. Removing a value from the latest file does not remove it from Git history or invalidate a leaked credential. Follow the security reporting process.
