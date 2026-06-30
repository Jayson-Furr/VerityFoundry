# Image Input Guidance

VerityFoundry can guide AI agents that inspect concept art or identity images.
Image analysis must be treated as interpretation, not objective truth.

Agents may produce:

- asset record candidates
- visual tags
- subject classifications
- style notes
- possible gameplay implications
- art direction questions
- brand tone questions

Agents must not silently claim:

- image licensing rights
- ownership
- commercial clearance
- platform approval
- accessibility compliance
- brand approval

Those remain unknown unless provided by a human or documented source.

Examples may include an `inputs/image-manifest.json` file. That file should
describe image roles, paths or placeholders, source notes, and interpretation
limits. It should not claim that a missing or described image has been
inspected as a binary asset.

`verityfoundry validate examples` validates image manifests against
`schemas/image-input-manifest.schema.json` when an example input references
`image-manifest.json`.

For example:

```json
{
  "id": "image-inputs.dream_extraction",
  "images": [
    {
      "id": "image.identity.key_art",
      "path": "art/identity/key-art.png",
      "role": "identity",
      "provided": false,
      "notesSource": "inputs/images.md",
      "interpretationLimits": [
        "Style tags are candidate interpretations from written image notes.",
        "Licensing, ownership, commercial clearance, accessibility, and platform approval are unknown."
      ]
    }
  ]
}
```

Every image entry must declare:

- `id`
- `path`
- `role`
- `provided`
- `notesSource`
- `interpretationLimits`

When image notes feed candidate workspace fixtures, preserve low confidence
and require human approval for visual identity, art direction, gameplay
implications, licensing, and approval-sensitive decisions.
