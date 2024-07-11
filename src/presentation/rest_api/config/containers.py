import punq
from automapper import Mapper
from mediatr import Mediator

from src.application.common.contracts.logger.logger import LoggerInterface
from src.application.common.contracts.repositories.account_repository import (
    UserRepositoryInterface,
)
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
from src.application.presenters.account_presenter import RegisterStep1Presenter
from src.application.presenters.currency_presenter import (
    CreateCurrencyPresenter,
    DetailCurrencyPresenter,
    ListCurrencyPresenter,
    UpdateCurrencyPresenter,
)
from src.infrastructure.loggers.logger_default import LoggerDefault
from src.infrastructure.repositories.account_repository import UserRepository
from src.infrastructure.repositories.currency_repository import CurrencyRepository
from src.interactor.interfaces.presenters.account_presenter import (
    RegisterStep1PresenterInterface,
)
from src.interactor.interfaces.presenters.currency_presenter import (
    CreateCurrencyPresenterInterface,
    DetailCurrencyPresenterInterface,
    ListCurrencyPresenterInterface,
    UpdateCurrencyPresenterInterface,
)
from src.interactor.use_cases.account import RegisterStep1UseCase
from src.interactor.use_cases.currency import (
    CreateCurrencyUseCase,
    DeleteCurrencyUseCase,
    DetailCurrencyUseCase,
    UpdateCurrencyUseCase,
)

container = punq.Container()

# common
container.register(service=LoggerInterface, instance=LoggerDefault())
container.register(service=Mapper, instance=mapper)

# mediator
container.register(service=Mediator, instance=mediator_registers)
container.register(GetCurrenciesListQueryHandler)
container.register(GetCurrencyDetailQueryHandler)
container.register(AddCurrencyCommandHandler)
container.register(EditCurrencyCommandHandler)
container.register(RemoveCurrencyCommandHandler)

# account
container.register(service=UserRepositoryInterface, instance=UserRepository())
container.register(
    service=RegisterStep1PresenterInterface, instance=RegisterStep1Presenter()
)
container.register(RegisterStep1UseCase)

# currency
container.register(service=CurrencyRepositoryInterface, instance=CurrencyRepository())

container.register(
    service=ListCurrencyPresenterInterface, instance=ListCurrencyPresenter()
)
container.register(
    service=DetailCurrencyPresenterInterface, instance=DetailCurrencyPresenter()
)
container.register(
    service=CreateCurrencyPresenterInterface, instance=CreateCurrencyPresenter()
)
container.register(
    service=UpdateCurrencyPresenterInterface, instance=UpdateCurrencyPresenter()
)
container.register(DetailCurrencyUseCase)
container.register(CreateCurrencyUseCase)
container.register(UpdateCurrencyUseCase)
container.register(DeleteCurrencyUseCase)
