---
{
  "id": "common.verityspec-context.v1",
  "name": "VeritySpec Context",
  "version": "0.1.0",
  "kind": "common",
  "domain": "common",
  "interviewMode": "not-applicable",
  "targetReadiness": "not-applicable",
  "inputTypes": [],
  "outputs": [
    "verityspec-context"
  ],
  "requiresHumanApproval": false,
  "notes": "Explains the VeritySpec and VerityFoundry boundary."
}
---

VeritySpec is the executable product-contract framework. VerityFoundry is the
AI-assisted authoring and prompt workflow layer.

Use this relationship:

```text
VeritySpec    = contract engine
VerityFoundry = candidate authoring workflow
```

Do not claim that VerityFoundry validates final product truth. It may create a
candidate workspace draft, but VeritySpec validation, linting, readiness, graph
checks, and human review remain required.
