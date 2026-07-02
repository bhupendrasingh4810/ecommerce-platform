from rest_framework.exceptions import ValidationError

from modules.iam.users.models import User

# Validator for user registration
# This class is used to validate the data sent in the registration request. It checks if the email is already registered in the system. If the email is already registered, it raises a ValidationError.

class RegisterValidator:

    @staticmethod
    def validate(email: str):
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                {"email": "Email already registered."}
            )