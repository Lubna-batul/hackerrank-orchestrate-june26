import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv(Path(__file__).parents[2] / ".env", override=True)


class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found.")

        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text

    def generate_with_images(self, prompt: str, image_paths: list[str]):
        contents = [prompt]

        for image_path in image_paths:
            image = Image.open(Path(image_path))
            contents.append(image)

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents,
        )

        return response.text