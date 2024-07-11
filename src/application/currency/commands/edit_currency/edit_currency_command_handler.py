from dataclasses import dataclass

from automapper import Mapper

from src.application.common.contracts.repositories.currency_repository import (
    CurrencyRepositoryInterface,
)
from src.application.currency.commands.edit_currency.edit_currency_command import (
    EditCurrencyCommand,
)
from src.application.currency.responses.currency_detail_vm import CurrencyDetailVm


@dataclass
class EditCurrencyCommandHandler:
    repository: CurrencyRepositoryInterface
    mapper: Mapper

    def handle(self, request: EditCurrencyCommand):
        data = {
            "code": request.code,
            "name": request.name,
            "symbol": request.symbol,
        }
        db_response = self.repository.update(object_id=request.id, **data)
        return self.mapper.to(CurrencyDetailVm).map(db_response)
