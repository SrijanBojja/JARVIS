"""
Vision service.
"""

from __future__ import annotations

from jarvis.services.perception import PerceptionService

from .ollama_provider import OllamaVisionProvider
from .provider import VisionProvider
from jarvis.actions import Action

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
            self.capture_screen(),
            prompt,
        )

    def capture_screen(
        self,
    ) -> str:
        """
        Capture the current screen and return its image path.
        """

        return self._perception.capture_screen()

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

    def verify_action(
        self,
        action: Action,
    ) -> bool:
        """
        Verify whether an action succeeded.
        """

        prompt = f"""
        You are verifying a desktop automation step.

        Executed action:
        {action.name}

        Target:
        {action.target or "None"}

        Look at the screenshot.

        Determine whether the requested action has already
        succeeded.

        Respond with ONLY one word.

        YES

        or

        NO
        """

        image_path = self.capture_screen()

        result = self._provider.describe(
            image_path,
            prompt,
        )

        return (
            result.strip()
            .upper()
            .startswith("YES")
        )