from typing import Optional

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.conversation import Conversation, Message
from api.chat_api import ChatCompletionAPI  

class AdvisorService:
    def __init__(self, chat_api: ChatCompletionAPI):
        """
        Initializes the AdvisorService with a reference to a ChatCompletionAPI instance.

        Args:
            chat_api (ChatCompletionAPI): An instance of the ChatCompletionAPI for making chat completion requests.
        """
        self.chat_api = chat_api

    def handle_query(self, conversation: Conversation, query: str) -> str:
        """
        Process a user query and return a response.

        Args:
            conversation (Conversation): The current conversation context.
            query (str): The user's query.

        Returns:
            str: The response to the user's query.
        """
        # Example: Simple logic to determine the type of query
        # In a real application, this might involve more complex NLP or keyword matching
        if "prerequisite" in query.lower():
            return self.get_course_prerequisite(conversation, query)
        elif "advice" in query.lower():
            return self.get_general_advice(conversation, query)
        else:
            # Fallback to a generic response or use the chat API directly
            return self.get_generic_response(query)

    def get_course_prerequisite(self, conversation: Conversation, query: str) -> str:
        """
        Retrieves course prerequisites based on the query.

        Args:
            conversation (Conversation): The current conversation context.
            query (str): The user's query, expected to contain course information.

        Returns:
            str: A response containing the course prerequisites.
        """
        # Placeholder implementation
        # Here you would implement logic to parse the course from the query
        # and retrieve its prerequisites from a database, API, or predefined data
        return "The prerequisites for CS 2450 are CS 1400 and CS 1410."

    def get_general_advice(self, conversation: Conversation, query: str) -> str:
        """
        Provides general advice based on the query.

        Args:
            conversation (Conversation): The current conversation context.
            query (str): The user's query.

        Returns:
            str: A response containing general advice.
        """
        # Placeholder for actual advice logic
        return "Make sure to consult your academic advisor for personalized advice."

    def get_generic_response(self, query: str) -> str:
        """
        Gets a generic response for the query using the chat API.

        Args:
            query (str): The user's query.

        Returns:
            str: A generic response obtained from the chat API.
        """
        # Directly use the chat API to get a response
        # This is a simplified example; actual implementation should handle errors and edge cases
        response = self.chat_api.post_completions([{"content": query}], stream=False)
        if response and 'choices' in response and len(response['choices']) > 0:
            return response['choices'][0]['message']['content']
        else:
            return "I'm sorry, I couldn't find an answer to your question."

# Example usage
if __name__ == "__main__":
    chat_api = ChatCompletionAPI(base_url='http://localhost:8001/v1')
    advisor_service = AdvisorService(chat_api)
    conversation = Conversation()
    response = advisor_service.handle_query(conversation, "What are the prerequisites for CS 2450?")
    print(response)
