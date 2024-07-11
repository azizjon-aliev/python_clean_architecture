import random
from http import HTTPMethod, HTTPStatus

from automapper import mapper
from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from src.interactor.dtos.account_dtos import RegisterStep1InputDto
from src.interactor.use_cases.account import RegisterStep1UseCase
from src.presentation.rest_api.apps.account.serializers import (
    RegisterStep1RequestSerializer,
    RegisterStep1ResponseSerializer,
)
from src.presentation.rest_api.config.containers import container


class RegisterAPIView(ViewSet):
    authentication_classes = ()

    @extend_schema(
        request=RegisterStep1RequestSerializer,
        responses={HTTPStatus.CREATED: RegisterStep1ResponseSerializer},
        methods=[HTTPMethod.POST],
    )
    def step1(self, request: Request) -> Response:
        # request
        serializer = RegisterStep1RequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp = random.randint(1000, 9999)

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
            data=RegisterStep1ResponseSerializer(result).data,
            status=status.HTTP_201_CREATED,
        )
