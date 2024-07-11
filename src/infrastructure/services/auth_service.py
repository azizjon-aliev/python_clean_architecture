from typing import Optional
from django.contrib.auth import authenticate

from src.domain.entities.account import User
from src.infrastructure.repositories.account_repository import UserRepository
from src.interactor.interfaces.services.auth_service import AuthServiceInterface


class AuthService(AuthServiceInterface):

    def authenticate(self, username: str, password: str) -> Optional[User]:
        user = authenticate(username=username, password=password)
        if user is not None:
            return UserRepository()._decode_model(user)
        return None
