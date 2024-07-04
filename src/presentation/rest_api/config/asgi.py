import os

from dotenv import load_dotenv

from django.core.asgi import get_asgi_application

load_dotenv()
settings_module = f"src.presentation.rest_api.config.settings.{os.getenv('DJANGO_ENV')}"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_asgi_application()
