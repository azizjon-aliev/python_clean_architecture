from django.contrib.auth.models import AbstractUser
from src.infrastructure.managers import UserManager
from src.infrastructure.models.base import Auditable, Timestampble


class User(AbstractUser, Timestampble, Auditable):
    objects = UserManager()
