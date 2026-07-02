from django.db import models

from core.db import SoftDeleteModel

from modules.tenancy.tenants.constants import (
    DEFAULT_CURRENCY,
    DEFAULT_TIMEZONE,
)
from modules.tenancy.tenants.enums import TenantStatus

class Tenant(SoftDeleteModel):
    """
    Represents a marketplace (tenant) in the SaaS platform.
    """

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
    )

    primary_domain = models.CharField(
        max_length=255,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    logo = models.URLField(
        blank=True,
    )

    currency = models.CharField(
        max_length=3,
        default="USD",
    )

    timezone = models.CharField(
        max_length=100,
        default="UTC",
    )

    status = models.CharField(
        max_length=20,
        choices=TenantStatus.choices,
        default=TenantStatus.PENDING,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "tenant"

    def __str__(self):
        return self.name