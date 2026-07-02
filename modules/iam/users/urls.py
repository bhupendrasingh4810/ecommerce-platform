from django.urls import include, path

urlpatterns = [
    path('me/', include('modules.iam.users.features.me.urls')),
    path(
        "change-password/",
        include("modules.iam.users.features.change_password.urls"),
    ),
]