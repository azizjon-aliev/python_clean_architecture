from django.contrib import admin

from src.infrastructure.models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass
