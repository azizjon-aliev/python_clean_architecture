from abc import ABC, abstractmethod


class LoggerInterface(ABC):
    @abstractmethod
    def log_debug(self, message: str) -> None:
        pass

    @abstractmethod
    def log_info(self, message: str) -> None:
        pass

    @abstractmethod
    def log_warning(self, message: str) -> None:
        pass

    @abstractmethod
    def log_error(self, message: str) -> None:
        pass

    @abstractmethod
    def log_critical(self, message: str) -> None:
        pass

    @abstractmethod
    def log_exception(self, message: str) -> None:
        pass
