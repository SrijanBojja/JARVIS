"""
Vision runtime using the official Ollama Python client.
"""

from __future__ import annotations

from ollama import chat


class VisionRuntime:

    def __init__(
        self,
        model: str = "qwen2.5vl:3b",
    ) -> None:
        self._model = model

    def describe(
        self,
        image_path: str,
        prompt: str,
    ) -> str:

        print("=" * 60)
        print("VISION DEBUG")
        print("=" * 60)
        print("Image:", image_path)

        response = chat(
            model=self._model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                    "images": [image_path],
                }
            ],
        )

        return response.message.content