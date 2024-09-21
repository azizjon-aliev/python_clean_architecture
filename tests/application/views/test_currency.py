import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from tests.infrastructure.factories.currency_factory import CurrencyFactory

client = APIClient()


@pytest.mark.django_db
def test_list_currency_api_view() -> None:
    currency_count = 10
    CurrencyFactory.create_batch(currency_count)

    params = {
        "skip": 0,
        "limit": 5,
    }
    response = client.get(path=reverse("currency-list"), data=params, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == params.get("limit")


@pytest.mark.django_db
def test_retrieve_currency_api_view() -> None:
    currency = CurrencyFactory()
    response = client.get(
        path=reverse("currency-detail", kwargs={"pk": currency.id}), format="json"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("code") == currency.code
    assert response.data.get("name") == currency.name
    assert response.data.get("symbol") == currency.symbol


@pytest.mark.django_db
def test_create_currency_api_view() -> None:
    data = {
        "code": "USD",
        "name": "US Dollar",
        "symbol": "$",
    }
    response = client.post(path=reverse("currency-list"), data=data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data.get("code") == data.get("code")
    assert response.data.get("name") == data.get("name")
    assert response.data.get("symbol") == data.get("symbol")


@pytest.mark.django_db
def test_update_currency_api_view() -> None:
    currency = CurrencyFactory()
    data = {
        "code": "EUR",
        "name": "Euro",
        "symbol": "€",
    }
    response = client.patch(
        path=reverse("currency-detail", kwargs={"pk": currency.id}),
        data=data,
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("code") == data.get("code")
    assert response.data.get("name") == data.get("name")
    assert response.data.get("symbol") == data.get("symbol")


@pytest.mark.django_db
def test_delete_currency_api_view() -> None:
    currency = CurrencyFactory()
    response = client.delete(
        path=reverse("currency-detail", kwargs={"pk": currency.id}), format="json"
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
