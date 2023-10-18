import string

import factory
from factory import django, fuzzy

from src.infrastructure.models import Currency


class CurrencyFactory(django.DjangoModelFactory):
    class Meta:
        model = Currency

    code = fuzzy.FuzzyText(length=3, chars=string.ascii_uppercase)
    name = fuzzy.FuzzyText(length=15, chars=string.ascii_letters)
    symbol = fuzzy.FuzzyText(length=1)
