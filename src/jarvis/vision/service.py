"""
Vision service.
"""

from __future__ import annotations

from jarvis.services.perception import PerceptionService

from .ollama_provider import OllamaVisionProvider
from .provider import VisionProvider


class VisionService:

    def __init__(
        self,
        perception: PerceptionService,
        provider: VisionProvider | None = None,
    ) -> None:

        self._perception = perception
        self._provider = (
            provider or OllamaVisionProvider()
        )

    def describe_screen(
        self,
        prompt = """
            You are JARVIS.

            Describe the screen in under 80 words.

            Mention only:
            - active application
            - visible windows
            - important buttons
            - text fields
            - anything the assistant should interact with

            Do not explain.
            Do not speculate.
            Be concise.
            """
    ) -> str:

        return self._provider.describe(
            r"C:\Users\srija\AppData\Local\Temp\jarvis\screenshots\20260803_201852.png",
            prompt,
        )

    def describe_image(
        self,
        image_path: str,
        prompt: str = (
            "Describe this image."
        ),
    ) -> str:

        return self._provider.describe(
            image_path,
            prompt,
        )