from dataclasses import dataclass

from automapper import Mapper

from src.application.common.contracts.repositories.currency_repository import (
    CurrencyRepositoryInterface,
)
from src.application.currency.commands.add_currency.add_currency_command import (
    AddCurrencyCommand,
)
from src.application.currency.responses.currency_detail_vm import CurrencyDetailVm


@dataclass
class AddCurrencyCommandHandler:
    repository: CurrencyRepositoryInterface
    mapper: Mapper

    def handle(self, request: AddCurrencyCommand):
        data = {
            "code": request.code,
            "name": request.name,
            "symbol": request.symbol,
        }
        db_response = self.repository.create(**data)
        return self.mapper.to(CurrencyDetailVm).map(db_response)
