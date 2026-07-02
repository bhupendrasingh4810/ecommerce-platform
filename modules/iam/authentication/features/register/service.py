from modules.iam.users.models import User

from .validator import RegisterValidator

class RegisterService:

    @staticmethod
    def register(data):
        RegisterValidator.validate(data["email"])
        
        return User.objects.create_user(
            email=data["email"],
            password=data["password"],
            first_name=data["first_name"],
            last_name=data["last_name"],
        )