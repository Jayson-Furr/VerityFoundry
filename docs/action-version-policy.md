# Action Version Policy

VerityFoundry uses GitHub Actions for CI and release checks. Workflow action
versions should remain explicit, reviewable, and easy to update.

## Current Policy

Known actions have repository minimum major versions in
`src/verityfoundry/workflow_hygiene.py`.

The checker currently verifies:

- `actions/checkout`
- `actions/setup-python`
- `actions/upload-artifact`
- `actions/download-artifact`
- `softprops/action-gh-release`

Known actions should use `vN` major-version references unless there is a
documented reason to pin more tightly.

## Changing Minimums

Raise a minimum major version only when:

- the workflow has been tested locally or in CI
- upstream release notes justify the update
- release workflow behavior still matches the release checklist
- the changelog or release notes mention the workflow-impacting change when
  relevant

Do not lower a minimum to make a failing check pass without recording why the
older action is required.

## Future Configuration

A future sprint may move action-version minimums into a config file. Until
then, changes to action minimums should be reviewed as code changes and
covered by workflow hygiene tests.
