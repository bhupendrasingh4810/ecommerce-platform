from django.urls import path

from .api import LogoutAPIView

urlpatterns = [
    path("", LogoutAPIView.as_view(), name="logout"),
]