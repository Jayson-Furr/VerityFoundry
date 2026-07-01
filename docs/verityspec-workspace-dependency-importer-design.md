# VeritySpec Workspace Dependency Importer Design

This is a design note for future VerityFoundry prompt workflows that prepare
candidate VeritySpec workspace dependency imports. It is not an implemented
importer.

## Desired Workflow

```text
rough dependency notes
  -> VerityFoundry interview or fabrication prompt
  -> candidate dependency records and assumptions
  -> generated workspace fixture
  -> VeritySpec dependency/import command
  -> validation report and human review
```

## Importer Inputs

- source workspace path or repository
- dependency alias
- expected workspace ID
- intended version constraint
- public/exported record expectations
- unresolved compatibility questions
- human approval requirements

## Importer Outputs

- dependency assumption report
- candidate manifest update
- cross-workspace reference candidates
- unresolved questions
- VeritySpec validation command
- migration or import follow-up items

## Boundary

VerityFoundry should prepare and explain dependency import intent. VeritySpec
must perform the real import, dependency resolution, compatibility checks, and
graph validation. Human approval remains required for release-impacting
dependency changes.
