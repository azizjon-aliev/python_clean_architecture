import logging
from dataclasses import dataclass

from automapper import Mapper

from src.application.authentication.queries.login_user.login_user_query import (
    LoginUserQuery,
)
from src.application.authentication.responses.token_vm import TokenVm
from src.application.common.contracts.providers.token_provider import (
    TokenProviderInterface,
)
from src.application.common.contracts.repositories.account_repository import (
    UserRepositoryInterface,
)
from src.application.common.contracts.services.auth_service import AuthServiceInterface
from src.application.common.exceptions.authentication_exceptions import (
    EntityInvalidCredentialsException,
)

logger = logging.getLogger(__name__)


@dataclass
class LoginUserQueryHandler:
    repository: UserRepositoryInterface
    service: AuthServiceInterface
    provider: TokenProviderInterface
    mapper: Mapper

    def handle(self, request: LoginUserQuery) -> TokenVm:
        logger.info("Handling LoginUserQuery...")

        user = self.service.authenticate(request.username, request.password)
        if not user:
            logger.info("The user has entered incorrect data")
            raise EntityInvalidCredentialsException("Invalid username or password")

        response = self.provider.get_token(user)

        logger.info("Successfully handled LoginUserQuery...")

        return self.mapper.to(TokenVm).map(response)
