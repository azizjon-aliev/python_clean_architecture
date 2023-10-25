from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.account import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def exists(self, **kwargs) -> bool:
        pass

    @abstractmethod
    def create(
        self,
        phone: str,
        email: Optional[str],
        password: str,
        role: str,
        is_staff: Optional[bool] = False,
        is_active: Optional[bool] = False,
        is_superuser: Optional[bool] = False,
        otp: Optional[int] = 0,
        is_verified: Optional[bool] = False,
        company: Optional[str] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
    ) -> User:
        pass
