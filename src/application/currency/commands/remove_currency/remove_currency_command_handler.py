import logging
from dataclasses import dataclass

from automapper import Mapper

from src.application.common.contracts.repositories.currency_repository import (
    CurrencyRepositoryInterface,
)
from src.application.currency.commands.remove_currency.remove_currency_command import (
    RemoveCurrencyCommand,
)

logger = logging.getLogger(__name__)


@dataclass
class RemoveCurrencyCommandHandler:
    repository: CurrencyRepositoryInterface
    mapper: Mapper

    def handle(self, request: RemoveCurrencyCommand) -> None:
        logger.info("Handler RemoveCurrencyCommand...")
        self.repository.delete(object_id=request.id)
        logger.info("Success RemoveCurrencyCommand handler.")
