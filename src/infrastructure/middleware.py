from django.http import JsonResponse
import logging

from src.application.common.exceptions.authentication_exceptions import EntityInvalidCredentialsException
from src.application.common.exceptions.entity_already_exist_exception import EntityAlreadyExistException

logger = logging.getLogger(__name__)

class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        logger.error(f'Exception occurred: {exception}', exc_info=True)

        status_code = 400

        if isinstance(exception, EntityInvalidCredentialsException):
            status_code = 401

        if isinstance(exception, EntityAlreadyExistException):
            status_code = 409

        response_data = {
            "error": str(exception),
        }
        return JsonResponse(response_data, status=status_code)
