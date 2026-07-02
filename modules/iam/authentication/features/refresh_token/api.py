from rest_framework.response import Response
from rest_framework.views import APIView

from .schemas import RefreshTokenRequestSerializer
from .service import RefreshTokenService


class RefreshTokenAPIView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = RefreshTokenRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            RefreshTokenService.refresh(serializer.validated_data)
        )