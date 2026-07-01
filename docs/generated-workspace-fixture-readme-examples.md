# Generated Workspace Fixture README Examples

Generated workspace fixtures can be inspected directly from the repository.

```bash
python -m unittest tests.test_generated_workspace_fixtures -v
verityfoundry validate
verityfoundry report release-summary
```

When the sibling VeritySpec source checkout is available, a local smoke check
can run without installing `verity` globally:

```bash
PYTHONPATH=/Users/jaysonfurr/Code/Jayson-Furr/VeritySpec/src \
  python3 -m verityspec.cli validate fixtures/generated-workspaces/customer-portal

PYTHONPATH=/Users/jaysonfurr/Code/Jayson-Furr/VeritySpec/src \
  python3 -m verityspec.cli validate fixtures/generated-workspaces/dream-extraction
```

These commands prove that the checked fixture shape is locally valid against
the available VeritySpec source. They do not replace human review, production
approval, or future VeritySpec readiness gates.
