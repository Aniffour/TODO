from django import forms 
from django.contrib.auth.models import User
from .models import Task

class UserCreateForm(forms.ModelForm): 
    class Meta: 
        model = User
        fields = ['username' , 'email' , 'password']

class TaskFrom(forms.ModelForm): 
    class Meta : 
        model = Task 
        fields = ['task' , 'finish_at']
        widgets = {
            'finish_at': forms.DateTimeInput(attrs={'type':'date'}),
        }