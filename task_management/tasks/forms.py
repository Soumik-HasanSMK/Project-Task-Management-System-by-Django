from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save'))

        # Add custom date picker widget
        self.fields['due_date'].widget = forms.DateInput(attrs={'type': 'date'})
