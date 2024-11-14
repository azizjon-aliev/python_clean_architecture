from abc import ABC, abstractmethod


class LoggerInterface(ABC):
    """
    An abstract base class that defines the interface for a logger.

    This interface enforces the implementation of various logging methods
    to handle different levels of log messages, ensuring consistency across
    different logging mechanisms.
    """

    @abstractmethod
    def log_debug(self, message: str) -> None:
        """
        Log a message with DEBUG severity.

        DEBUG messages are typically used for detailed information, useful
        for diagnosing problems and tracing the flow of an application.

        Parameters:
            message (str): The debug message to be logged.
        """
        pass

    @abstractmethod
    def log_info(self, message: str) -> None:
        """
        Log a message with INFO severity.

        INFO messages convey general information about the application's
        progress or state, providing insights into its operation.

        Parameters:
            message (str): The informational message to be logged.
        """
        pass

    @abstractmethod
    def log_warning(self, message: str) -> None:
        """
        Log a message with WARNING severity.

        WARNING messages indicate potential issues or unexpected events
        that are not critical but may require attention.

        Parameters:
            message (str): The warning message to be logged.
        """
        pass

    @abstractmethod
    def log_error(self, message: str) -> None:
        """
        Log a message with ERROR severity.

        ERROR messages report serious issues that have occurred, typically
        indicating a failure in a part of the application.

        Parameters:
            message (str): The error message to be logged.
        """
        pass

    @abstractmethod
    def log_critical(self, message: str) -> None:
        """
        Log a message with CRITICAL severity.

        CRITICAL messages denote severe errors that may cause the application
        to abort or require immediate attention.

        Parameters:
            message (str): The critical message to be logged.
        """
        pass

    @abstractmethod
    def log_exception(self, message: str) -> None:
        """
        Log an exception message with ERROR severity, including traceback information.

        This method is specifically designed to log exceptions, capturing
        stack traces and other relevant debugging information.

        Parameters:
            message (str): The exception message to be logged.
        """
        pass
