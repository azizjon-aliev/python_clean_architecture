from dataclasses import dataclass


@dataclass
class GetCurrenciesListQuery:
    skip: int = 0
    limit: int = 100
