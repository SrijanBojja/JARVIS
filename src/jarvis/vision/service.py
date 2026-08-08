"""
Vision service.
"""

from __future__ import annotations

from jarvis.actions import Action
from jarvis.responses import Response
from jarvis.services.perception import PerceptionService

from .ollama_provider import OllamaVisionProvider
from .provider import VisionProvider


class VisionService:
    """
    Provides visual understanding capabilities.
    """

    def __init__(
        self,
        perception: PerceptionService,
        provider: VisionProvider | None = None,
    ) -> None:

        self._perception = perception

        self._provider = (
            provider or OllamaVisionProvider()
        )

    def capture_screen(
        self,
    ) -> str:
        """
        Capture the current screen and return its image path.
        """

        return self._perception.capture_screen()

    def describe_screen(
        self,
        prompt: str = """
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
        """,
    ) -> str:
        """
        Describe the current screen.
        """

        image_path = self.capture_screen()

        return self._provider.describe(
            image_path,
            prompt,
        )

    def verify_action(
        self,
        action: Action,
        response: Response | None = None,
    ) -> bool:
        """
        Verify whether an executed action has succeeded.
        """

        execution_result = (
            response.text
            if response is not None
            else "No execution result available."
        )

        prompt = f"""
    You are JARVIS verifying a desktop automation action.

    ACTION:
    {action.name}

    TARGET:
    {action.target or "None"}

    SYSTEM EXECUTION RESULT:
    {execution_result}

    Look at the current screenshot and determine whether
    the requested final state is satisfied.

    IMPORTANT DECISION RULES:

    1. The system execution result is authoritative evidence
    about what happened.

    2. If the execution result says that an application is
    "already running", "already open", or equivalent,
    then an OPEN action is SUCCESSFUL.

    3. If the execution result indicates that an application
    was opened successfully, then an OPEN action is
    SUCCESSFUL unless the screenshot clearly proves
    otherwise.

    4. If the action is FOCUS, the target application should
    be the active or foreground application.

    5. If the action is CLOSE, the target application should
    no longer be running or visible.

    6. If the requested final state was already satisfied
    before the action, consider the action SUCCESSFUL.

    7. Only answer NO when there is clear evidence that the
    requested final state is NOT satisfied.

    ACTION SUCCESS means the requested final state exists,
    not necessarily that the screen visibly changed.

    Respond with exactly one word:

    YES

    or

    NO
    """

        image_path = self.capture_screen()

        result = self._provider.describe(
            image_path,
            prompt,
        )

        print(
            f"[VISION RAW] {result.strip()}"
        )

        return (
            result.strip()
            .upper()
            .startswith("YES")
        )
    def describe_image(
        self,
        image_path: str,
        prompt: str = "Describe this image.",
    ) -> str:
        """
        Describe an image.
        """

        return self._provider.describe(
            image_path,
            prompt,
        )