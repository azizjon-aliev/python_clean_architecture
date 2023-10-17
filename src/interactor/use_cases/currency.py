from typing import Dict, List

from src.domain.value_objects import CurrencyId
from src.interactor.errors.error_classes import EntityDoesNotExist
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.interfaces.repotisories.currency_repository import CurrencyRepositoryInterface
from src.interactor.interfaces.presenters.currency_presenter import CreateCurrencyPresenterInterface, \
    UpdateCurrencyPresenterInterface, ListCurrencyPresenterInterface, DetailCurrencyPresenterInterface
from src.interactor.dtos.currency_dtos import CreateCurrencyInputDto, CreateCurrencyOutputDto, UpdateCurrencyInputDto, \
    UpdateCurrencyOutputDto, ListCurrencyInputDto, ListCurrencyOutputDto, DetailCurrencyOutputDto
from src.interactor.validations.currency_validation import CreateCurrencyInputDtoValidator, \
    UpdateCurrencyInputDtoValidator, ListCurrencyInputDtoValidator


class ListCurrencyUseCase:
    def __init__(self,
                 repository: CurrencyRepositoryInterface,
                 presenter: ListCurrencyPresenterInterface,
                 logger: LoggerInterface):
        self.repository = repository
        self.presenter = presenter
        self.logger = logger

    def execute(self, input_dto: ListCurrencyInputDto) -> Dict:
        validator = ListCurrencyInputDtoValidator(
            skip=input_dto.skip,
            limit=input_dto.limit,
        )
        currencies = self.repository.list(**validator.model_dump())
        output_dto = ListCurrencyOutputDto(
            currencies=currencies,
            total=self.repository.count(),
            count=len(currencies)
        )
        self.logger.log_info("Currencies get all successfully")
        return self.presenter.present(output_dto)


class CreateCurrencyUseCase:
    def __init__(self,
                 repository: CurrencyRepositoryInterface,
                 presenter: CreateCurrencyPresenterInterface,
                 logger: LoggerInterface):
        self.repository = repository
        self.presenter = presenter
        self.logger = logger

    def execute(self, input_dto: CreateCurrencyInputDto) -> Dict:
        validator = CreateCurrencyInputDtoValidator(
            code=input_dto.code,
            name=input_dto.name,
            symbol=input_dto.symbol
        )
        currency = self.repository.create(**validator.model_dump())
        output_dto = CreateCurrencyOutputDto(currency)
        self.logger.log_info("Currency created successfully")
        return self.presenter.present(output_dto)


class UpdateCurrencyUseCase:
    def __init__(self,
                 repository: CurrencyRepositoryInterface,
                 presenter: UpdateCurrencyPresenterInterface,
                 logger: LoggerInterface):
        self.repository = repository
        self.presenter = presenter
        self.logger = logger

    def execute(self, currency_id: CurrencyId, input_dto: UpdateCurrencyInputDto) -> Dict:
        if not self.repository.exists(pk=currency_id):
            self.logger.log_error(f'Currency id {currency_id} not found in repository')
            raise EntityDoesNotExist(f'Currency id {currency_id} not found')

        validator = UpdateCurrencyInputDtoValidator(
            code=input_dto.code,
            name=input_dto.name,
            symbol=input_dto.symbol
        )
        currency = self.repository.update(currency_id, **validator.model_dump())
        output_dto = UpdateCurrencyOutputDto(currency)
        self.logger.log_info("Currency updated successfully")
        return self.presenter.present(output_dto)


class DetailCurrencyUseCase:
    def __init__(self,
                 repository: CurrencyRepositoryInterface,
                 presenter: DetailCurrencyPresenterInterface,
                 logger: LoggerInterface):
        self.repository = repository
        self.presenter = presenter
        self.logger = logger

    def execute(self, currency_id: CurrencyId) -> Dict:
        if not self.repository.exists(pk=currency_id):
            self.logger.log_error(f'Currency id {currency_id} not found in repository')
            raise EntityDoesNotExist(f'Currency id {currency_id} not found')

        currency = self.repository.get(currency_id)
        output_dto = DetailCurrencyOutputDto(currency)
        self.logger.log_info("Currency detail show successfully")
        return self.presenter.present(output_dto)


class DeleteCurrencyUseCase:
    def __init__(self,
                 repository: CurrencyRepositoryInterface,
                 logger: LoggerInterface):
        self.repository = repository
        self.logger = logger

    def execute(self, currency_id: CurrencyId) -> None:
        if not self.repository.exists(pk=currency_id):
            self.logger.log_error(f'Currency id {currency_id} not found in repository')
            raise EntityDoesNotExist(f'Currency id {currency_id} not found')

        currency = self.repository.delete(currency_id)
        self.logger.log_info("Currency deleted successfully")
