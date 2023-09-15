# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY main.py /app/main.py
COPY data /app/data

# Install the required Python packages
RUN pip install -r requirements.txt

# Expose the port that the FastAPI application will run on
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
