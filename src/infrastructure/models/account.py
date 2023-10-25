from django.contrib.auth.models import AbstractUser
from django.db import models
from src.infrastructure.constaints import Role
from src.infrastructure.managers import UserManager
from src.infrastructure.models.base import Auditable, Timestampble


class User(AbstractUser, Timestampble, Auditable):
    username = None
    first_name = None
    last_name = None

    base_role = Role.STAFF
    role = models.CharField(verbose_name="Роль", max_length=50, choices=Role.choices)
    email = models.EmailField(
        verbose_name="Email",
        blank=True,
        unique=True,
        null=True,
        max_length=200,
    )
    phone = models.CharField(
        max_length=15,
        unique=True,
        verbose_name="Телефон",
        blank=False,
        help_text="Введите с 992 и 9-значный номер телефона",
    )
    otp = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)
