from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:category_slug>/", views.category_detail, name="category_detail"),
    path(
        "<slug:category_slug>/<slug:service_slug>/",
        views.service_detail,
        name="service_detail",
    ),
]
