from abc import ABC, abstractmethod
from typing import Optional

from rest_framework.request import Request
from rest_framework.response import Response


class AbstractViewInterface[TKey](ABC):
    """
    Abstract base class for defining REST API view interfaces.

    Attributes:
        TKey: Type of the primary key or identifier for the entity handled by the views.
    """

    @abstractmethod
    def list(self, request: Request) -> Response:
        """
        Abstract method to handle HTTP GET request for retrieving a list of entities.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: The HTTP response object.
        """
        pass

    @abstractmethod
    def retrieve(self, request: Request, pk: Optional[TKey]) -> Response:
        """
        Abstract method to handle HTTP GET request for retrieving a single entity.

        Args:
            request (Request): The HTTP request object.
            pk (Optional[TKey]): The primary key or identifier of the entity to retrieve.

        Returns:
            Response: The HTTP response object.
        """
        pass

    @abstractmethod
    def create(self, request: Request) -> Response:
        """
        Abstract method to handle HTTP POST request for creating a new entity.

        Args:
            request (Request): The HTTP request object containing entity data.

        Returns:
            Response: The HTTP response object.
        """
        pass

    @abstractmethod
    def partial_update(self, request: Request, pk: Optional[TKey]) -> Response:
        """
        Abstract method to handle HTTP PATCH request for partially updating an entity.

        Args:
            request (Request): The HTTP request object containing partial update data.
            pk (Optional[TKey]): The primary key or identifier of the entity to update.

        Returns:
            Response: The HTTP response object.
        """
        pass

    @abstractmethod
    def destroy(self, request: Request, pk: Optional[TKey]) -> Response:
        """
        Abstract method to handle HTTP DELETE request for deleting an entity.

        Args:
            request (Request): The HTTP request object.
            pk (Optional[TKey]): The primary key or identifier of the entity to delete.

        Returns:
            Response: The HTTP response object.
        """
        pass
