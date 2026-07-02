from django.urls import path

from .api import RefreshTokenAPIView

urlpatterns = [
    path("", RefreshTokenAPIView.as_view(), name="refresh-token"),
]