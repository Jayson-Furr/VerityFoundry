"""Optional local integration checks for companion tools."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import os
from pathlib import Path
import shutil
import subprocess


CHECK_PASSED = "passed"
CHECK_FAILED = "failed"
CHECK_SKIPPED = "skipped"


@dataclass
class VeritySpecCheckResult:
    """Result for the optional VeritySpec smoke check."""

    status: str
    reason: str
    command: list[str]
    returnCode: int | None
    stdout: str
    stderr: str
    workspace: str | None
    verity: str | None

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def check_verityspec(
    root: Path,
    workspace: str | None = None,
    executable: str | None = None,
    timeout_seconds: int = 30,
) -> VeritySpecCheckResult:
    """Run a small VeritySpec smoke check when the `verity` CLI is available."""

    verity = _resolve_executable(executable)
    if verity is None:
        requested = executable or "verity"
        return VeritySpecCheckResult(
            status=CHECK_SKIPPED,
            reason=f"{requested} executable not found",
            command=[],
            returnCode=None,
            stdout="",
            stderr="",
            workspace=None,
            verity=None,
        )

    resolved_workspace = _resolve_workspace(root, workspace)
    if workspace is not None and resolved_workspace is None:
        return VeritySpecCheckResult(
            status=CHECK_FAILED,
            reason=f"workspace not found: {workspace}",
            command=[],
            returnCode=None,
            stdout="",
            stderr="",
            workspace=workspace,
            verity=verity,
        )

    if resolved_workspace is None:
        command = [verity, "--version"]
        reason = "verity executable is available; no VeritySpec workspace fixture was found"
    else:
        command = [verity, "validate", str(resolved_workspace)]
        reason = "verity validate completed for the selected workspace"

    try:
        completed = subprocess.run(
            command,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired as exc:
        return VeritySpecCheckResult(
            status=CHECK_FAILED,
            reason=f"command timed out after {timeout_seconds} seconds",
            command=command,
            returnCode=None,
            stdout=exc.stdout or "",
            stderr=exc.stderr or "",
            workspace=str(resolved_workspace) if resolved_workspace else None,
            verity=verity,
        )

    status = CHECK_PASSED if completed.returncode == 0 else CHECK_FAILED
    return VeritySpecCheckResult(
        status=status,
        reason=reason if status == CHECK_PASSED else "verity smoke command failed",
        command=command,
        returnCode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
        workspace=str(resolved_workspace) if resolved_workspace else None,
        verity=verity,
    )


def format_verityspec_check_result(result: VeritySpecCheckResult) -> str:
    """Format a VeritySpec smoke check result for humans."""

    header = {
        CHECK_PASSED: "VeritySpec smoke check passed",
        CHECK_FAILED: "VeritySpec smoke check failed",
        CHECK_SKIPPED: "VeritySpec smoke check skipped",
    }.get(result.status, "VeritySpec smoke check result")

    lines = [f"{header}: {result.reason}"]
    if result.verity:
        lines.append(f"Verity executable: {result.verity}")
    if result.workspace:
        lines.append(f"Workspace: {result.workspace}")
    if result.command:
        lines.append(f"Command: {' '.join(result.command)}")
    if result.returnCode is not None:
        lines.append(f"Return code: {result.returnCode}")
    if result.stdout.strip():
        lines.append("Stdout:")
        lines.append(result.stdout.rstrip())
    if result.stderr.strip():
        lines.append("Stderr:")
        lines.append(result.stderr.rstrip())
    return "\n".join(lines) + "\n"


def _resolve_executable(executable: str | None) -> str | None:
    requested = executable or "verity"
    if os.sep in requested:
        path = Path(requested)
        if path.exists() and os.access(path, os.X_OK):
            return str(path)
        return None
    return shutil.which(requested)


def _resolve_workspace(root: Path, workspace: str | None) -> Path | None:
    if workspace is not None:
        candidate = Path(workspace)
        if not candidate.is_absolute():
            candidate = root / candidate
        return candidate if _looks_like_verityspec_workspace(candidate) else None

    candidates = [
        root,
        root / "examples" / "verityspec" / "basic",
        root / "examples" / "verityspec-workspace",
        root / "examples" / "generated-workspace",
        root / "generated-workspaces" / "basic",
    ]
    for candidate in candidates:
        if _looks_like_verityspec_workspace(candidate):
            return candidate

    examples = root / "examples"
    if examples.exists():
        for manifest in sorted(examples.rglob("verityspec.json")):
            return manifest.parent
    return None


def _looks_like_verityspec_workspace(path: Path) -> bool:
    return path.exists() and path.is_dir() and (path / "verityspec.json").exists()
