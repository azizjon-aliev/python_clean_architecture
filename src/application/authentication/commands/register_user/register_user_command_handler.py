import logging
from dataclasses import dataclass

from automapper import Mapper

from src.application.authentication.commands.register_user.register_user_command import (
    RegisterUserCommand,
)
from src.application.authentication.responses.token_vm import TokenVm
from src.application.authentication.validations.authentication_validation import (
    RegisterInputDtoValidator,
)
from src.application.common.contracts.providers.token_provider import (
    TokenProviderInterface,
)
from src.application.common.contracts.repositories.account_repository import (
    UserRepositoryInterface,
)
from src.application.common.exceptions.authentication_exceptions import (
    EntityDontMatchPasswordException,
)
from src.application.common.exceptions.entity_already_exist_exception import (
    EntityAlreadyExistException,
)
from src.application.common.exceptions.entity_incorrect_format_exception import (
    EntityIncorrectFormatException,
)
from src.domain.entities.account import User

logger = logging.getLogger(__name__)


@dataclass
class RegisterUserCommandHandler:
    repository: UserRepositoryInterface
    provider: TokenProviderInterface
    mapper: Mapper

    def handle(self, request: RegisterUserCommand) -> TokenVm:
        logger.info("Handling RegisterUserCommand...")

        logger.info("User validation...")

        RegisterInputDtoValidator(
            username=request.username,
            email=request.email,
            password=request.password,
            password_confirmation=request.password_confirmation,
        )

        if request.password != request.password_confirmation:
            logger.error("The passwords don't match")
            raise EntityDontMatchPasswordException

        if self.repository.exists(email=request.email):
            logger.error("The passwords don't match")
            raise EntityAlreadyExistException("Email")

        if self.repository.exists(username=request.username):
            logger.error("The passwords don't match")
            raise EntityAlreadyExistException("Username")

        if not User.check_password(password=request.password):
            logger.error("Incorrect password format.")
            raise EntityIncorrectFormatException("password")

        logger.info("User successfully created")
        user = self.repository.create(
            username=request.username,
            email=request.email,
            password=request.password,
            is_active=True,
        )

        token = self.provider.get_token(user)

        logger.info("Successfully handled RegisterUserCommand...")

        return self.mapper.to(TokenVm).map(token)
