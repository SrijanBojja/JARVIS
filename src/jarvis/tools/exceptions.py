class ToolError(Exception):
    """Base Tool exception."""


class ToolAlreadyRegistered(ToolError):
    """Tool already exists."""


class ToolNotFound(ToolError):
    """Requested tool does not exist."""