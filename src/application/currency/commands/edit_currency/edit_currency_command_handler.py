import logging
from dataclasses import dataclass

from automapper import Mapper

from src.application.common.contracts.repositories.currency_repository import (
    CurrencyRepositoryInterface,
)
from src.application.currency.commands.edit_currency.edit_currency_command import (
    EditCurrencyCommand,
)
from src.application.currency.responses.currency_detail_vm import CurrencyDetailVm

logger = logging.getLogger(__name__)


@dataclass
class EditCurrencyCommandHandler:
    repository: CurrencyRepositoryInterface
    mapper: Mapper

    def handle(self, request: EditCurrencyCommand):
        logger.info("Handler EditCurrencyCommand...")

        data = {
            "code": request.code,
            "name": request.name,
            "symbol": request.symbol,
        }
        db_response = self.repository.update(object_id=request.id, **data)

        logger.info("Success EditCurrencyCommand handler.")
        return self.mapper.to(CurrencyDetailVm).map(db_response)
