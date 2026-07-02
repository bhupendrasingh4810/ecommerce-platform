from rest_framework import status
from rest_framework.views import APIView
from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)

from core.responses.response import ApiResponse
from .schemas import RegisterRequestSerializer
from .service import RegisterService


class RegisterAPIView(APIView):

    permission_classes = []
    
    @extend_schema(
        tags=["Authentication"],
        summary="Register",
        description="Register a new user.",
        request=RegisterRequestSerializer,
        responses={
            201: OpenApiResponse(
                description="User registered successfully.",
            ),
        },
        examples=[
            OpenApiExample(
                "Example",
                value={
                    "email": "bhupendra@test.com",
                    "password": "Password@123",
                    "first_name": "Bhupendra",
                    "last_name": "Singh"
                }
            )
        ]
    )
    def post(self, request):
        serializer = RegisterRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = RegisterService.register(
            serializer.validated_data
        )

        return ApiResponse.success(
            data={
                "id": str(user.id),
                "email": user.email,
            },
            message="User registered successfully.",
            status=status.HTTP_201_CREATED,
        )