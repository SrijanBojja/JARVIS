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

        return Plan(
            actions=[],
        )