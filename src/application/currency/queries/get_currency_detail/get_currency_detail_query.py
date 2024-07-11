from dataclasses import dataclass

from mediatr import GenericQuery

from src.application.currency.responses.currency_vm import CurrencyVm
from src.domain.value_objects import CurrencyId


@dataclass
class GetCurrencyDetailQuery(GenericQuery[CurrencyVm]):
    id: CurrencyId
