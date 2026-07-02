from rest_framework.exceptions import ValidationError


class ChangePasswordService:

    @staticmethod
    def change_password(user, data):
        if not user.check_password(data["old_password"]):
            raise ValidationError(
                {
                    "old_password": [
                        "Old password is incorrect."
                    ]
                }
            )

        user.set_password(data["new_password"])
        user.save()

        return user