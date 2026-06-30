# Release Integrity Report Schema

`verityfoundry check release-integrity --format json` emits a deterministic
JSON object for release bookkeeping review. This document records the current
shape for downstream tools and release reviewers.

## Current Shape

```json
{
  "status": "passed",
  "expectedVersion": "0.15.0",
  "expectedTag": "v0.15.0",
  "issueCount": 0,
  "issues": []
}
```

When issues exist, each issue has this shape:

```json
{
  "code": "release.readme-badge",
  "path": "README.md",
  "message": "README release badge must reference the expected tag"
}
```

## Fields

| Field | Type | Meaning |
|---|---|---|
| `status` | string | `passed` or `failed` |
| `expectedVersion` | string | Package version under review |
| `expectedTag` | string | Git tag derived from the expected version |
| `issueCount` | number | Number of release-integrity issues |
| `issues` | array | Deterministic issue objects |

Issue fields:

| Field | Type | Meaning |
|---|---|---|
| `code` | string | Stable-ish issue category for local automation |
| `path` | string | File path inspected by the check |
| `message` | string | Human-readable explanation |

## Stability Notes

During v0.x, downstream tools may rely on the top-level fields and issue
fields listed here. New fields may be added in a minor release. Existing field
renames, removals, or type changes should be treated as compatibility changes
and called out in the changelog.

The report checks local files. It does not call GitHub, PyPI, external AI APIs,
or VeritySpec.

## Related Command

```bash
verityfoundry check release-integrity --format json
```
