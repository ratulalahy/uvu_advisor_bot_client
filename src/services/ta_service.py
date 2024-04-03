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