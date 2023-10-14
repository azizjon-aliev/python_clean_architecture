from abc import ABC, abstractmethod
from src.domain.value_objects import CurrencyId
from src.domain.entities.currency import Currency


class CurrencyRepositoryInterface(ABC):
    @abstractmethod
    def get(self, currency_id: CurrencyId) -> Currency:
        pass

    @abstractmethod
    def create(self, code: str, name: str, symbol: str) -> Currency:
        pass

    @abstractmethod
    def update(self, currency_id: CurrencyId, code: str, name: str, symbol: str) -> Currency:
        pass
