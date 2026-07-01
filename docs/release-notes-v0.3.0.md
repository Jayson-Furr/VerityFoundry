# VerityFoundry v0.3.0 Release Notes

VerityFoundry v0.3.0 adds the second deterministic golden output fixture,
covering Unity shared-library implementation-ready prompt behavior.

## Highlights

- Added a Unity shared-library implementation-ready golden output fixture for
  Shared Unity Runtime.
- Captured public/exported versus internal/private uncertainty for shared
  library contracts.
- Preserved assumptions, unresolved decisions, human approval requirements,
  readiness gaps, and the VeritySpec validation loop in the golden output.
- Added tests proving the shared-library golden fixture exists and validates.
- Updated README, roadmap, changelog, and golden output guidance for the new
  fixture.

## Compatibility

- Package version: `0.3.0`.
- Python support: `>=3.9`.
- VerityFoundry does not call external AI APIs.
- VerityFoundry creates candidate authoring outputs; VeritySpec remains the
  validation authority.
- PyPI publishing is not enabled yet.

## Installation

```bash
pip install "verityfoundry @ git+https://github.com/Jason-Furr/verity-foundry.git@v0.3.0"
```

## Verification

The release was prepared with local tests, CLI smoke checks, package build
checks, `twine check`, wheel smoke tests, and GitHub Actions.
