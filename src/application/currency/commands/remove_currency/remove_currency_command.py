from dataclasses import dataclass

from mediatr import GenericQuery

from src.domain.value_objects import CurrencyId


@dataclass
class RemoveCurrencyCommand(GenericQuery[None]):
    id: CurrencyId
