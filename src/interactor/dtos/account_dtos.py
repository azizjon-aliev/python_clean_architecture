from dataclasses import dataclass
from typing import Optional

from src.domain.entities.account import User


@dataclass
class RegisterStep1InputDto:
    phone: str
    email: Optional[str]
    otp: int
    password: str


@dataclass
class RegisterStep1OutputDto:
    user: User
