import punq
from automapper import Mapper
from mediatr import Mediator

from src.application.common.contracts.logger.logger import LoggerInterface
from src.application.common.contracts.repositories.currency_repository import (
    CurrencyRepositoryInterface,
)
from src.application.common.mappings.mapper import mapper
from src.application.common.mediator_registers import mediator_registers
from src.application.currency.commands.add_currency.add_currency_command_handler import (
    AddCurrencyCommandHandler,
)
from src.application.currency.commands.edit_currency.edit_currency_command_handler import (
    EditCurrencyCommandHandler,
)
from src.application.currency.commands.remove_currency.remove_currency_command_handler import (
    RemoveCurrencyCommandHandler,
)
from src.application.currency.queries.get_currencies_list.get_currencies_list_query_handler import (
    GetCurrenciesListQueryHandler,
)
from src.application.currency.queries.get_currency_detail.get_currency_detail_query_handler import (
    GetCurrencyDetailQueryHandler,
)
from src.infrastructure.loggers.logger_default import LoggerDefault
from src.infrastructure.repositories.currency_repository import CurrencyRepository

container = punq.Container()

# common
container.register(service=LoggerInterface, instance=LoggerDefault())
container.register(service=Mapper, instance=mapper)

# mediator
container.register(service=Mediator, instance=mediator_registers)

# currency
container.register(service=CurrencyRepositoryInterface, instance=CurrencyRepository())
container.register(GetCurrenciesListQueryHandler)
container.register(GetCurrencyDetailQueryHandler)
container.register(AddCurrencyCommandHandler)
container.register(EditCurrencyCommandHandler)
container.register(RemoveCurrencyCommandHandler)
