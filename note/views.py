from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from . import models


# Create your views here.

def home(request):
    data = {
        'now': datetime.now(),
        'title': 'Home Page'
    }
    return render(request, 'note/index.html', data)


@login_required(login_url='/admin')
def authorized(request):
    data: dict = {
        "title": "Restricted Area",
    }
    """
    This view is only accessible to logged-in users
    :param request:
    :return:
    """
    return render(request, 'note/authorized.html', data)


def list_notes(request):
    data = {
        'title': 'List of Notes',
        'notes': models.Note.objects.all()
    }
    return render(request, 'note/notelists.html', data)
