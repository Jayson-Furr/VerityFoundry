# Fixture to VeritySpec Checklist

Use this checklist when turning a VerityFoundry candidate workspace fixture
into a real VeritySpec workspace draft.

VerityFoundry fixtures are authoring artifacts. They preserve assumptions,
provenance, unresolved decisions, and human approval requirements. They are
not final VeritySpec workspaces until VeritySpec validates them.

## Prepare the Workspace

1. Create a real VeritySpec workspace directory.
2. Choose a supported VeritySpec workspace format version.
3. Add a `verityspec.json` manifest or the current VeritySpec manifest shape.
4. Install or declare the packs that own the candidate record kinds.
5. Split fixture records into the workspace record layout expected by
   VeritySpec.
6. Keep the original VerityFoundry fixture and provenance file available as
   source evidence.

## Convert Records

For every fixture record:

- preserve `id`, `kind`, `name`, `status`, and summary fields where they map
  cleanly
- preserve `provenance.sourceRefs`
- preserve `provenance.decisionSource`
- preserve `provenance.confidence`
- preserve `provenance.humanApprovalRequired`
- keep unresolved records unresolved unless a human has supplied the missing
  decision
- map `foundry.readiness-gap` records into VeritySpec readiness-gap, evidence,
  issue, or local extension records as appropriate
- document any field that cannot be mapped cleanly

Do not convert AI-inferred or AI-suggested values into approved product truth
without human approval.

## Check Pack Ownership

Candidate fixture kinds may point at future or extension packs. Review them
against the fixture inventory report:

```bash
verityfoundry report fixture-inventory
```

If a kind maps to a future pack, decide whether to:

- wait for VeritySpec to support that pack
- author a local extension pack
- translate the record into an existing supported kind
- keep the item as a gap or follow-up decision

## Validate With VeritySpec

After conversion, run VeritySpec from the generated workspace:

```bash
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```

If VeritySpec rejects the workspace, VeritySpec is authoritative. Update the
workspace, fixture, prompt workflow, or example expectations to preserve that
feedback instead of weakening validation.

## Review Before Handoff

Before handing the workspace to a human engineer or AI coding agent, confirm:

- every unresolved decision is visible
- every high-impact decision requiring approval remains marked
- every source reference points to a real input, expected output, or evidence
  file
- every AI-inferred, AI-defaulted, or AI-suggested value is labeled
- every generated record belongs to a known VeritySpec pack or an intentional
  extension
- readiness gaps explain what prevents the workspace from reaching the target
  profile

This keeps the handoff honest: VerityFoundry can draft and explain candidate
workspace structure, while VeritySpec validates the executable product
contract.
