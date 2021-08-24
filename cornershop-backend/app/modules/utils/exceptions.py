from rest_framework.views import exception_handler
from ..utils.response import ResponseDetail


def custom_exception_handler(exc, context):
    """
        Call REST framework's default exception handler first to get the standard error response.

        :param exc:
        :param context:
        :return: response
    """
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        if response.status_code == 404:
            response.data = ResponseDetail().not_found_detail()
        elif response.status_code == 401:
            response.data = ResponseDetail().errors_detail(code=401, message="Permission Denied", error="Invalid Token")
    return response


class NotFound(Exception):
    pass
