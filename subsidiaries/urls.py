from django.urls import path

from . import views

app_name = "subsidiaries"

urlpatterns = [
    path("", views.list_view, name="list"),
    path("<slug:slug>/", views.detail, name="detail"),
]
