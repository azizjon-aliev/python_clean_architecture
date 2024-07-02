FROM python:3.12-slim

# environment variables
ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
    PROJECT_DIR="/code" \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry:
    POETRY_VERSION=1.3.2 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

# system dependencies
RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends --no-install-suggests -y \
    build-essential \
    libpq-dev \
    # Cleaning cache:
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
    # Installing `poetry` package manager:
    && pip install poetry==$POETRY_VERSION && poetry --version

# set working directory
WORKDIR $PROJECT_DIR

# copy dependencies only
COPY ./pyproject.toml ./poetry.lock ${PROJECT_DIR}/

# Project initialization:
RUN poetry install $(test "$DJANGO_ENV" = production && echo "--no-dev") --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code

# copy script as an entry point:
COPY ./scripts ${PROJECT_DIR}/scripts/

COPY ./manage.py ./.env ${PROJECT_DIR}/

# Setting up proper permissions:
RUN chmod +x ${PROJECT_DIR}/scripts/start_api.sh \
  && mkdir -p /${PROJECT_DIR}/media /${PROJECT_DIR}/static \
  && chmod +x /${PROJECT_DIR}/media/ /${PROJECT_DIR}/static/

# expose port
EXPOSE $PORT