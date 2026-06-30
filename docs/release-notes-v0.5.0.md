# VerityFoundry v0.5.0 Release Notes

VerityFoundry v0.5.0 adds an optional local VeritySpec smoke check for the
handoff from prompt workflows to generated VeritySpec workspaces.

## Highlights

- Added `verityfoundry check verityspec`.
- The check skips cleanly when the `verity` CLI is not installed.
- When `verity` is available and a workspace is provided or detected, the
  check runs `verity validate`.
- Added tests for skipped, passed, and failed smoke-check behavior.
- Added CI and release workflow smoke coverage for the new command.
- Updated README, AGENTS, CI docs, release checklist, architecture docs, and
  VeritySpec handoff guidance.

## Verification

- Package version: `0.5.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry report prompt-quality`,
  and `verityfoundry check verityspec`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.5.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
