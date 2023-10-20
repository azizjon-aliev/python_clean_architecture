from django.db import models


class Currency(models.Model):
    code: str = models.CharField(verbose_name="Код", max_length=10)
    name: str = models.CharField(verbose_name="Название", max_length=100)
    symbol: str = models.CharField(verbose_name="Символ", max_length=10)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"
