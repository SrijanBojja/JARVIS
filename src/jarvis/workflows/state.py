from enum import Enum


class WorkflowState(str, Enum):
    """
    Represents the lifecycle state of a workflow.
    """

    CREATED = "created"
    RUNNING = "running"
    WAITING = "waiting"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"