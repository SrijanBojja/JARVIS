"""
Random skill.
"""

from __future__ import annotations

import random

from jarvis.responses import Response
from jarvis.skills import Skill


class RandomSkill(Skill):
    """
    Generate random numbers.
    """

    @property
    def name(self) -> str:
        return "random"

    @property
    def description(self) -> str:
        return "Generate a random number."

    @property
    def aliases(self) -> list[str]:
        return [
            "random number",
            "rand",
            "generate random",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        try:

            if len(args) == 0:
                value = random.randint(
                    1,
                    100,
                )

            elif len(args) == 1:
                maximum = int(args[0])

                value = random.randint(
                    1,
                    maximum,
                )

            elif len(args) == 2:
                minimum = int(args[0])
                maximum = int(args[1])

                value = random.randint(
                    minimum,
                    maximum,
                )

            else:
                return Response(
                    "Usage: random [max] or random [min] [max]",
                )

            return Response(
                f"Random number: {value}",
            )

        except ValueError:
            return Response(
                "Arguments must be integers.",
            )