from dataclasses import dataclass
from typing import List

from mediatr import GenericQuery

from src.domain.entities.currency import Currency


@dataclass
class GetCurrenciesListQuery(GenericQuery[List[Currency]]):
    skip: int = 0
    limit: int = 100
