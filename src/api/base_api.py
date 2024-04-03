import requests
from typing import Optional, Dict, Any, Union

class BaseAPI:
    """BaseAPI serves as a wrapper for basic REST API operations with a given base URL.
    
    Attributes:
        base_url (str): The base URL for the API endpoints.
        headers (Dict[str, str]): Default headers to include in all requests.
    """

    def __init__(self, base_url: str = "http://localhost:8001/v1"):
        """Initialize the BaseAPI with a base URL and default headers.

        Args:
            base_url (str): The base URL for the API endpoints. Defaults to a sample ngrok URL.
        """
        self.base_url: str = base_url
        self.headers: Dict[str, str] = {"Accept": "application/json"}

    def _post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, files: Optional[Dict[str, Any]] = None):# -> Optional[Dict[str, Any]]:
        """Sends a POST request to a specific endpoint.

        Args:
            endpoint (str): The API endpoint to post data to.
            data (Optional[Dict[str, Any]]): JSON data to send in the request. Defaults to None.
            files (Optional[Dict[str, Any]]): Files to upload. Defaults to None.

        Returns:
            Optional[Dict[str, Any]]: The JSON response from the API or None in case of an error.
        """
        url: str = f"{self.base_url}/{endpoint}"
        headers: Dict[str, str] = self.headers
        try:
            if files:
                response = requests.post(url, files=files, headers=headers)
            else:
                response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")
        return None

    def _get(self, endpoint: str) -> Optional[Dict[str, Any]]:
        """Performs a GET request to a specified endpoint.

        Args:
            endpoint (str): The API endpoint to retrieve data from.

        Returns:
            Optional[Dict[str, Any]]: The JSON response from the API or None in case of an error.
        """
        url: str = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")
        return None
