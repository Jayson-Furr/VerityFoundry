# Architecture

VerityFoundry is a prompt workflow library with a small deterministic utility
package.

Core pieces:

- `prompts/`: Markdown prompt workflows with JSON front matter manifests.
- `matrices/`: Markdown prompt matrices with JSON front matter manifests.
- `examples/`: input and expected-output examples with JSON manifests.
- `goldens/`: deterministic output fixtures with JSON manifests.
- `schemas/`: JSON schemas for machine-checkable manifests.
- `src/verityfoundry/`: local CLI and validation utilities.
- `evaluations/`: human review rubrics for prompt quality and uncertainty.

The CLI validates local artifacts, renders prompts and matrices, runs
decision-policy linting, reports deterministic prompt quality and matrix
coverage signals, and runs optional local integration smoke checks. It does
not call AI APIs.

VeritySpec remains the final authority for generated workspace validation. The
optional `verityfoundry check verityspec` command only verifies the local
handoff path when the `verity` CLI is available, and skips cleanly when it is
not installed.
