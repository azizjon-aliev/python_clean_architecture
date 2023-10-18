import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_list_currency_api_view():
    client = APIClient()
    url = reverse('currency-list')

    response = client.get(url, format='json')

    print(response)