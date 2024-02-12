import requests

class BaseAPI:
    def __init__(self, base_url="https://4158-161-28-242-155.ngrok-free.app/v1"):
        self.base_url = base_url
        self.headers = {"Accept": "application/json"}  # Removed "Content-Type" for flexibility

    def _post(self, endpoint, data=None, files=None):
        url = f"{self.base_url}/{endpoint}"
        headers = self.headers
        if files:
            # For file uploads, do not include JSON data and let requests handle content-type
            response = requests.post(url, files=files, headers=headers)
        else:
            # For JSON data, specify json parameter
            response = requests.post(url, json=data, headers=headers)
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e.response.status_code} {e.response.text}")
        except Exception as e:
            print(f"Unexpected Error: {str(e)}")
        return None

    def _get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    

class ChatCompletionAPI(BaseAPI):
    def __init__(self, base_url="https://4158-161-28-242-155.ngrok-free.app/v1"):
        super().__init__(base_url)
        self.conversation_history = []
    
    def post_completions(self, messages, role = None, stream=True):
        """
        Post messages to the chat completions endpoint.
        
        :param messages: A list of message dictionaries with "content" and "role" keys.
        :param stream: Boolean to enable or disable streaming.
        """
        endpoint = "completions"
        if role:
            payload = {"prompt": messages, "role": role, "stream": stream}
        else:
            payload = {"prompt": messages, "stream": stream}
        response = self._post(endpoint, payload)
        return response

    def post_chat_completions(self, message, role = 'user', is_init = False, stream=False):
        endpoint = "chat/completions"
        if is_init:
            self.conversation_history = []  # Clear existing conversation history
            self.conversation_history.append({"content": message, "role": role})
            return

        # Add the new message with its role to the conversation history
        self.conversation_history.append({"content": message, "role": role})

        payload = {
            "messages": self.conversation_history#,
            #"stream": stream
        }
        response = self._post(endpoint, payload)  # And here
        return response
