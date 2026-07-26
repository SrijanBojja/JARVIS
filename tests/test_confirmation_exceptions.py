from jarvis.confirmation.exceptions import (
    ActionExpiredError,
    NoPendingActionError,
)

try:
    raise NoPendingActionError(
        "No pending action."
    )
except NoPendingActionError as error:
    print(error)

try:
    raise ActionExpiredError(
        "Action expired."
    )
except ActionExpiredError as error:
    print(error)