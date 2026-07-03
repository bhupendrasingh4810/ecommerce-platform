from django.urls import path

from .api import GetAPIView

urlpatterns = [
    path(
        "<uuid:tenant_id>/",
        GetAPIView.as_view(),
        name="get-tenant",
    ),
]