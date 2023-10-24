from dataclasses import asdict, dataclass
from typing import Optional

from src.domain.value_objects import RegionId


@dataclass
class Region:
    region_id: RegionId
    name: str
    parent: Optional["Region"]

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return asdict(self)
