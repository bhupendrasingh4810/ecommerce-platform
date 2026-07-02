from rest_framework.exceptions import ValidationError

from modules.tenancy.tenants.repositories.repository import Repository


class CreateValidator:
    @staticmethod
    def validate(data):
        if Repository.exists(slug=data["slug"]):
            raise ValidationError(
                {"slug": "Tenant slug already exists."}
            )

        if Repository.exists(
            primary_domain=data["primary_domain"]
        ):
            raise ValidationError(
                {
                    "primary_domain":
                    "Primary domain already exists."
                }
            )