FROM ubuntu:latest

# Set proxy environment variables if necessary
ENV HTTP_PROXY http://rb-proxy-de.bosch.com:8080
ENV HTTPS_PROXY http://rb-proxy-de.bosch.com:8080

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    python \
    python-pip \
    firefox

# Set the working directory
WORKDIR /python-test-calculator

# Copy the project files to the working directory
COPY . /python-test-calculator

# Install the required packages
RUN pip3 install -r requirements.txt

# Run pytest
CMD ["pytest"]
