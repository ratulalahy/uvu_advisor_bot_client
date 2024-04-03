from enum import Enum, auto
from typing import List, Dict, Optional, Any

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from api.base_api import BaseAPI


class Role(Enum):
    USER = auto()
    SYSTEM = auto()
    ASSISTANT = auto()

    def __str__(self):
        return self.name.lower()

class ChatCompletionAPI(BaseAPI):
    """
    A specialized API client for handling chat completions with conversation history management,
    utilizing an enum for role management.
    """

    def __init__(self, base_url: str = "http://localhost:8001/v1"):
        super().__init__(base_url)
        self.conversation_history: List[Dict[str, Any]] = []


    def post_completions(self, messages: List[Dict[str, Any]], role: Optional[Role] = None, stream: bool = True, context_filter: Optional[str] = None, use_context: bool = True, include_source: bool = False) -> Optional[Dict[str, Any]]:
        """
        Post messages to the chat completions endpoint with optional parameters for role, streaming, and context configuration.

        Args:
            messages: A list of message dictionaries with "content" and optionally "role" keys.
            role: An optional role for all messages, overriding individual message roles if provided. Defaults to None.
            stream: Whether to enable or disable streaming responses. Defaults to True.
            context_filter: Optional filter to apply to the context, affecting which parts are used. Defaults to None.
            use_context: Whether to use the existing context for generating completions. Defaults to True.
            include_source: Whether to include the source information in the response. Defaults to False.

        Returns:
            Optional[Dict[str, Any]]: The JSON response from the API or None in case of an error.
        """
        endpoint = "completions"
        payload = {
            "prompt": messages,
            "stream": stream,
            "context_filter": context_filter,
            "use_context": use_context,
            "include_source": include_source
        }
        
        # Add role to payload if it is specified
        if role is not None:
            payload["role"] = str(role)

        response = self._post(endpoint, payload)
        return response

    def post_chat_completions(self, message: str, role: Role = Role.USER, is_init: bool = False, stream: bool = False) -> Optional[Dict[str, Any]]:
        """
        Post a single message to the chat completions endpoint, managing conversation history.

        Args:
            message: The message content to send.
            role: The role of the message sender, represented as an Enum. Defaults to Role.USER.
            is_init: Whether to initialize (reset) the conversation history. Defaults to False.
            stream: Whether to enable streaming for this message. Defaults to False.

        Returns:
            The JSON response from the API or None in case of an error.
        """
        endpoint = "chat/completions"

        if is_init:
            self.conversation_history = []
            if not message:  # If initializing without a new message, return here.
                return None
            else:
                self.conversation_history.append({"content": message, "role": str(role)})
            return None

        else:
            # Add the new message with its role to the conversation history
            self.conversation_history.append({"content": message, "role": str(role)})

        payload = {
            "messages": self.conversation_history,
            "stream": stream
        }

        response = self._post(endpoint, payload)
        return response
