from abc import ABC, abstractmethod
from typing import Dict

from src.interactor.dtos.account_dtos import RegisterStep1OutputDto


class RegisterStep1PresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto: RegisterStep1OutputDto) -> Dict:
        pass
