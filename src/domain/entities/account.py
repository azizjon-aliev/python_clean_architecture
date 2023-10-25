from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Optional

from django.utils import timezone
from src.domain.value_objects import UserId


@dataclass
class User:
    user_id: UserId
    email: Optional[str]
    phone: str
    password: str

    is_staff: Optional[bool]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    date_joined: Optional[datetime]
    otp: Optional[int]
    is_verified: Optional[bool]
    role: str
    company: Optional[str]

    created_by: Optional["User"]
    updated_by: Optional["User"]
    created_at: datetime = timezone.now
    updated_at: datetime = timezone.now

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return asdict(self)
