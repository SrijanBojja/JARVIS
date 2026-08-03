from pathlib import Path

from jarvis.services.perception import PerceptionService
from jarvis.tools import Tool, ToolMetadata


class CaptureScreenTool(Tool):

    def __init__(self, perception: PerceptionService):
        self._perception = perception

    @property
    def metadata(self) -> ToolMetadata:
        return ToolMetadata(
            name="capture_screen",
            description="Capture the current desktop screenshot.",
        )

    def execute(self) -> str:
        path: Path = self._perception.capture_screen()
        return str(path)