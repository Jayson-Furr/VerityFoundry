from pathlib import Path
import unittest

from verityfoundry.manifests import load_prompt_manifests
from verityfoundry.validation import validate_prompts


ROOT = Path(__file__).resolve().parents[1]


class PromptManifestTests(unittest.TestCase):
    def test_prompt_manifests_validate(self) -> None:
        self.assertEqual(validate_prompts(ROOT), [])

    def test_expected_prompt_ids_exist(self) -> None:
        ids = {item.manifest["id"] for item in load_prompt_manifests(ROOT)}
        self.assertIn("lifecycle.workspace.interview-medium.production-ready.release-gap-review.v1", ids)
        self.assertIn("lifecycle.shipped-product.interview-high.maintenance-ready.v1", ids)
        self.assertIn("lifecycle.retiring-product.interview-all.decommission-ready.v1", ids)
        self.assertIn("portfolio.games.interview-low.concept-complete.v1", ids)
        self.assertIn("portfolio.dependencies.interview-medium.implementation-ready.v1", ids)
        self.assertIn("unity-game.gdd-art.interview-medium.implementation-ready.v1", ids)
        self.assertIn("unity-library.description.interview-medium.implementation-ready.v1", ids)
        self.assertIn("decision-policy.medium-stakes.v1", ids)

    def test_prompt_manifests_preserve_human_approval_for_domain_prompts(self) -> None:
        domain_prompts = [
            item
            for item in load_prompt_manifests(ROOT)
            if item.manifest["kind"] == "domain-prompt"
        ]
        self.assertGreaterEqual(len(domain_prompts), 10)
        for prompt in domain_prompts:
            self.assertTrue(prompt.manifest["requiresHumanApproval"], prompt.path)


if __name__ == "__main__":
    unittest.main()
