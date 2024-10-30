#  Pytest configuration and fixtures
import pytest

@pytest.fixture
def api_client():
    from app.services.api_client import DeviceAPIClient
    return DeviceAPIClient(base_url="https://mockserver.com")

