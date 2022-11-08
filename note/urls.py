from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list_notes", views.list_notes, name="list_notes"),
    path("authorized", views.authorized, name="authorized.zone"),
]
