"""
Calculator skill.
"""

from __future__ import annotations

import math

from jarvis.responses import Response
from jarvis.skills import Skill


class CalculatorSkill(Skill):
    """
    Evaluate mathematical expressions.
    """

    @property
    def name(self) -> str:
        return "calc"

    @property
    def description(self) -> str:
        return "Evaluate mathematical expressions."

    def execute(
        self,
        args: list[str],
    ) -> Response:

        if not args:
            return Response(
                "Usage: calc <expression>",
            )

        expression = " ".join(args)

        try:
            result = eval(
                expression,
                {
                    "__builtins__": {},
                    "math": math,
                },
            )

            return Response(str(result))

        except Exception as error:
            return Response(
                f"Calculation error: {error}",
            )