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
        self.assertIn("verityfoundry 0.17.0", result.stdout)

    def test_list_prompts(self) -> None:
        result = run_cli("list", "prompts")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("unity-game.gdd-art.interview-medium.implementation-ready.v1", result.stdout)

    def test_list_matrices(self) -> None:
        result = run_cli("list", "matrices")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("unity-game", result.stdout)

    def test_list_profiles(self) -> None:
        result = run_cli("list", "profiles")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("codex", result.stdout)
        self.assertIn("github-copilot", result.stdout)
        self.assertIn("unity-ai", result.stdout)

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

    def test_render_prompt_with_profile(self) -> None:
        result = run_cli(
            "render",
            "--prompt",
            "unity-game.gdd-art.interview-medium.implementation-ready.v1",
            "--profile",
            "codex",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Profile: Codex", result.stdout)
        self.assertIn("Agent Handoff Profile", result.stdout)

    def test_render_prompt_to_file_for_every_profile(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            for profile in (
                "default",
                "codex",
                "claude-code",
                "chatgpt",
                "gemini",
                "github-copilot",
                "unity-ai",
            ):
                with self.subTest(profile=profile):
                    out = Path(tmp) / f"{profile}.md"
                    result = run_cli(
                        "render",
                        "--prompt",
                        "unity-game.gdd-art.interview-medium.implementation-ready.v1",
                        "--profile",
                        profile,
                        "--out",
                        str(out),
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertTrue(out.exists())
                    self.assertIn("VerityFoundry Rendered Prompt", out.read_text())

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

    def test_prompt_quality_trend_report_text(self) -> None:
        result = run_cli("report", "prompt-quality-trend")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Prompt Quality Trend Report", result.stdout)
        self.assertIn("Latest snapshot: v0.11.0", result.stdout)

    def test_prompt_quality_trend_report_json(self) -> None:
        result = run_cli("report", "prompt-quality-trend", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"snapshotCount"', result.stdout)
        self.assertIn('"deltaFromLatest"', result.stdout)

    def test_policy_lint_trend_report_text(self) -> None:
        result = run_cli("report", "policy-lint-trend")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Policy Lint Trend Report", result.stdout)
        self.assertIn("Latest snapshot: v0.17.0", result.stdout)

    def test_policy_lint_trend_report_json(self) -> None:
        result = run_cli("report", "policy-lint-trend", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"snapshotCount"', result.stdout)
        self.assertIn('"deltaFromLatest"', result.stdout)

    def test_matrix_coverage_report_text(self) -> None:
        result = run_cli("report", "matrix-coverage")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Matrix Coverage Report", result.stdout)
        self.assertIn("Domain prompt coverage:", result.stdout)

    def test_matrix_coverage_report_json(self) -> None:
        result = run_cli("report", "matrix-coverage", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"matrixCount"', result.stdout)
        self.assertIn('"missingDomainPrompts"', result.stdout)

    def test_release_summary_report_text(self) -> None:
        result = run_cli("report", "release-summary")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Release Summary Report", result.stdout)
        self.assertIn("Release integrity: passed", result.stdout)
        self.assertIn("Workflow hygiene: passed", result.stdout)

    def test_release_summary_report_json(self) -> None:
        result = run_cli("report", "release-summary", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"blockingIssueCount": 0', result.stdout)
        self.assertIn('"releaseIntegrity"', result.stdout)
        self.assertIn('"goldenInventory"', result.stdout)

    def test_golden_inventory_report_text(self) -> None:
        result = run_cli("report", "golden-inventory")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Golden Output Inventory Report", result.stdout)
        self.assertIn("golden.unity-game.dream-extraction.implementation-ready", result.stdout)

    def test_golden_inventory_report_json(self) -> None:
        result = run_cli("report", "golden-inventory", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"goldenCount"', result.stdout)
        self.assertIn('"goldens"', result.stdout)

    def test_example_inventory_report_text(self) -> None:
        result = run_cli("report", "example-inventory")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Example Inventory Report", result.stdout)
        self.assertIn("example.unity-game.dream-extraction", result.stdout)

    def test_example_inventory_report_json(self) -> None:
        result = run_cli("report", "example-inventory", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"exampleCount"', result.stdout)
        self.assertIn('"examples"', result.stdout)

    def test_fixture_inventory_report_text(self) -> None:
        result = run_cli("report", "fixture-inventory")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Fixture Inventory Report", result.stdout)
        self.assertIn("Recommended packs:", result.stdout)

    def test_fixture_inventory_report_json(self) -> None:
        result = run_cli("report", "fixture-inventory", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"fixtureCount"', result.stdout)
        self.assertIn('"packs"', result.stdout)

    def test_provenance_coverage_report_text(self) -> None:
        result = run_cli("report", "provenance-coverage")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Provenance Coverage Report", result.stdout)
        self.assertIn("Record provenance:", result.stdout)

    def test_provenance_coverage_report_json(self) -> None:
        result = run_cli("report", "provenance-coverage", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"recordProvenancePercent"', result.stdout)
        self.assertIn('"decisionExamplePercent"', result.stdout)

    def test_decision_policy_lint(self) -> None:
        result = run_cli("lint", "decision-policy")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Decision policy lint passed with warnings.", result.stdout)
        self.assertIn("policy.advisory-missing-output-contract", result.stdout)

    def test_decision_policy_lint_json(self) -> None:
        result = run_cli("lint", "decision-policy", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('"errorCount": 0', result.stdout)
        self.assertIn('"status": "passed"', result.stdout)
        self.assertIn('"warningCount"', result.stdout)

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

    def test_release_integrity_check_passes(self) -> None:
        result = run_cli("check", "release-integrity")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Release integrity check passed.", result.stdout)

    def test_release_integrity_check_json_failure(self) -> None:
        result = run_cli(
            "check",
            "release-integrity",
            "--expected-version",
            "0.0.0",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn('"status": "failed"', result.stdout)
        self.assertIn('"issueCount"', result.stdout)

    def test_quality_thresholds_check_passes(self) -> None:
        result = run_cli("check", "quality-thresholds")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Quality threshold check passed.", result.stdout)
        self.assertIn("Policy lint: 0 errors, 14 warnings", result.stdout)

    def test_workflow_hygiene_check_passes(self) -> None:
        result = run_cli("check", "workflow-hygiene")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Workflow hygiene check passed.", result.stdout)

    def test_unknown_prompt_fails_usage(self) -> None:
        result = run_cli("render", "--prompt", "missing.prompt.v1")
        self.assertEqual(result.returncode, 2)
        self.assertIn("unknown prompt id", result.stderr)


if __name__ == "__main__":
    unittest.main()
