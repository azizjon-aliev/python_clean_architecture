from http import HTTPMethod, HTTPStatus
from typing import Optional

from automapper import Mapper
from drf_spectacular.utils import OpenApiParameter, extend_schema
from mediatr import Mediator

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
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
from src.application.interfaces.currency_view import CurrencyViewInterface
from src.domain.value_objects import CurrencyId
from src.presentation.rest_api.apps.common.serializers import NotFoundResponseSerializer
from src.presentation.rest_api.apps.currency.serializers import (
    CreateCurrencyRequestSerializer,
    DetailCurrencyResponseSerializer,
    ListCurrencyResponseSerializer,
    UpdateCurrencyRequestSerializer,
)
from src.presentation.rest_api.config.containers import container


class CurrencyAPIView(ViewSet, CurrencyViewInterface):
    authentication_classes = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__mediator = container.resolve(Mediator)
        self.__mapper = container.resolve(Mapper)

    @extend_schema(
        methods=[HTTPMethod.GET],
        parameters=[
            OpenApiParameter(
                "skip",
                int,
                OpenApiParameter.QUERY,
                description="Number of items to skip.",
            ),
            OpenApiParameter(
                "limit",
                int,
                OpenApiParameter.QUERY,
                description="Maximum number of items to retrieve.",
            ),
        ],
        responses=ListCurrencyResponseSerializer,
    )
    def list(self, request: Request) -> Response:
        parameters = {
            "skip": int(request.query_params.get("skip", 0)),
            "limit": int(request.query_params.get("limit", 100)),
        }

        query = GetCurrenciesListQuery(**parameters)
        result = self.__mediator.send(query)

        return Response(
            data=ListCurrencyResponseSerializer(result, many=True).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        methods=[HTTPMethod.GET],
        parameters=[OpenApiParameter("id", CurrencyId, OpenApiParameter.PATH)],
        responses={
            HTTPStatus.OK: DetailCurrencyResponseSerializer,
            HTTPStatus.NOT_FOUND: NotFoundResponseSerializer,
        },
    )
    def retrieve(self, request: Request, pk: Optional[CurrencyId]) -> Response:
        query = GetCurrencyDetailQuery(id=pk)
        result = self.__mediator.send(query)

        return Response(
            data=DetailCurrencyResponseSerializer(result).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        request=CreateCurrencyRequestSerializer,
        responses={HTTPStatus.CREATED: DetailCurrencyResponseSerializer},
        methods=[HTTPMethod.POST],
    )
    def create(self, request: Request) -> Response:
        command = self.__mapper.to(AddCurrencyCommand).map(request.data)
        result = self.__mediator.send(command)

        return Response(
            data=DetailCurrencyResponseSerializer(result).data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        request=UpdateCurrencyRequestSerializer,
        responses={
            HTTPStatus.OK: DetailCurrencyResponseSerializer,
            HTTPStatus.NOT_FOUND: NotFoundResponseSerializer,
        },
        methods=[HTTPMethod.PATCH],
        parameters=[OpenApiParameter("id", CurrencyId, OpenApiParameter.PATH)],
    )
    def partial_update(self, request: Request, pk: Optional[CurrencyId]) -> Response:
        command = self.__mapper.to(EditCurrencyCommand).map(
            request.data, fields_mapping={"id": pk}
        )
        result = self.__mediator.send(command)

        return Response(
            data=DetailCurrencyResponseSerializer(result).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        methods=[HTTPMethod.DELETE],
        parameters=[OpenApiParameter("id", CurrencyId, OpenApiParameter.PATH)],
        responses={
            HTTPStatus.NO_CONTENT: None,
            HTTPStatus.NOT_FOUND: NotFoundResponseSerializer,
        },
    )
    def destroy(self, request: Request, pk: Optional[CurrencyId]) -> Response:
        command = RemoveCurrencyCommand(id=pk)
        result = self.__mediator.send(command)
        return Response(data=result, status=status.HTTP_204_NO_CONTENT)
