from __future__ import annotations

from jarvis.actions import Action

from .plan import Plan


class Planner:
    """
    Temporary rule-based planner.
    """

    def build(
        self,
        command: str,
    ) -> Plan:

        command = command.lower().strip()

        #
        # Type text
        #

        if command.startswith("type "):

            text = command.removeprefix(
                "type "
            ).strip()

            return Plan(
                actions=[
                    Action(
                        name="type",
                        target=text,
                    )
                ]
            )

        #
        # Open application
        #

        if command.startswith("open "):

            target = command.removeprefix(
                "open "
            ).strip()

            return Plan(
                actions=[
                    Action(
                        name="open",
                        target=target,
                    )
                ]
            )

        #
        # Close application
        #

        if command.startswith("close "):

            target = command.removeprefix(
                "close "
            ).strip()

            return Plan(
                actions=[
                    Action(
                        name="close",
                        target=target,
                    )
                ]
            )

        #
        # Focus / Activate application
        #

        if command.startswith("focus "):

            target = command.removeprefix(
                "focus "
            ).strip()

            return Plan(
                actions=[
                    Action(
                        name="focus",
                        target=target,
                    )
                ]
            )

        if command.startswith("activate "):

            target = command.removeprefix(
                "activate "
            ).strip()

            return Plan(
                actions=[
                    Action(
                        name="focus",
                        target=target,
                    )
                ]
            )

        #
        # Minimize application
        #

        if command.startswith("minimize "):

            target = command.removeprefix(
                "minimize "
            ).strip()

            return Plan(
                actions=[
                    Action(
                        name="minimize",
                        target=target,
                    )
                ]
            )

        #
        # Maximize application
        #

        if command.startswith("maximize "):

            target = command.removeprefix(
                "maximize "
            ).strip()

            return Plan(
                actions=[
                    Action(
                        name="maximize",
                        target=target,
                    )
                ]
            )

        #
        # Restore application
        #

        if command.startswith("restore "):

            target = command.removeprefix(
                "restore "
            ).strip()

            return Plan(
                actions=[
                    Action(
                        name="restore",
                        target=target,
                    )
                ]
            )


        #
        # Press key
        #

        if command.startswith("press "):

            key = command.removeprefix(
                "press "
            ).strip()

            return Plan(
                actions=[
                    Action(
                        name="press",
                        target=key,
                    )
                ]
            )

        #
        # Hotkey
        #

        if command.startswith("hotkey "):

            keys = command.removeprefix(
                "hotkey "
            ).strip()

            return Plan(
                actions=[
                    Action(
                        name="hotkey",
                        target=keys,
                    )
                ]
            )

        #
        # Mouse click
        #

        if command == "click":

            return Plan(
                actions=[
                    Action(
                        name="click",
                    )
                ]
            )

        #
        # Mouse double click
        #

        if command == "double click":

            return Plan(
                actions=[
                    Action(
                        name="double_click",
                    )
                ]
            )

        #
        # Mouse right click
        #

        if command == "right click":

            return Plan(
                actions=[
                    Action(
                        name="right_click",
                    )
                ]
            )

        #
        # Mouse scroll
        #

        if command.startswith("scroll "):

            amount = command.removeprefix(
                "scroll "
            ).strip()

            return Plan(
                actions=[
                    Action(
                        name="scroll",
                        target=amount,
                    )
                ]
            )

        #
        # Move mouse
        #

        if command.startswith("move mouse "):

            target = command.removeprefix(
                "move mouse "
            ).strip()

            return Plan(
                actions=[
                    Action(
                        name="move_mouse",
                        target=target,
                    )
                ]
            )

        return Plan(
            actions=[],
        )