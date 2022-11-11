from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from . import models
from .forms import NoteForm, SignupForm


# Create your views here.
class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = SignupForm
    success_url = '/notes'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/notes')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'


class LoginInterfaceView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    fields = "__all__"
    redirect_field_name = "redirect_to"
    success_url = "/notes"

    def get_success_url(self):
        return self.success_url


class HomeView(TemplateView):
    template_name = 'index.html'
    extra_context = {"now": datetime.now(), "title": "Home"}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'note/authorized.html'
    extra_context = {"title": "Authorized Zone"}
    login_url = '/admin'


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = models.Note
    form_class = NoteForm
    template_name = 'note/note-form.html'
    success_url = '/notes'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Note
    success_url = '/notes'
    template_name = 'note/note_delete.html'


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Note
    form_class = NoteForm
    template_name = 'note/note-form.html'
    success_url = '/notes'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return redirect('/notes')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class ListNotes(LoginRequiredMixin, ListView):
    model = models.Note
    template_name = 'note/note_lists.html'
    context_object_name = 'notes'
    extra_context = {"title": "List of Notes"}

    def get_queryset(self):
        # select all notes of login user
        return self.request.user.notes.all()


class NoteDetail(LoginRequiredMixin, DetailView):
    model = models.Note
    template_name = 'note/note_detail.html'
    context_object_name = 'note'
    extra_context = {"title": "Note Detail"}

    def get_queryset(self):
        # if self.request.user == self.get_object().user:
        return models.Note.objects.filter(user=self.request.user)
