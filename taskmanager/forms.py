from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import task

class FormNewTask(ModelForm):
    class Meta: 
        model= task
        fields = ['tasktitle', 'taskdescription']
        
class Usercreationwithemail(UserCreationForm):
    email = forms.EmailField(required = True, help_text = 'Debe introducir un email valido')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def duplicate_email(self):
        email = self.cleaned_data.get(email)
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya esta registrado')
        return email