from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from src.application.interfaces.account_view import RegisterViewInterface
from src.application.presenters.currency_presenter import (
    CreateCurrencyPresenter,
)
from src.application.serializers.account import RegisterStep1RequestSerializer
from src.application.serializers.currency import (
    CreateCurrencyRequestSerializer,
    CreateCurrencyResponseSerializer,
)
from src.infrastructure.loggers.logger_default import LoggerDefault
from src.infrastructure.repotisories.currency_repository import CurrencyRepository
from src.interactor.dtos.currency_dtos import (
    CreateCurrencyInputDto,
)
from src.interactor.use_cases.currency import (
    CreateCurrencyUseCase,
)


class RegisterAPIView(ViewSet, RegisterViewInterface):
    authentication_classes = ()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = CurrencyRepository()
        self.logger = LoggerDefault()

    @extend_schema(
        request=RegisterStep1RequestSerializer,
        responses={201: CreateCurrencyResponseSerializer},
        methods=["POST"],
    )
    def step1(self, request: Request) -> Response:
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
        request=CreateCurrencyRequestSerializer,
        responses={200: CreateCurrencyResponseSerializer},
        methods=["POST"],
    )
    def step2(self, request: Request) -> Response:
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
