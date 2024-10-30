# API client for making requests to mocked server
import requests

class DeviceAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_hemostasis_data(self):
        response = requests.get(f"{self.base_url}/hemostasis")
        return response.json()

    def fetch_point_of_care_data(self):
        response = requests.get(f"{self.base_url}/point-of-care")
        return response.json()