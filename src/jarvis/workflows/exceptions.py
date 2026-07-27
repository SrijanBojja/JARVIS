class WorkflowError(Exception):
    """Base exception for workflow errors."""


class InvalidWorkflowError(WorkflowError):
    """Raised when a workflow definition is invalid."""


class WorkflowExecutionError(WorkflowError):
    """Raised when workflow execution fails."""


class WorkflowCancelledError(WorkflowError):
    """Raised when a workflow is cancelled."""