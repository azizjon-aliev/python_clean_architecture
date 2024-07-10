from typing import Optional

from pydantic import BaseModel


class CreateCurrencyInputDtoValidator(BaseModel):
    code: str
    name: str
    symbol: str


class UpdateCurrencyInputDtoValidator(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    symbol: Optional[str] = None
