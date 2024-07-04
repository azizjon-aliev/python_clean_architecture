from abc import ABC, abstractmethod
from typing import List

class AbstractRepositoryInterface[T, TKey](ABC):
    @abstractmethod
    def get(self, object_id: TKey) -> T:
        pass

    @abstractmethod
    def delete(self, object_id: TKey) -> None:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def list(self, skip: int = 0, limit: int = 100) -> List[T]:
        pass

    @abstractmethod
    def exists(self, **kwargs) -> bool:
        pass

    @abstractmethod
    def create(self, **kwargs) -> T:
        pass

    @abstractmethod
    def update(self, object_id: TKey, **kwargs) -> T:
        pass
