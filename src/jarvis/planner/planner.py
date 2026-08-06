from __future__ import annotations

from jarvis.actions import Action

from .plan import Plan

from .result import PlanningResult

class Planner:
    """
    Temporary rule-based planner.
    """

    def build(
        self,
        command: str,
    ) -> PlanningResult:

        command = command.lower().strip()
        if " and " in command:
            return self._plan_compound(
                command,
            )

        #
        # Type text
        #

        if command.startswith("type "):

            text = command.removeprefix(
                "type "
            ).strip()

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="type",
                            target=text,
                        )
                    ],
                ),
                remaining_text="",
            )

        #
        # Open application
        #

        if command.startswith("open "):

            target = command.removeprefix(
                "open "
            ).strip()

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="open",
                            target=target,
                        )
                    ],
                ),
                remaining_text="",
            )

        #
        # Close application
        #

        if command.startswith("close "):

            target = command.removeprefix(
                "close "
            ).strip()

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="close",
                            target=target,
                        )
                    ],
                ),
                remaining_text="",
            )

        #
        # Focus / Activate application
        #

        if command.startswith("focus "):

            target = command.removeprefix(
                "focus "
            ).strip()

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="focus",
                            target=target,
                        )
                    ],
                ),
                remaining_text="",
            )

        if command.startswith("activate "):

            target = command.removeprefix(
                "activate "
            ).strip()

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="focus",
                            target=target,
                        )
                    ],
                ),
                remaining_text="",
            )

        #
        # Minimize application
        #

        if command.startswith("minimize "):

            target = command.removeprefix(
                "minimize "
            ).strip()

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="minimize",
                            target=target,
                        )
                    ],
                ),
                remaining_text="",
            )

        #
        # Maximize application
        #

        if command.startswith("maximize "):

            target = command.removeprefix(
                "maximize "
            ).strip()

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="maximize",
                            target=target,
                        )
                    ],
                ),
                remaining_text="",
            )

        #
        # Restore application
        #

        if command.startswith("restore "):

            target = command.removeprefix(
                "restore "
            ).strip()

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="restore",
                            target=target,
                        )
                    ],
                ),
                remaining_text="",
            )


        #
        # Press key
        #

        if command.startswith("press "):

            key = command.removeprefix(
                "press "
            ).strip()

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="press",
                            target=key,
                        )
                    ],
                ),
                remaining_text="",
            )

        #
        # Hotkey
        #

        if command.startswith("hotkey "):

            keys = command.removeprefix(
                "hotkey "
            ).strip()

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="hotkey",
                            target=keys,
                        )
                    ],
                ),
                remaining_text="",
            )
        #
        # Mouse click
        #

        if command == "click":

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="click",
                        )
                    ],
                ),
                remaining_text="",
            )

        #
        # Mouse double click
        #

        if command == "double click":

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="double_click",
                        )
                    ],
                ),
                remaining_text="",
            )

        #
        # Mouse right click
        #

        if command == "right click":

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="right_click",
                        )
                    ],
                ),
                remaining_text="",
            )

        #
        # Mouse scroll
        #

        if command.startswith("scroll "):

            amount = command.removeprefix(
                "scroll "
            ).strip()

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="scroll",
                            target=amount,
                        )
                    ],
                ),
                remaining_text="",
            )

        #
        # Move mouse
        #

        if command.startswith("move mouse "):

            target = command.removeprefix(
                "move mouse "
            ).strip()

            return PlanningResult(
                plan=Plan(
                    actions=[
                        Action(
                            name="move_mouse",
                            target=target,
                        )
                    ],
                ),
                remaining_text="",
            )

        return PlanningResult(
            plan=Plan(
                actions=[],
            ),
            remaining_text=command,
        )

    def _plan_compound(
        self,
        command: str,
    ) -> PlanningResult:

        actions: list[Action] = []

        remaining_parts: list[str] = []

        parts = [
            part.strip()
            for part in command.split(" and ")
        ]

        for part in parts:

            result = self.build(
                part,
            )

            actions.extend(
                result.plan.actions,
            )

            if result.remaining_text:
                remaining_parts.append(
                    result.remaining_text,
                )

        return PlanningResult(
            plan=Plan(
                actions=actions,
            ),
            remaining_text=" and ".join(
                remaining_parts,
            ),
        )