from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Note


# TODO: Add User Authentication Form

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content')
        labels = {
            'title': "Note's Title: ",
            'content': "Note's Content: ",
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb-3'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'Django' not in title:
            raise forms.ValidationError('Title cannot be created without Django')
        return title


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        labels = {
            'username': "Username: ",
            'email': "Email: ",
            'password1': "Password: ",
            'password2': "Confirm Password: ",
            'first_name': "First Name: ",
            'last_name': "Last Name: ",
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email
