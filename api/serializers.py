from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'username',
            'task_name',
            'task_tel',
            'ice_type',
            'quantity',
            'price',
            'status',
            'time'
            )