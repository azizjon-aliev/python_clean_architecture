from dataclasses import dataclass
from typing import Optional

from src.domain.entities.currency import Currency


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
