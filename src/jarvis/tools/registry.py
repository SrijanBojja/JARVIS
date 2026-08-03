from __future__ import annotations

from typing import Dict

from .exceptions import (
    ToolAlreadyRegistered,
    ToolNotFound,
)
from .tool import Tool


class ToolRegistry:
    """
    Stores every callable tool.
    """

    def __init__(self) -> None:
        self._tools: Dict[str, Tool] = {}

    def register(
        self,
        tool: Tool,
    ) -> None:

        name = tool.metadata.name

        if name in self._tools:
            raise ToolAlreadyRegistered(name)

        self._tools[name] = tool

    def get(
        self,
        name: str,
    ) -> Tool:

        if name not in self._tools:
            raise ToolNotFound(name)

        return self._tools[name]

    def execute(
        self,
        name: str,
        **kwargs,
    ):

        tool = self.get(name)

        return tool.execute(**kwargs)

    def names(self):

        return sorted(self._tools.keys())

    def all(self):

        return tuple(self._tools.values())