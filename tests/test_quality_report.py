from pathlib import Path
import unittest

from verityfoundry.quality import format_prompt_quality_report, generate_prompt_quality_report


ROOT = Path(__file__).resolve().parents[1]


class PromptQualityReportTests(unittest.TestCase):
    def test_prompt_quality_report_scores_prompts(self) -> None:
        report = generate_prompt_quality_report(ROOT)
        self.assertGreater(report["promptCount"], 0)
        self.assertGreater(report["score"], 0)
        self.assertGreater(report["uncertaintyPreservation"]["score"], 0)
        self.assertGreater(report["provenanceCompleteness"]["score"], 0)
        self.assertEqual(len(report["weakestPrompts"]), 5)

    def test_domain_prompt_gets_uncertainty_and_provenance_evidence(self) -> None:
        report = generate_prompt_quality_report(ROOT)
        prompts = {prompt["id"]: prompt for prompt in report["prompts"]}
        prompt = prompts["unity-game.gdd-art.interview-medium.implementation-ready.v1"]
        self.assertEqual(prompt["uncertaintyPreservation"]["score"], 6)
        self.assertIn(
            "source-references",
            prompt["provenanceCompleteness"]["matched"],
        )
        self.assertIn(
            "verityspec-validation-authority",
            prompt["provenanceCompleteness"]["matched"],
        )

    def test_prompt_quality_report_formats_text(self) -> None:
        report = generate_prompt_quality_report(ROOT)
        text = format_prompt_quality_report(report)
        self.assertIn("Prompt Quality Report", text)
        self.assertIn("Uncertainty preservation:", text)
        self.assertIn("Provenance completeness:", text)
        self.assertIn("Weakest prompts:", text)


if __name__ == "__main__":
    unittest.main()
