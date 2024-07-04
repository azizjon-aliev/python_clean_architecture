from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from src.infrastructure.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Административная панель для модели User.

    Здесь можно настроить отображение и редактирование пользователей.
    """

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone",
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = ("phone", "email", "is_staff", "role")
    search_fields = ("phone",)
    ordering = ("phone",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
