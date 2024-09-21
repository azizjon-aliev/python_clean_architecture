from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.account import User


class AuthServiceInterface(ABC):
    @abstractmethod
    def authenticate(self, username: str, password: str) -> Optional[User]:
        pass
