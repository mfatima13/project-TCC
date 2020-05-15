from rest_framework import serializers

from .models import Task, ToDo
from ..team.models import Team

class ToDoSerializer(serializers.ModelSerializer):
    group = Team.serializers.StringRelatedField(many=True)

    class Meta:
        model = ToDo
        fields = ['id', 'name', 'group', 'initDate', 'endDate']

class TaskSerializer(serializers.ModelSerializer):
    toDo = ToDoSerializer(many=True)
    
    class Meta:
        model = Task
        fields = [
            'id', 
            'name', 
            'description', 
            'completed', 
            'priority', 
            'toDo', 
            'order'
        ]
