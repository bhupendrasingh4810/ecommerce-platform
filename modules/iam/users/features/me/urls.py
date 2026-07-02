from django.urls import path

from .api import MeAPIView

urlpatterns = [
    path('', MeAPIView.as_view(), name='me'),
]