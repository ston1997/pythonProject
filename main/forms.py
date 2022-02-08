from .models import task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'введите описание'
        })
        }