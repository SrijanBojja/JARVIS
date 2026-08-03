from jarvis.services.perception import PerceptionService
from jarvis.tools import Tool, ToolMetadata


class ListWindowsTool(Tool):

    def __init__(self, perception: PerceptionService):
        self._perception = perception

    @property
    def metadata(self):
        return ToolMetadata(
            name="list_windows",
            description="Returns all visible windows.",
        )

    def execute(self):
        return self._perception.windows()