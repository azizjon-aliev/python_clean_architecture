from typing import Type

from automapper import Mapper
from mediatr import Mediator

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from src.presentation.rest_api.apps.common.extend_schema_meta import ExtendSchemaMeta
from src.presentation.rest_api.config.containers import container


class BaseAPIView[
    ListSerializerType,
    DetailSerializerType,
    CreateSerializerType,
    UpdateSerializerType,
    ListQueryType,
    DetailQueryType,
    CreateCommandType,
    UpdateCommandType,
    RemoveCommandType,
    PKType,
](ViewSet, metaclass=ExtendSchemaMeta):
    authentication_classes = ()

    list_serializer: Type[ListSerializerType]
    detail_serializer: Type[DetailSerializerType]
    create_serializer: Type[CreateSerializerType]
    update_serializer: Type[UpdateSerializerType]
    list_query: Type[ListQueryType]
    detail_query: Type[DetailQueryType]
    create_command: Type[CreateCommandType]
    update_command: Type[UpdateCommandType]
    remove_command: Type[RemoveCommandType]

    pk_type: Type[PKType]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__mediator: Mediator = container.resolve(Mediator)
        self.__mapper: Mapper = container.resolve(Mapper)

    def list(self, request: Request) -> Response:
        parameters = {
            "skip": int(request.query_params.get("skip", 0)),
            "limit": int(request.query_params.get("limit", 100)),
        }

        query = self.list_query(**parameters)
        result = self.__mediator.send(query)

        return Response(
            data=self.list_serializer(result, many=True).data,
            status=status.HTTP_200_OK,
        )

    def retrieve(self, request: Request, pk: PKType) -> Response:
        query = self.detail_query(id=pk)
        result = self.__mediator.send(query)

        if not result:
            return Response(
                data={"detail": "Not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            data=self.detail_serializer(result).data,
            status=status.HTTP_200_OK,
        )

    def create(self, request: Request) -> Response:
        serializer = self.create_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        command = self.__mapper.to(self.create_command).map(serializer.validated_data)
        result = self.__mediator.send(command)

        return Response(
            data=self.detail_serializer(result).data,
            status=status.HTTP_201_CREATED,
        )

    def partial_update(self, request: Request, pk: PKType) -> Response:
        serializer = self.update_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        command = self.__mapper.to(self.update_command).map(
            serializer.validated_data, fields_mapping={"id": pk}
        )
        result = self.__mediator.send(command)

        if not result:
            return Response(
                data={"detail": "Not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            data=self.detail_serializer(result).data,
            status=status.HTTP_200_OK,
        )

    def destroy(self, request: Request, pk: PKType) -> Response:
        command = self.remove_command(id=pk)
        result = self.__mediator.send(command)
        return Response(data=result, status=status.HTTP_204_NO_CONTENT)
