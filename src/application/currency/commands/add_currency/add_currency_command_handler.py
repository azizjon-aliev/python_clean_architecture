import logging
from dataclasses import dataclass

from automapper import Mapper

from src.application.common.contracts.repositories.currency_repository import (
    CurrencyRepositoryInterface,
)
from src.application.currency.commands.add_currency.add_currency_command import (
    AddCurrencyCommand,
)
from src.application.currency.responses.currency_detail_vm import CurrencyDetailVm

logger = logging.getLogger(__name__)


@dataclass
class AddCurrencyCommandHandler:
    repository: CurrencyRepositoryInterface
    mapper: Mapper

    def handle(self, request: AddCurrencyCommand):
        logger.info("Handling AddCurrencyCommand...")

        data = {
            "code": request.code,
            "name": request.name,
            "symbol": request.symbol,
        }
        db_response = self.repository.create(**data)

        logger.info("Successfully handled AddCurrencyCommand...")
        return self.mapper.to(CurrencyDetailVm).map(db_response)
