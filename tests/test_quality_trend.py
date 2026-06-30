from pathlib import Path
import unittest

from verityfoundry.quality_trend import (
    format_prompt_quality_trend_report,
    generate_prompt_quality_trend_report,
)


ROOT = Path(__file__).resolve().parents[1]


class PromptQualityTrendTests(unittest.TestCase):
    def test_prompt_quality_trend_uses_snapshot(self) -> None:
        report = generate_prompt_quality_trend_report(ROOT)

        self.assertGreaterEqual(report["snapshotCount"], 1)
        self.assertEqual(report["latestSnapshot"]["label"], "v0.11.0")
        self.assertEqual(report["current"]["promptCount"], 46)
        self.assertIsNotNone(report["deltaFromLatest"])

        text = format_prompt_quality_trend_report(report)
        self.assertIn("Prompt Quality Trend Report", text)
        self.assertIn("Latest snapshot: v0.11.0", text)


if __name__ == "__main__":
    unittest.main()
