# Use a lightweight Python image to keep the container small
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy all project files from the host into the container
COPY . /app

# Run the Python integrity checker script automatically when the container starts
CMD ["python", "checker.py"]
