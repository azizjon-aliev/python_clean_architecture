from django.db import models


class Role(models.TextChoices):
    ADMIN = "ADMIN", "Админ"
    CLIENT = "CLIENT", "Клиент"
    STAFF = "STAFF", "Сотрудник"
