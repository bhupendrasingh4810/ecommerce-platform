from django.urls import include, path

urlpatterns = [
    path(
        "me/",
        include("modules.iam.users.features.me.urls"),
    ),
]