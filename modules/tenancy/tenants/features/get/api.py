from drf_spectacular.utils import extend_schema

from rest_framework.views import APIView

from core.responses.response import ApiResponse

from .schemas import GetResponseSerializer
from .service import GetService


class GetAPIView(APIView):

    @extend_schema(
        tags=["Tenants"],
        summary="Get Tenant",
        responses=GetResponseSerializer,
    )
    def get(self, request, tenant_id):
        tenant = GetService.get(tenant_id)

        serializer = GetResponseSerializer(tenant)

        return ApiResponse.success(
            data=serializer.data,
            message="Tenant fetched successfully.",
        )