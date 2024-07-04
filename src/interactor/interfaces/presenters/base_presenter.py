from abc import ABC, abstractmethod
from typing import Dict

class AbstractPresenterInterface[T](ABC):
    """
    Abstract base class for defining presenter interfaces.

    Attributes:
        T: Type parameter representing the output DTO type.
    """

    @abstractmethod
    def present(self, output_dto: T) -> Dict:
        """
        Abstract method to present an output DTO as a dictionary.

        Args:
            output_dto (T): The output DTO object to present.

        Returns:
            Dict: The presented output as a dictionary.
        """
        pass
