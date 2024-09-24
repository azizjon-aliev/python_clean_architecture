from dataclasses import dataclass

from src.domain.value_objects import UserId


@dataclass
class UserVm:
    id: UserId
    username: str
    email: str
