from modules.tenancy.tenants.models import Tenant

# This repository class provides methods to interact with the Tenant model, including creating, retrieving, checking existence, listing, and saving tenants.
# Why use a repository class? The repository pattern is used to abstract the data access layer, providing a clean API for the rest of the application to interact with the data source. It helps in maintaining separation of concerns, making the code more maintainable and testable.

class Repository:
    @staticmethod
    def create(**kwargs) -> Tenant:
        return Tenant.objects.create(**kwargs)

    @staticmethod
    def all():
        return Tenant.objects.filter(
            is_deleted=False,
        ).order_by("-created_at")


    @staticmethod
    def save(instance):
        instance.save()
        return instance

    @staticmethod
    def get(**filters) -> Tenant | None:
        filters["is_deleted"] = False
        return Tenant.objects.filter(**filters).first()

    @staticmethod
    def filter(**filters):
        filters["is_deleted"] = False
        return Tenant.objects.filter(**filters)

    @staticmethod
    def exists(**filters) -> bool:
        filters["is_deleted"] = False
        return Tenant.objects.filter(**filters).exists()

    @staticmethod
    def update(instance: Tenant, **kwargs) -> Tenant:
        for key, value in kwargs.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    @staticmethod
    def delete(instance: Tenant) -> Tenant:
        instance.is_deleted = True
        instance.save(update_fields=["is_deleted"])
        return instance