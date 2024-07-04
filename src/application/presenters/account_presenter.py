from typing import Dict

from src.interactor.dtos.account_dtos import RegisterStep1OutputDto
from src.interactor.interfaces.presenters.account_presenter import (
    RegisterStep1PresenterInterface,
)


class RegisterStep1Presenter(RegisterStep1PresenterInterface):
    def present(self, output_dto: RegisterStep1OutputDto) -> Dict:
        return {
            "id": output_dto.user.user_id,
            "username": output_dto.user.username,
            "email": output_dto.user.email,
        }
