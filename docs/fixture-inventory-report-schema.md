# Fixture Inventory Report Schema

`verityfoundry report fixture-inventory --format json` emits deterministic
candidate workspace fixture inventory data for release reviewers and
downstream tooling.

The top-level JSON fields are:

| Field | Meaning |
|---|---|
| `status` | Report status for the inventory command |
| `fixtureCount` | Number of candidate workspace fixture files |
| `recordCount` | Total records across fixture files |
| `kindCount` | Unique record kinds across fixture files |
| `fixtures` | Per-fixture path, example ID, record count, kind count, and presence data |
| `kinds` | Record-kind counts and recommended VeritySpec pack mappings |
| `packs` | Recommended pack counts inferred from fixture record kinds |

The report is an inventory, not a generated-workspace validation result. Use
VeritySpec to validate converted workspaces:

```bash
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
```

For v0.x releases, downstream tools should treat additional JSON fields as
non-breaking and avoid parsing human text output.
