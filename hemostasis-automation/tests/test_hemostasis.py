# Unit and functional tests for Hemostasis
import pytest
from app.devices.hemostasis import HemostasisDevice
from app.data.mock_data import HEMOSTASIS_MOCK_DATA

def test_hemostasis_device_results():
    device = HemostasisDevice(device_id="ACL_TOP_001")
    results = device.get_test_results()

    assert results["device"] == "ACL TOP Family"
    assert results["tests"]["D-Dimer"] == 0.35
    assert results["status"] == "completed"

def test_sample_integrity_check():
    device = HemostasisDevice(device_id="ACL_TOP_002")
    assert device.check_sample_integrity() == True