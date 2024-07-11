from automapper import mapper

from src.application.currency.responses.currency_vm import CurrencyVm
from src.infrastructure.models import Currency

mapper.add(CurrencyVm, Currency, fields_mapping={"id": "Currency.id"})
