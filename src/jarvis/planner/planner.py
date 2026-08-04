from jarvis.actions import Action
from .plan import Plan


class Planner:

    def build(
        self,
        command: str,
    ) -> Plan:

        command = command.lower().strip()

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

        return Plan(
            actions=[],
        )