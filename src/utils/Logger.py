# Imports
import logging
import os
import traceback

# Consts
from .consts import DF_MYSQL, HF_FULL, LEVEL_ERROR, LEVEL_INFO, UTF8


class Logger():

    @classmethod
    def add_to_log(cls, level: str, message: str) -> None:
        try:
            logger = cls.__set_logger(cls)

            if level == 'critical':
                logger.critical(message)
            elif level == 'debug':
                logger.debug(message)
            elif level == LEVEL_ERROR:
                logger.error(message)
            elif level == LEVEL_INFO:
                logger.info(message)
            elif level == 'warn':
                logger.warn(message)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)

    def __set_logger(self) -> logging.Logger:
        log_directory = 'src/utils/logs'
        log_filename = 'app.log'

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        log_path = os.path.join(log_directory, log_filename)
        file_handler = logging.FileHandler(log_path, encoding=UTF8)
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', f"{DF_MYSQL} {HF_FULL}")
        file_handler.setFormatter(formatter)

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(file_handler)

        return logger
