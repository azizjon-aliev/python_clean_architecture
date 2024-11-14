import re
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Optional

from src.domain.value_objects import UserId


@dataclass
class User:
    user_id: UserId
    email: str | None
    phone: str
    password: str

    is_staff: bool | None
    is_active: bool | None
    is_superuser: bool | None
    date_joined: datetime | None
    otp: int | None
    is_verified: bool | None
    role: str
    company: str | None

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
    def check_phone_number(phone: str) -> bool:
        return bool(re.match(r"^992\d{9}$", phone))

    @staticmethod
    def check_password(password: str) -> bool:
        return bool(re.match(r"^[!-~]+$", password))
