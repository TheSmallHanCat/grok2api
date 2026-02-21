"""
Response formatting utilities for OpenAI-compatible API responses.
"""

import os
import time
import uuid
from typing import Optional


def make_response_id() -> str:
    """Generate a unique response ID."""
    return f"chatcmpl-{int(time.time() * 1000)}{os.urandom(4).hex()}"


def make_chat_chunk(
    response_id: str,
    model: str,
    content: str,
    index: int = 0,
    role: str = "assistant",
    is_final: bool = False,
) -> dict:
    """
    Create an OpenAI-compatible chat completion chunk.

    Args:
        response_id: Unique response ID
        model: Model name
        content: Content to send
        index: Choice index
        role: Role (assistant)
        is_final: Whether this is the final chunk (includes finish_reason)

    Returns:
        Chat completion chunk dict
    """
    choice: dict = {
        "index": index,
        "delta": {
            "role": role,
            "content": content,
        },
    }

    if is_final:
        choice["finish_reason"] = "stop"

    chunk: dict = {
        "id": response_id,
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": model,
        "choices": [choice],
    }

    if is_final:
        chunk["usage"] = {
            "total_tokens": 0,
            "input_tokens": 0,
            "output_tokens": 0,
            "input_tokens_details": {"text_tokens": 0, "image_tokens": 0},
        }

    return chunk


def make_chat_response(
    model: str,
    content: str,
    response_id: Optional[str] = None,
    index: int = 0,
    usage: Optional[dict] = None,
) -> dict:
    """
    Create an OpenAI-compatible non-streaming chat completion response.

    Args:
        model: Model name
        content: Response content
        response_id: Unique response ID (generated if not provided)
        index: Choice index
        usage: Custom usage dict (defaults to zeros)

    Returns:
        Chat completion response dict
    """
    if response_id is None:
        response_id = f"chatcmpl-{uuid.uuid4().hex[:8]}"

    if usage is None:
        usage = {
            "total_tokens": 0,
            "input_tokens": 0,
            "output_tokens": 0,
            "input_tokens_details": {"text_tokens": 0, "image_tokens": 0},
        }

    return {
        "id": response_id,
        "object": "chat.completion",
        "created": int(time.time()),
        "model": model,
        "choices": [
            {
                "index": index,
                "message": {
                    "role": "assistant",
                    "content": content,
                    "refusal": None,
                },
                "finish_reason": "stop",
            }
        ],
        "usage": usage,
    }


def wrap_image_content(content: str, response_format: str = "url") -> str:
    """
    Wrap image content in markdown format for chat interface.

    Args:
        content: Image URL or base64 data
        response_format: "url" or "b64_json"/"base64"

    Returns:
        Markdown-wrapped image content
    """
    if not content:
        return content

    if response_format == "url":
        return f"![image]({content})"
    else:
        return f"![image](data:image/png;base64,{content})"


__all__ = [
    "make_response_id",
    "make_chat_chunk",
    "make_chat_response",
    "wrap_image_content",
]
