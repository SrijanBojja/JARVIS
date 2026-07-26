from jarvis.actions.engine import ActionEngine
from jarvis.confirmation.manager import ConfirmationManager


confirmation = ConfirmationManager()

engine = ActionEngine(
    confirmation=confirmation,
)

print(engine.confirmation is confirmation)