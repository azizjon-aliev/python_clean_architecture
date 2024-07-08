from datetime import datetime
from typing import Optional

from src.domain.entities.account import User
from src.domain.value_objects import UserId
from src.infrastructure.models import User as UserModel
from src.infrastructure.repositories.base_repository import AbstractRepository
from src.interactor.errors.error_classes import EntityAlreadyExists
from src.interactor.interfaces.repositories.account_repository import (
    UserRepositoryInterface,
)


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
            otp=instance.otp,
            otp_expire_time=instance.otp_expire_time,
            is_verified=instance.is_verified,
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
        otp: Optional[int] = 0,
        otp_expire_time: Optional[datetime] = None,
        is_verified: Optional[bool] = False,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
    ) -> User:
        if self.exists(username=username):
            raise EntityAlreadyExists("username already exists")

        if self.exists(email=email):
            raise EntityAlreadyExists("Email already exists")

        instance = UserModel(
            username=username,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            otp=otp,
            otp_expire_time=otp_expire_time,
            is_verified=is_verified,
            created_by=created_by,
            updated_by=updated_by,
        )
        instance.set_password(password)
        instance.save()
        return self._decode_model(instance)
