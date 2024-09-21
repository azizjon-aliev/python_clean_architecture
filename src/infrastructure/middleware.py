import logging
from http import HTTPStatus

from django.http import JsonResponse
from src.application.common.exceptions.authentication_exceptions import (
    EntityInvalidCredentialsException,
)
from src.application.common.exceptions.entity_already_exist_exception import (
    EntityAlreadyExistException,
)

logger = logging.getLogger(__name__)


class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception) -> JsonResponse:
        logger.error(f"Exception occurred: {exception}", exc_info=True)

        status_code = HTTPStatus.BAD_REQUEST

        if isinstance(exception, EntityInvalidCredentialsException):
            status_code = HTTPStatus.UNAUTHORIZED

        if isinstance(exception, EntityAlreadyExistException):
            status_code = HTTPStatus.CONFLICT

        response_data = {
            "error": str(exception),
        }
        return JsonResponse(response_data, status=status_code)
