from abc import ABC, abstractmethod
from typing import Optional

from rest_framework.request import Request
from rest_framework.response import Response


class AbstractViewInterface[TKey](ABC):
    @abstractmethod
    def list(self, request: Request) -> Response:
        pass

    @abstractmethod
    def retrieve(self, request: Request, pk: Optional[TKey]) -> Response:
        pass

    @abstractmethod
    def create(self, request: Request) -> Response:
        pass

    @abstractmethod
    def partial_update(self, request: Request, pk: Optional[TKey]) -> Response:
        pass

    @abstractmethod
    def destroy(self, request: Request, pk: Optional[TKey]) -> Response:
        pass
