from src.llm.gemini_client import GeminiClient

client = GeminiClient()
print(client.generate("Say hello"))