# unit and functional tests for Point-of-Care
import pytest
from app.devices.point_of_care import PointOfCareDevice
from app.data.mock_data import POCT_MOCK_DATA

def test_point_of_care_results():
    device = PointOfCareDevice(device_id="GEM_5000_001")
    results = device.get_test_results()

    assert results["device"] == "GEM Premier 5000"
    assert results["tests"]["Blood Gas"] == "7.4"
    assert results["status"] == "completed"

def test_device_calibration():
    device = PointOfCareDevice(device_id="GEM_5000_002")
    calibration_result = device.run_calibration()

    assert calibration_result == "calibration successful"