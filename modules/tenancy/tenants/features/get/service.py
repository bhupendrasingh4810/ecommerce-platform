from .validator import GetValidator


class GetService:

    @staticmethod
    def get(tenant_id):
        return GetValidator.validate(tenant_id)