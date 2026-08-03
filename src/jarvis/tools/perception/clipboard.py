from jarvis.services.perception import PerceptionService
from jarvis.tools import Tool, ToolMetadata


class ClipboardTool(Tool):

    def __init__(self, perception: PerceptionService):
        self._perception = perception

    @property
    def metadata(self):
        return ToolMetadata(
            name="clipboard",
            description="Returns clipboard contents.",
        )

    def execute(self):
        return self._perception.clipboard()