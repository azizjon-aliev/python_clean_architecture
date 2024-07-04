from src.interactor.interfaces.presenters.base_presenter import AbstractPresenterInterface
from src.interactor.dtos.currency_dtos import (
    CreateCurrencyOutputDto,
    DetailCurrencyOutputDto,
    ListCurrencyOutputDto,
    UpdateCurrencyOutputDto,
)

class ListCurrencyPresenterInterface(AbstractPresenterInterface[ListCurrencyOutputDto]):
    pass

class CreateCurrencyPresenterInterface(AbstractPresenterInterface[CreateCurrencyOutputDto]):
    pass

class UpdateCurrencyPresenterInterface(AbstractPresenterInterface[UpdateCurrencyOutputDto]):
    pass

class DetailCurrencyPresenterInterface(AbstractPresenterInterface[DetailCurrencyOutputDto]):
    pass
