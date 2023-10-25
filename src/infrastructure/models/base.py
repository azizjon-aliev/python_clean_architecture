from django.db import models


class Permalinkable(models.Model):
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        abstract = True


class Publishable(models.Model):
    publish_date = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class Timestampble(models.Model):
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Время изменения", auto_now=True)

    class Meta:
        abstract = True


class Auditable(models.Model):
    created_by = models.ForeignKey(
        "infrastructure.User",
        verbose_name="Кто создал",
        on_delete=models.SET_NULL,
        related_name="%(class)s_created_by",
        blank=True,
        null=True,
    )
    updated_by = models.ForeignKey(
        "infrastructure.User",
        verbose_name="Кто изменил",
        on_delete=models.SET_NULL,
        related_name="%(class)s_updated_by",
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
