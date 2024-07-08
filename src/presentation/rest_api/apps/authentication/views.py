from http import HTTPMethod, HTTPStatus

from automapper import mapper
from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from src.application.interfaces.authentication_view import (
    AuthViewInterface,
)
from src.interactor.dtos.authentication_dtos import (
    RegisterStep1InputDto,
    LoginInputDto,
)
from src.interactor.use_cases.authentication import (
    RefreshTokenUseCase,
    RegisterStep1UseCase,
    LoginUseCase,
)
from src.interactor.use_cases.notification import generate_otp
from src.presentation.rest_api.apps.authentication.serializers import (
    RefreshTokenRequestSerializer,
    RegisterStep1RequestSerializer,
    LoginRequestSerializer,
    TokenResponseSerializer,
)
from src.presentation.rest_api.config.containers import container


class AuthAPIView(ViewSet, AuthViewInterface):
    authentication_classes = ()

    @extend_schema(
        request=RegisterStep1RequestSerializer,
        responses={HTTPStatus.CREATED: TokenResponseSerializer},
        methods=[HTTPMethod.POST],
    )
    def step1(self, request: Request) -> Response:
        # request
        serializer = RegisterStep1RequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp = generate_otp()

        # logic
        input_dto = mapper.to(RegisterStep1InputDto).map(
            serializer.data,
            fields_mapping={
                "otp": otp,
            },
        )
        use_case = container.resolve(RegisterStep1UseCase)
        result = use_case.execute(input_dto)

        # response
        return Response(
            data=TokenResponseSerializer(result).data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        request=LoginRequestSerializer,
        responses={HTTPStatus.OK: TokenResponseSerializer},
        methods=[HTTPMethod.POST],
    )
    def login(self, request: Request) -> Response:
        # request
        serializer = LoginRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # logic
        use_case = container.resolve(LoginUseCase)
        input_dto = LoginInputDto(**serializer.validated_data)
        result = use_case.execute(input_dto)

        # response
        return Response(
            data=TokenResponseSerializer(result).data,
            status=status.HTTP_200_OK
        )

    @extend_schema(
        request=RefreshTokenRequestSerializer,
        responses={HTTPStatus.OK: TokenResponseSerializer},
        methods=[HTTPMethod.POST],
    )
    def refresh_token(self, request: Request) -> Response:
        # request
        serializer = RefreshTokenRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # logic
        use_case = container.resolve(RefreshTokenUseCase)
        refresh_token = serializer.validated_data['refresh_token']

        # response
        result = use_case.execute(refresh_token)
        return Response(
            data=TokenResponseSerializer(result).data,
            status=status.HTTP_200_OK
        )
