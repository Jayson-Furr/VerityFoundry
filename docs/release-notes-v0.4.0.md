# VerityFoundry v0.4.0 Release Notes

VerityFoundry v0.4.0 adds deterministic prompt quality reporting for the prompt
workflow library.

## Highlights

- Added `verityfoundry report prompt-quality`.
- Added text and JSON report output.
- Scored rendered prompts for uncertainty preservation evidence.
- Scored rendered prompts for provenance completeness evidence.
- Reported weakest prompts and missing rubric checks for maintainer review.
- Added tests for report scoring and CLI output.
- Updated CI, README, agent guidance, release checklist, and evaluation docs.

## Compatibility

- Package version: `0.4.0`.
- Python support: `>=3.9`.
- VerityFoundry does not call external AI APIs.
- The prompt quality report is deterministic and local.
- The prompt quality report is an inspection aid, not a readiness
  certification.
- VerityFoundry creates candidate authoring outputs; VeritySpec remains the
  validation authority.
- PyPI publishing is not enabled yet.

## Installation

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.4.0"
```

## Verification

The release was prepared with local tests, CLI smoke checks, package build
checks, `twine check`, wheel smoke tests, and GitHub Actions.
