import pytest
from src.application.presenters.currency_presenter import (
    CreateCurrencyPresenter,
    ListCurrencyPresenter,
    UpdateCurrencyPresenter,
)
from src.domain.entities.currency import Currency
from src.infrastructure.repotisories.currency_repository import CurrencyRepository
from src.interactor.dtos.currency_dtos import (
    CreateCurrencyInputDto,
    ListCurrencyInputDto,
    UpdateCurrencyInputDto,
)
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.use_cases.currency import (
    CreateCurrencyUseCase,
    DeleteCurrencyUseCase,
    ListCurrencyUseCase,
    UpdateCurrencyUseCase,
)

from tests.infrastucture.factories.currency_factory import CurrencyFactory


class MockLogger(LoggerInterface):
    def log_debug(self, message: str) -> None:
        pass

    def log_warning(self, message: str) -> None:
        pass

    def log_critical(self, message: str) -> None:
        pass

    def log_exception(self, message: str) -> None:
        pass

    def log_info(self, message):
        pass

    def log_error(self, message):
        pass


repository = CurrencyRepository()


@pytest.mark.django_db
def test_list_currency_use_case() -> None:
    use_case = ListCurrencyUseCase(
        repository=repository,
        presenter=ListCurrencyPresenter(),
        logger=MockLogger(),
    )
    input_dto = ListCurrencyInputDto(skip=0, limit=100)
    response = use_case.execute(input_dto=input_dto)

    assert isinstance(response.get("currencies"), list)
    assert all(
        isinstance(currency, Currency) for currency in response.get("currencies")
    )


@pytest.mark.django_db
def test_create_currency_use_case() -> None:
    data = {
        "code": "USD",
        "name": "Dollar",
        "symbol": "$",
    }

    use_case = CreateCurrencyUseCase(
        repository=repository,
        presenter=CreateCurrencyPresenter(),
        logger=MockLogger(),
    )
    input_dto = CreateCurrencyInputDto(**data)
    response = use_case.execute(input_dto=input_dto)

    assert data.get("code") == response.get("code")
    assert data.get("name") == response.get("name")
    assert data.get("symbol") == response.get("symbol")


@pytest.mark.django_db
def test_update_currency_use_case() -> None:
    currency_old = CurrencyFactory.create()

    use_case = UpdateCurrencyUseCase(
        repository=repository,
        presenter=UpdateCurrencyPresenter(),
        logger=MockLogger(),
    )
    input_dto = UpdateCurrencyInputDto(
        code="USD",
        name="Dollar",
        symbol=None,
    )

    response = use_case.execute(currency_id=currency_old.pk, input_dto=input_dto)

    assert input_dto.code == response.get("code")
    assert input_dto.name == response.get("name")
    assert currency_old.symbol == response.get("symbol")


@pytest.mark.django_db
def test_delete_currency_use_case() -> None:
    currency = CurrencyFactory.create()

    use_case = DeleteCurrencyUseCase(
        repository=repository,
        logger=MockLogger(),
    )
    use_case.execute(currency_id=currency.pk)

    assert repository.exists(pk=currency.pk) is False
