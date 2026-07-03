from drf_spectacular.utils import extend_schema

from rest_framework.views import APIView

from core.responses.response import ApiResponse

from .schemas import (
    UpdateRequestSerializer,
    UpdateResponseSerializer,
)
from .service import UpdateService


class UpdateAPIView(APIView):

    @extend_schema(
        tags=["Tenants"],
        summary="Update Tenant",
        request=UpdateRequestSerializer,
        responses=UpdateResponseSerializer,
    )
    def put(self, request, tenant_id):
        serializer = UpdateRequestSerializer(
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)

        tenant = UpdateService.update(
            tenant_id,
            serializer.validated_data,
        )

        response = UpdateResponseSerializer(
            tenant,
        )

        return ApiResponse.success(
            data=response.data,
            message="Tenant updated successfully.",
        )