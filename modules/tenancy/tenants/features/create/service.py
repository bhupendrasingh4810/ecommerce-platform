from modules.tenancy.tenants.repositories.repository import Repository


class CreateService:
    @staticmethod
    def create(data):
        tenant = Repository.create(
            name=data["name"],
            slug=data["slug"],
            primary_domain=data["primary_domain"],
            description=data.get("description", ""),
            logo=data.get("logo", ""),
        )

        return tenant