from django.contrib import admin

from .models import ToDo, Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'priority', 'completed', 'order', 'toDo', )
    ordering = ['order']

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'group', 'initDate', 'endDate', )
    ordering = ['pk']

admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Task, TaskAdmin)