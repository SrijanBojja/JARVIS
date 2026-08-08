"""
Vision-based automation verification.
"""

from __future__ import annotations

from jarvis.actions import Action
from jarvis.responses import Response
from jarvis.vision import VisionService


class VisionAutomationVerifier:
    """
    Verifies automation actions using visual feedback.
    """

    def __init__(
        self,
        vision_service: VisionService,
    ) -> None:

        self._vision_service = vision_service

    def verify(
        self,
        action: Action,
        response: Response | None = None,
    ) -> bool:
        """
        Verify whether an automation action succeeded.
        """

        result = self._vision_service.verify_action(
            action,
            response,
        )

        print(
            f"[VISION VERIFY] "
            f"{action.name}({action.target}) -> {result}"
        )

        return result