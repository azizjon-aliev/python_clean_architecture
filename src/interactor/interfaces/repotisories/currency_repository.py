from abc import ABC, abstractmethod
from typing import List

from src.domain.value_objects import CurrencyId
from src.domain.entities.currency import Currency


class CurrencyRepositoryInterface(ABC):
    @abstractmethod
    def get(self, currency_id: CurrencyId) -> Currency:
        pass

    @abstractmethod
    def delete(self, currency_id: CurrencyId) -> None:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def list(self, skip: int = 0, limit: int = 100) -> List[Currency]:
        pass

    @abstractmethod
    def exists(self, **kwargs) -> bool:
        pass

    @abstractmethod
    def create(self, code: str, name: str, symbol: str) -> Currency:
        pass

    @abstractmethod
    def update(self, currency_id: CurrencyId, code: str, name: str, symbol: str) -> Currency:
        pass
