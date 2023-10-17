from typing import Optional

from drf_spectacular.utils import OpenApiParameter, extend_schema

from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from src.application.interfaces.currency_view import CurrencyViewInterface
from src.application.presenters.currency_presenter import (
    CreateCurrencyPresenter,
    DetailCurrencyPresenter,
    ListCurrencyPresenter,
    UpdateCurrencyPresenter,
)
from src.application.serializers.core import NotFoundResponseSerializer
from src.application.serializers.currency import (
    CreateCurrencyRequestSerializer,
    CreateCurrencyResponseSerializer,
    DetailCurrencyResponseSerializer,
    ListCurrencyResponseSerializer,
    UpdateCurrencyRequestSerializer,
    UpdateCurrencyResponseSerializer,
)
from src.domain.value_objects import CurrencyId
from src.infrastructure.loggers.logger_default import LoggerDefault
from src.infrastructure.repotisories.currency_repository import CurrencyRepository
from src.interactor.dtos.currency_dtos import (
    CreateCurrencyInputDto,
    ListCurrencyInputDto,
    UpdateCurrencyInputDto,
)
from src.interactor.errors.error_classes import EntityDoesNotExist
from src.interactor.use_cases.currency import (
    CreateCurrencyUseCase,
    DeleteCurrencyUseCase,
    DetailCurrencyUseCase,
    ListCurrencyUseCase,
    UpdateCurrencyUseCase,
)


class CurrencyAPIView(ViewSet, CurrencyViewInterface):
    authentication_classes = ()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = CurrencyRepository()
        self.logger = LoggerDefault()

    @extend_schema(
        responses={200: ListCurrencyResponseSerializer},
        methods=["GET"],
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
    )
    def list(self, request: Request) -> Response:
        # request
        parameters = {
            "skip": int(request.query_params.get("skip", 0)),
            "limit": int(request.query_params.get("limit", 100)),
        }

        # logic
        use_case = ListCurrencyUseCase(
            presenter=ListCurrencyPresenter(),
            repository=self.repository,
            logger=self.logger,
        )
        input_dto = ListCurrencyInputDto(**parameters)
        result = use_case.execute(input_dto)

        # response
        return Response(
            data=ListCurrencyResponseSerializer(result).data, status=status.HTTP_200_OK
        )

    @extend_schema(
        responses={
            200: DetailCurrencyResponseSerializer,
            404: NotFoundResponseSerializer,
        },
        methods=["GET"],
        parameters=[OpenApiParameter("id", CurrencyId, OpenApiParameter.PATH)],
    )
    def retrieve(self, request: Request, pk: Optional[CurrencyId]) -> Response:
        # logic
        try:
            use_case = DetailCurrencyUseCase(
                presenter=DetailCurrencyPresenter(),
                repository=self.repository,
                logger=self.logger,
            )
            result = use_case.execute(pk)
        except EntityDoesNotExist:
            raise Http404()

        # response
        return Response(
            data=DetailCurrencyResponseSerializer(result).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        request=CreateCurrencyRequestSerializer,
        responses={201: CreateCurrencyResponseSerializer},
        methods=["POST"],
    )
    def create(self, request: Request) -> Response:
        # request
        serializer = CreateCurrencyRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # logic
        use_case = CreateCurrencyUseCase(
            presenter=CreateCurrencyPresenter(),
            repository=self.repository,
            logger=self.logger,
        )
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
            200: UpdateCurrencyResponseSerializer,
            404: NotFoundResponseSerializer,
        },
        methods=["PATCH"],
        parameters=[OpenApiParameter("id", CurrencyId, OpenApiParameter.PATH)],
    )
    def partial_update(self, request: Request, pk: Optional[CurrencyId]) -> Response:
        # request
        serializer = UpdateCurrencyRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # logic
        try:
            use_case = UpdateCurrencyUseCase(
                presenter=UpdateCurrencyPresenter(),
                repository=self.repository,
                logger=self.logger,
            )
            input_dto = UpdateCurrencyInputDto(**serializer.data)
            result = use_case.execute(pk, input_dto)
        except EntityDoesNotExist:
            raise Http404()

        # response
        return Response(
            data=UpdateCurrencyResponseSerializer(result).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        responses={
            204: None,
            404: NotFoundResponseSerializer,
        },
        methods=["DELETE"],
        parameters=[OpenApiParameter("id", CurrencyId, OpenApiParameter.PATH)],
    )
    def destroy(self, request: Request, pk: Optional[CurrencyId]) -> Response:
        # logic
        try:
            use_case = DeleteCurrencyUseCase(
                repository=self.repository,
                logger=self.logger,
            )
            use_case.execute(pk)
        except EntityDoesNotExist:
            raise Http404()

        return Response(data=None, status=status.HTTP_204_NO_CONTENT)
