from rest_framework.views import APIView

from core.responses.response import ApiResponse

from .schemas import LogoutRequestSerializer
from .service import LogoutService


class LogoutAPIView(APIView):

    def post(self, request):
        serializer = LogoutRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        LogoutService.logout(serializer.validated_data)

        return ApiResponse.success(
            message="Logged out successfully."
        )