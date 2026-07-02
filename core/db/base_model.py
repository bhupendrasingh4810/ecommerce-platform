import uuid

from django.db import models


class BaseModel(models.Model):
    """
    Base model for all entities.
    Provides UUID primary key.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True # This model will not be used to create any database table. It is only used for inheritance purposes.