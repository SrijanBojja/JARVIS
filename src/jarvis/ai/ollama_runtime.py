"""
Ollama runtime for JARVIS.
"""

from __future__ import annotations

from typing import Any

import httpx

from jarvis.ai.exceptions import AIRuntimeError
from jarvis.ai.message import Message
from jarvis.ai.models import (
    ChatResponse,
    FinishReason,
    ToolCall,
)
from jarvis.ai.runtime import AIRuntime
from jarvis.config.settings import settings


class OllamaRuntime(AIRuntime):
    """
    Runtime responsible for communicating with Ollama.
    """

    def __init__(
        self,
        host: str | None = None,
        model: str | None = None,
    ) -> None:

        self._host = host or settings.ai_host
        self._model = model or settings.ai_model

    def start(self) -> None:
        """
        Start the runtime.
        """

    def stop(self) -> None:
        """
        Stop the runtime.
        """

    def chat(
        self,
        messages: list[Message],
        tools: list[dict[str, Any]] | None = None,
    ) -> ChatResponse:

        payload: dict[str, Any] = {
            "model": self._model,
            "messages": [
                {
                    key: value
                    for key, value in {
                        "role": message.role,
                        "content": message.content,
                        "name": message.name,
                        "tool_call_id": message.tool_call_id,
                    }.items()
                    if value is not None
                }
                for message in messages
            ],
            "stream": False,
        }

        if tools:
            payload["tools"] = tools

        try:
            response = httpx.post(
                f"{self._host}/api/chat",
                json=payload,
                timeout=120,
            )

            response.raise_for_status()

            return self._parse_response(
                response.json(),
            )

        except Exception as error:
            raise AIRuntimeError(
                f"Failed to communicate with Ollama: {error}"
            ) from error

    @staticmethod
    def _parse_response(
        data: dict[str, Any],
    ) -> ChatResponse:

        message = data.get("message", {})

        tool_calls: list[ToolCall] = []

        for index, call in enumerate(
            message.get("tool_calls", [])
        ):
            function = call.get("function", {})

            tool_calls.append(
                ToolCall(
                    id=str(index),
                    name=function.get("name", ""),
                    arguments=function.get(
                        "arguments",
                        {},
                    ),
                )
            )

        finish_reason = FinishReason(
            data.get(
                "done_reason",
                "stop",
            )
        )

        return ChatResponse(
            text=message.get(
                "content",
                "",
            ),
            tool_calls=tool_calls,
            finish_reason=finish_reason,
        )