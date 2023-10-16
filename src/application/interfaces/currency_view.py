from typing import Optional
from abc import ABC, abstractmethod
from rest_framework.request import Request
from rest_framework.response import Response
from src.domain.value_objects import CurrencyId


class CurrencyViewInterface(ABC):
    @abstractmethod
    def create(self, request: Request) -> Response:
        pass

    @abstractmethod
    def partial_update(self, request: Request, pk: Optional[CurrencyId]) -> Response:
        pass
