# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file first to leverage Docker cache
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install required packages including curl and unzip
RUN apt-get update && \
    apt-get install -y curl unzip && \
    rm -rf /var/lib/apt/lists/*

# Install Terraform
RUN curl -LO https://releases.hashicorp.com/terraform/1.3.0/terraform_1.3.0_linux_amd64.zip && \
    unzip terraform_1.3.0_linux_amd64.zip && \
    mv terraform /usr/local/bin/ && \
    chmod +x /usr/local/bin/terraform && \
    rm terraform_1.3.0_linux_amd64.zip

# Copy the rest of the application files
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Start the application
CMD ["python", "app.py"]
