import json
from pathlib import Path
from src.llm.json_parser import JsonParser
from src.models.extracted_claim import ExtractedClaim

from src.llm.gemini_client import GeminiClient


class ClaimExtractionAgent:

    def __init__(self):
        self.client = GeminiClient()
        self.prompt = self._load_prompt()

    def _load_prompt(self):
        prompt_path = Path("prompts") / "claim_extraction.txt"
        return prompt_path.read_text(encoding="utf-8")

    def extract(self, conversation: str):

        prompt = self.prompt.replace(
            "{conversation}",
            conversation
        )

        response = self.client.generate(prompt)

        data = JsonParser.parse(response)

        return ExtractedClaim(
            object_type=data["object_type"],
            claimed_issue=data["claimed_issue"],
            claimed_part=data["claimed_part"],
            claim_summary=data["claim_summary"],
)