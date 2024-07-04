from src.domain.entities.currency import Currency
from src.domain.value_objects import CurrencyId
from src.infrastructure.models import Currency as CurrencyModel
from src.infrastructure.repositories.base_repository import AbstractRepository
from src.interactor.interfaces.repositories.currency_repository import CurrencyRepositoryInterface

class CurrencyRepository(AbstractRepository[CurrencyModel, CurrencyId], CurrencyRepositoryInterface):

    model = CurrencyModel

    def _decode_model(self, instance: CurrencyModel) -> Currency:
        return Currency(
            currency_id=instance.pk,
            code=instance.code,
            name=instance.name,
            symbol=instance.symbol,
        )
