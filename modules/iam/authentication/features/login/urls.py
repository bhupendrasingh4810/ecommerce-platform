from django.urls import path

from .api import LoginAPIView

urlpatterns = [
    path("", LoginAPIView.as_view(), name="login"),
]