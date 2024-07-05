from dataclasses import dataclass
from typing import Optional

from src.domain.entities.account import User


@dataclass
class RegisterStep1InputDto:
    username: str
    email: str
    otp: int
    password: str


@dataclass
class RegisterStep1OutputDto:
    user: User
