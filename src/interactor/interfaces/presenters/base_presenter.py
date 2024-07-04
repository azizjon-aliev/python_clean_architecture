from abc import ABC, abstractmethod
from typing import Dict

class AbstractPresenterInterface[T](ABC):
    @abstractmethod
    def present(self, output_dto: T) -> Dict:
        pass
