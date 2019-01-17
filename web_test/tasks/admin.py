from django.contrib import admin
from tasks.models import Task, TaskState

class TasksAdmin(admin.ModelAdmin):
    pass


class TaskStateAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TasksAdmin)
admin.site.register(TaskState, TaskStateAdmin)