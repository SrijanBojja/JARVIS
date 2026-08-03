from jarvis.services.perception import PerceptionService
from jarvis.tools import Tool, ToolMetadata


class ActiveWindowTool(Tool):

    def __init__(self, perception: PerceptionService):
        self._perception = perception

    @property
    def metadata(self):
        return ToolMetadata(
            name="active_window",
            description="Returns the current foreground window.",
        )

    def execute(self):
        return self._perception.active_window()