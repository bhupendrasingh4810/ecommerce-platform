from django.urls import path

from .api import ChangePasswordAPIView

urlpatterns = [
    path(
        "",
        ChangePasswordAPIView.as_view(),
        name="change-password",
    ),
]