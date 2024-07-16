import punq
from automapper import Mapper
from mediatr import Mediator

from src.application.authentication.commands.register_user.register_user_command_handler import (
    RegisterUserCommandHandler,
)
from src.application.authentication.queries.login_user.login_user_query_handler import (
    LoginUserQueryHandler,
)
from src.application.authentication.queries.refresh_token.refresh_token_query_handler import (
    RefreshTokenQueryHandler,
)
from src.application.common.contracts.logger.logger import LoggerInterface
from src.application.common.contracts.providers.token_provider import TokenProviderInterface
from src.application.common.contracts.repositories.account_repository import (
    UserRepositoryInterface,
)
from src.application.common.contracts.repositories.currency_repository import (
    CurrencyRepositoryInterface,
)
from src.application.common.contracts.services.auth_service import AuthServiceInterface
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
from src.infrastructure.providers.token_provider import TokenProvider
from src.infrastructure.repositories.account_repository import UserRepository
from src.infrastructure.repositories.currency_repository import CurrencyRepository
from src.infrastructure.services.auth_service import AuthService

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

# account
container.register(service=UserRepositoryInterface, instance=UserRepository())

# authentication
container.register(service=AuthServiceInterface, instance=AuthService())
container.register(service=TokenProviderInterface, instance=TokenProvider())
container.register(LoginUserQueryHandler)
container.register(RefreshTokenQueryHandler)
container.register(RegisterUserCommandHandler)
