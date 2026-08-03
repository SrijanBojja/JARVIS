"""
AI service for JARVIS.
"""

from __future__ import annotations

from typing import Any

from jarvis.ai.memory import ConversationMemory
from jarvis.ai.message import Message
from jarvis.ai.models import ChatResponse
from jarvis.ai.prompts import SYSTEM_PROMPT
from jarvis.ai.provider import AIProvider
from jarvis.tools import ToolRegistry


class AIService:
    """
    High-level AI service.
    """

    def __init__(
        self,
        provider: AIProvider,
        memory: ConversationMemory,
        tool_registry: ToolRegistry,
    ) -> None:

        self._provider = provider
        self._memory = memory
        self._tools = tool_registry

    @property
    def provider(
        self,
    ) -> AIProvider:
        return self._provider

    def add_tool_message(
        self,
        tool_name: str,
        content: str,
        tool_call_id: str | None = None,
    ) -> None:

        self._memory.add_tool_message(
            tool_name=tool_name,
            content=content,
            tool_call_id=tool_call_id,
        )

    def chat(
        self,
        message: str,
    ) -> ChatResponse:

        if message:
            self._memory.add_user_message(
                message,
            )

        while True:

            messages = [
                Message(
                    role="system",
                    content=SYSTEM_PROMPT,
                ),
                *self._memory.messages(),
            ]

            response = self._provider.chat(
                messages=messages,
                tools=self._build_tool_schema(),
            )

            if response.text:
                self._memory.add_assistant_message(
                    response.text,
                )

            #
            # Finished.
            #

            if not response.tool_calls:
                return response

            #
            # Execute every requested tool.
            #

            for tool_call in response.tool_calls:

                result = self._tools.execute(
                    tool_call.name,
                    **tool_call.arguments,
                )

                self.add_tool_message(
                    tool_name=tool_call.name,
                    tool_call_id=tool_call.id,
                    content=str(result),
                )

    def _build_tool_schema(
        self,
    ) -> list[dict[str, Any]]:

        schema = []

        for tool in self._tools.all():

            schema.append(
                {
                    "type": "function",
                    "function": {
                        "name": tool.metadata.name,
                        "description": tool.metadata.description,
                        "parameters": {
                            "type": "object",
                            "properties": {},
                        },
                    },
                }
            )

        return schema