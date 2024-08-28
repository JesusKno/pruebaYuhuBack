from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class task(models.Model):
    tasktitle = models.TextField(max_length=100)
    taskdescription = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
