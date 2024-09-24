from dataclasses import dataclass

from src.domain.value_objects import CurrencyId


@dataclass
class CurrencyVm:
    id: CurrencyId
    # code: str
    name: str
    # symbol: str
