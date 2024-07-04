from abc import abstractmethod
from typing import Optional

from src.interactor.interfaces.repotisories.base_repository import AbstractRepositoryInterface
from src.domain.entities.account import User
from src.domain.value_objects import CurrencyId


class UserRepositoryInterface(AbstractRepositoryInterface[User, CurrencyId]):
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
