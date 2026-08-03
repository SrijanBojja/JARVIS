from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ToolResult:
    tool: str
    success: bool
    data: Any = None
    message: str = ""