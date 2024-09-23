from src.presentation.rest_api.apps.common.views import BaseAPIView
from src.domain.value_objects import CurrencyId
from src.application.currency.commands.add_currency.add_currency_command import (
    AddCurrencyCommand,
)
from src.application.currency.commands.edit_currency.edit_currency_command import (
    EditCurrencyCommand,
)
from src.application.currency.commands.remove_currency.remove_currency_command import (
    RemoveCurrencyCommand,
)
from src.application.currency.queries.get_currencies_list.get_currencies_list_query import (
    GetCurrenciesListQuery,
)
from src.application.currency.queries.get_currency_detail.get_currency_detail_query import (
    GetCurrencyDetailQuery,
)
from src.presentation.rest_api.apps.currency.serializers import (
    CreateCurrencyRequestSerializer,
    DetailCurrencyResponseSerializer,
    ListCurrencyResponseSerializer,
    UpdateCurrencyRequestSerializer,
)


class CurrencyAPIView(
    BaseAPIView[
        ListCurrencyResponseSerializer,
        DetailCurrencyResponseSerializer,
        CreateCurrencyRequestSerializer,
        UpdateCurrencyRequestSerializer,
        GetCurrenciesListQuery,
        GetCurrencyDetailQuery,
        AddCurrencyCommand,
        EditCurrencyCommand,
        RemoveCurrencyCommand,
        CurrencyId,
    ]
):
    authentication_classes = ()
    list_serializer = ListCurrencyResponseSerializer
    detail_serializer = DetailCurrencyResponseSerializer
    create_serializer = CreateCurrencyRequestSerializer
    update_serializer = UpdateCurrencyRequestSerializer
    list_query = GetCurrenciesListQuery
    detail_query = GetCurrencyDetailQuery
    create_command = AddCurrencyCommand
    update_command = EditCurrencyCommand
    remove_command = RemoveCurrencyCommand
    pk_type = CurrencyId
