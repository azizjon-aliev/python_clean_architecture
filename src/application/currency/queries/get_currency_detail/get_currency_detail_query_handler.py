from dataclasses import dataclass

from automapper import Mapper

from src.application.common.contracts.repositories.currency_repository import (
    CurrencyRepositoryInterface,
)
from src.application.currency.queries.get_currency_detail.get_currency_detail_query import (
    GetCurrencyDetailQuery,
)
from src.application.currency.responses.currency_detail_vm import CurrencyDetailVm


@dataclass
class GetCurrencyDetailQueryHandler:
    repository: CurrencyRepositoryInterface
    mapper: Mapper

    def handle(self, request: GetCurrencyDetailQuery):
        db_response = self.repository.get(object_id=request.id)
        return self.mapper.to(CurrencyDetailVm).map(db_response)
