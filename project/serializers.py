from rest_framework import serializers

from .models import Task, ToDo
from team.models import Team
from team.serializers import TeamSerializer

class TaskSerializer(serializers.ModelSerializer):
    #toDo = ToDoSerializer()
    
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
    def create(self, validated_data):
        todo = validated_data.pop('toDo')
        task = Task.objects.create(toDo=todo, **validated_data)
        return task

class ToDoSerializer(serializers.ModelSerializer):
    #group = serializers.StringRelatedField(many=True, )
    #group = serializers.
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = ToDo
        fields = ['id', 'name', 'group', 'initDate', 'endDate', 'tasks']