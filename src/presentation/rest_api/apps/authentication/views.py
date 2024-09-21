from http import HTTPMethod, HTTPStatus

from automapper import Mapper
from drf_spectacular.utils import extend_schema
from mediatr import Mediator

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from src.application.authentication.commands.register_user.register_user_command import (
    RegisterUserCommand,
)
from src.application.authentication.queries.login_user.login_user_query import (
    LoginUserQuery,
)
from src.application.authentication.queries.refresh_token.refresh_token_query import (
    RefreshTokenQuery,
)
from src.presentation.rest_api.apps.authentication.serializers import (
    LoginRequestSerializer,
    RefreshTokenRequestSerializer,
    RegisterRequestSerializer,
    TokenResponseSerializer,
)
from src.presentation.rest_api.config.containers import container


class AuthAPIView(ViewSet):
    authentication_classes = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__mediator = container.resolve(Mediator)
        self.__mapper = container.resolve(Mapper)

    @extend_schema(
        request=RegisterRequestSerializer,
        responses={HTTPStatus.CREATED: TokenResponseSerializer},
        methods=[HTTPMethod.POST],
    )
    def register(self, request: Request) -> Response:
        command = self.__mapper.to(RegisterUserCommand).map(request.data)
        result = self.__mediator.send(command)

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
        command = self.__mapper.to(LoginUserQuery).map(request.data)
        result = self.__mediator.send(command)

        return Response(
            data=TokenResponseSerializer(result).data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        request=RefreshTokenRequestSerializer,
        responses={HTTPStatus.OK: TokenResponseSerializer},
        methods=[HTTPMethod.POST],
    )
    def refresh_token(self, request: Request) -> Response:
        command = self.__mapper.to(RefreshTokenQuery).map(request.data)
        result = self.__mediator.send(command)

        return Response(
            data=TokenResponseSerializer(result).data,
            status=status.HTTP_201_CREATED,
        )
