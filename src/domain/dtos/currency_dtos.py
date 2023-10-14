from dataclasses import dataclass
from ..entities.currency import Currency


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
    code: str
    name: str
    symbol: str


@dataclass
class UpdateCurrencyOutputDto:
    code: str
    name: str
    symbol: str
