from typing import Optional
from src.domain.entities.account import User
from src.domain.value_objects import UserId
from src.infrastructure.models import User as UserModel
from src.infrastructure.repotisories.base_repository import AbstractRepository
from src.interactor.errors.error_classes import EntityAlreadyExists
from src.interactor.interfaces.repotisories.account_repository import UserRepositoryInterface

class UserRepository(AbstractRepository[UserModel, UserId], UserRepositoryInterface):

    model = UserModel

    def _decode_model(self, instance: UserModel) -> User:
        return User(
            user_id=instance.pk,
            phone=instance.phone,
            email=instance.email,
            password=instance.password,
            is_staff=instance.is_staff,
            is_active=instance.is_active,
            is_superuser=instance.is_superuser,
            date_joined=instance.date_joined,
            otp=instance.otp,
            is_verified=instance.is_verified,
            role=instance.role,
            company=None,
            created_by=instance.created_by,
            updated_by=instance.updated_by,
            created_at=instance.created_at,
            updated_at=instance.updated_at,
        )

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
        if self.exists(phone=phone):
            raise EntityAlreadyExists("Phone already exists")

        if email and self.exists(email=email):
            raise EntityAlreadyExists("Email already exists")

        instance = UserModel(
            phone=phone,
            email=email,
            role=role,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            otp=otp,
            is_verified=is_verified,
            # company
            created_by=created_by,
            updated_by=updated_by,
        )
        instance.set_password(password)
        instance.BASE_ROLE = role
        instance.save()
        return self.__decode_model(instance)
