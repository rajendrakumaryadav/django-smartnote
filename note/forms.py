from django import forms

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
