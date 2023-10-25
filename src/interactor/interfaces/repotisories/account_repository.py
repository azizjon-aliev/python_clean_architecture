from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.account import User
from src.domain.value_objects import UserId


class UserRepositoryInterface(ABC):
    @abstractmethod
    def get(self, user_id: UserId) -> User:
        pass

    @abstractmethod
    def delete(self, user_id: UserId) -> None:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def list(self, skip: int = 0, limit: int = 100) -> List[User]:
        pass

    @abstractmethod
    def exists(self, **kwargs) -> bool:
        pass

    @abstractmethod
    def create(self, code: str, name: str, symbol: str) -> User:
        pass

    @abstractmethod
    def update(self, user_id: UserId, code: str, name: str, symbol: str) -> User:
        pass
