Create a file called `Dockerfile` in the same directory as the script.

Add the following lines to the `Dockerfile` to specify the base image and install the required dependencies:

```python
FROM python:3

RUN pip install requests beautifulsoup4
```

Add the following line to the Dockerfile to copy the script to the container:
```python
COPY search_scraper.py /app/search_scraper.py
```

Add the following line to the Dockerfile to set the working directory to the app directory:
```python
WORKDIR /app
```

Add the following line to the Dockerfile to run the script when the container starts:
```python
CMD ["python", "search_scraper.py"]
```

Build the Docker image using the following command:
```python
docker build -t search-scraper .
```
This will create a Docker image with the name "search-scraper".

Run the image in a container using the following command:
```python
docker run -it search-scraper
```
This will start a new container from the "search-scraper" image and run the script inside it.

To save the search results to a CSV file, you can modify the script to write the results to a file using the csv module. Here is an example of how to do this:

```python
import csv

# Open the file in write mode
with open('results.csv', 'w', newline='') as csvfile:
  # Create a CSV writer object
  writer = csv.DictWriter(csvfile, fieldnames=['title', 'link'])

  # Write the header row
  writer.writeheader()

  # Write the search results to the file
  for result in search_results:
    writer.writerow(result)
```
This will write the search results to a file called "results.csv" in the same directory as the script.