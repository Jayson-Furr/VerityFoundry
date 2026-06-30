from pathlib import Path
import unittest

from verityfoundry.rendering import render_profiles, render_prompt


ROOT = Path(__file__).resolve().parents[1]


class RenderProfileTests(unittest.TestCase):
    def test_render_profiles_include_expected_agents(self) -> None:
        profile_ids = {profile["id"] for profile in render_profiles()}

        self.assertIn("codex", profile_ids)
        self.assertIn("claude-code", profile_ids)
        self.assertIn("chatgpt", profile_ids)
        self.assertIn("gemini", profile_ids)
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

    def test_default_profile_omits_handoff_guidance(self) -> None:
        rendered = render_prompt(
            ROOT,
            "unity-game.gdd-art.interview-medium.implementation-ready.v1",
        )

        self.assertIn("Profile: Default", rendered)
        self.assertNotIn("## Agent Handoff Profile", rendered)


if __name__ == "__main__":
    unittest.main()
