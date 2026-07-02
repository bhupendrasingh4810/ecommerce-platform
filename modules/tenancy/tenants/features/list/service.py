from modules.tenancy.tenants.repositories.repository import Repository


class ListService:

    @staticmethod
    def list():
        return Repository.all()