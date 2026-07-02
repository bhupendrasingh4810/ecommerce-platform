from django.urls import include, path

urlpatterns = [
    path(
        "login/",
        include("modules.iam.authentication.features.login.urls"),
    ),
    path(
        "register/",
        include("modules.iam.authentication.features.register.urls"),
    ),
    path(
        "refresh/",
        include("modules.iam.authentication.features.refresh_token.urls"),
    ),
    path(
        "logout/",
        include("modules.iam.authentication.features.logout.urls"),
    ),
]