from src.domain.entities.currency import Currency
from src.domain.value_objects import CurrencyId
from src.interface.repotisories.currency_repository import CurrencyRepositoryInterface
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
            raise Exception("currency does not exists")

        instance.code = code
        instance.name = name
        instance.symbol = symbol
        instance.save()

        return self.__decode_model(instance)
