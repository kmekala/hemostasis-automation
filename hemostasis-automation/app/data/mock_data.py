# Mocked data for testing
# Mock data for Hemostasis and Point-of-Care devices

HEMOSTASIS_MOCK_DATA = {
    "device": "ACL TOP Family",
    "tests": [
        {"name": "D-Dimer", "result": 0.45},
        {"name": "Fibrinogen", "result": 2.8},
        {"name": "PT/INR", "result": 1.0}
    ],
    "status": "completed"
}

POCT_MOCK_DATA = {
    "device": "GEM Premier 5000",
    "tests": [
        {"name": "Blood Gas", "result": 7.4},
        {"name": "Lactate", "result": 1.9}
    ],
    "status": "completed"
}
