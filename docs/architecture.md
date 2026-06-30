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

The CLI validates and renders local artifacts. It does not call AI APIs.

VeritySpec remains the final authority for generated workspace validation.
