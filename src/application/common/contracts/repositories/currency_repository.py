from abc import ABC

from src.application.common.contracts.repositories.base_repository import (
    AbstractRepositoryInterface,
)
from src.domain.entities.currency import Currency
from src.domain.value_objects import CurrencyId


class CurrencyRepositoryInterface(
    AbstractRepositoryInterface[Currency, CurrencyId], ABC
):
    pass
