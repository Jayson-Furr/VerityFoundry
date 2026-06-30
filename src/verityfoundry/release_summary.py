"""Aggregate release-review report."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from . import __version__
from .inventory import (
    generate_example_inventory_report,
    generate_fixture_inventory_report,
    generate_golden_inventory_report,
    generate_provenance_coverage_report,
)
from .matrix_coverage import generate_matrix_coverage_report
from .policy_lint import (
    SEVERITY_ERROR,
    SEVERITY_WARNING,
    count_policy_lint_severities,
    lint_decision_policy,
)
from .quality import generate_prompt_quality_report
from .quality_trend import generate_prompt_quality_trend_report
from .release_integrity import check_release_integrity
from .thresholds import check_quality_thresholds
from .workflow_hygiene import check_workflow_hygiene


def generate_release_summary_report(root: str | Path) -> dict[str, Any]:
    """Generate a deterministic aggregate release-review report."""

    root_path = Path(root)
    prompt_quality = generate_prompt_quality_report(root_path)
    prompt_quality_trend = generate_prompt_quality_trend_report(root_path)
    matrix_coverage = generate_matrix_coverage_report(root_path)
    golden_inventory = generate_golden_inventory_report(root_path)
    example_inventory = generate_example_inventory_report(root_path)
    fixture_inventory = generate_fixture_inventory_report(root_path)
    provenance_coverage = generate_provenance_coverage_report(root_path)
    release_integrity = _safe_release_integrity(root_path)
    quality_thresholds = check_quality_thresholds(root_path)
    workflow_hygiene = _safe_workflow_hygiene(root_path)
    policy_issues = lint_decision_policy(root_path)
    policy_counts = count_policy_lint_severities(policy_issues)

    blocking_issue_count = (
        int(release_integrity["issueCount"])
        + int(quality_thresholds["issueCount"])
        + int(workflow_hygiene["issueCount"])
        + int(policy_counts[SEVERITY_ERROR])
    )
    warning_count = int(policy_counts[SEVERITY_WARNING])

    return {
        "status": "failed" if blocking_issue_count else "passed",
        "blockingIssueCount": blocking_issue_count,
        "warningCount": warning_count,
        "checks": {
            "releaseIntegrity": {
                "status": release_integrity["status"],
                "issueCount": release_integrity["issueCount"],
                "expectedVersion": release_integrity["expectedVersion"],
                "expectedTag": release_integrity["expectedTag"],
            },
            "qualityThresholds": {
                "status": quality_thresholds["status"],
                "issueCount": quality_thresholds["issueCount"],
            },
            "workflowHygiene": {
                "status": workflow_hygiene["status"],
                "issueCount": workflow_hygiene["issueCount"],
                "workflowCount": workflow_hygiene["workflowCount"],
                "actionCount": workflow_hygiene["actionCount"],
            },
            "decisionPolicyLint": {
                "status": "failed" if policy_counts[SEVERITY_ERROR] else "passed",
                "errorCount": policy_counts[SEVERITY_ERROR],
                "warningCount": policy_counts[SEVERITY_WARNING],
            },
        },
        "reports": {
            "promptQuality": {
                "promptCount": prompt_quality["promptCount"],
                "percent": prompt_quality["percent"],
                "uncertaintyPercent": prompt_quality["uncertaintyPreservation"]["percent"],
                "provenancePercent": prompt_quality["provenanceCompleteness"]["percent"],
            },
            "promptQualityTrend": {
                "snapshotCount": prompt_quality_trend["snapshotCount"],
                "currentPercent": prompt_quality_trend["current"]["percent"],
                "latestSnapshotLabel": prompt_quality_trend["latestSnapshot"]["label"],
                "deltaPercent": prompt_quality_trend["deltaFromLatest"]["percent"],
            },
            "matrixCoverage": {
                "matrixCount": matrix_coverage["matrixCount"],
                "rowCount": matrix_coverage["matrixRowCount"],
                "coveragePercent": matrix_coverage["coveragePercent"],
                "missingDomainPromptCount": matrix_coverage["missingDomainPromptCount"],
                "unknownPromptRefCount": len(matrix_coverage["unknownPromptRefs"]),
            },
            "goldenInventory": {
                "goldenCount": golden_inventory["goldenCount"],
                "domainCount": golden_inventory["domainCount"],
            },
            "exampleInventory": {
                "exampleCount": example_inventory["exampleCount"],
                "domainCount": example_inventory["domainCount"],
            },
            "fixtureInventory": {
                "fixtureCount": fixture_inventory["fixtureCount"],
                "recordCount": fixture_inventory["recordCount"],
                "kindCount": fixture_inventory["kindCount"],
            },
            "provenanceCoverage": {
                "exampleCount": provenance_coverage["exampleCount"],
                "recordProvenancePercent": provenance_coverage["recordProvenancePercent"],
                "decisionExamplePercent": provenance_coverage["decisionExamplePercent"],
            },
        },
        "notes": [
            "Release summary is deterministic and does not call external AI APIs.",
            "Run VeritySpec validation separately for generated workspaces that are in scope.",
        ],
    }


def format_release_summary_report(report: dict[str, Any]) -> str:
    """Format an aggregate release-review report for humans."""

    lines = [
        "Release Summary Report",
        "",
        f"Status: {report['status']}",
        f"Blocking issues: {report['blockingIssueCount']}",
        f"Warnings: {report['warningCount']}",
        "",
        "Checks:",
    ]

    checks = report["checks"]
    lines.append(
        "- Release integrity: "
        f"{checks['releaseIntegrity']['status']} "
        f"({checks['releaseIntegrity']['issueCount']} issues, "
        f"{checks['releaseIntegrity']['expectedTag']})"
    )
    lines.append(
        "- Quality thresholds: "
        f"{checks['qualityThresholds']['status']} "
        f"({checks['qualityThresholds']['issueCount']} issues)"
    )
    lines.append(
        "- Workflow hygiene: "
        f"{checks['workflowHygiene']['status']} "
        f"({checks['workflowHygiene']['workflowCount']} workflows, "
        f"{checks['workflowHygiene']['actionCount']} actions, "
        f"{checks['workflowHygiene']['issueCount']} issues)"
    )
    lines.append(
        "- Decision policy lint: "
        f"{checks['decisionPolicyLint']['status']} "
        f"({checks['decisionPolicyLint']['errorCount']} errors, "
        f"{checks['decisionPolicyLint']['warningCount']} warnings)"
    )

    reports = report["reports"]
    lines.extend(
        [
            "",
            "Reports:",
            (
                "- Prompt quality: "
                f"{reports['promptQuality']['percent']}% overall, "
                f"{reports['promptQuality']['promptCount']} prompts"
            ),
            (
                "- Prompt quality trend: "
                f"{reports['promptQualityTrend']['deltaPercent']:+.1f} points from "
                f"{reports['promptQualityTrend']['latestSnapshotLabel']}"
            ),
            (
                "- Matrix coverage: "
                f"{reports['matrixCoverage']['coveragePercent']}% coverage, "
                f"{reports['matrixCoverage']['missingDomainPromptCount']} missing prompts"
            ),
            (
                "- Golden outputs: "
                f"{reports['goldenInventory']['goldenCount']} across "
                f"{reports['goldenInventory']['domainCount']} domains"
            ),
            (
                "- Examples: "
                f"{reports['exampleInventory']['exampleCount']} across "
                f"{reports['exampleInventory']['domainCount']} domains"
            ),
            (
                "- Workspace fixtures: "
                f"{reports['fixtureInventory']['fixtureCount']} fixtures, "
                f"{reports['fixtureInventory']['recordCount']} records, "
                f"{reports['fixtureInventory']['kindCount']} kinds"
            ),
            (
                "- Provenance coverage: "
                f"{reports['provenanceCoverage']['recordProvenancePercent']}% records, "
                f"{reports['provenanceCoverage']['decisionExamplePercent']}% decision examples"
            ),
            "",
            "Notes:",
        ]
    )

    for note in report["notes"]:
        lines.append(f"- {note}")

    return "\n".join(lines) + "\n"


def _safe_release_integrity(root_path: Path) -> dict[str, Any]:
    """Run release integrity when source files are present, otherwise skip."""

    try:
        return check_release_integrity(root_path)
    except (FileNotFoundError, ValueError) as exc:
        return {
            "status": "skipped",
            "expectedVersion": __version__,
            "expectedTag": f"v{__version__}",
            "issueCount": 0,
            "issues": [],
            "reason": str(exc),
        }


def _safe_workflow_hygiene(root_path: Path) -> dict[str, Any]:
    """Run workflow hygiene when source workflow files are present."""

    workflow_dir = root_path / ".github" / "workflows"
    if not workflow_dir.exists():
        return {
            "status": "skipped",
            "workflowCount": 0,
            "actionCount": 0,
            "issueCount": 0,
            "actions": [],
            "issues": [],
            "reason": f"{workflow_dir} does not exist",
        }
    return check_workflow_hygiene(root_path)
