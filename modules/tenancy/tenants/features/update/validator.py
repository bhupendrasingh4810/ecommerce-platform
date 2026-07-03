from rest_framework.exceptions import NotFound, ValidationError

from modules.tenancy.tenants.repositories.repository import Repository


class UpdateValidator:

    @staticmethod
    def validate(tenant_id, data):
        tenant = Repository.get(id=tenant_id)

        if tenant is None:
            raise NotFound("Tenant not found.")

        slug = Repository.get(slug=data["slug"])

        if slug and slug.id != tenant.id:
            raise ValidationError(
                {"slug": ["Slug already exists."]}
            )

        domain = Repository.get(
            primary_domain=data["primary_domain"]
        )

        if domain and domain.id != tenant.id:
            raise ValidationError(
                {"primary_domain": ["Primary domain already exists."]}
            )

        return tenant