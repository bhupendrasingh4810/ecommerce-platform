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
    path(
        "",
        include("modules.tenancy.tenants.features.get.urls"),
    ),
    path(
        "",
        include("modules.tenancy.tenants.features.update.urls"),
    ),
    path(
        "",
        include("modules.tenancy.tenants.features.delete.urls"),
    ),
]