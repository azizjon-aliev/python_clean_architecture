import logging
from src.interactor.interfaces.logger.logger import LoggerInterface


class LoggerDefault(LoggerInterface):
    def __init__(self):
        logging.basicConfig(
            filename='app.log',
            filemode='a',
            datefmt='%Y-%m-%d %H:%M:%S',
            format='%(asctime)-s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

    def log_debug(self, message: str) -> None:
        logging.debug(message)

    def log_info(self, message: str) -> None:
        logging.info(message)

    def log_warning(self, message: str) -> None:
        logging.warning(message)

    def log_error(self, message: str) -> None:
        logging.error(message)

    def log_critical(self, message: str) -> None:
        logging.critical(message)

    def log_exception(self, message: str) -> None:
        logging.exception(message)