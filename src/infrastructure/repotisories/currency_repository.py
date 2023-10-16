import os
import django
from dotenv import load_dotenv
from src.domain.entities.currency import Currency
from src.domain.value_objects import CurrencyId
from src.interactor.errors.error_classes import EntityDoesNotExist
from src.interactor.interfaces.repotisories.currency_repository import CurrencyRepositoryInterface

load_dotenv()
settings_module = f"src.application.config.settings.{os.getenv('DJANGO_ENV')}"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

django.setup()

from src.infrastructure.models import Currency as CurrencyModel


class CurrencyRepository(CurrencyRepositoryInterface):

    @staticmethod
    def __decode_model(instance: CurrencyModel) -> Currency:
        return Currency(
            currency_id=instance.pk,
            code=instance.code,
            name=instance.name,
            symbol=instance.symbol
        )

    def exists(self, **kwargs) -> bool:
        if CurrencyModel.objects.filter(**kwargs).exists():
            return True
        else:
            return False

    def get(self, currency_id: CurrencyId) -> Currency:
        instance = CurrencyModel.objects.filter(pk=currency_id).first()

        if not instance:
            raise Exception("currency does not exists")
        return self.__decode_model(instance)

    def create(self, code: str, name: str, symbol: str) -> Currency:
        instance = CurrencyModel(
            code=code,
            name=name,
            symbol=symbol
        )
        instance.save()
        return self.__decode_model(instance)

    def update(self, currency_id: CurrencyId, code: str, name: str, symbol: str) -> Currency:
        instance = CurrencyModel.objects.filter(pk=currency_id).first()

        if not instance:
            raise EntityDoesNotExist(f'Currency id {currency_id} not found')

        data = {
            "code": code,
            "symbol": symbol,
            "name": name
        }

        for field, value in data.items():
            if value is not None:
                setattr(instance, field, value)
        instance.save()

        return self.__decode_model(instance)
