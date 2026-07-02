from django.urls import include, path

urlpatterns = [
    path("tenants/", include("modules.tenancy.tenants.urls")),
]