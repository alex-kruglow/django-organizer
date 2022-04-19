from django.contrib import admin

from .models import toDo


@admin.register(toDo)
class toDoAdmin(admin.ModelAdmin):
    list_display = ('username', 'title', 'link')
    list_filter = ('username', 'title', 'link')
    search_field = ('title')
