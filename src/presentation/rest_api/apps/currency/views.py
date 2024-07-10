from http import HTTPMethod, HTTPStatus
from typing import Optional

from drf_spectacular.utils import OpenApiParameter, extend_schema
from mediatr import Mediator

from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from src.application.currency.queries.get_currencies_list.get_currencies_list_query import (
    GetCurrenciesListQuery,
)
from src.application.currency.queries.get_currency_detail.get_currency_detail_query import (
    GetCurrencyDetailQuery,
)
from src.application.interfaces.currency_view import CurrencyViewInterface
from src.domain.value_objects import CurrencyId
from src.interactor.dtos.currency_dtos import (
    CreateCurrencyInputDto,
    UpdateCurrencyInputDto,
)
from src.interactor.errors.error_classes import EntityDoesNotExist
from src.interactor.use_cases.currency import (
    CreateCurrencyUseCase,
    DeleteCurrencyUseCase,
    UpdateCurrencyUseCase,
)
from src.presentation.rest_api.apps.common.serializers import NotFoundResponseSerializer
from src.presentation.rest_api.apps.currency.serializers import (
    CreateCurrencyRequestSerializer,
    CreateCurrencyResponseSerializer,
    DetailCurrencyResponseSerializer,
    ListCurrencyResponseSerializer,
    UpdateCurrencyRequestSerializer,
    UpdateCurrencyResponseSerializer,
)
from src.presentation.rest_api.config.containers import container


class CurrencyAPIView(ViewSet, CurrencyViewInterface):
    authentication_classes = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__mediator = container.resolve(Mediator)

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
        responses={HTTPStatus.CREATED: CreateCurrencyResponseSerializer},
        methods=[HTTPMethod.POST],
    )
    def create(self, request: Request) -> Response:
        # request
        serializer = CreateCurrencyRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # logic
        use_case = container.resolve(CreateCurrencyUseCase)
        input_dto = CreateCurrencyInputDto(**serializer.data)
        result = use_case.execute(input_dto)

        # response
        return Response(
            data=CreateCurrencyResponseSerializer(result).data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        request=UpdateCurrencyRequestSerializer,
        responses={
            HTTPStatus.OK: UpdateCurrencyResponseSerializer,
            HTTPStatus.NOT_FOUND: NotFoundResponseSerializer,
        },
        methods=[HTTPMethod.PATCH],
        parameters=[OpenApiParameter("id", CurrencyId, OpenApiParameter.PATH)],
    )
    def partial_update(self, request: Request, pk: Optional[CurrencyId]) -> Response:
        # request
        serializer = UpdateCurrencyRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # logic
        try:
            use_case = container.resolve(UpdateCurrencyUseCase)
            input_dto = UpdateCurrencyInputDto(**serializer.data)
            result = use_case.execute(pk, input_dto)
        except EntityDoesNotExist as e:
            raise Http404() from e

        # response
        return Response(
            data=UpdateCurrencyResponseSerializer(result).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        responses={
            HTTPStatus.NO_CONTENT: None,
            HTTPStatus.NOT_FOUND: NotFoundResponseSerializer,
        },
        methods=[HTTPMethod.DELETE],
        parameters=[OpenApiParameter("id", CurrencyId, OpenApiParameter.PATH)],
    )
    def destroy(self, request: Request, pk: Optional[CurrencyId]) -> Response:
        # logic
        try:
            use_case = container.resolve(DeleteCurrencyUseCase)
            use_case.execute(pk)
        except EntityDoesNotExist as e:
            raise Http404() from e

        return Response(data=None, status=status.HTTP_204_NO_CONTENT)
