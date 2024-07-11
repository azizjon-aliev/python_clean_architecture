from dataclasses import dataclass
from typing import Optional

from mediatr import GenericQuery

from src.application.currency.responses.currency_detail_vm import CurrencyDetailVm
from src.domain.value_objects import CurrencyId


@dataclass
class EditCurrencyCommand(GenericQuery[CurrencyDetailVm]):
    id: CurrencyId
    code: Optional[str]
    name: Optional[str]
    symbol: Optional[str]
