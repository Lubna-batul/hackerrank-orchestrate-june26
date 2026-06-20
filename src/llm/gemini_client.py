import os
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv(Path(__file__).parents[2] / ".env", override=True)


class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        print("\n========== GEMINI CLIENT ==========")
        print("Loaded Key:", api_key[:15])
        print("===================================\n")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found.")

        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str):
        for attempt in range(5):
            try:
                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )
                return response.text

            except Exception as e:
                print(f"Text request attempt {attempt + 1} failed: {e}")

                if attempt == 4:
                    raise

                time.sleep(5)

    def generate_with_images(self, prompt: str, image_paths: list[str]):
        contents = [prompt]

        for image_path in image_paths:
            image = Image.open(Path(image_path))
            contents.append(image)

        for attempt in range(5):
            try:
                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=contents,
                )
                return response.text

            except Exception as e:
                print(f"Image request attempt {attempt + 1} failed: {e}")

                if attempt == 4:
                    raise

                time.sleep(5)