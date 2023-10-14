from abc import ABC, abstractmethod
from typing import Dict
from src.domain.dtos.currency_dtos import CreateCurrencyOutputDto, UpdateCurrencyOutputDto


class CreateCurrencyPresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto: CreateCurrencyOutputDto) -> Dict:
        pass


class UpdateCurrencyPresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto: UpdateCurrencyOutputDto) -> Dict:
        pass
