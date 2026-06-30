# Release Integrity

`verityfoundry check release-integrity` checks public release bookkeeping from a
source checkout.

It compares:

- `pyproject.toml` package version
- `src/verityfoundry/__init__.py` `__version__`
- README release badge, latest-release text, install command, and release-note
  link
- latest released `CHANGELOG.md` heading
- `ROADMAP.md` release state
- `docs/release-checklist.md` tag command
- matching `docs/release-notes-vX.Y.Z.md` file

Run:

```bash
verityfoundry check release-integrity
verityfoundry check release-integrity --format json
```

During release prep, pass the intended package version explicitly:

```bash
verityfoundry check release-integrity --expected-version 0.11.0
```

The command is deterministic and local. It does not check GitHub tags or
releases. Use GitHub Actions and `gh release view` for public release
verification after tagging.
