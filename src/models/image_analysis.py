import json
from pathlib import Path

from src.llm.gemini_client import GeminiClient


class ImageAnalysisAgent:

    def __init__(self):
        self.client = GeminiClient()
        self.prompt = self._load_prompt()

    def _load_prompt(self):
        prompt_path = Path("prompts") / "image_analysis.txt"
        return prompt_path.read_text(encoding="utf-8")

    def analyze(self, image_paths: list[str]):
        response = self.client.generate_with_images(
            self.prompt,
            image_paths,
        )

        print("========== GEMINI IMAGE RESPONSE ==========")
        print(response)
        print("===========================================")

        response = (
            response.replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(response)