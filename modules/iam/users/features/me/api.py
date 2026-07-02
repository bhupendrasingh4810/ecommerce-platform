from rest_framework.views import APIView

from core.responses.response import ApiResponse

from .service import MeService


class MeAPIView(APIView):

    def get(self, request):
        return ApiResponse.success(
            data=MeService.get_profile(request.user)
        )