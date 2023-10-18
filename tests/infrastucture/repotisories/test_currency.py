import pytest
from src.domain.entities.currency import Currency
from src.infrastructure.repotisories.currency_repository import CurrencyRepository

from tests.infrastucture.factories.currency_factory import CurrencyFactory

repository = CurrencyRepository()


@pytest.mark.django_db
def test_get_currency_repository():
    currency = CurrencyFactory.create()
    response: Currency = repository.get(currency_id=currency.pk)

    assert isinstance(response, Currency)
    assert response.code == currency.code
    assert response.name == currency.name
    assert response.symbol == currency.symbol


@pytest.mark.django_db
def test_create_currency_repository():
    data = {
        "code": "USD",
        "name": "Dollar",
        "symbol": "$",
    }

    response: Currency = repository.create(**data)

    assert isinstance(response, Currency)
    assert response.code == data.get("code")
    assert response.name == data.get("name")
    assert response.symbol == data.get("symbol")


@pytest.mark.django_db
def test_update_currency_repository():
    currency_old = CurrencyFactory.create()
    data = {
        "code": "USD",
        "name": "Dollar",
        "symbol": "$",
    }

    response: Currency = repository.update(currency_id=currency_old.pk, **data)

    assert isinstance(response, Currency)
    assert response.code == data.get("code")
    assert response.name == data.get("name")
    assert response.symbol == data.get("symbol")


@pytest.mark.django_db
def test_delete_currency_repository():
    currency = CurrencyFactory.create()
    repository.delete(currency_id=currency.pk)

    assert repository.exists(pk=currency.pk) is False
