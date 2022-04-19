from django.forms import ModelForm
from .models import toDo


class toDoForm(ModelForm):
    class Meta:
        model = toDo
        fields = ['title', 'description']
