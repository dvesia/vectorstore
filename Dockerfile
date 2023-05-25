# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /semantic-search
WORKDIR /semantic-search

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    python3-dev

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python && \
    ln -s ~/.poetry/bin/poetry /usr/local/bin/

# Add poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy the necessary files to the container
COPY pyproject.toml poetry.lock ./

# Install project dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-dev

# Copy the application source code into the working directory
COPY . .

# Set the entry point
ENTRYPOINT ["python", "main.py"]
