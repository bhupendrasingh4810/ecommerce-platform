from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample
)

from core.responses.response import ApiResponse
from .schemas import TenantSerializer
from .service import ListService


class ListAPIView(APIView):

    @extend_schema(
        tags=["Tenants"],
        summary="List Tenants",
        responses=TenantSerializer(many=True),
        examples=[
        OpenApiExample(
            name="Create Tenant",
            value={
                "name": "EcoMall",
                "slug": "ecomall",
                "primary_domain": "ecomall.local",
            },
            request_only=True,
        )
    ]
    )

    def get(self, request):

        tenants = ListService.list()

        serializer = TenantSerializer(
            tenants,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data,
            message="Tenants fetched successfully.",
        )