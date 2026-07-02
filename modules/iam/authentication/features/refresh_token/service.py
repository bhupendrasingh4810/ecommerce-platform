from rest_framework_simplejwt.tokens import RefreshToken


class RefreshTokenService:

    @staticmethod
    def refresh(data):
        refresh = RefreshToken(data["refresh_token"])

        return {
            "access_token": str(refresh.access_token),
        }