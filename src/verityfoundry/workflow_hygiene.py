"""Workflow hygiene checks for GitHub Actions files."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any


MINIMUM_ACTION_MAJORS = {
    "actions/checkout": 7,
    "actions/setup-python": 6,
    "actions/upload-artifact": 7,
    "actions/download-artifact": 8,
    "softprops/action-gh-release": 3,
}

USE_PATTERN = re.compile(r"^\s*-?\s*uses:\s*([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)@([^\s#]+)")


@dataclass(frozen=True)
class WorkflowIssue:
    """A workflow hygiene issue."""

    code: str
    path: str
    line: int
    message: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "path": self.path,
            "line": self.line,
            "message": self.message,
        }


def check_workflow_hygiene(root: str | Path) -> dict[str, Any]:
    """Check workflow action versions against known repository standards."""

    root_path = Path(root)
    workflow_dir = root_path / ".github" / "workflows"
    issues: list[WorkflowIssue] = []
    actions: list[dict[str, Any]] = []

    for path in sorted(workflow_dir.glob("*.yml")) + sorted(workflow_dir.glob("*.yaml")):
        relative = str(path.relative_to(root_path))
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            match = USE_PATTERN.match(line)
            if not match:
                continue
            action, ref = match.groups()
            item = {
                "action": action,
                "ref": ref,
                "path": relative,
                "line": line_number,
            }
            actions.append(item)

            minimum = MINIMUM_ACTION_MAJORS.get(action)
            if minimum is None:
                continue

            major = _major_version(ref)
            if major is None:
                issues.append(
                    WorkflowIssue(
                        "workflow.action-unpinned-major",
                        relative,
                        line_number,
                        f"{action}@{ref} does not use a vN major version",
                    )
                )
            elif major < minimum:
                issues.append(
                    WorkflowIssue(
                        "workflow.action-stale-major",
                        relative,
                        line_number,
                        (
                            f"{action}@{ref} is below the repository minimum "
                            f"v{minimum}; this may reintroduce known runner annotations"
                        ),
                    )
                )

    return {
        "status": "failed" if issues else "passed",
        "workflowCount": len(list(workflow_dir.glob("*.yml")) + list(workflow_dir.glob("*.yaml"))),
        "actionCount": len(actions),
        "actions": actions,
        "issueCount": len(issues),
        "issues": [issue.to_dict() for issue in issues],
    }


def format_workflow_hygiene_report(report: dict[str, Any]) -> str:
    """Format workflow hygiene results for humans."""

    lines = [
        "Workflow Hygiene Check",
        "",
        f"Workflows: {report['workflowCount']}",
        f"Actions: {report['actionCount']}",
    ]

    if report["issueCount"]:
        lines.extend(["", "Issues:"])
        for issue in report["issues"]:
            lines.append(
                f"- {issue['code']}: {issue['path']}:{issue['line']}: {issue['message']}"
            )
    else:
        lines.extend(["", "Workflow hygiene check passed."])

    return "\n".join(lines) + "\n"


def _major_version(ref: str) -> int | None:
    match = re.match(r"^v([0-9]+)$", ref)
    if not match:
        return None
    return int(match.group(1))
