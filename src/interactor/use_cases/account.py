from typing import Dict

from src.infrastructure.constaints import Role
from src.interactor.dtos.account_dtos import (
    RegisterStep1InputDto,
    RegisterStep1OutputDto,
)
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.interfaces.presenters.account_presenter import (
    RegisterStep1PresenterInterface,
)
from src.interactor.interfaces.repotisories.account_repository import (
    UserRepositoryInterface,
)
from src.interactor.validations.account_validation import RegisterStep1InputDtoValidator


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
            phone=input_dto.phone,
            email=input_dto.email,
            otp=input_dto.otp,
            password=input_dto.password,
        )
        user = self.repository.create(
            phone=input_dto.phone,
            email=input_dto.email,
            password=input_dto.password,
            is_active=True,
            role=Role.CLIENT,
            otp=input_dto.otp,
        )
        output_dto = RegisterStep1OutputDto(user)
        self.logger.log_info("Registered successfully")
        return self.presenter.present(output_dto)
