from rest_framework.views import APIView

from core.responses.response import ApiResponse

from .schemas import ChangePasswordRequestSerializer
from .service import ChangePasswordService


class ChangePasswordAPIView(APIView):

    def post(self, request):
        serializer = ChangePasswordRequestSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        ChangePasswordService.change_password(
            request.user,
            serializer.validated_data,
        )

        return ApiResponse.success(
            message="Password changed successfully."
        )