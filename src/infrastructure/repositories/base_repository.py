import os
from typing import List, Type

from dotenv import load_dotenv

import django
from django.db.models import Model
from src.application.common.exceptions.entity_does_not_exist_exception import (
    EntityDoesNotExistException,
)

load_dotenv()
settings_module = f"src.presentation.rest_api.config.settings.{os.getenv('DJANGO_ENV')}"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

django.setup()


class AbstractRepository[T: Model, TKey]:
    """
    Abstract base class for generic repository operations.

    Args:
            T: Type of the model entity, expected to be a Django Model.
            TKey: Type of the primary key or identifier for the entity.

    Attributes:
            model: Type[T]
                    The Django Model type associated with this repository.
    """

    model: Type[T]

    def __init__(self):
        """
        Initializes the repository with the model type.

        Raises:
                ValueError: If the `model` attribute is not a valid Django Model type.
        """
        if (
            not hasattr(self, "model")
            or not isinstance(self.model, type)
            or not issubclass(self.model, Model)
        ):
            raise ValueError(f"Invalid model type for repository: {self.model}")

    def _decode_model(self, instance: T) -> T:
        """
        Abstract method to decode a database instance into a domain entity.

        Args:
                instance (T): The database instance to decode.

        Returns:
                T: The decoded domain entity.

        Raises:
                NotImplementedError: If the method is not implemented in the subclass.
        """
        raise NotImplementedError("You must implement the _decode_model method")

    def exists(self, **kwargs) -> bool:
        """
        Checks if an entity exists in the database based on given criteria.

        Args:
                **kwargs: Arbitrary keyword arguments for filtering.

        Returns:
                bool: True if the entity exists, False otherwise.
        """
        return bool(self.model.objects.filter(**kwargs).exists())

    def count(self) -> int:
        """
        Counts the total number of entities in the database.

        Returns:
                int: The count of entities.
        """
        return self.model.objects.count()

    def delete(self, object_id: TKey) -> None:
        """
        Deletes an entity from the database by its primary key.

        Args:
                object_id (TKey): The primary key of the entity to delete.

        Raises:
                EntityDoesNotExist: If the entity with the given primary key does not exist.
        """
        instance = self.model.objects.filter(pk=object_id).first()
        if not instance:
            raise EntityDoesNotExistException(
                f"{self.model.__name__} with id {object_id} not found"
            )
        instance.delete()

    def list(self, skip: int = 0, limit: int = 100) -> List[T]:
        """
        Retrieves a list of entities from the database with optional pagination.

        Args:
                skip (int, optional): Number of entities to skip. Defaults to 0.
                limit (int, optional): Maximum number of entities to retrieve. Defaults to 100.

        Returns:
                List[T]: List of decoded domain entities.
        """
        instances = self.model.objects.all()[skip : skip + limit]
        return [self._decode_model(instance) for instance in instances]

    def get(self, object_id: TKey) -> T:
        """
        Retrieves an entity from the database by its primary key.

        Args:
                object_id (TKey): The primary key of the entity to retrieve.

        Returns:
                T: The decoded domain entity.

        Raises:
                EntityDoesNotExist: If the entity with the given primary key does not exist.
        """
        instance = self.model.objects.filter(pk=object_id).first()
        if not instance:
            raise EntityDoesNotExistException(
                f"{self.model.__name__} with id {object_id} not found"
            )
        return self._decode_model(instance)

    def create(self, **kwargs) -> T:
        """
        Creates a new entity in the database with the provided data.

        Args:
                **kwargs: Arbitrary keyword arguments representing entity attributes.

        Returns:
                T: The created domain entity.

        """
        instance = self.model(**kwargs)
        instance.save()
        return self._decode_model(instance)

    def update(self, object_id: TKey, **kwargs) -> T:
        """
        Updates an existing entity in the database with the provided data.

        Args:
                object_id (TKey): The primary key of the entity to update.
                **kwargs: Arbitrary keyword arguments representing updated entity attributes.

        Returns:
                T: The updated domain entity.

        Raises:
                EntityDoesNotExist: If the entity with the given primary key does not exist.
        """
        instance = self.model.objects.filter(pk=object_id).first()
        if not instance:
            raise EntityDoesNotExistException(
                f"{self.model.__name__} with id {object_id} not found"
            )
        for field, value in kwargs.items():
            if value is not None:
                setattr(instance, field, value)
        instance.save()
        return self._decode_model(instance)
