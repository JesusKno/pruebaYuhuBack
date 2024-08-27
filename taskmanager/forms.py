from django.forms import ModelForm
from .models import task

class FormNewTask(ModelForm):
    class Meta: 
        model= task
        fields = ['tasktitle', 'taskdescription']