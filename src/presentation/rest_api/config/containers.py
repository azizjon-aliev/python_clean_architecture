import punq

from src.application.presenters.currency_presenter import (
    CreateCurrencyPresenter,
    DetailCurrencyPresenter,
    ListCurrencyPresenter,
    UpdateCurrencyPresenter,
)
from src.infrastructure.loggers.logger_default import LoggerDefault
from src.infrastructure.repotisories.currency_repository import CurrencyRepository
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.interfaces.presenters.currency_presenter import (
    CreateCurrencyPresenterInterface,
    DetailCurrencyPresenterInterface,
    ListCurrencyPresenterInterface,
    UpdateCurrencyPresenterInterface,
)
from src.interactor.interfaces.repotisories.currency_repository import (
    CurrencyRepositoryInterface,
)
from src.interactor.use_cases.currency import (
    CreateCurrencyUseCase,
    DeleteCurrencyUseCase,
    DetailCurrencyUseCase,
    ListCurrencyUseCase,
    UpdateCurrencyUseCase,
)

container = punq.Container()

container.register(service=CurrencyRepositoryInterface, instance=CurrencyRepository())
container.register(service=LoggerInterface, instance=LoggerDefault())
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
