from django.conf import settings
from django.db import models

from core.db import SoftDeleteModel

from modules.tenancy.tenants.models import Tenant


class TenantMembership(SoftDeleteModel):
    """
    User belongs to a tenant.
    One user can belong to multiple tenants.
    """

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="memberships",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tenant_memberships",
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "tenant_memberships"

        unique_together = (
            "tenant",
            "user",
        )

    def __str__(self):
        return f"{self.user.email} - {self.tenant.name}"