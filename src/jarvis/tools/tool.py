from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(slots=True, frozen=True)
class ToolMetadata:
    name: str
    description: str


class Tool(ABC):
    """
    Base class for every AI callable tool.
    """

    @property
    @abstractmethod
    def metadata(self) -> ToolMetadata:
        ...

    @abstractmethod
    def execute(
        self,
        **kwargs: Any,
    ) -> Any:
        ...