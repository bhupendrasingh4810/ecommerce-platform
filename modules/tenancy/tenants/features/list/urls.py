from django.urls import path

from .api import ListAPIView

urlpatterns = [
    path(
        "list/",
        ListAPIView.as_view(),
        name="list-tenants",
    ),
]