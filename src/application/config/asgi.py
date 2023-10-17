"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from dotenv import load_dotenv

from django.core.asgi import get_asgi_application

load_dotenv()
settings_module = f"src.application.config.settings.{os.getenv('DJANGO_ENV')}"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_asgi_application()
