# Integration tests for overall workflows
import pytest
from app.services.api_client import DeviceAPIClient
from app.data.mock_data import HEMOSTASIS_MOCK_DATA, POCT_MOCK_DATA

# Mock the API client using pytest-mock
def test_hemostasis_api_integration(mocker):
    mocker.patch('app.services.api_client.DeviceAPIClient.fetch_hemostasis_data', return_value=HEMOSTASIS_MOCK_DATA)
    
    client = DeviceAPIClient(base_url="https://mockserver.com")
    response = client.fetch_hemostasis_data()

    assert response["device"] == "ACL TOP Family"
    assert response["status"] == "completed"
    assert response["tests"][0]["name"] == "D-Dimer"
    assert response["tests"][0]["result"] == 0.45

def test_point_of_care_api_integration(mocker):
    mocker.patch('app.services.api_client.DeviceAPIClient.fetch_point_of_care_data', return_value=POCT_MOCK_DATA)
    
    client = DeviceAPIClient(base_url="https://mockserver.com")
    response = client.fetch_point_of_care_data()

    assert response["device"] == "GEM Premier 5000"
    assert response["status"] == "completed"
    assert response["tests"][0]["name"] == "Blood Gas"
    assert response["tests"][0]["result"] == 7.4
