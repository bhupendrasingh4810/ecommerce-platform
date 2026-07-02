from django.urls import path

from .api import RegisterAPIView

urlpatterns = [
    path(
        "",
        RegisterAPIView.as_view(),
        name="register",
    ),
]