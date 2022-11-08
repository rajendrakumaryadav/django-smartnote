from django.contrib import admin

from . import models
from . import models


# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at')


admin.site.register(models.Note, NotesAdmin)
