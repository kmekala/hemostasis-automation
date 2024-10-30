# Core logic for Hemostasis devices
class HemostasisDevice:
    def __init__(self, device_id):
        self.device_id = device_id

    def get_test_results(self):
        # Simulate fetching test results from the device
        return {
            "device": "ACL TOP Family",
            "tests": {
                "D-Dimer": 0.35,
                "Fibrinogen": 3.2,
                "PT/INR": 1.1
            },
            "status": "completed"
        }

    def check_sample_integrity(self):
        # Simulate a sample integrity check
        return True