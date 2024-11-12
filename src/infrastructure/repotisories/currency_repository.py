import os
from typing import List

import django
from dotenv import load_dotenv

from src.domain.entities.currency import Currency
from src.domain.value_objects import CurrencyId
from src.interactor.errors.error_classes import EntityDoesNotExist
from src.interactor.interfaces.repotisories.currency_repository import (
    CurrencyRepositoryInterface,
)

load_dotenv()
settings_module = f"src.application.config.settings.{os.getenv('DJANGO_ENV')}"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

django.setup()

from src.infrastructure.models import Currency as CurrencyModel  # noqa: E402


class CurrencyRepository(CurrencyRepositoryInterface):
    @staticmethod
    def __decode_model(instance: CurrencyModel) -> Currency:
        return Currency(
            currency_id=instance.pk,
            code=instance.code,
            name=instance.name,
            symbol=instance.symbol,
        )

    def exists(self, **kwargs) -> bool:
        return bool(CurrencyModel.objects.filter(**kwargs).exists())

    def count(self) -> int:
        return CurrencyModel.objects.count()

    def delete(self, currency_id: CurrencyId) -> None:
        instance = CurrencyModel.objects.filter(pk=currency_id).first()

        if not instance:
            raise Exception("currency does not exists")

        instance.delete()

    def list(self, skip: int = 0, limit: int = 100) -> List[Currency]:
        currency_models = CurrencyModel.objects.all()[skip : skip + limit]
        return [self.__decode_model(instance) for instance in currency_models]

    def get(self, currency_id: CurrencyId) -> Currency:
        instance = CurrencyModel.objects.filter(pk=currency_id).first()

        if not instance:
            raise Exception("currency does not exists")
        return self.__decode_model(instance)

    def create(self, code: str, name: str, symbol: str) -> Currency:
        instance = CurrencyModel(code=code, name=name, symbol=symbol)
        instance.save()
        return self.__decode_model(instance)

    def update(
        self, currency_id: CurrencyId, code: str, name: str, symbol: str
    ) -> Currency:
        instance = CurrencyModel.objects.filter(pk=currency_id).first()

        if not instance:
            raise EntityDoesNotExist(f"Currency id {currency_id} not found")

        data = {"code": code, "symbol": symbol, "name": name}

        for field, value in data.items():
            if value is not None:
                setattr(instance, field, value)
        instance.save()

        return self.__decode_model(instance)
