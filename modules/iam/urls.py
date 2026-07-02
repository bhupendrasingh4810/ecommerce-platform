from django.urls import path, include

urlpatterns = [
    path('auth/', include('modules.iam.authentication.urls')),
    path('users/', include('modules.iam.users.urls')),
]