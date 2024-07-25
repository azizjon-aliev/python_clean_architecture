import re
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Optional

from src.domain.value_objects import UserId


@dataclass
class User:
    user_id: UserId
    email: str
    username: str
    password: str

    is_staff: Optional[bool]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    date_joined: Optional[datetime]

    created_by: Optional["User"]
    updated_by: Optional["User"]
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def check_password(password: str) -> bool:
        return bool(re.match(r"^[!-~]+$", password))
