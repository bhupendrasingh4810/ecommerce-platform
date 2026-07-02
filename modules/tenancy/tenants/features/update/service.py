from modules.tenancy.tenants.models import Tenant

from .validator import CreateTenantValidator


class CreateTenantService:

    @staticmethod
    def create_tenant(data):
        CreateTenantValidator.validate(data)

        return Tenant.objects.create(
            **data
        )