from django.db import models

from team.models import Team, Membership

from .managers import TaskManager

# Create your models here.

class ToDo(models.Model):
    name = models.CharField(max_length=300)
    group = models.ForeignKey(
        Team,
        related_name='toDo',
        on_delete=models.CASCADE,
    )
    initDate = models.DateField(auto_now_add=True)
    endDate = models.DateField()

    def __str__(self):
        return self.name    

class Task(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=800, blank=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    priority = models.CharField(max_length=10)
    toDo = models.ForeignKey(
        ToDo,
        related_name='tasks',
        on_delete=models.CASCADE,
    )
    order = models.IntegerField(null=True, blank=True)

    objects = TaskManager()

    class Meta:
        index_together = ('toDo', 'order')

    def __str__(self):
        return self.name
