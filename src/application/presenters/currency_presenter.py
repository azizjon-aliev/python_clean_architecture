from typing import Dict
from src.interactor.dtos.currency_dtos import CreateCurrencyOutputDto, UpdateCurrencyOutputDto
from src.interactor.interfaces.presenters.currency_presenter import CreateCurrencyPresenterInterface, \
    UpdateCurrencyPresenterInterface


class CreateCurrencyPresenter(CreateCurrencyPresenterInterface):
    def present(self, output_dto: CreateCurrencyOutputDto) -> Dict:
        return {
            "id": output_dto.currency.currency_id,
            "code": output_dto.currency.code,
            "name": output_dto.currency.name,
            "symbol": output_dto.currency.symbol
        }


class UpdateCurrencyPresenter(UpdateCurrencyPresenterInterface):
    def present(self, output_dto: UpdateCurrencyOutputDto) -> Dict:
        return {
            "id": output_dto.currency.currency_id,
            "code": output_dto.currency.code,
            "name": output_dto.currency.name,
            "symbol": output_dto.currency.symbol
        }
