import pytest
import requests_mock
from src.api.chat_api import BaseAPI  # Adjust the import path based on your project structure

@pytest.fixture
def base_api():
    """Fixture to create a BaseAPI instance for tests."""
    return BaseAPI()

def test_base_api_initialization():
    """Test BaseAPI initialization with default base URL."""
    api = BaseAPI()
    assert api.base_url == "https://4158-161-28-242-155.ngrok-free.app/v1"

def test_base_api_get_success(base_api):
    """Test successful GET request."""
    with requests_mock.Mocker() as m:
        m.get(f"{base_api.base_url}/test", json={"success": True}, status_code=200)
        response = base_api._get("test")
        assert response == {"success": True}

def test_base_api_post_error(base_api):
    """Test handling of a POST request resulting in a 400 error."""
    with requests_mock.Mocker() as m:
        m.post(f"{base_api.base_url}/test", status_code=400)
        response = base_api._post("test", data={"key": "value"})
        assert response is None


def test_base_api_get_failure(base_api):
    """Test handling of a failed GET request."""
    with requests_mock.Mocker() as m:
        m.get(f"{base_api.base_url}/test", status_code=404)
        response = base_api._get("test")
        assert response is None

def test_base_api_post_success(base_api):
    """Test successful POST request."""
    with requests_mock.Mocker() as m:
        m.post(f"{base_api.base_url}/test", json={"success": True}, status_code=200)
        response = base_api._post("test", data={"key": "value"})
        assert response == {"success": True}

def test_base_api_put_success(base_api):
    """Test successful PUT request."""
    with requests_mock.Mocker() as m:
        m.put(f"{base_api.base_url}/test", json={"success": True}, status_code=200)
        response = base_api._put("test", data={"key": "value"})
        assert response == {"success": True}

def test_base_api_delete_success(base_api):
    """Test successful DELETE request."""
    with requests_mock.Mocker() as m:
        m.delete(f"{base_api.base_url}/test", status_code=204)
        response = base_api._delete("test")
        assert response is None