import os

from .base import *  # noqa: F403

DEBUG = False

# CORS
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(",")
CSRF_TRUSTED_ORIGINS = os.getenv("DJANGO_CORS_ALLOWED_ORIGINS").split(",")

CORS_ALLOWED_ORIGINS = os.getenv("DJANGO_CORS_ALLOWED_ORIGINS").split(",")

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)

# DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}
