from django.db import models


class PermalinkMixin(models.Model):
    """
    Mixin to add a unique slug field for permalink.
    """

    slug: models.SlugField = models.SlugField(
        unique=True, db_index=True, help_text="Unique identifier for permalink."
    )

    class Meta:
        abstract = True


class PublishableMixin(models.Model):
    """
    Mixin to add a publishing date to a model.
    """

    publish_date: models.DateTimeField = models.DateTimeField(
        null=True, blank=True, help_text="Date and time when the item was published."
    )

    class Meta:
        abstract = True


class TimestampMixin(models.Model):
    """
    Mixin to add timestamp fields for creation and last update.
    """

    created_at: models.DateTimeField = models.DateTimeField(
        verbose_name="Time of creation",
        auto_now_add=True,
        help_text="Timestamp when the object was created.",
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        verbose_name="Time of change",
        auto_now=True,
        help_text="Timestamp when the object was last updated.",
    )

    class Meta:
        abstract = True


class AuditableMixin(models.Model):
    """
    Mixin to add auditing fields for tracking creation and updates by users.
    """

    created_by: models.ForeignKey = models.ForeignKey(
        "infrastructure.User",
        verbose_name="Who created",
        on_delete=models.SET_NULL,
        related_name="%(class)s_created_by",
        blank=True,
        null=True,
        help_text="User who created the object.",
    )
    updated_by: models.ForeignKey = models.ForeignKey(
        "infrastructure.User",
        verbose_name="Who updated",
        on_delete=models.SET_NULL,
        related_name="%(class)s_updated_by",
        blank=True,
        null=True,
        help_text="User who last updated the object.",
    )

    class Meta:
        abstract = True
