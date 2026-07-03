from django.urls import path

from .api import DeleteAPIView

urlpatterns = [
    path(
        "<uuid:tenant_id>/delete/",
        DeleteAPIView.as_view(),
        name="delete-tenant",
    ),
]