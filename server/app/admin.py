from django.contrib import admin
from .models import *

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'image', 'created_by']
    search_fields = ['title', 'created_by', 'id']
    readonly_fields = ['created_at', 'created_by']
    list_filter = ['created_at']


admin.site.register(Note, NoteAdmin)