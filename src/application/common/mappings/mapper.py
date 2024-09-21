from automapper import mapper

from src.application.authentication.responses.user_vm import UserVm
from src.application.currency.responses.currency_vm import CurrencyVm
from src.infrastructure.models import Currency, User

mapper.add(CurrencyVm, Currency, fields_mapping={"id": "Currency.id"})
mapper.add(UserVm, User, fields_mapping={"id": "User.id"})
