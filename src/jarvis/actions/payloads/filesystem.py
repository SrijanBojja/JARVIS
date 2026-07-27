from dataclasses import dataclass

from .base import ActionPayload


@dataclass(frozen=True, slots=True)
class ReadFilePayload(ActionPayload):
    path: str


@dataclass(frozen=True, slots=True)
class WriteFilePayload(ActionPayload):
    path: str
    content: str


@dataclass(frozen=True, slots=True)
class DeleteFilePayload(ActionPayload):
    path: str


@dataclass(frozen=True, slots=True)
class CreateDirectoryPayload(ActionPayload):
    path: str


@dataclass(frozen=True, slots=True)
class DeleteDirectoryPayload(ActionPayload):
    path: str


@dataclass(frozen=True, slots=True)
class ListDirectoryPayload(ActionPayload):
    path: str


@dataclass(frozen=True, slots=True)
class MoveFilePayload(ActionPayload):
    source: str
    destination: str