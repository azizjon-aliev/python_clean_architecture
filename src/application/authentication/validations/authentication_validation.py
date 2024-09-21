from typing import Optional

from pydantic import BaseModel


class RegisterInputDtoValidator(BaseModel):
    username: str
    email: Optional[str]
    password: str
    password_confirmation: str
