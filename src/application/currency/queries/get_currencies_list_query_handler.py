from dataclasses import dataclass

from automapper import Mapper

from src.application.common.contracts.repositories.currency_repository import (
    CurrencyRepositoryInterface,
)
from src.application.currency.queries.get_currencies_list_query import (
    GetCurrenciesListQuery,
)
from src.application.currency.responses.currency_vm import CurrencyVm


@dataclass
class GetCurrenciesListQueryHandler:
    repository: CurrencyRepositoryInterface
    mapper: Mapper

    def handle(self, request: GetCurrenciesListQuery):
        db_response = self.repository.list(skip=request.skip, limit=request.limit)
        return [self.mapper.to(CurrencyVm).map(currency) for currency in db_response]
