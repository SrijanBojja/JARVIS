"""
AI Planner.
"""

from __future__ import annotations

from jarvis.ai import AIService

from .plan import Plan

from .prompt import build_planner_prompt

from .parser import PlannerParser

from .validator import PlannerValidator

class AIPlanner:
    """
    Builds execution plans using AI.
    """

    def __init__(
        self,
        ai_service: AIService,
        parser: PlannerParser,
        validator: PlannerValidator,
    ) -> None:

        self._ai_service = ai_service
        self._parser = parser
        self._validator = validator

    def build(
        self,
        request: str,
    ) -> Plan:
        """
        Build an action plan using AI.
        """

        prompt = build_planner_prompt(
            request,
        )

        response = self._ai_service.chat(
            prompt,
        )

        print(response.text)

        plan = self._parser.parse(
            response.text,
        )
        return self._validator.validate(
            plan,
        )