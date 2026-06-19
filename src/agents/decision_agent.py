import json

from src.llm.gemini_client import GeminiClient
from src.llm.json_parser import JsonParser
from src.models.decision import Decision


class DecisionAgent:

    def __init__(self):
        self.client = GeminiClient()
        with open("prompts/decision.txt", "r", encoding="utf-8") as f:
            self.prompt = f.read()

    def decide(
        self,
        claim,
        matching,
    ):

        prompt = (
            self.prompt
            .replace("{claim}", json.dumps(claim.__dict__, indent=2))
            .replace("{matching}", json.dumps(matching, indent=2))
        )

        response = self.client.generate(prompt)

        print("========== DECISION RESPONSE ==========")
        print(response)
        print("=======================================\n")

        data = JsonParser.parse(response)

        return Decision(**data)