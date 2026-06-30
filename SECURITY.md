# Security

VerityFoundry is a prompt workflow and local validation repository. It should
not contain secrets, API keys, credentials, private prompts, or private product
data.

## Supported Versions

Security review applies to the current `main` branch until tagged releases are
published.

## Reporting a Vulnerability

Open a private security advisory on GitHub when available, or contact the
maintainer through the support channels listed in `SUPPORT.md`.

Do not publish exploit details in a public issue before maintainers have had a
reasonable chance to respond.

## Prompt Safety

Prompt workflows must not ask AI agents to invent:

- legal compliance claims
- platform certification status
- image licensing rights
- privacy guarantees
- child-safety posture
- production launch dates
- archival completion evidence

Unknown sensitive decisions must remain unresolved until a human provides and
approves them.
