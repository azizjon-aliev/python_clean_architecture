from typing import Optional

from pydantic import BaseModel


class RegisterStep1InputDtoValidator(BaseModel):
    phone: str
    email: Optional[str] = None
    otp: int
    password: str
