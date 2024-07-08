import punq

from src.application.presenters.authentication_presenter import LoginPresenter
from src.application.presenters.currency_presenter import (
    CreateCurrencyPresenter,
    DetailCurrencyPresenter,
    ListCurrencyPresenter,
    UpdateCurrencyPresenter,
)
from src.infrastructure.loggers.logger_default import LoggerDefault
from src.infrastructure.repositories.account_repository import UserRepository
from src.infrastructure.repositories.currency_repository import CurrencyRepository
from src.infrastructure.repositories.authentication_repository import AuthRepository
from src.infrastructure.providers.token_provider import TokenProvider
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.interfaces.presenters.authentication_presenter import (
    LoginPresenterInterface,
)
from src.interactor.interfaces.presenters.currency_presenter import (
    CreateCurrencyPresenterInterface,
    DetailCurrencyPresenterInterface,
    ListCurrencyPresenterInterface,
    UpdateCurrencyPresenterInterface,
)
from src.interactor.interfaces.repositories.account_repository import (
    UserRepositoryInterface,
)
from src.interactor.interfaces.repositories.authentication_repository import (
    AuthRepositoryInterface,
)
from src.interactor.interfaces.providers.token_provider import (
    TokenProviderInterface,
)
from src.interactor.interfaces.repositories.currency_repository import (
    CurrencyRepositoryInterface,
)
from src.interactor.use_cases.authentication import RefreshTokenUseCase, RegisterStep1UseCase, LoginUseCase
from src.interactor.use_cases.currency import (
    CreateCurrencyUseCase,
    DeleteCurrencyUseCase,
    DetailCurrencyUseCase,
    ListCurrencyUseCase,
    UpdateCurrencyUseCase,
)

container = punq.Container()

# common
container.register(service=LoggerInterface, instance=LoggerDefault())

# account
container.register(service=UserRepositoryInterface, instance=UserRepository())

# authentication
container.register(service=AuthRepositoryInterface, instance=AuthRepository())
container.register(service=TokenProviderInterface, instance=TokenProvider())
container.register(service=LoginPresenterInterface, instance=LoginPresenter())
container.register(RegisterStep1UseCase)
container.register(LoginUseCase)
container.register(RefreshTokenUseCase)

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
container.register(ListCurrencyUseCase)
container.register(DetailCurrencyUseCase)
container.register(CreateCurrencyUseCase)
container.register(UpdateCurrencyUseCase)
container.register(DeleteCurrencyUseCase)
