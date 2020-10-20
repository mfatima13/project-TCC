from django.contrib import admin

from .models import ToDo, Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'description',
        'priority',
        'completed',
        'order',
        'toDo',
    )
    ordering = ['order']


class ToDoAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'group',
        'order',
        'initDate',
        'endDate',
    )
    ordering = ['order']


admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Task, TaskAdmin)
