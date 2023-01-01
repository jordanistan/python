# Use the official Python image as the base image
FROM python:3

# Install the requests and beautifulsoup4 libraries
RUN pip install requests beautifulsoup4

# Copy the search_items.py script to the Docker image
COPY search_items.py /app/search_items.py

# Set the working directory to the app directory
WORKDIR /app

# Run the search_items.py script when the Docker container starts
CMD ["python", "search_items.py"]
