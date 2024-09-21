from typing import Optional

from src.application.common.contracts.repositories.account_repository import (
    UserRepositoryInterface,
)
from src.application.common.exceptions.entity_already_exist_exception import (
    EntityAlreadyExistException,
)
from src.domain.entities.account import User
from src.domain.value_objects import UserId
from src.infrastructure.models import User as UserModel
from src.infrastructure.repositories.base_repository import AbstractRepository


class UserRepository(AbstractRepository[UserModel, UserId], UserRepositoryInterface):
    model = UserModel

    def _decode_model(self, instance: UserModel) -> User:
        return User(
            user_id=instance.pk,
            username=instance.username,
            email=instance.email,
            password=instance.password,
            is_staff=instance.is_staff,
            is_active=instance.is_active,
            is_superuser=instance.is_superuser,
            date_joined=instance.date_joined,
            created_by=instance.created_by,
            updated_by=instance.updated_by,
            created_at=instance.created_at,
            updated_at=instance.updated_at,
        )

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
        if self.exists(username=username):
            raise EntityAlreadyExistException("Username")

        if self.exists(email=email):
            raise EntityAlreadyExistException("Email")

        instance = UserModel(
            username=username,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            created_by=created_by,
            updated_by=updated_by,
        )
        instance.set_password(password)
        instance.save()
        return self._decode_model(instance)
