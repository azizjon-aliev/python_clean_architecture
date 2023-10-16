from typing import Optional

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from src.application.interfaces.currency_view import CurrencyViewInterface
from src.application.presenters.currency_presenter import CreateCurrencyPresenter, UpdateCurrencyPresenter
from src.application.serializers.currency import CreateCurrencyRequestSerializer, CreateCurrencyResponseSerializer, \
    UpdateCurrencyRequestSerializer, UpdateCurrencyResponseSerializer
from src.domain.value_objects import CurrencyId
from src.infrastructure.loggers.logger_default import LoggerDefault
from rest_framework.viewsets import ViewSet
from src.infrastructure.repotisories.currency_repository import CurrencyRepository
from src.interactor.dtos.currency_dtos import CreateCurrencyInputDto, UpdateCurrencyInputDto
from src.interactor.use_cases.currency import CreateCurrencyUseCase, UpdateCurrencyUseCase


class CurrencyAPIView(ViewSet, CurrencyViewInterface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = CurrencyRepository()
        self.logger = LoggerDefault()

    @extend_schema(
        request=CreateCurrencyRequestSerializer,
        responses={201: CreateCurrencyResponseSerializer},
        methods=["POST"]
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
            status=status.HTTP_201_CREATED
        )

    @extend_schema(
        request=UpdateCurrencyRequestSerializer,
        responses={200: UpdateCurrencyResponseSerializer},
        methods=["PATCH"],
        parameters=[
            OpenApiParameter("id", CurrencyId, OpenApiParameter.PATH)
        ]
    )
    def partial_update(self, request: Request, pk: Optional[CurrencyId]) -> Response:
        # request
        serializer = UpdateCurrencyRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # logic
        use_case = UpdateCurrencyUseCase(
            presenter=UpdateCurrencyPresenter(),
            repository=self.repository,
            logger=self.logger,
        )
        input_dto = UpdateCurrencyInputDto(**serializer.data)
        result = use_case.execute(pk, input_dto)

        # response
        return Response(
            data=UpdateCurrencyResponseSerializer(result).data,
            status=status.HTTP_200_OK
        )
