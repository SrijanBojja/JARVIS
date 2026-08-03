from jarvis.services.perception import PerceptionService
from jarvis.tools import Tool, ToolMetadata


class RunningProcessesTool(Tool):

    def __init__(self, perception: PerceptionService):
        self._perception = perception

    @property
    def metadata(self):
        return ToolMetadata(
            name="running_processes",
            description="Returns the number of running processes.",
        )

    def execute(self):
        return self._perception.running_processes()