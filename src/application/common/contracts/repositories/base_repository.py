from abc import ABC, abstractmethod
from typing import List


class AbstractRepositoryInterface[T, TKey](ABC):
    """
    Abstract base class for defining repository interfaces.

    Args:
            T: Type parameter representing the entity type.
            TKey: Type parameter representing the primary key type.

    Attributes:
            T: Type parameter representing the entity type.
            TKey: Type parameter representing the primary key type.
    """

    @abstractmethod
    def get(self, object_id: TKey) -> T:
        """
        Abstract method to retrieve an entity by its primary key.

        Args:
                object_id (TKey): The primary key of the entity to retrieve.

        Returns:
                T: The retrieved entity object.
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(self, object_id: TKey) -> None:
        """
        Abstract method to delete an entity by its primary key.

        Args:
                object_id (TKey): The primary key of the entity to delete.
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def count(self) -> int:
        """
        Abstract method to count the total number of entities.

        Returns:
                int: The total count of entities.
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def list(self, skip: int = 0, limit: int = 100) -> List[T]:
        """
        Abstract method to retrieve a list of entities with optional pagination.

        Args:
                skip (int, optional): Number of entities to skip. Defaults to 0.
                limit (int, optional): Maximum number of entities to retrieve. Defaults to 100.

        Returns:
                List[T]: List of retrieved entities.
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def exists(self, **kwargs) -> bool:
        """
        Abstract method to check if an entity exists based on given criteria.

        Args:
                **kwargs: Arbitrary keyword arguments for filtering.

        Returns:
                bool: True if the entity exists, False otherwise.
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def create(self, **kwargs) -> T:
        """
        Abstract method to create a new entity with the provided data.

        Args:
                **kwargs: Arbitrary keyword arguments representing entity attributes.

        Returns:
                T: The created entity object.
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def update(self, object_id: TKey, **kwargs) -> T:
        """
        Abstract method to update an existing entity with the provided data.

        Args:
                object_id (TKey): The primary key of the entity to update.
                **kwargs: Arbitrary keyword arguments representing updated entity attributes.

        Returns:
                T: The updated entity object.
        """
        raise NotImplementedError("Method not implemented")
