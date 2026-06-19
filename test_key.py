import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

try:
    models = list(client.models.list())
    print("SUCCESS")
    print(models[0].name if models else "No models found")
except Exception as e:
    print(e)
