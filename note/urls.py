from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("notes", views.ListNotes.as_view(), name="list_notes"),
    path("note/<int:pk>", views.NoteDetail.as_view(), name="note_detail"),
    path("authorized", views.AuthorizedView.as_view(), name="authorized.zone"),

]
