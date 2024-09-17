from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    PRIORITY_CHOICES=[
        (1,'Low'),
        (2,'Medium'),
        (3,'High'),
    ]
    priority=forms.ChoiceField(choices=PRIORITY_CHOICES,required=True,label='Priority')
    class Meta:
        model=Task
        fields=['title','description','completed','priority']
        
