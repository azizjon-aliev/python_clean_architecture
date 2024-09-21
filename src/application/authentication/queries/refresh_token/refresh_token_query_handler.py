import logging
from dataclasses import dataclass

from automapper import Mapper

from src.application.authentication.queries.refresh_token.refresh_token_query import (
    RefreshTokenQuery,
)
from src.application.authentication.responses.token_vm import TokenVm
from src.application.common.contracts.providers.token_provider import (
    TokenProviderInterface,
)

logger = logging.getLogger(__name__)


@dataclass
class RefreshTokenQueryHandler:
    provider: TokenProviderInterface
    mapper: Mapper

    def handle(self, request: RefreshTokenQuery) -> TokenVm:
        logger.info("Handling RefreshTokenQuery...")

        tokens = self.provider.verify_refresh_token(request.refresh_token)

        logger.info("Successfully handled RefreshTokenQuery...")

        return self.mapper.to(TokenVm).map(tokens)
