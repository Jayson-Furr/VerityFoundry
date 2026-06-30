from pathlib import Path
import unittest

from verityfoundry.manifests import load_prompt_manifests
from verityfoundry.policy_lint import HIGH_RISK_INTERVIEW_MODES, HIGH_RISK_TARGETS
from verityfoundry.rendering import render_profiles, render_prompt


ROOT = Path(__file__).resolve().parents[1]


class RenderProfileTests(unittest.TestCase):
    def test_render_profiles_include_expected_agents(self) -> None:
        profile_ids = {profile["id"] for profile in render_profiles()}

        self.assertIn("codex", profile_ids)
        self.assertIn("claude-code", profile_ids)
        self.assertIn("chatgpt", profile_ids)
        self.assertIn("gemini", profile_ids)
        self.assertIn("github-copilot", profile_ids)
        self.assertIn("unity-ai", profile_ids)

    def test_codex_profile_adds_handoff_guidance(self) -> None:
        rendered = render_prompt(
            ROOT,
            "unity-game.gdd-art.interview-medium.implementation-ready.v1",
            profile="codex",
        )

        self.assertIn("Profile: Codex", rendered)
        self.assertIn("## Agent Handoff Profile", rendered)
        self.assertIn("bounded repository context", rendered)
        self.assertIn("## Prompt Workflow", rendered)

    def test_github_copilot_profile_adds_handoff_guidance(self) -> None:
        rendered = render_prompt(
            ROOT,
            "unity-game.gdd-art.interview-medium.implementation-ready.v1",
            profile="github-copilot",
        )

        self.assertIn("Profile: GitHub Copilot", rendered)
        self.assertIn("Copilot-assisted edits", rendered)
        self.assertIn("## Agent Handoff Profile", rendered)

    def test_default_profile_omits_handoff_guidance(self) -> None:
        rendered = render_prompt(
            ROOT,
            "unity-game.gdd-art.interview-medium.implementation-ready.v1",
        )

        self.assertIn("Profile: Default", rendered)
        self.assertNotIn("## Agent Handoff Profile", rendered)

    def test_high_risk_prompts_render_safety_and_provenance_for_agent_profiles(self) -> None:
        profile_ids = [
            profile["id"]
            for profile in render_profiles()
            if profile["id"] != "default"
        ]
        high_risk_prompt_ids = [
            str(prompt.manifest["id"])
            for prompt in load_prompt_manifests(ROOT)
            if prompt.manifest.get("kind") == "domain-prompt"
            and (
                prompt.manifest.get("interviewMode") in HIGH_RISK_INTERVIEW_MODES
                or prompt.manifest.get("targetReadiness") in HIGH_RISK_TARGETS
            )
        ]

        self.assertGreater(len(high_risk_prompt_ids), 0)
        self.assertGreater(len(profile_ids), 0)
        for prompt_id in high_risk_prompt_ids:
            for profile_id in profile_ids:
                with self.subTest(prompt_id=prompt_id, profile_id=profile_id):
                    rendered = render_prompt(ROOT, prompt_id, profile=profile_id)
                    self.assertIn("## Included: Safety and Uncertainty Rules", rendered)
                    self.assertIn("## Included: Provenance Rules", rendered)


if __name__ == "__main__":
    unittest.main()
