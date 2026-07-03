from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.views import APIView

from core.responses.response import ApiResponse

from .service import DeleteService


class DeleteAPIView(APIView):

    @extend_schema(
        tags=["Tenants"],
        summary="Delete Tenant",
        responses={204: None},
    )
    def delete(self, request, tenant_id):
        DeleteService.delete(tenant_id)

        return ApiResponse.success(
            message="Tenant deleted successfully.",
            status=status.HTTP_204_NO_CONTENT,
        )