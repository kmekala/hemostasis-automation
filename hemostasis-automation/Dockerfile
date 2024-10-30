# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Install Java (required for Allure CLI)
RUN apt-get update && apt-get install -y default-jre curl

# Install Allure CLI (try a different version if needed)
RUN curl -o allure.tgz -L https://github.com/allure-framework/allure2/releases/download/2.21.0/allure-2.21.0.tgz && \
    tar -zxvf allure.tgz -C /opt/ && \
    ln -s /opt/allure-2.21.0/bin/allure /usr/bin/allure && \
    rm allure.tgz

# Copy the project files to the container
COPY ./ ./

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install allure-pytest plugin to generate Allure results
RUN pip install allure-pytest

# Ensure the reports directory exists and is writable for test artifacts
RUN mkdir -p reports/test_results reports/allure_results && chmod -R 777 reports

# Expose port 8080 for accessing the Allure report
EXPOSE 8080

# CMD to run tests, generate timestamped Allure results, create HTML reports, and serve them via HTTP using `sh`
CMD sh -c \
    "timestamp=$(date +'%Y%m%d_%H%M%S') && \
    echo 'Running tests and generating allure results...' && \
    pytest --alluredir=reports/allure_results_$timestamp --disable-warnings -v && \
    echo 'Generating Allure report...' && \
    allure generate reports/allure_results_$timestamp -o reports/test_results/allure-report_$timestamp --clean && \
    echo 'Allure report generated at reports/test_results/allure-report_$timestamp' && \
    echo 'Starting HTTP server to serve the Allure report on port 8080...' && \
    cd reports/test_results/allure-report_$timestamp && \
    python3 -m http.server 8080"