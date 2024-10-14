# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install any necessary dependencies
RUN pip install requests beautifulsoup4

# Run the script when the container launches
CMD ["python", "./scraper.py"]
