from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login", views.LoginInterfaceView.as_view(), name="login"),
    path("logout", views.LogoutInterfaceView.as_view(), name="logout"),
    path("notes", views.ListNotes.as_view(), name="list_notes"),
    path("notes/new", views.NoteCreateView.as_view(), name="new_note"),
    path("notes/<int:pk>/edit", views.NoteUpdateView.as_view(), name="edit_note"),
    path("notes/<int:pk>/delete", views.NoteDeleteView.as_view(), name="delete_note"),
    path("notes/<int:pk>", views.NoteDetail.as_view(), name="note_detail"),
    path("authorized", views.AuthorizedView.as_view(), name="authorized.zone"),
]
