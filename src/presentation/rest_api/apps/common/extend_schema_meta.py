from http import HTTPMethod, HTTPStatus
from typing import Any

from drf_spectacular.utils import OpenApiParameter, extend_schema

from rest_framework.request import Request
from src.presentation.rest_api.apps.common.serializers import NotFoundResponseSerializer


class ExtendSchemaMeta(type):
    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)

        list_serializer = getattr(cls, "list_serializer", None)
        detail_serializer = getattr(cls, "detail_serializer", None)
        create_serializer = getattr(cls, "create_serializer", None)
        update_serializer = getattr(cls, "update_serializer", None)
        pk_type = getattr(cls, "pk_type", int)

        cls = mcs.decorate_list(cls, list_serializer)
        cls = mcs.decorate_retrieve(cls, detail_serializer, pk_type)
        cls = mcs.decorate_create(cls, create_serializer, detail_serializer)
        cls = mcs.decorate_partial_update(
            cls, update_serializer, detail_serializer, pk_type
        )
        cls = mcs.decorate_destroy(cls, pk_type)

        return cls

    @staticmethod
    def decorate_list(cls, list_serializer):
        if hasattr(cls, "list") and list_serializer:
            original_list = cls.list

            @extend_schema(
                methods=[HTTPMethod.GET],
                parameters=[
                    OpenApiParameter(
                        name="skip",
                        type=int,
                        location=OpenApiParameter.QUERY,
                        description="Number of items to skip.",
                    ),
                    OpenApiParameter(
                        name="limit",
                        type=int,
                        location=OpenApiParameter.QUERY,
                        description="Maximum number of items to retrieve.",
                    ),
                ],
                responses={HTTPStatus.OK: list_serializer},
            )
            def list_decorated(self, request: Request, *args, **kwargs):
                return original_list(self, request, *args, **kwargs)

            cls.list = list_decorated
        return cls

    @staticmethod
    def decorate_retrieve(cls, detail_serializer, pk_type):
        if hasattr(cls, "retrieve") and detail_serializer:
            original_retrieve = cls.retrieve

            @extend_schema(
                methods=[HTTPMethod.GET],
                parameters=[
                    OpenApiParameter(
                        name="id",
                        type=pk_type,
                        location=OpenApiParameter.PATH,
                        description="Item ID",
                    ),
                ],
                responses={
                    HTTPStatus.OK: detail_serializer,
                    HTTPStatus.NOT_FOUND: NotFoundResponseSerializer,
                },
            )
            def retrieve_decorated(self, request: Request, pk: Any, *args, **kwargs):
                return original_retrieve(self, request, pk, *args, **kwargs)

            cls.retrieve = retrieve_decorated
        return cls

    @staticmethod
    def decorate_create(cls, create_serializer, detail_serializer):
        if hasattr(cls, "create") and create_serializer and detail_serializer:
            original_create = cls.create

            @extend_schema(
                request=create_serializer,
                responses={HTTPStatus.CREATED: detail_serializer},
                methods=[HTTPMethod.POST],
            )
            def create_decorated(self, request: Request, *args, **kwargs):
                return original_create(self, request, *args, **kwargs)

            cls.create = create_decorated
        return cls

    @staticmethod
    def decorate_partial_update(cls, update_serializer, detail_serializer, pk_type):
        if hasattr(cls, "partial_update") and update_serializer and detail_serializer:
            original_partial_update = cls.partial_update

            @extend_schema(
                request=update_serializer,
                responses={
                    HTTPStatus.OK: detail_serializer,
                    HTTPStatus.NOT_FOUND: NotFoundResponseSerializer,
                },
                methods=[HTTPMethod.PATCH],
                parameters=[
                    OpenApiParameter(
                        name="id",
                        type=pk_type,
                        location=OpenApiParameter.PATH,
                        description="Item ID",
                    ),
                ],
            )
            def partial_update_decorated(
                self, request: Request, pk: Any, *args, **kwargs
            ):
                return original_partial_update(self, request, pk, *args, **kwargs)

            cls.partial_update = partial_update_decorated
        return cls

    @staticmethod
    def decorate_destroy(cls, pk_type):
        if hasattr(cls, "destroy"):
            original_destroy = cls.destroy

            @extend_schema(
                methods=[HTTPMethod.DELETE],
                parameters=[
                    OpenApiParameter(
                        name="id",
                        type=pk_type,
                        location=OpenApiParameter.PATH,
                        description="Item ID",
                    ),
                ],
                responses={
                    HTTPStatus.NO_CONTENT: None,
                    HTTPStatus.NOT_FOUND: NotFoundResponseSerializer,
                },
            )
            def destroy_decorated(self, request: Request, pk: Any, *args, **kwargs):
                return original_destroy(self, request, pk, *args, **kwargs)

            cls.destroy = destroy_decorated
        return cls
