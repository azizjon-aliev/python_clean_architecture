from dataclasses import dataclass

from mediatr import GenericQuery

from src.application.currency.responses.currency_detail_vm import CurrencyDetailVm


@dataclass
class AddCurrencyCommand(GenericQuery[CurrencyDetailVm]):
    code: str
    name: str
    symbol: str
