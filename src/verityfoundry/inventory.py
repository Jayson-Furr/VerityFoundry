"""Release-review inventory reports for examples and golden outputs."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

from .manifests import load_example_manifests, load_golden_manifests


def generate_example_inventory_report(root: str | Path) -> dict[str, Any]:
    """Summarize example manifests for release reviewers."""

    root_path = Path(root)
    examples = []
    for path, manifest in load_example_manifests(root_path):
        examples.append(
            {
                "id": manifest.get("id"),
                "name": manifest.get("name"),
                "domain": manifest.get("domain"),
                "interviewMode": manifest.get("interviewMode"),
                "targetReadiness": manifest.get("targetReadiness"),
                "inputCount": len(manifest.get("inputs", [])),
                "expectedOutputCount": len(manifest.get("expectedOutputs", [])),
                "workspaceFixtureCount": len(manifest.get("workspaceFixtures", [])),
                "expectedRecordCategoryCount": len(manifest.get("expectedRecordCategories", [])),
                "provenanceExampleCount": len(manifest.get("provenanceExamples", [])),
                "promptRefCount": len(manifest.get("promptRefs", [])),
                "path": str(path.relative_to(root_path)),
            }
        )

    examples.sort(key=lambda item: str(item["id"]))
    domains = _domain_summary(examples)
    return {
        "exampleCount": len(examples),
        "domainCount": len(domains),
        "domains": domains,
        "examples": examples,
    }


def format_example_inventory_report(report: dict[str, Any]) -> str:
    """Format an example inventory report for humans."""

    lines = [
        "Example Inventory Report",
        "",
        f"Examples: {report['exampleCount']}",
        f"Domains: {report['domainCount']}",
        "",
        "Domains:",
    ]
    for domain in report["domains"]:
        lines.append(f"- {domain['domain']}: {domain['count']} examples")

    lines.extend(["", "Examples:"])
    for example in report["examples"]:
        lines.append(
            f"- {example['id']} ({example['domain']} / {example['targetReadiness']}): "
            f"{example['inputCount']} inputs, {example['expectedOutputCount']} expected outputs, "
            f"{example['workspaceFixtureCount']} workspace fixtures, "
            f"{example['provenanceExampleCount']} provenance examples"
        )

    return "\n".join(lines) + "\n"


def generate_golden_inventory_report(root: str | Path) -> dict[str, Any]:
    """Summarize golden output manifests for release reviewers."""

    root_path = Path(root)
    goldens = []
    for path, manifest in load_golden_manifests(root_path):
        output_path = path.parent / str(manifest.get("outputPath", ""))
        goldens.append(
            {
                "id": manifest.get("id"),
                "name": manifest.get("name"),
                "domain": manifest.get("domain"),
                "promptRef": manifest.get("promptRef"),
                "exampleRef": manifest.get("exampleRef"),
                "interviewMode": manifest.get("interviewMode"),
                "targetReadiness": manifest.get("targetReadiness"),
                "requiredSectionCount": len(manifest.get("requiredSections", [])),
                "outputPath": str(output_path.relative_to(root_path)),
                "outputExists": output_path.exists(),
                "path": str(path.relative_to(root_path)),
            }
        )

    goldens.sort(key=lambda item: str(item["id"]))
    domains = _domain_summary(goldens)
    return {
        "goldenCount": len(goldens),
        "domainCount": len(domains),
        "domains": domains,
        "goldens": goldens,
    }


def format_golden_inventory_report(report: dict[str, Any]) -> str:
    """Format a golden output inventory report for humans."""

    lines = [
        "Golden Output Inventory Report",
        "",
        f"Golden outputs: {report['goldenCount']}",
        f"Domains: {report['domainCount']}",
        "",
        "Domains:",
    ]
    for domain in report["domains"]:
        lines.append(f"- {domain['domain']}: {domain['count']} golden outputs")

    lines.extend(["", "Golden outputs:"])
    for golden in report["goldens"]:
        output_status = "present" if golden["outputExists"] else "missing"
        lines.append(
            f"- {golden['id']} ({golden['domain']} / {golden['targetReadiness']}): "
            f"{golden['requiredSectionCount']} required sections, output {output_status}, "
            f"prompt {golden['promptRef']}"
        )

    return "\n".join(lines) + "\n"


def _domain_summary(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    counts = Counter(str(item.get("domain", "unknown")) for item in items)
    return [
        {
            "domain": domain,
            "count": count,
        }
        for domain, count in sorted(counts.items())
    ]
