from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("services/", include("services.urls")),
    path("subsidiaries/", include("subsidiaries.urls")),
    path("contact/", include("contact.urls")),
]
