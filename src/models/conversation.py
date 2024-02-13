from typing import List, Dict, Optional
from datetime import datetime, timezone

class Message:
    def __init__(self, content: str, sender: str, timestamp: Optional[datetime] = None):
        """
        Initialize a new message.

        Args:
            content (str): The text content of the message.
            sender (str): Identifier for who sent the message (e.g., "user", "system", "assistant").
            timestamp (datetime, optional): The timestamp when the message was created. Defaults to the current time.
        """
        self.content = content
        self.sender = sender
        self.timestamp = timestamp if timestamp else datetime.now(timezone.utc)

    def to_dict(self) -> Dict[str, any]:
        """
        Convert the message to a dictionary format, suitable for serialization or storage.

        Returns:
            Dict[str, any]: The message as a dictionary.
        """
        return {
            "content": self.content,
            "sender": self.sender,
            "timestamp": self.timestamp.isoformat()
        }

class Conversation:
    def __init__(self):
        """
        Initialize a new conversation with an empty history and default context.
        """
        self.history: List[Message] = []
        self.context: Dict[str, any] = {}

    def add_message(self, message: Message):
        """
        Add a new message to the conversation history.

        Args:
            message (Message): The message to add.
        """
        self.history.append(message)

    def get_history(self) -> List[Dict[str, any]]:
        """
        Retrieve the conversation history.

        Returns:
            List[Dict[str, any]]: The conversation history as a list of dictionaries.
        """
        return [message.to_dict() for message in self.history]

    def set_context(self, key: str, value: any):
        """
        Set a value in the conversation's context.

        Args:
            key (str): The key in the context to set.
            value (any): The value to set for the given key.
        """
        self.context[key] = value

    def get_context(self, key: str) -> any:
        """
        Retrieve a value from the conversation's context by key.

        Args:
            key (str): The key to retrieve from the context.

        Returns:
            any: The value associated with the key in the context, or None if the key does not exist.
        """
        return self.context.get(key, None)

# Example Usage
if __name__ == "__main__":
    conversation = Conversation()
    conversation.add_message(Message("Hi, how can I help you?", "system"))
    conversation.add_message(Message("What is the prerequisite for CS 2450?", "user"))
    print(conversation.get_history())
    conversation.set_context("current_course", "CS 2450")
    print(conversation.get_context("current_course"))
