from typing import Dict

from src.interactor.dtos.authentication_dtos import (
    RefreshTokenInputDto,
    RegisterStep1InputDto,
    LoginInputDto,
    TokenDto,
)
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.interfaces.presenters.authentication_presenter import (
    LoginPresenterInterface,
)
from src.interactor.interfaces.repositories.account_repository import (
    UserRepositoryInterface,
)
from src.interactor.interfaces.repositories.authentication_repository import (
    AuthRepositoryInterface,
)
from src.interactor.validations.authentication_validation import RegisterStep1InputDtoValidator
from src.interactor.interfaces.providers.token_provider import TokenProviderInterface
from src.interactor.errors.error_classes import InvalidCredentials


class RegisterStep1UseCase:
    def __init__(
        self,
        repository: UserRepositoryInterface,
        presenter: LoginPresenterInterface,
        provider: TokenProviderInterface,
        logger: LoggerInterface,
    ):
        self.repository = repository
        self.presenter = presenter
        self.provider = provider
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
        token = self.provider.get_token(user)
        access_token = token.get("access_token")
        refresh_token = token.get("refresh_token")
        output_dto = TokenDto(access_token=access_token, refresh_token=refresh_token)
        self.logger.log_info("Registered successfully")
        return self.presenter.present(output_dto)



class LoginUseCase:
    def __init__(
        self,
        repository: AuthRepositoryInterface,
        provider: TokenProviderInterface,
        presenter: LoginPresenterInterface,
        logger: LoggerInterface,
    ):
        self.repository = repository
        self.provider = provider
        self.presenter = presenter
        self.logger = logger

    def execute(self, input_dto: LoginInputDto) -> Dict:
        user = self.repository.authenticate(input_dto.username, input_dto.password)
        if not user:
            raise InvalidCredentials("Invalid username or password")

        token = self.provider.get_token(user)
        access_token = token.get("access_token")
        refresh_token = token.get("refresh_token")
        output_dto = TokenDto(access_token=access_token, refresh_token=refresh_token)
        self.logger.log_info("Logged successfully")
        return self.presenter.present(output_dto)



class RefreshTokenUseCase:
    def __init__(
        self,
        provider: TokenProviderInterface,
        presenter: LoginPresenterInterface,
        logger: LoggerInterface,
    ):
        self.provider = provider
        self.presenter = presenter
        self.logger = logger

    def execute(self, input_dto: RefreshTokenInputDto) -> Dict:
        tokens = self.provider.verify_refresh_token(input_dto)
        access_token = tokens.get("access_token")
        new_refresh_token = tokens.get("refresh_token")
        output_dto = TokenDto(access_token=access_token, refresh_token=new_refresh_token)
        self.logger.log_info("Logged successfully")
        return self.presenter.present(output_dto)
