# Base Python image 
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Install necessary system packages for dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    libssl-dev \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy `requirements.txt` to install dependencies
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Define the port the application runs on
EXPOSE 8000

# Environment variables for production environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_ENV=production \
    MONGO_URI=mongodb://mongo:27017/mydatabase

# Command to start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

