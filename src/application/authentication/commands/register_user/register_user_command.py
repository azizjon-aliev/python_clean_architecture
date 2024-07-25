from dataclasses import dataclass
from typing import Optional

from mediatr import GenericQuery

from src.application.currency.responses.currency_detail_vm import CurrencyDetailVm


@dataclass
class RegisterUserCommand(GenericQuery[CurrencyDetailVm]):
    username: str
    email: Optional[str]
    password: str
    password_confirmation: str
