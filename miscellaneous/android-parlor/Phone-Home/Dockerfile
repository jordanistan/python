FROM python:3.13.0a3-slim

# Install the necessary libraries
RUN pip install requests beautifulsoup4 paramiko

# Copy the Python script into the Docker container
COPY ph.py /app/ph.py

# Set the default command to run the Python script
# CMD ["python", "/app/find_macbooks.py"]
CMD ["python", "/app/ph.py"]