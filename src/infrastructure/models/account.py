from django.contrib.auth.models import AbstractUser
from django.db import models
from src.infrastructure.managers import UserManager
from src.infrastructure.models.base import Auditable, Timestampble


class User(AbstractUser, Timestampble, Auditable):
    otp = models.IntegerField(default=0)
    otp_expire_time = models.DateTimeField(
        verbose_name="Otp expiry time",
        blank=True,
        null=True,
    )

    is_verified = models.BooleanField(default=False)

    REQUIRED_FIELDS = []

    objects = UserManager()
