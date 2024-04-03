import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from api.base_api import BaseAPI


class UtilAPI(BaseAPI):
    def get_embeddings(self, input_text):
        """Post data to the embeddings endpoint."""
        endpoint = "embeddings"
        payload = {"input": input_text}
        return self._post(endpoint, data=payload)

    def check_health(self):
        """Get the health status of the API."""
        endpoint = "health"
        return self._get(endpoint)
    
    def post_chunks(self, text):
        """Post chunks of text."""
        endpoint = "chunks"
        payload = {"text": text}
        return self._post(endpoint, data=payload)