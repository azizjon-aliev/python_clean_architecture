from typing import Dict

from automapper import mapper

from src.domain.value_objects import CurrencyId
from src.interactor.dtos.currency_dtos import (
    CreateCurrencyInputDto,
    CreateCurrencyOutputDto,
    DetailCurrencyOutputDto,
    ListCurrencyInputDto,
    ListCurrencyOutputDto,
    UpdateCurrencyInputDto,
    UpdateCurrencyOutputDto,
)
from src.interactor.errors.error_classes import EntityDoesNotExist
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.interfaces.presenters.currency_presenter import (
    CreateCurrencyPresenterInterface,
    DetailCurrencyPresenterInterface,
    ListCurrencyPresenterInterface,
    UpdateCurrencyPresenterInterface,
)
from src.interactor.interfaces.repositories.currency_repository import (
    CurrencyRepositoryInterface,
)
from src.interactor.validations.currency_validation import (
    ListCurrencyInputDtoValidator,
    UpdateCurrencyInputDtoValidator,
)


class ListCurrencyUseCase:
    def __init__(
        self,
        repository: CurrencyRepositoryInterface,
        presenter: ListCurrencyPresenterInterface,
        logger: LoggerInterface,
    ):
        self.repository = repository
        self.presenter = presenter
        self.logger = logger

    def execute(self, input_dto: ListCurrencyInputDto) -> Dict:
        validator = mapper.to(ListCurrencyInputDtoValidator).map(input_dto)
        currencies = self.repository.list(**validator.model_dump())
        output_dto = mapper.to(ListCurrencyOutputDto).map(
            {
                "currencies": currencies,
                "total": self.repository.count(),
                "count": len(currencies),
            }
        )
        self.logger.log_info("Currencies get all successfully")
        return self.presenter.present(output_dto)


class CreateCurrencyUseCase:
    def __init__(
        self,
        repository: CurrencyRepositoryInterface,
        presenter: CreateCurrencyPresenterInterface,
        logger: LoggerInterface,
    ):
        self.repository = repository
        self.presenter = presenter
        self.logger = logger

    def execute(self, input_dto: CreateCurrencyInputDto) -> Dict:
        validator = mapper.to(CreateCurrencyUseCase).map(input_dto)
        currency = self.repository.create(**validator.model_dump())
        output_dto = mapper.to(CreateCurrencyOutputDto).map(currency)
        self.logger.log_info("Currency created successfully")
        return self.presenter.present(output_dto)


class UpdateCurrencyUseCase:
    def __init__(
        self,
        repository: CurrencyRepositoryInterface,
        presenter: UpdateCurrencyPresenterInterface,
        logger: LoggerInterface,
    ):
        self.repository = repository
        self.presenter = presenter
        self.logger = logger

    def execute(
        self, currency_id: CurrencyId, input_dto: UpdateCurrencyInputDto
    ) -> Dict:
        if not self.repository.exists(pk=currency_id):
            self.logger.log_error(f"Currency id {currency_id} not found in repository")
            raise EntityDoesNotExist(f"Currency id {currency_id} not found")

        validator = mapper.to(UpdateCurrencyInputDtoValidator).map(input_dto)
        currency = self.repository.update(currency_id, **validator.model_dump())
        output_dto = mapper.to(UpdateCurrencyOutputDto).map(currency)
        self.logger.log_info("Currency updated successfully")
        return self.presenter.present(output_dto)


class DetailCurrencyUseCase:
    def __init__(
        self,
        repository: CurrencyRepositoryInterface,
        presenter: DetailCurrencyPresenterInterface,
        logger: LoggerInterface,
    ):
        self.repository = repository
        self.presenter = presenter
        self.logger = logger

    def execute(self, currency_id: CurrencyId) -> Dict:
        if not self.repository.exists(pk=currency_id):
            self.logger.log_error(f"Currency id {currency_id} not found in repository")
            raise EntityDoesNotExist(f"Currency id {currency_id} not found")

        currency = self.repository.get(currency_id)
        output_dto = mapper.to(DetailCurrencyOutputDto).map(currency)
        self.logger.log_info("Currency detail show successfully")
        return self.presenter.present(output_dto)


class DeleteCurrencyUseCase:
    def __init__(
        self, repository: CurrencyRepositoryInterface, logger: LoggerInterface
    ):
        self.repository = repository
        self.logger = logger

    def execute(self, currency_id: CurrencyId) -> None:
        if not self.repository.exists(pk=currency_id):
            self.logger.log_error(f"Currency id {currency_id} not found in repository")
            raise EntityDoesNotExist(f"Currency id {currency_id} not found")

        self.repository.delete(currency_id)
        self.logger.log_info("Currency deleted successfully")
