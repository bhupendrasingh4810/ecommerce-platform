from modules.tenancy.tenants.repositories.repository import Repository

from .validator import UpdateValidator


class UpdateService:

    @staticmethod
    def update(tenant_id, data):
        tenant = UpdateValidator.validate(
            tenant_id,
            data,
        )

        return Repository.update(
            tenant,
            **data,
        )