from abc import ABC, abstractmethod

from rest_framework.request import Request
from rest_framework.response import Response


class RegisterViewInterface(ABC):
    @abstractmethod
    def step1(self, request: Request) -> Response:
        pass

    @abstractmethod
    def step2(self, request: Request) -> Response:
        pass


class RegisterStep2ViewInterface(ABC):
    @abstractmethod
    def post(self, request: Request) -> Response:
        pass
