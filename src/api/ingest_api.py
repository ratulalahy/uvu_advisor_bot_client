import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from api.base_api import BaseAPI


class IngestAPI(BaseAPI):
    def ingest_file(self, file_path):
        """Ingest a file to a specific endpoint."""
        endpoint = "ingest/file"
        with open(file_path, 'rb') as f:
            files = {'file': (file_path.split('/')[-1], f)}
            response = self._post(endpoint, files=files)
        return response

    def ingest_text(self, file_name, text):
        """Ingest text with a file name."""
        endpoint = "ingest/text"
        payload = {"file_name": file_name, "text": text}
        return self._post(endpoint, data=payload)

    def list_ingest_jobs(self):
        """List all ingest jobs."""
        endpoint = "ingest/list"
        return self._get(endpoint)