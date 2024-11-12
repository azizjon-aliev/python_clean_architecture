# Use the official Python 3.12 slim image as the base
FROM python:3.12-slim-bookworm

# Set environment variables
ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
    PROJECT_DIR="/code" \
    # Python:
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # Pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Install system dependencies
RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends --no-install-suggests -y \
    build-essential \
    libpq-dev \
    curl \
    # Clean up to reduce image size
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set the working directory
WORKDIR $PROJECT_DIR

# Copy the project files
COPY . ${PROJECT_DIR}/

# Install project dependencies using uv
RUN uv sync

# Set execute permissions for the start script
RUN chmod +x ${PROJECT_DIR}/scripts/start_api.sh \
    && mkdir -p ${PROJECT_DIR}/media ${PROJECT_DIR}/static \
    && chmod -R 755 ${PROJECT_DIR}/media ${PROJECT_DIR}/static

# Expose the application port
EXPOSE $PORT

# Define the entry point
CMD ["./scripts/start_api.sh"]
