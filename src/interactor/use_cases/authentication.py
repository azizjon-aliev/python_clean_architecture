from typing import Dict

from src.interactor.dtos.authentication_dtos import (
    RegisterStep1InputDto,
    RegisterStep1OutputDto,
)
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.interfaces.presenters.authentication_presenter import (
    RegisterStep1PresenterInterface,
)
from src.interactor.interfaces.repositories.account_repository import (
    UserRepositoryInterface,
)
from src.interactor.validations.authentication_validation import RegisterStep1InputDtoValidator


class RegisterStep1UseCase:
    def __init__(
        self,
        repository: UserRepositoryInterface,
        presenter: RegisterStep1PresenterInterface,
        logger: LoggerInterface,
    ):
        self.repository = repository
        self.presenter = presenter
        self.logger = logger

    def execute(self, input_dto: RegisterStep1InputDto) -> Dict:
        RegisterStep1InputDtoValidator(
            username=input_dto.username,
            email=input_dto.email,
            otp=input_dto.otp,
            password=input_dto.password,
        )
        user = self.repository.create(
            username=input_dto.username,
            email=input_dto.email,
            password=input_dto.password,
            is_active=True,
            otp=input_dto.otp,
        )
        output_dto = RegisterStep1OutputDto(user)
        self.logger.log_info("Registered successfully")
        return self.presenter.present(output_dto)
