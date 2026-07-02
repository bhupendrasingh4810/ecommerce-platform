from django.urls import include, path

urlpatterns = [
    path(
        "",
        include("modules.tenancy.tenants.features.create.urls"),
    ),
    path(
        "",
        include("modules.tenancy.tenants.features.list.urls"),
    ),
]