---
{
  "id": "decision-policy.medium-stakes.v1",
  "name": "Medium-Stakes Decision Policy",
  "version": "0.1.0",
  "kind": "common",
  "domain": "common",
  "interviewMode": "not-applicable",
  "targetReadiness": "not-applicable",
  "inputTypes": [],
  "outputs": [
    "decision-policy"
  ],
  "requiresHumanApproval": true,
  "notes": "Reusable decision policy for implementation-oriented prompt workflows."
}
---

AI may infer likely genre, candidate core loop, art style descriptors,
candidate feature taxonomy, likely prototype scope, and likely workspace record
categories.

AI may default status to `draft`, owner to `unknown`, platform to `pc
prototype` only for low-stakes drafts, and monetization to `undecided` when it
is not provided.

AI may suggest telemetry questions, readiness gates, implementation milestones,
and VeritySpec record categories.

AI must ask or leave unresolved production target platforms, monetization,
multiplayer/networking, data collection, liveops expectations, external
service dependencies, launch dates, decommissioning, and archival policy.

AI must not invent legal compliance claims, platform certification status,
image licensing rights, privacy guarantees, child-safety posture, commercial
clearance, production launch dates, or archival completion evidence.
