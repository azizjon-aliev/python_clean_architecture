from dataclasses import dataclass

from mediatr import GenericQuery

from src.application.authentication.responses.token_vm import TokenVm


@dataclass
class RefreshTokenQuery(GenericQuery[TokenVm]):
    refresh_token: str
