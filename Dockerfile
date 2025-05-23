# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /api

# Copy the application code into the container
COPY /api /api

# Install Python dependencies
RUN pip install -r /api/requirements.txt

# Set environment variables
ENV DB_USER=?
ENV DB_PASSWORD=?
ENV DB_HOST=?
ENV DB_PORT=?
ENV DB_NAME=?

# Run the application
CMD ["python", "/api/app.py"]