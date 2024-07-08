from dataclasses import dataclass


@dataclass
class RegisterStep1InputDto:
    username: str
    email: str
    otp: int
    password: str



@dataclass
class LoginInputDto:
    username: str
    password: str



@dataclass
class TokenDto:
    access_token: str
    refresh_token: str



@dataclass
class RefreshTokenInputDto:
    refresh_token: str
