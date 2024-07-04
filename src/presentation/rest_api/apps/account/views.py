from http import HTTPMethod, HTTPStatus

from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from src.application.interfaces.account_view import RegisterViewInterface
from src.infrastructure.loggers.logger_default import LoggerDefault
from src.infrastructure.repositories.account_repository import UserRepository
from src.interactor.dtos.account_dtos import RegisterStep1InputDto
from src.interactor.use_cases.account import RegisterStep1UseCase
from src.interactor.use_cases.notification import generate_otp, send_sms_notification
from src.presentation.rest_api.apps.account.serializers import (
    RegisterStep1RequestSerializer,
    RegisterStep1ResponseSerializer,
)
from src.presentation.rest_api.config.containers import container


class RegisterAPIView(ViewSet, RegisterViewInterface):
    authentication_classes = ()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = UserRepository()
        self.logger = LoggerDefault()

    @extend_schema(
        request=RegisterStep1RequestSerializer,
        responses={HTTPStatus.CREATED: RegisterStep1ResponseSerializer},
        methods=[HTTPMethod.POST],
    )
    def step1(self, request: Request) -> Response:
        # request
        serializer = RegisterStep1RequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp = generate_otp()

        # logic
        input_dto = RegisterStep1InputDto(
            username=serializer.data.get("username"),
            email=serializer.data.get("email"),
            otp=otp,
            password=serializer.data.get("password"),
        )
        use_case = container.resolve(RegisterStep1UseCase)
        result = use_case.execute(input_dto)
        print(
            send_sms_notification(
                username=input_dto.username, message=f"Your confirmation code - {otp}"
            )
        )
        self.logger.log_info("Send sms notification with otp success")

        # response
        return Response(
            data=RegisterStep1ResponseSerializer(result).data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        request=RegisterStep1RequestSerializer,
        responses={HTTPStatus.CREATED: RegisterStep1ResponseSerializer},
        methods=[HTTPMethod.POST],
    )
    def step2(self, request: Request) -> Response:
        # request
        serializer = RegisterStep1RequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # logic
        input_dto = RegisterStep1InputDto(
            username=serializer.username,
            email=serializer.email,
            password=serializer.password,
        )
        use_case = container.resolve(RegisterStep1UseCase)
        result = use_case.execute(input_dto)

        # response
        return Response(
            data=RegisterStep1ResponseSerializer(result).data,
            status=status.HTTP_201_CREATED,
        )
