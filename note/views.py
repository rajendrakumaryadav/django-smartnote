from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from . import models
from .forms import NoteForm


# Create your views here.

# TODO: Add User Authentication

class HomeView(TemplateView):
    template_name = 'note/index.html'
    extra_context = {"now": datetime.now(), "title": "Home"}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'note/authorized.html'
    extra_context = {"title": "Authorized Zone"}
    login_url = '/admin'


class NoteCreateView(CreateView):
    model = models.Note
    form_class = NoteForm
    template_name = 'note/note-form.html'
    success_url = '/notes'


class NoteDeleteView(DeleteView):
    model = models.Note
    success_url = '/notes'
    template_name = 'note/note_delete.html'


class NoteUpdateView(UpdateView):
    model = models.Note
    form_class = NoteForm
    template_name = 'note/note-form.html'
    success_url = '/notes'


class ListNotes(ListView):
    model = models.Note
    template_name = 'note/note_lists.html'
    context_object_name = 'notes'
    extra_context = {"title": "List of Notes"}


class NoteDetail(DetailView):
    model = models.Note
    template_name = 'note/note_detail.html'
    context_object_name = 'note'
    extra_context = {"title": "Note Detail"}
