from dataclasses import dataclass


@dataclass
class TokenVm:
    access_token: str
    refresh_token: str
