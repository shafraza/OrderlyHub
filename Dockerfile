# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set environment variables for Python to run in unbuffered mode
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        default-libmysqlclient-dev \
        pkg-config \
        libmariadb-dev-compat \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app/
COPY requirements.txt /app/

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
