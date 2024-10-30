# Diagnostics Simulation

This repository simulates an API client for Werfen's diagnostic devices, including Hemostasis and Point of Care testing devices. The simulation leverages mocking techniques to mimic the behavior of Werfen's endpoints using mock data.

## Project Structure

```
├── Dockerfile                   # Docker setup for the project
├── README.md                    # Project documentation
├── app                          # Application source code
│   ├── __init__.py              # App initialization
│   ├── data                     # Mock data for testing
│   │   ├── __init__.py
│   │   └── mock_data.py         # Mock data for API responses
│   ├── devices                  # Logic for different Werfen devices
│   │   ├── __init__.py
│   │   ├── hemostasis.py        # Hemostasis device simulation
│   │   └── point_of_care.py     # Point-of-care device simulation
│   └── services                 # Service layer for external API interaction
│       ├── __init__.py
│       └── api_client.py        # API client for requesting Werfen's endpoints
├── pytest.ini                   # Pytest configuration file
├── requirements.txt             # Python dependencies
└── tests                        # Unit tests and integration tests
    ├── __init__.py
    ├── conftest.py              # Fixtures for Pytest
    ├── test_hemostasis.py       # Unit tests for Hemostasis device
    ├── test_integration.py      # Integration tests
    └── test_point_of_care.py    # Unit tests for Point-of-Care device
```

# Libraries Used

```
pytest ==7.0.1: Framework for unit testing.
requests ==2.26.0: Library for making HTTP requests.
pytest-mock ==3.6.1: Mocking library integrated with pytest.
allure-pytest ==2.9.45: A plugin to generate allure reports for pytest.
```
# Setup and Installation

```
Prerequisites
Python 3.8+
Docker (optional, for containerized environments)
```

# Install Dependencies
## Clone the repository:

```
git clone https://github.com/your-repository/werfen-simulation.git
cd werfen-simulation
```
# Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

# Install the required dependencies:
```
pip install -r requirements.txt
```

# Running Tests
To execute all tests, run:
```
pytest
```

# To generate an Allure report, run:

```
pytest --alluredir=allure-results
```

# Then generate the report:
```
allure serve allure-results
```

# Docker Setup
## Build the Docker image:
```
docker build -t werfen-simulation .
```
## Run the Docker container:
```
docker run --rm -p 8080:8080 werfen-simulatio
```
## Application Overview
```
app/devices/hemostasis.py
This module simulates the behavior of Werfen's Hemostasis diagnostic system. It includes functions that mock interactions with the Hemostasis testing devices.

app/devices/point_of_care.py
This module simulates Point of Care testing devices, providing mock data and functionality similar to Werfen's point-of-care systems.

app/services/api_client.py
This is the API client that interacts with Werfen's endpoints. In this simulation, requests are mocked to return predefined data from the data/mock_data.py file.
```


# Testing
## Unit Tests
```
Unit tests for Hemostasis devices are found in tests/test_hemostasis.py.
Unit tests for Point of Care devices are located in tests/test_point_of_care.py.
```
## Integration Tests
```
Integration tests that simulate the interaction between the API client and mock data are in tests/test_integration.py.
```

## Mocking
```
The pytest-mock library is used for mocking external API calls during testing.
```

