import sys

from loguru import logger

from src.interactor.interfaces.logger.logger import LoggerInterface


class LoggerDefault(LoggerInterface):
    """
    A default logger implementation using Loguru.

    This logger writes log messages to both the console and a file named 'app.log'.
    It supports various log levels as defined by the LoggerInterface.
    """

    def __init__(self):
        # Remove the default Loguru handler to prevent duplicate logs
        logger.remove()

        # Configure logging to a file with rotation and retention policies
        logger.add(
            "app.log",
            rotation="10 MB",  # Rotate after the log file reaches 10 MB
            retention="10 days",  # Keep logs for 10 days
            level="DEBUG",  # Capture all log levels DEBUG and above
            format="{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}",
            enqueue=True,  # Thread-safe logging
        )

        # Configure logging to the console with colored output
        logger.add(
            sys.stderr,
            level="DEBUG",  # Capture all log levels DEBUG and above
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> - "
            "<level>{level}</level> - <level>{message}</level>",
            colorize=True,  # Enable colored logs
        )

    def log_debug(self, message: str) -> None:
        """
        Log a message with DEBUG severity.
        """
        logger.debug(message)

    def log_info(self, message: str) -> None:
        """
        Log a message with INFO severity.
        """
        logger.info(message)

    def log_warning(self, message: str) -> None:
        """
        Log a message with WARNING severity.
        """
        logger.warning(message)

    def log_error(self, message: str) -> None:
        """
        Log a message with ERROR severity.
        """
        logger.error(message)

    def log_critical(self, message: str) -> None:
        """
        Log a message with CRITICAL severity.
        """
        logger.critical(message)

    def log_exception(self, message: str) -> None:
        """
        Log an exception message with ERROR severity, including traceback information.
        """
        logger.exception(message)
