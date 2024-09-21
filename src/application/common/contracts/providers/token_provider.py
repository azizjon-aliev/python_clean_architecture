from abc import ABC, abstractmethod

from src.domain.entities.account import User


class TokenProviderInterface(ABC):
    @abstractmethod
    def get_token(self, user: User) -> dict:
        pass

    @abstractmethod
    def verify_refresh_token(self, token: str) -> dict:
        pass
