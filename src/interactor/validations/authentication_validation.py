from typing import Optional

from pydantic import BaseModel


class RegisterStep1InputDtoValidator(BaseModel):
    username: str
    email: str
    otp: int
    password: str
