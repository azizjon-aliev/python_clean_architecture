from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.infrastructure.constaints import Role
from src.infrastructure.managers import UserManager
from src.infrastructure.models.base import AuditableMixin, TimestampMixin


class User(AbstractUser, TimestampMixin, AuditableMixin):
    """
    Custom User model extending Django's AbstractUser
    with additional fields and functionality.

    This model replaces the default username with a phone number for authentication.
    It includes roles, email, phone verification, and OTP management.
    """

    # Removing default fields from AbstractUser
    username = None
    first_name = None
    last_name = None

    # Constants
    BASE_ROLE = Role.STAFF

    # Fields
    role = models.CharField(
        _("Role"),
        max_length=50,
        choices=Role.choices,
        default=BASE_ROLE,
        help_text=_("User role within the application."),
    )
    email = models.EmailField(
        _("Email"),
        blank=True,
        unique=True,
        null=True,
        max_length=200,
        help_text=_("Unique email address for the user."),
    )
    phone = models.CharField(
        _("Phone"),
        max_length=15,
        unique=True,
        help_text=_(
            "Enter a phone number starting with 992 followed by a 9-digit number."
        ),
    )
    otp = models.PositiveIntegerField(
        _("OTP"),
        default=0,
        help_text=_("One-Time Password for user verification."),
    )
    is_verified = models.BooleanField(
        _("Is Verified"),
        default=False,
        help_text=_("Indicates whether the user's phone number has been verified."),
    )

    # Authentication settings
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    # Managers
    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.phone} - {self.email or 'No Email'}"

    def save(self, *args, **kwargs) -> None:
        """
        Override the save method to set the default role upon creation.
        """
        if not self.pk:
            self.role = self.BASE_ROLE
        super().save(*args, **kwargs)
