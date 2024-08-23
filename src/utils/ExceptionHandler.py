# Imports
import traceback

# Consts
from .consts import LEVEL_ERROR

# Logger
from .Logger import Logger


class ExceptionHandler():

    @classmethod
    def log_exception(cls, ex: Exception) -> None:
        Logger.add_to_log(LEVEL_ERROR, str(ex))
        Logger.add_to_log(LEVEL_ERROR, traceback.format_exc())
