FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files from the current directory to /app in the container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir flask numpy pandas

# Expose port 80 for the Flask app
EXPOSE 80

# Run app2.py as the entrypoint
CMD ["python", "app1.py"]

