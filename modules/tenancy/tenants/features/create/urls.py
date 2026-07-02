from django.urls import path

from .api import CreateAPIView

urlpatterns = [
    path(
        "create/",
        CreateAPIView.as_view(),
        name="create-tenant",
    ),
]