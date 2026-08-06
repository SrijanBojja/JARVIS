from jarvis.ai import (
    AIService,
    OllamaProvider,
)
from jarvis.ai.memory import ConversationMemory
from jarvis.planner import AIPlanner
from jarvis.tools import ToolRegistry
from jarvis.planner.parser import PlannerParser
from jarvis.planner.validator import PlannerValidator


provider = OllamaProvider()

memory = ConversationMemory()

tool_registry = ToolRegistry()

ai_service = AIService(
    provider,
    memory,
    tool_registry,
)

parser = PlannerParser()

validator = PlannerValidator()

planner = AIPlanner(
    ai_service,
    parser,
    validator,
)

plan = planner.build(
    "Search YouTube",
)

for action in plan.actions:
    print(action)