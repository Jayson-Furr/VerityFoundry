# Release-Summary Snapshot Update Checklist

Release-summary snapshots live under:

```text
snapshots/release-summary/
```

They capture selected historical release-summary output for release reviewers.
Do not add a new snapshot for every release automatically. Add one when a
release changes meaningful release-review shape, checks, report counts, or
schema expectations.

## Update Steps

1. Confirm the repository is on the intended release-prep branch.
2. Run `verityfoundry check release-integrity`.
3. Run `verityfoundry report release-summary --format json`.
4. Save the snapshot with a release label:

   ```bash
   verityfoundry report release-summary --format json > snapshots/release-summary/vX.Y.Z.json
   ```

5. Run release-summary schema tests:

   ```bash
   python -m unittest tests.test_release_summary -v
   ```

6. Confirm package-data tests include the snapshot:

   ```bash
   python -m unittest tests.test_packaged_fixture_files -v
   ```

7. Update docs, changelog, roadmap, and release notes.

## Review Criteria

Add a snapshot when it helps humans compare:

- new report sections
- changed warning or blocking issue counts
- changed quality-threshold behavior
- changed workflow hygiene behavior
- changed inventory counts
- changed provenance or portfolio coverage reports

Do not use snapshots to hide failing checks. If release-summary has blocking
issues, fix the underlying issue or document the external blocker before
release.

## Boundary

A release-summary snapshot is VerityFoundry release-review evidence. It is not
VeritySpec validation evidence, human approval, or product readiness evidence.
