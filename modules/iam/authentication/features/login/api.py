from rest_framework.views import APIView
from drf_spectacular.utils import (
    extend_schema, 
    OpenApiResponse,
    OpenApiExample,
)

from core.responses.response import ApiResponse
from .schemas import LoginRequestSerializer
from .service import LoginService


class LoginAPIView(APIView):

    permission_classes = []

    @extend_schema(
        tags=["Authentication"],
        summary="Login",
        description="Authenticate a user and return access and refresh tokens.",
        request=LoginRequestSerializer,
        responses={
            200: OpenApiResponse(
                description="Login successful.",
            ),
        },
        examples=[
            OpenApiExample(
                "Example",
                value={
                    "email": "bhupendra@test.com",
                    "password": "Password@123"
                }
            )
        ]
    )

    def post(self, request):
        serializer = LoginRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = LoginService.login(serializer.validated_data)

        return ApiResponse.success(
            data=result,
            message="Login successful.",
        )