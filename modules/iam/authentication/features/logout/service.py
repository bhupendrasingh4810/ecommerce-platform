from rest_framework_simplejwt.tokens import RefreshToken


class LogoutService:

    @staticmethod
    def logout(data):
        token = RefreshToken(data["refresh_token"])
        token.blacklist()