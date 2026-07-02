from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return Response(
            {
                "success": False,
                "message": "Internal Server Error",
                "errors": None,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    message = "Request failed."

    if isinstance(exc, ValidationError):
        message = "Validation failed."

    return Response(
        {
            "success": False,
            "message": message,
            "errors": response.data,
        },
        status=response.status_code,
    )