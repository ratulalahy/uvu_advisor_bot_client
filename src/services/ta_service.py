from typing import Optional

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.conversation import Conversation, Message
from api.chat_api import ChatCompletionAPI  

class TAService:
    def __init__(self, chat_api: ChatCompletionAPI):
        """
        Initializes the TA Service with a reference to a ChatCompletionAPI instance.

        Args:
            chat_api (ChatCompletionAPI): An instance of the ChatCompletionAPI for making chat completion requests.
        """
        self.chat_api = chat_api
        
    def general_query(self, query: str) -> str:
        response = self.chat_api.post_completions([{"content": query}], stream=False)
        if response and 'choices' in response and len(response['choices']) > 0:
            return response['choices'][0]['message']['content']
        else:
            return "I'm sorry, I couldn't find an answer to your question."        