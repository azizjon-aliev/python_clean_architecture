from src.domain.entities.currency import Currency
from src.domain.value_objects import CurrencyId
from src.interactor.interfaces.repotisories.base_repository import AbstractRepositoryInterface

class CurrencyRepositoryInterface(AbstractRepositoryInterface[Currency, CurrencyId]):
    pass
