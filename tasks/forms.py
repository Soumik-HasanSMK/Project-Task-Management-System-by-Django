from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'deadline']  # Add 'deadline' here
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker
        }
