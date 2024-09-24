from dataclasses import asdict, dataclass

from src.domain.value_objects import CurrencyId


@dataclass
class Currency:
    id: CurrencyId
    code: str
    name: str
    symbol: str

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return asdict(self)
