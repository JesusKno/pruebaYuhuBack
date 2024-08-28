from rest_framework.serializers import ModelSerializer
from .models import task

class taskSerializer(ModelSerializer):
    class Meta:
        model = task
        fields = ['id', 'tasktitle', 'taskdescription', 'user']