from rest_framework.exceptions import NotFound

from modules.tenancy.tenants.repositories.repository import Repository


class GetValidator:

    @staticmethod
    def validate(tenant_id):
        tenant = Repository.get(id=tenant_id)

        if tenant is None:
            raise NotFound("Tenant not found.")

        return tenant