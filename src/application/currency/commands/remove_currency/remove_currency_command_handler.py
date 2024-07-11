from dataclasses import dataclass

from automapper import Mapper

from src.application.common.contracts.repositories.currency_repository import (
    CurrencyRepositoryInterface,
)
from src.application.currency.commands.remove_currency.remove_currency_command import (
    RemoveCurrencyCommand,
)


@dataclass
class RemoveCurrencyCommandHandler:
    repository: CurrencyRepositoryInterface
    mapper: Mapper

    def handle(self, request: RemoveCurrencyCommand):
        self.repository.delete(object_id=request.id)
