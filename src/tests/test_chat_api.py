
import pytest
from src.api.chat_api import ChatCompletionAPI, Role

@pytest.fixture
def chat_api():
    """Fixture to create a ChatCompletionAPI instance for tests."""
    return ChatCompletionAPI()

def test_chat_api_initialization(chat_api):
    """Test ChatCompletionAPI initialization with default settings."""
    assert chat_api.base_url == "https://4158-161-28-242-155.ngrok-free.app/v1"
    assert chat_api.conversation_history == []

def test_post_chat_completions_single_message(chat_api):
    """Test adding a single message to an empty conversation history."""
    chat_api.post_chat_completions("Hello", Role.USER)
    assert len(chat_api.conversation_history) == 1
    assert chat_api.conversation_history[0]["content"] == "Hello"
    assert chat_api.conversation_history[0]["role"] == "user"

def test_post_chat_completions_multiple_messages(chat_api):
    """Test adding multiple messages to the conversation history."""
    chat_api.post_chat_completions("Hello", Role.USER)
    chat_api.post_chat_completions("How are you?", Role.USER)
    chat_api.post_chat_completions("I need some help.", Role.USER)
    assert len(chat_api.conversation_history) == 3
    assert chat_api.conversation_history[0]["content"] == "Hello"
    assert chat_api.conversation_history[1]["content"] == "How are you?"
    assert chat_api.conversation_history[2]["content"] == "I need some help."

def test_post_chat_completions_different_roles(chat_api):
    """Test adding messages with different roles to the conversation history."""
    chat_api.post_chat_completions("Hello", Role.USER)
    chat_api.post_chat_completions("How can I assist you?", Role.ASSISTANT)
    chat_api.post_chat_completions("I'm here to help.", Role.SYSTEM)
    assert len(chat_api.conversation_history) == 3
    assert chat_api.conversation_history[0]["role"] == "user"
    assert chat_api.conversation_history[1]["role"] == "assistant"
    assert chat_api.conversation_history[2]["role"] == "system"

def test_post_chat_completions_init_message(chat_api):
    """Test adding an initialization message to the conversation history."""
    chat_api.post_chat_completions("Initializing chat...", Role.SYSTEM, is_init=True)
    assert len(chat_api.conversation_history) == 1
    assert chat_api.conversation_history[0]["content"] == "Initializing chat..."
    assert chat_api.conversation_history[0]["role"] == "system"


