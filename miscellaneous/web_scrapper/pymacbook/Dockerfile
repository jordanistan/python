FROM python:3.13-slim

# Install the necessary libraries
RUN pip install requests beautifulsoup4

# Copy the Python script into the Docker container
# COPY find_macbooks.py /app/find_macbooks.py
COPY craigslist_macbook_notifier.py /app/craigslist_macbook_notifier.py

# Set the default command to run the Python script
# CMD ["python", "/app/find_macbooks.py"]
CMD ["python", "/app/craigslist_macbook_notifier.py"]