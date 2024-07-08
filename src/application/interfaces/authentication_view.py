from abc import ABC, abstractmethod

from rest_framework.request import Request
from rest_framework.response import Response



class AuthViewInterface(ABC):
    @abstractmethod
    def step1(self, request: Request) -> Response:
        pass

    @abstractmethod
    def login(self, request: Request) -> Response:
        pass
