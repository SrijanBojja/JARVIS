"""
Conversation confirmation integration test.
"""

from jarvis.actions import Action
from jarvis.actions.engine import ActionEngine
from jarvis.actions.executors.echo import EchoActionExecutor
from jarvis.confirmation.manager import ConfirmationManager


confirmation = ConfirmationManager()

engine = ActionEngine(
    confirmation=confirmation,
)

engine.register(
    EchoActionExecutor(),
)

response = engine.execute(
    Action(
        name="echo",
        target="Hello JARVIS!",
        requires_confirmation=True,
    )
)

print(response.text)

response = engine.execute_pending()

print(response.text)