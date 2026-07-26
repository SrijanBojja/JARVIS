from jarvis.confirmation.manager import ConfirmationManager
from jarvis.confirmation.exceptions import NoPendingActionError


manager = ConfirmationManager()

try:
    manager.confirm()
except NoPendingActionError as error:
    print(error)

try:
    manager.cancel()
except NoPendingActionError as error:
    print(error)

try:
    manager.is_expired()
except NoPendingActionError as error:
    print(error)