import json
from pathlib import Path
from dataclasses import asdict

from src.llm.gemini_client import GeminiClient


class EvidenceMatchingAgent:

    def __init__(self):
        self.client = GeminiClient()
        self.prompt = self._load_prompt()

    def _load_prompt(self):
        prompt_path = Path("prompts") / "evidence_matching.txt"

        if not prompt_path.exists():
            raise FileNotFoundError(f"Prompt not found: {prompt_path}")

        return prompt_path.read_text(encoding="utf-8")

    def match(self, claim: dict, image_analysis: dict):

        prompt = (
            self.prompt
            .replace("{claim}", json.dumps(asdict(claim), indent=2))
            .replace("{image_analysis}", json.dumps(image_analysis, indent=2))
        )

        response = self.client.generate(prompt)

        print("========== EVIDENCE MATCHING RESPONSE ==========")
        print(response)
        print("================================================")

        response = (
            response.replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(response)