from django.contrib import admin
from tasks.models import Task

class TasksAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task, TasksAdmin)