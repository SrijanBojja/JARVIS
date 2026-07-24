"""
Calculator skill.
"""

from __future__ import annotations

import math

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
    ) -> None:

        if not args:
            print("Usage: calc <expression>")
            return

        expression = " ".join(args)

        try:
            result = eval(
                expression,
                {
                    "__builtins__": {},
                    "math": math,
                },
            )

            print(result)

        except Exception as error:
            print(f"Calculation error: {error}")