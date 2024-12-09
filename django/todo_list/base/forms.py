from django import forms
from django.forms import ModelForm

from .models import Task


class TaskForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Add a New Task'}))
    description = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Description'}))

    class Meta:
        model = Task
        fields = '__all__'
