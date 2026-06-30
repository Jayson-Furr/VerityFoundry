# Contributing

VerityFoundry welcomes prompt workflow, decision policy, example, and tooling
contributions that strengthen VeritySpec workspace authoring without hiding
uncertainty.

## Contribution Standards

- Preserve uncertainty and provenance.
- Do not add prompts that convert unknowns into unsupported facts.
- Include decision-policy, safety, and provenance controls for high-stakes
  prompts.
- Include or update tests for manifest, matrix, example, or CLI behavior.
- Update README, docs, changelog, and roadmap entries when behavior changes.
- Keep examples deterministic and suitable for CI.
- Do not call external AI APIs in tests or CI.

## Prompt Workflow Proposals

Prompt workflows should include:

- Stable prompt ID.
- JSON front matter manifest.
- Clear input assumptions.
- Output contract.
- Decision policy reference.
- Safety and provenance includes when the prompt handles high-stakes readiness,
  operations, maintenance, decommissioning, archival, legal, privacy,
  certification, or commercial commitments.
- Human approval requirements.
- Unresolved-question behavior.

## Local Checks

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip setuptools
pip install -e .
python -m unittest discover -s tests -v
verityfoundry validate
verityfoundry lint decision-policy
git diff --check
```
