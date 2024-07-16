from dataclasses import dataclass

from mediatr import GenericQuery

from src.application.authentication.responses.user_vm import UserVm


@dataclass
class LoginUserQuery(GenericQuery[UserVm]):
    username: str
    password: str
