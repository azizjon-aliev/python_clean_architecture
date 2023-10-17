from typing import Dict

from src.interactor.dtos.currency_dtos import (
    CreateCurrencyOutputDto,
    ListCurrencyOutputDto,
    UpdateCurrencyOutputDto,
)
from src.interactor.interfaces.presenters.currency_presenter import (
    CreateCurrencyPresenterInterface,
    DetailCurrencyPresenterInterface,
    ListCurrencyPresenterInterface,
    UpdateCurrencyPresenterInterface,
)


class ListCurrencyPresenter(ListCurrencyPresenterInterface):
    def present(self, output_dto: ListCurrencyOutputDto) -> Dict:
        return {
            "count": output_dto.count,
            "total": output_dto.total,
            "currencies": [
                {
                    "id": currency.currency_id,
                    "code": currency.code,
                    "name": currency.name,
                    "symbol": currency.symbol
                }
                for currency in output_dto.currencies
            ]
        }


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


class DetailCurrencyPresenter(DetailCurrencyPresenterInterface):
    def present(self, output_dto: UpdateCurrencyOutputDto) -> Dict:
        return {
            "id": output_dto.currency.currency_id,
            "code": output_dto.currency.code,
            "name": output_dto.currency.name,
            "symbol": output_dto.currency.symbol
        }
