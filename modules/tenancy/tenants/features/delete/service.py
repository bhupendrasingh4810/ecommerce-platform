from modules.tenancy.tenants.repositories.repository import Repository

from .validator import DeleteValidator


class DeleteService:

    @staticmethod
    def delete(tenant_id):
        tenant = DeleteValidator.validate(tenant_id)

        Repository.delete(tenant)