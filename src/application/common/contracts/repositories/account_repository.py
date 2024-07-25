from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.account import User
from src.domain.value_objects import UserId
from src.application.common.contracts.repositories.base_repository import (
    AbstractRepositoryInterface,
)


class UserRepositoryInterface(
    AbstractRepositoryInterface[User, UserId], ABC
):
    @abstractmethod
    def create(
        self,
        username: str,
        email: str,
        password: str,
        is_staff: Optional[bool] = False,
        is_active: Optional[bool] = False,
        is_superuser: Optional[bool] = False,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
    ) -> User:
        pass
