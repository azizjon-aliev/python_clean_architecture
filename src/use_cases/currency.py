from typing import Dict
from src.interface.repotisories.currency_repository import CurrencyRepositoryInterface
from src.interface.presenters.currency_presenter import CreateCurrencyPresenterInterface
from src.domain.dtos.currency_dtos import CreateCurrencyInputDto, CreateCurrencyOutputDto


class CreateCurrencyUseCase:
    def __int__(self, repository: CurrencyRepositoryInterface, presenter: CreateCurrencyPresenterInterface):
        self.repository = repository
        self.presenter = presenter

    def execute(self, input_dto: CreateCurrencyInputDto) -> Dict:
        currency = self.repository.create(
            code=input_dto.code,
            name=input_dto.name,
            symbol=input_dto.symbol
        )
        output_dto = CreateCurrencyOutputDto(currency)
        return self.presenter.present(output_dto)
