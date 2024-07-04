from django.db import models


class Currency(models.Model):
    code: str = models.CharField(verbose_name="Code", max_length=10)
    name: str = models.CharField(verbose_name="Name", max_length=100)
    symbol: str = models.CharField(verbose_name="Symbol", max_length=10)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
