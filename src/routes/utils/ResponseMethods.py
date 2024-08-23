# Imports
from flask import jsonify, wrappers


class ResponseMethods():

    @classmethod
    def get_response_successful(cls, body: dict = None) -> wrappers.Response:
        response = cls.__get_json_dict(cls, True, 'SUCCESS')

        if body != None:
            response.update(body)

        return jsonify(response)

    @classmethod
    def get_response_successful_notfound(cls) -> wrappers.Response:
        return jsonify(cls.__get_json_dict(cls, True, 'NOTFOUND'))

    @classmethod
    def get_response_with_status_code(cls, status_code: int) -> wrappers.Response:
        message = cls.__get_http_response_codes(cls)[status_code]
        json_object = cls.__get_json_dict(cls, False, message)

        response = jsonify(json_object)
        response.status_code = status_code

        return response

    def __get_json_dict(self, is_success: bool, message: str) -> dict:
        return {'success': is_success, 'message': message}

    def __get_http_response_codes(self) -> dict:
        return {
            200: "OK",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            422: "Unprocessable Content",
            500: "Internal Server Error"
        }
