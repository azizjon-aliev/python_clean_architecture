from typing import Dict

from src.interactor.dtos.authentication_dtos import TokenDto
from src.interactor.interfaces.presenters.authentication_presenter import (
    LoginPresenterInterface,
)


class LoginPresenter(LoginPresenterInterface):
    def present(self, output_dto: TokenDto) -> Dict:
        return {
            "access_token": output_dto.access_token,
            "refresh_token": output_dto.refresh_token,
        }
