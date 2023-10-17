from dataclasses import dataclass, field
from typing import Optional, List, Union

from src.domain.entities.currency import Currency


@dataclass
class ListCurrencyInputDto:
    skip: Optional[int]
    limit: Optional[int]

    def __post_init__(self) -> None:
        if self.skip is None:
            self.skip = 0
        if self.limit is None:
            self.limit = 100


@dataclass
class ListCurrencyOutputDto:
    currencies: List[Currency]
    total: int
    count: int


@dataclass
class CreateCurrencyInputDto:
    code: str
    name: str
    symbol: str


@dataclass
class CreateCurrencyOutputDto:
    currency: Currency


@dataclass
class UpdateCurrencyInputDto:
    code: Optional[str]
    name: Optional[str]
    symbol: Optional[str]


@dataclass
class UpdateCurrencyOutputDto:
    currency: Currency


@dataclass
class DetailCurrencyOutputDto:
    currency: Currency
