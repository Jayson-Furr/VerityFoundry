from pathlib import Path
import tempfile
import unittest

from verityfoundry.workflow_hygiene import (
    check_workflow_hygiene,
    format_workflow_hygiene_report,
)


ROOT = Path(__file__).resolve().parents[1]


class WorkflowHygieneTests(unittest.TestCase):
    def test_workflow_hygiene_passes_repository_workflows(self) -> None:
        report = check_workflow_hygiene(ROOT)

        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["issueCount"], 0)
        self.assertGreaterEqual(report["actionCount"], 1)

        text = format_workflow_hygiene_report(report)
        self.assertIn("Workflow Hygiene Check", text)
        self.assertIn("Workflow hygiene check passed.", text)

    def test_workflow_hygiene_fails_stale_action_major(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workflow_dir = root / ".github" / "workflows"
            workflow_dir.mkdir(parents=True)
            (workflow_dir / "ci.yml").write_text(
                """name: CI
jobs:
  test:
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
""",
                encoding="utf-8",
            )

            report = check_workflow_hygiene(root)

        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["issueCount"], 2)
        codes = {issue["code"] for issue in report["issues"]}
        self.assertEqual(codes, {"workflow.action-stale-major"})


if __name__ == "__main__":
    unittest.main()
