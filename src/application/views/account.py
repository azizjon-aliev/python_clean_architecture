from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from src.application.interfaces.account_view import RegisterViewInterface
from src.application.presenters.account_presenter import RegisterStep1Presenter
from src.application.serializers.account import (
    RegisterStep1RequestSerializer,
    RegisterStep1ResponseSerializer,
)
from src.infrastructure.loggers.logger_default import LoggerDefault
from src.infrastructure.repotisories.account_repository import UserRepository
from src.interactor.dtos.account_dtos import RegisterStep1InputDto
from src.interactor.use_cases.account import RegisterStep1UseCase
from src.interactor.use_cases.notification import send_sms_notification, generate_otp


class RegisterAPIView(ViewSet, RegisterViewInterface):
    authentication_classes = ()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = UserRepository()
        self.logger = LoggerDefault()

    @extend_schema(
        request=RegisterStep1RequestSerializer,
        responses={201: RegisterStep1ResponseSerializer},
        methods=["POST"],
    )
    def step1(self, request: Request) -> Response:
        # request
        serializer = RegisterStep1RequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp = generate_otp()

        # logic
        input_dto = RegisterStep1InputDto(
            phone=serializer.data.get("phone"),
            email=serializer.data.get("email"),
            otp=otp,
            password=serializer.data.get("password"),
        )
        use_case = RegisterStep1UseCase(
            presenter=RegisterStep1Presenter(),
            repository=self.repository,
            logger=self.logger,
        )
        result = use_case.execute(input_dto)
        print(send_sms_notification(phone=input_dto.phone, message=f"Ваш код подтверждения - {otp}"))
        self.logger.log_info("Send sms notification with otp success")

        # response
        return Response(
            data=RegisterStep1ResponseSerializer(result).data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        request=RegisterStep1RequestSerializer,
        responses={201: RegisterStep1ResponseSerializer},
        methods=["POST"],
    )
    def step2(self, request: Request) -> Response:
        # request
        serializer = RegisterStep1RequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # logic
        input_dto = RegisterStep1InputDto(
            phone=serializer.phone,
            email=serializer.email,
            password=serializer.password,
        )
        use_case = RegisterStep1UseCase(
            presenter=RegisterStep1Presenter(),
            repository=self.repository,
            logger=self.logger,
        )
        result = use_case.execute(input_dto)

        # response
        return Response(
            data=RegisterStep1ResponseSerializer(result).data,
            status=status.HTTP_201_CREATED,
        )
