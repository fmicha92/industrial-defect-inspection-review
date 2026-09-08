# Security policy

## Supported versions

Only the latest tagged release is supported.

## Reporting

Do not open a public issue for exposed credentials, private source material, malicious Agent Skill instructions, or code-execution vulnerabilities. Contact the repository maintainers privately after the GitHub repository is created; add the preferred security contact here and in the repository security settings.

## Data-safety expectations

- Never commit API tokens, cookies, credentials, paper PDFs, restricted datasets, or private annotations.
- Review Agent Skills before installation because skills can instruct an agent to execute code or access external systems.
- Acquisition utilities make network requests only when explicitly invoked; the supported export and validation workflow is offline and dependency-free.
- Treat URLs and extracted publication text as untrusted input when extending parsers.

