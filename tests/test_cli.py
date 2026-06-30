from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "verityfoundry", "--root", str(ROOT), *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


class CliTests(unittest.TestCase):
    def test_version(self) -> None:
        result = run_cli("--version")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("verityfoundry 0.5.0", result.stdout)

    def test_list_prompts(self) -> None:
        result = run_cli("list", "prompts")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("unity-game.gdd-art.interview-medium.implementation-ready.v1", result.stdout)

    def test_list_matrices(self) -> None:
        result = run_cli("list", "matrices")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("unity-game", result.stdout)

    def test_validate_all(self) -> None:
        result = run_cli("validate")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Validation passed.", result.stdout)

    def test_validate_examples_json(self) -> None:
        result = run_cli("validate", "examples", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('"issueCount": 0', result.stdout)

    def test_validate_goldens_json(self) -> None:
        result = run_cli("validate", "goldens", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('"issueCount": 0', result.stdout)

    def test_render_prompt(self) -> None:
        result = run_cli(
            "render",
            "--prompt",
            "unity-game.gdd-art.interview-medium.implementation-ready.v1",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("VerityFoundry Rendered Prompt", result.stdout)
        self.assertIn("Included: VeritySpec Context", result.stdout)
        self.assertIn("Prompt Workflow", result.stdout)

    def test_render_prompt_to_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "prompt.md"
            result = run_cli(
                "render",
                "--prompt",
                "unity-game.gdd-art.interview-medium.implementation-ready.v1",
                "--out",
                str(out),
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(out.exists())
            self.assertIn("Wrote", result.stdout)

    def test_matrix_command(self) -> None:
        result = run_cli("matrix", "unity-game")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Unity Game Prompt Matrix", result.stdout)

    def test_prompt_quality_report_text(self) -> None:
        result = run_cli("report", "prompt-quality")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Prompt Quality Report", result.stdout)
        self.assertIn("Uncertainty preservation:", result.stdout)
        self.assertIn("Provenance completeness:", result.stdout)

    def test_prompt_quality_report_json(self) -> None:
        result = run_cli("report", "prompt-quality", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"promptCount"', result.stdout)
        self.assertIn('"uncertaintyPreservation"', result.stdout)
        self.assertIn('"provenanceCompleteness"', result.stdout)

    def test_verityspec_check_skips_when_verity_is_missing(self) -> None:
        result = run_cli(
            "check",
            "verityspec",
            "--verity",
            "/definitely/missing/verity",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"status": "skipped"', result.stdout)
        self.assertIn("not found", result.stdout)

    def test_unknown_prompt_fails_usage(self) -> None:
        result = run_cli("render", "--prompt", "missing.prompt.v1")
        self.assertEqual(result.returncode, 2)
        self.assertIn("unknown prompt id", result.stderr)


if __name__ == "__main__":
    unittest.main()
