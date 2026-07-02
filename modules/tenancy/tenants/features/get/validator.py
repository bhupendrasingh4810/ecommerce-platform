from rest_framework.exceptions import ValidationError

from modules.tenant.models import Tenant


class CreateTenantValidator:

    @staticmethod
    def validate(data):
        if Tenant.objects.filter(slug=data["slug"]).exists():
            raise ValidationError(
                {
                    "slug": [
                        "Tenant slug already exists."
                    ]
                }
            )

        if Tenant.objects.filter(
            primary_domain=data["primary_domain"]
        ).exists():
            raise ValidationError(
                {
                    "primary_domain": [
                        "Primary domain already exists."
                    ]
                }
            )