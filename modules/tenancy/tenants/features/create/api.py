from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample,
    OpenApiResponse,
)

from .schemas import (
    CreateRequestSerializer,
    CreateResponseSerializer,
)
from .service import CreateService
from .validator import CreateValidator


class CreateAPIView(APIView):
    @extend_schema(
        tags=["Tenants"],
        summary="Create Tenant",
        description="Creates a new marketplace tenant.",
        request=CreateRequestSerializer,
        responses={
            201: OpenApiResponse(
                description="Tenant created successfully."
            ),
            400: OpenApiResponse(
                description="Validation error."
            ),
        },
        examples=[
            OpenApiExample(
                "Example",
                value={
                    "name": "EcoMall",
                    "slug": "ecomall",
                    "primary_domain": "ecomall.local",
                    "description": "Eco marketplace",
                    "currency": "USD",
                    "timezone": "UTC",
                },
                request_only=True,
            )
        ],
    )

    def post(self, request):
        serializer = CreateRequestSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        CreateValidator.validate(
            serializer.validated_data
        )

        tenant = CreateService.create(
            serializer.validated_data
        )

        response = CreateResponseSerializer(
            tenant
        )

        return Response(
            response.data,
            status=status.HTTP_201_CREATED,
        )