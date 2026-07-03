from django.urls import path

from .api import UpdateAPIView

urlpatterns = [
    path(
        "<uuid:tenant_id>/update/",
        UpdateAPIView.as_view(),
        name="update-tenant",
    ),
]