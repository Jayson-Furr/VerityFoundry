# Executable Fixture Release-Summary Coverage

`verityfoundry report release-summary` does not yet report generated
VeritySpec-shaped workspace fixtures as a separate section. Until that exists,
release reviewers should pair release-summary output with generated fixture
tests and optional VeritySpec validation.

## Current Coverage

Generated fixture coverage currently comes from:

- `tests/test_generated_workspace_fixtures.py`
- recursive package-data fixture checks
- README link coverage
- optional `verity validate` smoke checks when VeritySpec is available

## Future Release-Summary Addition

A future release-summary field could report:

- generated workspace fixture count
- record count by generated fixture
- optional VeritySpec validation status
- skipped validation reason when `verity` is unavailable
- unresolved human approval count

## Boundary

Release-summary output helps reviewers inspect VerityFoundry repository state.
It should not certify generated VeritySpec workspaces without VeritySpec
validation and human approval.
