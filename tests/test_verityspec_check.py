from pathlib import Path
import tempfile
import unittest

from verityfoundry.integration import (
    CHECK_FAILED,
    CHECK_PASSED,
    CHECK_SKIPPED,
    check_verityspec,
    format_verityspec_check_result,
)


ROOT = Path(__file__).resolve().parents[1]


class VeritySpecCheckTests(unittest.TestCase):
    def test_missing_verity_executable_skips(self) -> None:
        result = check_verityspec(ROOT, executable="/definitely/missing/verity")

        self.assertEqual(result.status, CHECK_SKIPPED)
        self.assertIn("not found", result.reason)
        self.assertEqual(result.command, [])

    def test_available_verity_without_workspace_runs_version_smoke(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            verity = _write_fake_verity(Path(tmp), "version")
            result = check_verityspec(ROOT, executable=str(verity))

        self.assertEqual(result.status, CHECK_PASSED)
        self.assertEqual(result.returnCode, 0)
        self.assertEqual(result.command[-1], "--version")
        self.assertIn("verity fake 1.0.0", result.stdout)
        self.assertIsNone(result.workspace)

    def test_workspace_runs_validate_smoke(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            verity = _write_fake_verity(tmp_path, "validate-pass")
            workspace = tmp_path / "workspace"
            workspace.mkdir()
            (workspace / "verityspec.json").write_text("{}", encoding="utf-8")

            result = check_verityspec(ROOT, workspace=str(workspace), executable=str(verity))

        self.assertEqual(result.status, CHECK_PASSED)
        self.assertEqual(result.returnCode, 0)
        self.assertEqual(result.command[1], "validate")
        self.assertEqual(result.command[2], str(workspace))
        self.assertIn("validated", result.stdout)

    def test_workspace_validate_failure_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            verity = _write_fake_verity(tmp_path, "validate-fail")
            workspace = tmp_path / "workspace"
            workspace.mkdir()
            (workspace / "verityspec.json").write_text("{}", encoding="utf-8")

            result = check_verityspec(ROOT, workspace=str(workspace), executable=str(verity))

        self.assertEqual(result.status, CHECK_FAILED)
        self.assertEqual(result.returnCode, 7)
        self.assertIn("failed", result.reason)
        self.assertIn("broken workspace", result.stderr)

    def test_format_includes_status_reason_and_command(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            verity = _write_fake_verity(Path(tmp), "version")
            result = check_verityspec(ROOT, executable=str(verity))

        text = format_verityspec_check_result(result)
        self.assertIn("VeritySpec smoke check passed", text)
        self.assertIn("Command:", text)
        self.assertIn("Stdout:", text)


def _write_fake_verity(directory: Path, mode: str) -> Path:
    script = directory / "verity"
    if mode == "validate-pass":
        body = """#!/bin/sh
if [ "$1" = "validate" ]; then
  echo "validated $2"
  exit 0
fi
echo "unexpected command" >&2
exit 2
"""
    elif mode == "validate-fail":
        body = """#!/bin/sh
if [ "$1" = "validate" ]; then
  echo "broken workspace" >&2
  exit 7
fi
echo "unexpected command" >&2
exit 2
"""
    else:
        body = """#!/bin/sh
if [ "$1" = "--version" ]; then
  echo "verity fake 1.0.0"
  exit 0
fi
echo "unexpected command" >&2
exit 2
"""
    script.write_text(body, encoding="utf-8")
    script.chmod(0o755)
    return script


if __name__ == "__main__":
    unittest.main()
