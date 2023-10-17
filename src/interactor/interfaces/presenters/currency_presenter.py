from abc import ABC, abstractmethod
from typing import Dict, List
from src.interactor.dtos.currency_dtos import CreateCurrencyOutputDto, UpdateCurrencyOutputDto, ListCurrencyOutputDto, \
    DetailCurrencyOutputDto


class ListCurrencyPresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto: ListCurrencyOutputDto) -> Dict:
        pass


class CreateCurrencyPresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto: CreateCurrencyOutputDto) -> Dict:
        pass


class UpdateCurrencyPresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto: UpdateCurrencyOutputDto) -> Dict:
        pass


class DetailCurrencyPresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto: DetailCurrencyOutputDto) -> Dict:
        pass
