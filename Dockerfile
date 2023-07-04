# Use a base Python image
FROM python:3.11.1

# Set the working directory
WORKDIR /python-test-calculator

# Copy the project files to the working directory
COPY . /python-test-calculator

# Set proxy environment variables if necessary
ENV HTTP_PROXY http://rb-proxy-de.bosch.com:8080
ENV HTTPS_PROXY http://rb-proxy-de.bosch.com:8080

# Install the necessary dependencies
RUN pip install --upgrade pip setuptools
RUN pip install pexpect
RUN pip install -r requirements.txt

# Set the environment variables for Selenium
ENV SELENIUM_HOST selenium-hub
ENV SELENIUM_PORT 4444

# Run PyTest
CMD ["pytest"]
