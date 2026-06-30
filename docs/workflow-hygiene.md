# Workflow Hygiene

`verityfoundry check workflow-hygiene` checks GitHub Actions workflow action
versions against repository minimums.

Run:

```bash
verityfoundry check workflow-hygiene
verityfoundry check workflow-hygiene --format json
```

This command runs from a source checkout because it inspects:

```text
.github/workflows/
```

The check currently guards against stale major versions for common actions
such as `actions/checkout` and `actions/setup-python`. It is intended to catch
runner annotation risks before they become recurring CI noise.
