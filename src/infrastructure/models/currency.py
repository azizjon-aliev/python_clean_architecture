from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Currency(models.Model):
    """
    Represents a currency with its ISO code, name, and symbol.

    Attributes:
        code (str): The ISO 4217 currency code (e.g., USD, EUR).
        name (str): The full name of the currency (e.g., United States Dollar).
        symbol (str): The symbol associated with the currency (e.g., $, €, ₽).
    """

    # Validators
    ISO_CODE_VALIDATOR = RegexValidator(
        regex=r"^[A-Z]{3}$",
        message=_("Currency code must consist of exactly 3 uppercase letters."),
        code="invalid_currency_code",
    )

    SYMBOL_VALIDATOR = RegexValidator(
        regex=r"^[^\s]{1,10}$",
        message=_("Currency symbol must be 1 to 10 non-whitespace characters."),
        code="invalid_currency_symbol",
    )

    # Fields
    code: str = models.CharField(
        _("Code"),
        max_length=3,
        unique=True,
        validators=[ISO_CODE_VALIDATOR],
        help_text=_("ISO 4217 currency code (3 uppercase letters)."),
    )
    name: str = models.CharField(
        _("Name"),
        max_length=100,
        unique=True,
        help_text=_("Full name of the currency."),
    )
    symbol: str = models.CharField(
        _("Symbol"),
        max_length=10,
        validators=[SYMBOL_VALIDATOR],
        help_text=_("Symbol of the currency (e.g., $, €, ₽)."),
    )

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")
        ordering = ["code"]
        indexes = [
            models.Index(fields=["code"], name="currency_code_idx"),
            models.Index(fields=["name"], name="currency_name_idx"),
        ]

    def __str__(self) -> str:
        """
        Returns the string representation of the Currency instance.

        Returns:
            str: The name of the currency.
        """
        return self.name

    def save(self, *args, **kwargs) -> None:
        """
        Overrides the save method to ensure data consistency before saving.

        - Converts the currency code to uppercase.
        - Formats the currency name in title case.
        - Strips any leading or trailing whitespace from the symbol.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.code = self.code.upper()
        self.name = self.name.title()
        self.symbol = self.symbol.strip()
        super().save(*args, **kwargs)
