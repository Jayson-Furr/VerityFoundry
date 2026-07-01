# VerityFoundry v0.2.0 Release Notes

VerityFoundry v0.2.0 adds the first deterministic golden output fixture for
Unity game implementation-ready prompt behavior.

## Highlights

- Added a golden output manifest schema.
- Added `verityfoundry validate goldens`.
- Added the first Unity game implementation-ready golden output fixture for
  Dream Extraction.
- Added tests for golden output validation and CLI coverage.
- Updated CI to validate golden fixtures.
- Updated README, roadmap, agent guidance, and golden output guidance for the
  new fixture contract.

## Compatibility

- Package version: `0.2.0`.
- Python support: `>=3.9`.
- VerityFoundry does not call external AI APIs.
- VerityFoundry creates candidate authoring outputs; VeritySpec remains the
  validation authority.
- PyPI publishing is not enabled yet.

## Installation

```bash
pip install "verityfoundry @ git+https://github.com/Jason-Furr/verity-foundry.git@v0.2.0"
```

## Verification

The release was prepared with local tests, CLI smoke checks, package build
checks, `twine check`, wheel smoke tests, and GitHub Actions.
