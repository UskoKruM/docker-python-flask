# Imports
from flask import wrappers
from werkzeug import exceptions

# Consts
from src.utils.consts import LEVEL_INFO

# Exception Handler
from src.utils.ExceptionHandler import ExceptionHandler

# Logger
from src.utils.Logger import Logger

# Response Methods
from src.routes.utils.ResponseMethods import ResponseMethods


class ErrorMiddleware():

    @classmethod
    def handle_error_401(cls, ex: exceptions.Unauthorized) -> wrappers.Response:
        Logger.add_to_log(LEVEL_INFO, ex)
        return ResponseMethods.get_response_with_status_code(401)

    @classmethod
    def handle_error_500(cls, ex: Exception) -> wrappers.Response:
        ExceptionHandler.log_exception(ex)
        return ResponseMethods.get_response_with_status_code(500)
