# Uncertainty Preservation Checklist

Before accepting a prompt workflow, check:

- Does it distinguish human-provided facts from AI inference?
- Does it mark defaulted values as defaults?
- Does it avoid claiming final readiness?
- Does it identify unresolved questions?
- Does it require human approval for high-stakes decisions?
- Does it avoid inventing licensing, privacy, certification, legal, financial,
  safety, launch, support, or archival claims?
- Does it preserve source references?
- Does it recommend VeritySpec validation for generated workspaces?

Use `verityfoundry report prompt-quality` to inspect deterministic uncertainty
and provenance evidence across the prompt library.
