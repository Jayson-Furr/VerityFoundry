---
{
  "id": "unity-shared-library",
  "name": "Unity Shared Library Prompt Matrix",
  "version": "0.1.0",
  "domain": "unity-shared-library",
  "rows": [
    {
      "domain": "Unity shared library",
      "input": "description + README",
      "interviewMode": "interview-medium-stakes",
      "target": "implementation-ready",
      "output": "library workspace outline, package records, capability records",
      "promptId": "unity-library.description.interview-medium.implementation-ready.v1"
    },
    {
      "domain": "Unity shared library",
      "input": "consumer games + package dependencies",
      "interviewMode": "interview-medium-stakes",
      "target": "implementation-ready",
      "output": "dependency contract notes and compatibility questions",
      "promptId": "unity-library.dependencies.interview-medium.implementation-ready.v1"
    },
    {
      "domain": "Unity shared library",
      "input": "full package + release process",
      "interviewMode": "interview-high-stakes",
      "target": "operations-ready",
      "output": "operations gaps and consumer-impact questions",
      "promptId": "unity-library.full-package.interview-high.operations-ready.v1"
    },
    {
      "domain": "Unity shared library",
      "input": "archive notes + consumer impact",
      "interviewMode": "interview-all",
      "target": "archival-ready",
      "output": "archive gaps and consumer handoff questions",
      "promptId": "unity-library.full-package.interview-all.archival-ready.v1"
    }
  ]
}
---

| Domain | Input | Interview mode | Target | Output |
|---|---|---|---|---|
| Unity shared library | description + README | interview-medium-stakes | implementation-ready | library workspace outline, package records, capability records |
| Unity shared library | consumer games + package dependencies | interview-medium-stakes | implementation-ready | dependency contract notes and compatibility questions |
| Unity shared library | full package + release process | interview-high-stakes | operations-ready | operations gaps and consumer-impact questions |
| Unity shared library | archive notes + consumer impact | interview-all | archival-ready | archive gaps and consumer handoff questions |
